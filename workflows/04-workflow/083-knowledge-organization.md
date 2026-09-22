---
id: "083"
slug: "knowledge-organization"
title: "Organize a Knowledge Base"
category: "workflow"
aliases:
  - organize notes
  - knowledge organization
  - taxonomy
  - wiki
triggers:
  - organize notes
  - knowledge base
  - set up a wiki
input_types:
  - content corpus
output_types:
  - information architecture
requires:
  - content corpus or domain
  - users
produces:
  - information architecture
  - taxonomy
  - naming rules
related:
  - documentation-template
  - knowledge-map
  - classification
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



# 083 — Organize a Knowledge Base

## What is this?

Produce an information architecture: top-level categories, subcategories, naming rules, and tagging conventions.

## Why use it?

A messy knowledge base wastes more time than it saves. A clean architecture turns notes into leverage.

## When should I use it?

- Your team notes are scattered.
- You're setting up a wiki or Notion space.

## When should I not use it?

- You're writing one document — use documentation-template (082).

## What should I prepare?

- Content or domain summary.
- User roles.
- Existing taxonomy (optional).

## How does the AI help me?

1. Confirm inputs.
2. Propose categories.
3. Set naming rules.
4. Define tagging conventions.

## What will I get?

- Information architecture.
- Naming rules.
- Tagging conventions.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [documentation-template](../04-workflow/082-documentation-template.md)
- [knowledge-map](../03-research/062-knowledge-map.md)
- [classification](../03-research/061-classification.md)

## Recommended next steps

- documentation-template (082)

---

## AI specification

```text
purpose: "Design an information architecture for a knowledge base."
required_inputs:
  - content corpus or domain
  - users
optional_inputs:
  - existing taxonomy
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're writing one document — use documentation-template (082)."
workflow:
  - "1. Confirm inputs."
  - "2. Propose categories."
  - "3. Set naming rules."
  - "4. Define tagging conventions."
output_contract:
  - "information architecture"
  - "taxonomy"
  - "naming rules"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: architecture
    description: categories and subcategories
  - key: naming_rules
    description: naming conventions
```