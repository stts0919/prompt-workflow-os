---
id: "074"
slug: "weekly-plan"
title: "Plan the Week"
category: "workflow"
aliases:
  - weekly planning
  - this week
  - week plan
triggers:
  - plan my week
  - this week
  - weekly plan
input_types:
  - tasks
  - goals
output_types:
  - weekly plan
requires:
  - task list
  - weekly goals
  - constraints
produces:
  - day-by-day plan
  - focus blocks
  - weekly review checklist
related:
  - task-breakdown
  - priority-planning
  - weekly-plan
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



# 074 — Plan the Week

## What is this?

Build a day-by-day plan with focus blocks, meetings protected, and a Friday weekly-review ritual.

## Why use it?

Weeks drift into meetings without explicit plans. A weekly plan protects focus time and builds review habits.

## When should I use it?

- Sunday / Monday planning.
- A week got away from you and you want to reset.

## When should I not use it?

- You only have one task — use task-breakdown (072).
- You're planning a long project — use project-plan (076).

## What should I prepare?

- Task list.
- Weekly goals.
- Known meetings.

## How does the AI help me?

1. Confirm tasks and goals.
2. Group by day and energy level.
3. Block focus time.
4. Add a Friday review.

## What will I get?

- Day-by-day plan.
- Focus blocks.
- Friday review template.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [task-breakdown](../04-workflow/072-task-breakdown.md)
- [priority-planning](../04-workflow/073-priority-planning.md)
- [weekly-plan](../04-workflow/074-weekly-plan.md)

## Recommended next steps

- self-review (088)

---

## AI specification

```text
purpose: "Plan a realistic week with focus blocks and a weekly review ritual."
required_inputs:
  - task list
  - weekly goals
  - constraints
optional_inputs:
  - calendar
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You only have one task — use task-breakdown (072)."
  - "You're planning a long project — use project-plan (076)."
workflow:
  - "1. Confirm tasks and goals."
  - "2. Group by day and energy level."
  - "3. Block focus time."
  - "4. Add a Friday review."
output_contract:
  - "day-by-day plan"
  - "focus blocks"
  - "weekly review checklist"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: weekly_plan
    description: day-by-day plan
  - key: review_template
    description: Friday review checklist
```