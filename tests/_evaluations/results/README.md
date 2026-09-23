# AI Evaluation Results

This directory holds recorded runs from the
[AI evaluation harness](../README.md).

## Architecture note

Results are produced via **paste-into-UI** runs against the user's
own chat subscription. There is no API integration. See
[`../README.md`](../README.md) § "Architecture" and
[`../../../shared/MODELS_OF_RECORD.md`](../../../shared/MODELS_OF_RECORD.md)
§ "Architecture" for the full rationale.

## Layout

```text
results/
├── 2026-Q3/                 ← one directory per batch (quarter / month / week — operator's choice)
│   ├── README.md            ← batch summary
│   ├── gpt-6-sol/           ← one directory per model
│   │   ├── language-cases.jsonl
│   │   └── workflow-cases.jsonl
│   ├── gpt-6-luna/
│   ├── claude-opus-5/
│   └── gemini-3.8-flash/
└── YYYY-Qn/                 ← next batch
```

## How to read a result file

Every line in `<batch>/<model>/<case-kind>.jsonl` is one record. See
[`../README.md`](../README.md) for the canonical shape and
[`../schema.py`](../schema.py) for field definitions.

`response` is the verbatim model output. `rubric` is the operator's
1–5 scores per dimension. `rubric_average` is the mean of those five
scores.

A line is **acceptable** when `rubric_average >= 4.0` and no individual
dimension is below 3.

A batch is **acceptable** when ≥ 90% of lines are acceptable.

## How to add a new batch

1. Pick a directory name. Recommended: `YYYY-Qn` (year + quarter) for
   monthly cadence, or `YYYY-MM` for ad-hoc.
2. Run the harness from the repo root:

   ```bash
   python3 tests/_evaluations/harness.py run-batch \
       --cases-glob 'tests/language-cases/zh-tw-localization-cases.md' \
       --run-id <YYYY-Qn>/<model-id> \
       --model <model-id>
   ```

3. For each stub row, paste the prompt into your chat subscription UI
   (ChatGPT / Claude.ai / Gemini) and paste the response back. Score
   per `rubric.md`. See [`../operators/manual.md`](../operators/manual.md).
4. Save the JSONL under `results/<YYYY-Qn>/<model>/`. The file is
   gitignored — do not commit it.

## How to add a new model

Models enter via the user's recommended list. Update
[`../README.md`](../README.md) when a new model becomes part of the
regular evaluation set, and update the canonical reference at
[`../../../shared/MODELS_OF_RECORD.md`](../../../shared/MODELS_OF_RECORD.md)
with release date and subscription surface.

## What NOT to do

- Do not check real model outputs into version control without
  confirming the response contains no private or sensitive data.
- Do not edit a recorded response after the fact. If you need to
  re-record, save under a new `<run-id>`.
- Do not commit a record with `rubric` left at zero. The stub is for
  in-progress work only.
