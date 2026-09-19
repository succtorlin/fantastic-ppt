---
name: fantastic-ppt
description: Use when creating, critiquing, repairing, or rebuilding investor decks, pitch decks, executive presentations, slide images, PowerPoint files, PPTX files, or visually consistent presentation narratives.
---

# Fantastic PPT

## Overview

Turn a presentation into a defensible story and a visually coherent artifact. Treat content strategy, claim verification, real-world visual evidence, slide rendering, and independent visual QA as one production system. Default to realistic people, physical objects, product-in-context, institutional artifacts, or real environments when they prove the takeaway more concretely than abstract graphics.

## Required Skills

- **REQUIRED:** Use `imagegen` with `model: gpt-image-2` for every generated or edited raster slide asset.
- **REQUIRED:** Do not silently substitute another image model. If GPT Image 2 is unavailable, preserve approved real assets and native graphics, report the blocked image step, and wait for access or explicit user authorization to change models.
- **REQUIRED:** Use `pdf` when reading or visually inspecting a PDF deck.
- **REQUIRED:** Use `presentations` when native slide editing or richer PPTX composition is needed.
- For information-dense slides, use `baoyu-infographic` to choose the layout and `svg-infographic` to sharpen the logical structure. Use `baoyu-article-illustrator` to choose the visual role, style, and palette.

If a named skill is unavailable, follow this workflow with the closest native tool and disclose the fallback.

## Output Contract

Work inside the active workspace. Default to:

```text
outputs/<deck-slug>-fantastic-ppt/
  critique.md
  claim-ledger.md
  asset-ledger.md
  style-used.md
  presentation-plan.json
  prompts/NN-slide-slug.md
  slides/NN-slide-slug.png
  thumbnail-board.png
  qa/NN-slide-slug.md
  revision-log.md
  versions/
  <deck-slug>.pptx
```

Do not assume `/mnt/user-data` exists. Use it only when the active runtime explicitly provides it.

Every slide must have one investor takeaway, exact visible copy, a saved prompt, a rendered image, and a QA verdict. Each `qa/NN-slide-slug.md` must record `reviewer`, `verdict`, and severity-ordered findings.

For a scoped request involving one or a few slides, inspect the full deck only enough to preserve narrative and visual continuity. Create artifacts only for the changed scope unless the user asks for a full rebuild. Do not compose a PPTX when the requested deliverable is only slide images or visual options.

## Workflow

### 1. Inspect Before Rewriting

Render the source deck and inspect every slide at full size and thumbnail size. Extract text and record:

- audience, objective, ask, and presentation setting
- current narrative order and missing proof
- aspect ratio, grid, palette, typography, logo treatment, and recurring motifs
- unsupported claims, stale facts, dense slides, and visual inconsistencies

Preserve unrelated slides and user edits.

### 2. Pass the Theme Choice Gate

For every new deck or full-deck redesign, read [audience-themes.md](references/audience-themes.md) and present three materially distinct theme options before generating the full deck. This is the **Theme Choice Gate**.

- Identify the primary decision-making audience and presentation setting.
- Offer exactly three recommended choices drawn from Tech Investors, Educators, University Leadership, or purpose-built variants derived from Existing Brand / Custom. Always include an Existing Brand / Custom route when supplied brand assets materially constrain the palette.
- Give each option a name, audience purpose, semantic palette, typography direction, photography grade, and one-sentence rationale. Mark one as recommended.
- Wait for selection before full-deck generation unless the user explicitly delegates visual decisions or requests autonomous execution. In autonomous mode, select the recommendation, record the reason, and continue without an approval interruption.
- Preserve supplied brand colors as locked semantic tokens.
- Render the same representative anchor slide in all three themes when previews are requested, the palette is being corrected, or the choice is consequential. Keep copy, layout, and imagery constant so only the theme changes.
- Save the selected profile, status, tokens, chart sequence, photography grade, locked brand tokens, and anchor slide in `presentation-plan.json`.
- Apply colors by semantic role; never rely on color alone.

### 3. Establish the Reusable Style System

Read [style-library.md](references/style-library.md) when the user supplies visual references, asks to reuse or save a style, requests a full-deck redesign, or the deck needs stronger cross-slide consistency.

- Start from a curated audience theme, a saved profile under `styles/`, or an extracted style from approved references.
- Convert the selection into one deck-specific **Style Lock** covering typography, grid, spacing, component grammar, color ratios, photography, data behavior, header/footer rules, density, logo handling, and negative constraints.
- Save the resolved lock to `style-used.md` and embed it in `presentation-plan.json` and every generation prompt.
- Enforce style isolation: do not blend unrelated reference images, earlier experiments, or historical deck styles unless the user explicitly requests a hybrid.
- For full decks of six or more slides, or whenever rhythm is uncertain, create a GPT Image 2 thumbnail rhythm board before full-size generation. Use it to validate pacing and composition, not claim-bearing copy.
- Save a strong new style under `styles/<style-name>.md` only when the user asks to reuse it or the pattern is broadly reusable.

