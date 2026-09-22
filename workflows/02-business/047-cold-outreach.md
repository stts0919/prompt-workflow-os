---
id: "047"
slug: "cold-outreach"
title: "Draft Cold Outreach"
category: "business"
aliases:
  - cold email
  - cold pitch
  - outreach
triggers:
  - cold email
  - cold outreach
  - intro email
  - first contact
input_types:
  - recipient
  - context
  - ask
output_types:
  - outreach variants
requires:
  - recipient context
  - the ask
  - your credibility
produces:
  - outreach variants
  - subject lines
  - follow-up variants
related:
  - email-sequence
  - partnership-pitch
  - sales-objection-handling
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



# 047 — Draft Cold Outreach

## What is this?

Write a short, specific outreach email or message. Provide subject lines and a follow-up.

## Why use it?

Cold outreach fails when it talks about the sender. The recipient should see relevance in the first sentence.

## When should I use it?

- You're reaching out to a prospect, partner, or press contact.
- Your open rates are low on cold emails.

## When should I not use it?

- You're replying to a known prospect — use sales-objection-handling (048).

## What should I prepare?

- Recipient context.
- The ask.
- Your credibility line.

## How does the AI help me?

1. Confirm recipient and ask.
2. Write a 4–7 sentence email.
3. Provide a subject line and follow-up variant.
4. Sanity-check for warmth vs creepiness.

## What will I get?

- Outreach copy.
- Subject line variants.
- Follow-up variant.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [email-sequence](../02-business/046-email-sequence.md)
- [partnership-pitch](../02-business/049-partnership-pitch.md)
- [sales-objection-handling](../02-business/048-sales-objection-handling.md)

## Recommended next steps

- sales-objection-handling (048)
- email-sequence (046)

---

## AI specification

```text
purpose: "Draft cold outreach that earns a reply."
required_inputs:
  - recipient context
  - the ask
  - your credibility
optional_inputs:
  - tone
  - channels (email vs DM)
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're replying to a known prospect — use sales-objection-handling (048)."
workflow:
  - "1. Confirm recipient and ask."
  - "2. Write a 4–7 sentence email."
  - "3. Provide a subject line and follow-up variant."
  - "4. Sanity-check for warmth vs creepiness."
output_contract:
  - "outreach variants"
  - "subject lines"
  - "follow-up variants"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: outreach_copy
    description: short cold email/message
  - key: follow_up
    description: follow-up variant
```