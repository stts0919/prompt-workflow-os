# Locale Architecture — shared/locales/

This directory defines how locale packs are organized in `prompt-workflow-os`. The Taiwan Traditional Chinese (`zh-TW`) layer under [../ZH_TW_LOCALIZATION_AND_WRITING_RULES.md](../ZH_TW_LOCALIZATION_AND_WRITING_RULES.md) is the **reference implementation** for this architecture. Future locale packs must satisfy the same structural contract even when their content differs.

## What a locale is

A locale is more than a language code. A locale pack defines:

- Language (which language the AI speaks).
- Region / market (which conventions, terminology, and culture apply).
- Variant (Traditional vs Simplified, Simplified vs Simplified-Chinese-Taiwan, etc.).
- Channels and platforms the locale commonly writes for.

A locale pack is **not**:

- A translation table. Terminology is context-sensitive, not blind replacement.
- A dialect dictionary. Local slang is included only when it matches the requested audience and channel.
- A way to bypass AI detection. No locale pack makes that claim.

## How locale packs are organized

Every locale pack lives under a dedicated subdirectory named by its primary locale code, e.g.:

```text
shared/locales/
├── README.md                                  ← this file
├── LOCALE_ROUTING_RULES.md                    ← how the router activates each locale
├── LOCALE_STYLE_PROFILE_SCHEMA.md             ← canonical profile schema
├── LOCALE_TERM_GLOSSARY_SCHEMA.md             ← canonical glossary schema
├── LOCALE_QUALITY_CHECKLIST_SCHEMA.md         ← canonical checklist schema
├── FUTURE_LOCALE_EXPANSION_PLAN.md            ← planning for future locales
├── research/                                  ← cross-language editorial references
└── zh-CN/                                     ← first subdirectory-pack implementation
    ├── README.md                              ← locale entry point
    ├── WRITING_RULES.md                       ← source of truth
    ├── TERM_GLOSSARY.md
    ├── STYLE_PROFILES.md
    └── QUALITY_CHECKLIST.md
```

`zh-TW` predates this directory layout and lives at the top of `shared/`
(`shared/ZH_TW_*.md`). New locale packs should follow the subdirectory
pattern under `shared/locales/<code>/` so the locale tree stays organized.

## Files in this directory

| File                                | Purpose                                                   |
| ----------------------------------- | --------------------------------------------------------- |
| `README.md`                         | Architecture overview (this file).                        |
| `LOCALE_ROUTING_RULES.md`           | Rules for activating a locale pack.                      |
| `LOCALE_STYLE_PROFILE_SCHEMA.md`    | Schema every locale's style profiles must follow.        |
| `LOCALE_TERM_GLOSSARY_SCHEMA.md`    | Schema every locale's term glossary must follow.          |
| `LOCALE_QUALITY_CHECKLIST_SCHEMA.md` | Schema every locale's quality checklist must follow.      |
| `FUTURE_LOCALE_EXPANSION_PLAN.md`    | Per-locale implementation plan for next locales.          |

## Architectural principles

These principles apply to every locale pack.

1. **Locale selection follows explicit instruction first, target market second, requested output language third, input language last.** Do not assume a locale from one signal alone.
2. **Default unspecified Traditional Chinese to `zh-TW`.** Other locales require explicit user instruction or strong contextual signal.
3. **Glossaries are guidance, not blind replacement.** Context, user preference, brand names, industry vocabulary, and required regulated wording override defaults.
4. **User terminology always wins.** Once recorded in the context ledger, the user's preferred form is used consistently.
5. **Protected content is never rewritten by default.** Code, IDs, URLs, brand names, citations, quotes, dates, numbers, units, and required disclosures are protected in every locale.
6. **Each locale pack contains its own writing rules, term glossary, style profiles, quality checklist, and tests.** A locale is not a thin skin over another locale.
7. **Locale packages load selectively.** The router does not load every locale's files; it loads only what the current output requires.
8. **Editing intensity is locale-aware.** `none`, `light`, `standard`, `strict_precision` are universal categories, but the rules inside each category can vary per locale.
9. **Style profiles cover real channels.** Threads / Instagram / LinkedIn / Email / Sales / Landing / Long-form / Research / Technical / SOP / Agent spec / Support are the canonical channel set; new channels add new profiles.
10. **The `zh-TW` implementation is the quality bar.** Do not weaken it to make space for other locales. Other locales must match its structure and rigor, even when the content differs.

## Locale activation contract

The router must follow this contract every turn:

```text
1. Detect the user's input language.
2. Detect the requested output language (separately).
3. Detect the target market / locale (separately).
4. Default unspecified Traditional Chinese to zh-TW.
5. Load the matching locale pack's files only when relevant.
6. Choose a style profile based on workflow category, channel, audience, formality, evidence sensitivity.
7. Choose editing intensity (none | light | standard | strict_precision).
8. Apply glossary substitutions only to non-protected prose.
9. Skip the locale layer entirely when the deliverable's output language is not the locale's primary language.
10. Record the activation decision and chosen profile in the context ledger.
```

## Adding a new locale

To add a new locale:

1. Read the four schema files in this directory.
2. Read the `zh-TW` implementation as the reference.
3. Decide whether the new locale lives as a subdirectory of `shared/locales/` (recommended for new locales) or gets promoted to top-level shared files (only after it reaches the same maturity as `zh-TW`).
4. Write a per-locale plan in `FUTURE_LOCALE_EXPANSION_PLAN.md`.
5. Add the locale to the router's `LOCALE_ROUTING_RULES.md` activation matrix.
6. Run the validation script to confirm minimum content thresholds.

The `zh-TW` layer was implemented first because it is the most subtle (Mainland vs Taiwan differences, mixed Traditional Chinese inputs, traditional-only readers). Other locales will be easier to add but should match the same structural quality.
