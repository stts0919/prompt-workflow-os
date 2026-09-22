# Router Case — Incomplete Content Brief

## Setup

- Mode: `quick`.
- Language: English.

## Input

> Write me an article about productivity.

## Expected routing

This is incomplete. Either ask 1–2 short questions or proceed in `quick mode` with labeled assumptions. Default is `guide`; `quick` is allowed because the request is generic.

## Expected questions (guide mode)

1. "Who will read this, and where will it appear (blog, newsletter, LinkedIn)?"
2. "Roughly what length do you want, and any tone constraints?"

## Expected output (quick mode)

An `article-outline` (006) + first 250 words of the article with explicit assumptions: assumed audience = general knowledge workers; assumed length = 1,000 words; assumed tone = informative and concise.

## Failure conditions

- Producing a full 1,500-word article with no clarifying questions in guide mode.
- Inventing a specific brand or company context.
- Using a tech tone when audience is unspecified (acceptable but flag it).
