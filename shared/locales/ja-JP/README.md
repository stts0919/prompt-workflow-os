# Locale Pack — `ja-JP` (Japanese — Japan)

This directory is the `ja-JP` locale pack. It targets Japanese readers
in Japan — with proper keigo (honorific language), full-width
punctuation, sentence-ending particles in casual writing, and
channel-specific register conventions.

## Files in this directory

| File | Purpose |
| --- | --- |
| `README.md` | Locale entry point (this file). |
| `WRITING_RULES.md` | Editorial principles, protected content, editing intensity, keigo rules. |
| `TERM_GLOSSARY.md` | Loanword handling, katakana conventions, business / platform terms. |
| `STYLE_PROFILES.md` | Style profiles for JP channels (Email, Twitter / X, LINE, note.com, business docs). |
| `QUALITY_CHECKLIST.md` | Dual-layer quality gate. |

## How the router activates this pack

See [`../LOCALE_ROUTING_RULES.md`](../LOCALE_ROUTING_RULES.md). The
activation contract:

1. Detect input language, requested output language, and target market.
2. Activate `ja-JP` when **all**:
   - the user requested output in Japanese, **or** explicitly named
     Japan as target market, **or** the input contains Japanese
     characters.
3. Skip the locale layer entirely when the deliverable's output
   language is not Japanese.

## Key localization dimensions

- **Keigo (honorific language)**: sonkeigo (尊敬語, respect for the
  other party), kenjōgo (謙譲語, humility for one's own actions),
  teineigo (丁寧語, polite endings).
- **Full-width punctuation**: 「」、。「」 for quotes; comma `、` and
  period `。`.
- **Sentence-ending particles**: ね、よ、かな for casual register;
  です / ます for polite; だ for plain.
- **Loanword handling**: transliterate English to katakana for
  established terms, preserve English for brand names.
- **Channels**: Email (very high keigo), Twitter / X (casual),
  LINE (semi-casual), note.com (long-form), Business docs (very
  high keigo).

## Reference

- [`zh-TW` reference implementation](../zh-TW/README.md) —
  structural bar.
- [`zh-CN` reference implementation](../zh-CN/README.md) — parallel
  structure.
- [`yue-Hant-HK` reference implementation`](../yue-Hant-HK/README.md) —
  regional Traditional Chinese variant.
- [`en-US` reference implementation`](../en-US/README.md) and
  [`en-GB`](../en-GB/README.md) — English locale pairs.
- [`FUTURE_LOCALE_EXPANSION_PLAN.md`](../FUTURE_LOCALE_EXPANSION_PLAN.md)
  section 5 — original plan.