---
id: "066"
slug: "reasoning-audit"
title: "Audit Your Reasoning"
category: "research"
aliases:
  - reasoning audit
  - logic check
  - check my reasoning
triggers:
  - check my reasoning
  - audit my logic
  - is this argument sound
input_types:
  - argument
output_types:
  - reasoning audit
requires:
  - argument text
  - audience
produces:
  - logical gaps
  - fallacy checks
  - suggested fixes
related:
  - counterargument
  - evidence-matrix
  - decision-memo
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



# 066 — Audit Your Reasoning

## What is this?

Walk through the argument step by step. Identify logical gaps, unstated assumptions, and known fallacies. Recommend fixes.

## Why use it?

Most reasoning errors hide in unstated assumptions. An audit surfaces them before they become decisions.

## When should I use it?

- You're preparing a memo or strategy document.
- You want to challenge your own argument.

## When should I not use it?

- You want counter-evidence — use counterargument (067).

## What should I prepare?

- Argument text.
- Audience.

## How does the AI help me?

1. Identify the conclusion.
2. Walk through the steps.
3. Flag gaps and assumptions.
4. Recommend fixes.

## What will I get?

- Step-by-step trace.
- Logical gaps.
- Suggested fixes.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [counterargument](../03-research/067-counterargument.md)
- [evidence-matrix](../03-research/065-evidence-matrix.md)
- [decision-memo](../03-research/069-decision-memo.md)

## Recommended next steps

- counterargument (067)
- decision-memo (069)

---

## AI specification

```text
purpose: "Audit the reasoning behind an argument."
required_inputs:
  - argument text
  - audience
optional_inputs:
  - target conclusion
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You want counter-evidence — use counterargument (067)."
workflow:
  - "1. Identify the conclusion."
  - "2. Walk through the steps."
  - "3. Flag gaps and assumptions."
  - "4. Recommend fixes."
output_contract:
  - "logical gaps"
  - "fallacy checks"
  - "suggested fixes"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: gaps
    description: list of logical gaps
  - key: fixes
    description: recommended corrections
```