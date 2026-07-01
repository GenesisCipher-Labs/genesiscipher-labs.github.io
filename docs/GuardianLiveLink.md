# Guardian Live-Link — `/track/` viewer

The Guardian Live-Link is HomeSafe's "no-app-needed" live-trip share. Someone on a trip texts a
trusted person a secret link; that person opens it in any browser and watches them move toward their
destination on a map. The link dies the moment the trip ends.

This document describes the **public viewer** hosted at `genesiscipher-labs.github.io/track/`. The iOS
publisher side (which writes the records this page reads) lives in the private HomeSafe iOS repo
(`GuardianLinkPublisher` + the `GuardianTrip` CloudKit schema).

## How it works

- The link is `https://genesiscipher-labs.github.io/track/#<token>`. The token rides in the URL
  **fragment** (`#…`), so it never reaches the GitHub Pages host — it is read entirely in-browser.
- The token is the `recordName` of a public Apple **CloudKit** record of type `GuardianTrip`. The page
  polls that record and renders the live position, ETA, distance, and safety score.
- No map API token is needed: the map is Leaflet + CARTO dark tiles over OpenStreetMap data.
- With no token (or `#demo`), the page plays a scripted demo trip so the experience is always visible.

## The record (`GuardianTrip`)

PII-free by construction. The publisher may write only these fields:

`latitude`, `longitude`, `course`, `etaMinutes`, `distanceKm`, `score`, `transportSymbol`,
`destinationLabel`, and the opt-in `destinationLatitude` / `destinationLongitude`.

There is **no name, phone, home address, or saved place** in the record. The destination is a label by
default; the destination pin is opt-in.

### Terminal status (the arrival contract)

The viewer must never show a false "Made it safe". Silence — a stale record, a deleted record, an
expired trip, a stopped share, or a dead phone — is **not** proof of a safe arrival, so all of those
resolve to the neutral **"Live sharing ended"** state.

The positive **"Made it safe"** message is shown **only** when the record carries an explicit
`endReason` field equal to `arrived` — a short-lived tombstone the phone writes just before it purges
the trip, and only on a positively-confirmed arrival. Until the iOS publisher writes that field (and
the CloudKit schema has it deployed to Production), the viewer safely defaults to the neutral state for
every termination.

## Founder config (`track/index.html` → `CONFIG`)

| Key | Meaning |
|---|---|
| `containerIdentifier` | `iCloud.com.genesiscipherlabs.HomeSafe` — the CloudKit container. |
| `apiToken` | CloudKit JS API token **"track-prod"**. Intended scope: **public-database read-only, origin-restricted** to `genesiscipher-labs.github.io`. It can only fetch the token-keyed `GuardianTrip` records; it grants no write access and no private-database access, so it is safe in this public client. |
| `environment` | `production` — release/TestFlight builds write to the Production DB. Use `development` only when validating new schema fields against a Debug build before redeploying. |
| `recordType` | `GuardianTrip`. |
| `pollMs` | How often the browser refreshes (default 7 s). |
| `staleSeconds` | No fresh update for this long → treat the trip as ended (neutral). |

## Keeping this page in sync

The source of truth for the viewer is `dist/track/index.html` in the HomeSafe iOS repo; this repo's
`track/index.html` is the deployed mirror. When either changes, mirror the other and keep the arrival
contract above identical on both sides.
