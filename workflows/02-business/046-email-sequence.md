---
id: "046"
slug: "email-sequence"
title: "Build an Email Sequence"
category: "business"
aliases:
  - drip campaign
  - email automation
  - sequence
triggers:
  - email sequence
  - drip campaign
  - nurture sequence
  - automated emails
input_types:
  - goal
  - audience
  - trigger
output_types:
  - email sequence
  - subject lines
requires:
  - sequence goal
  - audience
  - entry trigger
produces:
  - per-email copy
  - subject lines
  - preview text
  - send timing
related:
  - newsletter
  - marketing-funnel
  - sales-page
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
  default_style_profile: zh-tw-email-professional
  locale_style_profile_overrides:
    zh-TW:
  editing_intensity: standard
handoff:
  - key: context
    description: "summary of upstream context"
---



# 046 — Build an Email Sequence

## What is this?

Design a multi-email sequence (typically 3–7 emails) with subject lines, body copy, preview text, send timing, and exit conditions.

## Why use it?

One-off emails convert only at the moment of intent. A timed sequence nudges people back into a decision.

## When should I use it?

- You're onboarding new users.
- You're launching a campaign that needs follow-up.

## When should I not use it?

- You only need a single newsletter issue — use newsletter (011).

## What should I prepare?

- Sequence goal.
- Audience and trigger.
- Tone.

## How does the AI help me?

1. Confirm goal, audience, trigger.
2. Sequence the emails (3–7).
3. Write subject lines and body.
4. Add timing and exit conditions.

## What will I get?

- Per-email copy.
- Subject lines and preview text.
- Timing and exit conditions.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [newsletter](../01-content/011-newsletter.md)
- [marketing-funnel](../02-business/044-marketing-funnel.md)
- [sales-page](../02-business/043-sales-page.md)

## Recommended next steps

- content-quality-review (029)
- marketing-funnel (044)

---

## AI specification

```text
purpose: "Design a triggered email sequence with the right cadence and goal."
required_inputs:
  - sequence goal
  - audience
  - entry trigger
optional_inputs:
  - tone guide
  - deliverability constraints
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You only need a single newsletter issue — use newsletter (011)."
workflow:
  - "1. Confirm goal, audience, trigger."
  - "2. Sequence the emails (3–7)."
  - "3. Write subject lines and body."
  - "4. Add timing and exit conditions."
output_contract:
  - "per-email copy"
  - "subject lines"
  - "preview text"
  - "send timing"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: email_sequence
    description: ordered emails with timing
  - key: exit_conditions
    description: rules to remove from sequence
```