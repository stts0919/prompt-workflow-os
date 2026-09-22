---
id: "067"
slug: "counterargument"
title: "Build the Counter-Argument"
category: "research"
aliases:
  - counterargument
  - steelman the other side
  - devil's advocate
triggers:
  - counterargument
  - steelman
  - devils advocate
  - what's the other side
input_types:
  - argument
output_types:
  - counter-argument
requires:
  - argument or position
  - context
produces:
  - counter-argument
  - strongest counter-points
  - how to address them
related:
  - reasoning-audit
  - decision-memo
  - scenario-planning
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



# 067 — Build the Counter-Argument

## What is this?

Restate the position, then build the strongest counter-case using available evidence. Suggest how the original position can be reinforced.

## Why use it?

Stronger arguments survive contact with strong counter-arguments. Building them in advance is a sign of rigor.

## When should I use it?

- You're defending a position in writing.
- You want to stress-test a decision.

## When should I not use it?

- You want a logical audit — use reasoning-audit (066).

## What should I prepare?

- Position.
- Context.

## How does the AI help me?

1. Restate the position.
2. Build the strongest counter-case.
3. Identify the strongest counter-points.
4. Recommend responses.

## What will I get?

- Counter-argument.
- Strongest counter-points.
- Recommended responses.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [reasoning-audit](../03-research/066-reasoning-audit.md)
- [decision-memo](../03-research/069-decision-memo.md)
- [scenario-planning](../03-research/068-scenario-planning.md)

## Recommended next steps

- decision-memo (069)
- reasoning-audit (066)

---

## AI specification

```text
purpose: "Build the strongest counter-argument to a position."
required_inputs:
  - argument or position
  - context
optional_inputs:
  - target audience
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You want a logical audit — use reasoning-audit (066)."
workflow:
  - "1. Restate the position."
  - "2. Build the strongest counter-case."
  - "3. Identify the strongest counter-points."
  - "4. Recommend responses."
output_contract:
  - "counter-argument"
  - "strongest counter-points"
  - "how to address them"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: counter_argument
    description: strongest counter-argument
  - key: responses
    description: how to address them
```