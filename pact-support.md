---
title: Pact Support
permalink: /pact/support/
---

# Pact Support

Email **[genesiscipherlabs@gmail.com](mailto:genesiscipherlabs@gmail.com)** and a human will reply.
Tell us your device, your iOS or macOS version, and — if it's about a figure Pact read — the wording
of the line it read it from. Never send us a real brand's contract; a paraphrase is enough.

Most questions we get are one of these.

---

## Tax and GST

### I'm not GST registered — can I use Pact?

Yes, and you're the majority of Pact's users. Leave the GSTIN field blank during setup. Your invoices
carry no GST, and Pact never asks which state the brand is in, because you charge nothing either way.

Your invoice is a **plain invoice**, not a "Bill of Supply". Rule 49 reserves that term for a
*registered* person making exempt or composition supplies, and it requires a supplier GSTIN — which
is precisely what you don't have.

### Why is Pact asking which state the brand is in?

Because GST's **place of supply** is the *recipient's* location (Section 12(2)(a), IGST Act), and it
decides whether you charge CGST + SGST or IGST. It cannot be worked out from your own state, and it
cannot be worked out from the currency.

Pact reads it automatically when the email contains a checksum-valid GSTIN. Otherwise it asks once
per brand and remembers the answer. It will not guess: an invoice that states a place of supply
nobody told it is a document asserting something untrue.

### The brand paid less than the invoice. Did they short-pay me?

Almost certainly not. Indian brands withhold **TDS** — usually 10% under Section 194J, calculated on
the *taxable value*, not the total — and remit it to the government against your PAN. The cash that
arrives is lawfully less than the invoice.

Long-press the deal → **Record payment…** → tick *TDS deducted*. Pact suggests the figure from the
invoice so you confirm rather than type it. Your outstanding then becomes invoiced − received −
withheld, and every reminder and follow-up quotes the real balance.

Chasing a brand for TDS they have already paid the government is accusing them of not paying it.
Pact is built not to let you do that by accident.

### Can I invoice a brand in dollars?

Yes — USD, EUR, GBP and AED, as well as rupees.

**The currency does not decide the tax.** An Indian agency paying you in USD is still a domestic
taxable supply. Only a recipient *outside India* makes it a zero-rated export. So Pact asks where the
brand is and never infers it from the currency.

The rupee equivalent prints only if you enter an exchange rate yourself. Rule 34 pins that rate to
the RBI reference rate for the date of supply, and Pact has no network connection of any kind — so
it leaves the line out rather than invent a number. A foreign-currency invoice also carries **no UPI
QR**, because UPI is domestic only.

---

## Your money and your data

### Three invoices? Really?

Three **for life** on the free tier — not three a month. *"Try a sample"* never spends one.

**Exporting your book and backing it up are free forever and will never be gated.** Pact holds the
only copy of a statutory record you're required to keep for around six years. "I can't get my data
out" is not something we will ever charge you to fix.

### Where is my data? Is it backed up?

On your device, in local storage. No account, no sign-in, no cloud, no tracking, and no network
requests of Pact's own.

Whether iCloud Backup covers an app-group container is not documented by Apple — which is exactly
why Pact carries its own backup instead of depending on the answer. In Settings, nominate a folder
once; Pact then writes a dated zip of your whole book into it, at most once a day. Dated, so backups
accumulate and one bad run can't destroy the last good copy. If that folder happens to live in
iCloud Drive or Dropbox, the *system* syncs it — Pact just writes a file.

Settings shows when the last backup ran, or why it failed. A backup that has quietly stopped is the
one failure worth being loud about.

### How do I get my invoices out?

Settings → **Export all invoices**. You get a single zip containing every invoice PDF, a
`ledger.csv` with one row per invoice, and a `tax-summary.csv` giving GST output tax by financial
year plus a TDS reconciliation. It's the pack your CA can open directly. Sample invoices are
excluded. It's free.

### I made a mistake — can I delete an invoice?

If you never shared it, it hasn't already been cancelled, no money or TDS is recorded against it, and
it holds the newest invoice number — then yes, it's deleted and the number is reused.

Otherwise Pact **voids** it. The invoice stays, keeps its number, prints a CANCELLED band on its own
face, and drops its payment QR. That's Rule 46(b): a serial number a brand is already holding cannot
be reissued to somebody else, and a document headed CANCELLED must not tell anyone how to pay it.

---

## Reading emails and getting paid

### The amount it read is wrong. Why is a field amber?

Amber means Pact isn't confident and wants you to look before you confirm. Tap the field and correct
it — nothing is ever created, sent or shared without your tap.

A blurry screenshot deliberately caps the money fields at amber even when the parser is otherwise
sure. A garbled digit on a tax invoice is the single failure this app is built to avoid, so Pact
would rather ask you twice than be confidently wrong once.

If Pact read a figure wrongly from clear text, please tell us the exact wording. That's the most
useful bug report we can get.

### Reminders aren't arriving.

Check that notifications are allowed for Pact — the app shows a "Reminders are off" banner when
permission has been denied. iOS allows only 64 pending notifications app-wide, so Pact gives every
deal its next reminder before any deal gets a second one; no deal goes unchased.

Snoozing a reminder never moves the **due date** on the invoice the brand is holding. It only moves
when Pact next nudges you.

---

## What Pact does not do

Pact is for one person invoicing brands for their own work. It is deliberately not a shop's billing
system, and if you need any of the following, Pact is the wrong tool and we'd rather you knew now:

- It does **not** file your GST returns, and does not connect to the GST portal.
- No e-invoicing or IRN generation.
- No e-way bills.
- No inventory, stock or counter billing.
- No staff logins or multi-user accounts.
- No bank feeds or automatic reconciliation.
- No expense tracking.
- No quotations, proforma invoices or credit notes.

Pact prepares the invoice, tracks the payment, chases it, and hands your CA a clean export. That's
the whole job.

---

## Still stuck?

**[genesiscipherlabs@gmail.com](mailto:genesiscipherlabs@gmail.com)** — we read everything.

- [Pact Privacy Policy](../privacy/)
- [Pact Terms of Use](../terms/)
- [About Pact](../)
