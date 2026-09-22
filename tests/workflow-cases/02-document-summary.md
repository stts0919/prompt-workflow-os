# Workflow Case — Document Summary

## Setup

- Mode: `guide`.
- Workflow: `document-summary` (058).

## Input

A 25-page PDF paper on retrieval-augmented generation.

## Expected behavior

1. Detect that this is a long document.
2. Use `document-summary` (058).
3. Ask the reader and use case (or proceed with labeled assumptions).
4. Produce a structured summary with: purpose, key claims, evidence, conclusions, open questions.

## Verification

- Output covers each major section of the paper.
- Claims are explicitly labeled with their source (e.g., Section 3).
- Inferences are distinguished from claims.
- Open questions are listed at the bottom.

## Failure conditions

- Producing a 100-word summary without structure.
- Inventing conclusions not in the paper.
- Skipping verification of recency or sources.
