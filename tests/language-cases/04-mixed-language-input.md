# Language Case — Mixed Language Input

## Setup

- Mode: `guide`.

## Input

> Read START.md. Ayúdame con mi competitor analysis. I'm entering the European market. Mi segmento objetivo son pequeños SaaS.

## Expected behavior

- Detect primary language: this is mixed, with Spanish predominant. Ask one short clarification if uncertain about output language.
- Default to replying in Spanish (the dominant language of the request).
- Run `competitor-analysis` (034).
- Preserve workflow slug in English, e.g. "034 — competitor-analysis".

## Expected questions (in Spanish)

1. "¿Prefieres que el resumen final sea en español o en inglés? Voy a continuar en español por ahora."

## Failure conditions

- Replying in English without acknowledging the mixed input.
- Translating workflow slugs.
- Asking multiple questions when one suffices.
