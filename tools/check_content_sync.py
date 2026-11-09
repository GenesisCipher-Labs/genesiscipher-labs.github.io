#!/usr/bin/env python3
"""Check the website's current content across all six sibling repositories.

--sync copies only explicitly owned mirrors, never app code or historical archives. A repository
mirror (`repositoryMirrors`) is a whole checkout kept identical to its source: every tracked file
byte-for-byte, and no tracked file the source lacks.
"""
import argparse
import ast
import json
from pathlib import Path
import shutil
import subprocess
import sys

SITE = Path(__file__).resolve().parents[1]
ROOT = SITE.parent


def tracked_files(repo):
    """The repository's tracked paths, or None when it is not a git checkout."""
    result = subprocess.run(['git', '-C', str(repo), 'ls-files', '-z'], capture_output=True)
    if result.returncode != 0:
        return None
    return {path for path in result.stdout.decode().split('\0') if path}


def check_repository_mirror(entry, sync, failures):
    source = ROOT / entry['source']
    target = ROOT / entry['target']
    source_files = tracked_files(source)
    target_files = tracked_files(target)
    if source_files is None or target_files is None:
        failures.append(f'Missing checkout: {source if source_files is None else target}')
        return
    for path in sorted(target_files - source_files):
        if sync:
            (target / path).unlink(missing_ok=True)
        else:
            failures.append(f'Extra in mirror: {entry["target"]}/{path}')
    for path in sorted(source_files):
        source_file = source / path
        target_file = target / path
        if sync:
            target_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source_file, target_file)
        if not target_file.is_file() or source_file.read_bytes() != target_file.read_bytes():
            failures.append(f'Drift: {entry["source"]}/{path} -> {entry["target"]}/{path}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sync', action='store_true', help='Update the declared mirrors from their owners')
    args = parser.parse_args()
    manifest = json.loads((SITE / 'content-sync.json').read_text())
    failures = []
    count = 0
    for entry in manifest['mirrors']:
        source = ROOT / entry['source']
        target = ROOT / entry['target']
        if not source.is_file():
            failures.append(f'Missing source: {source}')
            continue
        if not target.parent.is_dir():
            failures.append(f'Missing checkout/directory: {target.parent}')
            continue
        if args.sync:
            shutil.copyfile(source, target)
        if not target.is_file() or source.read_bytes() != target.read_bytes():
            failures.append(f'Drift: {entry["source"]} -> {entry["target"]}')
        count += 1
    repositories = manifest.get('repositoryMirrors', [])
    for entry in repositories:
        check_repository_mirror(entry, args.sync, failures)
    # Pin factual exceptions that previously disagreed with the public copy.
    ha = ROOT / 'genesiscipherlabs-HomeSafe-Android'
    gate = ha / 'app/src/main/java/com/genesiscipher/homesafe/model/GuardianLinkSession.kt'
    if 'const val IS_GUARDIAN_LINK_ENABLED = false' not in gate.read_text():
        failures.append('Android Guardian gate changed: review public privacy and tracking behavior together')
    for file in ['homesafe-android-privacy.md', 'homesafe-android-terms.md']:
        if 'Guardian Live-Link is disabled' not in (SITE / file).read_text():
            failures.append(f'{file}: must disclose disabled Guardian sharing')
    policy = (SITE / 'pact-android-privacy.md').read_text()
    if 'Device-to-device transfer behavior can vary' not in policy:
        failures.append('Pact Android transfer disclosure requires review against its manifest')
    availability_script = ROOT / 'genesiscipherlabs-Pact-iOS/Scripts/set-app-availability.py'
    tree = ast.parse(availability_script.read_text())
    excluded = next(ast.literal_eval(node.value) for node in tree.body
                    if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'EXCLUDED' for t in node.targets))
    if excluded != {'IND'}:
        failures.append('Availability script contradicts the India-only exclusion')
    for file in ['index.md', 'privacy.md', 'terms.md']:
        if 'except India' in (SITE / file).read_text():
            failures.append(f'{file}: public pages state availability in general terms only')
    if failures:
        print('\n'.join('FAIL: ' + item for item in failures), file=sys.stderr)
        return 1
    print(f'PASS: {count} content mirrors and {len(repositories)} repository mirror(s) across all six repositories; '
          'availability and platform disclosures agree')
    return 0


if __name__ == '__main__':
    sys.exit(main())
