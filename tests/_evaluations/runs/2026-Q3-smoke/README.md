# Smoke Eval Round — 2026-Q3

First operator-driven eval round using the `tests/_evaluations/` harness
against `gpt-5.6-luna`, `claude-opus-5`, and `gemini-3.8-flash`.

## Goal

Produce the **first concrete evidence** that `prompt-workflow-os` v1.2.0
works against the three model families the user evaluates with. The round
is intentionally small (9 cases) so an operator can finish it in one
session without burning serious API budget.

## Coverage

One case per locale pack. Each case targets the locale's most distinctive
behavior:

| Smoke ID | Locale | Profile | Source case | What it exercises |
| --- | --- | --- | --- | --- |
| `zh-TW-01` | zh-TW | `zh-tw-friendly-professional` | zh-tw-localization #1 | Reference baseline. Natural Taiwan conversation. |
| `zh-CN-04` | zh-CN | `zh-cn-xiaohongshu-lifestyle` | zh-cn-localization #4 | Mainland 小红书 channel + glossary. |
| `yue-Hant-HK-01` | yue-Hant-HK | `yue-hk-chat-casual` | locale-coverage #1 | HK WhatsApp Cantonese 口語. |
| `en-US-04` | en-US | `en-us-linkedin-professional` | locale-coverage #4 | US spelling + polite LinkedIn register. |
| `en-GB-06` | en-GB | `en-gb-formal-letter` | locale-coverage #6 | UK formal letter (strict_precision auto-escalation). |
| `ja-JP-08` | ja-JP | `ja-jp-email-formal` | locale-coverage #8 | Japanese keigo (sonkeigo / kenjōgo / teineigo). |
| `ko-KR-10` | ko-KR | `ko-kr-email-formal` | locale-coverage #10 | Korean 합쇼체 register. |
| `id-ID-12` | id-ID | `id-id-whatsapp-casual` | locale-coverage #12 | ID casual vs formal `kamu`/`Anda`. |
| `vi-VN-14` | vi-VN | `vi-vn-zalo-casual` | locale-coverage #14 | Vietnamese diacritics + casual particles. |

## How to run

### 0. Pre-flight (always do this first)

```bash
# Verify all 9 locale layers actually load — catches path regressions.
python3 tests/_evaluations/runs/2026-Q3-smoke/check_paths.py
```

Expected: `OK — all locales load their LANGUAGE_FILES layer.`

### 1. Generate stub JSONL files

```bash
# Build stubs for all 3 models at once.
python3 tests/_evaluations/runs/2026-Q3-smoke/build.py
```

This writes three files:

- `tests/_evaluations/results/2026-Q3/smoke/gpt-5.6-luna/smoke-cases.jsonl`
- `tests/_evaluations/results/2026-Q3/smoke/claude-opus-5/smoke-cases.jsonl`
- `tests/_evaluations/results/2026-Q3/smoke/gemini-3.8-flash/smoke-cases.jsonl`

Each file has 9 rows. Each row carries the `prompt` text and an empty
`response` field. **Do not commit these files** — they are
gitignored (`.gitignore` line 32–35 cover the `results/**/` pattern).

### 2. Pick your operator mode

#### Option A — Manual (paste into chat UI)

For each model file:

1. Open `tests/_evaluations/results/2026-Q3/smoke/<model>/smoke-cases.jsonl`
2. For each row:
   - Copy the value at `prompt` into a new chat with the target model.
   - Copy the model's reply into `response`.
   - Score per `tests/_evaluations/rubric.md` (5 dimensions, 1–5 each).
   - Update `locale_actual`, `profile_actual`,
     `editing_intensity_actual` based on what the model produced.
   - Note any `failure_conditions_triggered` from the case file.
3. Save the JSONL.

Detailed paste-into-UI protocol: `tests/_evaluations/operators/manual.md`.

#### Option B — API-driven

Write a tiny client loop that reads the JSONL, calls the model, and
writes back the response + rubric fields. The schema lives in
`tests/_evaluations/schema.py`. Reference pattern:
`tests/_evaluations/operators/api.md`.

### 3. Run the auto-scorer

Once a model's JSONL has filled-in responses:

```bash
python3 tests/_evaluations/auto_scorer.py \
    tests/_evaluations/results/2026-Q3/smoke/<model>/smoke-cases.jsonl
```

The auto-scorer runs three deterministic checks:

1. **language_check** — does the output language match `expected_locale`?
   (Latin vs CJK broad classification. Disambiguating zh-TW vs zh-CN
   stays with the human scorer.)
2. **banned_phrase_check** — does the output use any of the documented
   cross-strait vocabulary leakage patterns?
3. **protected_span_check** — are protected spans (workflow IDs, brand
   names, order numbers, etc.) preserved verbatim?

It writes `<input>.auto-verdict.jsonl` next to the source file. It
**never overwrites the operator's `rubric` scores**.

### 4. Compare across models

```bash
python3 tests/_evaluations/harness.py compare \
    --runs 2026-Q3/smoke/gpt-5.6-luna,2026-Q3/smoke/claude-opus-5,2026-Q3/smoke/gemini-3.8-flash \
    --out tests/_evaluations/results/2026-Q3/smoke/_compare.md
```

Output is a small markdown table: rows are case IDs, columns are models,
cells are `rubric_average`. Models with empty cells didn't have data
yet for that case.

## Cost estimate

| Model | Input tokens (approx) | Output tokens (approx) | Per-round cost |
| --- | --- | --- | --- |
| `gpt-5.6-luna` | ~600K | ~5K | ~$3 (promo through 2026-11-21: ~$2.5) |
| `claude-opus-5` | ~600K | ~5K | ~$10–$15 |
| `gemini-3.8-flash` | ~600K | ~5K | < $1 |

(Pricing snapshots are best-effort; confirm against each vendor's pricing
page before running.)

The prompts are large because they embed the full locale layer (so the
model can apply style profiles and glossary terms correctly). For a
real product you'd want to do retrieval over the layer files instead of
shipping them in every prompt — but for a smoke round this is fine.

## Customising the manifest

Edit `cases.json`:

- Add or remove cases — the script only processes the cases in the
  manifest, so you can shrink it to 3 cases if you only want to spot-
  check one locale.
- Swap a model — change the `models` array. The script will write one
  stub file per model.
- Add a locale — add a new entry under `LANGUAGE_FILES` in
  `tests/_evaluations/prompt_builder.py`, then add the case here.

After editing the manifest, rerun `build.py`. Stubs are rewritten from
scratch; nothing is appended.

## What NOT to commit

Everything under `tests/_evaluations/results/` is gitignored. Don't
commit:

- The stub JSONL files (contain prompts only — not sensitive, but the
  convention is "results are operator-local").
- The filled-in JSONL files (contain verbatim model output — may leak
  private content from the model's response).
- The `_compare.md` output (it's a derived artifact, regenerate when
  needed).

If you want to share a result set, copy it to a separate scratch
location outside the repo first.
