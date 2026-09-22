# 2026-Q3 evaluation batch — sample

This directory is the **placeholder layout** for the 2026-Q3 evaluation batch. It contains three empty model directories and stub JSONL files that demonstrate the schema.

The stub files are produced by running:

```bash
python3 tests/_evaluations/harness.py run-batch \
    --cases-glob 'tests/language-cases/zh-tw-localization-cases.md' \
    --run-id 2026-Q3/<model> \
    --model <model>
```

After the stub is generated, an operator (manual or API) fills the empty `response`, `rubric`, and metadata fields, then commits the file.

## Status

| Model              | Stub | Manual run | API run | Notes |
| ------------------ | :--: | :--------: | :-----: | ----- |
| gpt-5.6-luna       |  ✅  |     —      |    —    | awaiting operator |
| claude-opus-5      |  ✅  |     —      |    —    | awaiting operator |
| gemini-3.8-flash   |  ✅  |     —      |    —    | awaiting operator |

Canonical model IDs and current pricing live in
[`../../../../shared/MODELS_OF_RECORD.md`](../../../../shared/MODELS_OF_RECORD.md)
(last verified 2026-09-22).

## How to fill the first run

```bash
# Build prompts
python3 ../harness.py run-batch \
    --cases-glob '../../../language-cases/zh-tw-localization-cases.md' \
    --run-id 2026-Q3/gpt-5.6-luna \
    --model gpt-5.6-luna

# Edit the resulting JSONL, paste responses, score per rubric.md
$EDITOR gpt-5.6-luna/language-cases.jsonl

# Compare across models when you have at least two
python3 ../../harness.py compare \
    --runs 2026-Q3/gpt-5.6-luna,2026-Q3/claude-opus-5 \
    --out _compare.md
```
