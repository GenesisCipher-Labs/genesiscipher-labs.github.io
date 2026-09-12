---
title: HomeSafe Privacy Policy
permalink: /privacy/
description: How HomeSafe handles data on Apple platforms.
---

# HomeSafe Privacy Policy

Last updated: September 12, 2026

This policy applies to HomeSafe on Apple platforms. GenesisCipher Labs Private Limited is the data controller.

> HomeSafe is decision support, not a guarantee of safety, and it never contacts emergency services for you. See our [Terms & Emergency Services Disclaimer](/terms/).

Data comes from information you enter or select and from device permissions and sensors you enable.

## visionOS journey-card edition

The current visionOS edition keeps only a destination draft or verified destination, travel mode, and departure choice in process memory. It does not request location, contacts, Motion & Fitness, microphone, or speech recognition; calculate a route or safety rating; start or monitor a live trip; submit a community report; or contact a weather, civic-data, or CloudKit provider. Its Membership tab shows HomeSafe's in-app purchases through Apple's own store interface, and Restore Purchases asks the App Store about purchases already made with your Apple Account; HomeSafe never sees your Apple Account credentials, Apple processes any purchase, and this edition unlocks no feature with a membership. When you verify a destination, HomeSafe sends the place query and a fixed search region for the selected city — never your device location or HomeSafe account — directly to Apple Maps, and accepts a result only inside that city's supported service area. The journey card is not written to persistent storage: clearing it removes it immediately, and otherwise it disappears when the app process ends. The route, communication, and data-control features described below apply to the iPhone, iPad, and Apple Watch editions unless a section says otherwise.

## Data handling

| Data | Use and location |
|---|---|
| Location, destinations and routes | Used for routing, trip progress, arrival, nearby conditions and safety information. Stored on your device. Necessary queries are sent directly to Apple Maps, geocoding and WeatherKit. |
| Contacts | A contact you select is used on your device to prepare a message that you decide whether to send. |
| Trips, saved places, chats and travel preferences | Used for app features and stored on your device. |
| Motion, visit and speech data | Used on your device for walking estimates, trip completion and optional voice input. HomeSafe does not retain raw motion, visit or audio histories. |
| Apple Watch delivery records | Used to deliver and deduplicate actions. Stored on your Apple devices for up to seven days. |
| Safety reports created in older versions | Category, location, time and an opaque Apple identifier may remain in Apple's public CloudKit database until deleted. New reports are not currently uploaded or used. |

HomeSafe also requests fixed regional public information from the US National Weather Service, DataSF, and the United States Geological Survey. Those requests do not include your location, route, destination or account identifier.

Apple receives the requests described above under its own privacy terms. A person or service receives data only when you deliberately share it using the system share sheet. GenesisCipher Labs does not operate a server that receives your routes, contacts, trip history or continuous location. We do not sell personal data or use advertising or analytics SDKs.

Any provider processing data for GenesisCipher Labs must protect it consistently with this policy and applicable law.

## Community reports

Community reporting is disabled in this build for all markets pending an authenticated Production `SafetyReport` schema, index, and role probe. Previously submitted records may remain in Apple's public CloudKit until deleted; author-deletion and GenesisCipher Labs moderation, support, and deletion-request controls remain available.

- **Community reporting is disabled in this build for all markets.** HomeSafe accepts no new report, does not fetch reports for product use, save a new submission, publish, display, or score reports, and sends no new `SafetyReport` record to CloudKit. Records submitted by an earlier build may remain in Apple's **public CloudKit** until deleted. Those records carry no name, phone, or email, but they may carry the opaque account identifier Apple assigned the submitting device for this app. GenesisCipher Labs can access and remove previously submitted records for moderation, support, or a deletion request. **You can delete any report you submitted at any time** in Settings → Privacy & Data → My flags. These deletion and moderation controls remain available while new reporting is disabled.

## Sensors and permissions

These describe exactly what each permission is used for, how long readings live, and what happens
if you decline. The route, communication, and data-control features here apply to the iPhone, iPad,
and Apple Watch editions.

### Location, including in the background

During a live trip, HomeSafe keeps receiving your location in the background so the trip continues while your screen is locked or you are in another app, and it asks iOS not to pause those updates while you wait somewhere. iOS shows its own background-location indicator whenever that is happening. HomeSafe requests only When In Use location access and never asks for Always access. Background updates are started when a trip starts and surrendered when it ends; the same background access runs while your car's CarPlay screen is showing the HomeSafe map, and is surrendered when that screen goes. A live trip also turns on Apple's visit monitoring, so iOS can tell HomeSafe you have settled somewhere for several minutes and the trip can finish on its own if the phone went into a pocket for the last few metres. Each reported visit is compared with your destination on this device and used for nothing else: HomeSafe keeps no visit history, adds no visit to your trip journal, and uploads no visit. Visit monitoring stops when the trip ends.

