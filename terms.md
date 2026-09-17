---
title: HomeSafe Terms & Emergency Services Disclaimer
permalink: /terms/
description: Terms for HomeSafe on Apple platforms.
---

# HomeSafe Terms & Emergency Services Disclaimer

Last updated: September 17, 2026

These terms are between you and GenesisCipher Labs Private Limited. By using HomeSafe on an Apple platform, you agree to them.

HomeSafe is published by **GenesisCipher Labs Private Limited**, a company incorporated in India ("GenesisCipher Labs", "we", "us"). These terms are an agreement between you and GenesisCipher Labs alone. **They are not an agreement with Apple, and Apple is not responsible for HomeSafe or its content.** We — not Apple — are solely responsible for supporting HomeSafe and for answering any question, complaint, or claim about it. Write to us at **genesiscipherlabs@gmail.com**.

HomeSafe ranks route options by publicly available safety signals, including Apple Maps points of interest, time of day, street-lighting and pedestrian-infrastructure data derived from OpenStreetMap (street lighting, sidewalks and footways, pedestrian crossings, and surface quality), and weather. Community reporting is disabled in this build and no community report is displayed or used in a route score. HomeSafe is decision support. It is not a substitute for your judgement.

HomeSafe is a route-planning and location-sharing aid. Its routes, scores, alerts and estimates may be incomplete, delayed or wrong. They do not guarantee safety and are not professional advice. HomeSafe does not contact, dispatch or communicate with emergency or crisis services for you. In an emergency, contact the appropriate service directly and use your own judgment.

You control whether to place a call, send a message, share information or follow a route. Use HomeSafe lawfully and do not use it to harm, harass, mislead or track anyone without consent. You must be at least 13; if you are under the age of majority, a parent or guardian must approve your use.

## visionOS journey-card edition

The current visionOS edition keeps only a destination draft or verified destination, travel mode, and departure choice in process memory. It does not request location, contacts, Motion & Fitness, microphone, or speech recognition; calculate a route or safety rating; start or monitor a live trip; submit a community report; or contact a weather, civic-data, or CloudKit provider. Its Membership tab shows HomeSafe's in-app purchases through Apple's own store interface, and Restore Purchases asks the App Store about purchases already made with your Apple Account; HomeSafe never sees your Apple Account credentials, Apple processes any purchase, and this edition unlocks no feature with a membership. When you verify a destination, HomeSafe sends the place query and a fixed search region for the selected city — never your device location or HomeSafe account — directly to Apple Maps, and accepts a result only inside that city's supported service area. The journey card is not written to persistent storage: clearing it removes it immediately, and otherwise it disappears when the app process ends. The route, communication, and data-control features described below apply to the iPhone, iPad, and Apple Watch editions unless a section says otherwise.

HomeSafe is not offered in the Indian App Store. Indian city coverage is also withheld from this version: the mapped Indian city data stays bundled and any history you already hold is untouched, but routing, search, place reads, Help directories and the companion surfaces are available in the supported United States cities only.

## What HomeSafe does not do

- HomeSafe does not contact emergency services on your behalf.
- HomeSafe does not relay, dispatch, or forward your location to 911, 988, or any other emergency or crisis line.
- HomeSafe does not have any commercial, technical, or government partnership with any emergency service.
- HomeSafe cannot verify that any call or message was received, read, or acted on.

## What HomeSafe does

- Within current United States coverage, surfaces 911 plus national support lines and a verified local crisis line when location resolves to San Francisco, New York City, Los Angeles, or the Peninsula & South Bay. Outside current coverage, HomeSafe does not guess an emergency number.
- Opens the system Phone dialer with the number prefilled. You decide whether to place the call.
- Opens the system share sheet so you can pick a personal contact and send your current location via Messages, WhatsApp, or any other installed app. You decide whether to send.
- HomeSafe does not draft, address, or send any SMS to 911 or any other emergency line. The only path from inside HomeSafe to an emergency number is the system dialler. Emergency services may support text contact in some places, including San Francisco's Text-to-911. Text-to-911 availability is determined by the local public safety answering point, not HomeSafe. HomeSafe is not part of those systems and cannot verify receipt, response, or dispatch.

