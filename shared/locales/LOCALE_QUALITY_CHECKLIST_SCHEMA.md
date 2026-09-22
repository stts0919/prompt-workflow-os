# Locale Quality Checklist Schema

Every locale pack must define its quality checklist using this two-layer schema. The `zh-TW` check list under [../ZH_TW_QUALITY_CHECKLIST.md](../ZH_TW_QUALITY_CHECKLIST.md) is the reference implementation.

## Two layers

### Layer 1 — Compact AI-readable checklist

The AI applies this compressed form silently to its own draft:

```text
language:
  - is locale-appropriate (or requested variant)
  - words regionally natural
  - user terminology preserved
  - protected content (code, IDs, URLs, brand names) intact
  - one style profile, consistent
  - no silent language drift

accuracy:
  - facts, numbers, quotes, dates preserved or labeled
  - sources cited
  - assumption / inference / recommendation labeled
  - no invented evidence or experience
  - uncertainty stays uncertain
  - no detector / watermark / authorship claims

writing:
  - opening reaches the point
  - no empty era framing
  - adjectives carry evidence
  - sentence rhythm varied
  - connectives used when needed
  - triadic lists only when distinct
  - verbs concrete
  - lists genuinely distinct
  - transitions necessary
  - ending matches content
  - no reflective human-experience claims

voice:
  - tone matches audience and channel
  - casualness is appropriate
  - first-person matches profile policy
  - second-person matches profile policy (formality)
  - rhetorical questions only when useful
  - reads like competent human editorial pass

channel:
  - profile matches the platform
  - length matches platform norms
  - punctuation follows profile notes

intensity:
  - chosen intensity matches content type
  - high-risk content is in strict_precision

safety:
  - code / URLs / citations / brand names unchanged
  - workflow IDs and slugs unchanged
  - no fabricated evidence
  - no detector / watermark / authorship claims
  - required disclosures preserved
```

### Layer 2 — Human-readable editorial review checklist

A human editor walks through these checks before approving the deliverable:

- **Language and localization**: wording natural for the locale; user terminology preserved; protected spans unchanged.
- **Accuracy and evidence**: facts, numbers, sources, quotes, and uncertainty preserved; assumptions separated from facts; no invented evidence.
- **Writing quality**: opening reaches the point; sentence rhythm varied; lists genuinely distinct; ending fits purpose; AI tells removed.
- **Channel fit**: tone matches platform; casualness appropriate; punctuation and length follow profile notes.
- **Safety**: protected spans unchanged; no watermark-removal or detector-evasion claims; required disclosures preserved.

## Locale-specific additions

Each locale pack may add language-specific checks under the same five concerns. For example:

- `ja-JP` may add a keigo-correctness check under voice and channel fit.
- `en-GB` may add spelling-variation checks (organisation vs organization).
- `zh-CN` may add political-terminology awareness checks under accuracy.

These additions must not remove the universal checks.

## Validation

The structural validator checks:

- Layer 1 is present in the locale's quality checklist.
- Layer 2 is present.
- The five concerns are explicitly named.
- The locale does not claim that editing bypasses detection, removes watermarks, or proves human authorship.
