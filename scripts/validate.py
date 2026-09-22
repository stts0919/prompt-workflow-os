#!/usr/bin/env python3
"""Structural validation for the prompt-workflow-os repository.

Exit code is non-zero when any check fails.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKFLOWS_DIR = ROOT / "workflows"
INDEXES_DIR = ROOT / "indexes"
ROUTER_DIR = ROOT / "router"
SHARED_DIR = ROOT / "shared"
PLAYBOOKS_DIR = ROOT / "playbooks"
TESTS_DIR = ROOT / "tests"

CATEGORY_DIR = {
    "content": "01-content",
    "business": "02-business",
    "research": "03-research",
    "workflow": "04-workflow",
    "technical": "05-technical",
}

EXPECTED_CATEGORY_COUNTS = {
    "content": 29,
    "business": 24,
    "research": 18,
    "workflow": 17,
    "technical": 12,
}

REQUIRED_FRONT_FIELDS = [
    "id", "slug", "title", "category", "aliases", "triggers",
    "input_types", "output_types", "requires", "produces",
    "related", "playbooks", "mode_support", "language_support", "handoff",
]

REQUIRED_HUMAN_SECTIONS = [
    "## What is this?",
    "## Why use it?",
    "## When should I use it?",
    "## When should I not use it?",
    "## What should I prepare?",
    "## How does the AI help me?",
    "## What will I get?",
    "## How to start",
    "## Related workflows",
    "## Recommended next steps",
    "## AI specification",
]

REQUIRED_AI_SPEC_KEYS = [
    "purpose", "required_inputs", "ask_if_missing",
    "do_not_use_when", "workflow", "output_contract",
    "quality_rules", "handoff",
]


def parse_frontmatter(text):
    """Parse the YAML frontmatter block. Returns dict with raw string values."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    block = text[4:end]
    fields = {}
    # Naive YAML list parser for our frontmatter format.
    current_list = None
    current_key = None
    for line in block.splitlines():
        if not line.strip():
            continue
        m_list = re.match(r"^([a-z_]+):\s*$", line)
        m_scalar = re.match(r'^([a-z_]+):\s*"?(.*?)"?\s*$', line)
        m_item = re.match(r"^\s+-\s+(.*)$", line)
        m_item_kv = re.match(r"^\s+-\s+([a-z_]+):\s*(.+)$", line)
        m_item_kv_cont = re.match(r"^\s+([a-z_]+):\s*(.+)$", line)
        if m_list:
            current_list = m_list.group(1)
            fields.setdefault(current_list, [])
            current_key = None
        elif m_scalar:
            current_list = None
            fields[m_scalar.group(1)] = m_scalar.group(2)
            current_key = None
        elif m_item_kv:
            current_list = None
            fields[m_item_kv.group(1)] = fields.get(m_item_kv.group(1), [])
            current_key = m_item_kv.group(1)
            # Append as a dict.
            fields[m_item_kv.group(1)].append({m_item_kv.group(1): m_item_kv.group(2)})
        elif m_item_kv_cont and current_key:
            fields[current_key][-1][m_item_kv_cont.group(1)] = m_item_kv_cont.group(2)
        elif m_item and current_list is not None:
            fields[current_list].append(m_item.group(1))
        elif m_item:
            # Default to a list of "misc"
            fields.setdefault("_misc", []).append(m_item.group(1))
    return fields


def load_workflows():
    out = []
    for cat, dir_name in CATEGORY_DIR.items():
        d = WORKFLOWS_DIR / dir_name
        for p in sorted(d.iterdir()):
            if not p.name.endswith(".md"):
                continue
            out.append((cat, p, p.read_text()))
    return out


