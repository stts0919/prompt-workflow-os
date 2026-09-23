# AI Evaluation Harness

This directory holds the evaluation harness for the `prompt-workflow-os`
repository. It tests how well real models behave when given the
repository's prompts and routing logic.

## Architecture — read this first

`prompt-workflow-os` **never** calls any model API. The harness builds
prompts and writes stub JSONL files; operators paste each prompt into
their own chat subscription (ChatGPT Plus / Pro, Claude Free / Pro /
Max, Gemini AI Pro / Ultra) and paste the response back into the JSONL.
See [`../../shared/MODELS_OF_RECORD.md`](../../shared/MODELS_OF_RECORD.md)
§ "Architecture" for the full rationale.

The only operator protocol the project supports is
[`operators/manual.md`](operators/manual.md). The `operators/api.md`
file is **deprecated** — kept for transparency only.

## What this is

- A **prompt builder** that turns each test case into a single prompt
  by combining:
  - the case's expected locale / profile / intensity,
  - the relevant locale-layer files (when the case requires one),
  - the relevant workflow file (when the case selects a workflow).
- A **schema** (`schema.py`) for recording each result as one JSONL
  line.
- A **runner** (`harness.py`) that writes stub JSONL files with prompts
  filled in.
- An **operator protocol** (`operators/manual.md`) for paste-into-UI
  runs. `operators/api.md` is deprecated.
- A **rubric** (`rubric.md`) that defines how a human (or future
  auto-scorer) scores each result.

## What this is NOT

- Not a model client. The harness never calls any API or chat surface.
- Not an automatic scorer. The rubric is a human-judgment tool.
- Not a detector. We do not score "human-likeness" against any
  detector.
- Not a watermark remover. We do not test removal of any provenance
  signal.

## Models the user is evaluating

The current target list (subject to change; see
[`../../shared/MODELS_OF_RECORD.md`](../../shared/MODELS_OF_RECORD.md)
for full details):

- **OpenAI**: `gpt-6-sol`, `gpt-6-luna` (the `gpt-5.6-*` family and
  `gpt-6-astra` are deprecated as of 2026-09-23).
- **Anthropic**: `claude-opus-5`, `claude-sonnet-5`, `claude-fable-5-1`.
- **Google**: `gemini-3.8-flash`.

These are recommendations only. Bring whatever subscription tier you
have and record the model ID + tier in the JSONL.

## How to run

### 1. Build prompts (always works locally)

```bash
# Build a single prompt and print to stdout
python3 tests/_evaluations/harness.py build-prompt \
    tests/language-cases/zh-tw-localization-cases.md --case 1

# Build prompts for every case in the file (stub JSONL)
python3 tests/_evaluations/harness.py run-batch \
    --cases-glob 'tests/language-cases/zh-tw-localization-cases.md' \
    --run-id 2026-Q3/<model-id> \
    --model <model-id>
```

### 2. Capture responses (paste-into-UI)

For each stub row:

- Copy `prompt` into your chat UI (ChatGPT / Claude.ai / Gemini).
- Copy the model's reply into `response` (verbatim).
- Score per `rubric.md` (5 dimensions, 1–5 each).
- Fill `locale_actual`, `profile_actual`,
  `editing_intensity_actual`, and any `failure_conditions_triggered`.

See [`operators/manual.md`](operators/manual.md) for the full step-by-step.

### 3. Score and commit (or keep local)

Fill in `rubric` per `rubric.md`. The JSONL file lives under
`results/<run-id>/<case-kind>.jsonl` and is gitignored.

### 4. Compare across runs

```bash
python3 tests/_evaluations/harness.py compare \
    --runs 2026-Q3/gpt-6-sol,2026-Q3/claude-opus-5,2026-Q3/gemini-3.8-flash \
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
│   ├── manual.md              ← paste-into-UI protocol (the supported path)
│   └── api.md                 ← API client protocol — DEPRECATED, not used
├── results/
│   ├── README.md              ← how to read result files
│   └── 2026-Q3/
│       ├── README.md          ← batch summary (run-by-run notes)
│       ├── gpt-6-sol/
│       │   ├── language-cases.jsonl     ← one record per case (operator fills)
│       │   └── workflow-cases.jsonl
│       ├── gpt-6-luna/
│       ├── claude-opus-5/
│       └── gemini-3.8-flash/
└── scripts/                   ← operator helpers (one-off or recurring)
```

## Sample stub file

`harness.py run-batch` writes a stub JSONL with empty `response` fields
and a note that says "stub — operator must fill response and rubric".
This is the canonical shape for the final record.

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

- `scripts/validate.py` is the **structural validator** — pure regex and
  file-shape checks.
- `tests/_evaluations/` is the **behavioral evaluator** — needs humans
  with chat subscriptions to run.
- Both are part of the v1.0.0 release. The CI in
  `.github/workflows/validate.yml` runs only the structural validator.
- The behavioral evaluator is meant to run periodically, not on every
  PR.

## Limits

- The harness does not detect whether the model is a "good" Taiwanese
  writer beyond the case's failure conditions.
- The rubric is opinionated. Different teams will score differently.
  Run the same batch twice with two operators and compare scores for
  an inter-rater check.
- No test is ever truly complete; new failure modes emerge. Add new
  failure conditions to existing cases when you find them, or add new
  cases.
