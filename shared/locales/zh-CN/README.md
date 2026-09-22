# Locale Pack — `zh-CN` (Simplified Chinese, Mainland China)

This directory is the `zh-CN` locale pack. It mirrors the `zh-TW` reference
implementation in structure (4 files) while adapting content for Mainland
China audiences.

## Files in this directory

| File | Purpose |
| --- | --- |
| `WRITING_RULES.md` | 编辑原则、保护内容、编辑强度、AI-pattern 减少 |
| `TERM_GLOSSARY.md` | 大陆 / 港澳台 术语对照 |
| `STYLE_PROFILES.md` | 10 个 style profile 覆盖大陆主要频道 |
| `QUALITY_CHECKLIST.md` | 双层品质检查（AI-readable + human editorial） |

The top-level shared files ([../../ZH_CN_*.md](../../)) mirror these same
four files. The two locations must stay in sync.

## How the router activates this pack

See [../LOCALE_ROUTING_RULES.md](../LOCALE_ROUTING_RULES.md). The
activation contract is:

1. Detect input language, requested output language, and target market.
2. Default unspecified Traditional Chinese to `zh-TW`, not `zh-CN`.
3. Activate `zh-CN` only when **both**:
   - the user requested output in Simplified Chinese (or explicitly named
     Mainland China / a Mainland city as target market), AND
   - the user did not explicitly request Traditional Chinese.
4. Skip the locale layer entirely when the deliverable's output language is
   not Chinese.

## Key localization dimensions

- **Terminology**: 大陆通用词（软件、信息、视频、网络、鼠标等）。
- **Politics- and regulatory-aware phrasing**: 默认中性、事实性表述。
- **Mainland-specific channels**: 公众号、微博、小红书、抖音、哔哩哔哩、
  知乎等。

## Reference

- [`zh-TW` reference implementation](../../ZH_TW_LOCALIZATION_AND_WRITING_RULES.md)
  — 結構上的品質標杆。
- [`FUTURE_LOCALE_EXPANSION_PLAN.md`](../FUTURE_LOCALE_EXPANSION_PLAN.md) section 1
  — zh-CN 計劃的原始範圍。
- [`../research/HUMANIZER_REFERENCES.md`](../research/HUMANIZER_REFERENCES.md) —
  编辑原则借鉴来源（仅 editorial，不延伸至反 AI 检测）。