def check_workflow(cat, path, text):
    errors = []
    name = path.name
    fm = parse_frontmatter(text)
    if fm is None:
        return [f"{name}: missing or invalid frontmatter"]
    if fm.get("id") != path.name[:3]:
        errors.append(f"{name}: frontmatter id {fm.get('id')} does not match filename id {path.name[:3]}")
    if fm.get("slug") != path.stem[4:]:
        errors.append(f"{name}: frontmatter slug '{fm.get('slug')}' does not match filename slug")
    if fm.get("category") != cat:
        errors.append(f"{name}: category '{fm.get('category')}' does not match folder '{cat}'")
    for field in REQUIRED_FRONT_FIELDS:
        if field not in fm:
            errors.append(f"{name}: missing frontmatter field '{field}'")
    body = text[text.find("\n---\n", 4) + 5:]
    for section in REQUIRED_HUMAN_SECTIONS:
        if section not in body:
            errors.append(f"{name}: missing human section '{section}'")
    if "## AI specification" not in body:
        errors.append(f"{name}: missing AI specification section")
    else:
        ai_block_match = re.search(r"## AI specification\n+```text\n(.+?)\n```", body, re.DOTALL)
        if not ai_block_match:
            errors.append(f"{name}: AI specification must be in a ```text``` block")
        else:
            ai_block = ai_block_match.group(1)
            for key in REQUIRED_AI_SPEC_KEYS:
                if not re.search(rf"^{re.escape(key)}:", ai_block, flags=re.MULTILINE):
                    errors.append(f"{name}: AI spec missing key '{key}'")
    return errors


def check_links(root):
    errors = []
    for p in root.rglob("*.md"):
        text = p.read_text()
        for label, target in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text):
            if target.startswith(("http", "#", "mailto:")):
                continue
            target_path = (p.parent / target).resolve()
            if not target_path.exists():
                errors.append(f"{p.relative_to(ROOT)}: link '{target}' (from '{label}') is missing")
    return errors


