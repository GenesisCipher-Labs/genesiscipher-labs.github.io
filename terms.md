---
title: HomeSafe Terms & Emergency Services Disclaimer
permalink: /terms/
---

# HomeSafe Terms & Emergency Services Disclaimer

Last updated: August 14, 2026

HomeSafe ranks route options by publicly available safety signals, including Apple Maps points of interest, time of day, street-lighting data, weather, and user reports. HomeSafe is decision support. It is not a substitute for your judgement.

## What HomeSafe does not do

- HomeSafe does not contact emergency services on your behalf.
- HomeSafe does not relay, dispatch, or forward your location to 911, 112, 988, 1091, 1098, 181, or any other emergency or crisis line.
- HomeSafe does not have any commercial, technical, or government partnership with any emergency service.
- HomeSafe cannot verify that any call or message was received, read, or acted on.

## What HomeSafe does

- Surfaces the appropriate numbers for the supported region: in the United States, 911 plus national support lines and a verified local crisis line when location resolves to San Francisco, New York City, or Los Angeles; in India, 112 unified ERSS plus applicable support lines such as 1091, 1098, and 181.
- Opens the system Phone dialer with the number prefilled. You decide whether to place the call.
- Opens the system share sheet so you can pick a personal contact and send your current location via Messages, WhatsApp, or any other installed app. You decide whether to send.
- HomeSafe does not draft, address, or send any SMS to 911, 112, or any other emergency line. The only path from inside HomeSafe to an emergency number is the system dialler. Emergency services may support text contact in some places, including San Francisco's Text-to-911 and India's ERSS-112 distress channels. Text-to-911 availability is determined by the local public safety answering point, not HomeSafe. HomeSafe is not part of those systems and cannot verify receipt, response, or dispatch.

No safety app can guarantee your safety. Always trust your judgement and contact local emergency services directly when at risk. If you cannot use HomeSafe for any reason, dial the local primary emergency number directly using your phone — 911 in the United States or 112 in India.

HomeSafe is provided as-is. Scores and signals are heuristics derived from public and device-side data; they may be wrong. Do not rely on them in life-threatening situations.

## Data handling

- Route scores, safety signals, contacts, trip logs, recent and saved places, and AI Bestie conversations are processed and stored on your device only.
- HomeSafe's personal learning profile stays on your device. It keeps interpretable aggregates such as walking pace, travel rhythm, coarse place familiarity and check-in responsiveness, plus at most the latest 24 dimensionless ETA differences per travel mode and time band. Those timing values carry no route, endpoint, timestamp, or trip identifier. They can add a private planning allowance after enough comparable arrivals, but never change a route's safety score. The profile is included in Export and Delete all.
- When you use HomeSafe on Apple Watch, the phone keeps a bounded delivery ledger for up to seven days (a random request identifier, check-in/help action, and received/handled times). It exists only to recover queued actions and reject duplicates, stays on your Apple devices, and is included in Export and Delete all.
- GenesisCipher Labs operates no server that receives your location, routes, contacts, or trips, and does not sell or share personal data.
- If you tap the mic button in the AI Bestie chat, your speech is transcribed on your device using Apple's on-device speech recognition. The audio is never recorded, stored, or uploaded, and the transcription stays on your device like the rest of your Bestie conversation. If on-device speech recognition is unavailable, the mic button is not shown.
- Apple Maps and Apple Weather may be queried directly from your device for directions, points of interest, and weather near your route; a public OpenStreetMap (Overpass) service may be queried for street-lighting data near your route; and, in the US launch cities, the National Weather Service may be queried for that city's fixed county alert zones, 511 SF Bay for current service alerts from a Bay Area market's transit operators (Muni and BART in San Francisco; Caltrain, BART and VTA in Silicon Valley), in San Francisco only, DataSF for delayed city dispatch calls, and in New York only, NYC Open Data for the City's current sidewalk-work permits. Those civic-feed requests contain no user coordinate, destination, or route: the county zones, operator codes and borough codes are fixed values for the city, and which permits sit on your route is worked out on your device. Open-Meteo may be queried for the local temperature, air-quality index, and rain outlook, using only a coarse (roughly 11 km) coordinate cell rather than your position; that reading is shown to you and is never an input to a safety score. Those requests go to those providers, not to us.
- Community safety reports you choose to submit are shared with other HomeSafe users by design: they sync through a public Apple CloudKit database, are moderated, and are hosted by Apple — we never receive them. A report carries no name, phone number, or email address, but like every record in a public database it carries the opaque account identifier Apple assigns your device for this app, which other readers of that database can see.
- After 90 days HomeSafe stops displaying a community report and stops counting it toward any score. That is a rule the app applies on your device, not deletion: the record remains in Apple's public database until it is deleted. You can delete any report you submitted at any time in Settings → Privacy & Data → My flags, which removes it from the shared map as well as from your device; you can also write to us to have one removed.
- If you choose to share a Guardian Live-Link with someone you trust during a trip, your live coordinate, ETA, distance, score, transport, and destination label are published to a public Apple CloudKit record — keyed by an unguessable per-trip token in the URL fragment, carrying no name, phone, home address, or saved place — only while that trip is active. Your location data is deleted from the record the moment you arrive — a brief, non-locating "arrived" confirmation remains so your recipient sees you made it, removed the next time the app runs — and the record is deleted entirely when you end the trip or tap Stop sharing. Sharing stops after six hours in any case, and any deletion the app could not complete in the moment is completed the next time the app runs.
- You can view, export, or delete your on-device data at any time in Settings → Privacy & Data, and revoke location access in iOS Settings. See our [Privacy Policy](/privacy/) for full data-handling and regional-rights details.

By using HomeSafe, you acknowledge that HomeSafe is a routing and location-sharing aid, not an emergency-services intermediary.
