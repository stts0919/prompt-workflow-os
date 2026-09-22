# Locale Pack — `en-US` (English — United States)

This directory is the `en-US` locale pack. It targets US English
readers — a regional variant of English with distinct spelling
(`organization` vs `organisation`), date format (MM/DD/YYYY), idioms,
and professional register conventions.

## Files in this directory

| File | Purpose |
| --- | --- |
| `README.md` | Locale entry point (this file). |
| `WRITING_RULES.md` | Editorial principles, protected content, editing intensity, AI-pattern reduction. |
| `TERM_GLOSSARY.md` | US spellings + US / UK idiom flips + date / number / currency conventions. |
| `STYLE_PROFILES.md` | Style profiles for US channels (LinkedIn, Twitter / X, Reddit, email, landing pages). |
| `QUALITY_CHECKLIST.md` | Dual-layer quality gate. |

## How the router activates this pack

See [`../LOCALE_ROUTING_RULES.md`](../LOCALE_ROUTING_RULES.md). The
activation contract:

1. Detect input language, requested output language, and target market.
2. Activate `en-US` when **all**:
   - the user requested output in English, AND
   - the user explicitly named the United States (or US city) as target
     market, OR no specific locale was named (default to en-US for
     English requests), AND
   - the user did not explicitly request en-GB, en-AU, en-CA, or any
     other English regional variant.
3. For ambiguous requests (no target market specified), default to
   `en-US` because most global English training data and most users
   default to US conventions.
4. Skip the locale layer entirely when the deliverable's output
   language is not English.

## Key localization dimensions

- **Spelling**: -ize / -yze, -or (not -our), single consonants in some
  verbs (modeled, traveled).
- **Date / number format**: MM/DD/YYYY, 1,000 separator, $ symbol
  before number.
- **Idioms**: US-specific phrasal verbs and expressions.
- **Quotation style**: double quotes `" "` by default.
- **Honorifics**: Mr./Ms./Mrs./Dr. with period.

## Reference

- [`zh-TW` reference implementation](../zh-TW/README.md) — structural
  bar.
- [`zh-CN` reference implementation](../zh-CN/README.md) — parallel
  structure, simplified Chinese.
- [`yue-Hant-HK` reference implementation`](../yue-Hant-HK/README.md) —
  regional Traditional Chinese variant.
- [`FUTURE_LOCALE_EXPANSION_PLAN.md`](../FUTURE_LOCALE_EXPANSION_PLAN.md)
  section 3 — original plan.