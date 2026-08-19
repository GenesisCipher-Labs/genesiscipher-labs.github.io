---
title: Pact Support
permalink: /pact/support/
description: Answers to what Pact users actually ask — GST registration and place of supply, TDS and short payments, how the tax rate is set outside India, why EU reverse charge is not handled, backups and exports, and what Pact deliberately does not do.
---

# Pact Support

Email **[genesiscipherlabs@gmail.com](mailto:genesiscipherlabs@gmail.com)** and a human will reply.
Tell us your device, your iOS or macOS version, and — if it's about a figure Pact read — the wording
of the line it read it from. Never send us a real brand's contract; a paraphrase is enough.

Most questions we get are one of these.

*Last updated: 13 August 2026*

---

## Tax and GST — India

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

### Why did my invoice number restart?

Because the financial year rolled over on 1 April. Pact's numbering is financial-year-continuous —
`PACT/26-27/0001` — which is what Rule 46(b) asks for, and the counter resets when the year token
changes.

That token is pinned to a Gregorian calendar in IST, not to whatever calendar your phone is set to.
If it followed your device, switching your phone to a Buddhist or Hijri calendar and back would
change the token, reset the counter, and reissue a serial number a brand is already holding. That is
the one thing an invoice number exists to prevent.

---

## Tax outside India

### I'm not in India. What does my invoice look like?

Like an invoice from your own country, and nothing on it mentions India's tax code.

Six things are printed only on documents Indian GST actually governs, and all six are suppressed on
yours: the SAC tariff code, the Reverse Charge row, Place of Supply, the "GST — Not registered" row,
your state and PAN, and the Section 194J TDS footnote. The column headed "Taxable Value" on an Indian
invoice reads "Amount" on yours.

If you are registered for tax where you live and have entered your rate, you get a tax invoice
charging it. If you are not, you get a clean invoice with no tax line, headed **Invoice** rather than
**Tax Invoice** — because "Tax Invoice" is itself a claim about your registration status, and it is a
defined term with consequences in some countries.

### Why won't Pact fill in my VAT rate for me?

Because Pact would have to guess, and a guess here is a wrong figure on a statutory document.

Pact knows the *word*: that Germany calls it USt and its number a USt-IdNr, that France calls it TVA,
that the Netherlands calls it BTW. Those are stable facts about language. Being wrong about them
would be a cosmetic embarrassment.

The *rate* is a fact about current legislation in a country the app cannot see. Pact has no network
of any kind, so a built-in rate table would go stale the day a jurisdiction legislates and there
would be no way for the app to find out. So Pact knows the word and asks you for the number. You
enter it once during setup, or later in Settings › Your business.

This is the same reason Pact will not invent a rupee exchange rate: it knows what Rule 34 asks for
and it knows it cannot see the RBI reference rate, so it leaves the line out.

### What word will my tax line use?

Whichever one your clients expect. Pact knows the term for 31 countries:

| Term | Where |
|---|---|
| GST | India, Australia, New Zealand, Singapore, Malaysia, Canada |
| VAT | United Kingdom, Ireland, Poland, South Africa, UAE, Saudi Arabia, Bahrain, Oman |
| USt | Germany, Austria |
| TVA | France |
| IVA | Spain, Italy, Portugal |
| BTW | Netherlands |
| BTW/TVA | Belgium |
| MOMS | Sweden, Denmark, Norway, Iceland |
| ALV | Finland |
| MWST | Switzerland, Liechtenstein |
| Consumption tax | Japan |
| Sales tax | United States |

Anywhere else, the line reads **VAT**, which is the most widely correct default. If you have told
Pact no country at all, it reads the neutral **Tax**. A line reading "Tax @ 15%" is true everywhere;
a line naming somebody else's statute is not.

