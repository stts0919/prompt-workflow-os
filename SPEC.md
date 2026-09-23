# SPEC — `prompt-workflow-os` design rationale

This document is for **reviewers, contributors, and future maintainers** who
need to understand *why* the system is shaped the way it is, not just *how*
to use it. For day-to-day usage, see [`README.md`](README.md) and
[`START.md`](START.md). For extension paths and PR rules, see
[`CONTRIBUTING.md`](CONTRIBUTING.md).

## Why this exists

The user-facing problem: people have to remember dozens of prompt templates,
or they have to copy-paste a wall of instructions into ChatGPT every time
they want a structured output. Both are brittle.

The product bet: **don't ship a prompt gallery. Ship a routing system that
takes a plain-language request and tells the AI which of 100 well-tested
workflows to apply, with the right language conventions and editing
discipline.**

The repository is the public, model-agnostic specification of that routing
system. The maintainers do not ship a host application; any sufficiently
capable AI that reads the repository can serve as the host.

## Non-goals

These are the things `prompt-workflow-os` deliberately does **not** try to
be. They are listed up front because every contributor eventually proposes
one of them.

1. **A prompt gallery or template marketplace.** There are other repos that
   do that well; we do not compete with them.
2. **An AI agent framework.** The workflows assume the host is a single
   model conversation, not a tool-using agent. Adjacent workflow
   `091 agent-task-spec` covers the boundary where the workflow's output
   becomes input to a downstream agent.
3. **A detector / bypass / watermark-removal tool.** Editorial rewriting
   improves clarity, naturalness, and tone; it does not claim to defeat any
   detector, remove any watermark, or prove human authorship. This boundary
   is enforced in [`router/FALLBACK_RULES.md`](router/FALLBACK_RULES.md) and
   in the introduction of every locale pack.
4. **A model benchmark.** The maintainers track results in
   [`tests/_evaluations/`](tests/_evaluations/), but the harness is
   operator-driven on purpose — see the test contract below.
5. **A runtime.** The repository is static Markdown; there is nothing to
   "deploy" beyond GitHub Pages.
6. **A single-vendor system.** `shared/MODELS_OF_RECORD.md` documents the
   vendor list for context, but any sufficiently capable model can run the
   workflows.

## Design principles

These six principles explain most of the structural choices. Each one has
been paid for in code; violating one will likely break something downstream.

### 1. The router is text-only.

`router/AI_ROUTER.md`, `router/ROUTING_RULES.md`, and
`router/CLARIFICATION_PROTOCOL.md` are all Markdown. The router is a
decision procedure a language model can apply at inference time, not a
compiled rule engine. This is why all four cases (input/output language
combinations) are spelled out in prose — the host model needs to read them
and apply them, not execute them.

### 2. Two layers per workflow, one source of truth.

Every workflow file under `workflows/` has two layers:

- a **human-readable guide** with 11 fixed sections (the canonical section
  list is in [`templates/WORKFLOW_TEMPLATE.md`](templates/WORKFLOW_TEMPLATE.md));
- a **compact AI specification** in YAML frontmatter that the router parses.

The frontmatter is generated from a canonical content map in
[`scripts/generate_workflows.py`](scripts/generate_workflows.py). Hand-editing
the rendered file works for one-offs; the validator regenerates them on the
next run. The map is the single source of truth.

### 3. Locale packs match the `zh-TW` structure, not its the size.

`shared/locales/zh-TW/` (legacy top-level mirror) and
`shared/locales/zh-CN/` (canonical subdirectory implementation) both follow
the same four-file layout: writing rules, glossary, style profiles, quality
checklist. Future locales must match this layout — they do not have to
match the size. The reference (zh-TW) sets the structural bar, not a word
count.

### 4. Editing intensity is automatic and escalates on regulated content.

Every workflow declares `editing_intensity` in its frontmatter
(`none` / `light` / `standard` / `strict_precision`). The router
auto-escalates to `strict_precision` for legal / medical / financial /
security / compliance / regulated outputs, regardless of the workflow's
declared intensity. This is the main thing keeping the layer from
"improving" a sentence it should not touch.

