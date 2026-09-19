# fantastic-ppt

Evidence-first GPT Image 2 presentation skill with selectable themes, reusable Style Locks, editable PowerPoint composition, and independent visual QA.

## Highlights

- Enforces GPT Image 2 for generated and edited raster assets.
- Offers three audience-fit visual themes before full-deck generation.
- Converts selected or extracted visual direction into a reusable Style Lock.
- Keeps claim-bearing text, metrics, charts, citations, and logos editable.
- Prioritizes realistic human, physical, product, and institutional evidence.
- Uses thumbnail rhythm boards, sequential generation, and independent slide QA.
- Supports scoped slide repair, version safety, and reproducible delivery packages.

## Install

```bash
git clone https://github.com/succtorlin/fantastic-ppt.git \
  ~/.codex/skills/fantastic-ppt
```

Then invoke the skill as `$fantastic-ppt` when creating, critiquing, repairing, or rebuilding a presentation.

## Validate

```bash
python3 scripts/test_generation_and_theme_policy.py
python3 scripts/test_real_world_evidence_policy.py
python3 scripts/test_style_library_and_revision_policy.py
python3 scripts/test_theme_profiles.py
```
