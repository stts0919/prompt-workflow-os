---
id: "094"
slug: "debugging"
title: "Debug Failing Code"
category: "technical"
aliases:
  - debug
  - fix bug
  - failing code
triggers:
  - this is broken
  - debug this
  - find the bug
input_types:
  - failing code
  - error
output_types:
  - debug plan
  - fix
requires:
  - failing code or error message
  - reproduction steps
produces:
  - root-cause candidates
  - fix proposal
  - verification plan
related:
  - code-review
  - code-explanation
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



# 094 — Debug Failing Code

## What is this?

Reproduce mentally, list root-cause candidates ranked by likelihood, propose a fix, and define how to verify the fix.

## Why use it?

Most debugging time is spent on the wrong hypothesis. Structured root-cause ranking shortens the loop.

## When should I use it?

- Your code fails or returns wrong output.
- You have an error message and don't know where to start.

## When should I not use it?

- You're auditing code quality — use code-review (095).

## What should I prepare?

- Code.
- Error or reproduction steps.

## How does the AI help me?

1. Confirm code and error.
2. List root-cause candidates ranked by likelihood.
3. Propose a fix.
4. Define verification.

## What will I get?

- Root-cause candidates.
- Fix proposal.
- Verification plan.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [code-review](../05-technical/095-code-review.md)
- [code-explanation](../05-technical/092-code-explanation.md)

## Recommended next steps

- code-review (095)
- code-generation (093)

---

## AI specification

```text
purpose: "Diagnose and propose a fix for failing code."
required_inputs:
  - failing code or error message
  - reproduction steps
optional_inputs:
  - logs
  - expected vs actual
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're auditing code quality — use code-review (095)."
workflow:
  - "1. Confirm code and error."
  - "2. List root-cause candidates ranked by likelihood."
  - "3. Propose a fix."
  - "4. Define verification."
output_contract:
  - "root-cause candidates"
  - "fix proposal"
  - "verification plan"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: root_cause
    description: top candidate cause
  - key: fix
    description: proposed fix
```