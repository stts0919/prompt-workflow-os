# Locale Pack — `yue-Hant-HK` (Traditional Chinese — Hong Kong)

This directory is the `yue-Hant-HK` locale pack. It targets Hong Kong
Traditional Chinese readers — a regional variant of Traditional Chinese
that shares characters with `zh-TW` but uses different terminology in
many IT / consumer / formal contexts, and may include Cantonese
vocabulary in colloquial writing.

## Files in this directory

| File | Purpose |
| --- | --- |
| `README.md` | Locale entry point (this file). |
| `WRITING_RULES.md` | 寫作原則、保護內容、編輯強度、AI-pattern 減少。 |
| `TERM_GLOSSARY.md` | 香港 / 台灣 / 大陸 術語對照、Cantonese 口語詞。 |
| `STYLE_PROFILES.md` | Style profiles for HK channels (WhatsApp, Facebook, LIHKG, formal email, etc.). |
| `QUALITY_CHECKLIST.md` | Dual-layer quality gate (compact AI-readable + human editorial). |

## How the router activates this pack

See [[LOCALE_ROUTING_RULES.md](../LOCALE_ROUTING_RULES.md)](LOCALE_ROUTING_RULES.md). The
activation contract:

1. Detect input language, requested output language, and target market.
2. Activate `yue-Hant-HK` when **all**:
   - the user requested output in Traditional Chinese, AND
   - the user explicitly named Hong Kong (or a HK city / Cantonese) as the
     target market, AND
   - the user did not explicitly request Simplified Chinese or Taiwan.
3. When in doubt between `yue-Hant-HK` and `zh-TW`, ask one short
   clarification. Default to `zh-TW` if the user does not answer (because
   `zh-TW` is the reference implementation and covers more channels).
4. Skip the locale layer entirely when the deliverable's output language
   is not Chinese.

## Key localization dimensions

- **Terminology**: HK tends to follow Mainland IT conventions
  (軟件 / 程式 / 寬頻) while keeping Taiwan formal register (的 / 與 /
  並) in business writing. Both are acceptable in the HK layer.
- **Cantonese vocabulary**: 食字、搞掂、嘅、喺、唔該、點解、邊度,
  etc. Common in casual chat (WhatsApp, Facebook comments). Rare in
  formal documents.
- **Bilingual mixing**: HK writing commonly mixes English and Chinese
  in the same sentence (e.g. 「記得 check 吓個 file」). Preserve the mix
  when the source mixes; do not force monolingual output.
- **Channels**: WhatsApp / Signal / Telegram (messaging), Facebook (still
  dominant), LIHKG (forum), Instagram, LinkedIn (English-leaning).

## Reference

- [`zh-TW` reference implementation](../zh-TW/README.md) — 結構上的
  品質標杆。
- [`zh-CN` reference implementation`](../zh-CN/README.md) — 平行結構、
  簡體中文版本。
- [`FUTURE_LOCALE_EXPANSION_PLAN.md`](../FUTURE_LOCALE_EXPANSION_PLAN.md)
  section 2 — 原始計劃。