### 5. Protected content is named, not implied.

Every locale pack lists, in writing, the categories of content that are
never rewritten: code, identifiers, URLs, brand names, citations, numbers,
units, currency, dates, required technical or legal wording, and any term
the user has recorded in the context ledger. This is enforced at three
levels: the writing rules, the quality checklist, and the rubric's
`protected_content_preservation` dimension (1–5 score).

### 6. Evaluation is operator-driven on purpose, and is subscription-only.

[`tests/_evaluations/`](tests/_evaluations/) ships no API client, no
auto-scorer, no detector, and no API key handling of any kind. The
project explicitly does not use vendor APIs; operators run the
prompts in their own chat subscription (ChatGPT Plus / Pro, Claude
Free / Pro / Max, Gemini AI Pro / Ultra). The harness builds JSONL
stubs; the operator pastes each prompt into their chat UI, pastes
the response back, and scores per
[`tests/_evaluations/rubric.md`](tests/_evaluations/rubric.md). Reasons:

- Subscription billing is the user's choice, not the project's.
- A 100 % pass-rate batch is suspicious — partial results are normal.
- Auto-scorers do not catch subtle failures (e.g. wrong tone despite
  correct content) that a human reviewer sees immediately.

## Architecture overview

```text
                ┌──────────────────────────────────────────────┐
                │              user request                     │
                └────────────────────┬─────────────────────────┘
                                     │
                                     ▼
       ┌────────────────────────────────────────────────────┐
       │                       router                        │
       │  AI_ROUTER.md + ROUTING_RULES.md +                  │
       │  CLARIFICATION_PROTOCOL.md + CONTEXT_LEDGER.md +    │
       │  FALLBACK_RULES.md                                  │
       └────────────┬───────────────────────────┬────────────┘
                    │                           │
                    ▼                           ▼
   ┌────────────────────────┐    ┌────────────────────────────┐
   │   one of 100 workflows │    │     shared rule stack      │
   │   workflows/NNN-*.md   │    │     shared/MULTILINGUAL_*. │
   │   (29 + 24 + 18 + 17   │    │     shared/FACT_INFERENCE │
   │    + 12 = 100)         │    │     shared/OUTPUT_FORMATS │
   └────────────────────────┘    │     shared/QUALITY_*      │
                                 │     shared/SOURCE_AND_*   │
                                 └────────────────────────────┘
                                            │
                              ┌─────────────┴─────────────┐
                              ▼                           ▼
                 ┌────────────────────┐    ┌────────────────────────┐
                 │   locale layer      │    │   locale layer         │
                 │   shared/locales/   │    │   shared/locales/      │
                 │     zh-CN/         │    │     zh-TW/ (legacy     │
                 │   (4 files + readme)│    │      top-level mirror) │
                 └────────────────────┘    └────────────────────────┘
```

## Workflow contract

A workflow file under `workflows/NN-category/NNN-slug.md` is one unit of
work. It must contain:

| Section | Required | Source of truth |
| --- | :-: | --- |
| frontmatter: `id`, `slug`, `title`, `category`, `aliases`, `triggers`, `input_types`, `output_types`, `requires`, `produces`, `related`, `playbooks`, `mode_support`, `language_support`, `handoff` | yes | `scripts/generate_workflows.py` `WORKFLOWS` dict |
| frontmatter: `localization` block (only on high-traffic workflows) | no | `LOCALIZATION_OVERRIDES` map |
| `## What is this?` | yes | section list |
| `## Why use it?` | yes | section list |
| `## When should I use it?` | yes | section list |
| `## When should I not use it?` | yes | section list |
| `## What should I prepare?` | yes | section list |
| `## How does the AI help me?` | yes | section list |
| `## What will I get?` | yes | section list |
| `## How to start` | yes | section list |
| `## Related workflows` | yes | section list |
| `## Recommended next steps` | yes | section list |
| `## text` AI-spec (purpose / required_inputs / …) | yes | `templates/WORKFLOW_TEMPLATE.md` |

