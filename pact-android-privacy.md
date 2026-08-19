---
title: Pact for Android — Privacy Policy
permalink: /pact/android/privacy/
description: What Pact for Android processes, where it goes, and the one thing that does leave your device — Google's ML Kit diagnostics — stated plainly.
---

# Pact for Android — Privacy Policy

Last updated: August 17, 2026

GenesisCipher Labs ("we", "us") builds Pact, an invoicing and payment-tracking app for creators and
freelancers — it turns a brand-deal email into a tax invoice and tracks when you get paid. **Pact
stores your records on your device and we operate no server that receives them.** This policy
explains exactly what is processed, what leaves the device, and the rights you have under India's
**Digital Personal Data Protection Act, 2023 (DPDP Act)** and, if you live elsewhere, under laws
such as the **EU/UK GDPR** and the **California Consumer Privacy Act (CCPA)**.

> **This is the Android policy.** The iOS and macOS version of Pact is a different build with
> different components — it uses Apple Intelligence and Apple's StoreKit, neither of which exists
> here, and it does not contain the Google component described below. Its policy is at
> [/pact/privacy/](/pact/privacy/). Where the two differ, the difference is real, not editorial.

## The short version

- Everything you put into Pact — your business profile (including PAN, GSTIN, bank account, UPI ID
  and address), your brands, deals, invoices and payment records — is stored **on your device only**.
- We, GenesisCipher Labs, **never receive** any of it. We run no servers, no accounts, no logins, no
  advertising, no analytics of our own and no crash-reporting SDK, and we do not sell or share
  personal data.
- Deal details are read from pasted or shared text **on your device**, by a plain offline parser.
  Your email text is never sent anywhere.
- Reading a **screenshot** uses Google's ML Kit text recognition with a model **bundled inside the
  app**. Your image and the text recognised from it never leave your device.
