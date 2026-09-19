# Realistic Human And Physical Evidence Workflow

Use this workflow when real or realistically depicted people, physical objects, materials, product interfaces, institutional artifacts, or environments can make an investor claim more concrete than a schematic. This is the default visual route when concrete evidence can carry the takeaway honestly.

## Mandatory Evidence Priority

Use the strongest available level:

1. approved real asset;
2. cleared documentary capture;
3. anonymous AI-generated realistic illustration;
4. diagram or abstraction with recorded necessity.

Do not skip to a diagram for convenience. Do not add decorative people or objects that are unrelated to the slide's proof.

## Mandatory Image Backend

Prefer GPT Image 2.5 (`gpt-image-2.5`) for generated or edited raster assets. Verify the exact supported identifier and availability through the active provider before invoking it. If unavailable, use the authorized GPT Image 2 (`gpt-image-2`) fallback without asking again. Follow the Image Model Generation Gate in SKILL.md.

No silent fallback is permitted: disclose the fallback and record the actual selected model and reason in the prompt, plan and asset ledger. If neither model can be confirmed or invoked, stop only image generation and preserve completed work. Model names in prompts alone do not prove which backend was used.

## Intake For Scoped Slide Work

Before proposing visuals, identify the slide's investor takeaway, exact approved copy, aspect ratio, source slide, visual anchor, brand assets, relevant claim-ledger entries, and neighboring-slide handoff. Ask only for inputs that cannot be discovered from the workspace. Do not expand a scoped slide request into a full-deck rebuild.

## Choose The Evidence Type

Select the smallest real-world visual that proves the takeaway:

- **Human workflow:** Show the buyer, operator, user, or decision-maker performing the relevant work.
- **Physical transformation:** Show inputs, materials, evidence, or operational artifacts changing state.
- **Product in context:** Show the real interface or a restrained product view inside a credible workflow.
- **Environmental journey:** Use architecture and spatial progression when expansion across an organization matters.
- **Diagram:** Retain a diagram when causality, topology, comparison, or quantitative structure is the argument.

Do not replace a precise chart with decorative photography. Combine photography with restrained labels, lines, or metrics when both proof types are needed.

For physical-object scenes, name the exact object and state change: a marked document becoming a reviewed version, an evidence packet being assembled, a device being inspected, a production item changing state, or a decision artifact moving from draft to approval. Generic laptops, handshakes, and meeting tables are not evidence by themselves.

## Avoid Generic AI Shorthand

Reject circuitry, glowing brains, holograms, humanoid robots, floating dashboards, abstract neural networks, portal imagery, and anonymous blue-light control rooms unless the product literally contains them and the image is evidentiary.

Prefer believable work: documents, meetings, classrooms, laboratories, factories, stores, devices, evidence packets, whiteboards, or customer environments appropriate to the business.

## Explore Materially Different Directions

When the user requests options or the visual direction is uncertain, propose three written approaches that differ in evidence, not color:

1. a human-workflow direction;
2. a physical-transformation or product direction;
3. an environmental or narrative direction.

Wait for the user to select a written direction before generation unless the user explicitly asks to see generated previews. If previews are requested, save one prompt and output per direction, run independent QA on every preview, then run a comparative review scoring takeaway clarity, realism, human credibility, brand continuity, and presentation-distance readability. Record the selected option in a manifest and create a stable selected filename.

## Prompt For Realism

Specify:

- credible roles, age ranges, clothing, posture, and professional behavior;
- natural skin texture, hands, expressions, and eye lines;
- real materials, lighting, architecture, and device proportions;
- camera framing and scene hierarchy appropriate to the slide;
- how photography and overlays divide the composition;
- exact approved visible copy and prohibited additions.

Do not request a named real person without a supplied reference image. Anonymous synthetic role depictions are permitted when they represent a generic workflow, are not labeled as actual employees or customers, and do not imply a real endorsement. Do not invent founder, employee, customer, advisor, or institutional identities. For named team slides, use supplied portraits or identity-safe nonportrait treatments.

## Control Object Text And Branding

Generated photographs often introduce accidental claims. Require:

- intentionally unreadable line blocks on documents and screens unless the text is approved copy;
- plain unbranded devices, clothing, mugs, binders, books, and signage;
- no third-party logos, fake university marks, malformed captions, legal language, or invented citations;
- neutral charts and document blocks that communicate materiality without readable content.

If QA finds object text or branding, make a surgical edit that preserves the scene and removes only the defect. Re-run independent QA because image edits can remove logos, alter approved copy, or introduce new artifacts.

## Mandatory Generated-Scene Disclosure

Every photorealistic generated person, workplace, physical workflow, or environment must be disclosed visibly on the slide. Use concise audience-facing language such as:

`Anonymous AI-generated workflow illustration; not customer, employee, or documentary photography.`

Adapt singular/plural grammar and the relevant identity categories, but retain both ideas: the scene is AI-generated and it is not documentary evidence or an endorsement. Prompt metadata or speaker notes alone do not satisfy this requirement.

## Preserve Investor Hierarchy

Photography must still prove one conclusion in three seconds:

- keep the dominant subject or metric visually dominant;
- use scale, lighting, depth, framing, and eye direction before adding boxes;
- use restrained arrows only when direction or expansion matters;
- keep secondary scenes smaller and visually subordinate;
- preserve presentation-distance readability and safe margins.

## Use The Selected Anchor

After selection:

1. copy the passing image to a stable selected filename;
2. update the output manifest with the date and selected direction;
3. describe the transferable visual rules, not project-specific content;
4. use the selected slide plus the most recent passing slide as references for later generation.

## Photographic QA Gate

Require `REVISE` for:

- malformed faces, hands, body geometry, or implausible interactions;
- invented identities, logos, institutions, or claims;
- readable unapproved text on screens, documents, books, binders, clothing, or signage;
- stock-photo staging that contradicts the claimed workflow;
- generic AI motifs dominating the composition;
- photography that weakens the data hierarchy or slide takeaway;
- a slide that uses generic abstraction when a realistic person, physical object, product-in-context view, artifact, or environment could prove the takeaway more directly and no diagram necessity is recorded;
- a photorealistic generated scene without visible AI-generated and non-documentary/non-endorsement disclosure;
- a cleanup edit that removes approved copy or brand elements.

Allow `PASS` with low-severity notes for small background softness that does not affect credibility, hierarchy, or presentation use.
