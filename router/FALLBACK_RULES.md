# Fallback Rules

What the AI does when no workflow is a clean match, when information is insufficient, or when the request is out of scope.

## 1. No matching workflow

If no workflow in [indexes/05-all-100-workflows.md](../indexes/05-all-100-workflows.md) is a clean match:

1. Pick the closest workflow by purpose and category. Say which one you chose and why.
2. State explicitly which parts of the user's request fall outside any workflow's scope.
3. Apply the workflow's AI specification to the parts that fit, and write a structured "outside-scope" section for the rest.
4. Suggest a workflow to add to the repository (suggest slug + 1-line purpose) so future requests are covered.

## 2. Missing required input

If a workflow's `requires` list cannot be satisfied even after five clarifications:

1. Switch into `recommend` mode. Present the planned workflow chain plus the inputs you still need.
2. State which assumption you will make for each missing input, and how it would change if the user supplied the real value.
3. Ask one final focused question that, if answered, unblocks the work.

## 3. Current-information gap

If the request needs current information and the user has not provided sources or browsing permission:

1. State that verification is required. Do not invent sources.
2. Offer two paths:
   - User supplies links / files.
   - User grants browsing permission.
3. If the user picks path 2, follow [../shared/SOURCE_AND_CITATION_RULES.md](../shared/SOURCE_AND_CITATION_RULES.md).

## 4. Out-of-scope or unsafe request

If the request is outside the repository's domain (medical, legal, financial advice requiring a license, etc.):

1. State the boundary plainly.
2. Offer the workflow that *does* fit (often `customer-interview`, `market-research`, or `business-decision`) and explain why.
3. Recommend that the user consult a qualified professional for the specific decision.

## 5. Forbidden content

If the request asks for disallowed content (hate speech, instructions to harm, illegal activity, or anything disallowed by the AI provider's policy):

1. Refuse at the policy layer first.
2. Do not route through any workflow.
3. Offer an alternative legitimate workflow when possible.

## 6. Multi-language delivery

If the deliverable must be in a different language than the conversation:

1. Keep the conversation in the user's writing language.
2. Produce the deliverable in the requested language.
3. Preserve code, IDs, and English workflow names.

## 7. Long input handling

If the input is too large for one prompt:

1. Use `document-summary` (058) or `content-summary` (010) to compress it.
2. Route downstream into the consuming workflow with the summary as context.
3. Tell the user which sections were summarized and which were preserved verbatim.

## 8. Partial completion

If execution fails partway (the workflow chain is interrupted):

1. Mark the deliverable as partial.
2. List what was produced, what was skipped, and why.
3. Suggest the next workflow to resume from.
