---
id: "058"
slug: "document-summary"
title: "Summarize a Long Document"
category: "research"
aliases:
  - document summary
  - long doc summary
  - summarize paper
triggers:
  - summarize this document
  - long doc summary
  - summarize this paper
input_types:
  - document
output_types:
  - structured summary
requires:
  - document (text or URL)
  - reader and use case
produces:
  - structured summary
  - key facts
  - open questions
related:
  - content-summary
  - fact-check
  - evidence-matrix
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



# 058 — Summarize a Long Document

## What is this?

Produce a structured summary (purpose, key claims, evidence, conclusions, open questions) tuned to a chosen reader and use case.

## Why use it?

Long documents often bury the punchline. A structured summary surfaces what matters for the reader.

## When should I use it?

- You're reviewing a 20+ page report or paper.
- You're preparing for a decision meeting.

## When should I not use it?

- You're summarizing short content — use content-summary (010).

## What should I prepare?

- Document.
- Reader and use case.

## How does the AI help me?

1. Read the document.
2. Identify purpose, key claims, evidence, conclusions.
3. Summarize per section.
4. Flag open questions and verification needs.

## What will I get?

- Structured summary.
- Key facts list.
- Open questions list.
- Suggested next workflow: evidence-matrix (065).

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [content-summary](../01-content/010-content-summary.md)
- [fact-check](../03-research/064-fact-check.md)
- [evidence-matrix](../03-research/065-evidence-matrix.md)

## Recommended next steps

- evidence-matrix (065)
- decision-memo (069)

---

## AI specification

```text
purpose: "Summarize a long document into a structured, decision-ready briefing."
required_inputs:
  - document (text or URL)
  - reader and use case
optional_inputs:
  - question to answer
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're summarizing short content — use content-summary (010)."
workflow:
  - "1. Read the document."
  - "2. Identify purpose, key claims, evidence, conclusions."
  - "3. Summarize per section."
  - "4. Flag open questions and verification needs."
output_contract:
  - "structured summary"
  - "key facts"
  - "open questions"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: structured_summary
    description: summary by section
  - key: open_questions
    description: verification needs
```