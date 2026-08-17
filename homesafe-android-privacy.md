---
title: HomeSafe for Android — Privacy Policy
permalink: /privacy/android/
description: What HomeSafe for Android processes on your device, the six public map and weather services it queries directly, and the Google components Play Billing brings with it — stated plainly.
---

# HomeSafe for Android — Privacy Policy

Last updated: July 27, 2026

> **This is the Android policy.** The iPhone version of HomeSafe is a different build with different
> data flows — it syncs community reports through Apple's public CloudKit database, uses Apple Maps
> and WeatherKit, and carries an Apple account identifier on each public record. **None of that
> exists in the Android app.** Its policy is at [/privacy/](/privacy/). Where the two differ, the
> difference is real, not editorial.

## The short version

HomeSafe has no account, no sign-in, no advertising identifier, and no analytics of our own. There is
no HomeSafe server. Every route score, safety signal, contact, saved place, trip snapshot, journal
entry, community report and Bestie conversation is processed and stored **on your device only**.

Two things leave the phone because you asked for them: the map/routing/weather lookups the app needs
to work at all, and — if you switch it on — a Guardian Live-Link. One more thing is in the app that
we did not write and do not control, and we would rather name it than let you find it: see
"[Google Play Billing brings its own components](#google-play-billing-brings-its-own-components)".

## What HomeSafe is not

HomeSafe does **not** contact emergency services on your behalf, does not relay or forward your
location to 112, 1091, 1098, 181 or any other emergency line, and has no partnership of any kind with
any emergency service. It pre-fills the system dialler; you place the call.

## No cloud backup

The app sets `android:allowBackup="false"` and ships `res/xml/data_extraction_rules.xml` that excludes
every storage domain from **both** Android Auto Backup and device-to-device transfer. The operating
system therefore does not copy HomeSafe's data to your Google account or to a new phone.

The honest cost of that promise: if you lose, reset or replace this phone, what HomeSafe stored is
gone. We consider that the right trade for an app that holds your home address and your trusted
contacts' phone numbers.

## Services HomeSafe queries directly from your device

These requests go from your phone to these providers. They never pass through GenesisCipher Labs, and
like any web request they show that provider your device's IP address and roughly the area you are
asking about.

| Purpose | Service |
|---|---|
| Address search / geocoding | Nominatim (`nominatim.openstreetmap.org`) |
| Route geometry | FOSSGIS OSRM (`routing.openstreetmap.de`) |
| Street lighting, crossings, points of interest | Overpass (`overpass-api.de`) |
| Map tiles | OpenStreetMap tiles, OpenFreeMap (`tiles.openfreemap.org`) |
| Temperature, rain outlook, air quality | Open-Meteo (`api.open-meteo.com`, `air-quality-api.open-meteo.com`) |
| Guardian Live-Link transport (opt-in only) | ntfy.sh |

## Google Play Billing brings its own components

Premium is sold through Google Play, so the app includes Google's Play Billing library. That library
does not arrive alone. Google ships it bundled with its own **DataTransport** components
(`com.google.android.datatransport`, including the `transport-backend-cct` uploader and the
`com.google.firebase:firebase-encoders` wire encoders) and with parts of Play Services
(`play-services-base`, `play-services-basement`, `play-services-tasks`, and — despite HomeSafe using
none of it — `play-services-location` and `play-services-places-placereport`).

What that means, stated plainly:

- **DataTransport is a telemetry uploader.** It belongs to Google and reports Google's own billing
  diagnostics to Google. We do not configure it, cannot see what it sends, and have not measured it.
  We are naming it rather than hiding behind "we added no analytics", which was the truthful-but-
  incomplete way to describe this.
- **HomeSafe adds no analytics, crash reporting or advertising SDK of its own.** That part is
  unchanged and remains true — grep the source for it.
- **`play-services-location` is linked but never called.** HomeSafe's location comes from the Android
  framework `LocationManager`, not from Google Play Services. The library is present only because
  Play Billing depends on it. It is not a second location pipeline.

If you never open the Premium screen, none of this changes what HomeSafe itself does with your data:
your places, contacts, journal and flags still never leave the phone.

## Microphone and speech

The mic button in the Bestie chat is optional and only active while you hold it. HomeSafe hands the
audio to **your phone's own speech-recognition service** and asks it to work offline
(`EXTRA_PREFER_OFFLINE`), so that nothing leaves the phone where the system supports it. HomeSafe
itself never records, stores or uploads your audio, and the button only appears when your phone has a
recognition service at all.

We will not over-promise here: on Android, "prefer offline" is a request, not a guarantee. Whether the
transcription actually stays on the phone is decided by that system service, and on some devices your
speech may be sent to its provider to be transcribed. The transcript becomes a message only when you
tap Send.

## Community safety reports

Reports you submit **stay on this device**. Unlike the iPhone version of HomeSafe, the Android app has
no shared reports database: your flags are never uploaded, never shown to other users, and carry no
account, device or advertising identifier anywhere — because they never leave your phone.

HomeSafe stops showing and stops counting a report after 90 days and deletes it from the device the
next time it reads them.

## Guardian Live-Link (opt-in)

If you choose to share a live trip link, HomeSafe publishes your live position, remaining ETA and
distance, safety score, transport type and a destination **label** to ntfy.sh — a free, account-less
public messaging service — on a channel named by an unguessable 160-bit token that is also the link.

- It never carries your name, phone number, home address or saved places.
- Anyone holding the link can watch, so only send it to someone you trust.
- HomeSafe stops publishing and posts a final "ended" note the moment the trip ends or you tap Stop,
  and sharing stops after six hours in any case.
- ntfy.sh keeps recently delivered messages in its own cache for a limited time afterwards. That is
  outside our control, and we say so rather than claim an instant delete we cannot perform.

## Permissions, and why

| Permission | Why |
|---|---|
| Location (fine/coarse) | Scoring the route you are actually on, live navigation, and the location you choose to share. Never uploaded to us. |
| Microphone | Only while you hold the Bestie mic button (see above). |
| Notifications | Trip check-in prompts. |
| Internet / network state | The services in the table above. |
| Vibrate | The on-device Fake Call ring (simulated; no telephony). |

## Your rights (GDPR Art. 15/17/20, India DPDP)

Settings → **Privacy & data**:

- **Export my data** writes a readable JSON file with everything the app holds — recents, saved Home
  and Work, trusted contacts, trip journal, community reports, the fake-caller name, your
  contribution count, the profile learned from your trips, any in-flight trip snapshot, armed trip
  modes, and which premium samples you have used. It is shared only through your own share sheet, and
  the cached copy is deleted afterwards.
- **Delete my data** erases all of the above from the device, and retracts a live Guardian Live-Link
  before dropping the handle to it. Theme, safety-vibe, EULA acceptance and your Play purchase are
  kept: they are not personal data, and a purchase is not ours to delete.

There is nothing to request from us, because we hold nothing.

## Payments

Premium is billed by Google Play. We never see your card. Premium never buys a safer score, a faster
check-in or a different way to reach help — every safety surface is identical whether or not you pay.

## Children

HomeSafe is not directed at children under 13.

## Changes

If this policy changes materially we will update the date at the top and, where the change affects
what leaves your device, say so in the app's release notes.

## Contact

GenesisCipher Labs — **genesiscipherlabs@gmail.com**
