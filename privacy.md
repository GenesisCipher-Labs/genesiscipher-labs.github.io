---
title: HomeSafe Privacy Policy
permalink: /privacy/
---

# HomeSafe Privacy Policy

Last updated: August 26, 2026

GenesisCipher Labs Private Limited, a company incorporated in India ("GenesisCipher Labs", "we", "us"), builds HomeSafe, a route-choice and location-sharing aid distributed through the **United States App Store**. Its in-app travel coverage includes San Francisco, the Peninsula & South Bay, New York City, Los Angeles, Delhi NCR, Mumbai, Bengaluru, Pune, and Hyderabad; those India references describe travel coverage, not an Indian App Store listing. This policy applies wherever HomeSafe is used. Privacy is the architecture, not a footnote: most processing happens on your device, and we do not operate an application backend that receives your private routes, contacts, trip history, or continuous location. Community reports are the explicit exception described below: records you choose to submit go to Apple's public CloudKit database. This policy explains exactly what is processed, where it goes, and the privacy choices available to you, including rights that may apply under India's **Digital Personal Data Protection Act, 2023 (DPDP Act)** and California law.

> HomeSafe is decision support, not a guarantee of safety, and it never contacts emergency services for you. See our [Terms & Emergency Services Disclaimer](/terms/).

## The short version

