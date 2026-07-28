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
        "Reusable Style System",
        "Style Lock",
        "thumbnail rhythm board",
        "style isolation",
        "revision-log.md",
        "style-used.md",
        "references/style-library.md",
        "references/revision-and-packaging.md",
    ],
)
require(
    ROOT / "references" / "style-library.md",
    [
        "Style Extraction",
        "Style Lock Contract",
        "Thumbnail Rhythm Board",
        "Style Isolation",
        "editable PowerPoint",
    ],
)
require(
    ROOT / "references" / "revision-and-packaging.md",
    [
        "Scoped Revision",
        "Revision Log",
        "Version Safety",
        "Delivery Package",
        "Do not flatten editable claim-bearing text",
    ],
)
require(
    ROOT / "styles" / "institutional-evidence-editorial.md",
    [
        "Style Lock",
        "Component Grammar",
        "Negative Constraints",
        "GPT Image 2",
    ],
)

print("Style-library and revision policy: PASS")
