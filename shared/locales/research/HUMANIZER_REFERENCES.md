# Humanizer-style References — Cross-language check

This document is the **research note** the locale team uses to keep editorial references fresh. It is **not** a locale pack and **not** a source of bypass claims. We use these references only for editorial principles (clarity, naturalness, tone, fact-handling, AI-pattern reduction). We do not cite any tool that promises to evade AI detection or remove watermarks through rewriting.

## Scope boundary

What this list is for:

- Editorial principles that improve clarity, naturalness, cultural fit, and tone.
- Awareness of common AI writing tells that we want to reduce.
- Reference language conventions for non-English locale packs.

What this list is **not** for:

- Anti-detection bypass. No humanizer in this list is cited for that purpose.
- Watermark removal. No humanizer in this list is cited for that purpose.
- Authorship verification. No humanizer in this list is cited for that purpose.

If any tool in this list makes claims about detection evasion or watermark removal, we cite it only for its editorial guidance and ignore the bypass claims.

## How to read this list

| Column        | Meaning |
| ------------- | ------- |
| Repo          | GitHub repo URL |
| Language      | Primary locale this fork targets |
| Stars         | GitHub stars at time of cross-check |
| Pushed        | Last commit date (UTC) |
| Within 30 days | Yes / No at time of check (the user's preference: prefer recent updates) |
| Editorial-only | Yes = we cite for editorial principles; No = excluded as anti-detection bypass |
| Note          | Why we cite it (or don't) |

Cross-check timestamp: **2026-09-22**.

## Cross-language index — editorial principles

| Repo | Language | Stars | Pushed | Within 30 days | Editorial-only | Note |
| --- | --- | ---: | --- | :---: | :---: | --- |
| [`blader/humanizer`](https://github.com/blader/humanizer) | en | 51,112 | 2026-09-06 | ✅ | ✅ | English original. Major rebuild 2026-09-06 reorganized around 25 patterns ordered by strength. Cited for the canonical editorial pattern list. |
| [`kevintsai1202/Humanizer-zh-TW`](https://github.com/kevintsai1202/Humanizer-zh-TW) | zh-TW | 850 | 2026-08-26 | ✅ | ✅ | Taiwan Traditional Chinese. Recent commits added watermark-cleaner scripts; the README explicitly disclaims detector evasion. We cite for zh-TW editorial principles only. |
| [`op7418/Humanizer-zh`](https://github.com/op7418/Humanizer-zh) | zh-CN | 17,685 | 2026-01-19 | ❌ (8 months) | ✅ | Simplified Chinese. Older but still authoritative. Cited as a reference for the zh-CN locale pack planning. |
| [`LifelongLazyLearner/qu-ai-wei`](https://github.com/LifelongLazyLearner/qu-ai-wei) | zh-CN | 594 | 2026-09-10 | ✅ | ✅ | Simplified Chinese, 2026 release. Smaller but fresh. Cited as a secondary zh-CN reference. |
| [`ai-zixun/humanizer-zh`](https://github.com/ai-zixun/humanizer-zh) | zh-CN | 159 | 2026-05-22 | ❌ | ✅ | Simplified Chinese. Older but covers long-form Chinese rewriting. Cited for the long-form profile cross-check. |
| [`epoko77-ai/im-not-ai`](https://github.com/epoko77-ai/im-not-ai) | ko | 5,666 | 2026-09-22 | ✅ | ✅ | Korean AI-text humanizer. Very active, multiple PRs merged in last 24h. Cited for the future ko-KR locale pack. |
| [`devswha/patina`](https://github.com/devswha/patina) | ko / en / zh / ja | 358 | 2026-09-20 | ✅ | ✅ | Multilingual (KO / EN / ZH / JA). Cited as a cross-language pattern catalog. |
| [`smixs/humanizer-ru`](https://github.com/smixs/humanizer-ru) | ru | 171 | 2026-08-30 | ✅ | ✅ | Russian humanizer + detector skill. Cited for Russian-language pattern list when relevant to cross-locale reviews. |
| [`ilyautov/humanizer-ru`](https://github.com/ilyautov/humanizer-ru) | ru | 371 | 2026-09-19 | ✅ | ✅ | Russian humanizer. "64 признака" pattern catalog. Cited as a secondary Russian reference. |
| [`matsuikentaro1/humanizer_academic`](https://github.com/matsuikentaro1/humanizer_academic) | academic / multilingual | 261 | 2026-09-19 | ✅ | ✅ | Academic-medical rewriting. Cited only for the academic register profile cross-check; not a general reference. |
| [`Anbeeld/WRITING.md`](https://github.com/Anbeeld/WRITING.md) | en (rules) | 371 | 2026-08-02 | ✅ | ✅ | "Rules that make AI text sharper, genre-aware, with concrete anchors and self-auditing workflow". Cited for the editorial ruleset itself. |

## Cross-language index — excluded as anti-detection bypass

These exist in the search results but **we do not cite them** because their explicit claim is detection evasion, which is outside the scope of this repository. Listing here is for transparency only.

| Repo | Why excluded |
| --- | --- |
| [`Aboudjem/humanizer-skill`](https://github.com/Aboudjem/humanizer-skill) | Self-described as "AI writing humanizer and detector. 55 patterns, 5 voices, a 0-100 AI-tell score". Detector framing out of scope. |
| [`korcarc/text-humanizer`](https://github.com/korcarc/text-humanizer) | "Bypasses the most of AI detectors such as Turnitin or GPTZero". Explicit bypass claim. |
| [`rudra496/StealthHumanizer`](https://github.com/rudra496/StealthHumanizer) | "🔓 Free open-source AI text humanizer — bypass GPTZero, Turnitin & AI detectors". Explicit bypass claim. |
| [`redbaronyyyyy-eng/humanizer-zh-academic`](https://github.com/redbaronyyyyy-eng/humanizer-zh-academic) | "Reduce AIGC detection rate for Chinese academic writing". Explicit AIGC-detection-rate reduction claim. |
| [`TheGP/untidetect-tools`](https://github.com/TheGP/untidetect-tools) | Meta-list of anti-detect and humanizing tools. Listing itself is the focus; not a content reference. |

## Locale-specific lookups

| Locale | First-look reference | Secondary reference | Notes |
| --- | --- | --- | --- |
| `en` | `blader/humanizer` | `Anbeeld/WRITING.md` | English baseline. |
| `zh-TW` | `kevintsai1202/Humanizer-zh-TW` | (none — TW fork is the canonical reference) | Active in last 30 days. |
| `zh-CN` | `op7418/Humanizer-zh` | `LifelongLazyLearner/qu-ai-wei`, `ai-zixun/humanizer-zh` | Mainline is older but authoritative; newer forks useful for long-form. |
| `yue-Hant-HK` | (none found) | `devswha/patina` (ZH flavor) | No Hong Kong Cantonese-specific humanizer found in this cross-check. Future locale work should also check Wikipedia's "Signs of AI writing" article for Cantonese patterns. |
| `ja-JP` | `devswha/patina` (JA flavor) | (none — JA-specific humanizer not found) | ja-JP pack should rely on keigo + structural guidance more than humanizer-style AI-tell removal. |
| `ko-KR` | `epoko77-ai/im-not-ai` | `devswha/patina` (KO flavor) | Korean coverage is healthy; multiple recent updates. |
| `ru-RU` | `ilyautov/humanizer-ru` | `smixs/humanizer-ru` | Russian coverage is healthy. (Russian is not on our target locale list but useful for cross-language pattern checks.) |
| `en-US`, `en-GB` | `blader/humanizer` | `Anbeeld/WRITING.md` | Use English reference; spelling/idiom differences are regional. |
| `id-ID`, `vi-VN` | (none found) | (none) | No Indonesian or Vietnamese humanizer found. Future locale packs should rely on general AI-tell patterns and local-language quality reviews. |

## Cross-check protocol

When this document is stale (the user's preference: within the last month), refresh by running:

```bash
gh search repos "humanizer" --limit 30 --json fullName,description,stargazersCount,pushedAt,language --jq '.[] | "\(.stargazersCount)\t\(.fullName)\t\(.pushedAt)\t\(.language // "?")"'
```

Then for each "Editorial-only ✅" candidate that is within the last 30 days, confirm the description does not include "bypass", "detector", "stealth", or "watermark removal". Update the tables.

## Cited by

- [`../../ZH_TW_LOCALIZATION_AND_WRITING_RULES.md`](../../ZH_TW_LOCALIZATION_AND_WRITING_RULES.md) — the Taiwan layer points here for cross-language context.
- [`../FUTURE_LOCALE_EXPANSION_PLAN.md`](../FUTURE_LOCALE_EXPANSION_PLAN.md) — uses the locale-specific lookups as starting hints for future locale work.
- This file does **not** replace any locale pack. Each locale pack owns its own writing rules, glossary, profiles, and tests.
