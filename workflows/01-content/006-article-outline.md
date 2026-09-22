---
id: "006"
slug: "article-outline"
title: "Create an Article Outline"
category: "content"
aliases:
  - outline
  - post outline
  - article structure
triggers:
  - outline an article
  - structure a post
  - help me organize
  - skeleton of article
input_types:
  - topic
  - reader
  - key points or sources
output_types:
  - outline
  - section beats
  - opening hook draft
requires:
  - topic and angle
  - target reader
  - key points or sources
produces:
  - structured outline
  - section beats
  - draft opening hook
related:
  - article-draft
  - article-rewrite
  - storytelling
playbooks:
  - create-high-quality-content
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



# 006 — Create an Article Outline

## What is this?

Create a hierarchical outline (H2/H3) with one or two lines per section and a stated job for each section. Optionally draft the opening hook.

## Why use it?

Drafting without an outline produces bloated, meandering posts. A tight outline keeps every section earning its place.

## When should I use it?

- You're starting a long article (800+ words).
- You have sources or notes and need a skeleton.
- You want to check structure before committing to a draft.

## When should I not use it?

- You're writing a short post — go straight to social-post (012).
- You already have a draft and want refinement — use content-editing (009).

## What should I prepare?

- Topic and angle.
- Target reader.
- Key points, quotes, or sources to include.

## How does the AI help me?

1. Lock the reader and the angle.
2. Build the H2/H3 outline with one-line jobs per section.
3. Insert evidence placeholders where claims will need sources.
4. Draft the opening hook.
5. Suggest the next workflow: article-draft (007).

## What will I get?

- Hierarchical outline.
- One-line job per section.
- Draft opening hook.
- Source placeholders where needed.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [article-draft](../01-content/007-article-draft.md)
- [article-rewrite](../01-content/008-article-rewrite.md)
- [storytelling](../01-content/024-storytelling.md)

## Recommended next steps

- article-draft (007)

---

## AI specification

```text
purpose: "Produce a tight, ready-to-write outline for an article or long-form post."
required_inputs:
  - topic and angle
  - target reader
  - key points or sources
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're writing a short post — go straight to social-post (012)."
  - "You already have a draft and want refinement — use content-editing (009)."
workflow:
  - "1. Lock the reader and the angle."
  - "2. Build the H2/H3 outline with one-line jobs per section."
  - "3. Insert evidence placeholders where claims will need sources."
  - "4. Draft the opening hook."
  - "5. Suggest the next workflow: article-draft (007)."
output_contract:
  - "structured outline"
  - "section beats"
  - "draft opening hook"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: outline
    description: section-by-section outline
  - key: hook
    description: opening hook draft
  - key: source_placeholders
    description: list of places where sources are needed
```