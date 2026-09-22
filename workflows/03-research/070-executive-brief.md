---
id: "070"
slug: "executive-brief"
title: "Write an Executive Brief"
category: "research"
aliases:
  - exec brief
  - brief
  - leadership brief
triggers:
  - exec brief
  - executive brief
  - leadership update
input_types:
  - topic
  - audience
output_types:
  - 1-page executive brief
requires:
  - topic or decision
  - executive audience
  - key facts
produces:
  - 1-page brief
  - recommendation
  - ask
related:
  - decision-memo
  - report-review
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
  default_style_profile: zh-tw-business-consulting
  locale_style_profile_overrides:
    zh-TW:
  editing_intensity: strict_precision
handoff:
  - key: context
    description: "summary of upstream context"
---



# 070 — Write an Executive Brief

## What is this?

Produce a one-page brief: bottom line, why now, key facts, risks, recommended actions, and the ask.

## Why use it?

Executives want the bottom line first. A short brief saves time and earns the next meeting.

## When should I use it?

- You're briefing executives.
- You're preparing for a board update.

## When should I not use it?

- The decision needs full criteria — use decision-memo (069).

## What should I prepare?

- Topic or decision.
- Key facts.
- Audience.

## How does the AI help me?

1. Confirm inputs.
2. Write bottom line.
3. Add why now, key facts, risks, actions, ask.
4. Trim to one page.

## What will I get?

- One-page brief.
- Bottom line.
- Ask.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [decision-memo](../03-research/069-decision-memo.md)
- [report-review](../03-research/071-report-review.md)

## Recommended next steps

- decision-memo (069)
- report-review (071)

---

## AI specification

```text
purpose: "Compress a topic or decision into a one-page brief for executives."
required_inputs:
  - topic or decision
  - executive audience
  - key facts
optional_inputs:
  - constraints
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "The decision needs full criteria — use decision-memo (069)."
workflow:
  - "1. Confirm inputs."
  - "2. Write bottom line."
  - "3. Add why now, key facts, risks, actions, ask."
  - "4. Trim to one page."
output_contract:
  - "1-page brief"
  - "recommendation"
  - "ask"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: brief
    description: one-page brief
  - key: ask
    description: explicit decision requested
```