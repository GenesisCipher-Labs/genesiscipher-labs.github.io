# genesiscipher-labs.github.io

The GenesisCipher Labs organisation root **GitHub Pages** site, served at
<https://genesiscipher-labs.github.io/>. It is a static, Jekyll-built site (GitHub Pages renders the
Markdown front-matter pages automatically — there is no local build step or Node toolchain). Push to
the default branch and Pages publishes.

## Pages

| Path | Source | Purpose |
|---|---|---|
| `/` | `index.md` | Org landing page and links. |
| `/privacy/` | `privacy.md` | HomeSafe Privacy Policy (GDPR + India DPDP Act). App Review and the App Store Connect privacy section hit this URL. |
| `/terms/` | `terms.md` | HomeSafe Terms & Emergency Services Disclaimer. Mirrors the in-app EULA; App Review verifies the non-dispatch 5.1.5 language here. |
| `/track/` | `track/index.html` | The **Guardian Live-Link** viewer (see below). |

`privacy.md` and `terms.md` are legal source-of-truth mirrors of the HomeSafe iOS repo's `dist/` copies
and the in-app EULA — keep the three in sync, and keep the "Last updated" date accurate to the last
substantive edit.

## Guardian Live-Link (`/track/`)

`track/index.html` is the no-app-needed live-trip viewer: a HomeSafe user texts a trusted person a
secret link and they watch the trip on a map in any browser until it ends. It uses Leaflet + CARTO dark
tiles over OpenStreetMap (no map API token) and Apple **CloudKit JS** to read a public, token-keyed
`GuardianTrip` record. The secret token rides in the URL **fragment** so it never reaches the Pages
host. With no token (or `#demo`) the page plays a scripted demo trip.

Configuration lives in the `CONFIG` block at the top of the page (`containerIdentifier`, the read-only
origin-restricted `apiToken`, `environment`, `recordType`, poll interval, staleness window). See
[`docs/GuardianLiveLink.md`](./docs/GuardianLiveLink.md) for the full field set, the CloudKit token
scope, and the **arrival contract** — the viewer only shows the positive "Made it safe" on an explicit
`endReason === 'arrived'` and otherwise defaults to the neutral "Live sharing ended", so a stale or
dead link is never shown as a safe arrival.

## Contact

genesiscipherlabs@gmail.com
