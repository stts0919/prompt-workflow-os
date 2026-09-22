# Router Case — Explicit Quick Mode

## Setup

- Mode: `quick` (user-stated).
- Language: English.

## Input

> Quick mode: I need a Twitter thread on why SDR teams should care about AI. Eight posts. Conversational tone. Don't ask me anything.

## Expected routing

`thread-series` (013). No clarifying questions. Label explicit assumptions.

## Expected output

Eight-post thread outline with post-1 hook variants.

## Failure conditions

- Asking clarifying questions despite the explicit "don't ask me anything".
- Producing fewer or more than eight posts.
- Forgetting to label assumptions.
