# Models of Record

This document tracks the AI models that the `prompt-workflow-os` maintainers
have evaluated against. The list is informational — `prompt-workflow-os` is
model-agnostic, and any sufficiently capable frontier model can run the
workflows. Use this list to:

- know which models were used to baseline the system,
- cross-reference API model IDs and current pricing,
- plan an operator-driven evaluation sweep (see
  [../tests/_evaluations/README.md](../tests/_evaluations/README.md)).

`prompt-workflow-os` does not endorse any particular vendor. The maintainers
chose this list based on availability, capability, and the diverse set of
organizational, pricing, and channel trade-offs they represent. If you evaluate
against a different model and want your data included in future baseline
sweeps, open a PR that adds your run under
`tests/_evaluations/results/<YYYY-Qn>/<model>/` and follow the schema in
[../tests/_evaluations/schema.py](../tests/_evaluations/schema.py).

## Last verified

2026-09-22. Pricing snapshots are best-effort and may have shifted since.
Always confirm against the vendor's own pricing page before budgeting a
sweep.

## OpenAI

### `gpt-6-astra`

| Field | Value |
| --- | --- |
| Release date | 2026-09-03 (limited), 2026-09-04 (general) |
| API model ID | `gpt-6-astra` |
| Context window | 1,050,000 tokens (922k input, 128k output) |
| Knowledge cutoff | 2026-04-30 |
| Reasoning effort | `low, medium, high, xhigh, max` |
| Pricing | $10 / $50 per million input / output tokens |
| Cached input | $1.00 per million tokens |
| Cache write | $12.50 per million tokens |
| Endpoints | Chat Completions, Responses, Batch |
| Surfaces | ChatGPT Plus / Pro / Business / Enterprise; OpenAI API; Azure; AWS Bedrock |
| Source | [openai.com/index/gpt-6-astra](https://openai.com/index/gpt-6-astra/) |

### `gpt-5.6-sol` (flagship)

| Field | Value |
| --- | --- |
| Release date | 2026-07-09 (GA) |
| API model ID | `gpt-5.6-sol` (also reachable via the bare `gpt-5.6` alias) |
| Pricing (list) | $5 / $30 per million input / output tokens |
| Pricing (promo through 2026-11-21) | $4 / $20 |
| Context window | Up to 1M tokens (Fast mode long-context up to 272K+) |
| Surfaces | ChatGPT Plus / Pro / Business / Enterprise; Codex; OpenAI API |
| Source | [openai.com/index/gpt-5-6](https://openai.com/index/gpt-5-6/) |

### `gpt-5.6-terra` (balanced)

| Field | Value |
| --- | --- |
| Release date | 2026-07-09 (GA) |
| API model ID | `gpt-5.6-terra` |
| Pricing | $2.50 / $15 per million input / output tokens (40% cut effective 2026-07-30) |
| Context window | Up to 1M tokens |
| Surfaces | ChatGPT Free / Go / Plus / Pro / Business / Enterprise; Codex; OpenAI API |
| Source | [openai.com/index/gpt-5-6](https://openai.com/index/gpt-5-6/) |

### `gpt-5.6-luna` (cost-efficient)

| Field | Value |
| --- | --- |
| Release date | 2026-07-09 (GA) |
| API model ID | `gpt-5.6-luna` |
| Pricing | $1 / $6 per million input / output tokens (80% cut effective 2026-07-30) |
| Context window | Up to 1M tokens |
| Surfaces | ChatGPT Plus / Pro / Business / Enterprise; Codex; OpenAI API |
| Source | [openai.com/index/gpt-5-6](https://openai.com/index/gpt-5-6/) |

## Anthropic

Anthropic ships tier-by-tier, never a monolithic "Claude 5". The current
self-serve line-up as of 2026-09-22:

### `claude-fable-5-1` (Mythos-class flagship)

| Field | Value |
| --- | --- |
| Release date | 2026-09-01 |
| API model ID | `claude-fable-5-1` |
| Pricing | $10 / $50 per million input / output tokens |
| Cached input | $0.25 per million tokens (75% cheaper than Fable 5) |
| Context window | 1M tokens (128k output) |
| Surfaces | Claude API, Claude in Amazon Bedrock, Claude on Google Cloud, Claude in Microsoft Foundry |
| Source | [docs.anthropic.com/en/release-notes/api](https://docs.anthropic.com/en/release-notes/api) (entry 2026-09-01) |

The pre-2026-09-01 release was `claude-fable-5`, released 2026-06-09 and
re-deployed after an export-control pause on 2026-06-30. New work should
target `claude-fable-5-1`; `claude-fable-5` remains available.

### `claude-opus-5` (flagship workhorse)

| Field | Value |
| --- | --- |
| Release date | 2026-07-24 |
| API model ID | `claude-opus-5` |
| Pricing | $5 / $25 per million input / output tokens |
| Context window | 1M tokens (128k output) |
| Surfaces | Claude API, Claude.ai (Pro/Max/Team/Enterprise), Claude Code, Vertex AI, AWS Bedrock, Microsoft Foundry |
| Source | [anthropic.com/news/claude-opus-5](https://www.anthropic.com/news/claude-opus-5) |

### `claude-sonnet-5` (general-purpose default)

| Field | Value |
| --- | --- |
| Release date | 2026-06-30 |
| API model ID | `claude-sonnet-5` |
| Pricing | $2 / $10 per million input / output tokens (introductory pricing made permanent 2026-08-10) |
| Context window | 1M tokens (128k output, raisable to 300k via batch-API beta header) |
| Surfaces | Claude API, Claude.ai Free/Pro (default), Max/Team/Enterprise, Claude Code, Bedrock, Vertex AI, Microsoft Foundry |
| Source | [anthropic.com/news/claude-sonnet-5](https://www.anthropic.com/news/claude-sonnet-5) |

## Google

### `gemini-3.8-flash`

| Field | Value |
| --- | --- |
| Release date | 2026-09-02 |
| API model ID | `gemini-3.8-flash` |
| Pricing (intro through 2026-12-31) | $0.75 / $3.75 per million input / output tokens |
| Pricing (standard from 2027-01-01) | $1.50 / $7.50 per million input / output tokens |
| Context window | 1M tokens (64k output) |
| Thinking levels | `low, medium, high` (`minimal` is not supported and returns an error) |
| Surfaces | Gemini API, Google AI Studio, Vertex AI, Google Antigravity (default), Gemini app for AI Pro / Ultra subscribers, Gemini Enterprise |
| Source | [ai.google.dev/gemini-api/docs/models/gemini-3.8-flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash) |

A `gemini-3.8-flash-cyber` variant is also available through Google's Fairwind
Program (trusted defenders only).

## Notes for maintainers

- **Pricing churns fast.** The Sol 5.6 and Luna 5.6 cuts landed within 30 days
  of GA; Sonnet 5's introductory price became permanent two months later. Don't
  treat any number in this file as a quote — re-check before a sweep.
- **The operator-driven harness does not depend on a particular ID.** Any
  model that can run the `prompt` strings produced by
  `tests/_evaluations/harness.py build-prompt` is acceptable. If you swap
  vendors, record the new `model_id` in the JSONL so the comparison tool can
  distinguish runs.
- **Knowledge cutoffs vary.** When a workflow makes a recency-sensitive claim,
  check whether the model under test has the data. As of 2026-09-22, Astra's
  cutoff is 2026-04-30, Gemini 3.8 Flash is 2026-03 / 2025-01 (mixed),
  Claude Opus 5 is 2026-05, GPT-5.6 family has not published a single
  explicit date.
- **Frontier capability tiers are uneven.** Astra leads on cyber / agentic
  benchmarks; Opus 5 leads the Intelligence Index as of mid-September; Gemini
  3.8 Flash hits the Intelligence vs Cost Pareto at $0.58 per task. None of
  this matters for `prompt-workflow-os` correctness — only for what to budget
  when picking a model for a particular evaluation pass.

## Not in this list

The following are not added because they were not in scope for the initial
evaluation plan and the maintainers have not baseline-tested them:

- GPT-5, GPT-5.5, GPT-5.5 Pro (older OpenAI tiers).
- Claude Opus 4.5 / 4.6 / 4.7 / 4.8, Claude Sonnet 4.5 / 4.6, Claude Haiku 4.5,
  Claude Mythos 5 / 5.1 (project-Glasswing / trusted-access only).
- Gemini 3.7 Flash, 3.8 Live, 3.8 Live Extended Thinking, Gemini Omni.
- Grok 4.6, Llama, Mistral, DeepSeek, Qwen, and other non-frontier or
  non-API-first tiers.

These models can still run `prompt-workflow-os`; they are just not part of
the maintainers' regular evaluation set.