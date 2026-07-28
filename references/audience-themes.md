# Audience Theme Selection

Use these rules when the user wants color choices, the audience changes, the current palette is weak, or a new deck lacks an approved visual system. Load the machine-readable profiles from `../assets/audience-themes.json`.

## Mandatory Theme Choice Gate

For every new deck or full-deck redesign, Offer exactly three recommended choices before full-deck generation. Each choice must state its audience purpose, semantic palette, typography direction, photography grade, and rationale. Mark one as recommended.

Use the same representative slide for visual comparison when previews are requested or the choice is consequential. Save previews under `slides/theme-options/<theme-id>.png`; the stable directory name is `theme-options`.

- **User selection:** Wait for the user to choose when they retain visual approval.
- **Autonomous selection:** When the user delegates design decisions or requests autonomous execution, choose the recommendation, record why it fits the audience, mark it `agent-selected`, and continue without asking for approval.
- **Scoped slide repair:** Preserve the deck's selected theme unless the repair request explicitly concerns visual style or palette.

## Selection Order

1. Inspect supplied brand colors and existing deck conventions.
2. Identify the primary decision-making audience and presentation setting.
3. Preserve supplied brand colors as locked tokens.
4. Build exactly three relevant options from the curated profiles and Existing Brand / Custom, then recommend one.
5. Record the user's choice before generating the full deck.

Do not infer a final selection merely because an audience is named. Mark it `recommended` until the user confirms. If the user explicitly delegates the decision, mark it `agent-selected`.

## Available Profiles

- **Tech Investors:** High-contrast, analytical, product-forward.
- **Educators:** Human-centered, accessible, approachable.
- **University Leadership:** Institutional, composed, strategic.
- **Existing Brand / Custom:** Derive supporting colors around supplied locked brand tokens.

Treat audience profiles as starting systems, not stereotypes. Recommend based on the decision context. A university innovation pitch may appropriately use Tech Investors; an education product investor meeting may appropriately use Educators.

## Preview Workflow

Start with three labeled palette swatches and a short rationale. When the choice is consequential, uncertain, or explicitly visual:

1. choose one representative slide containing headline, photography or product evidence, and a small chart or metric;
2. keep its content, composition, typography, and imagery constant;
3. render the same slide in three audience profiles;
4. label previews outside the slide image, never by adding unapproved slide copy;
5. compare them at full size and thumbnail size;
6. wait for selection before generating later slides.

Do not compare different layouts when testing color. That confounds theme and composition.

## Semantic Tokens

Apply colors by role:

| Token | Role |
|---|---|
| `canvas` | Primary light background |
| `surface_dark` | Dark bands, image overlays, and inverse sections |
| `text_primary` | Body and headline text on `canvas` |
| `text_inverse` | Text on `surface_dark` |
| `accent_primary` | Dominant emphasis and selected path |
| `accent_secondary` | Secondary emphasis and expansion |
| `evidence_positive` | Verified progress and positive evidence |
| `risk` | Material uncertainty, warning, or constraint |
| `grid` | Rules, axes, separators, and neutral structure |

Never change a token's meaning between slides. Never rely on color alone: use labels, line styles, shapes, or direct annotations.

## Brand Precedence

When a brand guide or brand color exists:

- lock the supplied value exactly;
- assign it a semantic role;
- adapt supporting tokens instead of replacing the brand;
- preserve logo clear space and approved logo variants;
- flag a contrast conflict rather than silently changing the locked color;
- use a compliant text or surface pairing when the locked color cannot carry text accessibly.

Do not treat a theme profile as permission to recolor a protected logo.

## Persist The Selection

Store this shape in `presentation-plan.json`:

```json
{
  "audience": {
    "primary": "university leadership",
    "setting": "executive investment review"
  },
  "visual_system": {
    "theme": {
      "id": "university-leadership",
      "status": "user-selected",
      "selected_at": "YYYY-MM-DD",
      "source": "fantastic-ppt/assets/audience-themes.json",
      "locked_brand_tokens": {
        "brand_primary": "#A67C00"
      },
      "tokens": {
        "canvas": "#F7F5F0",
        "surface_dark": "#172235",
        "text_primary": "#101820",
        "text_inverse": "#FFFFFF",
        "accent_primary": "#A67C00",
        "accent_secondary": "#356F7A",
        "evidence_positive": "#2F7D5B",
        "risk": "#9E3F4A",
        "grid": "#D5D8DC"
      },
      "chart_sequence": ["#A67C00", "#356F7A", "#7C455A", "#2F7D5B", "#718096"],
      "photo_grade": "Natural institutional light, restrained saturation, composed contrast",
      "anchor_slide": "slides/theme-anchor.png"
    }
  }
}
```

Copy the full selected profile into the plan so the deck remains reproducible if the skill changes later.

## Prompt Integration

Every slide prompt must name:

- selected theme ID and status;
- exact semantic tokens used on that slide;
- chart series order when applicable;
- photography grade;
- locked brand colors and logo rules;
- prohibited palette drift.

Reference the approved theme-anchor slide and most recent passing slide during sequential generation.

## Accessibility And QA

Require:

- at least 4.5:1 contrast for normal text;
- at least 3:1 for large text and meaningful non-text graphics;
- direct labels or non-color cues for charts;
- distinguishable chart series under grayscale and common color-vision deficiencies;
- consistent photography grading with natural skin tones;
- matching colors across generated images, native slide elements, PPTX, PDF, and rendered output.

Use `python3 scripts/test_theme_profiles.py` from the skill directory after editing curated theme data.
