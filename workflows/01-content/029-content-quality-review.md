---
id: "029"
slug: "content-quality-review"
title: "Review Content Quality"
category: "content"
aliases:
  - content review
  - qa
  - quality check
  - editorial review
triggers:
  - review this content
  - is this good
  - qa the draft
  - quality check
input_types:
  - content
  - criteria
output_types:
  - review report
  - improvement suggestions
requires:
  - content
  - review criteria (clarity, accuracy, voice, accessibility)
produces:
  - review report
  - severity-tagged issues
  - improvement suggestions
related:
  - content-editing
  - article-rewrite
  - fact-check
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



# 029 — Review Content Quality

## What is this?

Run a multi-axis review (clarity, structure, voice, accuracy, accessibility). Return a structured report with severity tags and concrete improvement suggestions.

## Why use it?

Most publishing regret comes from skipping review. A repeatable rubric catches the issues the author is blind to.

## When should I use it?

- You're publishing an important piece.
- You're onboarding a new editor.

## When should I not use it?

- You're polishing prose — use content-editing (009).
- You want to change direction — use article-rewrite (008).

## What should I prepare?

- Content.
- Review criteria.
- Target audience.

## How does the AI help me?

1. Confirm criteria.
2. Run each axis.
3. Tag issues by severity (blocker, should-fix, nice-to-have).
4. Recommend concrete edits.

## What will I get?

- Review report.
- Severity-tagged issues.
- Concrete improvement suggestions.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [content-editing](../01-content/009-content-editing.md)
- [article-rewrite](../01-content/008-article-rewrite.md)
- [fact-check](../03-research/064-fact-check.md)

## Recommended next steps

- content-editing (009)
- article-rewrite (008)

---

## AI specification

```text
purpose: "Audit content against a defined quality rubric."
required_inputs:
  - content
  - review criteria (clarity, accuracy, voice, accessibility)
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're polishing prose — use content-editing (009)."
  - "You want to change direction — use article-rewrite (008)."
workflow:
  - "1. Confirm criteria."
  - "2. Run each axis."
  - "3. Tag issues by severity (blocker, should-fix, nice-to-have)."
  - "4. Recommend concrete edits."
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
  - key: review_report
    description: structured review with severity tags
  - key: suggestions
    description: list of concrete edits
```