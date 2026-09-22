# Language Case — German Conversation with English Code

## Setup

- Mode: `guide`.
- Detected language: German.

## Input

> Bitte hilf mir mit debugging (094). Mein Code wirft einen TypeError.

```python
def total(items): return items.sum()
total([1,2,3])
```

## Expected behavior

- Reply in German.
- Use `debugging` (094).
- Keep code in English / Python.
- Diagnosis should be in German, code references preserve case.

## Expected output

A root-cause analysis in German naming the `sum()` method does not exist on lists (use `sum` builtin or `numpy.sum`).

## Failure conditions

- Replying in English.
- Translating code identifiers (`items` → `Artikel`).
- Failing to identify the actual bug.
