# Models of Record

This document lists the AI models the `prompt-workflow-os` maintainers
**recommend** for evaluating the system's workflows. It is a
recommendation list, **not** an API integration.

## Architecture — read this first

`prompt-workflow-os` **never** calls any model API itself. Users run the
prompts in their own chat subscription — ChatGPT Plus / Pro / Business,
Claude Free / Pro / Max / Team, Gemini app for AI Pro / Ultra, or any
other surface that supports the recommended models. The maintainers'
role is to recommend which models are worth evaluating against; the
operator's role is to bring their own subscription.

This is a deliberate scope choice, set at project inception:

- **No API client ships in the harness.** `tests/_evaluations/harness.py`
  builds prompts and writes stub JSONL files; it does not call any model.
- **No API key handling.** There are no `*_API_KEY` environment variables
  anywhere in the codebase. Operator cost = their subscription tier.
- **No billing tables.** Pricing columns in older revisions of this file
  were removed because pricing is irrelevant when the operator is not
  paying per token.
- **The protocol is paste-into-UI.** See
  [`../tests/_evaluations/operators/manual.md`](../tests/_evaluations/operators/manual.md).
  The previous `operators/api.md` is kept as deprecated reference only —
  see its banner.

If you want to run the eval against a model with an API instead of a
chat subscription, that is fine, but it is **not** the project default
and it is not supported by the harness out of the box.

## What this file is for

Use this list to:

- know which models the maintainers consider worth evaluating against,
- cross-reference release dates and the surface (subscription tier) each
  model is reachable through,
- plan an operator-driven evaluation sweep (see
  [`../tests/_evaluations/README.md`](../tests/_evaluations/README.md)).

`prompt-workflow-os` does not endorse any particular vendor. The list is
chosen for capability, surface diversity, and recency. If you evaluate
against a different model and want the run included in future baseline
sweeps, open a PR that adds your run under
`tests/_evaluations/results/<YYYY-Qn>/<model>/` and follow the schema in
[`../tests/_evaluations/schema.py`](../tests/_evaluations/schema.py).

## Last verified

2026-09-23. Model availability and subscription surfaces change frequently;
re-check before any large sweep.

## OpenAI

### `gpt-6-sol` (flagship, current recommendation)

| Field | Value |
| --- | --- |
| Released | 2026-09 (general availability) |
| Tier | Flagship |
| Subscription surfaces | ChatGPT Plus / Pro / Business / Enterprise |
| Replaces | `gpt-5.6-sol` (deprecated 2026-09) |

### `gpt-6-luna` (balanced, current recommendation)

| Field | Value |
| --- | --- |
| Released | 2026-09 (general availability) |
| Tier | Balanced / cost-efficient |
| Subscription surfaces | ChatGPT Plus / Pro / Business / Enterprise |
| Replaces | `gpt-5.6-luna` and `gpt-5.6-terra` (both deprecated 2026-09) |

### Previously recommended (now deprecated)

The `gpt-5.6-*` family (`sol` / `terra` / `luna`) and `gpt-6-astra` are
no longer recommended for new eval sweeps as of 2026-09-23. Existing
result files under `tests/_evaluations/results/` that reference these
IDs remain valid historical data.

## Anthropic

Anthropic ships tier-by-tier, never a monolithic "Claude 5". The current
self-serve line-up as of 2026-09-23:

### `claude-opus-5` (flagship workhorse)

| Field | Value |
| --- | --- |
| Released | 2026-07-24 |
| Subscription surfaces | Claude Pro / Max / Team / Enterprise, Claude Code |
| Note | Highest capability per token among subscription tiers. |

### `claude-sonnet-5` (general-purpose default)

| Field | Value |
| --- | --- |
| Released | 2026-06-30 |
| Subscription surfaces | Claude Free / Pro (default), Max / Team / Enterprise |
| Note | Default model on Claude Free and Pro. Best availability across tiers. |

### `claude-fable-5-1` (creative / personality-class)

| Field | Value |
| --- | --- |
| Released | 2026-09-01 |
| Subscription surfaces | Claude Max / Team / Enterprise |
| Note | Best for tasks where voice and personality matter more than raw correctness. |

## Google

### `gemini-3.8-flash`

| Field | Value |
| --- | --- |
| Released | 2026-09-02 |
| Subscription surfaces | Gemini app for AI Pro / Ultra, Google AI Studio, Vertex AI, Gemini Enterprise |
| Note | The only Gemini model currently in the maintainers' eval set. |

A `gemini-3.8-flash-cyber` variant is available through Google's Fairwind
Program (trusted defenders only) — out of scope for this list.

## Notes for maintainers

- **Subscription tier coverage is uneven.** Opus 5 requires Max or above
  on Claude; Sonnet 5 is the default on Free / Pro. Document which tier
  you actually used when you record a result, so future operators can
  reproduce your eval.
- **The operator-driven harness does not depend on a particular ID.**
  Any model that can run the `prompt` strings produced by
  `tests/_evaluations/harness.py build-prompt` is acceptable. If you swap
  vendors, record the new `model_id` in the JSONL so the comparison tool
  can distinguish runs.
- **Knowledge cutoffs vary.** When a workflow makes a recency-sensitive
  claim, check whether the model under test has the data. As of
  2026-09-23, no single source publishes a uniform cutoff table; check
  the vendor's own page.
- **Frontier capability tiers are uneven.** Within OpenAI, `sol`
  generally outperforms `luna` on agentic / reasoning benchmarks; within
  Anthropic, Opus 5 leads Sonnet 5 on most tasks but Sonnet 5 has wider
  subscription availability. None of this affects `prompt-workflow-os`
  correctness — only what tier you bring to a particular eval pass.

## Not in this list

The following are not added because the maintainers do not include them
in the regular eval set:

- Older OpenAI tiers (GPT-5, GPT-5.5, GPT-5.5 Pro).
- `gpt-5.6-*` and `gpt-6-astra` (deprecated 2026-09; kept as
  historical reference).
- Older Anthropic tiers (Claude Opus 4.5 / 4.6 / 4.7 / 4.8, Claude Sonnet
  4.5 / 4.6, Claude Haiku 4.5, Claude Mythos 5 / 5.1 which is
  project-Glasswing only).
- Other Google tiers (Gemini 3.7 Flash, 3.8 Live, 3.8 Live Extended
  Thinking, Gemini Omni).
- Grok, Llama, Mistral, DeepSeek, Qwen, and other non-frontier or
  non-subscription-first tiers.

These models can still run `prompt-workflow-os`; they are just not part
of the maintainers' regular evaluation set.

## See also

- [`../tests/_evaluations/README.md`](../tests/_evaluations/README.md) —
  harness overview and architecture (subscription-only).
- [`../tests/_evaluations/operators/manual.md`](../tests/_evaluations/operators/manual.md) —
  the only operator protocol the project supports.
