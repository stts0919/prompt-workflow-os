---
id: "061"
slug: "classification"
title: "Classify Items into Buckets"
category: "research"
aliases:
  - classify
  - categorize
  - tagging
triggers:
  - classify
  - categorize
  - sort into buckets
  - tag these
input_types:
  - items
  - categories
output_types:
  - classification result
requires:
  - items list
  - taxonomy or categories
  - rules
produces:
  - classification per item
  - ambiguous flags
related:
  - data-extraction
  - knowledge-organization
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



# 061 — Classify Items into Buckets

## What is this?

Apply the taxonomy to each item and produce a classification. Flag items that don't fit cleanly.

## Why use it?

Manual classification is slow and inconsistent. A consistent rubric surfaces edge cases and patterns.

## When should I use it?

- You have customer feedback to triage.
- You want to bucket transactions or inventory.

## When should I not use it?

- You want a free-form summary — use document-summary (058).

## What should I prepare?

- Items list.
- Taxonomy.
- Optional examples.

## How does the AI help me?

1. Confirm taxonomy.
2. Classify each item.
3. Flag ambiguous items.
4. Suggest taxonomy refinements.

## What will I get?

- Classification per item.
- Ambiguous flags.
- Taxonomy refinement notes.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [data-extraction](../03-research/060-data-extraction.md)
- [knowledge-organization](../04-workflow/083-knowledge-organization.md)

## Recommended next steps

- data-analysis (097)
- knowledge-organization (083)

---

## AI specification

```text
purpose: "Classify a set of items into a defined taxonomy."
required_inputs:
  - items list
  - taxonomy or categories
  - rules
optional_inputs:
  - examples
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You want a free-form summary — use document-summary (058)."
workflow:
  - "1. Confirm taxonomy."
  - "2. Classify each item."
  - "3. Flag ambiguous items."
  - "4. Suggest taxonomy refinements."
output_contract:
  - "classification per item"
  - "ambiguous flags"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: classifications
    description: per-item categories
  - key: ambiguous_flags
    description: items needing review
```