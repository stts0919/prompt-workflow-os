# Tests

Evaluation cases for the router, language behavior, and individual workflows.

Each case is a single Markdown file under one of:

- `router-cases/` — how the router classifies and routes a request.
- `language-cases/` — multilingual detection and output behavior.
- `workflow-cases/` — single-workflow execution correctness.

Use [templates/EVALUATION_CASE_TEMPLATE.md](../templates/EVALUATION_CASE_TEMPLATE.md) to add new cases.

## Counts (current)

| Area           | Cases |
| -------------- | ----: |
| router-cases   |    15 |
| language-cases |    11 |
| workflow-cases |    11 |

## Why these cases

Router cases cover:

- vague user requests (1, 4, 7, 8)
- incomplete inputs (3, 11)
- already-complete inputs (5, 9)
- requests needing current information (13)
- requests that map to multiple workflows (10)
- requests where `quick mode` should bypass questioning (6, 9)
- cases where the router should ask clarifying questions (1, 2, 4, 7, 8)
- cases where no exact workflow exists (12, 14, 15)

Language cases cover detection, mixed-language input, output in a different language, and preserving English workflow IDs in non-English content.

Workflow cases cover key outputs of representative workflows.

## How to run

The validation script `scripts/validate.py` checks the repository's structural rules. Use it before merging. Run from the repository root:

```bash
python3 scripts/validate.py
```

This script does not run the test cases themselves — it validates the structure. Functional evaluation of cases requires running them against an AI model with the latest repository attached.

## Operator-driven evaluation harness

A small `prompt-builder + run-batch + compare` harness lives under
`tests/_evaluations/`. The directory is gitignored: it is operator-local scratch
space that is created when you actually evaluate, not part of the public v1.0.0
release.

The harness:

- parses each test case (`split_cases` on `## N.` headings, `parse_case` for fields),
- assembles a prompt that includes the case + the relevant locale layer + the
  workflow file when applicable,
- writes a per-kind stub JSONL (one line per case) under
  `tests/_evaluations/results/<YYYY-Qn>/<model>/<kind>-cases.jsonl`,
- produces a markdown comparison across runs via `harness.py compare`.

It does **not** call any model API itself. API costs and key handling stay with
the operator. Models the user is currently evaluating with:

- `gpt-5.6-luna` / `gpt-5.6-terra` / `gpt-5.6-sol`
- `gpt-6-astra`
- `claude-sonnet-5` / `claude-opus-5` / `claude-fable-5-1`
- `gemini-3.8-flash`

The canonical model IDs, release dates, context windows, and current pricing
live in [`../shared/MODELS_OF_RECORD.md`](../shared/MODELS_OF_RECORD.md)
(last verified 2026-09-22).

See `tests/_evaluations/operators/manual.md` for the paste-into-UI protocol and
`tests/_evaluations/operators/api.md` for the API client pattern. The rubric
the operator scores against lives at `tests/_evaluations/rubric.md`.

To initialize the directory on a fresh clone, copy the harness from the team's
archive or recreate it from the schema described in
`tests/_evaluations/README.md`. The directory layout is:

```text
tests/_evaluations/
├── README.md             ← how to use it
├── harness.py            ← CLI entry point
├── prompt_builder.py     ← builds prompts from case files
├── schema.py             ← EvalResult / RubricScore dataclasses
├── rubric.md             ← scoring rubric
├── operators/
│   ├── manual.md         ← paste-into-UI protocol
│   └── api.md            ← API client pattern
└── results/              ← gitignored; recorded runs go here
```
