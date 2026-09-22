---
id: "080"
slug: "sop-builder"
title: "Build a Standard Operating Procedure"
category: "workflow"
aliases:
  - sop
  - standard operating procedure
  - playbook
triggers:
  - sop
  - standard operating procedure
  - build a playbook
input_types:
  - process
  - audience
output_types:
  - SOP
requires:
  - process to document
  - operator profile
  - exceptions
produces:
  - SOP
  - exceptions section
  - quality check
related:
  - checklist-builder
  - documentation-template
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



# 080 — Build a Standard Operating Procedure

## What is this?

Produce a SOP with purpose, scope, prerequisites, numbered steps, an exceptions section, and a quality check.

## Why use it?

Processes that live in one person's head create bus-factor risk. SOPs scale without sacrificing quality.

## When should I use it?

- You're scaling a process across people or teams.
- Your team keeps making the same mistakes.

## When should I not use it?

- You're building a quick checklist — use checklist-builder (081).

## What should I prepare?

- Process description.
- Operator profile.
- Known exceptions.

## How does the AI help me?

1. Confirm process.
2. List prerequisites.
3. Number the steps.
4. Add exceptions and quality check.

## What will I get?

- SOP.
- Exceptions list.
- Quality check.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [checklist-builder](../04-workflow/081-checklist-builder.md)
- [documentation-template](../04-workflow/082-documentation-template.md)

## Recommended next steps

- checklist-builder (081)

---

## AI specification

```text
purpose: "Document a repeatable process so others can execute it consistently."
required_inputs:
  - process to document
  - operator profile
  - exceptions
optional_inputs:
  - tools
  - compliance
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're building a quick checklist — use checklist-builder (081)."
workflow:
  - "1. Confirm process."
  - "2. List prerequisites."
  - "3. Number the steps."
  - "4. Add exceptions and quality check."
output_contract:
  - "SOP"
  - "exceptions section"
  - "quality check"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: sop
    description: structured SOP
  - key: exceptions
    description: known exceptions
```