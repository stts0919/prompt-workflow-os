---
id: "022"
slug: "faq-creation"
title: "Create FAQs"
category: "content"
aliases:
  - faq
  - frequently asked questions
  - qa page
  - questions and answers
triggers:
  - faq
  - questions and answers
  - make a faq
  - common questions
input_types:
  - product or service
  - audience
  - existing questions
output_types:
  - FAQ list
  - categorized questions
requires:
  - product or service description
  - audience
  - any existing customer questions
produces:
  - categorized FAQ
  - short-form answers
  - suggested long-form articles
related:
  - customer-feedback-analysis
  - content-repurposing
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
  default_style_profile: zh-tw-customer-support
  locale_style_profile_overrides:
    zh-TW:
  editing_intensity: standard
handoff:
  - key: context
    description: "summary of upstream context"
---



# 022 — Create FAQs

## What is this?

Draft an FAQ grouped by category, with concise answers and pointers to long-form articles where useful.

## Why use it?

An FAQ catches the most common support questions, removes friction before conversion, and improves SEO on long-tail queries.

## When should I use it?

- You're launching a product or service.
- Your support team keeps answering the same questions.
- You want a public "common questions" page.

## When should I not use it?

- You're responding to specific public comments — use comment-response (026).
- You're capturing real customer questions before launching — start with customer-interview (032).

## What should I prepare?

- Product or service summary.
- Existing questions or support tickets.
- Audience.

## How does the AI help me?

1. Read product summary and any supplied questions.
2. Group by category.
3. Write concise answers and link to long-form where useful.
4. Flag questions that need a domain expert.

## What will I get?

- Categorized FAQ.
- Short-form answers.
- Suggestions for follow-up articles.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [customer-feedback-analysis](../02-business/033-customer-feedback-analysis.md)
- [content-repurposing](../01-content/028-content-repurposing.md)

## Recommended next steps

- article-outline (006)
- sales-page (043)

---

## AI specification

```text
purpose: "Convert product, service, or policy information into an FAQ for a chosen audience."
required_inputs:
  - product or service description
  - audience
  - any existing customer questions
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're responding to specific public comments — use comment-response (026)."
  - "You're capturing real customer questions before launching — start with customer-interview (032)."
workflow:
  - "1. Read product summary and any supplied questions."
  - "2. Group by category."
  - "3. Write concise answers and link to long-form where useful."
  - "4. Flag questions that need a domain expert."
output_contract:
  - "categorized FAQ"
  - "short-form answers"
  - "suggested long-form articles"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: faq
    description: categorized question list with answers
```