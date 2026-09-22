---
id: "011"
slug: "newsletter"
title: "Write a Newsletter"
category: "content"
aliases:
  - newsletter issue
  - email newsletter
  - mailing
triggers:
  - newsletter
  - send an email update
  - weekly newsletter
input_types:
  - theme or topic
  - audience
  - previous issues
output_types:
  - newsletter issue
  - subject lines
  - preview text
requires:
  - theme or topic
  - audience profile
  - voice reference
produces:
  - newsletter copy
  - subject line variants
  - preview text variants
related:
  - email-sequence
  - article-draft
  - content-calendar
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



# 011 — Write a Newsletter

## What is this?

Write a complete newsletter issue (lede, body, sections, footer) for a known audience. Provide three subject line variants and three preview text variants.

## Why use it?

Newsletters are the highest-trust one-to-many channel for many creators. A consistent format and a tight subject line set compound open rates over time.

## When should I use it?

- You're publishing a regular newsletter.
- You have an underused email list.

## When should I not use it?

- You're building a multi-step automated sequence — use email-sequence (046).
- You want a one-time announcement — consider campaign-plan (045) instead.

## What should I prepare?

- Theme or topic.
- Audience profile.
- Voice reference or previous issues.

## How does the AI help me?

1. Confirm theme and audience.
2. Draft the issue with sections and a clear lede.
3. Generate subject-line and preview-text variants.
4. Add plain-text fallback for email clients that strip CSS.

## What will I get?

- Newsletter copy.
- 3 subject line variants.
- 3 preview text variants.
- Plain-text fallback.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [email-sequence](../02-business/046-email-sequence.md)
- [article-draft](../01-content/007-article-draft.md)
- [content-calendar](../01-content/004-content-calendar.md)

## Recommended next steps

- email-sequence (046)
- content-quality-review (029)

---

## AI specification

```text
purpose: "Produce a single newsletter issue with subject-line variants and preview text."
required_inputs:
  - theme or topic
  - audience profile
  - voice reference
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're building a multi-step automated sequence — use email-sequence (046)."
  - "You want a one-time announcement — consider campaign-plan (045) instead."
workflow:
  - "1. Confirm theme and audience."
  - "2. Draft the issue with sections and a clear lede."
  - "3. Generate subject-line and preview-text variants."
  - "4. Add plain-text fallback for email clients that strip CSS."
output_contract:
  - "newsletter copy"
  - "subject line variants"
  - "preview text variants"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: issue_copy
    description: full newsletter text
  - key: subject_variants
    description: subject line options
```