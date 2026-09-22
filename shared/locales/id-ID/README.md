# Locale Pack — `id-ID` (Indonesian — Indonesia)

This directory is the `id-ID` locale pack. It targets Indonesian
readers in Indonesia — with proper PUEBI (Pedoman Umum Ejaan Bahasa
Indonesia) spelling conventions, formal / informal register handling,
and English loanword integration common in modern Indonesian writing.

## Files in this directory

| File | Purpose |
| --- | --- |
| `README.md` | Locale entry point (this file). |
| `WRITING_RULES.md` | Editorial principles, register rules, protected content, editing intensity. |
| `TERM_GLOSSARY.md` | Loanword handling, business / platform terms, register differences. |
| `STYLE_PROFILES.md` | Style profiles for ID channels (WhatsApp, Instagram, Twitter / X, email, LinkedIn). |
| `QUALITY_CHECKLIST.md` | Dual-layer quality gate. |

## How the router activates this pack

See [`../LOCALE_ROUTING_RULES.md`](../LOCALE_ROUTING_RULES.md). The
activation contract:

1. Detect input language, requested output language, and target market.
2. Activate `id-ID` when **all**:
   - the user requested output in Indonesian, **or** explicitly named
     Indonesia as target market, **or** the input contains Indonesian
     text.
3. Skip the locale layer entirely when the deliverable's output
   language is not Indonesian.

## Key localization dimensions

- **PUEBI spelling** (since 2015): official Indonesian spelling rules.
  Replaces the older EYD (Ejaan Yang Disempurnakan).
- **Register**: formal (Anda / kami) vs informal (kamu / kita). Bahasa
  Indonesia has lighter honorifics than Korean / Japanese, but formal
  register is expected in business / official contexts.
- **Loanwords**: English tech terms used directly (software, internet,
  email); some established loanwords adapted (komputer, surel / email).
- **Channels**: WhatsApp (dominant messaging), Instagram, Twitter / X,
  Email, LinkedIn.

## Reference

- [`zh-TW` reference implementation](../zh-TW/README.md) —
  structural bar.
- [`zh-CN` reference implementation`](../zh-CN/README.md) — parallel
  structure.
- [`yue-Hant-HK`](../yue-Hant-HK/README.md) / [`en-US`](../en-US/README.md)
  / [`en-GB`](../en-GB/README.md) / [`ja-JP`](../ja-JP/README.md) /
  [`ko-KR`](../ko-KR/README.md) — other locales.
- [`FUTURE_LOCALE_EXPANSION_PLAN.md`](../FUTURE_LOCALE_EXPANSION_PLAN.md)
  section 7 — original plan.