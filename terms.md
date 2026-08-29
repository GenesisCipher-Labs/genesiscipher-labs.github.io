---
title: HomeSafe Terms & Emergency Services Disclaimer
permalink: /terms/
---

# HomeSafe Terms & Emergency Services Disclaimer

Last updated: August 28, 2026

HomeSafe ranks route options by publicly available safety signals, including Apple Maps points of interest, time of day, street-lighting data, and weather. Community reporting is disabled in this build and no community report is displayed or used in a route score. HomeSafe is decision support. It is not a substitute for your judgement.

## visionOS journey-card edition

The current visionOS edition keeps only a destination, travel mode, and departure choice in process memory. It does not request location, contacts, Motion & Fitness, microphone, speech recognition, or account access; calculate a route or safety rating; start or monitor a live trip; submit a community report; or contact a map, weather, civic-data, or CloudKit provider. The journey card is not written to persistent storage: clearing it removes it immediately, and otherwise it disappears when the app process ends. The route, communication, and data-control features described below apply to the iPhone, iPad, and Apple Watch editions unless a section says otherwise.

## Who you are contracting with

HomeSafe is published by **GenesisCipher Labs Private Limited**, a company incorporated in India ("GenesisCipher Labs", "we", "us"). These terms are an agreement between you and GenesisCipher Labs alone. **They are not an agreement with Apple, and Apple is not responsible for HomeSafe or its content.** We — not Apple — are solely responsible for supporting HomeSafe and for answering any question, complaint, or claim about it. Write to us at **genesiscipherlabs@gmail.com**.

## Who can use HomeSafe

You must be at least 13 years old to use HomeSafe. If you are under 18, you may use it only with the consent and supervision of a parent or guardian, who accepts these terms on your behalf. HomeSafe is not directed to children under 13.

## What HomeSafe does not do

- HomeSafe does not contact emergency services on your behalf.
- HomeSafe does not relay, dispatch, or forward your location to 911, 112, 988, 1091, 1098, 181, or any other emergency or crisis line.
- HomeSafe does not have any commercial, technical, or government partnership with any emergency service.
- HomeSafe cannot verify that any call or message was received, read, or acted on.

## What HomeSafe does

- Surfaces the appropriate numbers for the supported region: in the United States, 911 plus national support lines and a verified local crisis line when location resolves to San Francisco, New York City, Los Angeles, or the Peninsula & South Bay; in India, 112 unified ERSS plus applicable support lines such as 1091, 1098, and 181.
- Opens the system Phone dialer with the number prefilled. You decide whether to place the call.
- Opens the system share sheet so you can pick a personal contact and send your current location via Messages, WhatsApp, or any other installed app. You decide whether to send.
- HomeSafe does not draft, address, or send any SMS to 911, 112, or any other emergency line. The only path from inside HomeSafe to an emergency number is the system dialler. Emergency services may support text contact in some places, including San Francisco's Text-to-911 and India's ERSS-112 distress channels. Text-to-911 availability is determined by the local public safety answering point, not HomeSafe. HomeSafe is not part of those systems and cannot verify receipt, response, or dispatch.

No safety app can guarantee your safety. Always trust your judgement and contact local emergency services directly when at risk. If you cannot use HomeSafe for any reason, dial the local primary emergency number directly using your phone — 911 in the United States or 112 in India.

HomeSafe is provided as-is. Scores and signals are heuristics derived from public and device-side data; they may be wrong. Do not rely on them in life-threatening situations.

## Data handling

