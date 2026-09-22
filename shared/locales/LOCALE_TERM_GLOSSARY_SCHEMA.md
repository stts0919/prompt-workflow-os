# Locale Term Glossary Schema

Every locale pack must define its term glossary using this canonical schema. The `zh-TW` glossary under [zh-TW/TERM_GLOSSARY.md](zh-TW/TERM_GLOSSARY.md) is the reference implementation.

## Row schema

```md
| # | Concept | Preferred {locale} | Acceptable alternatives | Avoid by default | Context notes | Example |
```

| Field                  | Type     | Description |
| ---------------------- | -------- | ----------- |
| `#`                    | int      | Stable entry number for cross-reference. |
| `Concept`              | string   | Plain-language description of the term. |
| `Preferred {locale}`   | string   | The locale's default wording in most contexts. |
| `Acceptable alternatives` | string | Variants that are also fine in some contexts. |
| `Avoid by default`     | string   | The form to avoid unless the context demands it. |
| `Context notes`        | string   | When the choice changes (industry, channel, region). |
| `Example`              | string   | Minimal example showing the term in use. |

## Minimum entry count

`zh-TW` currently has 156 entries. New locales should aim for at least 150 entries once they reach maturity, with a minimum of 50 entries when first published.

## Required categories

Locales should organize entries into categories. The `zh-TW` pack uses 13 categories. Other locales may use fewer or more, but should cover the equivalent territory:

1. Everyday digital and UI terms.
2. AI and technology.
3. Business and strategy.
4. Marketing and content.
5. Social media platforms and content formats.
6. Product, design, and UX.
7. Research and data.
8. Project management and operations.
9. E-commerce and customer support.
10. Education and learning.
11. Finance and business metrics.
12. Common conversational expressions.
13. Cross-border or cross-region terminology differences.

Some categories may not apply to every locale. For example, `ja-JP` may split the business category further (keigo-related terminology) and may not need a "cross-strait terminology" section.

## Variant table

The `zh-TW` glossary includes a section that documents how to handle related variants (`zh-HK`, `zh-CN`, etc.). Other locales with regional variants should include an equivalent section (for example, `en-US` vs `en-GB`).

## Editorial rules

These rules apply to every locale's glossary:

1. **The glossary guides editorial decisions.** It is not an automatic replacement engine.
2. **User-supplied terminology overrides defaults.** Once recorded in the context ledger, the user's preferred form is used consistently.
3. **Protected content is never translated.** Code, IDs, URLs, brand names, citations, quotes, dates, numbers, units are not touched.
4. **Context notes are mandatory.** A term without context is harder to use correctly.

## Validation

The structural validator checks:

- Each row has all 7 fields.
- Each row's `#` is unique.
- The locale's minimum entry threshold is met.
- The glossary file has at least one variant section (if the locale has variants).