The router decision is driven by `triggers` (free-form phrases the user
might type) plus `category` plus `mode_support`. When the router can't
pick one workflow from those signals, it asks one short clarifying
question per [`router/CLARIFICATION_PROTOCOL.md`](router/CLARIFICATION_PROTOCOL.md).

## Router contract

The router's job is to map `(user_input, conversation_state)` to:

1. **one workflow** (or none + clarification),
2. **one locale layer** (or none if the deliverable is not Chinese),
3. **one style profile** (or the category default),
4. **one editing intensity** (subject to auto-escalation).

Constraints:

- The router never picks a workflow whose `localization.supported_locales`
  excludes the user's output language without first asking.
- The router never applies locale-specific editing rules to a deliverable
  whose output language is not the locale's language.
- The router never claims to bypass AI detection, remove watermarks, or
  prove human authorship. See
  [`router/FALLBACK_RULES.md`](router/FALLBACK_RULES.md).

The four input / output language combinations (Cases A–D) are spelled out
in [`router/AI_ROUTER.md`](router/AI_ROUTER.md). zh-CN adds Cases E–H
(English conversation + zh-CN deliverable, etc.).

## Localization contract

A locale pack is structurally five files under
`shared/locales/<code>/`:

| File | Purpose |
| --- | --- |
| `README.md` | Locale entry point. Lists what is in the pack and how the router activates it. |
| `WRITING_RULES.md` | Editorial principles, protected content, editing intensity, AI-pattern reduction. |
| `TERM_GLOSSARY.md` | Region-specific terms + cross-strait / cross-region glossary flips. |
| `STYLE_PROFILES.md` | Style profiles with channel, second-person policy, exemplar. |
| `QUALITY_CHECKLIST.md` | Dual-layer quality gate (compact AI-readable + human editorial). |

`zh-TW` predates this layout and lives at the top of `shared/`
(`shared/ZH_TW_*.md`). It is the reference implementation; new locales
should follow the subdirectory pattern.

**The localization layer never:**

- Claims to bypass AI detection or remove watermarks.
- Translates code, identifiers, URLs, or brand names.
- Replaces protected content (regulatory wording, citations, user-recorded
  terms) with the locale's "preferred" form.
- Switches a deliverable's output language without the user asking.

**The localization layer does:**

- Improve clarity, naturalness, and tone on unprotected spans.
- Enforce the editing intensity declared by the workflow (or escalated by
  the router for regulated content).
- Track user-recorded terminology in the context ledger and apply it on
  subsequent turns.

## Test & eval contract

There are two kinds of tests in this repository:

### Static structural tests

Run on every push / PR via
[`.github/workflows/validate.yml`](.github/workflows/validate.yml):

- `scripts/validate.py` checks workflow counts, IDs, slugs, required
  sections, AI-spec keys, and link resolution.
- `scripts/apply_localization.py` (yes, the name is a leftover from
  the Taiwan-only origin; it now covers both zh-TW and zh-CN entries)
  verifies every workflow with a `localization:` block matches the
  override map.

These tests are fast and run in CI. They do not call any model API.

### Functional evaluation (operator-driven)

[`tests/_evaluations/`](tests/_evaluations/) is operator-local and
gitignored for results. The contract is:

- `harness.py build-prompt` assembles a prompt for one case.
- `harness.py run-batch` writes a per-kind stub JSONL.
- An operator fills `response` (manually or via their own SDK).
- An operator scores 5 dimensions 1–5 per
  [`tests/_evaluations/rubric.md`](tests/_evaluations/rubric.md).
- A line is acceptable when `rubric_average ≥ 4.0` and no dimension < 3.
- A batch is acceptable when ≥ 90 % of lines are acceptable.

`shared/MODELS_OF_RECORD.md` is the canonical reference for which models
are eligible to run this. Pricing and capability tiers change frequently;
re-verify before any sweep.