- Route scores, contacts, trip logs, recent and saved places, and AI Bestie conversations are processed and stored on your device. Direct provider requests are the exceptions described below; new community-report submission and product use are disabled in this build.
- HomeSafe's personal learning profile stays on your device. It keeps interpretable aggregates such as walking pace, travel rhythm, coarse place familiarity and check-in responsiveness, plus at most the latest 24 dimensionless ETA differences per travel mode and time band. Those timing values carry no route, endpoint, timestamp, or trip identifier. They can add a private planning allowance after enough comparable arrivals, but never change a route's safety score. The profile is included in Export and Delete all.
- During a live walking trip, HomeSafe uses Apple's Motion & Fitness data on your device to show measured steps, detect pace or declared-transport mismatches, improve on-device walking estimates, and support automatic pace-based Drink Mode signals. HomeSafe does not persist a raw motion history or upload motion readings. A final measured step count can remain briefly in the on-device trip summary; other live sensor state is cleared at trip end. If Motion & Fitness access is denied or unavailable, the trip continues using GPS-derived pace and estimated steps. One aggregate mean pace observation from a sufficiently sampled walking trip may update the on-device personal learning profile's pace mean, variability, and walking-trip count; that profile is included in Export and Delete all. Route wandering is derived from live route location, not Motion & Fitness data.
- During a live trip, HomeSafe keeps receiving your location in the background so the trip continues while your screen is locked or you are in another app, and it asks iOS not to pause those updates while you wait somewhere. iOS shows its own background-location indicator whenever that is happening. HomeSafe requests only When In Use location access and never asks for Always access. Background updates are started when a trip starts and surrendered when it ends; the same background access runs while your car's CarPlay screen is showing the HomeSafe map, and is surrendered when that screen goes. A live trip also turns on Apple's visit monitoring, so iOS can tell HomeSafe you have settled somewhere for several minutes and the trip can finish on its own if the phone went into a pocket for the last few metres. Each reported visit is compared with your destination on this device and used for nothing else: HomeSafe keeps no visit history, adds no visit to your trip journal, and uploads no visit. Visit monitoring stops when the trip ends.
- When you use HomeSafe on Apple Watch, the phone keeps a bounded delivery ledger for up to seven days (a random request identifier, check-in/help action, and received/handled times). It exists only to recover queued actions and reject duplicates, stays on your Apple devices, and is included in Export and Delete all.
- GenesisCipher Labs does not operate an application backend that ingests your private routes, contacts, trip history, or continuous location, and does not sell personal data. Community reporting is disabled in this build for all markets pending an authenticated Production `SafetyReport` schema, index, and role probe. Previously submitted records may remain in Apple's public CloudKit until deleted as described below.
- If you tap the mic button in the AI Bestie chat, your speech is transcribed on your device using Apple's on-device speech recognition. Audio is processed transiently for recognition and is not saved or uploaded by HomeSafe, and the transcription stays on your device like the rest of your Bestie conversation. If on-device speech recognition is unavailable, the mic button is not shown.
- Apple Maps and Apple Weather may be queried directly from your device for directions, points of interest, and weather near your route. In the US launch cities, the National Weather Service may be queried for the fixed county alert zones covering that city. In San Francisco only, DataSF may be queried for delayed city-wide open fight-dispatch calls. The 511 SF Bay service-alert integration is disabled in this build because no HomeSafe proxy endpoint is configured, so the app makes no 511 alert request. Enabled civic-feed requests contain no user coordinate, destination, or route: the county zones and city-wide filter are fixed values for the city, identical for every user in that market. Public OpenStreetMap (Overpass) route-corridor requests and NYC Open Data sidewalk-work permit requests are disabled in this build: the public Overpass instance is not an approved production backend, and the NYC dataset's production-use licence is unresolved. No route geometry is sent to Overpass and no NYC permit request is made. Open-Meteo local-conditions requests are disabled in this build and may be enabled only after a commercially licensed customer endpoint and credential are configured and this disclosure is updated. Enabled requests go to those providers, not to us.
- HomeSafe accepts no new community report, does not fetch reports for product use, save a new submission, publish, display, or score reports, and sends no new `SafetyReport` record to CloudKit in this build. Records submitted by earlier builds may remain in Apple's public CloudKit and are not copied into a GenesisCipher Labs-operated server. They carry no name, phone number, or email address, but they may carry the opaque account identifier Apple assigned the submitting device for this app. GenesisCipher Labs can access and remove those prior public records for moderation, support, or a deletion request.
- Previously submitted records remain in Apple's public database until deleted; CloudKit does not expire them automatically. Earlier enabled builds stopped displaying and scoring a report after 90 days, while this build displays and scores none. Neither rule is deletion. You can delete any report you submitted at any time in Settings → Privacy & Data → My flags, which removes its public CloudKit record as well as the local deletion handle; you can also write to us to have one removed. Author-deletion and GenesisCipher Labs moderation, support, and deletion-request controls remain available while new reporting is disabled.
- **Guardian Live-Link publishing is disabled in this build**, so the app cannot create a live share, working link, or active tracking session; the rest of this clause is what applies if it is re-enabled in a later release. If you choose to share a Guardian Live-Link with someone you trust during a trip, your live coordinate, ETA, distance, score, transport, and destination label are published to a public Apple CloudKit record — keyed by an unguessable per-trip token in the URL fragment, carrying no name, phone, home address, or saved place — only while that trip is active. Your location data is deleted from the record the moment you arrive — a brief, non-locating "arrived" confirmation remains so your recipient sees you made it, removed the next time the app runs — and the record is deleted entirely when you end the trip or tap Stop sharing. Sharing stops after six hours in any case, and any deletion the app could not complete in the moment is completed the next time the app runs.
- You can view, export, or delete your on-device data at any time in Settings → Privacy & Data, and revoke location access in iOS Settings. See our [Privacy Policy](/privacy/) for full data-handling and regional-rights details.

