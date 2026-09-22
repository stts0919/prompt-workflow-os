---
id: "025"
slug: "case-study"
title: "Write a Case Study"
category: "content"
aliases:
  - customer story
  - success story
  - case write-up
triggers:
  - case study
  - customer story
  - success story
  - write up a project
input_types:
  - project or customer outcome
  - metrics
  - testimonial
output_types:
  - case study
requires:
  - project description
  - outcome metrics
  - optional customer testimonial
produces:
  - structured case study (challenge, approach, result, takeaways)
related:
  - storytelling
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
  default_style_profile: zh-tw-long-form-article
  locale_style_profile_overrides:
    zh-TW:
  editing_intensity: standard
handoff:
  - key: context
    description: "summary of upstream context"
---



# 025 — Write a Case Study

## What is this?

Convert a project description into a structured case study that includes the customer's challenge, the approach, the result (with metrics), and the takeaways. Quote the customer where appropriate.

## Why use it?

B2B buyers trust peer outcomes more than vendor claims. A clear case study is one of the highest-ROI sales assets you can produce.

## When should I use it?

- You finished a successful project with measurable outcomes.
- Your sales team needs an asset for late-stage prospects.

## When should I not use it?

- You're documenting your own learning — use self-review (088).
- You're capturing results from a customer interview — use customer-interview (032).

## What should I prepare?

- Project description.
- Outcome metrics or changes.
- Optional: customer testimonial.

## How does the AI help me?

1. Identify the customer's challenge in one sentence.
2. Describe the approach in concrete steps.
3. Show results with before/after metrics.
4. Add customer quote and a takeaways section.

## What will I get?

- Case study (challenge → approach → result → takeaways).
- Pull-quote highlights.
- Suggested next workflow: sales-page (043).

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [storytelling](../01-content/024-storytelling.md)
- [marketing-funnel](../02-business/044-marketing-funnel.md)
- [sales-page](../02-business/043-sales-page.md)

## Recommended next steps

- sales-page (043)
- marketing-funnel (044)

---

## AI specification

```text
purpose: "Turn a project or customer outcome into a credible case study."
required_inputs:
  - project description
  - outcome metrics
  - optional customer testimonial
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're documenting your own learning — use self-review (088)."
  - "You're capturing results from a customer interview — use customer-interview (032)."
workflow:
  - "1. Identify the customer's challenge in one sentence."
  - "2. Describe the approach in concrete steps."
  - "3. Show results with before/after metrics."
  - "4. Add customer quote and a takeaways section."
output_contract:
  - "structured case study (challenge, approach, result, takeaways)"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: case_study
    description: structured case study text
  - key: metrics
    description: before/after metrics
```