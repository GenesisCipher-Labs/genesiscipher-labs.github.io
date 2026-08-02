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
| `/get/` | `get/index.html` | HomeSafe download page. |
| `/pact/` | `pact.md` | Pact product page. Also where the invoice watermark and "Share Pact" point, until the App Store listing is live. |
| `/pact/support/` | `pact-support.md` | Pact Support & FAQ. **The mandatory App Store Connect Support URL**, and the target of Settings → Help & FAQ in the app. |
| `/pact/privacy/` | `pact-privacy.md` | Pact Privacy Policy (India DPDP Act). App Review and the App Store Connect privacy field hit this URL. |
| `/pact/terms/` | `pact-terms.md` | Pact Terms of Use. |

`privacy.md` and `terms.md` are legal source-of-truth mirrors of the HomeSafe iOS repo's `dist/` copies
and the in-app EULA — keep the three in sync, and keep the "Last updated" date accurate to the last
substantive edit.

**Four of these URLs are compiled into the Pact iOS/macOS binary** — `PurchaseManager.supportURL`,
`.privacyURL`, `.termsURL` and `.appShareURL` — and they resolve through the `permalink:` front
matter, *not* through the filename. So renaming `pact-support.md`, or dropping its permalink, silently
404s a link inside a shipped app and (for the support URL) blocks App Store submission. Changing any
of them means changing the app in the same release. The watermark line in `InvoiceTemplateView` prints
its destination on invoices that have already reached brands and cannot be corrected afterwards — it
previously read `getpact.app`, which has no DNS record at all.

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
