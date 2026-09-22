# Multilingual Rules

1. Detect the primary language of the user's latest meaningful message. Do not infer from prior turns when the user switches language.
2. Reply in that language by default, including headings, explanations, and small UI strings.
3. If the user requests the deliverable in another language, keep the conversation in the user's writing language and produce the deliverable in the requested language.
4. Preserve code, file paths, URLs, IDs, JSON keys, commands, and product names unchanged unless the user explicitly asks for translation.
5. If the input is mixed-language and the target language is unclear, ask one short clarification question using the dominant language.
6. Workflow IDs and slugs remain English even in non-English content; reference them as readable identifiers, e.g. "031 — customer-persona".
7. Internal workflow instructions remain English regardless of user language.
8. When generating tables, lists, or schemas, prefer the user's language but keep technical keys in English.
9. Honor code-switching. A French user may paste an English snippet; reply in French with English preserved where it belongs.
10. Do not translate workflow category names (`content`, `business`, `research`, `workflow`, `technical`).

## Chinese variants

11. When the user's language is Traditional Chinese, identify whether they specified a locale (`zh-TW` Taiwan, `zh-HK` Hong Kong, `zh-MY` Malaysia, `zh-SG` Singapore). Default to **Taiwan (`zh-TW`)** when unspecified and the user's writing is Taiwan Traditional Chinese.
12. When the deliverable targets Taiwan readers, load the Taiwan Traditional Chinese localization layer:
    - `locales/zh-TW/WRITING_RULES.md`
    - `locales/zh-TW/TERM_GLOSSARY.md`
    - `locales/zh-TW/STYLE_PROFILES.md`
    - `locales/zh-TW/QUALITY_CHECKLIST.md`
13. When the user explicitly requests Hong Kong, Mainland, or international Chinese, honor that and do not apply `zh-TW` substitutions. Note the override in the context ledger.
14. The localization layer is editorial quality — it does not claim human authorship, does not remove watermarks, and does not evade AI detection.
15. For technical, factual, regulatory, or highly structured outputs, apply a lighter editing intensity and prefer precision over conversational tone.
16. Code, IDs, URLs, brand names, required disclosures, and direct quotations are protected content and are never substituted through the glossary.
17. User-supplied terminology overrides glossary entries once recorded in the context ledger.
18. The router decides an editing intensity (`none` / `light` / `standard` / `strict_precision`) per output. The decision is recorded in the context ledger.
19. The router skips the locale layer entirely when the deliverable's output language differs from the locale. Localization files load only when relevant to keep token use small.
20. Future locale packs follow the architecture in `shared/locales/README.md`. The `zh-TW` layer is the reference implementation; do not weaken it to make space for others.
