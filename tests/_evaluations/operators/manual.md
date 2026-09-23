# Manual Operator Protocol

> **This is the only operator protocol the project supports.**
>
> `prompt-workflow-os` does not use any model API. Operators evaluate
> the harness by pasting each prompt into their own chat subscription
> (ChatGPT Plus / Pro, Claude Free / Pro / Max, Gemini AI Pro / Ultra)
> and pasting the response back into the JSONL.
>
> See [`shared/MODELS_OF_RECORD.md`](../../../shared/MODELS_OF_RECORD.md)
> § "Architecture — read this first" for the rationale.

## When to use this protocol

This protocol covers every supported eval scenario:

- You have access to a chat UI (ChatGPT, Claude.ai, Gemini app) and
  want to evaluate the latest model snapshot your subscription tier
  gives you.
- You are doing a small or medium sample (≤ ~100 cases) reviewed by a
  human.
- You are evaluating a brand-new model that may not have a stable API
  surface yet.
- You want cost = your subscription tier (no per-token billing).

## When to consider other approaches

The project deliberately does not support API-driven eval. If you have
a hard requirement to use the API, you are working outside the project
scope and must bring your own client. See
[`api.md`](api.md) — it is deprecated but kept as a starting point
for operators who choose this route on their own.

## Steps

1. **Pick the batch.** The recommended cadence is one quarter per
   directory: `tests/_evaluations/results/2026-Q3/<model>/`. Run from
   the repo root:

   ```bash
   python3 tests/_evaluations/harness.py run-batch \
       --cases-glob 'tests/language-cases/zh-tw-localization-cases.md' \
       --run-id 2026-Q3/<model-name> \
       --model <model-name>
   ```

   This writes a stub JSONL with every prompt filled in and every
   `response` field empty.

2. **Open the JSONL.** Each line has a `prompt` field. Copy the prompt
   into your chat UI (Claude.ai / ChatGPT / Gemini / Claude Code /
   Codex, etc.).

3. **Capture the response.** Copy the model output verbatim into the
   JSONL line's `response` field. Do not edit or paraphrase. Even rough
   output is useful data.

4. **Score the response.** Open `tests/_evaluations/rubric.md`. Score
   each of the five dimensions 1–5. Write the scores into the JSONL
   line's `rubric` field.

5. **Record the metadata.** Fill in `locale_actual`, `profile_actual`,
   `editing_intensity_actual`. Note any `failure_conditions_triggered`
   from the case file.

6. **Append a note.** Use the `notes` field for anything an automated
   score would miss (e.g. "model refused to engage with the case",
   "subscribed tier didn't include Opus 5, used Sonnet 5 instead").

7. **Save the file** under the model-specific subdirectory, e.g.:

   ```text
   tests/_evaluations/results/2026-Q3/<model-name>/language-cases.jsonl
   ```

   The file is gitignored; do not commit it.

8. **Aggregate.** Once multiple runs are in `results/`, run:

   ```bash
   python3 tests/_evaluations/harness.py compare \
       --runs 2026-Q3/gpt-6-sol,2026-Q3/claude-opus-5,2026-Q3/gemini-3.8-flash \
       --out tests/_evaluations/results/2026-Q3/_compare.md
   ```

## How long does this take?

Roughly 2–4 minutes per case for an attentive operator:

- 30 seconds to read the case.
- 30–90 seconds for the model to respond.
- 60 seconds to score per rubric dimension.
- 30 seconds to fill the JSONL fields.

For the full 65 zh-TW cases, expect 3–5 hours of focused work. For a
smaller smoke test, pick the first 5 cases of each test file.

## What this protocol cannot do

- It does not call any model API (this is by design).
- It does not produce automated scoring.
- It does not enforce the rubric; that is the operator's job.
- It does not commit anything automatically.

## Trust boundary

The recorded responses are the model's actual output. The recorded
scores are the operator's interpretation. Anyone re-running the same
case on the same model later should expect different output (model
updates, temperature variation, etc.) and a possibly different score.

## When to update this protocol

Whenever a model is added to or removed from the recommended list in
[`shared/MODELS_OF_RECORD.md`](../../../shared/MODELS_OF_RECORD.md).
Update the example commands in step 8 to point at the new model IDs.
