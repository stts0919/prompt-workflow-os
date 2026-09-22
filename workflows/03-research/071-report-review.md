---
id: "071"
slug: "report-review"
title: "Review a Report"
category: "research"
aliases:
  - review report
  - report audit
  - manuscript review
triggers:
  - review this report
  - audit this report
  - report feedback
input_types:
  - report
output_types:
  - review report
requires:
  - report text
  - criteria
produces:
  - review report
  - improvement suggestions
related:
  - executive-brief
  - reasoning-audit
  - content-quality-review
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



# 071 — Review a Report

## What is this?

Audit the report's clarity, evidence, structure, and conclusions. Return severity-tagged issues and improvement suggestions.

## Why use it?

Reports often skip what an audience needs. A structured review turns rough drafts into publishable work.

## When should I use it?

- You finished a report and want a second pass.
- You're reviewing someone else's report.

## When should I not use it?

- You're reviewing prose — use content-quality-review (029).

## What should I prepare?

- Report text.
- Review criteria.

## How does the AI help me?

1. Confirm criteria.
2. Run each axis.
3. Tag issues by severity.
4. Recommend edits.

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

- [executive-brief](../03-research/070-executive-brief.md)
- [reasoning-audit](../03-research/066-reasoning-audit.md)
- [content-quality-review](../01-content/029-content-quality-review.md)

## Recommended next steps

- content-quality-review (029)
- executive-brief (070)

---

## AI specification

```text
purpose: "Review a report against clarity, evidence, and structure."
required_inputs:
  - report text
  - criteria
optional_inputs:
  - intended audience
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're reviewing prose — use content-quality-review (029)."
workflow:
  - "1. Confirm criteria."
  - "2. Run each axis."
  - "3. Tag issues by severity."
  - "4. Recommend edits."
output_contract:
  - "review report"
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