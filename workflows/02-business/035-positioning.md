---
id: "035"
slug: "positioning"
title: "Create Positioning"
category: "business"
aliases:
  - positioning statement
  - market position
  - positioning canvas
triggers:
  - positioning
  - where do we sit
  - market position
input_types:
  - customer
  - competitors
  - offer
output_types:
  - positioning statement
  - positioning canvas
requires:
  - customer
  - competitor landscape
  - offer
produces:
  - positioning statement
  - positioning canvas
  - alternative positions
related:
  - value-proposition
  - competitor-analysis
  - brand-voice-guide
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



# 035 — Create Positioning

## What is this?

Produce a positioning statement that names the target customer, the alternative, the value, and the reason to believe. Provide one alternative position.

## Why use it?

Positioning determines every downstream choice — pricing, channels, messages. Vague positioning leaks revenue.

## When should I use it?

- You're launching a new product or refreshing an old one.
- Your team disagrees on who you are for.

## When should I not use it?

- You only need a tag-line — use headline-generation (020).
- You're writing a sales page — use sales-page (043).

## What should I prepare?

- Customer profile.
- Competitor landscape.
- Offer summary.

## How does the AI help me?

1. Confirm inputs.
2. Draft a positioning statement.
3. Generate one alternative position.
4. Test against competitor language.

## What will I get?

- Positioning statement.
- Alternative position.
- Sanity check against competitors.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [value-proposition](../02-business/036-value-proposition.md)
- [competitor-analysis](../02-business/034-competitor-analysis.md)
- [brand-voice-guide](../01-content/023-brand-voice-guide.md)

## Recommended next steps

- value-proposition (036)
- sales-page (043)

---

## AI specification

```text
purpose: "Write a focused positioning statement."
required_inputs:
  - customer
  - competitor landscape
  - offer
optional_inputs:
  - current positioning
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You only need a tag-line — use headline-generation (020)."
  - "You're writing a sales page — use sales-page (043)."
workflow:
  - "1. Confirm inputs."
  - "2. Draft a positioning statement."
  - "3. Generate one alternative position."
  - "4. Test against competitor language."
output_contract:
  - "positioning statement"
  - "positioning canvas"
  - "alternative positions"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: positioning_statement
    description: the chosen position
  - key: alternative_position
    description: backup position
```