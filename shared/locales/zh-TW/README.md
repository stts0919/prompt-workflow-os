# Locale Pack — `zh-TW` (Traditional Chinese, Taiwan)

This directory is the `zh-TW` locale pack. It is the **reference implementation** for the locale architecture: the structural bar new locale packs must meet without weakening it. Future locales follow the four-file layout; they do not have to match the size.

## Files in this directory

| File | Purpose |
| --- | --- |
| `README.md` | Locale entry point (this file). |
| `WRITING_RULES.md` | 編輯原則、保護內容、編輯強度、AI-pattern 減少。 |
| `TERM_GLOSSARY.md` | 台灣 / 大陸 / 港澳 術語對照。 |
| `STYLE_PROFILES.md` | 15 個 style profile 涵蓋台灣主要場景。 |
| `QUALITY_CHECKLIST.md` | 雙層品質檢查（AI-readable + human editorial）。 |

The four content files predate the subdirectory layout — they previously lived at the top of `shared/` as `shared/ZH_TW_*.md`. The 2026-09-22 migration into `shared/locales/zh-TW/` brought them into structural parity with `zh-CN`.

## How the router activates this pack

See [`../LOCALE_ROUTING_RULES.md`](../LOCALE_ROUTING_RULES.md) section 1.5. The activation contract:

1. Detect input language, requested output language, and target market.
2. Activate `zh-TW` when **both**:
   - the user requested output in Traditional Chinese (or explicitly
     named Taiwan / a Taiwanese city as target market), AND
   - the user did not explicitly request Simplified Chinese.
3. Skip the locale layer entirely when the deliverable's output    language is not Chinese.

## Key localization dimensions

- **Terminology**: 台灣常用詞（軟體、資訊、影片、網路、滑鼠等），與大陸 / 港澳對照見 [`TERM_GLOSSARY.md`](TERM_GLOSSARY.md)。
- **Politics- and regulatory-aware phrasing**: 中性、實質性表述，不主動涉入統獨議題。
- **Taiwan-specific channels**: Threads / Instagram / LinkedIn / YouTube / Podcast 等。

## Reference

- [`zh-CN` reference implementation`](../zh-CN/README.md) — 平行結構、未來 locale 的設計模板。
- [`../research/HUMANIZER_REFERENCES.md`](../research/HUMANIZER_REFERENCES.md) — 編輯原則借鑑來源（僅 editorial，不延伸至反 AI 檢測）。
