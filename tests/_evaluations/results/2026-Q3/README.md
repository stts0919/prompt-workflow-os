# 2026-Q3 evaluation batch — sample

This directory is the **placeholder layout** for the 2026-Q3 evaluation
batch. It contains four empty model directories. The first round to
fill these in is the 2026-Q3 smoke round at
`runs/2026-Q3-smoke/README.md` (9 cases × 4 models).

The current recommended models (see
[`../../../../shared/MODELS_OF_RECORD.md`](../../../../shared/MODELS_OF_RECORD.md)):

| Model | Subscription surface |
| --- | --- |
| `gpt-6-sol` | ChatGPT Plus / Pro / Business / Enterprise |
| `gpt-6-luna` | ChatGPT Plus / Pro / Business / Enterprise |
| `claude-opus-5` | Claude Max / Team / Enterprise / Claude Code |
| `gemini-3.8-flash` | Gemini app (AI Pro / Ultra), Google AI Studio |

(`gpt-5.6-*` and `gpt-6-astra` are deprecated as of 2026-09-23.)

## How to fill the first run

```bash
# Build stub prompts (operator fills response + rubric afterwards)
python3 ../harness.py run-batch \
    --cases-glob '../../../language-cases/zh-tw-localization-cases.md' \
    --run-id 2026-Q3/<model-id> \
    --model <model-id>

# Edit the resulting JSONL; paste `prompt` into chat UI, paste response back,
# score per rubric.md. See ../operators/manual.md.
$EDITOR <model-id>/language-cases.jsonl

# Compare across models once at least two are filled in
python3 ../../harness.py compare \
    --runs 2026-Q3/gpt-6-sol,2026-Q3/claude-opus-5 \
    --out _compare.md
```

The full protocol lives at [`../../operators/manual.md`](../../operators/manual.md).
API-based eval is **not supported**; see
[`../../operators/api.md`](../../operators/api.md) for the deprecated
reference.
