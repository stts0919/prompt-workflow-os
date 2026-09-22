---
id: "023"
slug: "brand-voice-guide"
title: "Create a Brand Voice Guide"
category: "content"
aliases:
  - voice guide
  - tone of voice
  - writing style
  - brand voice
triggers:
  - voice guide
  - tone of voice
  - writing style
  - brand voice
input_types:
  - brand description
  - audience
  - samples
output_types:
  - voice guide
  - do/don't list
  - examples
requires:
  - brand summary
  - audience
  - any existing sample text
produces:
  - voice guide
  - do and don't list
  - sample paragraphs
related:
  - content-pillar-design
  - content-quality-review
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
  editing_intensity: standard
handoff:
  - key: context
    description: "summary of upstream context"
---



# 023 — Create a Brand Voice Guide

## What is this?

Define voice attributes (3–5), a do-and-don't list, and sample paragraphs that show the voice in action.

## Why use it?

Without a documented voice, every contributor reinvents the brand and content drifts. A voice guide eliminates arguments about tone.

## When should I use it?

- You're scaling content production across people or tools.
- Your content sounds inconsistent.

## When should I not use it?

- You're writing one piece — use content-editing (009) directly.

## What should I prepare?

- Brand summary or positioning.
- Audience.
- Optional: existing sample text that you like.

## How does the AI help me?

1. Read the brand summary and samples.
2. Name 3–5 voice attributes with one-line definitions.
3. Write do-and-don't examples per attribute.
4. Produce two sample paragraphs in the voice.

## What will I get?

- Voice attributes.
- Do-and-don't list.
- Sample paragraphs.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [content-pillar-design](../01-content/002-content-pillar-design.md)
- [content-quality-review](../01-content/029-content-quality-review.md)

## Recommended next steps

- content-quality-review (029)
- content-pillar-design (002)

---

## AI specification

```text
purpose: "Document a repeatable writing voice others can follow."
required_inputs:
  - brand summary
  - audience
  - any existing sample text
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're writing one piece — use content-editing (009) directly."
workflow:
  - "1. Read the brand summary and samples."
  - "2. Name 3–5 voice attributes with one-line definitions."
  - "3. Write do-and-don't examples per attribute."
  - "4. Produce two sample paragraphs in the voice."
output_contract:
  - "voice guide"
  - "do and don't list"
  - "sample paragraphs"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: voice_attributes
    description: 3–5 attributes with definitions
  - key: examples
    description: do/don't examples and sample paragraphs
```