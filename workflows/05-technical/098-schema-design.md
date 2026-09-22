---
id: "098"
slug: "schema-design"
title: "Design a Schema"
category: "technical"
aliases:
  - schema
  - database schema
  - data model
triggers:
  - design a schema
  - database design
  - data model
input_types:
  - data requirements
output_types:
  - schema
requires:
  - data requirements
  - query patterns
produces:
  - entity model
  - field definitions
  - index strategy
  - sample queries
related:
  - system-design
  - api-integration
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



# 098 — Design a Schema

## What is this?

Build a schema: entities, fields, types, relationships, indexes, and 3 sample queries.

## Why use it?

Most schema regret comes from mismatched query patterns. Designing around the real queries avoids rewrites.

## When should I use it?

- You're starting a new app or feature.
- You're restructuring an existing schema.

## When should I not use it?

- You're designing whole-system architecture — use system-design (100).

## What should I prepare?

- Data requirements.
- Query patterns.

## How does the AI help me?

1. Confirm requirements and queries.
2. Identify entities.
3. Define fields and types.
4. Mark indexes.
5. Write sample queries.

## What will I get?

- Entity model.
- Field definitions.
- Index strategy.
- Sample queries.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [system-design](../05-technical/100-system-design.md)
- [api-integration](../05-technical/099-api-integration.md)
- [data-analysis](../05-technical/097-data-analysis.md)

## Recommended next steps

- api-integration (099)
- system-design (100)

---

## AI specification

```text
purpose: "Design a data schema for the requirements and query patterns."
required_inputs:
  - data requirements
  - query patterns
optional_inputs:
  - scale
  - constraints
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're designing whole-system architecture — use system-design (100)."
workflow:
  - "1. Confirm requirements and queries."
  - "2. Identify entities."
  - "3. Define fields and types."
  - "4. Mark indexes."
  - "5. Write sample queries."
output_contract:
  - "entity model"
  - "field definitions"
  - "index strategy"
  - "sample queries"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: schema
    description: entity and field definitions
  - key: indexes
    description: index strategy
```