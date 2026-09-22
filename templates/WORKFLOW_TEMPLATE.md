---
id: "000"
slug: "example-workflow"
title: "Example Workflow"
category: "workflow"
aliases: []
triggers: []
input_types: []
output_types: []
requires: []
produces: []
related: []
playbooks: []
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
  default_style_profile:
  locale_style_profile_overrides:
    zh-TW:
  editing_intensity:
    - none
    - light
    - standard
    - strict_precision
handoff: []
---

# NNN — Example Workflow

## What is this?

Plain-language description in two or three short sentences. State what the user gets and what changes in the user's life when they use this workflow.

## Why use it?

Explain the underlying problem this workflow solves. State the typical cost of not solving it (rewrites, missed deadlines, low-quality output, decision regret).

## When should I use it?

- Situation 1 — the user shows up with X.
- Situation 2 — the user has Y and needs Z.
- Situation 3 — the user must decide between A and B.

## When should I not use it?

- When the request fits a single direct answer better.
- When a neighboring workflow better matches the desired output. Name it.
- When the user is unwilling to provide the required inputs.

## What should I prepare?

- Required input 1 — short description and a concrete example.
- Required input 2 — short description and a concrete example.
- Optional input 3 — short description.

## How does the AI help me?

1. The AI restates your goal in one sentence.
2. The AI confirms only the inputs that materially change the output.
3. The AI drafts the result using its AI specification.
4. The AI labels assumptions and verification gaps.
5. The AI suggests one next workflow when useful.

## What will I get?

- Output artifact 1 — short description.
- Output artifact 2 — short description.
- A short Assumptions section with each assumption labeled.
- A short Verification section (none / soft / strict) when factual claims are made.
- One recommended next workflow.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:
[your goal here]
```

## Related workflows

- [slug-of-related-workflow-1](../workflows/<category>/<id>-<slug>.md)
- [slug-of-related-workflow-2](../workflows/<category>/<id>-<slug>.md)

## Recommended next steps

Most often, follow up with:

- [slug-of-next-workflow](../workflows/<category>/<id>-<slug>.md) — when and why.

---

## AI specification

```text
purpose: One-sentence purpose.
required_inputs:
  - input 1
  - input 2
optional_inputs:
  - input 3
ask_if_missing:
  - "Question 1"
  - "Question 2"
do_not_use_when:
  - "Situation that disqualifies this workflow."
  - "Situation where a different workflow is better."
workflow:
  - "Step 1."
  - "Step 2."
  - "Step 3."
output_contract:
  - "What the deliverable must contain."
  - "Structure or format constraints."
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
handoff:
  - key: value
  - to_workflow: slug
```

## Localization metadata (optional)

A workflow can declare how the Taiwan Traditional Chinese layer is applied to its output. Optional fields:

```yaml
localization:
  supported_locales:
    - en
    - zh-TW
  default_style_profile: zh-tw-friendly-professional
  locale_style_profile_overrides:
    zh-TW: zh-tw-business-consulting
  editing_intensity: standard
```

Notes for authors:

- `supported_locales` lists the locales this workflow is designed to support. The router uses it to skip localization work for unsupported locales.
- `default_style_profile` is the chosen profile when the user did not specify a tone. Available profiles live in [../shared/ZH_TW_STYLE_PROFILES.md](../shared/ZH_TW_STYLE_PROFILES.md).
- `locale_style_profile_overrides` maps a locale code to a profile. The router prefers the override when the deliverable's output language (or target market) matches the locale. Future locales (`zh-CN`, `yue-Hant-HK`, `en-US`, `ja-JP`, etc.) plug in here when their locale packs are ready.
- `editing_intensity` is one of:
  - `none` — no prose edits; protect code, IDs, URLs, brand names, citations.
  - `light` — minimal cleanup; preserve technical or structured wording.
  - `standard` — apply glossary substitutions and AI-pattern reduction where natural.
  - `strict_precision` — high precision, light editing, label uncertainty, no rhetorical softening.

Notes on selection:

- `zh-TW` style profiles should only be set when a workflow has a stable default. Otherwise leave the field empty and let the router fall back to category defaults.
- Channel and user instructions can override the workflow default at runtime (recorded in the context ledger).
- High-precision tasks (legal, medical, financial, security, compliance, regulatory, citation-heavy statistical claims) must use `strict_precision`.
- Localization rules should not load when the output does not require them. The router skips the entire layer for non-zh-TW deliverables (Case A).

If the field is absent, the router infers a default from the workflow category:

- content → `zh-tw-friendly-professional` or a social profile (`zh-tw-threads-insightful`, `zh-tw-instagram-casual`, `zh-tw-linkedin-professional`)
- business → `zh-tw-business-consulting` or `zh-tw-sales-clear` or `zh-tw-landing-page-clear`
- research → `zh-tw-research-precise` or `zh-tw-technical-clear`
- workflow → `zh-tw-sop-direct`
- technical → `zh-tw-technical-clear` or `zh-tw-agent-spec-precise`

Localization metadata is optional. Workflows that do not include it still benefit from the universal multilingual and quality rules.
