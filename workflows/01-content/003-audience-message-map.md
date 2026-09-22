---
id: "003"
slug: "audience-message-map"
title: "Map Audience Messages"
category: "content"
aliases:
  - audience map
  - message map
  - awareness levels
  - message matrix
triggers:
  - map my audience
  - write for different awareness levels
  - message by segment
  - what to say to whom
input_types:
  - audience segments
  - product or topic
  - awareness levels
output_types:
  - message map
  - segment matrix
  - call to action matrix
requires:
  - audience segments
  - product, service or topic
  - awareness stages (problem-aware, solution-aware, etc.)
produces:
  - message map
  - segment × stage matrix
  - tailored CTAs per cell
related:
  - customer-persona
  - content-pillar-design
  - marketing-funnel
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



# 003 — Map Audience Messages

## What is this?

Build a 2-axis map: audience segment on one axis, awareness level on the other. For each cell, write the headline message, the supporting proof, and the call to action.

## Why use it?

A single message for everyone ignores where the reader is in their journey. Mapping segments to stages prevents both over-selling to novices and under-selling to ready buyers.

## When should I use it?

- Conversion is uneven — some segments engage, others bounce.
- You're scaling content and need predictable message patterns.
- Sales calls keep repeating "we didn't realize this was for us".

## When should I not use it?

- You don't yet know who the audience is — start with customer-persona (031).
- You only need one piece of content — skip the map and write directly.

## What should I prepare?

- Audience segments (2–5).
- Awareness levels you care about.
- Product or topic summary.

## How does the AI help me?

1. Confirm segments and stages.
2. Define the message per cell (headline, proof, CTA).
3. Highlight cells where the message is risky or unsupported.
4. Suggest a follow-up playbook to test one segment first.

## What will I get?

- A segment × stage message matrix.
- CTA per cell.
- Risk flags for unsupported cells.
- Next-workflow suggestion: marketing-funnel (044).

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [customer-persona](../02-business/031-customer-persona.md)
- [content-pillar-design](../01-content/002-content-pillar-design.md)
- [marketing-funnel](../02-business/044-marketing-funnel.md)

## Recommended next steps

- marketing-funnel (044)
- campaign-plan (045)

---

## AI specification

```text
purpose: "Match each audience segment to the right message and call to action across awareness levels."
required_inputs:
  - audience segments
  - product, service or topic
  - awareness stages (problem-aware, solution-aware, etc.)
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You don't yet know who the audience is — start with customer-persona (031)."
  - "You only need one piece of content — skip the map and write directly."
workflow:
  - "1. Confirm segments and stages."
  - "2. Define the message per cell (headline, proof, CTA)."
  - "3. Highlight cells where the message is risky or unsupported."
  - "4. Suggest a follow-up playbook to test one segment first."
output_contract:
  - "message map"
  - "segment × stage matrix"
  - "tailored CTAs per cell"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: message_matrix
    description: segment × stage map with headlines and CTAs
```