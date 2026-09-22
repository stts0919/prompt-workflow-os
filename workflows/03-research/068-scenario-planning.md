---
id: "068"
slug: "scenario-planning"
title: "Plan Across Scenarios"
category: "research"
aliases:
  - scenarios
  - scenario planning
  - what if
triggers:
  - scenarios
  - what if
  - scenario planning
  - futures
input_types:
  - decision context
  - drivers
output_types:
  - scenario set
requires:
  - decision context
  - key drivers (2–3)
  - time horizon
produces:
  - 3–4 scenarios
  - trigger indicators
  - implications
related:
  - risk-stress-test
  - decision-memo
  - business-decision
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



# 068 — Plan Across Scenarios

## What is this?

Build 3–4 distinct scenarios from the chosen drivers. For each, describe the situation, the trigger indicators, and the implications for the decision.

## Why use it?

Single-point forecasts fail when conditions change. Scenario planning builds robustness under uncertainty.

## When should I use it?

- You're making a long-horizon decision.
- A board wants to stress-test strategy.

## When should I not use it?

- You're consolidating existing evidence — use evidence-matrix (065).

## What should I prepare?

- Decision context.
- Key drivers.

## How does the AI help me?

1. Confirm inputs.
2. Build 3–4 scenarios.
3. Define trigger indicators.
4. List implications.

## What will I get?

- Scenario set.
- Trigger indicators.
- Implications per scenario.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [risk-stress-test](../02-business/053-risk-stress-test.md)
- [decision-memo](../03-research/069-decision-memo.md)
- [business-decision](../02-business/052-business-decision.md)

## Recommended next steps

- business-decision (052)
- risk-stress-test (053)

---

## AI specification

```text
purpose: "Plan across 3–4 plausible futures."
required_inputs:
  - decision context
  - key drivers (2–3)
  - time horizon
optional_inputs:
  - internal constraints
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're consolidating existing evidence — use evidence-matrix (065)."
workflow:
  - "1. Confirm inputs."
  - "2. Build 3–4 scenarios."
  - "3. Define trigger indicators."
  - "4. List implications."
output_contract:
  - "3–4 scenarios"
  - "trigger indicators"
  - "implications"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: scenarios
    description: distinct futures
  - key: trigger_indicators
    description: signals to watch
```