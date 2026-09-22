---
id: "072"
slug: "task-breakdown"
title: "Break a Task Down"
category: "workflow"
aliases:
  - task breakdown
  - subtasks
  - decompose task
triggers:
  - break this down
  - decompose this task
  - what are the steps
input_types:
  - task
  - context
output_types:
  - task tree
requires:
  - task description
  - definition of done
produces:
  - task tree
  - time estimates
  - dependencies
related:
  - priority-planning
  - weekly-plan
  - project-plan
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



# 072 — Break a Task Down

## What is this?

Produce a task tree with 3–7 levels of depth, time estimates, dependencies, and acceptance criteria per leaf.

## Why use it?

Unbroken tasks are skipped. Tasks with explicit subtasks and clear "done" conditions ship more reliably.

## When should I use it?

- You're staring at a fuzzy task.
- You're estimating effort and need structure.

## When should I not use it?

- You already have a project plan — use task-breakdown as the leaf step there.

## What should I prepare?

- Task description.
- Definition of done.

## How does the AI help me?

1. Confirm task and definition of done.
2. Break into subtasks.
3. Time each.
4. Mark dependencies.
5. Add acceptance criteria.

## What will I get?

- Task tree.
- Estimates.
- Dependencies.
- Acceptance criteria.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [priority-planning](../04-workflow/073-priority-planning.md)
- [weekly-plan](../04-workflow/074-weekly-plan.md)
- [project-plan](../04-workflow/076-project-plan.md)

## Recommended next steps

- priority-planning (073)
- weekly-plan (074)

---

## AI specification

```text
purpose: "Break a task into actionable subtasks with clear definitions of done."
required_inputs:
  - task description
  - definition of done
optional_inputs:
  - skills needed
  - dependencies
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You already have a project plan — use task-breakdown as the leaf step there."
workflow:
  - "1. Confirm task and definition of done."
  - "2. Break into subtasks."
  - "3. Time each."
  - "4. Mark dependencies."
  - "5. Add acceptance criteria."
output_contract:
  - "task tree"
  - "time estimates"
  - "dependencies"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: task_tree
    description: subtasks with estimates
  - key: acceptance_criteria
    description: done conditions
```