# Router Case — Already-Complete Inputs

## Setup

- Mode: `quick`.
- Language: English.

## Input

> I have an outline, a 1,200-word draft, and a brand voice guide. Run quality review and produce clean edits.

## Expected routing

`content-quality-review` (029) followed by `content-editing` (009). The user provided everything needed; do not re-outline or re-draft.

## Expected output

A review report with severity-tagged issues, and an edited draft with edit notes.

## Failure conditions

- Asking the user for an outline when one was provided.
- Re-drafting the article from scratch.
- Inventing facts not in the draft.