## Community reports — acceptable use

Community reporting is disabled in this build. The following rules continue to govern reports submitted previously and apply if reporting is deliberately re-enabled in a later build. If you submit a report in such a future build, you agree that:

- You are reporting a **place and a condition you have genuinely observed** — never a verdict on a neighbourhood, and never an accusation against an identifiable person, household, business, or community.
- You will not submit a report you know to be false, nor submit reports to harass, intimidate, target, defame, or retaliate against any person or property.
- You will not use HomeSafe to follow, surveil, or track any person without their knowledge and consent.

Community reports are submitted by other users, not by us. **We do not verify them and we do not adopt or endorse what they say.** We may remove any report, or decline to display or score it, at our discretion — including where we consider it false, abusive, unlawful, or aimed at an identifiable person. If you believe a report is false or abusive, email **genesiscipherlabs@gmail.com** with enough detail to identify it; we will review it and remove it where appropriate.

## No warranty

HomeSafe is provided **"as is" and "as available"**, without warranty of any kind, whether express, implied, or statutory — including any implied warranty of merchantability, fitness for a particular purpose, accuracy, or non-infringement. We do not warrant that HomeSafe will be uninterrupted, error-free, or available in any particular place, or that any score, signal, route, estimate, alert, or community report is accurate, complete, current, or suitable for your circumstances. **Safety signals are heuristics built from public and device-side data, and they may be wrong.**

## Limitation of liability

To the fullest extent permitted by applicable law:

- GenesisCipher Labs is **not liable** for any indirect, incidental, special, consequential, exemplary, or punitive loss, or for any loss of profits, revenue, data, goodwill, or opportunity, arising out of or relating to your use of — or inability to use — HomeSafe.
- GenesisCipher Labs is **not liable** for loss or harm arising from a route you chose, a score or signal you relied on, a report submitted by another user, an alert that did not arrive or arrived late, a check-in or share that failed to send, an emergency number that was wrong or unavailable, or the act or omission of any third party — including any emergency service, transport operator, data provider, or other user.
- Our total aggregate liability for all claims relating to HomeSafe will not exceed the greater of (a) what you paid us for HomeSafe in the twelve months before the event giving rise to the claim, or (b) **USD 50**.

**Nothing in these terms excludes or limits any liability that cannot lawfully be excluded or limited.** That includes, where applicable, liability for death or personal injury caused by negligence, for fraud or fraudulent misrepresentation, for gross negligence or wilful misconduct, and any right you have under mandatory consumer-protection law. Some jurisdictions do not allow certain exclusions or limitations, so parts of this section may not apply to you; if any part is held unenforceable, the rest continues to apply.

## Governing law and disputes

These terms are governed by the laws of **India**, and the courts having jurisdiction over the seat of our registered office in India will have jurisdiction over any dispute — **without depriving you of the protection of any mandatory consumer-protection law of your country or state of residence, or of any right you have under that law to bring proceedings in your local courts.** If any provision of these terms is found invalid or unenforceable, it is limited to the minimum extent necessary and the rest remains in full effect.

We would far rather fix a problem than argue about one: please write to **genesiscipherlabs@gmail.com** first, and we will try to resolve it with you directly.

By using HomeSafe, you acknowledge that HomeSafe is a routing and location-sharing aid, not an emergency-services intermediary.
