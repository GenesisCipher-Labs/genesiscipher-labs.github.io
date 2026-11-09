# GenesisCipher Labs website

The GitHub Pages site provides HomeSafe and Pact information, platform-specific privacy policies, terms and support. Current launch information is in [Release availability](RELEASE_AVAILABILITY.md).

## Verify before publishing

Keep all six repositories checked out alongside each other, fetch their current branches, then run:

```sh
python3 tools/check_content_sync.py
bundle install
bundle exec jekyll build --strict_front_matter
python3 tools/check_site.py
bash ../genesiscipherlabs-HomeSafe-iOS/Tools/legal/check_legal_mirror.sh
```

`content-sync.json` declares ownership for 19 exact mirrors, and one repository mirror: `gcl-privacy-policy` is kept identical to this repository, every tracked file byte-for-byte with nothing extra. HomeSafe iOS owns its public legal pages and landing page; this repository owns the concise Android and Pact pages and the shared release record. `python3 tools/check_content_sync.py --sync` updates only those declared mirrors. Review and commit every affected repository together.

The Pact August marketing package is archived in its app repository and is not a deployment source. HomeSafe iOS enabled Guardian Live-Link publishing on 2026-11-09, so `/track/` serves its tracker (`genesiscipherlabs-HomeSafe-iOS/dist/track/index.html`, byte-identical; its legal mirror check enforces this). HomeSafe Android still disables publishing and its pages say so. Do not publish this site's Guardian privacy section ahead of the iOS build that enables it, and review both platform gates and disclosures before changing either.

GitHub Pages publishes `main` from `/`. After pushing and the Pages deployment succeeds, run `python3 tools/check_site.py --live` to compare every public page with the verified local build. Existing noindex settings on the legal/support layout remain in place; the HomeSafe product page uses its own metadata.

The checks cover website content and links, not native app builds or an independent audit of every App Store / Google Play territory. Release availability is the publisher’s September 14 confirmation. Website changes do not modify store configuration.
