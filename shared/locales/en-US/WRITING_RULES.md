# Writing Rules — `en-US` (English — United States)

> Source-of-truth file for the `en-US` writing rules. Lives under
> `shared/locales/en-US/` per the architecture in
> [`../README.md`](../README.md).

## A. Purpose and scope

Defines how `prompt-workflow-os` produces user-facing content in US
English. Covers spelling, date / number / currency format, idioms,
and channel-specific tone for US audiences.

Does not cover:

- UK / Australian / Canadian English conventions (use en-GB / etc.).
- Bypassing AI detection or removing watermarks (see section K).

## B. Automatic activation rules

The router activates the `en-US` layer when **all** hold:

1. User requested output in English, **or** explicitly named United
   States as target market.
2. User did not explicitly request a different English variant
   (en-GB, en-AU, etc.).
3. Selected workflow's `localization.supported_locales` includes
   `en-US`, or category default applies.

When the user says "English" without further qualification, default to
`en-US` unless other signals (UK / Australian spelling, British idiom,
country code) appear in the user's input.

## C. Input vs output vs target market

| Input | Output | Target | Action |
| --- | --- | --- | --- |
| English | English | US | Load `en-US`. |
| English | English | UK / AU | Load `en-GB` / en-AU. |
| Any | English | unspecified | Default to `en-US`. |
| English | Chinese | any | Skip en-US; load appropriate Chinese locale. |

## D. Protected content

Same as other locale layers:

- Code, identifiers, URLs, brand names.
- Direct quotations, citations, regulatory disclosures.
- Numbers, units, currency, dates.
- Required technical or legal wording.

## E. US English guidance

### E.1 Spelling

Default US spellings (vs UK):

| US (default) | UK | Notes |
| --- | --- | --- |
| organization | organisation | -ize / -yze also: realize / realise, analyze / analyse |
| color | colour | -or endings: behavior / behaviour, favor / favour |
| center | centre | -er endings: theater / theatre, fiber / fibre |
| meter | metre | -er: liter / litre |
| modeled | modelled | single consonant for verbs ending in -l after stressed syllable |
| traveled | travelled | same pattern |
| defense | defence | -se / -ce distinction |
| license (noun) / license (verb) | licence (noun) / license (verb) | US allows both as verb; UK requires noun/verb distinction |
| gray | grey | -ay vs -ey |

See [TERM_GLOSSARY.md](TERM_GLOSSARY.md) section 1 for the full
table.

### E.2 Quotation marks

- Use double quotes `" "` for direct speech and emphasis in body
  text.
- Use single quotes `' '` for nested quotes inside double quotes.
- Avoid smart quotes in technical writing; ASCII straight quotes are
  fine.

### E.3 Numbers, dates, currency

- Currency: `$` symbol before number; no space between symbol and
  number (e.g. `$100`, `$1,000.00`). Use `USD` in international
  contexts.
- Date: `MM/DD/YYYY` (e.g. `09/22/2026`). Avoid `DD/MM/YYYY` (that's
  UK / EU). Use ISO `YYYY-MM-DD` in technical documents.
- Time: 12-hour format in casual (`2:30 PM`), 24-hour format in
  technical / military (`14:30`).
- Number separator: comma for thousands (e.g. `1,000`, `1,000,000`);
  period for decimal (`1.5`). Never space.
- Phone: `(555) 123-4567` or `555-123-4567`.
- Address: ZIP code 5 digits (`12345`) or ZIP+4 (`12345-6789`).

### E.4 Idioms and expressions

US-specific idioms (vs UK / international):

- "Take a rain check" (defer).
- "Touch base" (contact briefly).
- "Circle back" (return to a topic).
- "Let's table this" (defer for now — note: UK English uses the
  opposite meaning).
- "Hit me up" (contact me).
- "Bail" (leave).
- "Soccer" (not "football" — UK uses "football" for soccer).
- "Elevator" (not "lift").
- "Apartment" (not "flat").
- "Cookie" (web — both US and international; UK uses "biscuit" for
  the food).

When writing for an international audience, prefer neutral English
over US-specific idioms. When the audience is clearly US, idioms add
warmth.

### E.5 Honorifics and titles

- Mr. / Ms. / Mrs. / Dr. / Prof. — with period in US English.
- Academic: Dr. Jane Smith, Ph.D. (vs UK: Dr Jane Smith).
- Military: Capt. / Col. / Gen. (US uses period consistently; UK
  often omits).

### E.6 Email and professional register

US email is more direct than UK or international business English.
Common conventions:

- Subject line: clear, action-oriented, specific.
- Greeting: "Hi [Name]," (casual) or "Dear [Name]," (formal). Avoid
  "Dear Sir/Madam" — overly formal for most contexts.
