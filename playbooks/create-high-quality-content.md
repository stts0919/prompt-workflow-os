---
playbook: create-high-quality-content
slug: create-high-quality-content
title: Create High-Quality Content
mode_default: guide
stages: 6
---

# Create High-Quality Content

## User scenario

You have a topic and want to publish a substantive piece — an article, a long LinkedIn post, or a recurring newsletter issue — and you want a structured path from idea to publish-ready output.

## Intended final outcome

A publish-ready article or long-form post that has been outlined, drafted, edited, repurposed, and quality-reviewed.

## Workflow sequence

1. **[001 — Generate Content Ideas](../workflows/01-content/001-content-idea-generation.md)** — narrow to a chosen topic and angle.
2. **[005 — Prioritize Content Topics](../workflows/01-content/005-topic-prioritization.md)** — score the topic against criteria when you have multiple.
3. **[006 — Create an Article Outline](../workflows/01-content/006-article-outline.md)** — build the structure before drafting.
4. **[007 — Draft an Article](../workflows/01-content/007-article-draft.md)** — produce the first draft from the outline.
5. **[009 — Edit for Clarity](../workflows/01-content/009-content-editing.md)** — clean structure, sentence-level clarity, concision.
6. **[029 — Review Content Quality](../workflows/01-content/029-content-quality-review.md)** — run the rubric before publishing.

## Optional add-on

After step 6, run **[028 — Repurpose Content](../workflows/01-content/028-content-repurposing.md)** to spread the same effort across channels.

## Handoff data between steps

| From → To    | Key                | Description                                            |
| ------------ | ------------------ | ------------------------------------------------------ |
| step 1 → 2   | `idea_list`        | Ranked idea backlog                                    |
| step 2 → 3   | `chosen_topic`     | Selected topic with score rationale                    |
| step 3 → 4   | `outline`          | Hierarchical outline with section beats                |
| step 4 → 5   | `draft`            | Complete first draft                                   |
| step 5 → 6   | `edited_draft`     | Edited draft with edit notes                           |

## Routing conditions

- Trigger phrases include "write me an article", "publish a piece", "long-form post", "newsletter issue".
- Use when the user wants a structured publish-ready artifact.

## Skip conditions

- If the topic is set, skip step 1.
- If the outline exists, skip steps 1–3.
- If the user wants a short post only, switch to social-post (012).

## Example start message

```
Read this repository's START.md and help me publish this article.

Topic: [the topic]
Audience: [who will read]
Length: [target word count]
Voice: [reference or description]
Constraints: [must-include, must-avoid]
```

## Final quality check

Before sign-off:

- Outline matches the article's actual structure.
- Draft covers every outline point.
- Edit notes flag open questions for the author.
- Quality review produces a short list of severity-tagged issues, with no blockers remaining.

## AI specification

```yaml
playbook: create-high-quality-content
rule: "Skip steps whose output is already supplied."
mode: "guide by default; allow quick mode when the user provides a full outline."
skip_rules:
  - "If topic is set, skip step 1."
  - "If outline exists, skip steps 1–3."
  - "If the user wants a short post, switch to social-post."
```
