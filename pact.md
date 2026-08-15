---
title: Pact — Brand Deal Invoices
permalink: /pact/
description: Pact turns a brand's collaboration email into a proper tax invoice on your iPhone, iPad or Mac — GST with the correct CGST/SGST/IGST split in India, your own VAT, USt, TVA or GST if you are registered elsewhere — then tracks the payment and drafts the chase. Everything runs on your device.
---

# Pact — Brand Deal Invoices

Pact turns a brand's collaboration email into a proper tax invoice, tracks the
payment, and drafts the follow-up when it runs late. Everything happens on your
device — reading the email, the tax arithmetic, the PDF. There is no account, no
cloud, and no network connection of Pact's own.

Pact was built India-first and is now correct for creators in other countries
too. Which country you invoice from is the first thing Pact asks, and everything
downstream follows from that one answer.

[Download Pact on the App Store](https://apps.apple.com/app/id6790888314)

Pact runs on iPhone, iPad and Mac. One subscription covers all three.

*Last updated: 13 August 2026*

---

## What does Pact actually do?

Four things, in order.

1. **It reads the deal.** Paste the brand's email, share it in from Mail, take a
   screenshot of a DM, or hand it a PDF. Pact pulls out the brand, the fee, the
   currency, the deliverables, the payment terms and the due date.
2. **It issues the invoice.** A real A4 PDF with selectable text — not a
   screenshot — carrying a consecutive invoice number, the correct tax for where
   you invoice from, your bank details labelled the way your client's country
   labels them, and the due date.
3. **It tracks the payment.** Reminders arrive three days before the due date, on
   the day, and then one, seven and fourteen days after it.
4. **It drafts the chase.** When a payment is late, Pact writes the follow-up in
   one of three tones. You read it, edit it, and send it. Pact never sends
   anything by itself — it has no way to.

## Who is Pact for?

One person who is paid by companies for their own work: a creator, an influencer,
a UGC creator, a freelancer, a sole trader. Someone who invoices brands and
agencies rather than running a shop.

Pact is deliberately not accounting software. There is no inventory, no purchase
side, no staff logins, no bank feeds and no return filing. The
[support page](./support/) lists what Pact does not do, in full, because knowing
that before you install is worth more than a download.

## Does Pact work outside India?

Yes, and this is the part of the app that changed most recently.

- **You state your country once.** Pact then decides whether India's rules apply
  to your document at all. An invoice from London says nothing about India's tax
  code — no SAC tariff code, no place of supply, no reverse-charge row, no
  Section 194J footnote.
- **You state your own tax rate once, if you are registered.** Pact prints the
  tax at that rate and calls it by the right word: VAT, USt, TVA, IVA, BTW,
  MOMS, ALV, MWST, GST, or Sales tax, depending on where you are. It knows the
  word for 31 countries. Anywhere else the line reads VAT, which is the most
  widely correct default; only if you have named no country at all does it read
  the neutral Tax.
- **Pact never supplies the rate itself.** It knows Germany calls the tax USt; it
  does not claim to know what Germany charges this year. A rate table in an app
  with no network goes stale the day a jurisdiction legislates, and a stale rate
  is a wrong figure on a statutory document. So Pact knows the word and asks you
  for the number.
- **Your registration number is labelled properly** — VAT no., USt-IdNr, No. TVA,
  Partita IVA, ABN, TRN, GST/HST no., EIN and others.
- **Your bank details are labelled for your country.** Sort code in the UK, BSB
  in Australia, ABA routing number in the United States, transit number in
  Canada, BIC beside an IBAN across the SEPA zone, IFSC in India, SWIFT/BIC
  everywhere else.
- **44 currencies**, each with its own decimal rules and its own words. A yen
  invoice shows no decimals; a Kuwaiti dinar invoice shows three. The
  amount-in-words line reads "US Dollars and Cents", not "Rupees and Paise".

If you are not registered for tax anywhere, you get a clean invoice with no tax
line and the plain heading "Invoice" — because "Tax Invoice" is itself a claim
about your registration status.

## How deep does Pact go on Indian GST?

As deep as it needs to, and it is computed rather than typed.

- **CGST + SGST** for an intra-state supply, **IGST** for an inter-state one,
  **zero-rated** for an export under a furnished LUT, **IGST-paid** for an export
  without one, and a plain no-tax invoice if you are not registered.
- **Place of supply is the recipient's location** (Section 12(2)(a), IGST Act).
  Pact reads it from a checksum-valid GSTIN in the email, otherwise asks once per
  brand and remembers. It never infers it from your own state and never from the
  currency — an Indian agency paying you in dollars is still a domestic supply.
- **Invoice numbers are financial-year-continuous** and reset on 1 April, in the
  form `PACT/26-27/0001`. They are pinned to a Gregorian calendar in IST, so
  changing your phone's language cannot reissue a serial a brand already holds.
- **Section 170 rounding** on rupee invoices, to the nearest rupee.
- **TDS is arithmetic, not a form field.** When a brand withholds tax at source —
  usually 10% under Section 194J on the taxable value — record what landed and
  tick the box. Pact suggests the figure from the invoice, subtracts both the
  cash and the withholding from what you are owed, and re-aims the reminders at
  the new balance.
- **A scan-to-pay UPI QR** on every rupee invoice, once you have added your UPI
  ID. It is an offline `upi://` string with the payee, amount and invoice number
  already filled in. No gateway, no commission, no network.

## What happens when a payment is late?

Pact tells you, and then it writes the email.

Reminders fire at 10am your local time on a five-rung ladder: three days before
the due date, on the due date, then one, seven and fourteen days after. Each one
carries three actions you can use without opening the app — mark paid, draft a
follow-up, or snooze three days. Marking a payment paid from a notification
requires your face or your passcode.

Snoozing moves when Pact next nudges you. It never moves the due date on the
invoice the brand is holding.

The follow-up itself is a draft in one of three tones. Your payment details — the
UPI link and the bank line — are attached verbatim and cannot be reworded. You
send it from your own mail, share sheet or chat app.

## How does Pact read an email without sending it anywhere?

Two readers, and a third that checks them.

On a device with Apple Intelligence, Apple's on-device model reads the email
first. Everywhere else — and as a fallback everywhere — Pact's own offline parser
reads it. A third on-device check corroborates the money figure. Extraction never
hard-fails, and nothing is uploaded, because there is nothing to upload to.

**Anything Pact is not sure about turns amber and asks for a glance before you
confirm.** Two readers disagreeing about the amount turns it amber. A blurry
screenshot turns the money fields amber even when the parser is otherwise
confident. A currency written as a bare `$` in a country that writes its own
money with a `$` turns amber rather than being guessed at.

That is the design rule the whole app follows: where Pact was not told something,
it leaves it out rather than inventing it. No registration number it was not
given, no LUT endorsement it has no LUT for, no recipient's address it does not
know, no exchange rate it could not look up.

## What does Pact refuse to do?

- It does **not** file returns, and does not connect to any tax portal.
- No e-invoicing, IRN, e-way bills, GSTR filing.
- **No EU or UK reverse charge.** A creator outside India charges their own rate
  to every client regardless of where that client is. If your supply is one where
  the customer accounts for the tax, Pact's invoice will not say so, and you
  should not use it for that invoice.
- **No currency conversion.** Pact never adds two currencies together and never
  converts one into another. A rupee equivalent prints only if you type the rate
  yourself, because Rule 34 pins it to the RBI reference rate for the date of
  supply and Pact cannot see one.
- **No sync.** One subscription covers iPhone, iPad and Mac, but each device
  holds its own book. There is no iCloud sync, because there is no cloud.
- Pact's interface is English only.

## Is my data private?

There is no account, no sign-in, no cloud, and no network request Pact makes on
its own. Pact's App Privacy answer on the App Store is **Data Not Collected**.
There is no analytics SDK and no tracking of any kind. It works on a plane.

Getting your data out is free, and always will be. Export gives you one zip with
every invoice PDF, a `ledger.csv` with a row per invoice, and a `tax-summary.csv`
with tax grouped by the April–March financial year — Pact's only grouping,
wherever you invoice from — and a TDS reconciliation. Outside India your
accountant will need to regroup it to your own tax year; `ledger.csv` carries
every invoice date, so that is a spreadsheet filter rather than a rebuild. Backup lets you nominate a folder once, and Pact
drops a dated zip into it at most once a day. Neither is part of any
subscription. Pact holds the only copy of a record you are required to keep for
around six years, so "I can't get my data out" is not something we will ever
charge you to fix.

## What does it cost?

Free for life: your first three invoices. Trying a sample never spends one.

**Pact Pro** adds unlimited invoices; your own logo and no "Made with Pact" line;
zero-rated export invoicing for GST-registered Indian creators billing brands
abroad; and follow-ups rewritten in your own voice on devices with Apple
Intelligence. On a device without Apple Intelligence, Pro gives you the same
offline template the free tier gets.

Pact Pro is an auto-renewing subscription billed weekly, monthly, every three
months or every six months. Prices are shown in the app and on the App Store, in
your own currency. One subscription covers iPhone, iPad and Mac. Manage or cancel
any time in Settings › Apple Account › Subscriptions. Full billing terms are in
the [Terms of Use](./terms/).

## Requirements

iOS 26 or later, or macOS 26 or later. iPhone, iPad and Mac, as a universal
purchase.

---

## More

- **[How to invoice a brand deal](./how-to-invoice-a-brand-deal/)** — what goes
  on the invoice, what an accounts-payable team needs before it can pay you, how
  net terms work, and what to do when payment is late.
- **[Frequently asked questions](./faq/)**
- **[Support](./support/)** — GST registration, place of supply, TDS, foreign
  tax rates, bank identifiers, backups, and what Pact deliberately doesn't do.

Anything else: email
[genesiscipherlabs@gmail.com](mailto:genesiscipherlabs@gmail.com) and a human
will reply.

## Legal

- [Pact Privacy Policy](./privacy/)
- [Pact Terms of Use](./terms/)
