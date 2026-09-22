# Workflow Case — Debugging

## Setup

- Mode: `guide`.
- Workflow: `debugging` (094).

## Input

```python
def parse(date_str):
    from datetime import datetime
    return datetime.strptime(date_str, "%Y-%m-%d")

print(parse("2024/02/30"))
```

Error: `ValueError: time data '2024/02/30' does not match format '%Y-%m-%d'`.

## Expected output

A root-cause analysis that:

1. Names the format mismatch (`/` vs `-`).
2. Notes that `02/30` is also invalid as a date even with `/`.
3. Proposes a fix (handle multiple formats with try/except or normalize).
4. Defines a verification step (unit tests for multiple input shapes).

## Verification

- Top fix is the format mismatch, not invented causes.
- At least two root-cause candidates are considered.
- Suggested fix is minimal and safe.
- Verification approach is concrete.

## Failure conditions

- Inventing a Python library import error.
- Suggesting a complex refactor.
- Skipping verification.