- 🔴 **One thing does leave.** That Google component reports its own diagnostics to Google —
  device model, app version, a per-installation identifier, timings and error codes. **It never
  includes your invoice data, your screenshots or the text read from them.** It is described in full
  under *[The one thing that leaves your device](#the-one-thing-that-leaves-your-device)* below, and
  it is why Pact for Android holds the `INTERNET` permission.
- Pact for Android is **free**. There is no in-app purchase and no billing component, so no payment
  data of any kind is processed.
- Payment reminders are scheduled **locally**. There is no push server.

## Who is the data controller

GenesisCipher Labs is the controller for the limited processing described here. Because effectively
all processing happens on your device, your device does the work. Contact for privacy questions,
data-rights requests and grievances (including the grievance contact required under the DPDP Act):
**genesiscipherlabs@gmail.com**.

## What we process, why, and the legal basis

| Data | Where it is processed | Why | Lawful basis (DPDP Act) |
|---|---|---|---|
| Your business profile — legal name, PAN, GSTIN, registered address, email, bank account name/number/IFSC, UPI ID | On your device | To render tax invoices identifying you as the supplier | The specified purpose you voluntarily provided the data for |
| Brand / client records — name, tax registration, billing address, place-of-supply state, contact name, accounts-payable email, phone, notes | On your device | To address invoices and determine the correct GST treatment (CGST+SGST, IGST, or export) | The specified purpose you voluntarily provided the data for |
| Deal details — title, deliverables, amount, currency, payment terms, and the original pasted/shared text or screenshot | On your device | To create the deal, generate the invoice, and let you re-read it if needed | Your consent when you paste or share it |
| Invoices and payment records — invoice PDFs, tax breakup, supplier/brand snapshots, due dates, amounts, paid/overdue status | On your device | To track who owes you what, and to keep each invoice reproducible | The specified purpose you voluntarily provided the data for |
| Notification schedule entries | On your device | To schedule and cancel payment reminders | Your consent via the Android notification permission |

We do **not** profile you for advertising and we do **not** make solely-automated decisions producing
legal effects. Extraction confidence is a hint shown to you for your own review; you confirm every
invoice before it exists.

## The one thing that leaves your device

Pact includes **Google's ML Kit Text Recognition** so it can read a screenshot of a brand's message.
The recognition model ships inside the app and runs offline — **your screenshot and the text
recognised from it are never uploaded, to us or to anyone.**

However, the ML Kit component itself reports usage and diagnostic data to Google. Per
[Google's ML Kit Android data disclosure](https://developers.google.com/ml-kit/android-data-disclosure),
this includes:

- device information (manufacturer, model, OS version and build) and available ML hardware
  accelerators;
- application information (package name and app version);
- **identifiers**, including per-installation identifiers used for diagnostics;
- performance metrics such as latency;
- API configuration such as image format and resolution, plus event types and error codes.

Google states that this data is encrypted in transit over HTTPS and is not transferred by ML Kit to
third parties. **Google does not document any way for an app to switch this off**, so we cannot
honestly offer you a toggle for it; the only way to avoid it entirely would be to remove screenshot
reading from the app. We have chosen to keep the feature and tell you plainly instead. This is the
reason Pact for Android declares the `INTERNET` and `ACCESS_NETWORK_STATE` permissions, and the
reason the Google Play *Data safety* section for this app declares **Device or other IDs** and
**App info and performance** as collected for analytics and diagnostics — by Google, not by us.

To be unambiguous about the boundary: **no invoice, no amount, no client, no profile field, no email
text and no image ever forms part of that transmission.**

## How data enters Pact

- **Pasting or sharing text.** You can paste a brand's email, or send it to Pact from another app
  (Gmail, a messaging app) through the Android share sheet. The text is handed to Pact by the system
  and read on your device.
- **Sharing a screenshot.** Same share sheet, or picking an image inside the app. The image is
  decoded, read on-device, and not retained beyond the draft you are creating.
- **Typing it in.** You enter your profile and can edit any extracted field by hand.

## How data leaves Pact — always because you sent it

Apart from the ML Kit diagnostics described above, Pact transmits nothing on its own. Everything
below happens only when you tap something, and in each case you choose the destination:

- **Sharing an invoice.** You send the invoice PDF through the standard Android share sheet — to
  mail, a messaging app, Drive, Files, wherever you choose. Where it goes is entirely your choice,
  and it is then governed by whichever app or service you chose.
- **Exporting your book.** *Export* builds a pack — invoice PDFs, a CSV ledger and a GST/TDS summary
  — and hands it to that same share sheet. It is assembled on your device and goes nowhere until you
  send it.
- **Folder backup.** If you nominate a backup folder, Pact writes a dated zip into it, at most once a
  day. Pact only ever writes a file. **If the folder you choose is inside Google Drive, Dropbox,
  OneDrive or a similar service, that service will sync the file under its own terms and privacy
  policy** — usually the point of choosing such a folder, but worth choosing deliberately. Pick a
  purely local folder if you would rather nothing sync.
- **Payment and follow-up links.** A rupee invoice can carry a UPI QR code, and a follow-up can be
  sent over WhatsApp. Both are ordinary links built on your device from details you entered; opening
  one hands off to that app, which is then governed by its own terms. Pact contacts no payment
  gateway, takes no commission, and has no part in the payment itself.

## Who else receives data

- **Google LLC** receives the ML Kit diagnostics described above, and nothing else from Pact.
- **No one else.** There are no advertising SDKs, no analytics SDKs, no crash-reporting SDKs and no
  data brokers in this app.

## Android backup and device transfer

Pact sets `android:allowBackup="false"`. Your Pact records are therefore **excluded from Android's
automatic cloud backup and from device-to-device transfer** — they do not travel to Google Drive with
the rest of your phone. The trade is deliberate and you should know it: **if you lose the device, the
only copy is whatever backup pack you exported yourself.** Nominate a backup folder in Settings.

## Retention and deletion

Your records stay on your device until you remove them. You can delete any deal, brand, invoice or
payment inside the app at any time, and edit your profile freely. **Uninstalling Pact removes all of
it**, because there is no server copy to survive. We hold nothing to delete on your behalf; a
data-deletion request to us would find no data. Files you have already exported or shared are outside
Pact and must be deleted wherever you sent them.

## Your rights

Under the DPDP Act you have the right to access, correct and erase your personal data, and to
grievance redressal. Because Pact holds your data only on your device, you exercise access,
correction and erasure **directly in the app** — every field is editable and every record is
deletable. For anything else, including grievances, write to **genesiscipherlabs@gmail.com**.

**If you are outside India:** the same direct, on-device control is how you exercise your rights
under the EU/UK GDPR, the CCPA, or your own local law — access, rectification, erasure, portability
and objection are all in your hands, because your device is the only place your records exist and
we receive, sell and share nothing. The one transmission from the app — Google's ML Kit diagnostics,
described above — is Google's own processing under [Google's privacy policy](https://policies.google.com/privacy),
and never includes your records. You can also contact us at the address above, or lodge a complaint
with your local supervisory authority.

## Children

Pact is a business tool and is **not directed at children under 13**, and we do not knowingly process
children's data.

## Permissions Pact for Android requests, and why

| Permission | Why |
|---|---|
| `POST_NOTIFICATIONS` | To show your payment reminders. Decline it and the app still works; you just get no reminders. |
| `INTERNET`, `ACCESS_NETWORK_STATE` | Required by the bundled Google ML Kit component. Pact itself makes no network requests. |
| `RECEIVE_BOOT_COMPLETED`, `WAKE_LOCK`, `FOREGROUND_SERVICE` | Declared by Android's WorkManager and Google's data-transport libraries, which arrive as dependencies of ML Kit. |

Pact requests **no** location, contacts, camera, microphone, SMS or call-log permission, and does not
request `QUERY_ALL_PACKAGES`.

## Changes

If this policy changes materially we will update the date at the top and, where the change affects
what leaves your device, say so in the app's release notes.

*Questions: [genesiscipherlabs@gmail.com](mailto:genesiscipherlabs@gmail.com)*
