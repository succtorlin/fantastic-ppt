# Slide QA Rubric

Start the saved QA record with:

```yaml
reviewer: independent-agent
verdict: PASS
```

Use `PASS` or `REVISE`, then list concrete findings ordered by severity.

## Content

- Does the slide express one investor takeaway within three seconds?
- Is every visible word spelled correctly and present in the approved copy?
- Are dates, units, claims, and labels consistent with the claim ledger?
- Is interpretation clearly separated from verified fact?

## Narrative

- Does the visual structure prove the headline?
- Does the slide advance the deck rather than repeat the previous slide?
- Does it create a clean handoff to the next slide?

## Visual Design

- Is the hierarchy obvious at thumbnail size?
- Is all text readable at presentation distance?
- Are margins, alignment, spacing, and visual balance coherent?
- Does it match the anchor slide's palette, typography, logo treatment, and finish?
- Are diagrams understandable without narration?
- When photography is used, do people, hands, materials, devices, lighting, and interactions look credible?
- Does the real-world scene prove the takeaway rather than act as generic stock decoration?
- Does the slide avoid generic AI shorthand when a concrete visual is available?

## Real-World Evidence Integrity

- Does `presentation-plan.json` contain `visual_evidence` with type, subject, source status, diagram necessity, and disclosure?
- Does the slide use the strongest honest evidence available: approved real asset, documentary capture, generated realistic scene, then diagram?
- If no realistic person, physical object, product-in-context view, institutional artifact, or environment appears, is diagram necessity specific and persuasive?
- Is every human or physical element performing the workflow or proving the transformation rather than acting as stock decoration?
- If a scene is photorealistic and generated, does visible slide copy explicitly identify it as AI-generated and not customer, employee, endorsement, or documentary photography as applicable?

## Theme Integrity

- Does the slide use the selected theme ID and semantic token meanings recorded in `presentation-plan.json`?
- Are supplied brand colors and protected logo colors preserved exactly?
- Do normal text and large text meet the required contrast targets?
- Are chart series distinguishable without color through labels, shapes, or line styles?
- Does photography match the selected grade while preserving natural skin tones?
- Does the slide match the approved theme anchor at full size and thumbnail size?
- Do rendered PPTX and PDF outputs preserve the selected colors without material drift?

## Generated Image Integrity

- Is every readable word on screens, documents, books, binders, clothing, and signage part of the approved copy?
- Are devices, clothing, props, and environments free of unintended third-party logos or invented institutional marks?
- Are team, customer, employee, and advisor identities based on supplied references rather than invented portraits?
- Did a cleanup edit preserve the approved logo, wordmark, copy, hierarchy, and scene invariants?

## Production

- Is the image the requested aspect ratio and sufficiently sharp?
- Are there clipped elements, distorted logos, artifacts, watermarks, or invented text?
- Will composition into PPTX avoid letterboxing or cropping important content?

## Verdict

Use `REVISE` for any false claim, incorrect visible text, readable unapproved object text, invented identity or logo, malformed human anatomy, illegible content, incoherent logic, material brand drift, inaccessible contrast, changed semantic color meaning, protected-brand recoloring, missing `visual_evidence` metadata, unjustified abstraction, generic stock decoration, missing generated-scene disclosure, or production defect. Use `PASS` when remaining issues are cosmetic and do not justify regeneration; list those issues as low severity.
