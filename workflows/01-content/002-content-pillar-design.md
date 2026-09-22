---
id: "002"
slug: "content-pillar-design"
title: "Design Content Pillars"
category: "content"
aliases:
  - content pillars
  - niche pillars
  - editorial pillars
  - topic clusters
triggers:
  - what should I be about
  - build my brand pillars
  - editorial pillars
  - topic clusters
input_types:
  - brand or expert description
  - audience
  - competitors or references
output_types:
  - pillar list
  - pillar rationale
  - pillar boundaries
requires:
  - brand or expert positioning
  - target audience
  - optional reference creators or competitors
produces:
  - pillar list (3–6)
  - pillar rationale
  - pillar boundaries (what each pillar covers and excludes)
related:
  - content-idea-generation
  - positioning
  - audience-message-map
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



# 002 — Design Content Pillars

## What is this?

Pick 3–6 content pillars that justify every post you publish. Each pillar gets a clear scope (what it covers), a boundary (what it doesn't), and a differentiator (why you own it).

## Why use it?

Without pillars, content drifts across topics, confuses the audience, and never compounds. Pillars let ideas, repurposing, and SEO reinforce each other.

## When should I use it?

- You're starting a blog, channel, or newsletter.
- Your content feels scattered; readers can't summarize what you're about.
- You want to align your team or contractors around the same themes.

## When should I not use it?

- You already have working pillars and need ideas — use content-idea-generation (001).
- You need a one-time article — skip the pillar work.

## What should I prepare?

- Brand summary or expert bio.
- Target audience description.
- Optional: 3 creators or publications you admire, with reasons.

## How does the AI help me?

1. Restate the brand and audience in one sentence.
2. Propose 4–6 candidate pillars with one-line rationale each.
3. Note boundaries and overlap risks between pillars.
4. Recommend the strongest 3–5 pillars with confidence rationale.
5. Suggest how to test the pillars with content-idea-generation (001).

## What will I get?

- A pillar table (pillar → scope → boundary → differentiator).
- A 2-paragraph rationale for the chosen set.
- One next-workflow suggestion: content-idea-generation (001).

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [content-idea-generation](../01-content/001-content-idea-generation.md)
- [positioning](../02-business/035-positioning.md)
- [audience-message-map](../01-content/003-audience-message-map.md)

## Recommended next steps

- content-idea-generation (001)
- audience-message-map (003)

---

## AI specification

```text
purpose: "Define durable content pillars that anchor an editorial calendar and brand identity."
required_inputs:
  - brand or expert positioning
  - target audience
  - optional reference creators or competitors
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You already have working pillars and need ideas — use content-idea-generation (001)."
  - "You need a one-time article — skip the pillar work."
workflow:
  - "1. Restate the brand and audience in one sentence."
  - "2. Propose 4–6 candidate pillars with one-line rationale each."
  - "3. Note boundaries and overlap risks between pillars."
  - "4. Recommend the strongest 3–5 pillars with confidence rationale."
  - "5. Suggest how to test the pillars with content-idea-generation (001)."
output_contract:
  - "pillar list (3–6)"
  - "pillar rationale"
  - "pillar boundaries (what each pillar covers and excludes)"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: pillars
    description: list of pillars with one-line definitions
  - key: boundaries
    description: notes on what each pillar excludes
```