Your registration number gets its own label too — VAT no., USt-IdNr, No. TVA, NIF-IVA, Partita IVA,
BTW-nummer, MWST-Nr, ABN, GST number, GST reg. no., GST/HST no., TRN, EIN, or a neutral
"Tax registration no." where Pact doesn't have a specific one. The number is checked only where the
check is arithmetic rather than legislation: around twenty jurisdictions publish a real check digit
(the UK's mod-97 in both of its live variants, Germany's mod-11 chain, Australia's ABN, and so on),
and a number that fails its own checksum is refused — that is a typo worth catching before it prints
on a document your client reclaims tax against. A shape Pact doesn't recognise only warns, and a
jurisdiction it has no checksum for is accepted without comment, so a legitimately registered
creator is never blocked by a format Pact cannot check.

### I'm in the EU billing a business in another EU country. Does Pact handle reverse charge?

**Yes — provided Pact knows where your client is and that they are a business.**

For a cross-border B2B supply of services inside the EU, the place of supply is generally the
customer's country and the customer accounts for the VAT themselves — your invoice charges no VAT
and must carry wording saying the reverse charge applies, along with the customer's VAT number.

Pact does this. Put your client's country and VAT registration number on the brand record: the
registration number is what makes the supply B2B — that is Article 44's own test, never the currency
or the email domain — and the invoice then charges no VAT, prints the reverse-charge statement the
VAT Directive makes mandatory content (Article 226(11a)), and shows the client's number in the
Bill To block. The statement is frozen onto the invoice when it is issued, so a later edit to the
brand record can never silently add or remove statutory wording from a document your client already
holds.

Three edges, stated plainly:

- **If Pact does not know your client's country, it keeps charging your rate.** It never zero-rates
  on a guess: over-charging is correctable between the parties, while under-charging comes out of
  your own fee. Set the country on the brand before you confirm the deal.
- **The UK is not in the EU VAT area** — it has been a third country since 2021. A Dublin creator
  billing London, or a London creator billing Dublin, is treated as outside the scope of your VAT,
  not as an EU reverse charge, and the document is worded accordingly.
- **A VAT number that fails its check digit still counts as a business.** That is a typo, not
  evidence your client is a consumer, and refusing the reverse charge over it would charge tax that
  is not due.

### What if I'm registered but charge zero, or I'm not registered at all?

You get a plain invoice with no tax line, headed **Invoice**.

A stated rate of zero is not "registered at zero per cent" — it is you saying you charge none, and
Pact treats it that way. This matters more than it sounds: in Australia, "Tax Invoice" is a defined
term with consequences, so a document carrying that heading when you are not registered is a claim
about your ATO status that you did not intend to make.

### Which bank identifier will my invoice ask for?

The one a payer in your country looks for on the page:

| Field label | Where |
|---|---|
| IFSC | India |
| Sort code | United Kingdom |
| Routing number (ABA) | United States |
| BSB | Australia |
| Transit number | Canada |
| Bank/branch | New Zealand |
| Branch code | South Africa |
| BIC | The SEPA zone — Austria, Belgium, Bulgaria, Croatia, Cyprus, Czechia, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Iceland, Ireland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, Switzerland |
| SWIFT/BIC | Everywhere else |

In those SEPA countries and the UK, the account field is labelled **IBAN / account number** rather
than "Account number", because an IBAN is not "an account number" to a European accounts-payable
clerk — and asking for one by the wrong name is exactly how a creator supplies the short domestic
number that a cross-border transfer cannot use.

The fallback is SWIFT/BIC rather than a guess, because SWIFT is the one identifier that genuinely
works for an international transfer from anywhere.

### Which currencies can I invoice in?

44, covering Asia-Pacific, the Americas, Europe, the Middle East, Africa and South Asia. You can pick
any of them for any deal.

Three details that matter more than the count:

- **Each currency uses its own decimal rules.** A yen or won invoice shows no decimal places; a
  Kuwaiti, Bahraini or Omani dinar invoice shows three. Pact rounds to the currency's real minor
  unit rather than assuming two.
- **The amount in words uses the currency's own nouns** — "US Dollars and Cents", "Rupees and
  Paise", "Yen" — not rupee words with a different symbol in front.
- **Rupee amounts group the Indian way** (1,20,000), as do Pakistani and Sri Lankan rupees,
  Bangladeshi taka and Nepalese rupees. Everything else groups the way that currency is normally
  written.

Pact reads the currency out of the email where it can, but detection is a helpful default, not a
guarantee. A bare `$` written to a creator whose own currency also uses a `$` is deliberately turned
amber rather than assumed to be US dollars, and an email naming no currency at all falls back to
yours.

**The currency never decides the tax.** An Indian agency paying you in USD is still a domestic
taxable supply; only a recipient outside India makes it a zero-rated export. So Pact asks where the
brand is and never infers it from the money.

### Does Pact read emails in my language?

Partly, and it is worth being precise about which part.

Pact reads **payment terms** written in German, French, Spanish, Portuguese, Italian, Dutch, Polish
and Turkish — "Zahlungsziel 30 Tage", "paiement à 45 jours", "pagamento a 30 giorni". Before that it
read only English, so a European brand's stated terms fell through to a silent 30-day default and the
invoice printed a due date nobody had agreed.

The rest of the reading is English. The words Pact uses to tell a fee from a campaign budget, and to
recognise deliverables, are English. **Pact's interface is English only.**

If an email is in a language Pact cannot read, nothing breaks — the fields come back empty or amber
and you fill them in. Nothing is ever created without your tap.

### I moved country. What happens to my old invoices?

Nothing. That is deliberate.

An invoice freezes everything it prints at the moment it is issued: your name and address, your
registration number and its label, your bank details and *their* labels, the tax word, the country,
and the time zone the date of issue was written in. The PDF re-renders on demand long after the fact —
when you open the deal, when you upgrade, when you export your book — and if it read your live
profile instead, changing country would silently rewrite the tax face of invoices a brand is already
holding, under their original numbers.

So change your country, your bank, your logo or your tax registration freely. Everything you have
already sent stays exactly as it was. New invoices follow the new answer.

The one exception is your signature image, which is your own mark rather than a fact the brand acts
on, and is read live.

### Why is my invoice dated tomorrow / yesterday?

It shouldn't be any more. The date of issue is written in the document's own time zone, snapshotted
at issue — not the device's current one, and not a fixed Indian one.

Before that fix, an invoice raised in Los Angeles after about 11:30 in the morning printed
*tomorrow's* date, because the date was pinned to IST. The date of issue is the tax point, so that is
a future-dated document an accounts-payable system can reject and which files into the wrong year at
a year end.

Invoices issued from India stay pinned to IST wherever you happen to be standing.

---

## Your money and your data

### Three invoices? Really?

Three **for life** on the free tier — not three a month. *"Try a sample"* never spends one.

**Exporting your book and backing it up are free forever and will never be gated.** Pact holds the
only copy of a statutory record you're required to keep for around six years. "I can't get my data
out" is not something we will ever charge you to fix.

### What exactly is in Pact Pro?

Unlimited invoices; your own logo on the invoice and no "Made with Pact" line; zero-rated export
invoicing; and follow-ups rewritten in your own voice.

Two honest caveats. **Zero-rated export invoicing** is the Indian GST mechanism for supplying a
recipient outside India — it is what a GST-registered Indian creator needs, and it is not the same
thing as "billing in a foreign currency", which is available on the free tier. And **rewritten
follow-ups need Apple Intelligence**; on a device that doesn't have it, Pro gives you the same
offline template the free tier gets, and the paywall says so.

### Where is my data? Is it backed up?

On your device, in local storage. No account, no sign-in, no cloud, no tracking, and no network
requests of Pact's own.

Whether iCloud Backup covers an app-group container is not documented by Apple — which is exactly
why Pact carries its own backup instead of depending on the answer. In Settings, nominate a folder
once; Pact then writes a dated zip of your whole book into it, at most once a day. Dated, so backups
accumulate and one bad run can't destroy the last good copy. If that folder happens to live in
iCloud Drive or another synced folder, the *system* syncs it — Pact just writes a
file.

Settings shows when the last backup ran, or why it failed. A backup that has quietly stopped is the
one failure worth being loud about.

### Do my invoices sync between my iPhone, iPad and Mac?

No. One subscription covers all three devices, but each device holds its own separate book. There is
no iCloud sync and no account, because there is no cloud and no server.

Pact can export a book but it cannot import one, so a book cannot be moved onto a second device.
Export and backup keep a complete copy of everything you have issued, readable outside Pact — but
each device's Pact book is the one built on it.

### How do I get my invoices out?

Settings → **Export all invoices**. You get a single zip containing every invoice PDF, a
`ledger.csv` with one row per invoice, and a `tax-summary.csv` giving tax by the April–March
financial year — Pact's only grouping, wherever you invoice from — plus a TDS reconciliation. It's the pack your CA can open directly. Sample invoices are excluded. It's free.

Two things about that pack are worth knowing. Cancelled invoices are excluded from the tax figures,
and the sheet says so on its face — they stay in the ledger with their status, so nothing disappears.
And the summary never adds two currencies together: it reports one row per financial year *per
currency*, because a total made of dollars and rupees added up is not a quantity of anything.
Outside India the grouping is still April–March, so your accountant will regroup it to your own
tax year — every row in `ledger.csv` carries its invoice date, so that is a filter, not a rebuild.

### I made a mistake — can I delete an invoice?

If you never shared it, it hasn't already been cancelled, no money or TDS is recorded against it, and
it holds the newest invoice number — then yes, it's deleted and the number is reused.

Otherwise Pact **voids** it. The invoice stays, keeps its number, prints a CANCELLED band on its own
face, and drops its payment QR. That's Rule 46(b): a serial number a brand is already holding cannot
be reissued to somebody else, and a document headed CANCELLED must not tell anyone how to pay it.

Cancelling never writes off money that already arrived. It says no *further* money is coming; it
cannot un-receive what landed.

### Can I change a brand's contact after the first email?

Yes, and you should. Open the brand → Edit. You can set the contact person, the billing address, the
brand's own tax registration number, notes, and — the one that matters — the **email the chase goes
to**.

By default Pact writes to whoever sent the collaboration email. That is usually a marketing associate
who has no authority to release money. Accounts payable is a different desk, and pointing the
follow-up at it is often the whole difference between a payment landing and a thread going quiet.

---

## Reading emails and getting paid

### The amount it read is wrong. Why is a field amber?

Amber means Pact isn't confident and wants you to look before you confirm. Tap the field and correct
it — nothing is ever created, sent or shared without your tap.

A blurry screenshot deliberately caps the money fields at amber even when the parser is otherwise
sure. A garbled digit on a tax invoice is the single failure this app is built to avoid, so Pact
would rather ask you twice than be confidently wrong once.

Other things that deliberately turn amber rather than being asserted: a fee and a campaign budget
that score too closely to separate, a bare `$` where your own currency also uses one, a magnitude
word Pact cannot resolve, an equal 50/50 instalment split, and a price quoted per unit or as a range.
In each case Pact has a reading it thinks is likely and no basis to be certain.

If Pact read a figure wrongly from clear text, please tell us the exact wording. That's the most
useful bug report we can get.

### Can Pact read a screenshot or a PDF?

Yes. Text recognition runs on your device. Born-digital PDFs are read directly as text without
recognition at all; scans and screenshots go through recognition, capped at ten PDF pages.

When recognition quality is low, the amount, the currency, the due date **and the payment terms** are
all capped at amber. The payment terms matter as much as the date: on most briefs there is no due
date at all, and the invoice's due date is computed from the terms — so a blurry "Net 45" read as
"Net 15" would print a due date six weeks early with nothing on screen looking wrong.

Pact caps what it reads at 50,000 characters, cutting at a line break, and says so on screen when it
does.

### Reminders aren't arriving.

Check that notifications are allowed for Pact — the app shows a "Reminders are off" banner when
permission has been denied. iOS allows only 64 pending notifications app-wide, so Pact gives every
deal its next reminder before any deal gets a second one; no deal goes unchased.

Snoozing a reminder never moves the **due date** on the invoice the brand is holding. It only moves
when Pact next nudges you.

### Does Pact email the brand for me?

No. Pact **drafts** the follow-up; you send it.

Pact makes no network requests of its own and there is no server behind it, so it has no way to
send an email even in principle. You read the draft, edit it, and send it from your own mail app, share sheet or chat app.
Your payment details are attached beneath the draft as non-editable text, so the account number and
the pay link that leave your device are exactly the ones on the invoice.

---

## What Pact does not do

Pact is for one person invoicing brands for their own work. It is deliberately not a shop's billing
system, and if you need any of the following, Pact is the wrong tool and we'd rather you knew now:

- It does **not** file your GST returns, or any other return, and does not connect to any tax portal.
- No e-invoicing or IRN generation.
- No e-way bills.
- No inventory, stock or counter billing.
- No staff logins or multi-user accounts.
- No bank feeds or automatic reconciliation.
- No expense tracking.
- No quotations, proforma invoices or credit notes.
- No currency conversion and no exchange-rate lookup.
- No sync between your devices.
- English interface only.

Pact prepares the invoice, tracks the payment, chases it, and hands your accountant a clean export.
That's the whole job.

---

## Still stuck?

**[genesiscipherlabs@gmail.com](mailto:genesiscipherlabs@gmail.com)** — we read everything.

- [About Pact](../)
- [How to invoice a brand deal](../how-to-invoice-a-brand-deal/)
- [Pact FAQ](../faq/)
- [Pact Privacy Policy](../privacy/)
- [Pact Terms of Use](../terms/)
- [Download Pact on the App Store](https://apps.apple.com/app/id6790888314)
