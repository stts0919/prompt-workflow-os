---
id: "027"
slug: "translation-localization"
title: "Translate and Localize"
category: "content"
aliases:
  - translate
  - localization
  - localize
  - i18n
triggers:
  - translate
  - localize
  - i18n
  - convert to spanish
  - french version
input_types:
  - source content
  - target language
  - audience
output_types:
  - translated content
  - localization notes
requires:
  - source content
  - target language
  - audience context
produces:
  - localized translation
  - cultural adaptation notes
related:
  - article-rewrite
  - content-editing
  - brand-voice-guide
playbooks: []
mode_support:
  - guide
  - quick
  - recommend
language_support:
  input: auto-detect
  output: mirror-user-language
localization:
  supported_locales:
    - en
    - zh-TW
  default_style_profile: zh-tw-friendly-professional
  locale_style_profile_overrides:
    zh-TW:
  editing_intensity: light
handoff:
  - key: context
    description: "summary of upstream context"
---



# 027 — Translate and Localize

## What is this?

Produce a localized version of the content for the target language and audience, with notes on cultural adaptation choices.

## Why use it?

Direct translation loses nuance. Localization preserves meaning and adapts idioms, examples, and references.

## When should I use it?

- You're publishing content in a new market.
- You're adapting a campaign for a regional audience.

## When should I not use it?

- You're adapting for a different channel — use content-repurposing (028).
- You're rewriting in the same language — use article-rewrite (008).

## What should I prepare?

- Source content.
- Target language(s).
- Audience context (region, age, expertise).

## How does the AI help me?

1. Translate.
2. Adapt idioms and cultural references.
3. Preserve technical terms and brand names.
4. Add adaptation notes.

## What will I get?

- Localized version.
- Adaptation notes.
- Glossary of preserved terms.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [article-rewrite](../01-content/008-article-rewrite.md)
- [content-editing](../01-content/009-content-editing.md)
- [brand-voice-guide](../01-content/023-brand-voice-guide.md)

## Recommended next steps

- content-quality-review (029)
- content-repurposing (028)

---

## AI specification

```text
purpose: "Translate content while adapting tone, context, and terminology."
required_inputs:
  - source content
  - target language
  - audience context
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're adapting for a different channel — use content-repurposing (028)."
  - "You're rewriting in the same language — use article-rewrite (008)."
workflow:
  - "1. Translate."
  - "2. Adapt idioms and cultural references."
  - "3. Preserve technical terms and brand names."
  - "4. Add adaptation notes."
output_contract:
  - "localized translation"
  - "cultural adaptation notes"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: localized_text
    description: translated and adapted text
  - key: adaptation_notes
    description: list of notable choices
```