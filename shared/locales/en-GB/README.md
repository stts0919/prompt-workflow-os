# Locale Pack — `en-GB` (English — United Kingdom)

This directory is the `en-GB` locale pack. It targets British English
readers — UK-specific spelling (`organisation`, `colour`), idioms
(`whilst`, `amongst`, `fortnight`), date format (DD/MM/YYYY), and
formal letter register conventions.

## Files in this directory

| File | Purpose |
| --- | --- |
| `README.md` | Locale entry point (this file). |
| `WRITING_RULES.md` | Editorial principles, protected content, editing intensity, AI-pattern reduction. |
| `TERM_GLOSSARY.md` | GB vs US spellings, idioms, date / number / currency conventions, formal register. |
| `STYLE_PROFILES.md` | Style profiles for UK channels (LinkedIn, email, formal letter, long-form). |
| `QUALITY_CHECKLIST.md` | Dual-layer quality gate. |

## How the router activates this pack

See [`../LOCALE_ROUTING_RULES.md`](../LOCALE_ROUTING_RULES.md). The
activation contract:

1. Detect input language, requested output language, and target market.
2. Activate `en-GB` when **all**:
   - the user requested output in English, AND
   - the user explicitly named the United Kingdom (or UK city) as
     target market, OR the user's input contains UK spellings
     (`organisation`, `colour`, `behaviour`), OR the user explicitly
     requested "British English" / "UK English".
3. When the user says "English" without further qualification, default
   to `en-US` (because most global English training data and most
   users default to US conventions).
4. Skip the locale layer entirely when the deliverable's output
   language is not English.

## Key localization dimensions

- **Spelling**: -ise / -yse, -our (not -or), double consonants
  (`modelled`, `travelled`), -re endings (`theatre`, `fibre`).
- **Date / number format**: DD/MM/YYYY, £ symbol before number.
- **Idioms**: UK-specific phrasal verbs and expressions (`whilst`,
  `amongst`, `fortnight`, `at the end of the day`).
- **Quotation style**: single quotes `' '` by default (UK convention);
  double quotes for nested quotes.
- **Honorifics**: Mr / Mrs / Dr (no period in most UK style guides).
- **Formal letter register**: more common than in US business
  writing; uses "Yours sincerely" / "Yours faithfully" sign-offs.

## Reference

- [`zh-TW` reference implementation](../zh-TW/README.md) —
  structural bar.
- [`zh-CN` reference implementation](../zh-CN/README.md) — parallel
  structure.
- [`yue-Hant-HK` reference implementation`](../yue-Hant-HK/README.md) —
  regional Traditional Chinese variant.
- [`en-US` reference implementation`](../en-US/README.md) — sister
  English locale.
- [`FUTURE_LOCALE_EXPANSION_PLAN.md`](../FUTURE_LOCALE_EXPANSION_PLAN.md)
  section 4 — original plan.