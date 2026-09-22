# Manual Operator Protocol

Run the AI evaluation harness when you cannot or do not want to call model APIs directly. This is the typical path for solo review or when keys are restricted.

## When to use this protocol

- You have access to a chat UI (Claude.ai, ChatGPT, Gemini) and want to evaluate the latest model snapshot.
- You do not have API keys, or keys are restricted.
- You want a small sample (≤ 30 cases) reviewed by a human.
- You are evaluating a brand-new model that has no API yet.

## When NOT to use this protocol

- You want a full regression run (≥ 100 cases). Use the API protocol instead.
- You want to commit the results to `tests/_evaluations/results/<date>/<model>/` as the canonical baseline. Use the API protocol.

## Steps

1. **Pick the batch.** Run from the repo root:

   ```bash
   python3 tests/_evaluations/harness.py run-batch \
       --cases-glob 'tests/language-cases/zh-tw-localization-cases.md' \
       --run-id 2026-Q3/<model-name> \
       --model <model-name>
   ```

   This writes a stub JSONL with every prompt filled in and every `response` field empty.

2. **Open the JSONL.** Each line has a `prompt` field. Copy the prompt into your chat UI (Claude.ai / ChatGPT / Gemini / Claude Code / Codex, etc.).

3. **Capture the response.** Copy the model output verbatim into the JSONL line's `response` field. Do not edit or paraphrase. Even rough output is useful data.

4. **Score the response.** Open `tests/_evaluations/rubric.md`. Score each of the five dimensions 1–5. Write the scores into the JSONL line's `rubric` field.

5. **Record the metadata.** Fill in `locale_actual`, `profile_actual`, `editing_intensity_actual`. Note any `failure_conditions_triggered` from the case file.

6. **Append a note.** Use the `notes` field for anything an automated score would miss (e.g. "model refused to engage with the case").

7. **Commit the file.** Save under the model-specific subdirectory, e.g.:

   ```text
   tests/_evaluations/results/2026-Q3/<model-name>/language-cases.jsonl
   ```

   Then commit and push.

8. **Aggregate.** Once multiple runs are in `results/`, run:

   ```bash
   python3 tests/_evaluations/harness.py compare \
       --runs 2026-Q3/gpt-5.6-luna,2026-Q3/claude-opus-5,2026-Q3/gemini-flash-3.8 \
       --out tests/_evaluations/results/2026-Q3/_compare.md
   ```

## How long does this take?

Roughly 2–4 minutes per case for an attentive operator:
- 30 seconds to read the case.
- 30–90 seconds for the model to respond.
- 60 seconds to score per rubric dimension.
- 30 seconds to fill the JSONL fields.

For the full 65 zh-TW cases, expect 3–5 hours of focused work. For a smaller smoke test, pick the first 5 cases of each test file.

## What this protocol cannot do

- It does not call any model API.
- It does not produce automated scoring.
- It does not enforce the rubric; that is the operator's job.
- It does not commit anything automatically.

## Trust boundary

The recorded responses are the model's actual output. The recorded scores are the operator's interpretation. Anyone re-running the same case on the same model later should expect different output (model updates, temperature variation, etc.) and a possibly different score.
