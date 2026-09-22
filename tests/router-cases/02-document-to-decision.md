# Router Case — Long Document to Decision

## Setup

- Mode: `guide`.
- Language: English.

## Input

> Here is a 40-page market study. Tell me whether we should enter this market.

## Expected routing

Use `document-summary` (058), then `fact-check` (064) if claims are decision-critical, then `evidence-matrix` (065), then `decision-memo` (069).

Stop after `executive-brief` (070) if the user only needs a quick read.

## Expected questions

1. "Which decision criteria should the memo use (market size, competitive intensity, fit, risk)?"
2. "Any sources you trust or distrust a priori?"

## Expected output

A decision memo (1–2 pages) that states the recommendation, the trade-offs, and the verification gaps.

## Failure conditions

- Treating all report claims as confirmed facts.
- Skipping the decision criterion.
- Producing a generic summary without a recommendation.
