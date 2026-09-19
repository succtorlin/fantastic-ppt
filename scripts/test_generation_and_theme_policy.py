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
        "GPT Image 2 Generation Gate",
        "model: gpt-image-2",
        "Do not silently substitute another image model",
        "Theme Choice Gate",
        "three materially distinct theme options",
        '"image_generation"',
        '"theme_options"',
    ],
)
require(
    ROOT / "references" / "audience-themes.md",
    [
        "Mandatory Theme Choice Gate",
        "Offer exactly three recommended choices",
        "Autonomous selection",
        "theme-options",
    ],
)
require(
    ROOT / "references" / "photographic-slide-workflow.md",
    [
        "GPT Image 2 is mandatory",
        "gpt-image-2",
        "No silent fallback",
    ],
)

print("Generation and theme policy: PASS")
