# AI Evaluation Harness

This directory holds the evaluation harness for the `prompt-workflow-os` repository. It tests how well real models behave when given the repository's prompts and routing logic.

## What this is

- A **prompt builder** that turns each test case into a single prompt by combining:
  - the case's expected locale / profile / intensity,
  - the relevant `zh-TW` layer files (when the case requires Taiwan),
  - the relevant workflow file (when the case selects a workflow).
- A **schema** (`schema.py`) for recording each result as one JSONL line.
- A **runner** (`harness.py`) that writes stub JSONL files with prompts filled in.
- An **operator protocol** for both manual paste-into-UI runs (`operators/manual.md`) and API-driven runs (`operators/api.md`).
- A **rubric** (`rubric.md`) that defines how a human (or future auto-scorer) scores each result.

## What this is NOT

- Not a model client. The harness never calls any API itself.
- Not an automatic scorer. The rubric is a human-judgment tool.
- Not a detector. We do not score "human-likeness" against any detector.
- Not a watermark remover. We do not test removal of any provenance signal.

## Models the user is evaluating

The current target list (subject to change):

- **GPT-5.6 Luna / Terra / Sol + GPT-6 Astra** (OpenAI-side priority models).
- **Claude Sonnet / Opus / Fable 5+** (Anthropic-side priority models).
- **Gemini 3.8 Flash** (the only Gemini model the user evaluates for now).

The canonical model IDs, release dates, context windows, and current pricing
live in [`../../shared/MODELS_OF_RECORD.md`](../../shared/MODELS_OF_RECORD.md)
(last verified 2026-09-22). When you add a model, update that file first,
then update `operators/api.md`'s cost table and "Recommended client pattern"
example.

## How to run

### 1. Build prompts (always works locally)

```bash
# Build a single prompt and print to stdout
python3 tests/_evaluations/harness.py build-prompt \
    tests/language-cases/zh-tw-localization-cases.md --case 1

# Build prompts for every case in the file
python3 tests/_evaluations/harness.py run-batch \
    --cases-glob 'tests/language-cases/zh-tw-localization-cases.md' \
    --run-id 2026-Q3/my-model \
    --model my-model
```

### 2. Capture responses

Either:

- **Manual** — open each line, paste `prompt` into Claude.ai / ChatGPT / Gemini, paste `response` back. See `operators/manual.md`.
- **API** — write your own client loop that calls the model and fills `response`. See `operators/api.md`.

### 3. Score and commit

Fill in `rubric` per `rubric.md`. Commit the file under `results/<run-id>/<case-kind>.jsonl`.

### 4. Compare across runs

```bash
python3 tests/_evaluations/harness.py compare \
    --runs 2026-Q3/gpt-5.6-luna,2026-Q3/claude-opus-5,2026-Q3/gemini-3.8-flash \
    --out tests/_evaluations/results/2026-Q3/_compare.md
```

## Directory layout

```text
tests/_evaluations/
├── README.md                  ← this file
├── harness.py                 ← runner (build-prompt, run-batch, compare)
├── prompt_builder.py          ← builds the prompt for one case
├── schema.py                  ← EvalResult / RubricScore dataclasses
├── rubric.md                  ← how to score
├── operators/
│   ├── manual.md              ← paste-into-UI protocol
│   └── api.md                 ← API client protocol + cost estimate
├── results/
│   ├── README.md              ← how to read result files
│   └── 2026-Q3/
│       ├── README.md          ← batch summary (run-by-run notes)
│       ├── gpt-5.6-luna/
│       │   ├── language-cases.jsonl     ← one record per case
│       │   └── workflow-cases.jsonl
│       ├── claude-opus-5/
│       └── gemini-3.8-flash/
└── scripts/                   ← operator helpers (one-off or recurring)
```

## Sample stub file

`harness.py run-batch` writes a stub JSONL with empty `response` fields and a note that says "stub — operator must fill response and rubric". This is the canonical shape for the final record.

A stub line looks like:

```json
{
  "run_id": "2026-Q3/my-model",
  "case_id": "01-vague-product-idea",
  "case_path": "tests/router-cases/01-vague-product-idea.md",
  "case_kind": "router",
  "model_id": "my-model",
  "prompt": "...",
  "response": "",
  "model_version": "",
  "timestamp": "2026-09-22T10:30:00+00:00",
  "locale_actual": "",
  "profile_actual": "",
  "editing_intensity_actual": "",
  "protected_content_preserved": true,
  "failure_conditions_triggered": [],
  "rubric": {
    "locale_correctness": 0,
    "style_profile_adherence": 0,
    "protected_content_preservation": 0,
    "failure_condition_avoidance": 0,
    "output_language_correctness": 0
  },
  "notes": "stub — operator must fill response and rubric",
  "rubric_average": 0.0
}
```

## How this fits the rest of the repository

- `scripts/validate.py` is the **structural validator** — pure regex and file-shape checks.
- `tests/_evaluations/` is the **behavioral evaluator** — needs humans or paid APIs to run.
- Both are part of the v1.0.0 release. The CI in `.github/workflows/validate.yml` runs only the structural validator (it does not call any model API).
- The behavioral evaluator is meant to run periodically, not on every PR.

## Limits

- The harness does not detect whether the model is a "good" Taiwanese writer beyond the case's failure conditions.
- The rubric is opinionated. Different teams will score differently. Run the same batch twice with two operators and compare scores for an inter-rater check.
- No test is ever truly complete; new failure modes emerge. Add new failure conditions to existing cases when you find them, or add new cases.
