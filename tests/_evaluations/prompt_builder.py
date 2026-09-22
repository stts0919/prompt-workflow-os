"""Build the prompt sent to a model under test.

For every test case the harness:

1. Loads the case file.
2. Parses the schema fields (User request, Requested output language,
   Target market, Expected locale, Expected style profile, Expected editing
   intensity, Expected router behavior, Protected content, Failure conditions).
3. Loads the workflow file (for workflow cases) or the language layer files
   (for zh-TW localization cases).
4. Assembles a single prompt that asks the model to behave as the router
   plus the workflow / zh-TW layer, and produce the expected output.

The prompt is deliberately explicit: the model is told which locale, profile,
and intensity are expected, but it must choose whether to honor them or to
fail. The test is whether it honors them — not whether it can pick the right
ones from scratch.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

LANGUAGE_FILES = {
    "zh-TW": [
        "shared/ZH_TW_LOCALIZATION_AND_WRITING_RULES.md",
        "shared/ZH_TW_TERM_GLOSSARY.md",
        "shared/ZH_TW_STYLE_PROFILES.md",
        "shared/ZH_TW_QUALITY_CHECKLIST.md",
    ],
    "zh-CN": [],
    "yue-Hant-HK": [],
    "en": [],
}


def read(path: str) -> str:
    full = (REPO_ROOT / path).resolve()
    if not full.exists():
        raise FileNotFoundError(full)
    return full.read_text(encoding="utf-8")


def parse_case(text: str) -> dict[str, str]:
    """Parse the per-case markdown fields into a dict.

    The case files use a one-line-per-field pattern:

        - **User request:** ...
        - **Requested output language:** ...
        - ...

    We extract both the label and the value. Values can span multiple lines if
    the writer used a multi-line blockquote, which is rare; we keep the simple
    case for now.
    """
    fields: dict[str, str] = {}
    for line in text.splitlines():
        m = re.match(r"^\s*-\s+\*\*(.+?):\*\*\s*(.*)$", line)
        if not m:
            continue
        key = m.group(1).strip().lower().replace(" ", "_")
        value = m.group(2).strip()
        fields[key] = value
    return fields


def split_cases(text: str) -> list[tuple[int | None, dict[str, str]]]:
    """Split a multi-case file into a list of (case_number, fields) tuples.

    Each case begins with a `## N. <title>` heading (1-based, integer-prefixed).
    Field blocks under that heading belong to that case. A file with no such
    headings is treated as a single case with `case_number=None`.
    """
    case_pattern = re.compile(r"^##\s+(\d+)\.\s+", re.MULTILINE)
    matches = list(case_pattern.finditer(text))
    if not matches:
        return [(None, parse_case(text))]

    cases: list[tuple[int | None, dict[str, str]]] = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end]
        number = int(m.group(1))
        cases.append((number, parse_case(body)))
    return cases


def count_cases(case_path: str) -> int:
    """Count how many `## N.` cases live in a file."""
    text = read(case_path)
    return len(split_cases(text))


def build_prompt(case_path: str, case_index: int = 0) -> dict[str, Any]:
    """Build the prompt for one test case.

    `case_index` is 0-based within the file. Returns a dict with:

    - case_id, case_kind, case_path
    - fields: parsed case schema fields
    - prompt: the assembled prompt text
    - locale: the locale to load (resolved from case fields)
    """
    text = read(case_path)
    cases = split_cases(text)
    if case_index < 0 or case_index >= len(cases):
        raise IndexError(
            f"case_index {case_index} out of range; file has {len(cases)} case(s)"
        )
    case_number, fields = cases[case_index]
    case_kind = "workflow" if "/workflow-cases/" in case_path else (
        "router" if "/router-cases/" in case_path else "language"
    )

    locale = fields.get("expected_locale") or fields.get("expected_zh-tw_layer") or ""
    locale_code = extract_locale_code(locale)

    layer_files = LANGUAGE_FILES.get(locale_code, [])
    layer_blob = ""
    if layer_files:
        loaded = []
        for f in layer_files:
            try:
                loaded.append(f"=== {f} ===\n{read(f)}")
            except FileNotFoundError:
                continue
        if loaded:
            layer_blob = "\n\n".join(loaded)

    workflow_blob = ""
    workflow_section = ""
    if case_kind == "workflow":
        m = re.search(r"\*\*Workflow selected:\*\*\s*\`([\w\-]+)\`", text)
        if m:
            slug = m.group(1)
            wf_path = find_workflow(slug)
            if wf_path:
                workflow_blob = read(wf_path)
                workflow_section = f"\n\n=== Workflow file ({wf_path}) ===\n{workflow_blob}"

    prompt = build_prompt_text(
        case_kind=case_kind,
        case_fields=fields,
        layer_blob=layer_blob,
        workflow_blob=workflow_blob,
        locale=locale,
        locale_code=locale_code,
    )

    return {
        "case_id": extract_case_id(case_path, case_number),
        "case_kind": case_kind,
        "case_path": case_path,
        "case_index": case_index,
        "fields": fields,
        "locale": locale,
        "locale_code": locale_code,
        "prompt": prompt,
    }


def build_prompt_text(
    *,
    case_kind: str,
    case_fields: dict[str, str],
    layer_blob: str,
    workflow_blob: str,
    locale: str,
    locale_code: str,
) -> str:
    """Assemble the actual prompt text. Kept separate for testability."""
    case_text = "\n".join(
        f"- {k.replace('_', ' ').title()}: {v}" for k, v in case_fields.items()
    )

    parts: list[str] = []
    parts.append(
        "You are being evaluated against the `prompt-workflow-os` repository. "
        "The repository provides 100 prompt workflows plus a router, playbooks, "
        "and a Taiwan Traditional Chinese (`zh-TW`) localization layer."
    )
    parts.append("")
    parts.append("Read the case below. Then behave as the router would:")
    parts.append(
        "1. Detect the input language, requested output language, and target market."
    )
    parts.append("2. If the locale layer should be active, load it and apply it.")
    parts.append("3. Pick the smallest sufficient workflow.")
    parts.append("4. Apply the chosen style profile.")
    parts.append("5. Apply the chosen editing intensity.")
    parts.append("6. Produce the final deliverable in the requested output language.")
    parts.append("")
    parts.append("Do not skip steps. Do not claim to bypass AI detection or remove watermarks.")
    parts.append("")
    parts.append("=== Test case ===")
    parts.append(case_text)
    parts.append("")

    if layer_blob:
        parts.append(
            f"=== Locale layer ({locale_code}) ===\n"
            "The following files implement the locale. Apply them when the case "
            "requires this locale. Do not paraphrase protected spans."
        )
        parts.append(layer_blob)
        parts.append("")

    if workflow_blob:
        parts.append(
            "=== Workflow file ===\n"
            "If a workflow is selected in the case, use it as your execution contract."
        )
        parts.append(workflow_blob)
        parts.append("")

    parts.append(
        "Now produce the deliverable. Keep the protected spans verbatim. "
        "Do not invent sources, customer counts, or personal anecdotes. "
        "If the case's failure conditions would apply to your output, "
        "deliberately avoid them and explain why in a one-line note."
    )

    return "\n".join(parts)


def extract_locale_code(locale_text: str) -> str:
    """Pull a BCP-47 code out of a case's locale field, default to empty."""
    m = re.search(r"\b(zh-[A-Z]+|en-[A-Z]+|ja-JP|ko-KR|id-ID|vi-VN)\b", locale_text or "")
    if m:
        return m.group(1)
    if "Taiwan" in locale_text or "zh-TW" in locale_text:
        return "zh-TW"
    return ""


def extract_case_id(case_path: str, case_number: int | None = None) -> str:
    """Pull a stable case id from the filename and (optional) case number."""
    p = Path(case_path)
    if case_number is not None:
        return f"{p.stem}#{case_number:02d}"
    return p.stem


def find_workflow(slug: str) -> str | None:
    """Find the workflow file path for a slug across all category folders."""
    for cat in ("01-content", "02-business", "03-research", "04-workflow", "05-technical"):
        path = REPO_ROOT / "workflows" / cat
        if not path.exists():
            continue
        for p in path.iterdir():
            if p.stem.endswith(slug):
                return str(p.relative_to(REPO_ROOT))
    return None