### 4. Critique the Investor Story

Write `critique.md` before generating images. Test each slide for:

1. takeaway clarity
2. investor relevance
3. evidence and defensibility
4. narrative handoff to the next slide
5. visual comprehension in three seconds

Prefer a defensible category claim over a grand but fragile claim. For startup decks, usually build the sequence around problem, wedge, proof, moat, expansion, economics, and ask.

### 5. Verify Claims

Create `claim-ledger.md` for external facts, dates, legal requirements, market sizes, customer counts, performance metrics, and superlatives.

- Browse when a claim may have changed or when accuracy is high stakes.
- Prefer primary sources and record the source URL plus access date.
- Separate verified fact, company-provided metric, estimate, and interpretation.
- Qualify or remove claims that cannot be supported.
- Do not let an image model invent statistics, citations, customer logos, or regulatory language.

### 6. Map Each Slide to a Visual Argument

Read [slide-archetypes.md](references/slide-archetypes.md) and select one archetype per slide. Use diagrams only when relationships matter; use editorial composition when one statement or image should dominate.

Before choosing a schematic, run the **Real-World Evidence First Gate**:

1. Can a real person, physical workflow, product interface, institutional artifact, or real environment prove the takeaway more concretely?
2. Would a diagram clarify a relationship that photography cannot?
3. Is the proposed visual merely generic AI shorthand such as circuitry, glowing brains, holograms, abstract nodes, or futuristic dashboards?

Use this priority order unless the slide's argument requires a chart or relationship diagram:

1. approved real customer, team, product, document, or environment asset;
2. cleared documentary product capture or physical artifact;
3. anonymous generated human workflow, physical-object transformation, or product-in-context scene;
4. native diagram, chart, or abstract composition with a recorded necessity.

Do not choose option 4 merely because it is faster. A diagram is justified when causality, topology, sequence, comparison, or quantitative structure is itself the proof. If a slide has no realistic human, physical-object, product-in-context, institutional-artifact, or environmental element, record why concrete evidence would weaken or misstate the takeaway.

For human or physical slide directions, read [photographic-slide-workflow.md](references/photographic-slide-workflow.md). Generated photorealistic scenes must use anonymous roles, avoid implied endorsement, and carry visible audience-facing disclosure that they are AI-generated illustrations rather than customer, employee, or documentary photography. When the visual direction is consequential or uncertain, propose three materially different written concepts first. Wait for selection before generation unless the user explicitly asks to see generated previews. When previews are requested, generate and QA all requested previews, record the user's selection, and use the selected result as the next visual anchor.

Create `presentation-plan.json` with the visual system and one object per slide:

```json
{
  "title": "Deck title",
  "aspect_ratio": "16:9",
  "audience": {
    "primary": "<decision-making audience>",
    "setting": "<presentation setting>"
  },
  "visual_system": {
    "theme_options": [{
      "id": "<theme id>",
      "label": "<user-facing name>",
      "recommendation": "<recommended|alternative>",
      "preview": "<path or not-requested>"
    }],
    "theme": {
      "id": "<theme profile or brand-custom>",
      "status": "<recommended|user-selected|agent-selected|brand-derived>",
      "tokens": "<copy selected semantic tokens>",
      "chart_sequence": "<copy selected chart sequence>",
      "photo_grade": "<selected photography treatment>",
      "locked_brand_tokens": {},
      "anchor_slide": "<approved theme preview or anchor>"
    },
    "style_lock": {
      "source": "<curated|saved|extracted|hybrid-approved>",
      "profile": "<styles/file.md or theme id>",
      "rules_file": "style-used.md",
      "thumbnail_board": "<path or not-required>",
      "isolation": "locked"
    },
    "image_generation": {
      "provider": "OpenAI",
      "model": "gpt-image-2",
      "fallback_allowed": false,
      "asset_ledger": "asset-ledger.md"
    },
    "typography": "<deck-specific typography>",
    "layout": "<deck-specific layout grammar>",
    "brand_rules": "<deck-specific brand rules>"
  },
  "slides": [{
    "number": 1,
    "slug": "category-layer",
    "takeaway": "Defensible investor conclusion",
    "archetype": "category-bridge",
    "visual_evidence": {
      "type": "approved-real-asset|documentary-capture|generated-human-workflow|generated-physical-object|product-in-context|diagram|data-visualization",
      "real_world_subject": "Person, object, artifact, product, or environment shown",
      "source_status": "approved|generated-illustrative|gated|not-applicable",
      "diagram_necessity": "Required when no real-world element is used",
      "disclosure": "Exact visible disclosure or not-required"
    },
    "visible_text": ["Exact text only"],
    "sources": []
  }]
}
```

