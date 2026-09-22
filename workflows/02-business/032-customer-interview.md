---
id: "032"
slug: "customer-interview"
title: "Design Customer Interviews"
category: "business"
aliases:
  - interview script
  - user interview
  - discovery call
  - interview questions
triggers:
  - interview questions
  - user research script
  - discovery interview
  - research interview
input_types:
  - research goal
  - persona
  - topic
output_types:
  - interview script
  - consent note
requires:
  - research goal
  - persona or segment
  - topic boundaries
produces:
  - interview script (8–12 questions)
  - consent note
  - follow-up plan
related:
  - customer-persona
  - customer-feedback-analysis
  - research-plan
playbooks:
  - validate-a-business-idea
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



# 032 — Design Customer Interviews

## What is this?

Produce an interview script with an opener, behavior-anchored questions, follow-ups, and a closing note. Include the consent line and a recap plan.

## Why use it?

Leading questions confirm what you already believe. Behavior-anchored questions reveal what people actually do.

## When should I use it?

- You're validating a problem or solution.
- You're trying to understand how customers decide.

## When should I not use it?

- You have lots of interview transcripts and need synthesis — use customer-feedback-analysis (033).

## What should I prepare?

- Research goal.
- Persona or segment.
- Topic boundaries.

## How does the AI help me?

1. Confirm goal and persona.
2. Draft an opener that does not lead.
3. Build 8–12 behavior-anchored questions.
4. Add follow-ups and a wrap-up.
5. Include consent note.

## What will I get?

- Interview script.
- Consent line.
- Wrap-up plan.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [customer-persona](../02-business/031-customer-persona.md)
- [customer-feedback-analysis](../02-business/033-customer-feedback-analysis.md)
- [research-plan](../03-research/055-research-plan.md)

## Recommended next steps

- customer-feedback-analysis (033)

---

## AI specification

```text
purpose: "Create non-leading customer interview questions."
required_inputs:
  - research goal
  - persona or segment
  - topic boundaries
optional_inputs:
  - incentive
  - interview duration
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You have lots of interview transcripts and need synthesis — use customer-feedback-analysis (033)."
workflow:
  - "1. Confirm goal and persona."
  - "2. Draft an opener that does not lead."
  - "3. Build 8–12 behavior-anchored questions."
  - "4. Add follow-ups and a wrap-up."
  - "5. Include consent note."
output_contract:
  - "interview script (8–12 questions)"
  - "consent note"
  - "follow-up plan"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: interview_script
    description: ordered interview questions
  - key: consent_note
    description: consent statement
```