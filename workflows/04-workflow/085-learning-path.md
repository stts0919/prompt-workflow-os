---
id: "085"
slug: "learning-path"
title: "Design a Learning Path"
category: "workflow"
aliases:
  - learning plan
  - study plan
  - course plan
triggers:
  - learning path
  - how to learn
  - study plan
input_types:
  - topic
  - level
output_types:
  - learning path
requires:
  - topic
  - current level
  - goal level
  - time budget
produces:
  - learning path
  - milestones
  - resources
related:
  - concept-explanation
  - practice-design
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



# 085 — Design a Learning Path

## What is this?

Produce a learning path with phases, milestones, recommended resources, and verification exercises.

## Why use it?

Self-learning fails when it lacks structure. A path turns "learn X" into "do A, then B, then C".

## When should I use it?

- You're learning a new skill.
- You're onboarding someone to a topic.

## When should I not use it?

- You just need a single concept explained — use concept-explanation (086).

## What should I prepare?

- Topic.
- Current and goal level.
- Time budget.

## How does the AI help me?

1. Confirm inputs.
2. Build phases.
3. Pick resources.
4. Add verification per phase.

## What will I get?

- Learning path.
- Milestones.
- Resources and verification per phase.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [concept-explanation](../04-workflow/086-concept-explanation.md)
- [practice-design](../04-workflow/087-practice-design.md)

## Recommended next steps

- concept-explanation (086)
- practice-design (087)

---

## AI specification

```text
purpose: "Build a learning path that takes you from current to goal level."
required_inputs:
  - topic
  - current level
  - goal level
  - time budget
optional_inputs:
  - preferred format
  - tools
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You just need a single concept explained — use concept-explanation (086)."
workflow:
  - "1. Confirm inputs."
  - "2. Build phases."
  - "3. Pick resources."
  - "4. Add verification per phase."
output_contract:
  - "learning path"
  - "milestones"
  - "resources"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: path
    description: phased learning plan
  - key: resources
    description: resource list
```