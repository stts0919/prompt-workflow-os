# Router Case — Recommend Mode

## Setup

- Mode: `recommend` (user-stated).
- Language: English.

## Input

> Recommend a workflow chain. I have a 30-page research report and need to brief the leadership team in 10 minutes.

## Expected routing

Return a plan only. Suggested chain:

1. `document-summary` (058) — sections by section.
2. `fact-check` (064) — only on decision-critical claims.
3. `executive-brief` (070) — one-page output for the leadership meeting.

Do not execute; just present the path.

## Expected output

A short recommendation with three numbered steps, expected outputs, and a single open question if anything is blocking (e.g., "Which decision criteria?"). Wait for the user.

## Failure conditions

- Executing the chain immediately.
- Skipping the recommendation and asking what to do.
- Adding extraneous workflows not relevant to the goal.
