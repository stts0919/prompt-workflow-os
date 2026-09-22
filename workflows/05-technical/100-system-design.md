---
id: "100"
slug: "system-design"
title: "Design a System"
category: "technical"
aliases:
  - system design
  - architecture
  - tech design
triggers:
  - system design
  - architecture
  - design this system
input_types:
  - requirements
output_types:
  - system design
requires:
  - requirements (functional + non-functional)
  - constraints (scale, budget, team)
produces:
  - architecture
  - components
  - data flow
  - trade-offs
  - open questions
related:
  - schema-design
  - api-integration
  - agent-task-spec
playbooks:
  - build-an-ai-agent-task
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



# 100 — Design a System

## What is this?

Produce a system design: requirements, architecture, components, data flow, trade-offs, decisions, and open questions.

## Why use it?

Most systems accrue complexity without explicit design. A written design is the contract the team builds against.

## When should I use it?

- You're building a non-trivial system.
- A stakeholder asks how the system works.

## When should I not use it?

- You only need a database schema — use schema-design (098).
- You only need an API integration — use api-integration (099).

## What should I prepare?

- Requirements.
- Constraints.

## How does the AI help me?

1. Confirm requirements and constraints.
2. List components.
3. Map data flow.
4. State trade-offs.
5. List open questions.

## What will I get?

- Architecture.
- Components.
- Data flow.
- Trade-offs.
- Open questions.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [schema-design](../05-technical/098-schema-design.md)
- [api-integration](../05-technical/099-api-integration.md)
- [agent-task-spec](../05-technical/091-agent-task-spec.md)

## Recommended next steps

- schema-design (098)
- api-integration (099)
- code-generation (093)

---

## AI specification

```text
purpose: "Design the architecture for a system that meets stated requirements."
required_inputs:
  - requirements (functional + non-functional)
  - constraints (scale, budget, team)
optional_inputs:
  - existing system context
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You only need a database schema — use schema-design (098)."
  - "You only need an API integration — use api-integration (099)."
workflow:
  - "1. Confirm requirements and constraints."
  - "2. List components."
  - "3. Map data flow."
  - "4. State trade-offs."
  - "5. List open questions."
output_contract:
  - "architecture"
  - "components"
  - "data flow"
  - "trade-offs"
  - "open questions"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: architecture
    description: components and data flow
  - key: trade_offs
    description: explicit trade-offs
```