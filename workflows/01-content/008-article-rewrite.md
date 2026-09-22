---
id: "008"
slug: "article-rewrite"
title: "Rewrite an Existing Article"
category: "content"
aliases:
  - rewrite
  - rework draft
  - improve post
  - tighten article
triggers:
  - rewrite this
  - improve my draft
  - tighten this post
  - make this sharper
input_types:
  - existing draft
  - rewrite goal
output_types:
  - rewritten draft
  - change summary
requires:
  - existing draft or text
  - rewrite goal (shorter, sharper, different audience, new angle)
produces:
  - rewritten draft
  - summary of changes
related:
  - article-draft
  - content-editing
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



# 008 — Rewrite an Existing Article

## What is this?

Take an existing draft and produce a rewritten version that meets a specific goal (shorter, sharper, different angle, different audience, new voice). Return both a change summary and the rewritten text.

## Why use it?

Rewriting from scratch wastes work. A targeted rewrite preserves the proven core while fixing the specific weakness.

## When should I use it?

- An old post underperforms and needs a refresh.
- A draft hits the wrong tone.
- You need the same content for a different audience.

## When should I not use it?

- The draft is in good shape and only needs light editing — use content-editing (009).
- You're starting fresh — use article-draft (007).

## What should I prepare?

- Existing draft.
- Clear rewrite goal.
- Voice and audience constraints.

## How does the AI help me?

1. Diagnose what's not working in the draft (audience, structure, voice).
2. Define the rewrite target (length, angle, audience).
3. Rewrite section by section, preserving factual claims.
4. Add a 5-bullet change summary at the top.

## What will I get?

- Rewritten draft.
- 5-bullet change summary.
- Assumption and verification notes.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [article-draft](../01-content/007-article-draft.md)
- [content-editing](../01-content/009-content-editing.md)

## Recommended next steps

- content-editing (009)
- content-quality-review (029)

---

## AI specification

```text
purpose: "Rewrite an existing article to meet a stated goal while preserving intent and facts."
required_inputs:
  - existing draft or text
  - rewrite goal (shorter, sharper, different audience, new angle)
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "The draft is in good shape and only needs light editing — use content-editing (009)."
  - "You're starting fresh — use article-draft (007)."
workflow:
  - "1. Diagnose what's not working in the draft (audience, structure, voice)."
  - "2. Define the rewrite target (length, angle, audience)."
  - "3. Rewrite section by section, preserving factual claims."
  - "4. Add a 5-bullet change summary at the top."
output_contract:
  - "rewritten draft"
  - "summary of changes"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: rewritten_draft
    description: the rewritten article text
  - key: change_summary
    description: list of material changes
```