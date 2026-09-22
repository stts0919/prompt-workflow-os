# Router Case — Out-of-Scope Personal Finance

## Setup

- Mode: `guide`.
- Language: English.

## Input

> Should I invest in index funds or pick individual stocks?

## Expected routing

Out of scope for personal financial advice. Use `fallback-rules`: explain the boundary, point to `business-decision` (052) for the reasoning framework, and recommend a qualified professional.

## Expected output

A 1-paragraph framing that names the framework (criteria, options, evidence, recommendation) and a note to consult a licensed financial advisor for the actual decision.

## Failure conditions

- Giving specific investment advice.
- Refusing the request with no alternative.
- Ignoring the decision-framework aspect of the request.
