---
title: HomeSafe Privacy Policy
permalink: /privacy/
---

# HomeSafe Privacy Policy

Last updated: August 19, 2026

GenesisCipher Labs ("we", "us") builds HomeSafe, a route-choice and location-sharing aid for Delhi NCR, Mumbai, Bengaluru, Pune, Hyderabad, San Francisco, Silicon Valley, New York City, and Los Angeles. This policy applies wherever HomeSafe is offered, including India and the United States. Privacy is the architecture, not a footnote: **HomeSafe runs on your device and we do not operate a server that receives your location, routes, contacts, or trips.** This policy explains exactly what is processed, where it goes, and the privacy choices available to you, including rights that may apply under India's **Digital Personal Data Protection Act, 2023 (DPDP Act)** and California law.

> HomeSafe is decision support, not a guarantee of safety, and it never contacts emergency services for you. See our [Terms & Emergency Services Disclaimer](/terms/).

## The short version

- Your location, routes, trip history, saved places, contacts, and AI Bestie conversations are processed and stored **on your device only**.
- We, GenesisCipher Labs, **never receive** that data. We do not run analytics servers, ad networks, or trackers, and we do not sell or share personal data.
- Seven kinds of requests leave your device, and only to deliver a feature you asked for: (1) requests to **Apple** (Maps directions and points of interest, reverse geocoding, weather near your route's start and end, the community-reports sync, and the optional Guardian Live-Link publish below), (2) a request to a public **OpenStreetMap (Overpass)** service for street-lighting data near your route, (3) a request to the **US National Weather Service** for active official alerts, using the fixed county codes of the US city you are in, (4) a city-wide request to **DataSF** for open law-enforcement dispatch calls classified as fights, (5) a request to **511 SF Bay** for current service alerts from your Bay Area market's transit operators, and (6) in New York, a request to **NYC Open Data** for the City's current sidewalk-work permits. The NWS, DataSF, 511, and NYC Open Data requests contain no user coordinate, account identifier, destination, or route. (7) A request to **Open-Meteo** for the local temperature, air quality, and rain outlook, using only a coarse (roughly 11 km) coordinate cell.
- **Community safety reports** you choose to submit are shared with other HomeSafe users by design, through Apple's **public CloudKit** database. They are moderated and carry no name, phone, or email — but, like every record in a public database, they carry the opaque account identifier Apple assigns your device for this app. After 90 days the app stops showing and stops scoring a report, but the record stays in Apple's database until it is deleted. **You can delete any report you submitted at any time** in Settings → Privacy & Data → My flags.
- **Guardian Live-Link** (opt-in, per trip): if you tap "Share live" during a trip and **send the link** from the system Messages composer, your live coordinate, ETA, distance, safety score, transport mode, and destination *label* are published to a public Apple CloudKit record while the trip is active. The record is keyed by an unguessable 160-bit token (the secret link) and carries **no name, phone, home address, or saved place**. **Your location data is deleted from the record the moment you arrive** — what remains is a brief, non-locating "arrived" confirmation so your recipient sees you made it, removed the next time the app runs. **Ending the trip or tapping Stop sharing deletes the record entirely.** Sharing stops after 6 hours in any case, and a deletion the app could not complete in the moment (for example, offline) is completed on its next launch. Cancelling the composer publishes nothing.
- You can view, export, and delete your on-device data at any time in **Settings → Privacy & Data**, and revoke location access in iOS Settings.

## Who is the data controller

GenesisCipher Labs is the controller for the limited processing described here. Because almost all processing happens on your device, your device — and the platform providers below acting as processors — do most of the work. Contact for privacy questions, data-rights requests, and grievances (including the grievance contact required under the DPDP Act): **genesiscipherlabs@gmail.com**.

## What we process and why

| Data | Where it is processed | Why | Permission or purpose |
|---|---|---|---|
| Precise location (GPS) | On your device | Plan and score routes, determine day/night, show the map, reverse-geocode the area name, detect off-route drift and arrival during a trip | Your consent via the iOS location permission, for the specified purpose for which you voluntarily provided the data |
| Trusted contacts (name, phone) | On your device | Only to open your system Messages composer when **you** choose to share your location | Your consent / the specified purpose you voluntarily provided the data for |
| Trip journal, recent places, saved Home/Work | On your device | Convenience and your private history (never uploaded) | The specified purpose you voluntarily provided the data for |
| Personal learning profile (aggregate walking pace, travel-time error and a bounded set of recent dimensionless ETA residuals by travel mode/time band, travel rhythm, coarse place familiarity, and check-in responsiveness) | On your device | Adapt walking estimates, show a private planning allowance after enough comparable arrivals, time overdue nudges more realistically, and explain your own patterns. It never changes a route's safety score and stores no route, endpoint, timestamp, or trip identifier in the ETA residual buckets | The specified purpose you voluntarily provided the data for |
| Apple Watch action delivery ledger (random request identifier, check-in/help action, received and handled times; retained for at most seven days) | On your Apple devices | Recover a queued wrist action after process death and prevent duplicate WatchConnectivity deliveries from applying it twice; included in Export and Delete all | The specified purpose you voluntarily provided the data for |
| Community safety reports (category, coordinate, time, plus the opaque creator identifier Apple stamps on every public record) | Apple **public** CloudKit | Warn other users about on-ground conditions (poor lighting, waterlogging, no transport, etc.); the creator identifier lets the app count *distinct* authors on device, so repeat submissions from one person cannot manufacture agreement | Your consent each time you submit |
| The optional note you may add to a report | On your device | Your own reminder of what you saw. **It is not published** — see below | The specified purpose you voluntarily provided the data for |
| Guardian Live-Link (live coordinate, ETA, distance, score, transport, destination label) | Apple **public** CloudKit, keyed by a per-trip unguessable token; viewed by your recipient in any browser at `genesiscipher-labs.github.io/track/` | Let a person you trust watch you reach your destination, without needing the app, only while a trip is active | Your specific consent each trip — minted only when you tap **Share live** and **send** the iMessage; location data deleted on arrival (a brief, non-locating "arrived" marker remains), the whole record on stop/end; sharing stops after 6 hours |
| Optional motion data | On your device | Detect pace mismatch / wandering for the optional Drink-Safety mode | Your consent via the iOS motion permission |
| Speech, when you tap the mic button in the AI Bestie chat | On your device | Transcribe what you say into a typed question for the Bestie | Your consent via the iOS microphone and speech-recognition permissions |

The mic is used **only** while you hold the mic button in the Bestie chat. Speech is transcribed **on your device** using Apple's on-device speech recognition; the audio is never recorded, never stored, and never uploaded, and the transcription stays on your device like the rest of your Bestie conversation. If on-device speech recognition is not available, the mic button is not shown.

We do **not** process special-category data, we do **not** profile you for advertising, and we do **not** make solely-automated decisions producing legal effects. Safety scores are heuristics shown to you for your own decision; they are not a judgment about you.

## Who else receives data (processors and third parties)

- **Apple Inc.** acts as our processor and/or an independent controller for: MapKit directions and points-of-interest search, reverse geocoding, Apple WeatherKit (weather near your route, used to flag conditions like heavy rain), and CloudKit (the public database that broadcasts community reports). These requests are made directly from your device to Apple under Apple's privacy terms. We never receive the underlying data.
- **OpenStreetMap / Overpass API.** To estimate street lighting along a candidate route, your device sends the route's coordinates to a public Overpass API endpoint. The Overpass host may log request metadata (such as IP address) per its own policies. Results are cached on your device for 24 hours. No account or identifier is sent.
- **Open-Meteo** is queried for the local temperature, air quality, and rain outlook. The request carries only a coarse (roughly 11 km) coordinate cell, never your precise position, and never your destination, route, or any account identifier. The reading is display-only and is never an input to a safety score.
- **US National Weather Service.** In each US launch city, the app requests active alerts for that city's fixed county zone codes — San Francisco County in San Francisco; Manhattan, the Bronx, Brooklyn and Queens in New York; Los Angeles County in Los Angeles; San Mateo, Santa Clara and Alameda in Silicon Valley. These codes are fixed values for the city and are identical for every user in it: the app sends no user coordinate, account identifier, destination, or route. Results are cached on device and are display-only.
- **DataSF.** In San Francisco, the app requests the city-wide public rolling dispatch feed filtered to open calls classified as fights. It sends no user coordinate, account identifier, destination, or route. The feed is delayed and a dispatch call is a reported event, not proof of what responders found. These records may produce an advisory and optional reroute; they never enter the route score. San Francisco is the only city where this request is made — no other launch market publishes a comparable current feed.
- **NYC Open Data (New York City DOT).** In New York, the app requests the City's permitted street closures, filtered on the City's servers to sidewalk-affecting work that is currently permitted in the four boroughs HomeSafe covers. It sends no user coordinate, account identifier, destination, or route — the borough codes and the date are the whole request. Which permits sit on your route is worked out on your device. A permit records that work was authorised; it is not a report of a blocked pavement, and it never enters the safety score. The City publishes these data without warranty as to completeness or accuracy.
- **511 SF Bay.** In San Francisco and Silicon Valley, the app requests the service-alert feed for that market's transit operators — Muni and BART in San Francisco; Caltrain, BART and VTA in Silicon Valley. It sends the app's developer token and the operator codes, but no user coordinate, account identifier, destination, or route. Alerts support transit advice and never enter the safety score. 511 SF Bay is a Bay Area service, so this request is never made in New York or Los Angeles.

- **CARTO and unpkg — the Guardian Live-Link page only, and only in your recipient's browser.** When you share a live trip, the `/track/` page the recipient opens draws its map with OpenStreetMap data rendered by **CARTO**, and loads the open-source Leaflet mapping library from **unpkg**. Because that page follows the trip, their browser requests map tiles covering the area being watched: those requests carry the tile coordinates and their own IP address. They never carry the link token (it rides in the URL fragment, which browsers do not transmit, and the page sends no referrer), your destination label, or your safety score. **No request is made from your phone** — this is the only entry on this page describing something a recipient's device does rather than yours, and it happens only while a share is live.

Those nine — Apple, the Overpass host, Open-Meteo, the National Weather Service, DataSF, 511 SF Bay, NYC Open Data, CARTO, and unpkg — are our only third-party recipients in this build. There are no advertising SDKs, no analytics SDKs, and no data brokers.

## Guardian Live-Link — how the live share works

The Guardian Live-Link is opt-in, per trip, and built around three guarantees:

- **Nothing is published until you send.** Tapping "Share live" mints an unguessable 160-bit token and opens the system Messages composer with a link. Only if **you** tap **Send** in iMessage does HomeSafe begin publishing your live location. Cancelling the composer publishes nothing and the token is discarded.
- **The link is the secret.** The token rides in the URL **fragment** (`/track/#<token>`), so it never reaches our static-page host or any server log. The public CloudKit record is fetched by that token alone, by the recipient's browser, via Apple's CloudKit JS API.
- **Minimal data, automatic deletion.** The published record carries only: live coordinate, heading, ETA, remaining distance, safety score, transport icon, and your **destination label** (e.g. "home" or the place you typed). It never carries your name, phone, home address, or any saved place. By default it does **not** carry the destination's coordinate — only the label. The record's location data is deleted the instant you arrive — what remains is a non-locating "arrived" confirmation, removed the next time the app runs — and the whole record is deleted the instant you tap End trip or Stop sharing. Sharing stops after six hours in any case, and a deletion the app could not complete in the moment (for example, offline) is completed on its next launch. The link goes dark and the recipient sees an "ended" page — after an arrival, a "made it safe" confirmation.

The recipient can only watch — there is no reverse channel from the link back to you.

## Community reports, moderation, and defamation

Community reports are public by design — a poorly-lit corner one person flags should warn the next person. To keep them safe and lawful:

- Reports describe a **place and a condition**, never a verdict on a neighbourhood and never an accusation against an identifiable person or community.
- **The optional note you type is never published.** It stays on your device. What is shared is the category, the coordinate and the time — nothing you wrote in your own words. Earlier versions of the app did publish the note, and this page described that; the note was removed from the shared record because nothing in the app ever displayed it to anyone, which made it data collected for no purpose — and it was the one field that could carry a third party's personal information into a public database. The app still screens what you type (phone numbers, emails, links, slurs, hate speech, generalisations about a community) before storing it, so a note that would have been unlawful to publish is not kept either.
- **You can delete any report you submitted, at any time.** Open **Settings → Privacy & Data → My flags**: it lists what this device published — including older flags the app has already stopped displaying — and removing one deletes it from the shared map as well as from your device. Erasing all your data in the same screen deletes them too. There is currently **no in-app control to hide someone else's report**; if you believe a report is false or abusive, email us at **genesiscipherlabs@gmail.com** and we can remove it.
- **What "90 days" does, precisely.** After 90 days the app stops displaying a report and stops counting it toward any score. That is a rule applied by the app on your device — it is **not** deletion. The underlying record remains in Apple's public database, readable by the app, until someone deletes it: either its author (above) or us, on request. We say this plainly because the earlier wording — "reports expire automatically after 90 days" — described the app's behaviour as though it were the database's, and it is not.
- Reports carry **no name, phone number, or email address**. They do carry the account identifier Apple stamps on every record written to a public CloudKit database, which other readers of that database can see. It is an opaque value assigned by Apple, different for every app, and it cannot be used to look you up unless you have separately granted that app permission to discover you. The app reads it for one purpose — counting distinct authors so that several people flagging the same corner reads differently from one person flagging it several times — and stores it on your device only as a salted hash, so it does not appear in your data export in a form anyone could correlate.

## Where requests are processed

Apple's MapKit, reverse-geocoding, and CloudKit services run on Apple infrastructure that may be located outside your country; the public Overpass endpoint and other providers listed above may do the same. Those requests are made directly between your device and the respective provider under their own terms — we do not receive, store, or re-transfer the data on our own servers, and we do not initiate any additional cross-border transfer.

## Retention

- On-device data (location use, trips, recents, saved places, contacts, Bestie chats) is kept only on your device and only until you delete it or uninstall the app. Active-trip resume data is discarded automatically a couple of hours after a trip.
- Community reports are kept in Apple's public CloudKit database until they are deleted — by you, from **Settings → Privacy & Data → My flags**, or by us on request. There is no automatic server-side deletion: CloudKit does not expire records on a timer. The app independently stops displaying and stops scoring a report once it is 90 days old, but that is a display and scoring rule, not retention.

## Your rights

Under the DPDP Act, you can **access, correct, update, erase, and grieve** the processing of your personal data, and **withdraw consent** at any time. We will respond without undue delay and in any case within the timelines required by the Act once it is notified.

How to exercise them — most data never leaves your device, so you are in direct control:
- **View / export / delete everything:** open **Settings → Privacy & Data** in the app to see what is stored, export it as a file, or erase it in one tap.
- **Location & motion:** revoke or limit access in **iOS Settings → Privacy & Security**.
- **Your community reports:** delete them yourself in **Settings → Privacy & Data → My flags** — this removes them from the shared map, not just from your phone. They are not deleted by the passage of time, so use this control if you want one gone.
- **Grievance / complaints:** email **genesiscipherlabs@gmail.com** — this is the grievance contact under the DPDP Act. You also have the right to lodge a complaint with the **Data Protection Board of India** once it is operational.

### California privacy choices

California law may give residents rights to know or access personal information, request deletion or correction, opt out of sale or sharing for cross-context behavioural advertising, limit certain uses of sensitive personal information, and exercise those rights without discrimination. HomeSafe does **not** sell personal information, share it for cross-context behavioural advertising, use advertising SDKs, or use sensitive personal information for purposes outside the features described in this policy.

Most HomeSafe data never leaves your device, so the in-app View, Export, Delete all, My flags, and iOS permission controls are the fastest way to exercise those choices. For anything we can actually reach — such as a community report in public CloudKit — email **genesiscipherlabs@gmail.com**. You may use an authorised agent where applicable; we may ask for information needed to verify the request and the agent's authority. These disclosures do not expand the scope of any law that would not otherwise apply.

## Children

HomeSafe is not directed to children. We do not knowingly collect a child's personal data in a way that requires parental consent without obtaining that consent. If you believe a child has used the app, contact us and we will help you delete data we can reach; on-device data can also be cleared directly in the app or by deleting the app.

## Security

Data on your device is protected by iOS app sandboxing and device encryption. Community reports in CloudKit are secured by Apple. Because we hold no central database of your personal data, there is no company server containing that data for an attacker to breach. If a security issue affecting data we control arises, we will make any notifications required by applicable law.

## Changes

We will update this page when our practices change and revise the "Last updated" date. Material changes that affect on-device data handling are also reflected in the in-app terms you accept.

## Contact

GenesisCipher Labs — **genesiscipherlabs@gmail.com**

*This policy describes HomeSafe's actual on-device behaviour. It is provided in good faith and should be reviewed by qualified counsel before publication in your specific jurisdiction.*