No safety app can guarantee your safety. Always trust your judgement and contact local emergency services directly when at risk. Within the United States, dial 911 directly when appropriate. Outside current HomeSafe coverage, use your device's emergency controls or contact the local emergency service directly; HomeSafe does not guess a number.

HomeSafe is provided as-is. Scores and signals are heuristics derived from public and device-side data; they may be wrong. Do not rely on them in life-threatening situations.

## Community reports

Community reporting is disabled in this build for all markets pending an authenticated Production `SafetyReport` schema, index, and role probe. Previously submitted records may remain in Apple's public CloudKit until deleted; author-deletion and GenesisCipher Labs moderation, support, and deletion-request controls remain available.

- **Community reporting is disabled in this build for all markets.** HomeSafe accepts no new report, does not fetch reports for product use, save a new submission, publish, display, or score reports, and sends no new `SafetyReport` record to CloudKit. Records submitted by an earlier build may remain in Apple's **public CloudKit** until deleted. Those records carry no name, phone, or email, but they may carry the opaque account identifier Apple assigned the submitting device for this app. GenesisCipher Labs can access and remove previously submitted records for moderation, support, or a deletion request. **You can delete any report you submitted at any time** in Settings → Privacy & Data → My flags. These deletion and moderation controls remain available while new reporting is disabled.

## Location, including in the background

- During a live trip, HomeSafe keeps receiving your location in the background so the trip continues while your screen is locked or you are in another app, and it asks iOS not to pause those updates while you wait somewhere. iOS shows its own background-location indicator whenever that is happening. HomeSafe requests only When In Use location access and never asks for Always access. Background updates are started when a trip starts and surrendered when it ends; the same background access runs while your car's CarPlay screen is showing the HomeSafe map, and is surrendered when that screen goes. A live trip also turns on Apple's visit monitoring, so iOS can tell HomeSafe you have settled somewhere for several minutes and the trip can finish on its own if the phone went into a pocket for the last few metres. Each reported visit is compared with your destination on this device and used for nothing else: HomeSafe keeps no visit history, adds no visit to your trip journal, and uploads no visit. Visit monitoring stops when the trip ends.

## Personal learning profile

| Personal learning profile (aggregate walking pace, travel-time error and a bounded set of recent dimensionless ETA residuals by travel mode/time band, travel rhythm, coarse place familiarity, and check-in responsiveness) | On your device | Adapt walking estimates, show a private planning allowance after enough comparable arrivals, time overdue nudges more realistically, and explain your own patterns. It never changes a route's safety score and stores no route, endpoint, timestamp, or trip identifier in the ETA residual buckets. It also keeps an on-device per-region mean travel-time error and sample count; an existing aggregate may retain India or United States as its category, but current city coverage is United States only. Store distribution is separate: HomeSafe is available in every country except India. That regional aggregate carries no city, route, or timestamp. The whole profile is included in Export and Delete all | The specified purpose you voluntarily provided the data for |

## Motion & Fitness

During a live walking trip, HomeSafe uses Apple's Motion & Fitness data on your device to show measured steps, detect pace or declared-transport mismatches, improve on-device walking estimates, and support automatic pace-based Drink Mode signals. HomeSafe does not persist a raw motion history or upload motion readings. A final measured step count can remain briefly in the on-device trip summary; other live sensor state is cleared at trip end. If Motion & Fitness access is denied or unavailable, the trip continues using GPS-derived pace and estimated steps. One aggregate mean pace observation from a sufficiently sampled walking trip may update the on-device personal learning profile's pace mean, variability, and walking-trip count; that profile is included in Export and Delete all. Route wandering is derived from live route location, not Motion & Fitness data.

## Apple Watch action delivery

