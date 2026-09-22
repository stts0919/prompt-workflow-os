---
id: "024"
slug: "storytelling"
title: "Develop a Story"
category: "content"
aliases:
  - story arc
  - narrative
  - story structure
triggers:
  - story arc
  - narrative
  - tell a story
  - story structure
input_types:
  - raw events or facts
  - audience
  - story goal
output_types:
  - story outline
  - drafted story
requires:
  - raw events or facts
  - audience
  - story goal (inspire, teach, persuade, explain)
produces:
  - structured story
  - drafted story
  - moral or takeaway
related:
  - case-study
  - presentation-story
  - storytelling
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



# 024 — Develop a Story

## What is this?

Convert raw events or facts into a structured story with a clear setup, conflict, resolution, and takeaway. Return both an outline and a draft.

## Why use it?

Facts alone don't stick. A story makes the meaning memorable and the audience more likely to act on it.

## When should I use it?

- You want to land a key idea in a presentation or article.
- You're turning an experience into content.

## When should I not use it?

- You're documenting a customer outcome — use case-study (025).
- You're scripting a talk — use presentation-story (019).

## What should I prepare?

- Raw events or facts.
- Audience.
- Story goal.

## How does the AI help me?

1. Identify the protagonist, conflict, and turning point.
2. Build a 3-act arc.
3. Draft the story in the chosen voice.
4. State the takeaway plainly.

## What will I get?

- Story outline.
- Drafted story.
- One-line takeaway.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [case-study](../01-content/025-case-study.md)
- [presentation-story](../01-content/019-presentation-story.md)
- [storytelling](../01-content/024-storytelling.md)

## Recommended next steps

- article-draft (007)
- case-study (025)

---

## AI specification

```text
purpose: "Shape facts or experience into a coherent story with an arc and takeaway."
required_inputs:
  - raw events or facts
  - audience
  - story goal (inspire, teach, persuade, explain)
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're documenting a customer outcome — use case-study (025)."
  - "You're scripting a talk — use presentation-story (019)."
workflow:
  - "1. Identify the protagonist, conflict, and turning point."
  - "2. Build a 3-act arc."
  - "3. Draft the story in the chosen voice."
  - "4. State the takeaway plainly."
output_contract:
  - "structured story"
  - "drafted story"
  - "moral or takeaway"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: story_outline
    description: arc summary
  - key: story_draft
    description: drafted story text
```