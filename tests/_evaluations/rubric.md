# Evaluation Rubric

Each recorded result carries five rubric dimensions scored 1–5. A result line is **acceptable** only when the average ≥ 4.0 and no individual score is below 3.

## Dimensions

### 1. `locale_correctness` (1–5)

Did the model apply the right locale layer for the case's `Expected locale`?

- **5** — Activated the locale's writing rules / glossary / profiles correctly (or correctly skipped the layer when the case required a non-zh-TW override).
- **4** — Activated the locale but missed one sub-component (e.g. used the glossary but ignored the style profile).
- **3** — Activated a locale but the wrong one (e.g. applied Taiwan when Mainland was requested).
- **2** — Activated no locale when one was clearly needed.
- **1** — Mixed locales within one output (e.g. Mainland vocabulary inside a Taiwan-targeted piece).

### 2. `style_profile_adherence` (1–5)

Did the model's output match the case's `Expected style profile`?

- **5** — Tone, sentence rhythm, formality, and ending style all match the profile description.
- **4** — Three of the four match; one is mildly off.
- **3** — Roughly the right register but missing one defining trait of the profile (e.g. an Instagram-casual post that uses formal endings).
- **2** — Wrong register (e.g. a sales-clear response that reads as a research report).
- **1** — No perceptible profile awareness.

### 3. `protected_content_preservation` (1–5)

Did the model preserve protected spans verbatim?

- **5** — Every protected span (code, IDs, URLs, brand names, citations, quotes, dates, numbers, units, tables, required disclosures) appears exactly as supplied.
- **4** — Protected spans preserved but minor whitespace differences.
- **3** — One protected span altered (e.g. workflow ID translated).
- **2** — More than one protected span altered but recoverable.
- **1** — Critical protected span lost (e.g. quote rewritten, citation dropped).

### 4. `failure_condition_avoidance` (1–5)

Did the model avoid the case's listed failure conditions?

- **5** — Every failure condition in the case is avoided.
- **4** — One minor failure condition triggered.
- **3** — Multiple minor failures or one significant failure.
- **2** — Significant failures that materially damage the output.
- **1** — Critical failure (e.g. fabricated evidence, Mainland-only vocabulary in a Taiwan case, claim to bypass detectors).

### 5. `output_language_correctness` (1–5)

Did the model produce the deliverable in the case's `Requested output language`?

- **5** — Output language matches the request; conversation language rules are honored (e.g. zh-TW conversation → English email body).
- **4** — Output language correct but with a stray word from the conversation language (acceptable in casual contexts).
- **3** — Output language mostly correct with structural deviations.
- **2** — Wrong output language for a clear request.
- **1** — Output language matches the conversation but ignored an explicit deliverable-language request.

## Aggregate

`rubric_average` = mean of the five scores (rounded to 2 decimals).

A result is **acceptable** when `rubric_average >= 4.0` and no individual dimension is below 3.

A run is **acceptable** when ≥ 90% of cases are acceptable.

## How to score

The operator (human) reads the model's output against the case's `Expected` and `Failure conditions` sections, assigns a score per dimension, and writes them into the JSONL record. No automatic scoring is implemented; the rubric is intentionally a human-judgment tool.

For high-volume runs, a separate auto-scorer may later implement string-matching checks for protected content and forbidden phrases; today it is fully manual.

## What this rubric does NOT measure

- Whether the model's output is "human-like" by any detector. We do not score against detectors.
- Whether watermarks were removed. We do not allow that claim and do not measure it.
- Whether the output passes any third-party "AI detection" tool. Out of scope.