- Body: lead with the ask or summary; provide context after.
- Sign-off: "Best," / "Thanks," / "Regards,". Avoid
  "Yours faithfully" (UK convention).
- Reply chain: keep short, top-post or inline depending on team
  culture.

## F. Channel-specific tone

| Channel | Profile | Notes |
| --- | --- | --- |
| LinkedIn (US) | `en-us-linkedin-professional` | 100-300 字, achievement-focused, US idiom OK |
| Twitter / X | `en-us-twitter-casual` | short, punchy, emoji OK |
| Reddit | `en-us-reddit-casual` | long-form OK, personal voice, no marketing |
| Email (B2B) | `en-us-email-professional` | direct, ask first, sign-off |
| Email (B2C marketing) | `en-us-email-marketing` | subject-line-driven, casual |
| Sales page / landing | `en-us-landing-page-clear` | headline-driven, evidence, CTA |
| Customer support | `en-us-customer-support` | empathetic, specific action |
| Long-form blog / article | `en-us-long-form-article` | structured, citation-aware |
| General professional | `en-us-friendly-professional` | fallback |

See [STYLE_PROFILES.md](STYLE_PROFILES.md) for the full schema and
exemplars.

## G. AI-pattern reduction

Same rules as other locale layers:

- Three consecutive similar sentence structures (avoid).
- "In conclusion", "It's important to note", "delve into".
- Over-formal hedges ("It might be argued that", "One could
  potentially").
- Vague connectives ("Furthermore", "Moreover" in short text).
- Buzzword stacking ("synergy", "leverage", "circle back to" — even
  in US business writing).

## H. Editing intensity rules

Same as other locales:

- `none` — protect everything.
- `light` — minimal cleanup.
- `standard` — apply glossary + AI-pattern reduction.
- `strict_precision` — high precision, label uncertainty, mandatory for
  legal / medical / financial / security / compliance.

The router auto-escalates to `strict_precision` for regulated content.

## I. Before-and-after examples

### I.1 Intensity: standard, channel: friendly-professional

**Before:** Our company does software development.

**After:** We build enterprise software for [industry].

(Note: "Our company does" → "We build" is more direct and active.)

### I.2 Intensity: standard, channel: linkedin-professional

**Before:** I am thrilled to announce that I have joined XYZ as their
new head of marketing.

**After:** Excited to share that I've joined XYZ as Head of Marketing.
Looking forward to building with this team — [brief hook about
specifics].

(Note: US LinkedIn prefers "excited to share" over "thrilled to
announce"; specific role title; forward-looking.)

### I.3 Intensity: light, channel: translation

**Before (UK English):** "The organisation has realised the colour
scheme needs reorganising."

**After (US English):** "The organization has realized the color
scheme needs reorganizing."

(Note: US spellings throughout; preserve sentence structure since the
translation is light.)

### I.4 Intensity: strict_precision, channel: research-precise

**Before:** Most users prefer this product.

**After:** Based on the 2025 user survey (n=1,247, 95% CI), 78% of
respondents indicated preference for [product] over [competitor]. The
result applies to the [demographic] subsample.

(Note: cite sample size, confidence interval, demographic scope.)

### I.5 Intensity: standard, channel: customer-support

**Before:** We apologize for the inconvenience. We will process your
refund soon.

**After:**
```text
Hi [Name],

Sorry for the trouble. I've initiated a full refund for order [#12345].
You'll see it back on your original payment method within 5-7 business
days.

Let me know if anything else comes up.

Best,
[Agent name]
```

(Note: lead with action taken, specific timeline, open invitation.)

## K. Safety boundaries

Same as other locale layers:

- Does not claim to bypass AI detection, remove watermarks, or prove
  human authorship.
- Does not silently convert currency or units.
- Does not override user-recorded terminology.
- Default to neutral, factual phrasing on regulatory / political
  topics.

## L. Reference files

- [TERM_GLOSSARY.md](TERM_GLOSSARY.md) — US vs UK spelling / idiom
  table.
- [STYLE_PROFILES.md](STYLE_PROFILES.md) — Style profiles.
- [QUALITY_CHECKLIST.md](QUALITY_CHECKLIST.md) — Quality gate.
- [`../SHARED_STYLE_PROFILE_SCHEMA.md`](../SHARED_STYLE_PROFILE_SCHEMA.md) —
  core schema.
- [`../zh-TW/README.md`](../zh-TW/README.md) — reference
  structure.

## M. Citations

Editorial principles borrowed from US English style guides (Strunk &
White, AP Stylebook conventions for general usage). Specific citations
TBD as the pack matures.

The pack does not claim any anti-detection or watermark-removal
capability.