### 7. Save Production Prompts

Before generating any image, save the full prompt to `prompts/NN-slide-slug.md`. Include:

- exact visible text in a dedicated block
- slide takeaway and visual archetype
- composition, hierarchy, palette, typography, and safe margins
- selected theme ID, semantic tokens, chart sequence, photography grade, and locked brand colors
- visual-evidence type, real-world subject, source status, diagram necessity, and exact disclosure
- source and reference image paths
- prohibited additions: invented text, numbers, logos, citations, and watermarks
- target aspect ratio and output path
- an explicit generation line: `model: gpt-image-2`
- the complete deck `Style Lock`, thumbnail-board reference when used, and prohibited style drift

Use English prompts unless the requested slide language requires otherwise. Keep on-slide copy short enough to render reliably.

### 8. Pass the GPT Image 2 Generation Gate

GPT Image 2 is the mandatory raster generation and editing backend for this skill. Before the first generation call:

1. Confirm the available `imagegen` path uses `model: gpt-image-2`.
2. Record `provider`, `model`, prompt path, reference assets, output path, generation/edit mode, and timestamp in `asset-ledger.md`.
3. Put `model: gpt-image-2` in every saved prompt and `presentation-plan.json`.
4. Reject mixed-model visual sets unless the user explicitly authorizes a documented exception.
5. If the model cannot be confirmed or invoked, stop only the generated-image portion. Do not silently substitute another image model or claim GPT Image 2 provenance.

### 9. Generate the Rhythm Board and Slides Sequentially

For qualifying full decks, generate `thumbnail-board.png` first with GPT Image 2. It must show the planned slide rhythm, dominant visual anchors, density changes, and layout variety using tiny abstract labels or slide numbers only. It is a continuity reference, not a source of claims or a final slide. Review it against the outline, selected theme, and Style Lock before generating full-size slides.

Generate slides one at a time.

- Slide 1 establishes the full-size visual system; the thumbnail rhythm board establishes whole-deck pacing.
- Slide 2 references Slide 1.
- Each later slide references the most recent approved slide; also include the visual anchor slide when drift appears.
- Keep content structure appropriate to the archetype instead of repeating one layout.
- Copy tool-managed images into the workspace output path while preserving the originals.
- For photographic slides, neutralize unintended screen text, document text, third-party marks, and fake institutional branding. Treat cleanup edits as new generated versions that require fresh QA.
- Generate realistic people, physical objects, artifacts, and environments as standalone assets whenever native text and diagrams should remain editable. Do not flatten claim-bearing slide copy into the photograph.
- For photorealistic generated people or environments, place a concise visible disclosure on the slide, such as `Anonymous AI-generated workflow illustration; not customer, employee, or documentary photography.` Adapt singular/plural grammar without weakening the meaning.
- Keep generated people anonymous and generic. Never label them as actual founders, employees, customers, university representatives, or endorsers without supplied identity references and approval.
- When a user selects a visual option, create a stable selected filename or manifest entry and reference that artifact in later prompts.
- Treat the approved theme preview as a visual anchor. Do not silently change token meanings or recolor protected logos.
- Add logos, wordmarks, and repeated brand marks as approved native post-production assets. Do not ask GPT Image 2 to redraw them across pages.

### 10. Revise Without Collateral Damage

Read [revision-and-packaging.md](references/revision-and-packaging.md) for any repair, critique comment, or page-level regeneration.

- Change only the named slide or asset unless narrative dependencies require a broader update.
- Preserve the selected theme, Style Lock, dimensions, slide order, and all unmentioned content.
- Save material iterations under `versions/` and append the request, affected assets, model provenance, QA result, and PPTX rebuild status to `revision-log.md`.
- Re-render and independently QA every changed slide, then update the PPTX without altering untouched slides.

### 11. Pass the QA Release Gate

Before composing the PPTX, inspect the available tools for agent or subagent spawning.

