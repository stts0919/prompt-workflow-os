---
id: "075"
slug: "goal-setting"
title: "Set Goals"
category: "workflow"
aliases:
  - goals
  - okrs
  - set objectives
triggers:
  - set goals
  - okrs
  - what should we aim for
input_types:
  - context
  - horizon
output_types:
  - goals with criteria
requires:
  - context or domain
  - horizon (quarter, year)
  - definition of success
produces:
  - goal statement
  - key results or success metrics
related:
  - task-breakdown
  - project-plan
  - priority-planning
playbooks:
  - plan-and-execute-a-project
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



# 075 — Set Goals

## What is this?

Write a goal statement with 3–5 measurable key results. Distinguish outcomes from outputs and surface risks to each goal.

## Why use it?

Goals without metrics are wishes. Goals with metrics force trade-offs and accountability.

## When should I use it?

- You're starting a quarter or year.
- Your team lacks a shared definition of success.

## When should I not use it?

- You want a single metric — use metric definition outside this workflow.

## What should I prepare?

- Context or domain.
- Horizon.
- Definition of success.

## How does the AI help me?

1. Confirm inputs.
2. Draft a goal statement.
3. Add 3–5 key results.
4. Identify risks.

## What will I get?

- Goal statement.
- Key results with metrics.
- Risk list.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [task-breakdown](../04-workflow/072-task-breakdown.md)
- [project-plan](../04-workflow/076-project-plan.md)
- [priority-planning](../04-workflow/073-priority-planning.md)

## Recommended next steps

- project-plan (076)
- task-breakdown (072)

---

## AI specification

```text
purpose: "Set clear goals with measurable success criteria."
required_inputs:
  - context or domain
  - horizon (quarter, year)
  - definition of success
optional_inputs:
  - team or individual
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You want a single metric — use metric definition outside this workflow."
workflow:
  - "1. Confirm inputs."
  - "2. Draft a goal statement."
  - "3. Add 3–5 key results."
  - "4. Identify risks."
output_contract:
  - "goal statement"
  - "key results or success metrics"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: goals
    description: goal + key results
  - key: risks
    description: risks to each goal
```