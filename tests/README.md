# Tests

Evaluation cases for the router, language behavior, and individual workflows.

Each case is a single Markdown file under one of:

- `router-cases/` — how the router classifies and routes a request.
- `language-cases/` — multilingual detection and output behavior.
- `workflow-cases/` — single-workflow execution correctness.

Use [templates/EVALUATION_CASE_TEMPLATE.md](../templates/EVALUATION_CASE_TEMPLATE.md) to add new cases.

## Counts (current)

| Area           | Cases |
| -------------- | ----: |
| router-cases   |    15 |
| language-cases |    10 |
| workflow-cases |    10 |

## Why these cases

Router cases cover:

- vague user requests (1, 4, 7, 8)
- incomplete inputs (3, 11)
- already-complete inputs (5, 9)
- requests needing current information (13)
- requests that map to multiple workflows (10)
- requests where `quick mode` should bypass questioning (6, 9)
- cases where the router should ask clarifying questions (1, 2, 4, 7, 8)
- cases where no exact workflow exists (12, 14, 15)

Language cases cover detection, mixed-language input, output in a different language, and preserving English workflow IDs in non-English content.

Workflow cases cover key outputs of representative workflows.

## How to run

The validation script `scripts/validate.py` checks the repository's structural rules. Use it before merging. Run from the repository root:

```bash
python3 scripts/validate.py
```

This script does not run the test cases themselves — it validates the structure. Functional evaluation of cases requires running them against an AI model with the latest repository attached.
