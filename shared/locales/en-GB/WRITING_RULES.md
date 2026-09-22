# Writing Rules — `en-GB` (English — United Kingdom)

> Source-of-truth file for the `en-GB` writing rules. Lives under
> `shared/locales/en-GB/` per the architecture in
> [`../README.md`](../README.md).

## A. Purpose and scope

Defines how `prompt-workflow-os` produces user-facing content in British
English. Covers UK spelling, date / number / currency format, idioms,
formal register conventions.

Does not cover:

- US / Australian / Canadian English conventions (use en-US / etc.).
- Bypassing AI detection or removing watermarks (see section K).

## B. Automatic activation rules

The router activates the `en-GB` layer when **all** hold:

1. User requested output in English, **or** explicitly named United
   Kingdom as target market.
2. UK signal present: explicit UK locale name, UK spellings in user
   input, or "British English" / "UK English" request.
3. Selected workflow's `localization.supported_locales` includes
   `en-GB`, or category default applies.

Default to `en-US` when the user just says "English" without
qualification, because most global English training data is US-flavored
and `en-US` is the safer default.

## C. Input vs output vs target market

| Input | Output | Target | Action |
| --- | --- | --- | --- |
| English (UK) | English | UK | Load `en-GB`. |
| English (UK spellings) | English | unspecified | Likely `en-GB`; ask if ambiguous. |
| English (US) | English | unspecified | Default to `en-US`. |
| English | English | UK (explicit) | Load `en-GB`. |
| Any | English | non-English | Skip en-GB. |

## D. Protected content

Same as other locale layers:

- Code, identifiers, URLs, brand names.
- Direct quotations, citations, regulatory disclosures.
- Numbers, units, currency, dates.
- Required technical or legal wording.

## E. British English guidance

### E.1 Spelling

Default UK spellings (vs US):

| UK (default) | US | Notes |
| --- | --- | --- |
| organisation | organization | -ise / -yse endings: realise, analyse |
| colour | color | -our: behaviour, favour, honour |
| centre | center | -re: theatre, fibre, litre |
| metre | meter | -re |
| modelled | modeled | double consonant for verbs ending in stressed -l |
| travelled | traveled | same pattern |
| cancelled | canceled | same pattern |
| defence | defense | -ce |
| licence (n.) / license (v.) | license | UK requires noun / verb distinction |
| grey | gray | -ey vs -ay |
| mum | mom | |
| biscuit (food) | cookie | UK biscuit = US cookie |
| flat | apartment | |
| lift | elevator | |
| petrol | gasoline | |
| lorry | truck | |
| chips | fries | |
| football | soccer | UK football = soccer |
| autumn | fall | |
| got | gotten | past participle |
| dialogue | dialog | -gue |
| catalogue | catalog | -ue |
| programme (n.) | program | -mme for noun sense |
| sceptic | skeptic | -sc- |
| pyjamas | pajamas | |
| manoeuvre | maneuver | -oeu- |
| moustache | mustache | |

See [TERM_GLOSSARY.md](TERM_GLOSSARY.md) section 1 for the full
table.

### E.2 Quotation marks

- Use single quotes `' '` for direct speech and emphasis in body
  text (UK convention).
- Use double quotes `" "` for nested quotes inside single quotes.
- Use straight ASCII quotes in technical writing; curly quotes in
  narrative.

### E.3 Numbers, dates, currency

- Currency: `£` symbol before number; no space between symbol and
  number (e.g. `£100`, `£1,000.00`). Use `GBP` in international
  contexts.
- Date: `DD/MM/YYYY` (e.g. `22/09/2026`). Avoid `MM/DD/YYYY` (US).
  Use ISO `YYYY-MM-DD` in technical documents.
- Time: 24-hour format common in business (`14:30`); 12-hour with
  "am/pm" in casual.
- Number separator: comma for thousands (e.g. `1,000`); period for
  decimal (`1.5`).
- Phone: `020 7946 0958` (London) or `01632 960123` (UK standard).

### E.4 Idioms and expressions

UK-specific idioms:

- "Whilst" (instead of "while" in formal writing).
- "Amongst" (instead of "among" in formal writing).
- "Fortnight" (two weeks).
- "Lift" instead of "elevator".
- "Flat" instead of "apartment".
- "Petrol" instead of "gas/gasoline".
- "Biscuit" (food) — UK biscuit = US cookie.
- "At the end of the day" (conversational).
- "Brilliant" (positive — US often uses "great").
- "Bespoke" (custom-made — common in UK).
- "Lorry" instead of "truck".
- "Chips" instead of "fries" (and "crisps" for US "chips").

Avoid US idioms like "take a rain check", "touch base", "circle back"
in formal UK writing.

### E.5 Honorifics and titles

- Mr / Mrs / Ms / Dr / Prof — without period (UK convention) in most
  style guides. Academic style: Dr Jane Smith, PhD (no period).
- "Esq." rarely used (more common in legal contexts).
- Military: Capt / Col / Gen (no period).

### E.6 Email and professional register

UK email is more formal than US email on average. Common conventions:

- Subject line: clear, action-oriented.
- Greeting: "Dear [Name]," (formal) or "Hi [Name]," (casual). UK
  business often defaults to "Dear" for first contact.