## Versioning & compatibility

The repository follows [Semantic Versioning](https://semver.org/):

- **Patch** (1.0.x) — structural fixes, link fixes, typos. Backward
  compatible.
- **Minor** (1.x.0) — adds a workflow, a shared rule, or a locale pack.
  IDs and slugs of existing workflows are preserved.
- **Major** (x.0.0) — breaks the frontmatter schema, the routing
  contract, or the locale activation rules.

The maintainers cut tags from `main` after CI is green. The current
release is tagged in GitHub Releases.

## What we don't measure

- **AI detection scores.** The harness is not a detector benchmark. We
  do not run outputs through GPTZero, Originality.ai, or any commercial
  detector. The "human-likeness" of an output is not what
  `prompt-workflow-os` is optimizing for.
- **Watermark removal.** Not implemented, not tested, not promised.
- **Watermark presence.** If a vendor adds a watermark to model outputs,
  `prompt-workflow-os` does not interfere with it.
- **Real-time factuality.** We can flag factual risk via the rubric and
  the protected-content rules, but a verified, cited, true answer is not
  what the system guarantees. The user verifies claims; the AI surfaces
  what it knows.

## Resolved open questions

These four questions were raised in earlier versions of this document.
Each is resolved as of 2026-09-22.

1. **Should `zh-TW` migrate to the `shared/locales/zh-TW/` subdirectory
   layout?** — **Resolved: yes, done.** The four zh-TW content files now
   live at `shared/locales/zh-TW/` with shorter filenames matching the
   zh-CN convention (`WRITING_RULES.md`, `TERM_GLOSSARY.md`,
   `STYLE_PROFILES.md`, `QUALITY_CHECKLIST.md`) plus a `README.md` entry
   point. Every reference across the repository was rewritten.

2. **Should the harness auto-score?** — **Resolved: yes, with a thin
   guardrail.** [`tests/_evaluations/auto_scorer.py`](tests/_evaluations/auto_scorer.py)
   applies three checks: (a) main-content-language, (b) failure-condition
   phrase verbatim, (c) protected-span verbatim. It writes a verdict
   file next to the source JSONL and never overwrites the human
   `rubric` scores. The disambiguation between `zh-TW` and `zh-CN`
   (Traditional vs Simplified) is left to the human scorer — the
   auto-scorer only flags obvious failures like "expected English, got
   Chinese" or "this protected span is missing".

3. **Should `editing_intensity` be per-channel rather than per-workflow?**
   — **Resolved: keep per-workflow, add an override mechanism.** The
   current per-workflow model in the frontmatter is the source of truth
   for v1.x. The router already auto-escalates to `strict_precision`
   for regulated content. Channel-specific overrides would expand the
   schema without solving a problem the maintainers have evidence for;
   the router's channel hint already selects the style profile, which
   is the stronger lever. Revisit if per-channel failures start
   showing up in `tests/_evaluations/results/` baselines.

4. **How do we handle shared style profiles between `zh-TW` and `zh-CN`?**
   — **Resolved: shared core schema, locale-specific extensions.** See
   [`shared/locales/SHARED_STYLE_PROFILE_SCHEMA.md`](shared/locales/SHARED_STYLE_PROFILE_SCHEMA.md)
   for the 8 core fields and the two locale-specific extension sets.
   New locale packs implement the core first; locale-specific fields
   are optional.

## References

- [`README.md`](README.md) — entry point for new users.
- [`START.md`](START.md) — three-step quick start.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — PR rules and three contribution
  paths.
- [`router/AI_ROUTER.md`](router/AI_ROUTER.md) — canonical routing
  surface.
- [`shared/MODELS_OF_RECORD.md`](shared/MODELS_OF_RECORD.md) — model
  reference.
- [`shared/locales/`](shared/locales/) — locale architecture and
  reference implementations.
- [`tests/_evaluations/rubric.md`](tests/_evaluations/rubric.md) — the
  scoring rubric.

Last revised 2026-09-22.