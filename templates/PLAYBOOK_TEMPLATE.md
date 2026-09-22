---
playbook: example-playbook
slug: example-playbook
title: Example Playbook
mode_default: guide
stages: 4
---

# Example Playbook

## User scenario

Describe a concrete multi-step user situation in 2–4 sentences. Be specific about inputs and constraints.

## Intended final outcome

One sentence describing the artifact the user ends with.

## Workflow sequence

1. **[N — Slug](../workflows/<category>/<id>-<slug>.md)** — why this step comes first.
2. **[N — Slug](../workflows/<category>/<id>-<slug>.md)** — what changes because of step 1.
3. **[N — Slug](../workflows/<category>/<id>-<slug>.md)** — what changes because of step 2.

## Handoff data between steps

| From → To  | Key              | Description                          |
| ---------- | ---------------- | ------------------------------------ |
| step 1 → step 2 | `persona`    | Customer profile produced in step 1  |
| step 2 → step 3 | `comparison_table` | Competitor comparison produced in step 2 |

## Routing conditions

- Use this playbook when the user's stated goal fits the User scenario.
- Skip step 1 if the user already has a target customer profile (provide it as context).
- Skip step 3 if the user only wants a comparison, not a final recommendation.

## Skip conditions

- If the user asks for a specific workflow by name, run that workflow only.
- If a single workflow solves the user's question, do not run the playbook.

## Example start message

```
Read this repository's START.md and help me validate this business idea:

[describe the idea, the audience you have in mind, and any constraints]
```

## Final quality check

Before signing off, confirm:

- Each step's output contract was met.
- Assumptions and verification gaps were labeled.
- The final output includes the user's stated next-step criteria.

## AI specification

```yaml
playbook: <slug>
rule: "Start at the earliest missing dependency; do not force completed stages."
mode: "guide by default; allow quick mode when risk is low."
skip_rules:
  - "If user supplied the persona, skip step 1."
  - "If user wants comparison only, skip step 3."
```
