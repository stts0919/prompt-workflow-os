---
id: "028"
slug: "content-repurposing"
title: "Repurpose Content"
category: "content"
aliases:
  - repurpose
  - repurpose content
  - adapt for another channel
  - cross-post
triggers:
  - repurpose
  - adapt for twitter
  - convert to carousel
  - republish as newsletter
input_types:
  - source content
  - target channels
output_types:
  - channel-specific adaptations
requires:
  - source content
  - target channels
  - voice guide
produces:
  - one adaptation per target channel
  - publishing order recommendation
related:
  - social-post
  - thread-series
  - short-video-script
  - newsletter
playbooks:
  - create-high-quality-content
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



# 028 — Repurpose Content

## What is this?

Take the source asset and produce channel-specific adaptations that respect platform norms, returning one artifact per target channel plus a publishing order recommendation.

## Why use it?

Most content under-leverages its source asset. Repurposing lets a single research effort drive weeks of distribution.

## When should I use it?

- You finished a long article or talk and want more reach.
- You publish on multiple channels but produce only one source format.

## When should I not use it?

- You're translating — use translation-localization (027).
- You're splitting a single idea into a series — use thread-series (013).

## What should I prepare?

- Source content.
- Target channels.
- Voice guide.

## How does the AI help me?

1. Read the source.
2. For each channel, design the adaptation respecting norms.
3. Output each adaptation as a standalone artifact.
4. Recommend publishing order.

## What will I get?

- Per-channel adaptations.
- Publishing order recommendation.
- Channel-specific hashtags / mentions.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [social-post](../01-content/012-social-post.md)
- [thread-series](../01-content/013-thread-series.md)
- [short-video-script](../01-content/015-short-video-script.md)
- [newsletter](../01-content/011-newsletter.md)

## Recommended next steps

- content-quality-review (029)
- content-calendar (004)

---

## AI specification

```text
purpose: "Convert a source asset into multiple channel-specific formats."
required_inputs:
  - source content
  - target channels
  - voice guide
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're translating — use translation-localization (027)."
  - "You're splitting a single idea into a series — use thread-series (013)."
workflow:
  - "1. Read the source."
  - "2. For each channel, design the adaptation respecting norms."
  - "3. Output each adaptation as a standalone artifact."
  - "4. Recommend publishing order."
output_contract:
  - "one adaptation per target channel"
  - "publishing order recommendation"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: adaptations
    description: list of channel-specific adaptations
  - key: publish_order
    description: recommended publish order
```