# API Operator Protocol — DEPRECATED, NOT USED

> **⚠️ This project does not use model APIs.**
>
> `prompt-workflow-os` was designed from the start to be evaluated via
> chat subscription UIs (ChatGPT Plus / Pro, Claude Free / Pro / Max,
> Gemini AI Pro / Ultra), **not** via the vendor APIs. See
> [`shared/MODELS_OF_RECORD.md`](../../../shared/MODELS_OF_RECORD.md) §
> "Architecture — read this first" for the rationale.
>
> The **only** supported operator path is
> [`manual.md`](manual.md) — paste the prompt into your chat UI and
> paste the response back.
>
> This file is kept for two reasons:
>
> 1. Historical reference — operators who want to script their own
>    API-based eval against a model can use this as a starting point.
> 2. Transparency — readers reviewing the project's design should be
>    able to see that the no-API stance was a deliberate choice, not an
>    oversight.
>
> If you do decide to run an API-based eval against a model, you are
> doing it on your own. The harness does not support it out of the box;
> you write your own client loop. Cost, key handling, and rate limiting
> are entirely your problem.

---

# (Original content below, retained for reference)

## Why this is not implemented in `harness.py`

`harness.py` is model-agnostic and ships no API client. Reasons:

1. The project scope explicitly excludes API integration; the maintainers
   recommend subscription surfaces instead. See
   [`shared/MODELS_OF_RECORD.md`](../../../shared/MODELS_OF_RECORD.md).
2. Each model provider has its own SDK and idioms; bundling one would
   mean excluding the others.
3. Cost control: even when an operator does run an API eval, an operator
   decides when to run, not the harness.

The `harness.py run-batch` command writes a stub JSONL with the prompt
and an empty `response`. An external client (your own code, not the
harness) reads that stub, calls the API, fills the response, and writes
a final JSONL.

## Reference client pattern (NOT supported by the harness)

```python
import json
import pathlib
from openai import OpenAI  # example; substitute your provider

client = OpenAI()
stub = pathlib.Path("tests/_evaluations/results/2026-Q3/gpt-6-sol/language-cases.jsonl")
final = stub.with_name("language-cases.jsonl.filled")

with stub.open() as f_in, final.open("w") as f_out:
    for line in f_in:
        row = json.loads(line)
        resp = client.responses.create(
            model="gpt-6-sol",
            input=row["prompt"],
        )
        row["response"] = resp.output_text
        f_out.write(json.dumps(row, ensure_ascii=False) + "\n")
```

For Claude, use `anthropic.Anthropic().messages.create(...)`. For Gemini,
use `google.generativeai.GenerativeModel(...)`. Each provider's SDK
returns a different shape — adapt the example above accordingly.

## When you would actually use this

- You are evaluating a model that is **not** available on a subscription
  surface your team has access to.
- You are doing research that requires reproducible, scripted eval runs
  with full control over temperature, seed, and other parameters.
- You are running a high-volume sweep (≥ 100 cases per model) where
  paste-into-UI would be impractical.

If none of these apply, please use
[`manual.md`](manual.md) instead.

## What to record

For each case, the JSONL record must include:

- `response` — verbatim model output.
- `model_version` — vendor-supplied snapshot identifier
  (e.g. `claude-opus-5-20260724` or `gpt-6-sol-2026-09`).
- `timestamp` — UTC ISO-8601 string at time of call.
- `locale_actual`, `profile_actual`, `editing_intensity_actual` — what
  the model picked or appeared to use. These can be filled by an
  automatic extractor later.
- `rubric` — the five 1–5 scores.
- `failure_conditions_triggered` — list of strings from the case.
- `notes` — free-form notes.

`locale_actual` and friends are NOT automatic today. They are filled by
the operator after reading the response.

## Failure modes

- The harness prompt is too long. Split the case file into "case header"
  and "case body" if needed.
- The model refuses. Record the refusal in `notes` and skip the rubric
  for that case (average will not include refused cases).
- The model's output is truncated by token limits. Record the truncation
  in `notes`; do not retry silently.
- The API errors out. Record the error in `notes` and move on. A 100%
  pass-rate batch is suspicious; partial results are normal.

## When to update this protocol

This file is deprecated. If a model is added to the recommended list,
update [`manual.md`](manual.md) and
[`shared/MODELS_OF_RECORD.md`](../../../shared/MODELS_OF_RECORD.md)
instead.
