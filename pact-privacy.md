---
title: Pact Privacy Policy
permalink: /pact/privacy/
---

# Pact Privacy Policy

Last updated: August 19, 2026

GenesisCipher Labs ("we", "us") builds Pact, an invoicing and payment-tracking app for creators and freelancers — it turns a brand-deal email into a professional tax invoice and tracks when you get paid. Privacy is the architecture, not a footnote: **Pact runs entirely on your device and we do not operate any server that receives your data.** This policy explains exactly what is processed, where it goes, and the rights you have under India's **Digital Personal Data Protection Act, 2023 (DPDP Act)** and, if you live elsewhere, under laws such as the **EU/UK GDPR** and the **California Consumer Privacy Act (CCPA)**.

## The short version

- Everything you put into Pact — your business profile (including PAN, GSTIN, bank account, UPI ID, address, logo and signature), your brands, deals, invoices, and payment records — is stored **on your device only**.
- We, GenesisCipher Labs, **never receive** that data. We run no servers, no analytics, no ad networks, and no trackers, and we do not sell or share personal data. Pact contains **zero third-party SDKs**.
- Deal details are extracted from pasted or shared text **on your device**, using Apple Intelligence (the on-device Foundation Models on supported devices) or an offline text parser. **Your email text is never sent to us or to any cloud AI service.**
- The **only** thing that leaves your device is your subscription purchase, handled directly by **Apple** through StoreKit. We never see your payment details.
- Payment reminders are scheduled **locally** on your device — there is no push server.
- You can view, edit, and delete any profile, brand, deal, invoice, or payment at any time inside the app.

## Who is the data controller

GenesisCipher Labs is the controller for the limited processing described here. Because effectively all processing happens on your device, your device — and Apple, acting as a processor for subscriptions — does the work. Contact for privacy questions, data-rights requests, and grievances (including the grievance contact required under the DPDP Act): **genesiscipherlabs@gmail.com**.

## What we process, why, and the legal basis

| Data | Where it is processed | Why | Lawful basis (DPDP Act) |
|---|---|---|---|
| Your business profile — legal name, tax registration numbers (GSTIN, VAT/tax registration number, PAN), registered address, email, phone, bank details (account name/number or IBAN, and your routing code — IFSC, sort code, BIC, ABA or BSB), UPI ID, business logo and signature image | On your device | To render invoices that identify you as the supplier | The specified purpose you voluntarily provided the data for |
| Brand / client records — name, tax registration number (GSTIN or VAT number), billing address, place-of-supply state, contact name, email, phone, notes | On your device | To address invoices and determine the correct tax treatment (Indian CGST+SGST/IGST/export, your own VAT/GST rate, or EU reverse charge) | The specified purpose you voluntarily provided the data for |
| Deal details — title, deliverables, amount, currency, payment terms, and the original pasted/shared text | On your device | To create the deal, generate the invoice, and let you re-extract if needed | Your consent when you paste or share the text |
| Invoices and payment records — invoice documents, tax breakup, supplier/brand snapshots, due dates, amounts, and paid/overdue status | On your device | To track who owes you what and when, and to keep each invoice reproducible | The specified purpose you voluntarily provided the data for |
| Local notification identifiers | On your device | To schedule and cancel payment reminders | Your consent via the iOS notification permission |

We do **not** profile you for advertising and we do **not** make solely-automated decisions producing legal effects. Extraction confidence scores are hints shown to you for your own review; you confirm every invoice.

## On-device AI

