---
id: "014"
slug: "carousel"
title: "Create a Carousel"
category: "content"
aliases:
  - carousel post
  - instagram carousel
  - linkedin carousel
  - slide post
triggers:
  - carousel
  - instagram carousel
  - linkedin carousel
  - slide post
input_types:
  - core message
  - slide count target
  - audience
output_types:
  - slide-by-slide outline
  - slide copy
  - CTA slide
requires:
  - core message
  - target slide count
  - audience
produces:
  - slide-by-slide outline
  - slide text
  - CTA slide
related:
  - thread-series
  - social-post
  - presentation-story
playbooks: []
mode_support:
  - guide
  - quick
  - recommend
language_support:
  input: auto-detect
  output: mirror-user-language
handoff:
  - key: context
    description: "summary of upstream context"
---



# 014 — Create a Carousel

## What is this?

Design a carousel with a hook slide, a teaching arc, and a CTA slide. Each slide has one idea and one visual cue.

## Why use it?

Carousels reward clarity. One idea per slide beats dense text — the format itself teaches users how to read it.

## When should I use it?

- You're publishing a teaching post on Instagram or LinkedIn.
- You want a downloadable reference asset.

## When should I not use it?

- You need a multi-post text series — use thread-series (013).
- You're presenting live — use presentation-story (019).

## What should I prepare?

- Core message.
- Target slide count (typically 5–12).
- Audience and voice.

## How does the AI help me?

1. Design the arc (hook → problem → insight → steps → CTA).
2. Write one idea per slide.
3. Add visual suggestions per slide (chart, diagram, photo).
4. End with a CTA slide.

## What will I get?

- Slide-by-slide outline.
- Slide copy.
- Visual suggestions.
- CTA slide.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [thread-series](../01-content/013-thread-series.md)
- [social-post](../01-content/012-social-post.md)
- [presentation-story](../01-content/019-presentation-story.md)

## Recommended next steps

- content-quality-review (029)
- content-repurposing (028)

---

## AI specification

```text
purpose: "Plan a slide-by-slide carousel that teaches one idea clearly."
required_inputs:
  - core message
  - target slide count
  - audience
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You need a multi-post text series — use thread-series (013)."
  - "You're presenting live — use presentation-story (019)."
workflow:
  - "1. Design the arc (hook → problem → insight → steps → CTA)."
  - "2. Write one idea per slide."
  - "3. Add visual suggestions per slide (chart, diagram, photo)."
  - "4. End with a CTA slide."
output_contract:
  - "slide-by-slide outline"
  - "slide text"
  - "CTA slide"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: slides
    description: list of slides with text and visual cues
```