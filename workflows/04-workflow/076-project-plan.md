---
id: "076"
slug: "project-plan"
title: "Plan a Project"
category: "workflow"
aliases:
  - project plan
  - project management
  - Gantt-style plan
triggers:
  - project plan
  - plan a project
  - project management
input_types:
  - project
  - constraints
output_types:
  - project plan
requires:
  - objective
  - milestones
  - team or owner
  - timeline
produces:
  - milestones
  - tasks per milestone
  - owners
  - risks
related:
  - task-breakdown
  - project-risk
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
localization:
  supported_locales:
    - en
    - zh-TW
  default_style_profile: zh-cn-friendly-professional
  locale_style_profile_overrides:
    zh-TW:
  editing_intensity: standard
handoff:
  - key: context
    description: "summary of upstream context"
---



# 076 — Plan a Project

## What is this?

Produce a project plan: objective, milestones, tasks per milestone, owners, dependencies, risks, and a communication cadence.

## Why use it?

Most projects fail from coordination, not from design. A plan makes coordination explicit.

## When should I use it?

- You're starting a multi-week project.
- You need alignment across stakeholders.

## When should I not use it?

- You only need a weekly cadence — use weekly-plan (074).

## What should I prepare?

- Objective.
- Milestones.
- Team and timeline.

## How does the AI help me?

1. Confirm inputs.
2. Build milestones.
3. Tasks per milestone.
4. Owners and dependencies.
5. Risks and communication cadence.

## What will I get?

- Milestones.
- Tasks per milestone.
- Owners and dependencies.
- Risk register.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [task-breakdown](../04-workflow/072-task-breakdown.md)
- [project-risk](../04-workflow/077-project-risk.md)
- [weekly-plan](../04-workflow/074-weekly-plan.md)

## Recommended next steps

- project-risk (077)
- weekly-plan (074)

---

## AI specification

```text
purpose: "Build a complete project plan with milestones, tasks, and risks."
required_inputs:
  - objective
  - milestones
  - team or owner
  - timeline
optional_inputs:
  - dependencies
  - risks
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You only need a weekly cadence — use weekly-plan (074)."
workflow:
  - "1. Confirm inputs."
  - "2. Build milestones."
  - "3. Tasks per milestone."
  - "4. Owners and dependencies."
  - "5. Risks and communication cadence."
output_contract:
  - "milestones"
  - "tasks per milestone"
  - "owners"
  - "risks"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: project_plan
    description: full plan
  - key: risk_register
    description: risk list
```