---
id: "077"
slug: "project-risk"
title: "Manage Project Risks"
category: "workflow"
aliases:
  - risk management
  - project risks
  - risk register
triggers:
  - risk register
  - project risks
  - what could go wrong
input_types:
  - project
  - risks
output_types:
  - risk register
requires:
  - project or plan
  - known risks
produces:
  - risk register
  - mitigations
  - owners
related:
  - project-plan
  - risk-stress-test
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



# 077 — Manage Project Risks

## What is this?

Build a risk register: risk statement, likelihood, impact, score, mitigation, owner.

## Why use it?

Risks that aren't tracked become incidents. A risk register makes risk visible and assignable.

## When should I use it?

- You start any non-trivial project.
- A project slips and you want to reset.

## When should I not use it?

- You want scenario planning for the future — use scenario-planning (068).

## What should I prepare?

- Project summary.
- Known risks.

## How does the AI help me?

1. Confirm inputs.
2. List risks.
3. Score likelihood and impact.
4. Assign mitigations and owners.

## What will I get?

- Risk register.
- Mitigations.
- Owners.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [project-plan](../04-workflow/076-project-plan.md)
- [risk-stress-test](../02-business/053-risk-stress-test.md)

## Recommended next steps

- project-plan (076)
- weekly-plan (074)

---

## AI specification

```text
purpose: "Identify, score, and mitigate project-level risks."
required_inputs:
  - project or plan
  - known risks
optional_inputs:
  - stakeholders
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You want scenario planning for the future — use scenario-planning (068)."
workflow:
  - "1. Confirm inputs."
  - "2. List risks."
  - "3. Score likelihood and impact."
  - "4. Assign mitigations and owners."
output_contract:
  - "risk register"
  - "mitigations"
  - "owners"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: risk_register
    description: scored risks
  - key: mitigations
    description: actions to reduce risk
```