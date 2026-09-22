---
id: zh-tw-quality-checklist
title: "Taiwan Traditional Chinese Quality Checklist"
applies_when:
  - Taiwan localization layer is active and a deliverable is being produced
companion_files:
  - WRITING_RULES.md
  - TERM_GLOSSARY.md
  - STYLE_PROFILES.md
version: 2.0.0
---

# Taiwan Traditional Chinese Quality Checklist

Use this checklist before delivering any zh-TW output. The document has two layers:

1. **Compact AI-readable checklist** at the top — what the AI applies silently to its own output.
2. **Human-readable editorial review checklist** below — what a human editor uses for review.

Both layers cover the same five concerns: language and localization, accuracy and evidence, writing quality, channel fit, and safety.

## Layer 1 — Compact AI-readable checklist

The AI applies this compressed form to its own draft:

```text
language:
  - is Taiwan-appropriate (or requested variant)
  - words regionally natural
  - user terminology preserved
  - protected content (code, IDs, URLs, brand names) intact
  - one style profile, consistent
  - no silent language drift

accuracy:
  - facts, numbers, quotes, dates preserved or labeled
  - sources cited
  - assumption / inference / recommendation labeled
  - no invented evidence or experience
  - uncertainty stays uncertain
  - no detector / watermark / authorship claims

writing:
  - opening reaches the point
  - no empty era framing
  - adjectives carry evidence
  - sentence rhythm varied
  - connectives used when needed
  - triadic lists only when distinct
  - verbs concrete
  - lists genuinely distinct
  - transitions necessary
  - ending matches content
  - no reflective human-experience claims

voice:
  - tone matches audience and channel
  - casualness is appropriate
  - first-person matches profile policy
  - second-person matches profile policy (您 vs 你)
  - rhetorical questions only when useful
  - reads like competent human editorial pass
  - AI pattern reduction applied when appropriate, not damaging structure

channel:
  - profile matches the platform (Threads / Instagram / LinkedIn / Email / Sales / Landing / Article / Research / Tech / SOP / Agent spec / Support)
  - length matches platform norms
  - punctuation follows profile notes

intensity:
  - chosen intensity (none / light / standard / strict_precision) matches content type
  - high-risk content (legal, medical, financial, security, compliance, regulated) is in strict_precision

safety:
  - code / URLs / citations / brand names unchanged
  - workflow IDs and slugs unchanged
  - no fabricated evidence
  - no detector / watermark / authorship claims
  - required disclosures preserved
  - if user asked for unavailable capability, the router explained the boundary
```

## Layer 2 — Human-readable editorial review checklist

A human editor walks through these checks before approving the deliverable.

### Language and localization

- [ ] Is the wording natural for Taiwan readers (or for the explicitly named variant)?
- [ ] Are local terms appropriate for the requested channel?
- [ ] Is Mainland Chinese wording avoided unless the user explicitly requested it?
- [ ] Is the user's terminology preserved?
- [ ] Is the chosen style profile consistent with the channel?
- [ ] Are protected spans (code, IDs, URLs, citations, brand names) unchanged?
- [ ] Is there any silent language drift mid-document?

### Accuracy and evidence

- [ ] Are facts, numbers, sources, quotes, and uncertainty preserved exactly?
- [ ] Are assumptions, inferences, and recommendations clearly separated?
- [ ] Did the text avoid invented experience, social proof, and evidence?
- [ ] Did the text avoid unsourced statistics, customer counts, or testimonials?
- [ ] Is uncertainty explicit (假設 / 推論 / 估計 / 待驗證) where appropriate?

### Writing quality

- [ ] Does the opening get to the point quickly?
- [ ] Are abstract nouns replaced with concrete actions where helpful?
- [ ] Are transitions used only where needed (not at the start of every paragraph)?
- [ ] Are list items genuinely distinct?
- [ ] Is sentence rhythm varied?
- [ ] Does the ending fit the purpose?
- [ ] Does the piece avoid AI tells (era framing, slogan-like endings, uniform rhythm, three-item chains)?

### Channel fit

- [ ] Does the tone fit the intended audience and platform?
- [ ] Is the casualness level appropriate (LinkedIn vs Instagram, etc.)?
- [ ] Is the length appropriate for the platform?
- [ ] Is the second-person form (您 vs 你) correct for the channel?

### Safety

- [ ] Are protected spans unchanged?
- [ ] Does the output avoid claims of watermark removal or AI detector evasion?
- [ ] Does the output avoid claiming to prove human authorship?
- [ ] If the user requested capabilities outside the layer's scope, did the router explain the boundary plainly?

## How to apply

For routine outputs, the AI applies Layer 1 silently. For high-stakes outputs (legal, medical, financial, security, compliance, regulatory, statistical claims, anything that will be published under a brand or to a regulator), the AI should additionally surface Layer 2 as a self-review report at the top of the deliverable.

## When to return partial output

If a check fails and cannot be resolved:

- Return the deliverable with the heading `PARTIAL — 見下方說明`.
- Follow with a short note on what was produced, what was skipped, why, and what the user can supply to finish.
- Apply [../../../shared/QUALITY_CHECKLISTS.md](../../../shared/QUALITY_CHECKLISTS.md) plus this checklist together.