Pact can read a pasted or shared brand-deal email and pre-fill the deal for you. On supported devices this uses **Apple Intelligence** (Apple's on-device Foundation Models); on other devices it uses a built-in offline text parser. In both cases the text is processed **entirely on your device** and is never transmitted to us or to any third-party or cloud AI provider. Draft follow-up emails are generated the same way, and you edit and send them yourself — Pact never sends email on your behalf.

## How data enters Pact

- **Pasting or sharing text.** You can paste a deal email from the clipboard, or send it to Pact from another app (such as Mail or Gmail) using the iOS/macOS Share Sheet. Text shared to Pact is handed to the app through a private **App Group** container on your device (`group.com.genesiscipherlabs.Pact`) and is read and cleared by the app — it is never uploaded. A shared web link is stored only as text; Pact does not fetch it.
- **Typing it in.** You enter your profile and can edit any extracted field manually.

## How data leaves Pact — always because you sent it

Pact never transmits anything by itself. Everything below happens only when you tap something, and in each case you choose the destination:

- **Sharing an invoice.** You send the invoice PDF through the standard Share Sheet — to mail, a messaging app, Files, or by dragging it out on iPad and Mac. Where it goes and who receives it is entirely your choice, and it is then governed by whichever app or service you chose.
- **Exporting your book.** *Export all invoices* builds a zip — every invoice PDF, a CSV ledger, and a GST/TDS summary — and hands it to that same Share Sheet. It is assembled on your device and goes nowhere until you send it.
- **Folder backup.** If you nominate a backup folder, Pact writes a dated zip of that same pack into it, at most once a day. Pact only ever writes a file. **If the folder you choose sits inside iCloud Drive, Dropbox, Google Drive or a similar service, that service will sync the file under its own terms and privacy policy** — which is usually the point of choosing such a folder, but is worth choosing deliberately. Pick a purely local folder if you would rather nothing sync.
- **Payment and follow-up links.** A rupee invoice can carry a UPI QR code, and a follow-up can be sent over WhatsApp. Both are ordinary links built on your device from details you entered; opening one hands off to that app, which is then governed by its own terms. Pact contacts no payment gateway, takes no commission, and has no part in the payment itself.

## Who else receives data (processors and third parties)

- **Apple Inc.** processes your subscription purchase and entitlement through StoreKit, and stores invoice PDFs and the app database within the standard on-device app sandbox. If you have iCloud Backup enabled, your device backup — which may include Pact's data — is encrypted and stored by Apple under Apple's terms. We never receive any of this.
- **No one else.** There are no advertising SDKs, no analytics SDKs, no crash-reporting SDKs, and no data brokers. Pact makes no network requests other than Apple's StoreKit.

## Retention

Your data stays on your device until you delete it (per record, in-app) or uninstall the app. We hold nothing to retain or delete on a server, because we hold nothing.

## Your rights

Under the DPDP Act, you can **access, correct, update, erase, and grieve** the processing of your personal data, and **withdraw consent** at any time. Because your data never leaves your device, you are in direct control:

- **View / edit / delete:** open the relevant deal, invoice, brand, or your profile in the app and edit or delete it. Uninstalling the app removes all of it.
- **Notifications:** revoke or limit permission in **iOS/macOS Settings → Notifications**.
- **Grievance / complaints:** email **genesiscipherlabs@gmail.com** — this is the grievance contact under the DPDP Act. You also have the right to lodge a complaint with the **Data Protection Board of India** once it is operational.

## If you are outside India

Pact is available worldwide, and the architecture answers most jurisdictional questions the same way: **we receive no personal data, so there is no server-side processing, no cross-border transfer by us, and nothing for us to disclose, sell, or share.**

- **EU / EEA / UK (GDPR and UK GDPR).** GenesisCipher Labs does not collect or process your personal data on any server. The rights the GDPR gives you — access, rectification, erasure, restriction, portability, and objection — are all exercisable directly and immediately on your own device, because that is the only place the data exists: edit or delete any record in the app, or delete everything via *Settings → Delete all my data*. Nothing is transferred outside your country by us. If you believe we have processed your data unlawfully, you can contact us at the address below or lodge a complaint with your local supervisory authority.
- **California (CCPA/CPRA).** We do not collect, sell, or share personal information, and we have collected none in the preceding 12 months. There is nothing to opt out of and nothing to request deletion of from us — the data is on your device, under your direct control.
- **Everywhere else.** The same facts apply: your data stays on your device, and the controls in the app are how you exercise whatever rights your local law grants.

## Children

Pact is a professional invoicing tool and is not directed to children. We do not knowingly process the personal data of a child. Because all data is on-device, you can clear it directly at any time.

## Security

Data on your device is protected by operating-system app sandboxing and device encryption. Because we hold no central database of your personal data, there is no company server for an attacker to breach.

## Changes

We will update this page when our practices change and revise the "Last updated" date.

## Contact

GenesisCipher Labs — **genesiscipherlabs@gmail.com**
