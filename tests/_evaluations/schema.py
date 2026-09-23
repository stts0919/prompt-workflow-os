"""Result schema for AI evaluation runs.

Every recorded result is one line of JSON. The schema is intentionally small
so that human operators using the manual protocol can copy-paste a record
without formatting headaches.

Field semantics:

- run_id:       Identifier for the batch run (e.g. "2026-Q3/gpt-6-sol").
- case_id:      Test case identifier — section heading text from the test file.
- case_path:    Relative path to the test case file under tests/.
- case_kind:    "language" | "workflow" | "router".
- model_id:     The model under test. Free-form but should match the canonical
                IDs in shared/MODELS_OF_RECORD.md (e.g. "gpt-6-sol",
                "claude-opus-5", "gemini-3.8-flash").
- model_version: Optional vendor version string (e.g. "claude-opus-5-20260724"
                or "gpt-6-sol-2026-09"). Keep this as the vendor-supplied
                snapshot string; do not invent your own.
- timestamp:    ISO-8601 UTC timestamp at time of recording.
- prompt:       The full prompt sent to the model.
- response:     The full model output. If the manual operator protocol is used,
                this is a verbatim copy-paste from the chat UI.
- locale_actual: The locale the model chose or appeared to use.
- profile_actual: The style profile the model chose or appeared to use.
- editing_intensity_actual: The editing intensity the model chose or appeared to use.
- protected_content_preserved: bool — were the protected spans preserved verbatim?
- failure_conditions_triggered: list[str] — which failure conditions from the
                case were triggered, if any.
- rubric:       per-dimension 1-5 score (see rubric.md).
- notes:        Free-form operator notes.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class RubricScore:
    locale_correctness: int = 0
    style_profile_adherence: int = 0
    protected_content_preservation: int = 0
    failure_condition_avoidance: int = 0
    output_language_correctness: int = 0

    def average(self) -> float:
        scores = [
            self.locale_correctness,
            self.style_profile_adherence,
            self.protected_content_preservation,
            self.failure_condition_avoidance,
            self.output_language_correctness,
        ]
        valid = [s for s in scores if 1 <= s <= 5]
        if not valid:
            return 0.0
        return round(sum(valid) / len(valid), 2)


@dataclass
class EvalResult:
    run_id: str
    case_id: str
    case_path: str
    case_kind: str
    model_id: str
    prompt: str
    response: str

    model_version: str = ""
    timestamp: str = ""
    locale_actual: str = ""
    profile_actual: str = ""
    editing_intensity_actual: str = ""
    protected_content_preserved: bool = True
    failure_conditions_triggered: list[str] = field(default_factory=list)
    rubric: RubricScore = field(default_factory=RubricScore)
    notes: str = ""

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["rubric_average"] = self.rubric.average()
        return d
