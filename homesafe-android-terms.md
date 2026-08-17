---
title: HomeSafe for Android — Terms & Emergency Services Disclaimer
permalink: /terms/android/
description: HomeSafe for Android's Terms of Use and Emergency Services Disclaimer. HomeSafe ranks route options by safety signals from public map data; it does not dispatch emergency services and is not a substitute for calling them.
---

# HomeSafe for Android — Terms & Emergency Services Disclaimer

Last updated: July 27, 2026

> **These are the Android terms.** The iPhone version of HomeSafe is a different build with
> different data flows — no shared community-report database on Android, and no Apple Maps or
> WeatherKit infrastructure behind it. The iOS terms are at [/terms/](/terms/). Where the two
> differ, the difference is real, not editorial.

## The short version

HomeSafe is a **routing aid** and decision-support tool for movement decisions. It is **not** an
emergency dispatch service, not a safety authority, and it does not replace your own judgement.

By using HomeSafe you acknowledge:

- HomeSafe helps you choose safer-looking routes using public intelligence and your phone's live signals.
- You remain in control of whether you take or ignore any suggested route.
- HomeSafe does not own rescue operations.

## What HomeSafe does not do

HomeSafe does not contact emergency services on your behalf.

HomeSafe does not relay, dispatch, or forward your location to 112, 1091, 1098, 181, or any other emergency line.

HomeSafe does not have any commercial, technical, or government partnership with any emergency service.

## Emergency Services disclosure

The emergency-dispatch disclaimer above is core legal text, not a soft warning:

- The app does not place emergency calls automatically.
- It does not send pre-authenticated distress packets.
- If you are in immediate danger or distress, you should dial emergency services directly.

## What HomeSafe does do

- HomeSafe surfaces the correct emergency numbers for India: 112 unified ERSS, plus 1091, 1098, and 181.
- It can open the system Phone dialler with a selected number pre-filled. You place the call.
- It can open your messaging app or share sheet with a location pre-filled if you choose to share manually.
- It never sends an emergency call or message itself.

## Data, storage, and privacy posture

HomeSafe keeps route scores, safety signals, trip snapshots, trusted contacts, saved places, community
reports, and Bestie conversation history **on-device** by default. Nothing is uploaded to a
GenesisCipher Labs server as part of HomeSafe operation.

This Android build does not use a shared community safety report database. Community reports never
leave the phone and carry no account, device, or advertising identifier.

Map and routing support uses public services directly from your device:

- Geocoding/search: **Nominatim**
- Route geometry: **routing.openstreetmap.de** (FOSSGIS OSRM)
- POI / lighting / crossings intelligence: **overpass-api.de**
- Map tiles: **OpenFreeMap**
- Weather / rain outlook / air quality: **Open-Meteo**
- Live sharing transport (opt-in): **ntfy.sh**

Optional mic use in Bestie chat uses your phone's speech recognition service. HomeSafe requests
on-device preference where available, never records or stores audio locally as a permanent separate
file, and sends no message unless you press Send.

## Retention and erasure

- Community reports and similar safety artifacts are removed after 90 days and cleaned from storage on read.
- Settings → Privacy & data gives you full-device export and deletion of stored data you have provided to HomeSafe.
- Deleting data follows what HomeSafe stores and processes itself; there is no off-device safety dossier to erase.

See our [Privacy Policy](/privacy/android/) for India DPDP and GDPR details.

## Premium / billing

HomeSafe is sold via Google Play. Premium unlocks premium-only surfaces and explanations, but it does
not change the safety architecture:

- Premium does not buy a safer score.
- Premium does not buy faster safety check-ins.
- Premium does not change route scoring.

## Guardian Live-Link (opt-in)

If you enable live trip sharing, your live trip position/ETA/distance/safety score/transport headline
and destination label are published on a private ntfy.sh channel chosen from a random token.

The channel never carries your name, phone number, saved home/office address, or contact details.
Anyone with the share link can view that stream, which is why we treat it as personal data under your
control.

## Liability and limitation

HomeSafe is provided as-is. Heuristics can be wrong, data may be incomplete, and route safety signals
do not guarantee real-world safety.

You should always use your own judgement, and if you feel unsafe, contact trusted contacts or
emergency services directly.

## Miscellaneous

- HomeSafe for Android is not directed at children under 13.

By using HomeSafe, you acknowledge that HomeSafe is a routing and location-sharing aid, not an
emergency-services intermediary.

## Contact

GenesisCipher Labs — **genesiscipherlabs@gmail.com**
