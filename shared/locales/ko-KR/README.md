# Locale Pack — `ko-KR` (Korean — South Korea)

This directory is the `ko-KR` locale pack. It targets Korean readers in
South Korea — with proper honorific register, Korean punctuation, and
channel-specific conventions (Naver blog, KakaoTalk).

## Files in this directory

| File | Purpose |
| --- | --- |
| `README.md` | Locale entry point (this file). |
| `WRITING_RULES.md` | Editorial principles, honorific register rules, protected content, editing intensity. |
| `TERM_GLOSSARY.md` | Loanword handling, business / platform terms, Naver / Kakao specific. |
| `STYLE_PROFILES.md` | Style profiles for KR channels (Naver blog, KakaoTalk, Twitter / X, email). |
| `QUALITY_CHECKLIST.md` | Dual-layer quality gate. |

## How the router activates this pack

See [`../LOCALE_ROUTING_RULES.md`](../LOCALE_ROUTING_RULES.md). The
activation contract:

1. Detect input language, requested output language, and target market.
2. Activate `ko-KR` when **all**:
   - the user requested output in Korean, **or** explicitly named
     South Korea as target market, **or** the input contains Korean
     characters.
3. Skip the locale layer entirely when the deliverable's output
   language is not Korean.

## Key localization dimensions

- **Honorific register**: 합쇼체 (-습니다 / -입니다), 해요체 (-어 / -여요),
  반말체 (-다 / -야).
- **Punctuation**: full-width `,` `;` `:` `?` `!` (rare); `「」` for
  quotes; `.` for sentence period.
- **Loanwords**: English transliterated to Hangul; established
  loanwords common (컴퓨터, 인터넷).
- **Sentence-ending particles**: ~습니다 (formal), ~어요 (polite
  casual), ~다 (plain), ~야 (intimate casual).
- **Channels**: Naver blog (long-form), KakaoTalk (chat), Twitter / X
  (casual), Email (formal).

## Reference

- [`zh-TW` reference implementation](../zh-TW/README.md) —
  structural bar.
- [`zh-CN` reference implementation`](../zh-CN/README.md) — parallel
  structure.
- [`yue-Hant-HK` reference implementation`](../yue-Hant-HK/README.md) —
  regional Traditional Chinese variant.
- [`en-US`](../en-US/README.md) and [`en-GB`](../en-GB/README.md) —
  English locale pairs.
- [`ja-JP` reference implementation`](../ja-JP/README.md) — fellow
  East Asian locale.
- [`FUTURE_LOCALE_EXPANSION_PLAN.md`](../FUTURE_LOCALE_EXPANSION_PLAN.md)
  section 6 — original plan.