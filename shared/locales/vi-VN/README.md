# Locale Pack — `vi-VN` (Vietnamese — Vietnam)

This directory is the `vi-VN` locale pack. It targets Vietnamese readers
in Vietnam — with full diacritics, family-relationship pronouns,
and channel-specific tone for Zalo, Facebook, Email, LinkedIn.

## Files in this directory

| File | Purpose |
| --- | --- |
| `README.md` | Locale entry point (this file). |
| `WRITING_RULES.md` | Editorial principles, diacritics rules, register handling. |
| `TERM_GLOSSARY.md` | Loanword handling, business / platform terms, register differences. |
| `STYLE_PROFILES.md` | Style profiles for VN channels (Zalo, Facebook, Email, LinkedIn). |
| `QUALITY_CHECKLIST.md` | Dual-layer quality gate. |

## How the router activates this pack

See [`../LOCALE_ROUTING_RULES.md`](../LOCALE_ROUTING_RULES.md). The
activation contract:

1. Detect input language, requested output language, and target market.
2. Activate `vi-VN` when **all**:
   - the user requested output in Vietnamese, **or** explicitly named
     Vietnam as target market, **or** the input contains Vietnamese
     text.
3. Skip the locale layer entirely when the deliverable's output
   language is not Vietnamese.

## Key localization dimensions

- **Diacritics**: full diacritics are standard; omitting diacritics
  (e.g. "VN" without diacritics) is informal / SMS style.
- **Pronouns**: complex family / relationship system (anh / chị /
  em / ông / bà / cô / bác / chú...).
- **Loanwords**: English tech terms used directly; some Vietnamese
  adaptations (máy tính = computer).
- **Channels**: Zalo (dominant messaging), Facebook (still widely
  used), Email, LinkedIn.

## Reference

- [`zh-TW` reference implementation](../zh-TW/README.md) —
  structural bar.
- [`zh-CN` reference implementation`](../zh-CN/README.md) — parallel
  structure.
- [`yue-Hant-HK`](../yue-Hant-HK/README.md) / [`en-US`](../en-US/README.md)
  / [`en-GB`](../en-GB/README.md) / [`ja-JP`](../ja-JP/README.md) /
  [`ko-KR`](../ko-KR/README.md) / [`id-ID`](../id-ID/README.md) — other
  locales.
- [`FUTURE_LOCALE_EXPANSION_PLAN.md`](../FUTURE_LOCALE_EXPANSION_PLAN.md)
  section 8 — original plan.