### Motion & Fitness

During a live walking trip, HomeSafe uses Apple's Motion & Fitness data on your device to show measured steps, detect pace or declared-transport mismatches, improve on-device walking estimates, and support automatic pace-based Drink Mode signals. HomeSafe does not persist a raw motion history or upload motion readings. A final measured step count can remain briefly in the on-device trip summary; other live sensor state is cleared at trip end. If Motion & Fitness access is denied or unavailable, the trip continues using GPS-derived pace and estimated steps. One aggregate mean pace observation from a sufficiently sampled walking trip may update the on-device personal learning profile's pace mean, variability, and walking-trip count; that profile is included in Export and Delete all. Route wandering is derived from live route location, not Motion & Fitness data.

### Microphone and speech recognition

Voice input begins only after you tap the microphone button. It stops when you tap it again, leave Safety Bestie, the app becomes inactive or enters the background, recognition returns a final result, or recognition ends because of an error or interruption. Speech is transcribed **on your device** using Apple's on-device speech recognition. Audio is processed transiently for recognition; HomeSafe does not save or upload the audio or transcript. If on-device speech recognition is not available, the microphone button is not shown.

### Personal learning profile

| Personal learning profile (aggregate walking pace, travel-time error and a bounded set of recent dimensionless ETA residuals by travel mode/time band, travel rhythm, coarse place familiarity, and check-in responsiveness) | On your device | Adapt walking estimates, show a private planning allowance after enough comparable arrivals, time overdue nudges more realistically, and explain your own patterns. It never changes a route's safety score and stores no route, endpoint, timestamp, or trip identifier in the ETA residual buckets. It also keeps an on-device per-region mean travel-time error and sample count; an existing aggregate may retain India or United States as its category, but current market availability is United States only. That regional aggregate carries no city, route, or timestamp. The whole profile is included in Export and Delete all | The specified purpose you voluntarily provided the data for |

### Apple Watch action delivery

Apple Watch action delivery records (random request identifier, check-in/help action, tap time, tap-time opaque privacy-generation token, opaque trip token for a check-in, delivery result, and received time) — stored on your paired apple watch for delivery and receipt recovery, and on your iphone after receipt. Recover a queued wrist action or its receipt after process death, keep a delayed check-in bound to the trip shown on the Watch, and prevent duplicate WatchConnectivity deliveries from applying it twice. A versioned action can affect the phone only if it arrives within five minutes of its tap time (with up to five seconds allowed for clock skew); a missing, malformed, stale, or farther-future time is review-only before any action record, check-in, or Help handoff is created. The Watch first keeps a bounded delivery-recovery copy with at most one record per action type; a copy bearing an older privacy-generation token is erased when a reset reaches the Watch, and removing the Watch app erases its local copy. An iPhone Export or Delete all covers only records the iPhone has received; a Watch-only copy cannot appear in an iPhone export. Readable records expire individually after seven days and are removed the next time that app executes its delivery ledger; unreadable Watch bytes use the same execution-time bound. A versioned tokenless cold-start request remains review-only and is removed under that bound

### Bundled city knowledge

City knowledge on iPhone and iPad includes separate, read-only bundled extracts of Overture Places and Overture Transportation, limited to the supported United States service areas. Mapped names, categories, locations and source-supplied addresses support local place and street lookup. These dated map records do not establish current opening hours, staffing, pedestrian access, incidents or safety, and never change route scores. City lookup runs on your device, makes no request to Overture or its contributors, and adds no stored search history. The city data source details offer the public data and its license notices for export without a membership; that export contains no personal searches or trips. The data retains its source licenses. Those permissions apply to the city data, not to the HomeSafe app software. Some curated place and street descriptions draw on Wikipedia articles, which are available under the Creative Commons Attribution-ShareAlike 4.0 licence; those descriptions are available under the same licence and the article used is cited beside each one. The bundled OpenStreetMap-derived street-lighting and camera survey is a Derived Database under the Open Database License 1.0 (© OpenStreetMap contributors); a copy of that database and the method used to build it are available on request at genesiscipherlabs@gmail.com.

### Civic data sources

