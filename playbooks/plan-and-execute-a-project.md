---
playbook: plan-and-execute-a-project
slug: plan-and-execute-a-project
title: Plan and Execute a Project
mode_default: guide
stages: 5
---

# Plan and Execute a Project

## User scenario

You have a multi-step project ahead — a product launch, a research initiative, a content series, a process rollout — and you want a clean plan, a task breakdown, an owner map, and an explicit review cadence.

## Intended final outcome

A project plan with milestones, owners, dependencies, risks, and a weekly operating cadence.

## Workflow sequence

1. **[075 — Set Goals](../workflows/04-workflow/075-goal-setting.md)** — define success first.
2. **[072 — Break a Task Down](../workflows/04-workflow/072-task-breakdown.md)** — decompose the work into shippable units.
3. **[076 — Plan a Project](../workflows/04-workflow/076-project-plan.md)** — assemble a milestone-based plan with owners.
4. **[077 — Manage Project Risks](../workflows/04-workflow/077-project-risk.md)** — flag the riskiest assumptions and how to mitigate.
5. **[074 — Plan the Week](../workflows/04-workflow/074-weekly-plan.md)** — translate the project plan into this week's commitments.

## Optional add-on

After step 5, run **[088 — Run a Personal Review](../workflows/04-workflow/088-self-review.md)** at the end of each week.

## Handoff data between steps

| From → To    | Key                | Description                                       |
| ------------ | ------------------ | ------------------------------------------------- |
| step 1 → 2   | `goals`            | Goal + key results                                |
| step 2 → 3   | `task_tree`        | Hierarchical task tree with estimates             |
| step 3 → 4   | `project_plan`     | Milestone-based plan with owners                  |
| step 4 → 5   | `risk_register`    | Ranked risks                                      |

## Routing conditions

- Trigger phrases include "plan a project", "build a roadmap", "structure this initiative", "weekly cadence".
- Use when the user wants both strategy and operating rhythm.

## Skip conditions

- If the project is a single workstream, run task-breakdown (072) directly.
- If the user only needs risk review, run project-risk (077) directly.
- If a goal statement already exists, skip step 1.

## Example start message

```
Read this repository's START.md and help me plan this project.

Objective: [one sentence]
Duration: [weeks or months]
Team: [roles and known owners]
Constraints: [time, budget, dependencies]
```

## Final quality check

- Goals include measurable success criteria.
- The task tree maps cleanly to the milestones.
- Risks are scored and have owners.
- The weekly plan lists specific focus blocks for the week ahead.

## AI specification

```yaml
playbook: plan-and-execute-a-project
rule: "Skip goals if the user already has them."
mode: "guide by default."
skip_rules:
  - "Skip goals if user provided them."
  - "If single workstream, run task-breakdown only."
```
