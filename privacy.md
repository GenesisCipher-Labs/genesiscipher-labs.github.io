---
title: HomeSafe Privacy Policy
permalink: /privacy/
---

# HomeSafe Privacy Policy

Last updated: June 17, 2026

GenesisCipher Labs ("we", "us") builds HomeSafe, a route-choice and location-sharing aid for five Indian metros (Delhi NCR, Mumbai, Bengaluru, Pune, Hyderabad). Privacy is the architecture, not a footnote: **HomeSafe runs on your device and we do not operate a server that receives your location, routes, contacts, or trips.** This policy explains exactly what is processed, where it goes, and the rights you have under the EU/UK General Data Protection Regulation (GDPR) and India's Digital Personal Data Protection Act, 2023 (DPDP Act).

> HomeSafe is decision support, not a guarantee of safety, and it never contacts emergency services for you. See our [Terms & Emergency Services Disclaimer](/terms/).

## The short version

- Your location, routes, trip history, saved places, contacts, and AI Bestie conversations are processed and stored **on your device only**.
- We, GenesisCipher Labs, **never receive** that data. We do not run analytics servers, ad networks, or trackers, and we do not sell or share personal data.
- Two kinds of requests leave your device, and only to deliver a feature you asked for: (1) requests to **Apple** (Maps directions and points of interest, reverse geocoding, optional weather, and the community-reports sync), and (2) a request to a public **OpenStreetMap (Overpass)** service for street-lighting data near your route.
- **Community safety reports** you choose to submit are shared with other HomeSafe users by design, through Apple's **public CloudKit** database. They carry no account or user ID, auto-expire after 90 days, and are moderated.
- You can view, export, and delete your on-device data at any time in **Settings → Privacy & Data**, and revoke location access in iOS Settings.

## Who is the data controller

GenesisCipher Labs is the controller for the limited processing described here. Because almost all processing happens on your device, your device — and the platform providers below acting as processors — do most of the work. Contact for privacy questions, data-rights requests, and grievances (including the grievance contact required under the DPDP Act): **genesiscipherlabs@gmail.com**.

## What we process, why, and the legal basis

| Data | Where it is processed | Why | GDPR legal basis |
|---|---|---|---|
| Precise location (GPS) | On your device | Plan and score routes, determine day/night, show the map, reverse-geocode the area name, detect off-route drift and arrival during a trip | Performance of the service you request (Art. 6(1)(b)); your consent via the iOS location permission (Art. 6(1)(a)) |
| Trusted contacts (name, phone) | On your device | Only to open your system Messages composer when **you** choose to share your location | Performance of the service / your consent |
| Trip journal, recent places, saved Home/Work | On your device | Convenience and your private history (never uploaded) | Legitimate interest (Art. 6(1)(f)) / performance of the service |
| Community safety reports (category, coordinate, time, optional note) | Apple **public** CloudKit | Warn other users about on-ground conditions (poor lighting, waterlogging, no transport, etc.) | Your consent each time you submit; our legitimate interest in a community safety layer |
| Optional motion data | On your device | Detect pace mismatch / wandering for the optional Drink-Safety mode | Your consent via the iOS motion permission |

We do **not** process special-category data, we do **not** profile you for advertising, and we do **not** make solely-automated decisions producing legal effects. Safety scores are heuristics shown to you for your own decision; they are not a judgment about you.

## Who else receives data (processors and third parties)

- **Apple Inc.** acts as our processor and/or an independent controller for: MapKit directions and points-of-interest search, reverse geocoding, optional Apple WeatherKit (only when enabled in a future build), and CloudKit (the public database that broadcasts community reports). These requests are made directly from your device to Apple under Apple's privacy terms. We never receive the underlying data.
- **OpenStreetMap / Overpass API.** To estimate street lighting along a candidate route, your device sends the route's coordinates to a public Overpass API endpoint. The Overpass host may log request metadata (such as IP address) per its own policies. Results are cached on your device for 24 hours. No account or identifier is sent.

We have no other third-party recipients. There are no advertising SDKs, no analytics SDKs, and no data brokers.

## Community reports, moderation, and defamation

Community reports are public by design — a poorly-lit corner one person flags should warn the next person. To keep them safe and lawful:

- Reports describe a **place and a condition**, never a verdict on a neighbourhood and never an accusation against an identifiable person or community. The app's content policy blocks notes that contain phone numbers, emails, links, slurs, hate speech, or generalisations about a community before they are published.
- You can **hide any report** you believe is false or abusive, and you can delete reports you authored.
- Reports automatically expire after 90 days, and we may remove reports that violate this policy.
- Reports carry no account or user identifier.

## International transfers

Apple and the Overpass host may process requests on infrastructure outside your country. Where this involves transfers from the EEA/UK, the relevant safeguards (such as Standard Contractual Clauses) are those maintained by Apple and the respective host. Because we do not receive or store your data on our own servers, we do not initiate any additional cross-border transfer.

## Retention

- On-device data (location use, trips, recents, saved places, contacts, Bestie chats) is kept only on your device and only until you delete it or uninstall the app. Active-trip resume data is discarded automatically a couple of hours after a trip.
- Community reports auto-expire after 90 days in CloudKit.

## Your rights

Under the GDPR (Arts. 15–22) and the DPDP Act, you can **access, correct, delete, export (port), object to, and restrict** processing, and **withdraw consent** at any time.

How to exercise them — most data never leaves your device, so you are in direct control:
- **View / export / delete everything:** open **Settings → Privacy & Data** in the app to see what is stored, export it as a file, or erase it in one tap.
- **Location & motion:** revoke or limit access in **iOS Settings → Privacy & Security**.
- **Your community reports:** delete them in-app; they also expire after 90 days.
- **Help or complaints:** email **genesiscipherlabs@gmail.com**. You also have the right to lodge a complaint with your data-protection authority (your EU/UK supervisory authority, or, in India, the Data Protection Board once operational).

## Children

HomeSafe is not directed to children. We do not knowingly process the personal data of a child without verifiable parental consent as required by the DPDP Act. If you believe a child has used the app, contact us and we will help you delete the data (which, being on-device, you can also clear directly).

## Security

Data on your device is protected by iOS app sandboxing and device encryption. Community reports in CloudKit are secured by Apple. Because we hold no central database of your personal data, there is no company server for an attacker to breach. If a security issue affecting users' data ever arises, we will notify affected users and the relevant authorities without undue delay, consistent with GDPR and the DPDP Act.

## Changes

We will update this page when our practices change and revise the "Last updated" date. Material changes that affect on-device data handling are also reflected in the in-app terms you accept.

## Contact

GenesisCipher Labs — **genesiscipherlabs@gmail.com**

*This policy describes HomeSafe's actual on-device behaviour. It is provided in good faith and should be reviewed by qualified counsel before publication in your specific jurisdiction.*
