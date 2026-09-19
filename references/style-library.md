# Reusable Style System

Use this reference to extract, save, select, and enforce reusable deck styles while preserving editable PowerPoint structure.

## Style Extraction

Analyze approved screenshots, decks, brand guides, or webpages for transferable rules rather than copying a single composition. Record:

- audience, purpose, and emotional register;
- typography roles and relative scale;
- grid, margins, alignment, and whitespace rhythm;
- component geometry, line weight, corner treatment, and image cropping;
- semantic colors, approximate color ratios, and chart behavior;
- photography grade, real-world subjects, and visual-evidence preference;
- header, footer, source-note, logo, and page-number behavior;
- density limits and prohibited visual motifs.

Do not import third-party logos, protected identities, distinctive illustrations, or copyrighted page compositions as reusable assets. A style profile describes a system; it is not a template copy.

## Style Lock Contract

Every selected or extracted style must resolve into `style-used.md` with:

```markdown
# <Style Name>

## Purpose
## Typography System
## Layout Grid And Spacing
## Component Grammar
## Semantic Colors And Ratios
## Photography And Evidence
## Data And Diagram Behavior
## Header, Footer, Sources, And Logos
## Density Limits
## GPT Image 2.5 (GPT Image 2 fallback) Prompt Prefix
## Negative Constraints
## QA Checks
```

Copy the resolved rules into `presentation-plan.json`. Every slide prompt must reference the same lock. Native PowerPoint text, charts, and approved brand assets remain editable and take precedence over generated approximations.

## Style Isolation

After selection, use one primary Style Lock. Ignore visual DNA from unrelated prior tasks, rejected previews, and incidental reference images. A hybrid is allowed only when the user approves the named source styles and the merged rules are rewritten as one coherent lock.

Reject drift in component radius, dividers, shadows, type hierarchy, color meaning, photographic grade, or footer placement. Layout variety is encouraged; system inconsistency is not.

## Thumbnail Rhythm Board

Create a GPT Image 2.5 (GPT Image 2 fallback) thumbnail rhythm board for full decks of six or more slides, extracted styles, or visually consequential redesigns.

- Use the final aspect ratio for every tile.
- Include the cover, dense evidence pages, emotional or photographic moments, transitions, and closing slide.
- Show composition, density, color rhythm, and visual anchors; use only tiny slide numbers or abstract labels.
- Do not rely on the board for accurate claims, citations, logos, or final text.
- Compare the board with the outline and Style Lock before full-size generation.
- Reference the approved board alongside the most recent passing slide to reduce drift.

## Saving A Style

Save broadly reusable styles under `styles/<kebab-name>.md`. Include aliases and intended audiences. Do not overwrite workflow instructions to change a style. Update the profile instead.

For a one-off branded deck, keep `style-used.md` in the output folder without adding it to the shared library.

## Editable PowerPoint Boundary

Generated imagery may establish atmosphere, physical evidence, or a visual anchor. Keep claim-bearing text, metrics, charts, citations, accessibility tags, logos, and critical diagrams native whenever practical. The reusable style system complements editable PowerPoint; it does not turn the PPTX into an image-only container.
