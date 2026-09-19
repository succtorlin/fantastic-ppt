#!/usr/bin/env python3
import json
import re
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
THEMES_PATH = SKILL_ROOT / "assets" / "audience-themes.json"
HEX_COLOR = re.compile(r"^#[0-9A-F]{6}$")

REQUIRED_PROFILES = {
    "tech-investors",
    "educators",
    "university-leadership",
}

REQUIRED_TOKENS = {
    "canvas",
    "surface_dark",
    "text_primary",
    "text_inverse",
    "accent_primary",
    "accent_secondary",
    "evidence_positive",
    "risk",
    "grid",
}


def luminance(color):
    channels = [int(color[index:index + 2], 16) / 255 for index in (1, 3, 5)]
    linear = [
        value / 12.92 if value <= 0.04045
        else ((value + 0.055) / 1.055) ** 2.4
        for value in channels
    ]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast_ratio(first, second):
    lighter, darker = sorted((luminance(first), luminance(second)), reverse=True)
    return (lighter + 0.05) / (darker + 0.05)


class ThemeProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with THEMES_PATH.open(encoding="utf-8") as handle:
            cls.data = json.load(handle)

    def test_required_profiles_and_custom_mode_exist(self):
        profiles = {profile["id"] for profile in self.data["profiles"]}
        self.assertTrue(REQUIRED_PROFILES.issubset(profiles))
        self.assertEqual(self.data["custom_mode"]["id"], "brand-custom")

    def test_theme_choice_gate_is_machine_readable(self):
        policy = self.data["selection_policy"]
        self.assertEqual(policy["options_per_decision"], 3)
        self.assertTrue(policy["recommend_one"])
        self.assertTrue(policy["wait_for_user_unless_autonomous"])
        self.assertTrue(policy["constant_anchor_for_previews"])

    def test_profiles_have_required_semantic_tokens(self):
        for profile in self.data["profiles"]:
            with self.subTest(profile=profile["id"]):
                self.assertTrue(REQUIRED_TOKENS.issubset(profile["tokens"]))
                self.assertGreaterEqual(len(profile["chart_sequence"]), 4)
                self.assertEqual(len(profile["chart_sequence"]), len(set(profile["chart_sequence"])))

    def test_colors_are_uppercase_six_digit_hex(self):
        for profile in self.data["profiles"]:
            colors = list(profile["tokens"].values()) + profile["chart_sequence"]
            with self.subTest(profile=profile["id"]):
                self.assertTrue(all(HEX_COLOR.match(color) for color in colors))

    def test_primary_text_contrast_meets_wcag_aa(self):
        for profile in self.data["profiles"]:
            tokens = profile["tokens"]
            with self.subTest(profile=profile["id"]):
                self.assertGreaterEqual(
                    contrast_ratio(tokens["text_primary"], tokens["canvas"]),
                    4.5,
                )
                self.assertGreaterEqual(
                    contrast_ratio(tokens["text_inverse"], tokens["surface_dark"]),
                    4.5,
                )


if __name__ == "__main__":
    unittest.main()
