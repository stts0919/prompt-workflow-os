---
playbook: validate-a-business-idea
slug: validate-a-business-idea
title: Validate a Business Idea
mode_default: guide
stages: 5
---

# Validate a Business Idea

## User scenario

You're considering an offer — a product, course, service, or feature — and you need to validate demand, positioning, and pricing before you commit to build or launch. You may have an audience in mind or you may be choosing one.

## Intended final outcome

A validated offer brief that includes the target customer, competitive context, validation results, value proposition, and a price-test plan.

## Workflow sequence

1. **[031 — Define Target Customer](../workflows/02-business/031-customer-persona.md)** — start with the jobs-to-be-done. The persona anchors every later step.
2. **[034 — Analyze Competitors](../workflows/02-business/034-competitor-analysis.md)** — set the contrast that makes the offer distinct.
3. **[038 — Validate a Product Idea](../workflows/02-business/038-product-idea-validation.md)** — design cheap experiments that reduce risk.
4. **[036 — Create a Value Proposition](../workflows/02-business/036-value-proposition.md)** — turn the validated insight into a promise.
5. **[041 — Design Pricing Strategy](../workflows/02-business/041-pricing-strategy.md)** — close with the pricing logic and a test plan.

## Handoff data between steps

| From → To              | Key                | Description                                            |
| ---------------------- | ------------------ | ------------------------------------------------------ |
| step 1 → step 2        | `persona`          | Persona card from `customer-persona`                   |
| step 2 → step 3        | `competitor_table` | Comparison table from `competitor-analysis`            |
| step 3 → step 4        | `validation_plan`  | Plan and results from `product-idea-validation`        |
| step 4 → step 5        | `value_prop`       | Headline value proposition from `value-proposition`    |

## Routing conditions

- Trigger phrases include "validate my idea", "is this worth building", "before I launch", "should I build it".
- Use when the user has an offer but lacks validation or pricing.

## Skip conditions

- If the user already has a validated persona, skip step 1 and pass it as context.
- If the user already has pricing, skip step 5 and run quality check only.
- If the user asks for one specific step (e.g., pricing only), do not run the full playbook.

## Example start message

```
Read this repository's START.md and help me validate this business idea.

Idea: [describe the offer]
Audience in mind: [persona or segment, or "I'm not sure"]
Constraints: [budget, timeline, geography]
```

## Final quality check

Before signing off:

- Persona covers jobs, pains, gains, and an anti-persona.
- Competitor table covers direct, indirect, and substitute competitors.
- Validation plan has explicit go/no-go rules.
- Value proposition names a customer, value, and differentiator.
- Pricing strategy includes a test plan and a sensitivity note.

## AI specification

```yaml
playbook: validate-a-business-idea
rule: "Start at the earliest missing dependency; do not force completed stages."
mode: "guide by default; allow quick mode when risk is low."
skip_rules:
  - "If user supplied the persona, skip step 1."
  - "If user already validated the idea, skip step 3 and go straight to value proposition."
  - "If user only needs pricing, run only step 5."
```
