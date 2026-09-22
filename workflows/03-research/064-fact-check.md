---
id: "064"
slug: "fact-check"
title: "Fact-Check Claims"
category: "research"
aliases:
  - fact check
  - verify claims
  - check facts
triggers:
  - fact check
  - verify this
  - is this true
input_types:
  - claims
output_types:
  - verification report
requires:
  - claims to check
  - sources available
produces:
  - per-claim verdict
  - source references
  - open issues
related:
  - source-evaluation
  - evidence-matrix
  - web-research-synthesis
playbooks:
  - research-before-a-decision
mode_support:
  - guide
  - quick
  - recommend
language_support:
  input: auto-detect
  output: mirror-user-language
localization:
  supported_locales:
    - en
    - zh-TW
  default_style_profile: zh-tw-research-precise
  locale_style_profile_overrides:
    zh-TW:
  editing_intensity: strict_precision
handoff:
  - key: context
    description: "summary of upstream context"
---



# 064 — Fact-Check Claims

## What is this?

Examine each claim against available sources. Label it verified, partially verified, contradicted, or unverified.

## Why use it?

Decisions break on unverified claims. A structured fact-check turns a doc into one a decision-maker can rely on.

## When should I use it?

- You're about to publish or present claims.
- A decision rests on a contested number.

## When should I not use it?

- You want general source quality — use source-evaluation (056).

## What should I prepare?

- Claims.
- Sources.

## How does the AI help me?

1. List claims.
2. For each, retrieve source evidence.
3. Label the claim.
4. Note remaining uncertainty.

## What will I get?

- Per-claim verdict.
- Source references.
- Uncertainty log.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [source-evaluation](../03-research/056-source-evaluation.md)
- [evidence-matrix](../03-research/065-evidence-matrix.md)
- [web-research-synthesis](../03-research/057-web-research-synthesis.md)

## Recommended next steps

- evidence-matrix (065)
- decision-memo (069)

---

## AI specification

```text
purpose: "Check specific claims against sources and label their status."
required_inputs:
  - claims to check
  - sources available
optional_inputs:
  - verification standard (strict / soft)
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You want general source quality — use source-evaluation (056)."
workflow:
  - "1. List claims."
  - "2. For each, retrieve source evidence."
  - "3. Label the claim."
  - "4. Note remaining uncertainty."
output_contract:
  - "per-claim verdict"
  - "source references"
  - "open issues"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: verdicts
    description: per-claim label
  - key: uncertainty_log
    description: remaining doubts
```