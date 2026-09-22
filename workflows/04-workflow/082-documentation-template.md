---
id: "082"
slug: "documentation-template"
title: "Create a Documentation Template"
category: "workflow"
aliases:
  - doc template
  - documentation template
  - doc scaffold
triggers:
  - doc template
  - documentation template
  - create a doc scaffold
input_types:
  - doc purpose
output_types:
  - doc template
requires:
  - documentation purpose
  - audience
produces:
  - template skeleton
  - section guidance
related:
  - sop-builder
  - checklist-builder
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



# 082 — Create a Documentation Template

## What is this?

Produce a doc template with section structure, section guidance, and example snippets.

## Why use it?

Ad-hoc docs drift in style and depth. Templates keep documentation consistent and reviewable.

## When should I use it?

- You're scaling documentation across a team.
- Your existing docs are inconsistent.

## When should I not use it?

- You're documenting one process — use sop-builder (080).

## What should I prepare?

- Doc purpose.
- Audience.
- Style guide (optional).

## How does the AI help me?

1. Confirm purpose.
2. List sections.
3. Add guidance per section.
4. Provide example snippets.

## What will I get?

- Template skeleton.
- Section guidance.
- Example snippets.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [sop-builder](../04-workflow/080-sop-builder.md)
- [checklist-builder](../04-workflow/081-checklist-builder.md)
- [knowledge-organization](../04-workflow/083-knowledge-organization.md)

## Recommended next steps

- sop-builder (080)
- knowledge-organization (083)

---

## AI specification

```text
purpose: "Build a documentation template that fits a recurring need."
required_inputs:
  - documentation purpose
  - audience
optional_inputs:
  - style guide
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're documenting one process — use sop-builder (080)."
workflow:
  - "1. Confirm purpose."
  - "2. List sections."
  - "3. Add guidance per section."
  - "4. Provide example snippets."
output_contract:
  - "template skeleton"
  - "section guidance"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: template
    description: doc skeleton
  - key: guidance
    description: per-section guidance
```