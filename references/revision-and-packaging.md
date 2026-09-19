# Revision And Packaging

## Scoped Revision

Translate each comment into a target slide, affected elements, required preserved elements, and expected output. Modify only that scope unless the story or shared data source makes adjacent updates necessary. Preserve untouched slides byte-for-byte when the tooling permits and visually unchanged otherwise.

For generated assets, retrieve the saved prompt, Style Lock, references, and model provenance. Edit or regenerate only the affected asset with GPT Image 2.5 (GPT Image 2 fallback), then repeat independent QA.

## Revision Log

Append material changes to `revision-log.md`:

```markdown
## <version> - <date>
- Request:
- Slides/assets changed:
- Preserved constraints:
- Prompt/model provenance:
- Claim-ledger impact:
- Independent QA verdict:
- PPTX rebuilt and rendered:
```

Do not add a visible date to slides merely because the revision log is dated.

## Version Safety

- Keep the latest approved deck intact while developing a revision.
- Store material alternatives or superseded generated images under `versions/<version>/`.
- Use stable selected filenames only after QA passes.
- Never overwrite user-supplied source decks.
- Do not revert unrelated user changes.

## Delivery Package

For substantial decks, keep these reproducibility artifacts together:

```text
<deck>.pptx
presentation-plan.json
critique.md
claim-ledger.md
asset-ledger.md
style-used.md
revision-log.md
prompts/
slides/
qa/
versions/
thumbnail-board.png   # when used
```

Add speaker notes, PDF, archive, or source exports only when requested. Do not flatten editable claim-bearing text, charts, citations, or logos into slide images for packaging convenience.

## Final Reconciliation

After revision, render the PPTX and confirm slide count, order, changed-page fidelity, unchanged-page stability, Style Lock consistency, generated-image disclosure, model provenance, and QA verdicts. Update the delivery package only after these checks pass.
