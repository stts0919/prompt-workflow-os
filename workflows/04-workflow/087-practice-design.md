---
id: "087"
slug: "practice-design"
title: "Design a Practice Exercise"
category: "workflow"
aliases:
  - practice exercise
  - drill
  - exercise design
triggers:
  - design a drill
  - practice exercise
  - deliberate practice
input_types:
  - skill
  - current level
output_types:
  - practice exercise
requires:
  - skill
  - current level
  - available time
produces:
  - exercise
  - feedback criteria
  - success threshold
related:
  - learning-path
  - concept-explanation
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



# 087 — Design a Practice Exercise

## What is this?

Produce an exercise: setup, instructions, feedback criteria, and what success looks like.

## Why use it?

Practice without feedback builds habits, not skill. Deliberate practice is specific, measurable, and revisitable.

## When should I use it?

- You're learning a skill and need structured drills.
- You're designing a course or workshop.

## When should I not use it?

- You want general encouragement — use learning-path (085) instead.

## What should I prepare?

- Skill.
- Current level.
- Time available.

## How does the AI help me?

1. Confirm inputs.
2. Write the exercise.
3. Define feedback.
4. Define success.

## What will I get?

- Exercise.
- Feedback criteria.
- Success threshold.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [learning-path](../04-workflow/085-learning-path.md)
- [concept-explanation](../04-workflow/086-concept-explanation.md)

## Recommended next steps

- self-review (088)

---

## AI specification

```text
purpose: "Design a focused practice exercise for a chosen skill."
required_inputs:
  - skill
  - current level
  - available time
optional_inputs:
  - tools
  - feedback source
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You want general encouragement — use learning-path (085) instead."
workflow:
  - "1. Confirm inputs."
  - "2. Write the exercise."
  - "3. Define feedback."
  - "4. Define success."
output_contract:
  - "exercise"
  - "feedback criteria"
  - "success threshold"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: exercise
    description: exercise instructions
  - key: feedback
    description: feedback criteria
```