1. If agent tools exist, spawn a fresh QA agent for every generated or repaired slide. Self-review does not satisfy this gate.
2. Give the reviewer the prompt, source references, visual anchor, rendered slide, relevant claim-ledger entries, and neighboring-slide context needed to judge narrative handoff. Do not give the reviewer the creator's diagnosis or desired verdict.
3. Require `PASS` or `REVISE` using [qa-rubric.md](references/qa-rubric.md).
4. Save the response to `qa/NN-slide-slug.md` beginning with `reviewer: independent-agent` and `verdict: PASS|REVISE`.
5. If agent tools do not exist, save `reviewer: self-review-fallback`, perform the rubric at full size and thumbnail size, and disclose that QA was not independent.

The reviewer must explicitly test the Real-World Evidence First Gate. Use `REVISE` when a slide defaults to generic abstraction despite a more concrete available proof, when the plan omits `visual_evidence`, when a diagram lacks recorded necessity, or when a photorealistic generated scene lacks visible AI-generated/non-endorsement disclosure.

The reviewer must also reconcile each generated asset against `asset-ledger.md`. Use `REVISE` when GPT Image 2 provenance is missing, the saved prompt omits `model: gpt-image-2`, or an undeclared model substitution appears.

For full decks, compare the final montage with the thumbnail rhythm board and Style Lock. Use `REVISE` for accidental style blending, component drift, repetitive composition, uncontrolled density, inconsistent image grading, or a full-size slide that no longer serves the planned deck rhythm.

Do not compose the final PPTX until every changed slide has a QA record with a reviewer and verdict. Regenerate material failures such as wrong text, false claims, unreadable content, broken hierarchy, inconsistent branding, or incoherent logic. Record cosmetic issues without needless image churn. Independently verify the QA findings before declaring success.

### 12. Compose, Package, and Verify the PPTX

For image-backed slides, run:

```bash
python scripts/compose_pptx.py \
  --plan-file /absolute/path/presentation-plan.json \
  --slide-images /absolute/path/slides/01.png /absolute/path/slides/02.png \
  --output-file /absolute/path/deck.pptx
```

Use native presentation tooling instead when editable text, charts, notes, accessibility tags, or complex animations are required.

Render the final PPTX back to images and verify slide count, dimensions, cropping, text fidelity, image sharpness, and visual continuity. Do not claim completion from generation logs alone.

For substantial decks, preserve the editable source, final PPTX, slide renders, prompts, plan, claim and asset ledgers, `style-used.md`, `revision-log.md`, QA records, and optional thumbnail board in the workspace output folder. Create a delivery archive only when requested. Do not flatten editable claim-bearing text merely to imitate an image-only workflow.

## Common Failures

| Failure | Correction |
|---|---|
| Start drawing before fixing the story | Write the critique and takeaway map first |
| Repeat “the same style” without a reference image | Pass the previous approved slide and visual anchor |
| Put paragraphs into image generation | Compress to headline, proof line, and visual argument |
| Treat old facts as stable | Verify current primary sources and update the claim ledger |
| Let the creator approve its own output | Use an independent QA agent and verify its verdict |
| Force every slide into cards | Match the archetype to the information relationship |
| Use circuitry or glowing interfaces as default AI imagery | Prefer a real workflow, physical artifact, product view, or environment that proves the claim |
| Use polished diagrams because they are easier than evidence | Apply the Real-World Evidence First Gate and record diagram necessity |
| Show photorealistic generated people without disclosure | State visibly that they are anonymous AI-generated illustrations, not customers, employees, or documentary photography |
| Add a generic stock-like person beside an unrelated diagram | Show a specific role performing the physical or product workflow that proves the takeaway |
| Let generated screens and documents introduce claims | Make non-approved object text intentionally unreadable and remove third-party marks |
| Invent team portraits to make a slide feel human | Use supplied portraits or neutral identity-safe treatments |
| Pick attractive hex values independently on every slide | Select one audience profile and persist semantic tokens in the plan |
| Start a full deck without a user-facing theme choice | Pass the Theme Choice Gate with three comparable options or record autonomous selection |
| Use whichever image model is convenient | Enforce the GPT Image 2 Generation Gate and record provenance in the asset ledger |
| Substitute another model when GPT Image 2 fails | Stop the generated-image step and disclose the block; never falsify provenance |
| Override brand colors to fit a preset | Lock supplied brand tokens and derive accessible supporting colors |
| Compare palettes using different layouts | Preview themes on the same representative slide |
| Encode chart meaning through color alone | Add direct labels, shapes, or line styles and test grayscale differentiation |
| Mix visual DNA from every supplied reference | Resolve one Style Lock and enforce style isolation |
| Discover deck rhythm only after all slides are generated | Create a thumbnail rhythm board for qualifying full decks |
| Rebuild the whole deck for one slide comment | Use scoped revision, version safety, and a revision log |
| Hard-code runtime paths | Resolve paths from the active workspace |
