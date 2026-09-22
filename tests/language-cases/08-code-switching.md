# Language Case — Code-Switching Spanish-English

## Setup

- Mode: `quick`.

## Input

> Quick mode: necesito un article-outline sobre pricing strategies para SaaS B2B.

## Expected behavior

- Detect primary language: Spanish.
- Reply in Spanish.
- Run `article-outline` (006).
- Preserve English terms where they belong (B2B, SaaS).

## Expected output

Outline in Spanish with English technical terms preserved.

## Failure conditions

- Replying in English.
- Translating "B2B" and "SaaS".
- Producing an outline without section beats.