- Your continuous location, private routes, trip history, saved places, contacts, and AI Bestie conversations are processed and stored **on your device**, subject to the direct provider requests and deliberate community-report submission described below.
- GenesisCipher Labs does not ingest that private on-device data into a company-operated server. We do not run analytics servers, ad networks, or trackers, and we do not sell personal data.
- Four provider groups receive requests from the app, and only to deliver a feature you asked for: (1) **Apple** (Maps directions and points of interest, reverse geocoding, weather near your route's start and end, and the community-reports sync), (2) the **US National Weather Service** for active official alerts using fixed county codes, (3) **DataSF** for a city-wide delayed dispatch feed in San Francisco, and (4) **511 SF Bay** for current service alerts from your Bay Area market's transit operators. The NWS, DataSF, and 511 requests contain no user coordinate, account identifier, destination, or route. **Public Overpass and NYC Open Data requests are disabled in this build**, as are Open-Meteo local-conditions requests and Guardian Live-Link publishing.
- **Community safety reports** you choose to submit are shared with other HomeSafe users by design. Records go directly from your device to Apple's **public CloudKit** and are not copied into a GenesisCipher Labs-operated server. GenesisCipher Labs can access and remove those public records for moderation, support, or a deletion request. They carry no name, phone, or email — but, like every record in a public database, they carry the opaque account identifier Apple assigns your device for this app. After 90 days the app stops showing and stops scoring a report, but the record stays in Apple's database until it is deleted. **You can delete any report you submitted at any time** in Settings → Privacy & Data → My flags.
- **Guardian Live-Link publishing is disabled in this release.** The app cannot create a live share or link. If it is re-enabled in a later release, the opt-in flow and data handling described in the dedicated section below would apply.
- You can view, export, and delete your on-device data at any time in **Settings → Privacy & Data**, and revoke location access in iOS Settings.

## Who is the data controller

GenesisCipher Labs Private Limited is the data fiduciary / controller for the limited processing described here. Because almost all processing happens on your device, your device — and the platform providers below acting as processors — do most of the work. Contact for privacy questions, data-rights requests, and grievances (including the grievance contact required under the DPDP Act): **genesiscipherlabs@gmail.com**.

## What we process and why

| Data | Where it is processed | Why | Permission or purpose |
|---|---|---|---|
| Precise location (GPS) | On your device; selected coordinates are sent directly to Apple for Maps, reverse geocoding, and route-adjacent weather as described below | Plan and score routes, determine day/night, show the map, reverse-geocode the area name, detect off-route drift and arrival during a trip | Your consent via the iOS location permission, for the specified purpose for which you voluntarily provided the data |
| Trusted contacts (name, phone) | On your device | Only to open your system Messages composer when **you** choose to share your location | Your consent / the specified purpose you voluntarily provided the data for |
| Trip journal, recent places, saved Home/Work | On your device | Convenience and your private history (never uploaded) | The specified purpose you voluntarily provided the data for |
| Personal learning profile (aggregate walking pace, travel-time error and a bounded set of recent dimensionless ETA residuals by travel mode/time band, travel rhythm, coarse place familiarity, and check-in responsiveness) | On your device | Adapt walking estimates, show a private planning allowance after enough comparable arrivals, time overdue nudges more realistically, and explain your own patterns. It never changes a route's safety score and stores no route, endpoint, timestamp, or trip identifier in the ETA residual buckets | The specified purpose you voluntarily provided the data for |
| Apple Watch action delivery ledger (random request identifier, check-in/help action, received and handled times; retained for at most seven days) | On your Apple devices | Recover a queued wrist action after process death and prevent duplicate WatchConnectivity deliveries from applying it twice; included in Export and Delete all | The specified purpose you voluntarily provided the data for |
| Community safety reports (category, coordinate, time, plus the opaque creator identifier Apple stamps on every public record) | Apple **public** CloudKit | Warn other users about on-ground conditions (poor lighting, waterlogging, no transport, etc.); the creator identifier lets the app count *distinct* authors on device, so repeat submissions from one person cannot manufacture agreement | Your consent each time you submit |
| The optional note you may add to a report | On your device | Your own reminder of what you saw. **It is not published** — see below | The specified purpose you voluntarily provided the data for |
| Guardian Live-Link (disabled in this release; future behaviour only: live coordinate, ETA, distance, score, transport, destination label) | If re-enabled: Apple **public** CloudKit, keyed by a per-trip unguessable token; viewed by your recipient in any browser at `genesiscipher-labs.github.io/track/` | If re-enabled: let a person you trust watch you reach your destination, without needing the app, only while a trip is active | If re-enabled: your specific consent each trip — minted only when you tap **Share live** and **send** the iMessage; location data deleted on arrival (a brief, non-locating "arrived" marker remains), the whole record on stop/end; sharing stops after 6 hours |
| Motion & Fitness data during live walking trips (measured steps and pace) | On your device | Show measured steps, detect pace or declared-transport mismatches, improve on-device walking estimates, and support automatic pace-based Drink Mode signals | Your consent via the iOS Motion & Fitness permission; a trip still works if you deny access |
| Speech, when you tap the mic button in the AI Bestie chat | On your device | Transcribe what you say into a typed question for the Bestie | Your consent via the iOS microphone and speech-recognition permissions |

During a live walking trip, HomeSafe uses Apple's Motion & Fitness data on your device to show measured steps, detect pace or declared-transport mismatches, improve on-device walking estimates, and support automatic pace-based Drink Mode signals. HomeSafe does not persist a raw motion history or upload motion readings. A final measured step count can remain briefly in the on-device trip summary; other live sensor state is cleared at trip end. If Motion & Fitness access is denied or unavailable, the trip continues using GPS-derived pace and estimated steps. One aggregate mean pace observation from a sufficiently sampled walking trip may update the on-device personal learning profile's pace mean, variability, and walking-trip count; that profile is included in Export and Delete all. Route wandering is derived from live route location, not Motion & Fitness data.

Voice input begins only after you tap the microphone button. It stops when you tap it again, leave Safety Bestie, the app becomes inactive or enters the background, recognition returns a final result, or recognition ends because of an error or interruption. Speech is transcribed **on your device** using Apple's on-device speech recognition. Audio is processed transiently for recognition; HomeSafe does not save or upload the audio or transcript. If on-device speech recognition is not available, the microphone button is not shown.

We do **not** process special-category data, we do **not** profile you for advertising, and we do **not** make solely-automated decisions producing legal effects. Safety scores are heuristics shown to you for your own decision; they are not a judgment about you.

## Who else receives data (processors and third parties)

- **Apple Inc.** acts as our processor and/or an independent controller for: MapKit directions and points-of-interest search, reverse geocoding, Apple WeatherKit (weather near your route, used to flag conditions like heavy rain), and CloudKit (the public database that broadcasts community reports). These requests are made directly from your device to Apple under Apple's privacy terms rather than through a GenesisCipher Labs-operated intermediary. We do not ingest the Maps, geocoding, or WeatherKit results into a company server. Community-report records remain accessible to GenesisCipher Labs for moderation, support, and deletion requests as described above.
- **OpenStreetMap / Overpass API is disabled in this build.** HomeSafe retains OSM attribution for cited, bundled OSM-derived street and transit facts. The public Overpass route-corridor adapter cannot serve a cache or send a request unless a production-approved backend passes the source review. In this build no route geometry, account identifier, or request metadata is sent to an Overpass host.
- **Open-Meteo local-conditions requests are disabled in this build.** The app contains a fail-closed integration for local temperature, air quality, and rain outlook, but it cannot make an Open-Meteo request unless a commercially licensed customer endpoint and credential are deliberately configured in a future build. Enabling it requires an updated disclosure; any such reading would remain display-only and never become a safety-score input.
- **US National Weather Service.** In each US launch city, the app requests active alerts for that city's fixed county zone codes — San Francisco County in San Francisco; Manhattan, the Bronx, Brooklyn and Queens in New York; Los Angeles County in Los Angeles; San Mateo, Santa Clara and Alameda in the Peninsula & South Bay. These codes are fixed values for the city and are identical for every user in it: the app sends no user coordinate, account identifier, destination, or route. Results are cached on device and are display-only.
- **DataSF.** In San Francisco, the app requests the city-wide public rolling dispatch feed filtered to open calls classified as fights. It sends no user coordinate, account identifier, destination, or route. The feed is delayed and a dispatch call is a reported event, not proof of what responders found. These records may produce an advisory and optional reroute; they never enter the route score. San Francisco is the only city where this request is made — no other launch market publishes a comparable current feed.
- **NYC Open Data (New York City DOT) is disabled in this build.** The retained adapter is designed to request city permit data using fixed borough codes and a date, then match permits to a route on device. The dataset's licence field is empty, however, and no retained primary production-use grant or counsel approval exists. The source gate therefore prevents both cached data and network access: no NYC permit request is made and no permit is displayed or scored.
- **511 SF Bay.** The 511 SF Bay service-alert integration is disabled in this build because no HomeSafe proxy endpoint is configured, so the app makes no 511 alert request. If a later build enables it, its legal and privacy disclosures must be reviewed before release.

- **CARTO and unpkg — the Guardian Live-Link page only, and only in your recipient's browser. The app does not cause either to be contacted in this build.** Guardian Live-Link publishing is switched off in this release (see the section below), so the app cannot create or share a working `/track/#<token>` link. The rest of this entry describes what would apply if sharing is re-enabled, and is kept here so that change would be visible rather than silent. When you share a live trip, the `/track/` page the recipient opens draws its map with OpenStreetMap data rendered by **CARTO**, and loads the open-source Leaflet mapping library from **unpkg**. Because that page follows the trip, their browser requests map tiles covering the area being watched: those requests carry the tile coordinates and their own IP address. They never carry the link token (it rides in the URL fragment, which browsers do not transmit, and the page sends no referrer), your destination label, or your safety score. **No request is made from your phone** — this is the only entry on this page describing something a recipient's device does rather than yours, and it happens only while a share is live.

Apple, the National Weather Service, DataSF, and 511 SF Bay are the complete list of third-party provider groups anything from the app reaches in this build. CARTO and unpkg remain described above because the checked-in, unreachable Guardian page references them, but Guardian publishing is off. The public Overpass, NYC Open Data, and Open-Meteo integrations are also disabled and receive no request. There are no advertising SDKs, no analytics SDKs, and no data brokers.

## Guardian Live-Link — how the live share works

**Publishing is disabled in this release.** The app cannot create a live share, so nothing described in this section is happening in the build you have: no public record, working share link, or active tracking session is created. The static tracking-page source remains published but has no trip record or token from this build to retrieve. It is documented here because the feature ships switched off and this is the behaviour that would resume — unchanged — if it is turned back on.

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

Apple's MapKit, reverse-geocoding, WeatherKit, and CloudKit services, plus the enabled civic providers listed above, may run on infrastructure outside your country. Those requests are made directly between your device and the respective provider under their own terms — we do not route them through or store them on a GenesisCipher Labs-operated server, and we do not initiate any additional cross-border transfer. The public community-report records we can access and remove remain in Apple's CloudKit. The disabled public Overpass, NYC Open Data, and Open-Meteo adapters make no request.

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

Data on your device is protected by iOS app sandboxing and device encryption. Community reports are hosted in Apple's public CloudKit database and have the access characteristics described above. GenesisCipher Labs holds no company-operated central database of your private routes, contacts, trip history, or continuous location; public community-report records remain accessible for moderation, support, and deletion. If a security issue affecting data we control arises, we will make any notifications required by applicable law.

## Changes

We will update this page when our practices change and revise the "Last updated" date. Material changes that affect on-device data handling are also reflected in the in-app terms you accept.

## Contact

GenesisCipher Labs Private Limited — **genesiscipherlabs@gmail.com**
