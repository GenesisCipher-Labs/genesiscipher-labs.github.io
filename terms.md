---
title: HomeSafe Terms & Emergency Services Disclaimer
permalink: /terms/
---

# HomeSafe Terms & Emergency Services Disclaimer

Last updated: August 25, 2026

HomeSafe ranks route options by publicly available safety signals, including Apple Maps points of interest, time of day, street-lighting data, weather, and user reports. HomeSafe is decision support. It is not a substitute for your judgement.

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

- Surfaces the appropriate numbers for the supported region: in the United States, 911 plus national support lines and a verified local crisis line when location resolves to San Francisco, New York City, Los Angeles, or Silicon Valley; in India, 112 unified ERSS plus applicable support lines such as 1091, 1098, and 181.
- Opens the system Phone dialer with the number prefilled. You decide whether to place the call.
- Opens the system share sheet so you can pick a personal contact and send your current location via Messages, WhatsApp, or any other installed app. You decide whether to send.
- HomeSafe does not draft, address, or send any SMS to 911, 112, or any other emergency line. The only path from inside HomeSafe to an emergency number is the system dialler. Emergency services may support text contact in some places, including San Francisco's Text-to-911 and India's ERSS-112 distress channels. Text-to-911 availability is determined by the local public safety answering point, not HomeSafe. HomeSafe is not part of those systems and cannot verify receipt, response, or dispatch.

No safety app can guarantee your safety. Always trust your judgement and contact local emergency services directly when at risk. If you cannot use HomeSafe for any reason, dial the local primary emergency number directly using your phone — 911 in the United States or 112 in India.

HomeSafe is provided as-is. Scores and signals are heuristics derived from public and device-side data; they may be wrong. Do not rely on them in life-threatening situations.

## Data handling

- Route scores, contacts, trip logs, recent and saved places, and AI Bestie conversations are processed and stored on your device. Direct provider requests and deliberate community-report submissions are the exceptions described below.
- HomeSafe's personal learning profile stays on your device. It keeps interpretable aggregates such as walking pace, travel rhythm, coarse place familiarity and check-in responsiveness, plus at most the latest 24 dimensionless ETA differences per travel mode and time band. Those timing values carry no route, endpoint, timestamp, or trip identifier. They can add a private planning allowance after enough comparable arrivals, but never change a route's safety score. The profile is included in Export and Delete all.
- When you use HomeSafe on Apple Watch, the phone keeps a bounded delivery ledger for up to seven days (a random request identifier, check-in/help action, and received/handled times). It exists only to recover queued actions and reject duplicates, stays on your Apple devices, and is included in Export and Delete all.
- GenesisCipher Labs does not operate an application backend that ingests your private routes, contacts, trip history, or continuous location, and does not sell personal data. Community reports you deliberately submit are shared through Apple's public CloudKit as described below.
- If you tap the mic button in the AI Bestie chat, your speech is transcribed on your device using Apple's on-device speech recognition. The audio is never recorded, stored, or uploaded, and the transcription stays on your device like the rest of your Bestie conversation. If on-device speech recognition is unavailable, the mic button is not shown.
- Apple Maps and Apple Weather may be queried directly from your device for directions, points of interest, and weather near your route. In the US launch cities, the National Weather Service may be queried for the fixed county alert zones covering that city. In San Francisco and Silicon Valley, 511 SF Bay may be queried for current service alerts from that market's transit operators — Muni and BART in San Francisco; Caltrain, BART and VTA in Silicon Valley. In San Francisco only, DataSF may be queried for delayed city-wide open fight-dispatch calls. Those enabled civic-feed requests contain no user coordinate, destination, or route: the county zones, operator codes and city-wide filter are fixed values for the city, identical for every user in that market. The 511 request also contains the app's developer token. Public OpenStreetMap (Overpass) route-corridor requests and NYC Open Data sidewalk-work permit requests are disabled in this build: the public Overpass instance is not an approved production backend, and the NYC dataset's production-use licence is unresolved. No route geometry is sent to Overpass and no NYC permit request is made. Open-Meteo local-conditions requests are disabled in this build and may be enabled only after a commercially licensed customer endpoint and credential are configured and this disclosure is updated. Enabled requests go to those providers, not to us.
- Community safety reports you choose to submit are shared with other HomeSafe users by design. Records go directly from your device to Apple's public CloudKit and are not copied into a GenesisCipher Labs-operated server. GenesisCipher Labs can access and remove those public records for moderation, support, or a deletion request. A report carries no name, phone number, or email address, but like every record in a public database it carries the opaque account identifier Apple assigns your device for this app, which other readers of that database can see.
- After 90 days HomeSafe stops displaying a community report and stops counting it toward any score. That is a rule the app applies on your device, not deletion: the record remains in Apple's public database until it is deleted. You can delete any report you submitted at any time in Settings → Privacy & Data → My flags, which removes it from the shared map as well as from your device; you can also write to us to have one removed.
- **Guardian Live-Link publishing is disabled in this build**, so the app cannot create a live share, working link, or active tracking session; the rest of this clause is what applies if it is re-enabled in a later release. If you choose to share a Guardian Live-Link with someone you trust during a trip, your live coordinate, ETA, distance, score, transport, and destination label are published to a public Apple CloudKit record — keyed by an unguessable per-trip token in the URL fragment, carrying no name, phone, home address, or saved place — only while that trip is active. Your location data is deleted from the record the moment you arrive — a brief, non-locating "arrived" confirmation remains so your recipient sees you made it, removed the next time the app runs — and the record is deleted entirely when you end the trip or tap Stop sharing. Sharing stops after six hours in any case, and any deletion the app could not complete in the moment is completed the next time the app runs.
- You can view, export, or delete your on-device data at any time in Settings → Privacy & Data, and revoke location access in iOS Settings. See our [Privacy Policy](/privacy/) for full data-handling and regional-rights details.

## Community reports — acceptable use

Community reports exist to warn people about conditions on the ground. When you submit one, you agree that:

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
