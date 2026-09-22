---
id: "081"
slug: "checklist-builder"
title: "Build a Checklist"
category: "workflow"
aliases:
  - checklist
  - todo list
  - preflight
triggers:
  - checklist
  - preflight
  - verification list
input_types:
  - process
output_types:
  - checklist
requires:
  - process or context
  - verification criteria
produces:
  - checklist
  - grouping by phase
  - verification rules
related:
  - sop-builder
  - documentation-template
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



# 081 — Build a Checklist

## What is this?

Produce a checklist grouped by phase or role, with verification rules where useful.

## Why use it?

Checklists beat memory. Even experts miss steps under pressure; checklists catch them cheaply.

## When should I use it?

- You're running a recurring process.
- You want a pre-flight check before shipping.

## When should I not use it?

- The process is poorly defined — use sop-builder (080) first.

## What should I prepare?

- Process context.
- Common omissions or past mistakes.

## How does the AI help me?

1. Confirm context.
2. List the steps.
3. Group by phase.
4. Add verification rules where helpful.

## What will I get?

- Grouped checklist.
- Verification rules.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [sop-builder](../04-workflow/080-sop-builder.md)
- [documentation-template](../04-workflow/082-documentation-template.md)

## Recommended next steps

- sop-builder (080)

---

## AI specification

```text
purpose: "Build a checklist that catches the most common omissions."
required_inputs:
  - process or context
  - verification criteria
optional_inputs:
  - roles
  - frequencies
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "The process is poorly defined — use sop-builder (080) first."
workflow:
  - "1. Confirm context."
  - "2. List the steps."
  - "3. Group by phase."
  - "4. Add verification rules where helpful."
output_contract:
  - "checklist"
  - "grouping by phase"
  - "verification rules"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: checklist
    description: grouped checklist
  - key: verification_rules
    description: rules per item
```