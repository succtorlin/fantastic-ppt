#!/usr/bin/env python3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(path: Path, phrases: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    missing = [phrase for phrase in phrases if phrase not in text]
    if missing:
        raise SystemExit(f"{path.relative_to(ROOT)} missing: {missing}")


require(
    ROOT / "SKILL.md",
    [
        "Real-World Evidence First Gate",
        '"visual_evidence"',
        '"diagram_necessity"',
        "Anonymous AI-generated workflow illustration",
    ],
)
require(
    ROOT / "references" / "photographic-slide-workflow.md",
    [
        "Mandatory Evidence Priority",
        "Mandatory Generated-Scene Disclosure",
        "not documentary evidence or an endorsement",
    ],
)
require(
    ROOT / "references" / "qa-rubric.md",
    [
        "Real-World Evidence Integrity",
        "missing generated-scene disclosure",
        "unjustified abstraction",
    ],
)
require(
    ROOT / "references" / "slide-archetypes.md",
    [
        "Record `visual_evidence` for every slide",
        "record that necessity explicitly",
    ],
)

print("Real-world evidence policy: PASS")