Four provider groups receive requests from the app, and only to deliver a feature you asked for: (1) **Apple** (Maps directions and points of interest, reverse geocoding, weather near your route's start and end and — when a route is re-planned during a trip — near your current position, deletion requests for community-report records submitted previously, a one-time scrub that removes the free-text note from community-report records you submitted with an older version, and deletion of any live-trip share record left by an earlier build), (2) the **US National Weather Service** for active official alerts using fixed county codes, (3) **DataSF** for a city-wide delayed dispatch feed in San Francisco, and (4) the **United States Geological Survey** for its public worldwide catalog of recent magnitude-2.5-and-above earthquakes. The NWS, DataSF and USGS requests contain no user coordinate, account identifier, destination, or route. **511 SF Bay, public Overpass, and NYC Open Data requests are disabled in this build**, as are Open-Meteo local-conditions requests, all new community-report submission and product use, and Guardian Live-Link publishing.

- **Open-Meteo local-conditions requests are disabled in this build.** The app contains a fail-closed integration for local temperature, air quality, and rain outlook, but it cannot make an Open-Meteo request unless a commercially licensed customer endpoint and credential are deliberately configured in a future build. Enabling it requires an updated disclosure; any such reading would remain display-only and never become a safety-score input.

- **511 SF Bay.** The 511 SF Bay service-alert integration is disabled in this build because no HomeSafe proxy endpoint is configured, so the app makes no 511 alert request. If a later build enables it, its legal and privacy disclosures must be reviewed before release.

- **United States Geological Survey (USGS) — earthquakes.** In the US launch cities the app requests the USGS public summary feed of catalogued magnitude-2.5-and-above earthquakes from the past day. That request is a single fixed web address with no query parameters at all: it is byte-for-byte identical for every user of the app anywhere in the world, so USGS cannot tell from it which city you are in, let alone where you are. The whole worldwide answer is filtered to your city's fixed boundary **on your device**. USGS-authored data is stated by USGS to be in the U.S. Public Domain; USGS asks that proper credit be given, and the app carries that credit where the data is shown. A catalogued earthquake is a record of something that already happened: it is shown to you and can be discussed, and it never changes a route's safety rating.

### Guardian Live-Link page (recipient's browser only)

- **CARTO and unpkg — the Guardian Live-Link page only, and only in your recipient's browser. The app does not cause either to be contacted in this build.** Guardian Live-Link publishing is switched off in this release (see the section below), so the app cannot create or share a working `/track/#<token>` link. The rest of this entry describes what would apply if sharing is re-enabled, and is kept here so that change would be visible rather than silent. When you share a live trip, the `/track/` page the recipient opens draws its map with OpenStreetMap data rendered by **CARTO**, and loads the open-source Leaflet mapping library from **unpkg**. Because that page follows the trip, their browser requests map tiles covering the area being watched: those requests carry the tile coordinates and their own IP address. They never carry the link token (it rides in the URL fragment, which browsers do not transmit, and the page sends no referrer), your destination label, or your safety score. **No request is made from your phone** — this is the only entry on this page describing something a recipient's device does rather than yours, and it happens only while a share is live.

Apple, the National Weather Service, DataSF, and the United States Geological Survey are the complete list of third-party provider groups anything from the app reaches in this build. Links you choose to tap — a venue's website, a data source's licence page, the WhatsApp reach-home note, or a helpline number — open in Safari, in that app, or in the Phone app; those services see that request, and HomeSafe does not. Indian city packs are currently unavailable; no Indian civic, weather or transit feed is contacted in this build. CARTO and unpkg remain described above because the checked-in, unreachable Guardian page references them, but Guardian publishing is off. The 511 SF Bay, public Overpass, NYC Open Data, and Open-Meteo integrations are disabled and receive no request. There are no advertising SDKs, no analytics SDKs, and no data brokers.

## Retention and control

On-device data remains until you delete it in **Settings → Privacy & Data** or uninstall HomeSafe. Short-lived trip state expires automatically. Apple Watch delivery records expire after seven days. Older public safety reports remain until you delete them under **Settings → Privacy & Data → My flags** or ask us to delete them.

You can view, export or delete on-device data in the app. You can revoke location, contacts, motion, microphone, speech or notification access in system Settings. These controls also let you withdraw consent. Files or messages you choose to share are controlled by their recipients and the services you select.

## Who is the data controller, and your rights

GenesisCipher Labs Private Limited is the data fiduciary / controller for the limited processing described here. Because almost all processing happens on your device, your device — and the platform providers described above acting as processors — do most of the work. Contact for privacy questions, data-rights requests, and grievances (including the grievance contact required under the DPDP Act): **genesiscipherlabs@gmail.com**.

Depending on where you live, you may also have rights to access, correct, erase, restrict or obtain your personal data and to complain to a regulator. Email us to exercise any right involving data we can access or to raise a grievance.

- **Grievance / complaints:** email **genesiscipherlabs@gmail.com** — this is the grievance contact under the DPDP Act. You also have the right to lodge a complaint with the **Data Protection Board of India** once it is operational.

HomeSafe is not directed to children under 13. We use platform security protections and update this notice when our practices materially change.

Contact: GenesisCipher Labs Private Limited — [genesiscipherlabs@gmail.com](mailto:genesiscipherlabs@gmail.com)