def main():
    all_errors = []

    workflows = load_workflows()
    counts = {c: 0 for c in CATEGORY_DIR}
    for cat, path, text in workflows:
        counts[cat] += 1
        all_errors.extend(check_workflow(cat, path, text))

    # Counts
    if len(workflows) != 100:
        all_errors.append(f"total workflow count is {len(workflows)}, expected 100")
    for cat, expected in EXPECTED_CATEGORY_COUNTS.items():
        if counts.get(cat, 0) != expected:
            all_errors.append(f"category '{cat}' has {counts.get(cat, 0)} workflows, expected {expected}")

    # ID range + uniqueness
    seen_ids = set()
    seen_slugs = set()
    for cat, path, text in workflows:
        wid = path.name[:3]
        slug = path.stem[4:]
        if not re.fullmatch(r"\d{3}", wid):
            all_errors.append(f"{path.relative_to(ROOT)}: id '{wid}' is not a 3-digit numeric")
        if not (1 <= int(wid) <= 100):
            all_errors.append(f"{path.relative_to(ROOT)}: id '{wid}' is outside 001–100")
        if wid in seen_ids:
            all_errors.append(f"duplicate workflow id '{wid}'")
        seen_ids.add(wid)
        if slug in seen_slugs:
            all_errors.append(f"duplicate workflow slug '{slug}'")
        seen_slugs.add(slug)

    # Required directories
    for d in [INDEXES_DIR, ROUTER_DIR, SHARED_DIR, PLAYBOOKS_DIR, TESTS_DIR]:
        if not d.exists():
            all_errors.append(f"missing directory: {d.relative_to(ROOT)}")

    # Required files
    required_files = [
        "README.md", "START.md", "AGENTS.md", "LICENSE", "CHANGELOG.md",
        "AUDIT_REPORT.md", "VALIDATION_REPORT.md",
        "indexes/00-start-here.md", "indexes/01-by-goal.md", "indexes/02-by-problem.md",
        "indexes/03-by-input.md", "indexes/04-by-output.md", "indexes/05-all-100-workflows.md",
        "router/AI_ROUTER.md", "router/ROUTING_RULES.md", "router/CLARIFICATION_PROTOCOL.md",
        "router/CONTEXT_LEDGER.md", "router/FALLBACK_RULES.md",
        "shared/MULTILINGUAL_RULES.md", "shared/FACT_INFERENCE_RULES.md",
        "shared/OUTPUT_FORMATS.md", "shared/QUALITY_CHECKLISTS.md",
        "shared/SOURCE_AND_CITATION_RULES.md",
        "templates/WORKFLOW_TEMPLATE.md", "templates/PLAYBOOK_TEMPLATE.md",
        "templates/EVALUATION_CASE_TEMPLATE.md",
        "tests/README.md",
        "playbooks/README.md",
    ]
    for rel in required_files:
        if not (ROOT / rel).exists():
            all_errors.append(f"missing required file: {rel}")

    # Test counts
    router_cases = list((TESTS_DIR / "router-cases").glob("*.md")) if (TESTS_DIR / "router-cases").exists() else []
    language_cases = list((TESTS_DIR / "language-cases").glob("*.md")) if (TESTS_DIR / "language-cases").exists() else []
    workflow_cases = list((TESTS_DIR / "workflow-cases").glob("*.md")) if (TESTS_DIR / "workflow-cases").exists() else []
    if len(router_cases) < 15:
        all_errors.append(f"router-cases count is {len(router_cases)}, expected at least 15")
    if len(language_cases) < 10:
        all_errors.append(f"language-cases count is {len(language_cases)}, expected at least 10")
    if len(workflow_cases) < 10:
        all_errors.append(f"workflow-cases count is {len(workflow_cases)}, expected at least 10")

    # Playbook count + workflow links
    playbook_files = [p for p in PLAYBOOKS_DIR.glob("*.md") if p.name != "README.md"]
    if len(playbook_files) < 5:
        all_errors.append(f"playbook count is {len(playbook_files)}, expected at least 5")
    for p in playbook_files:
        text = p.read_text()
        if not re.search(r"##\s+Workflow sequence", text):
            all_errors.append(f"{p.relative_to(ROOT)}: missing 'Workflow sequence' section")

    # Index completeness
    all_index = INDEXES_DIR / "05-all-100-workflows.md"
    if all_index.exists():
        idx_text = all_index.read_text()
        for cat, dir_name in CATEGORY_DIR.items():
            d = WORKFLOWS_DIR / dir_name
            for p in sorted(d.iterdir()):
                if not p.name.endswith(".md"):
                    continue
                # Check the filename appears as a link
                if p.name not in idx_text:
                    all_errors.append(f"05-all-100-workflows.md missing entry for {p.name}")
                break  # spot-check one per category is enough

    # Link validity (across the whole repository) — skip placeholder template links.
    TEMPLATE_PLACEHOLDERS = (
        "../workflows/<category>/<id>-<slug>.md",
    )
    file_errors = check_links(ROOT)
    for err in file_errors:
        skip = False
        for placeholder in TEMPLATE_PLACEHOLDERS:
            if placeholder in err:
                skip = True
                break
        if not skip:
            all_errors.append(err)

    # === Taiwan Traditional Chinese localization layer checks =================

    zh_tw_files = [
        "shared/ZH_TW_LOCALIZATION_AND_WRITING_RULES.md",
        "shared/ZH_TW_TERM_GLOSSARY.md",
        "shared/ZH_TW_STYLE_PROFILES.md",
        "shared/ZH_TW_QUALITY_CHECKLIST.md",
        "tests/language-cases/zh-tw-localization-cases.md",
        "tests/workflow-cases/zh-tw-output-quality-cases.md",
        "ZH_TW_LOCALIZATION_VALIDATION_REPORT.md",
        "ZH_TW_IMPLEMENTATION_VALIDATION_REPORT.md",
        "shared/locales/README.md",
        "shared/locales/LOCALE_ROUTING_RULES.md",
        "shared/locales/LOCALE_STYLE_PROFILE_SCHEMA.md",
        "shared/locales/LOCALE_TERM_GLOSSARY_SCHEMA.md",
        "shared/locales/LOCALE_QUALITY_CHECKLIST_SCHEMA.md",
        "shared/locales/FUTURE_LOCALE_EXPANSION_PLAN.md",
    ]
    for rel in zh_tw_files:
        if not (ROOT / rel).exists():
            all_errors.append(f"missing required file: {rel}")

    # Router files must reference the zh-TW shared rule files.
    ai_router_text = (ROOT / "router/AI_ROUTER.md").read_text()
    for ref in [
        "ZH_TW_LOCALIZATION_AND_WRITING_RULES.md",
        "ZH_TW_STYLE_PROFILES.md",
        "ZH_TW_QUALITY_CHECKLIST.md",
        "ZH_TW_TERM_GLOSSARY.md",
    ]:
        if ref not in ai_router_text:
            all_errors.append(f"router/AI_ROUTER.md missing reference to {ref}")
    rrules_text = (ROOT / "router/ROUTING_RULES.md").read_text()
    if "ZH_TW_STYLE_PROFILES" not in rrules_text and "style_profile" not in rrules_text:
        all_errors.append("router/ROUTING_RULES.md missing zh-TW style profile rule")
    cproto_text = (ROOT / "router/CLARIFICATION_PROTOCOL.md").read_text()
    if "zh-TW" not in cproto_text and "Traditional Chinese" not in cproto_text:
        all_errors.append("router/CLARIFICATION_PROTOCOL.md missing zh-TW clarification guidance")

    # Workflow template must include the new locale metadata schema.
    template_text = (ROOT / "templates/WORKFLOW_TEMPLATE.md").read_text()
    for required_key in [
        "localization",
        "supported_locales",
        "locale_style_profile_overrides",
        "editing_intensity",
    ]:
        if required_key not in template_text:
            all_errors.append(f"templates/WORKFLOW_TEMPLATE.md missing '{required_key}'")

    # Glossary must contain at least 150 entries.
    glossary_path = ROOT / "shared/ZH_TW_TERM_GLOSSARY.md"
    if glossary_path.exists():
        glossary_text = glossary_path.read_text()
        entry_count = 0
        for line in glossary_text.splitlines():
            stripped = line.strip()
            if stripped.startswith("|") and not stripped.startswith("| #") and not stripped.startswith("|---"):
                if re.match(r"\|\s+\d+\s+\|", stripped):
                    entry_count += 1
        if entry_count < 150:
            all_errors.append(f"ZH_TW term glossary has {entry_count} entries, expected at least 150")

    # Style profiles must contain at least 15 profiles.
    profiles_path = ROOT / "shared/ZH_TW_STYLE_PROFILES.md"
    if profiles_path.exists():
        profiles_text = profiles_path.read_text()
        profile_ids = set(re.findall(r"id:\s+(zh-tw-[\w-]+)", profiles_text))
        profile_headers = set(re.findall(r"^##\s+\d+\.\s+`(zh-tw-[\w-]+)`", profiles_text, flags=re.MULTILINE))
        all_profiles = profile_ids | profile_headers
        if len(all_profiles) < 15:
            all_errors.append(
                f"ZH_TW style profiles has {len(all_profiles)} profiles, expected at least 15"
            )

    # Localization tests count (≥30).
    loc_cases_path = ROOT / "tests/language-cases/zh-tw-localization-cases.md"
    if loc_cases_path.exists():
        loc_text = loc_cases_path.read_text()
        loc_case_headers = re.findall(r"^##\s+\d+\.\s+", loc_text, flags=re.MULTILINE)
        if len(loc_case_headers) < 30:
            all_errors.append(
                f"zh-tw localization cases has {len(loc_case_headers)} cases, expected at least 30"
            )

    # Output-quality tests count (≥25).
    wf_cases_path = ROOT / "tests/workflow-cases/zh-tw-output-quality-cases.md"
    if wf_cases_path.exists():
        wf_text = wf_cases_path.read_text()
        wf_case_headers = re.findall(r"^##\s+\d+\.\s+", wf_text, flags=re.MULTILINE)
        if len(wf_case_headers) < 25:
            all_errors.append(
                f"zh-tw output-quality cases has {len(wf_case_headers)} cases, expected at least 25"
            )

    # === No false-claims check ================================================
    # The repository must not claim that the system can bypass AI detectors,
    # remove watermarks, or prove human authorship. Negative/descriptive mentions
    # are allowed; positive capability claims are not.

    FALSE_CLAIM_PATTERNS = [
        (r"can\s+bypass\s+(?:ai|gptzero|detector|detection)", "AI detection bypass claim"),
        (r"removes?\s+(?:ai|gptzero|claude)?\s*watermark", "watermark removal claim"),
        (r"guarantees?\s+human\s+authorship", "human authorship guarantee"),
        (r"proves?\s+(?:that|human)\s+authorship", "human authorship proof"),
        (r"(?:will|makes)\s+ai-?generated\s+text\s+(?:undetectable|pass)", "AI text undetectability"),
        (r"(?:bypass|evade)\s+(?:ai\s+)?detector", "detector bypass"),
    ]

    # Allowed contexts (negatives, descriptions, disclaimers) — file-level allowlist:
    # If the phrase appears in a clearly negative / disclaimer context, skip.
    def negative_context(line):
        lowered = line.lower()
        cues = [
            "does not", "do not", "doesn't", "don't", "cannot", "can't",
            "must not", "must never", "never", "no longer", "won't", "will not",
            "should not", "shouldn't", "would not", "wouldn't",
            "is not positioned", "not positioned", "not a tool",
            "do not claim", "not claim", "did not", "isn't", "aren't",
            "no ", "not ", "avoid", "without claiming", "without asserting",
            # Chinese
            "不", "未", "聲稱", "禁止", "聲明", "避免",
        ]
        if any(w in lowered for w in cues):
            return True
        # Header-style required protections often describe what the AI must avoid.
        if "required protections" in lowered or "禁止" in line or "禁止宣" in line:
            return True
        # Lines that describe what the user asks for (router/AI_ROUTER.md scenarios)
        # describe a request, not a system capability.
        scenario_cues = [
            "user asks", "user asks the ai", "user requested",
            "if the user asks", "if user asks",
            "you ask the ai", "user asks for",
        ]
        if any(w in lowered for w in scenario_cues):
            return True
        # Failure-condition lines describe what the AI must NOT do.
        if "failure condition" in lowered or "claim: " in lowered:
            return True
        return False


    def broader_negative_window(file_text, match_start):
        # Look at the surrounding 400 characters (e.g. previous bullet or sentence).
        window_start = max(0, match_start - 400)
        window = file_text[window_start:match_start].lower()
        return any(cue in window for cue in ["must not", "does not", "do not", "cannot", "never", "avoid", "不", "禁止"])

    for path in ROOT.rglob("*.md"):
        if path.is_relative_to(ROOT / "scripts") or path.is_relative_to(ROOT / ".git"):
            continue
        text = path.read_text()
        for pattern, label in FALSE_CLAIM_PATTERNS:
            for m in re.finditer(pattern, text, flags=re.IGNORECASE):
                # Capture the surrounding line.
                start = text.rfind("\n", 0, m.start()) + 1
                end = text.find("\n", m.end())
                line = text[start:end] if end != -1 else text[start:]
                if negative_context(line):
                    continue
                if broader_negative_window(text, m.start()):
                    continue
                rel = path.relative_to(ROOT)
                all_errors.append(
                    f"{rel}: prohibited claim about editing capability — '{label}' ({line.strip()[:120]})"
                )

    # Report
    print("=" * 60)
    if all_errors:
        print(f"VALIDATION FAILED — {len(all_errors)} issue(s)")
        print("=" * 60)
        for err in all_errors:
            print(" -", err)
        sys.exit(1)
    else:
        print("VALIDATION PASSED — 0 issues")
        print("=" * 60)
        print(f"Workflow counts: {counts}")
        print(f"Total workflows: {len(workflows)}")
        print(f"Router cases: {len(router_cases)}")
        print(f"Language cases: {len(language_cases)}")
        print(f"Workflow cases: {len(workflow_cases)}")
        print(f"Playbooks: {len(playbook_files)}")
        if glossary_path.exists():
            glossary_text = glossary_path.read_text()
            entry_count = sum(
                1 for line in glossary_text.splitlines()
                if re.match(r"\|\s+\d+\s+\|", line.strip())
            )
            print(f"zh-TW glossary entries: {entry_count}")
        if profiles_path.exists():
            profiles_text = profiles_path.read_text()
            profile_ids = set(re.findall(r"id:\s+(zh-tw-[\w-]+)", profiles_text))
            profile_headers = set(re.findall(r"^##\s+\d+\.\s+`(zh-tw-[\w-]+)`", profiles_text, flags=re.MULTILINE))
            all_profiles = profile_ids | profile_headers
            print(f"zh-TW style profiles: {len(all_profiles)}")
        if loc_cases_path.exists():
            loc_text = loc_cases_path.read_text()
            loc_count = len(re.findall(r"^##\s+\d+\.\s+", loc_text, flags=re.MULTILINE))
            print(f"zh-TW localization cases: {loc_count}")
        if wf_cases_path.exists():
            wf_text = wf_cases_path.read_text()
            wf_count = len(re.findall(r"^##\s+\d+\.\s+", wf_text, flags=re.MULTILINE))
            print(f"zh-TW output-quality cases: {wf_count}")
        # Locale architecture presence.
        locales_dir = ROOT / "shared" / "locales"
        if locales_dir.exists():
            print(f"shared/locales/ files: {len(list(locales_dir.glob('*.md')))}")


if __name__ == "__main__":
    main()
