---
id: "016"
slug: "video-hook"
title: "Generate Video Hooks"
category: "content"
aliases:
  - video hooks
  - tiktok hooks
  - opening lines for video
triggers:
  - video hook
  - opening line
  - scroll-stopper
  - first 3 seconds
input_types:
  - video topic
  - platform
  - tone
output_types:
  - hook variants
  - rationale per hook
requires:
  - video topic
  - platform
  - tone
produces:
  - ranked hook variants
  - rationale per hook
related:
  - short-video-script
  - headline-generation
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



# 016 — Generate Video Hooks

## What is this?

Produce multiple opening hooks tailored to platform norms, ranked by likely scroll-stopping power and fit with the topic.

## Why use it?

Short video lives or dies in the first 2 seconds. A bank of tested hooks is the single highest-leverage asset a video creator has.

## When should I use it?

- You're scripting a Reel / TikTok / Short and want a hook.
- Your hooks feel tired.

## When should I not use it?

- You already have a script — skip this and write the body.
- You want a full script — use short-video-script (015).

## What should I prepare?

- Video topic.
- Platform.
- Tone (educational, contrarian, funny, etc.).

## How does the AI help me?

1. Confirm topic and platform.
2. Generate 10–20 hooks across formats (question, stat, story, contrarian).
3. Score each for fit and scroll-stopping.
4. Recommend the top 5 with rationale.

## What will I get?

- 10–20 hook variants.
- Top-5 recommendation.
- Suggested next workflow: short-video-script (015).

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [short-video-script](../01-content/015-short-video-script.md)
- [headline-generation](../01-content/020-headline-generation.md)

## Recommended next steps

- short-video-script (015)

---

## AI specification

```text
purpose: "Generate and rank opening hooks for short-form video."
required_inputs:
  - video topic
  - platform
  - tone
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You already have a script — skip this and write the body."
  - "You want a full script — use short-video-script (015)."
workflow:
  - "1. Confirm topic and platform."
  - "2. Generate 10–20 hooks across formats (question, stat, story, contrarian)."
  - "3. Score each for fit and scroll-stopping."
  - "4. Recommend the top 5 with rationale."
output_contract:
  - "ranked hook variants"
  - "rationale per hook"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: hooks
    description: ranked list of hook variants
```