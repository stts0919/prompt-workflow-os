---
id: "062"
slug: "knowledge-map"
title: "Build a Knowledge Map"
category: "research"
aliases:
  - knowledge graph
  - concept map
  - taxonomy map
triggers:
  - knowledge map
  - map concepts
  - concept map
  - taxonomy
input_types:
  - domain
  - sources
output_types:
  - knowledge map
requires:
  - domain
  - source list or materials
produces:
  - concept map
  - definitions
  - relationships
related:
  - knowledge-organization
  - research-plan
  - concept-explanation
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



# 062 — Build a Knowledge Map

## What is this?

Build a concept map (entities, definitions, relationships) for a chosen domain.

## Why use it?

A concept map is faster to learn from than a long document. It also surfaces gaps in shared understanding.

## When should I use it?

- You're onboarding into a new domain.
- You're building a course or wiki.

## When should I not use it?

- You only need definitions — use concept-explanation (086).

## What should I prepare?

- Domain.
- Sources.

## How does the AI help me?

1. Confirm domain.
2. List core concepts.
3. Define each.
4. Identify relationships.
5. Render as a map.

## What will I get?

- Concept map.
- Definitions.
- Relationships.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [knowledge-organization](../04-workflow/083-knowledge-organization.md)
- [research-plan](../03-research/055-research-plan.md)
- [concept-explanation](../04-workflow/086-concept-explanation.md)

## Recommended next steps

- concept-explanation (086)
- knowledge-organization (083)

---

## AI specification

```text
purpose: "Map the core concepts and relationships in a domain."
required_inputs:
  - domain
  - source list or materials
optional_inputs:
  - target audience
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You only need definitions — use concept-explanation (086)."
workflow:
  - "1. Confirm domain."
  - "2. List core concepts."
  - "3. Define each."
  - "4. Identify relationships."
  - "5. Render as a map."
output_contract:
  - "concept map"
  - "definitions"
  - "relationships"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: concept_map
    description: entities and relationships
  - key: definitions
    description: short definitions per concept
```