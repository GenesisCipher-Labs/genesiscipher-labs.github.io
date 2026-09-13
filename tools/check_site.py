#!/usr/bin/env python3
"""Validate a Jekyll build and optionally compare each page with the live site."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import urllib.parse
import urllib.request

ORIGIN = 'https://genesiscipher-labs.github.io'
ROUTES = ['/', '/get/', '/track/', '/privacy/', '/terms/', '/privacy/android/',
          '/terms/android/', '/pact/', '/pact/support/', '/pact/privacy/',
          '/pact/android/privacy/', '/pact/terms/', '/404.html']


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.hidden = 0
        self.words = []
        self.links = []
        self.ids = set()
        self.h1s = 0
        self.description = False
        self.title = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('script', 'style'):
            self.hidden += 1
        if tag == 'h1':
            self.h1s += 1
        if tag == 'title':
            self.title = True
        if tag == 'meta' and a.get('name') == 'description' and a.get('content'):
            self.description = True
        if 'id' in a:
            self.ids.add(a['id'])
        if tag == 'a' and 'href' in a:
            self.links.append(a['href'])

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.hidden -= 1

    def handle_data(self, value):
        if not self.hidden:
            self.words.extend(value.split())


def output_path(build, route):
    path = build / route.lstrip('/')
    return path / 'index.html' if route.endswith('/') else path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', default='_site')
    parser.add_argument('--live', action='store_true')
    args = parser.parse_args()
    build = Path(args.build)
    failures = []
    pages = {}
    for route in ROUTES:
        path = output_path(build, route)
        if not path.is_file():
            failures.append('Missing route: ' + route)
            continue
        text = path.read_text()
        page = Page(text)
        pages[route] = page
        if page.h1s != 1 or not page.title:
            failures.append(f'{route}: expected one h1 and a title')
        if route != '/track/' and not page.description:
            failures.append(f'{route}: missing description')
        if '{{' in text or '{%' in text:
            failures.append(f'{route}: unrendered Liquid')
        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S):
            data = json.loads(block)
            for node in data.get('@graph', []):
                if node.get('@type') == 'FAQPage':
                    visible = ' '.join(page.words)
                    for item in node['mainEntity']:
                        if item['name'] not in visible or item['acceptedAnswer']['text'] not in visible:
                            failures.append(f'{route}: structured FAQ differs from visible content')
                if node.get('@type') == 'MobileApplication':
                    areas = {area['name'] for area in node['areaServed']}
                    if not {'Delhi NCR', 'Mumbai', 'Bengaluru', 'Pune', 'Hyderabad'} <= areas:
                        failures.append('HomeSafe structured coverage omits supported Indian cities')
    for route, page in pages.items():
        for href in page.links:
            url = urllib.parse.urlsplit(urllib.parse.urljoin(ORIGIN + route, href))
            if url.scheme not in ('http', 'https') or url.netloc != urllib.parse.urlsplit(ORIGIN).netloc:
                continue
            path = output_path(build, urllib.parse.unquote(url.path))
            if not path.is_file():
                failures.append(f'{route}: broken link {href}')
            elif url.fragment and urllib.parse.unquote(url.fragment) not in Page(path.read_text()).ids:
                failures.append(f'{route}: missing fragment {href}')
    for internal in ['RELEASE_AVAILABILITY.md', 'content-sync.json', 'tools', 'README.md', 'Gemfile']:
        if (build / internal).exists():
            failures.append('Internal file published: ' + internal)
    if args.live:
        def fetch(route):
            request = urllib.request.Request(ORIGIN + route, headers={'Cache-Control': 'no-cache'})
            with urllib.request.urlopen(request, timeout=30) as response:
                actual = Page(response.read().decode())
            expected = pages[route]
            return route, actual.words == expected.words and actual.links == expected.links
        with ThreadPoolExecutor(max_workers=5) as pool:
            for route, same in pool.map(fetch, pages):
                if not same:
                    failures.append('Live page differs from verified build: ' + route)
    if failures:
        print('\n'.join('FAIL: ' + failure for failure in failures), file=sys.stderr)
        return 1
    print(f'PASS: {len(pages)} routes, internal links, metadata, FAQ consistency and private-file exclusions' + ('; live content matches' if args.live else ''))
    return 0


if __name__ == '__main__':
    sys.exit(main())
