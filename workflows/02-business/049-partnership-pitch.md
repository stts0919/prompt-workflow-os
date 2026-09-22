---
id: "049"
slug: "partnership-pitch"
title: "Pitch a Partnership"
category: "business"
aliases:
  - partner pitch
  - partnership
  - joint venture
triggers:
  - partner pitch
  - partnership
  - joint venture
  - co-marketing
input_types:
  - partner
  - goal
  - offer
output_types:
  - partnership pitch deck or memo
requires:
  - partner profile
  - goal
  - your offer
produces:
  - partnership pitch memo
  - joint value story
  - next steps
related:
  - cold-outreach
  - value-proposition
  - case-study
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



# 049 — Pitch a Partnership

## What is this?

Write a partnership pitch: who you are, who they are, the joint opportunity, the structure, the ask. Keep it to one page.

## Why use it?

Most partnership pitches focus on one side. Framing joint value earns attention faster than pitching alone.

## When should I use it?

- You're approaching a potential partner.
- A partner approached you and you need a structured response.

## When should I not use it?

- You're selling to a customer — use cold-outreach (047) or sales-page (043).

## What should I prepare?

- Partner profile.
- Goal.
- Your offer.

## How does the AI help me?

1. Confirm partner and goal.
2. Frame the joint value.
3. Propose structures (co-marketing, bundling, distribution).
4. State the next step clearly.

## What will I get?

- Partnership pitch memo.
- Joint value story.
- Next step.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [cold-outreach](../02-business/047-cold-outreach.md)
- [value-proposition](../02-business/036-value-proposition.md)
- [case-study](../01-content/025-case-study.md)

## Recommended next steps

- email-sequence (046)
- case-study (025)

---

## AI specification

```text
purpose: "Build a partnership pitch that earns a meeting."
required_inputs:
  - partner profile
  - goal
  - your offer
optional_inputs:
  - case study
  - audience overlap
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're selling to a customer — use cold-outreach (047) or sales-page (043)."
workflow:
  - "1. Confirm partner and goal."
  - "2. Frame the joint value."
  - "3. Propose structures (co-marketing, bundling, distribution)."
  - "4. State the next step clearly."
output_contract:
  - "partnership pitch memo"
  - "joint value story"
  - "next steps"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: pitch_memo
    description: one-page pitch
  - key: joint_value
    description: explanation of mutual benefit
```