- Body: polite, more indirect than US style. Hedging is acceptable
  ("I wonder if...", "Perhaps we could...").
- Sign-off: "Yours sincerely," (when you know the name), "Yours
  faithfully," (when you don't), or "Kind regards," / "Best regards,"
  (less formal).
- Reply: keep professional; allow longer delays than US email
  culture typically expects.

### E.7 Formal letter register (more common in UK)

UK business letters follow established conventions:

- Sender's address top-right.
- Date below address.
- Recipient's address left.
- Salutation: "Dear Mr Smith," (with comma, not colon).
- Body: paragraphs, often with one main point per paragraph.
- Sign-off: "Yours sincerely," (named recipient) / "Yours faithfully,"
  (unnamed recipient).
- Signature above typed name.
- Encl. / cc at bottom.

This register is appropriate for legal letters, formal business
correspondence, and government communication. Email is typically less
formal but follows similar conventions.

## F. Channel-specific tone

| Channel | Profile | Notes |
| --- | --- | --- |
| LinkedIn (UK) | `en-gb-linkedin-professional` | achievement-focused, slightly more formal than US |
| Twitter / X (UK) | `en-gb-twitter-casual` | short, British humour OK |
| Email (B2B) | `en-gb-email-professional` | formal, polite hedging |
| Formal letter | `en-gb-formal-letter` | established conventions |
| Sales / landing | `en-gb-landing-page-clear` | direct, evidence-driven |
| Customer support | `en-gb-customer-support` | polite, specific action |
| Long-form article | `en-gb-long-form-article` | structured, citation-aware |
| General professional | `en-gb-friendly-professional` | fallback |

See [STYLE_PROFILES.md](STYLE_PROFILES.md) for full schema and
exemplars.

## G. AI-pattern reduction

Same rules as other locales:

- Three consecutive similar sentence structures.
- "In conclusion", "It's important to note", "delve into".
- Over-formal hedges (some acceptable in UK, but not when stacked).
- US buzzword leakage ("synergy", "leverage", "circle back").
- US idioms ("take a rain check" → use UK equivalent or remove).

## H. Editing intensity rules

Same as other locales:

- `none` — protect everything.
- `light` — minimal cleanup.
- `standard` — apply glossary + AI-pattern reduction.
- `strict_precision` — high precision, mandatory for legal / medical /
  financial / security / compliance.

The router auto-escalates to `strict_precision` for regulated content.

## I. Before-and-after examples

### I.1 Intensity: standard, channel: friendly-professional

**Before:** Our company does software development.

**After:** We build enterprise software for [industry].

### I.2 Intensity: standard, channel: linkedin-professional

**Before:** I am thrilled to announce that I have joined XYZ.

**After:** Delighted to share that I've joined XYZ as Head of
Marketing. Looking forward to building with this team.

(Note: "Delighted" reads as more natural in UK LinkedIn than
"Thrilled" / "Excited".)

### I.3 Intensity: light, channel: translation (US → GB)

**Before (US English):** "The organization has realized the color
scheme needs reorganizing."

**After (UK English):** "The organisation has realised the colour
scheme needs reorganising."

(Note: UK spellings throughout; preserve sentence structure.)

### I.4 Intensity: strict_precision, channel: research-precise

**Before:** Most users prefer this product.

**After:** Based on the 2025 user survey (n=1,247, 95% CI), 78% of
respondents indicated preference for [product] over [competitor].
The result applies to the [demographic] subsample.

### I.5 Intensity: standard, channel: email-professional

**Before:** Hi, can we hop on a call to discuss your product?

**After:**
```text
Subject: Introduction from [Company] — potential collaboration

Dear [Name],

I hope this finds you well. I'm writing from [Company], where we
help [target audience] with [specific outcome]. I've followed your
work at [their company] with great interest.

Would you be open to a 15-minute call in the coming weeks to explore
whether there might be a fit?

Kind regards,

[Your name]
[Title]
[Company]
```

(Note: formal opener ("I hope this finds you well"), hedging
("might be a fit"), formal sign-off ("Kind regards"). UK business
register.)

## K. Safety boundaries

Same as other locale layers:

- Does not claim to bypass AI detection, remove watermarks, or prove
  human authorship.
- Does not silently convert currency or units.
- Does not override user-recorded terminology.
- Default to neutral, factual phrasing on regulatory / political
  topics.

## L. Reference files

- [TERM_GLOSSARY.md](TERM_GLOSSARY.md) — UK / US spelling / idiom
  table.
- [STYLE_PROFILES.md](STYLE_PROFILES.md) — Style profiles.
- [QUALITY_CHECKLIST.md](QUALITY_CHECKLIST.md) — Quality gate.
- [`../SHARED_STYLE_PROFILE_SCHEMA.md`](../SHARED_STYLE_PROFILE_SCHEMA.md) —
  core schema.
- [`../zh-TW/README.md`](../zh-TW/README.md) — reference
  structure.

## M. Citations

Editorial principles borrowed from UK English style guides (The
Economist Style Guide, New Hart's Rules, Guardian / Observer style).
Specific citations TBD as the pack matures.

The pack does not claim any anti-detection or watermark-removal
capability.