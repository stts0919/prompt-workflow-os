---
id: "060"
slug: "data-extraction"
title: "Extract Structured Data"
category: "research"
aliases:
  - extract data
  - pull out facts
  - structured extraction
triggers:
  - extract data
  - pull out the data
  - structure these facts
input_types:
  - unstructured text
output_types:
  - structured table or JSON
requires:
  - source text
  - schema or field list
produces:
  - extracted records
  - missing-field flags
related:
  - classification
  - document-summary
  - data-analysis
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



# 060 — Extract Structured Data

## What is this?

Define the schema, then extract records from the text. Flag fields you cannot fill.

## Why use it?

Locked-in text is hard to query, audit, or feed into other tools. Structured extraction unlocks the data.

## When should I use it?

- You have invoices, contracts, or product pages to inventory.
- You want to feed downstream analytics with text.

## When should I not use it?

- You want a free-form summary — use document-summary (058).

## What should I prepare?

- Source text.
- Schema or field list.

## How does the AI help me?

1. Confirm the schema.
2. Extract records row by row.
3. Flag missing or unparsed fields.
4. Return as table or JSON.

## What will I get?

- Extracted records.
- Missing-field flags.
- Suggested schema refinements.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [classification](../03-research/061-classification.md)
- [document-summary](../03-research/058-document-summary.md)
- [data-analysis](../05-technical/097-data-analysis.md)

## Recommended next steps

- classification (061)
- data-analysis (097)

---

## AI specification

```text
purpose: "Convert unstructured text into structured data."
required_inputs:
  - source text
  - schema or field list
optional_inputs:
  - output format
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You want a free-form summary — use document-summary (058)."
workflow:
  - "1. Confirm the schema."
  - "2. Extract records row by row."
  - "3. Flag missing or unparsed fields."
  - "4. Return as table or JSON."
output_contract:
  - "extracted records"
  - "missing-field flags"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: extracted_records
    description: structured output
  - key: missing_fields
    description: list of fields that could not be filled
```