# TSI Design System 2.0 Agent Instructions

Use these instructions for any work inside this package or for TSI-branded output that uses this package.

## Source Priority

1. `DESIGN.md` for normative token values and design rationale.
2. `SKILL.md` for agent workflow and reference routing.
3. `assets/official/` and `uploads/` for official source materials.
4. `references/*.md` for focused implementation guidance.
5. `examples/` and `assets/generated-v2/` as directional examples, not binding law.

## Hard Rails

- Preserve official logo artwork. Do not redraw, recolor, glow, blur, crop, or generate TSI logos.
- **Logo aspect ratio is locked, always, no matter what.** Never stretch, squash, crop, or skew a brand mark. Set one dimension with the other `auto`, or `object-fit: contain`; never `cover`/`fill`/`width:100%`+`height:100%` or non-uniform `scale()`. Audit with `python3 scripts/check_logo_integrity.py <file.html>` (zero FAILs required).
- Do not generate fake client, account, patient, borrower, payment, legal, or collection records.
- Keep TSI blue and Poppins as identity anchors even when using warm neutrals, gradients, dark panels, or generated imagery.
- Use synthetic illustrative data only.
- Avoid shame, panic, threat, legal intimidation, distressed patients, exploitative consumer imagery, or scary collections tropes.

## HTML Deliverables

- Put project CSS inline inside the HTML file.
- Inline small JS when needed for motion or interaction.
- For anything the user will share, embed local assets as data URIs with `scripts/inline_assets.py` so the file renders standalone. Relative `../assets/...` paths are only for the in-repo `examples/`.
- Google Fonts links are allowed with strong local fallbacks.
- Include `prefers-reduced-motion` handling for animated examples.
- Audit logo integrity with `scripts/check_logo_integrity.py` before delivery (zero FAILs).

## Model And Evaluation Policy

Use the strongest available model for taste-sensitive review, generated-asset prompting, and formal evals. Keep prompts and docs provider agnostic; do not hard-code a specific model family.

## Delivery Notes

Flag substitutions, assumptions, external dependencies, unverified claims, and any content that should receive legal/product/COI review.
