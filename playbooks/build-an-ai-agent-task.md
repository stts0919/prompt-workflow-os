---
playbook: build-an-ai-agent-task
slug: build-an-ai-agent-task
title: Build an AI Agent Task
mode_default: guide
stages: 4
---

# Build an AI Agent Task

## User scenario

You want to give an AI agent — a coding assistant, a workflow bot, an automation — a precise task so it returns useful results. You may have a vague goal, a half-formed spec, or working code you want hardened.

## Intended final outcome

A precise agent task specification with acceptance criteria, plus a reviewed implementation that meets the spec.

## Workflow sequence

1. **[091 — Spec an AI Agent Task](../workflows/05-technical/091-agent-task-spec.md)** — write the spec: objective, inputs, outputs, acceptance criteria, non-goals.
2. **[100 — Design a System](../workflows/05-technical/100-system-design.md)** — for non-trivial work, design the architecture before code.
3. **[093 — Generate Code](../workflows/05-technical/093-code-generation.md)** — produce code with tests against the spec.
4. **[095 — Review Code](../workflows/05-technical/095-code-review.md)** — audit correctness, security, performance, style, tests.

## Optional add-on

- If the spec is broad, first run **[089 — Design a Prompt from Scratch](../workflows/05-technical/089-prompt-designer.md)** for the agent's system prompt.
- If the code fails, run **[094 — Debug Failing Code](../workflows/05-technical/094-debugging.md)** before review.

## Handoff data between steps

| From → To    | Key                 | Description                                           |
| ------------ | ------------------- | ----------------------------------------------------- |
| step 1 → 2   | `agent_spec`        | Spec with objective and acceptance criteria           |
| step 2 → 3   | `architecture`      | Components, data flow, trade-offs                     |
| step 3 → 4   | `code` + `tests`    | Generated code with tests                             |

## Routing conditions

- Trigger phrases include "build an agent", "automate this", "implement this spec", "give the AI a task".
- Use when the user wants a precise AI-driven build with clear acceptance criteria.

## Skip conditions

- For trivial scripts, skip step 2.
- For pure prompt design, start at step 1 and end at step 1.
- If the user already has a spec, start at step 2 or 3.

## Example start message

```
Read this repository's START.md and help me build this AI agent task.

Goal: [what the agent should do]
Inputs: [what it sees]
Outputs: [what it produces]
Acceptance criteria: [how we judge success]
Constraints: [tech stack, hosting, budget]
```

## Final quality check

- Spec is testable.
- Architecture is consistent with the spec and constraints.
- Code includes tests against acceptance criteria.
- Review surfaces severity-tagged issues, with no blockers remaining.

## AI specification

```yaml
playbook: build-an-ai-agent-task
rule: "Skip architecture step for trivial scripts."
mode: "guide by default; allow quick mode when the user provides a complete spec."
skip_rules:
  - "For trivial scripts, skip architecture."
  - "If user supplied code, jump straight to review."
```
