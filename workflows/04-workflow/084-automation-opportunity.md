---
id: "084"
slug: "automation-opportunity"
title: "Find Automation Opportunities"
category: "workflow"
aliases:
  - automation
  - what to automate
  - automate this
triggers:
  - automate this
  - what should i automate
  - find automation
input_types:
  - processes
  - tools
output_types:
  - automation candidates
requires:
  - process list
  - current tools
produces:
  - automation candidates
  - ROI notes
  - risk notes
related:
  - sop-builder
  - task-breakdown
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



# 084 — Find Automation Opportunities

## What is this?

Score processes on volume, error cost, and automation cost. Recommend the top 3 with ROI notes and risk notes.

## Why use it?

Most teams automate the wrong things first. A scoring rubric reveals which automation actually pays back.

## When should I use it?

- You're feeling manual work piling up.
- You want to pitch automation to leadership.

## When should I not use it?

- You're documenting one process — use sop-builder (080).

## What should I prepare?

- Process list.
- Current tools.

## How does the AI help me?

1. Confirm inputs.
2. Score each process.
3. Recommend the top 3.
4. Add risk and ROI notes.

## What will I get?

- Top 3 candidates.
- Scoring rationale.
- Risk and ROI notes.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [sop-builder](../04-workflow/080-sop-builder.md)
- [task-breakdown](../04-workflow/072-task-breakdown.md)

## Recommended next steps

- sop-builder (080)
- task-breakdown (072)

---

## AI specification

```text
purpose: "Identify and prioritize automation opportunities."
required_inputs:
  - process list
  - current tools
optional_inputs:
  - effort estimates
  - stakeholders
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're documenting one process — use sop-builder (080)."
workflow:
  - "1. Confirm inputs."
  - "2. Score each process."
  - "3. Recommend the top 3."
  - "4. Add risk and ROI notes."
output_contract:
  - "automation candidates"
  - "ROI notes"
  - "risk notes"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: candidates
    description: top automation candidates
  - key: roi_notes
    description: ROI rationale
```