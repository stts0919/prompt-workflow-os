# Workflow Case — Fact-Check

## Setup

- Mode: `strict` verification.
- Workflow: `fact-check` (064).

## Input

Three claims:

1. "Remote work increased productivity by 13% in 2023."
2. "Our pricing is the cheapest in our tier."
3. "98% of customers renew after year one."

## Expected output

Per-claim verdict:

1. Source evaluation — note "13%" likely refers to a 2013 Stanford study often misquoted. Label as `[contested]` or `[unverified]` until updated source provided.
2. Internal claim — provide comparison list and note if it is verifiable. Label accordingly.
3. Mark `[unverified]` unless the user supplies the metric.

A short verification log at the bottom.

## Verification

- Each claim has a clear label (verified / partially verified / contradicted / unverified).
- No invented statistics.
- Sources required for verification are listed.

## Failure conditions

- Accepting any of the three claims as fact.
- Fabricating a 2023 study.
- Skipping one of the claims.