Apple Watch action delivery records (random request identifier, check-in/help action, tap time, tap-time opaque privacy-generation token, opaque trip token for a check-in, delivery result, and received time) — stored on your paired apple watch for delivery and receipt recovery, and on your iphone after receipt. Recover a queued wrist action or its receipt after process death, keep a delayed check-in bound to the trip shown on the Watch, and prevent duplicate WatchConnectivity deliveries from applying it twice. A versioned action can affect the phone only if it arrives within five minutes of its tap time (with up to five seconds allowed for clock skew); a missing, malformed, stale, or farther-future time is review-only before any action record, check-in, or Help handoff is created. The Watch first keeps a bounded delivery-recovery copy with at most one record per action type; a copy bearing an older privacy-generation token is erased when a reset reaches the Watch, and removing the Watch app erases its local copy. An iPhone Export or Delete all covers only records the iPhone has received; a Watch-only copy cannot appear in an iPhone export. Readable records expire individually after seven days and are removed the next time that app executes its delivery ledger; unreadable Watch bytes use the same execution-time bound. A versioned tokenless cold-start request remains review-only and is removed under that bound

## Data sources

City knowledge on iPhone and iPad includes separate, read-only bundled extracts of Overture Places and Overture Transportation, limited to the mapped service areas in India and the United States. Only the United States city packs are reachable in this version. Mapped names, categories, locations and source-supplied addresses support local place and street lookup. These dated map records do not establish current opening hours, staffing, pedestrian access, incidents or safety, and never change route scores. City lookup runs on your device, makes no request to Overture or its contributors, and adds no stored search history. The city data source details offer the public data and its license notices for export without a membership; that export contains no personal searches or trips. The data retains its source licenses. Those permissions apply to the city data, not to the HomeSafe app software. Some curated place and street descriptions draw on Wikipedia articles, which are available under the Creative Commons Attribution-ShareAlike 4.0 licence; those descriptions are available under the same licence and the article used is cited beside each one. The bundled OpenStreetMap-derived street-lighting and camera survey is a Derived Database under the Open Database License 1.0 (© OpenStreetMap contributors); a copy of that database and the method used to build it are available on request at genesiscipherlabs@gmail.com. Curated descriptions and the Overture city-knowledge extracts stay bundled for the Indian and United States markets; only the United States markets are available in this version.

- Apple Maps and Apple Weather may be queried directly from your device for directions, points of interest, and weather near your route. In the US launch cities, the National Weather Service may be queried for the fixed county alert zones covering that city. In San Francisco only, DataSF may be queried for delayed city-wide open fight-dispatch calls. In the US launch cities, the United States Geological Survey may be queried for its public worldwide catalog of recent magnitude-2.5-and-above earthquakes; that request is one fixed address with no query of any kind, so it is identical for every user on earth and the filtering to your city happens on your device. The 511 SF Bay service-alert integration is disabled in this build because no HomeSafe proxy endpoint is configured, so the app makes no 511 alert request. Enabled civic-feed requests contain no user coordinate, destination, or route: the county zones and city-wide filter are fixed values for the city, identical for every user in that market. Public OpenStreetMap (Overpass) route-corridor requests and NYC Open Data sidewalk-work permit requests are disabled in this build: the public Overpass instance is not an approved production backend, and the NYC dataset's production-use licence is unresolved. No route geometry is sent to Overpass and no NYC permit request is made. Open-Meteo local-conditions requests are disabled in this build and may be enabled only after a commercially licensed customer endpoint and credential are configured and this disclosure is updated. Enabled requests go to those providers, not to us.

## Purchases, third-party services and liability

Third-party map, weather, communications and platform services remain subject to their own terms and availability. Any purchase is handled by Apple under the price and terms shown before purchase.

HomeSafe is provided “as is” and “as available,” without warranties to the extent permitted by law. To the extent permitted by law, GenesisCipher Labs is not liable for indirect or consequential loss, and its total liability relating to HomeSafe is limited to the greater of the amount you paid for HomeSafe during the previous 12 months or USD 50. Nothing here limits liability or consumer rights that cannot legally be limited.

These terms are governed by Indian law, without removing mandatory protections available where you live. If one provision is unenforceable, the remainder continues to apply. We may update these terms by changing this page and its date.

See the [HomeSafe Privacy Policy](/privacy/).

Contact: [genesiscipherlabs@gmail.com](mailto:genesiscipherlabs@gmail.com)
