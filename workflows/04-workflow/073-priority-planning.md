---
id: "073"
slug: "priority-planning"
title: "Plan Priorities"
category: "workflow"
aliases:
  - priorities
  - what to do first
  - ranking
triggers:
  - what to prioritize
  - rank these
  - priority order
input_types:
  - list
  - criteria
output_types:
  - ranked list
requires:
  - list of items
  - criteria
produces:
  - ranked list
  - rationale per item
related:
  - task-breakdown
  - goal-setting
  - weekly-plan
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



# 073 — Plan Priorities

## What is this?

Apply a scoring rubric to rank items. Show the reasoning and any ties.

## Why use it?

Unspoken priority means re-litigating every meeting. A transparent ranking ends the debate.

## When should I use it?

- You have a backlog of competing items.
- Your team needs a defensible priority order.

## When should I not use it?

- You only have a small todo list — use weekly-plan (074).

## What should I prepare?

- List of items.
- Criteria and weights.

## How does the AI help me?

1. Confirm criteria.
2. Score each item.
3. Apply weights.
4. Output the ranked list.

## What will I get?

- Ranked list.
- Score table.
- Tie-breaker notes.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [task-breakdown](../04-workflow/072-task-breakdown.md)
- [goal-setting](../04-workflow/075-goal-setting.md)
- [weekly-plan](../04-workflow/074-weekly-plan.md)

## Recommended next steps

- weekly-plan (074)
- task-breakdown (072)

---

## AI specification

```text
purpose: "Rank a list of items by explicit criteria."
required_inputs:
  - list of items
  - criteria
optional_inputs:
  - constraints
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You only have a small todo list — use weekly-plan (074)."
workflow:
  - "1. Confirm criteria."
  - "2. Score each item."
  - "3. Apply weights."
  - "4. Output the ranked list."
output_contract:
  - "ranked list"
  - "rationale per item"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: ranked_list
    description: items in priority order
  - key: rationale
    description: rationale per item
```