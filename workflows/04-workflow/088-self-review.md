---
id: "088"
slug: "self-review"
title: "Run a Personal Review"
category: "workflow"
aliases:
  - self review
  - weekly review
  - retrospective
triggers:
  - weekly review
  - self review
  - retrospective
input_types:
  - period
  - data
output_types:
  - self-review
requires:
  - period (week, month, quarter)
  - highlights and lowlights
produces:
  - self-review
  - lessons learned
  - next-period commitments
related:
  - weekly-plan
  - goal-setting
playbooks: []
mode_support:
  - guide
  - quick
  - recommend
language_support:
  input: auto-detect
  output: mirror-user-language
localization:
  supported_locales:
    - en
    - zh-TW
  default_style_profile: zh-cn-friendly-professional
  locale_style_profile_overrides:
    zh-TW:
  editing_intensity: standard
handoff:
  - key: context
    description: "summary of upstream context"
---



# 088 — Run a Personal Review

## What is this?

Build a review: highlights, lowlights, lessons, and next-period commitments. Connect lessons to specific actions.

## Why use it?

Reflection is only useful when it changes behavior. A review converts experience into the next plan.

## When should I use it?

- End of week / month / quarter.
- You're stuck and want to reset.

## When should I not use it?

- You're auditing a project's outcomes — use project-risk (077).

## What should I prepare?

- Period.
- Highlights and lowlights.
- Goals (optional).

## How does the AI help me?

1. Confirm inputs.
2. Structure highlights/lowlights.
3. Draw lessons.
4. Propose next-period commitments.

## What will I get?

- Self-review.
- Lessons.
- Next-period commitments.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [weekly-plan](../04-workflow/074-weekly-plan.md)
- [goal-setting](../04-workflow/075-goal-setting.md)

## Recommended next steps

- goal-setting (075)
- weekly-plan (074)

---

## AI specification

```text
purpose: "Run a structured personal review for a chosen period."
required_inputs:
  - period (week, month, quarter)
  - highlights and lowlights
optional_inputs:
  - goals
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're auditing a project's outcomes — use project-risk (077)."
workflow:
  - "1. Confirm inputs."
  - "2. Structure highlights/lowlights."
  - "3. Draw lessons."
  - "4. Propose next-period commitments."
output_contract:
  - "self-review"
  - "lessons learned"
  - "next-period commitments"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: review
    description: structured review
  - key: next_commitments
    description: next-period commitments
```