---
id: "095"
slug: "code-review"
title: "Review Code"
category: "technical"
aliases:
  - review code
  - PR review
  - code audit
triggers:
  - review my code
  - PR review
  - audit this code
input_types:
  - code
output_types:
  - review
requires:
  - code diff or file
  - review criteria (correctness, security, style)
produces:
  - review report
  - severity-tagged issues
  - improvement suggestions
related:
  - code-explanation
  - debugging
  - prompt-improvement
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



# 095 — Review Code

## What is this?

Audit code on correctness, security, performance, readability, and tests. Return severity-tagged issues and concrete suggestions.

## Why use it?

Most bugs hide in the corners of code that's "working". A structured review catches them before they ship.

## When should I use it?

- You're submitting a PR.
- You're inheriting new code.

## When should I not use it?

- The code is failing — use debugging (094) first.

## What should I prepare?

- Code.
- Review criteria.
- Context.

## How does the AI help me?

1. Confirm criteria.
2. Run each axis.
3. Tag issues by severity.
4. Recommend fixes.

## What will I get?

- Review report.
- Severity-tagged issues.
- Improvement suggestions.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [code-explanation](../05-technical/092-code-explanation.md)
- [debugging](../05-technical/094-debugging.md)
- [prompt-improvement](../05-technical/090-prompt-improvement.md)

## Recommended next steps

- debugging (094)
- code-generation (093)

---

## AI specification

```text
purpose: "Review code against correctness, security, and style criteria."
required_inputs:
  - code diff or file
  - review criteria (correctness, security, style)
optional_inputs:
  - context
  - tests
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "The code is failing — use debugging (094) first."
workflow:
  - "1. Confirm criteria."
  - "2. Run each axis."
  - "3. Tag issues by severity."
  - "4. Recommend fixes."
output_contract:
  - "review report"
  - "severity-tagged issues"
  - "improvement suggestions"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: review
    description: structured review
  - key: severity_tags
    description: per-issue severity
```