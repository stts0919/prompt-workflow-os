---
id: "086"
slug: "concept-explanation"
title: "Explain a Concept"
category: "workflow"
aliases:
  - explain
  - what is x
  - concept explanation
triggers:
  - explain
  - what is
  - how does x work
input_types:
  - concept
  - audience level
output_types:
  - explanation
requires:
  - concept
  - audience level
produces:
  - explanation with examples
  - analogy
  - common pitfalls
related:
  - learning-path
  - practice-design
  - knowledge-map
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



# 086 — Explain a Concept

## What is this?

Produce a multi-layer explanation: one-sentence summary, intuition, worked example, common pitfalls, and a deeper dive.

## Why use it?

Most "explanations" are still jargon. Plain-language explanations with examples make concepts stick.

## When should I use it?

- You're learning a new topic.
- You're teaching a concept to someone else.

## When should I not use it?

- You want a full curriculum — use learning-path (085).

## What should I prepare?

- Concept.
- Audience level.

## How does the AI help me?

1. Confirm concept and audience.
2. Write a one-sentence summary.
3. Add intuition and example.
4. Note pitfalls.
5. Offer a deeper dive.

## What will I get?

- One-sentence summary.
- Intuition.
- Worked example.
- Common pitfalls.
- Deeper dive pointer.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [learning-path](../04-workflow/085-learning-path.md)
- [practice-design](../04-workflow/087-practice-design.md)
- [knowledge-map](../03-research/062-knowledge-map.md)

## Recommended next steps

- learning-path (085)
- practice-design (087)

---

## AI specification

```text
purpose: "Explain a concept in plain language with examples."
required_inputs:
  - concept
  - audience level
optional_inputs:
  - background
  - desired depth
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You want a full curriculum — use learning-path (085)."
workflow:
  - "1. Confirm concept and audience."
  - "2. Write a one-sentence summary."
  - "3. Add intuition and example."
  - "4. Note pitfalls."
  - "5. Offer a deeper dive."
output_contract:
  - "explanation with examples"
  - "analogy"
  - "common pitfalls"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: explanation
    description: multi-layer explanation
  - key: analogy
    description: analogy used
```