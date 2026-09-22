# Workflow Case — Meeting Summary

## Setup

- Mode: `quick`.
- Workflow: `meeting-summary` (059).

## Input

A 30-minute sales-team standup transcript covering pipeline review, pricing objections, and three lost-deal reviews.

## Expected output

A structured summary with:

- Decisions made during the meeting.
- Action items (who / what / when).
- Open questions.
- A short context recap for absent teammates.

## Verification

- Each action item has an owner and a deadline (or a flagged "no deadline set").
- Decisions are clearly separated from discussion.
- Open questions are listed for follow-up.

## Failure conditions

- Producing a paragraph-form recap only.
- Inventing action items not in the transcript.
- Skipping open questions.
