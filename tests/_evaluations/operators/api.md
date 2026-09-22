# API Operator Protocol

Run the AI evaluation harness against model APIs when you want a fully-scripted batch. Use this for canonical baselines and for monthly drift checks.

## Why this is not implemented in `harness.py`

`harness.py` is model-agnostic and ships no API client. Reasons:

1. Model names and API endpoints change frequently. The user maintains the client of choice.
2. Each model provider has its own SDK and idioms; bundling one means excluding the others.
3. Cost control: an operator decides when to run, not the harness.

The `harness.py run-batch` command writes a stub JSONL with the prompt and an empty `response`. An API client reads that stub, calls the API, fills the response, and writes a final JSONL.

## Recommended client pattern

```python
import json
import pathlib
from openai import OpenAI  # example; substitute your provider

client = OpenAI()
stub = pathlib.Path("tests/_evaluations/results/2026-Q3/gpt-5.6-luna/language-cases.jsonl")
final = stub.with_name("language-cases.jsonl.filled")

with stub.open() as f_in, final.open("w") as f_out:
    for line in f_in:
        row = json.loads(line)
        resp = client.responses.create(
            model="gpt-5.6-luna",
            input=row["prompt"],
        )
        row["response"] = resp.output_text
        f_out.write(json.dumps(row, ensure_ascii=False) + "\n")
```

For Claude, use `anthropic.Anthropic().messages.create(...)`. For Gemini, use `google.generativeai.GenerativeModel(...)`. Each provider's SDK returns a different shape — adapt the example above accordingly.

## Cost estimation (rough)

The harness prompt for a single zh-TW case is typically 8k–25k tokens of input (including the locale layer and the workflow file). Output is typically 500–3,000 tokens depending on the workflow.

| Model | Approx. cost per case |
| ----- | --------------------: |
| gpt-5.6-luna | ~$0.02 |
| claude-opus-5 | ~$0.04 |
| gemini-3.8-flash | ~$0.005 |

For the full 65 zh-TW cases:

| Model | Approx. total |
| ----- | ------------: |
| gpt-5.6-luna | ~$1.30 |
| claude-opus-5 | ~$2.60 |
| gemini-3.8-flash | ~$0.33 |

These are very rough; verify against the current pricing of each model in
[`../../../shared/MODELS_OF_RECORD.md`](../../../shared/MODELS_OF_RECORD.md).
For monthly drift checks (e.g. once a quarter), budget around $15–$25 for
the full 100-case sweep across three model families.

## What to record

For each case, the JSONL record must include:

- `response` — verbatim model output.
- `model_version` — vendor-supplied snapshot identifier (e.g. `claude-opus-5-20260724` or `gpt-6-astra-2026-09-03`).
- `timestamp` — UTC ISO-8601 string at time of call.
- `locale_actual`, `profile_actual`, `editing_intensity_actual` — what the model picked or appeared to use. These can be filled by an automatic extractor later.
- `rubric` — the five 1–5 scores.
- `failure_conditions_triggered` — list of strings from the case.
- `notes` — free-form notes.

`locale_actual` and friends are NOT automatic today. They are filled by the operator after reading the response.

## Why human scoring is intentional

The rubric is a human-judgment tool. Automatic scoring would require defining pass/fail per failure condition as machine-checkable rules, which would not capture the cases where the model fails in a subtle way that a human can catch.

For future work: an auto-scorer can be a thin layer on top of the JSONL that flags obvious failures (e.g. main content language check, protected-content verbatim check, banned-phrase check). It does not replace the human scorer.

## Failure modes

- The harness prompt is too long. Split the case file into "case header" and "case body" if needed.
- The model refuses. Record the refusal in `notes` and skip the rubric for that case (average will not include refused cases).
- The model's output is truncated by token limits. Record the truncation in `notes`; do not retry silently.
- The API errors out. Record the error in `notes` and move on. A 100% pass-rate batch is suspicious; partial results are normal.

## When to update this protocol

Whenever a new model enters the operator's stable list. Update the cost table; update the "Recommended client pattern" example to mention the new provider's SDK.
