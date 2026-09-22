---
playbook: research-before-a-decision
slug: research-before-a-decision
title: Research Before a Decision
mode_default: guide
stages: 5
---

# Research Before a Decision

## User scenario

You face a decision (product, market, hiring, investment, technology) and you need evidence-based support before committing. You may already have some sources.

## Intended final outcome

A decision memo that states the decision, criteria, options, recommendation, trade-offs, and verification gaps.

## Workflow sequence

1. **[054 — Define Research Questions](../workflows/03-research/054-research-question.md)** — start by writing the questions the decision depends on.
2. **[055 — Plan a Research Project](../workflows/03-research/055-research-plan.md)** — pick methods, sources, and a timeline.
3. **[057 — Synthesize Web Research](../workflows/03-research/057-web-research-synthesis.md)** — gather and summarize current public information.
4. **[065 — Build an Evidence Matrix](../workflows/03-research/065-evidence-matrix.md)** — map claims to evidence and weight them.
5. **[069 — Write a Decision Memo](../workflows/03-research/069-decision-memo.md)** — close with a structured memo for the decision-maker.

## Optional add-on

Insert **[064 — Fact-Check Claims](../workflows/03-research/064-fact-check.md)** after step 4 when the decision depends on a contested claim.

## Handoff data between steps

| From → To    | Key                | Description                                            |
| ------------ | ------------------ | ------------------------------------------------------ |
| step 1 → 2   | `research_questions` | Ranked research questions                            |
| step 2 → 3   | `research_plan`    | Methods, sources, timeline                             |
| step 3 → 4   | `synthesis`        | Synthesis from web-research-synthesis                  |
| step 4 → 5   | `evidence_matrix`  | Weighted claim × evidence matrix                       |

## Routing conditions

- Trigger phrases include "research this", "should we", "I need evidence", "support a decision".
- Use when the user wants a defensible, evidence-based recommendation.

## Skip conditions

- If the user already has research questions, start at step 2.
- If the user already has a synthesis, start at step 4.
- If the decision doesn't need external evidence, start at decision-memo (069) directly.

## Example start message

```
Read this repository's START.md and help me research this decision.

Decision: [the decision in one sentence]
Known context: [facts and assumptions you already have]
Sources we trust: [if any]
Time budget: [hours or days]
Verification need: [soft / strict]
```

## Final quality check

- All research questions are answered or explicitly marked as gaps.
- Evidence matrix shows the strongest and weakest claims.
- Decision memo states the recommendation plus at least one alternative.
- Verification gaps are listed at the bottom.

## AI specification

```yaml
playbook: research-before-a-decision
rule: "Run only the steps whose outputs are not yet present."
mode: "guide by default."
skip_rules:
  - "If questions are defined, skip step 1."
  - "If synthesis exists, skip steps 2–3."
  - "If the decision is small, run decision-memo only."
```
