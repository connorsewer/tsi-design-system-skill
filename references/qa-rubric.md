# QA Rubric

Run this before delivering TSI 2.0 work.

**First, run the hard pre-flight gate in `references/anti-slop-engine.md`.** It blocks delivery on the structural slop failures (house template, hero-metric grid, eyebrow-everywhere, rainbow rails, contrast, CTA legibility). This rubric is the brand/compliance/asset layer on top of it. Do not ship with a known fail in either.

## Brand

- Official logo variant matches the background.
- Logo aspect ratio is locked and clear space preserved — never stretched, squashed, cropped, or skewed (absolute). `scripts/check_logo_integrity.py <file.html>` returns zero FAILs.
- TSI blue and Poppins are visible identity anchors.
- Warm neutrals or gradients support the brand rather than replacing it.
- Current tagline is used only where a tagline belongs.

## Taste

- A Design Read was stated and the output matches it.
- The layout could NOT be guessed from "TSI + category" alone (first-order reflex check).
- Zero items from the `anti-slop-engine.md` match-and-refuse list are present (no house template, hero-metric grid, eyebrow-on-every-section, 01/02/03 scaffolding, rainbow rails, gradient text, default glass, identical card grids).
- One accent logic, one radius scale, one type system across the whole artifact.
- The layout has a clear message, mechanism, or proof; every section is earned.
- Gradients are subtle and brand-derived. Depth is refined, not puffy or consumer.
- Dark mode is used intentionally, not by default; nor is light-premium applied as the same repeating template.

## Compliance And Data

- No fake client, account, patient, borrower, payment, or legal data.
- No shame, panic, threat, legal intimidation, or distressed consumer imagery.
- Claims are supportable or clearly illustrative.
- Synthetic data is plausible but not misleading.
- Product/COI/legal review caveats are flagged when needed.

## Accessibility And Motion

- Text contrast is adequate.
- HTML examples include reduced-motion behavior.
- Motion communicates hierarchy or state.
- Interactive elements have visible focus states.
- Images have useful alt text or empty decorative alt text.

## Asset Integrity

- Official assets are not distorted, recolored, or regenerated.
- Generated images include metadata sidecars.
- In-repo HTML examples use relative package asset paths; **shareable deliverables embed assets** as data URIs (`scripts/inline_assets.py`) so they render standalone with zero `../assets/...` paths.
- The package includes the PowerPoint template and Brand Identity Guide PDF.

## Delivery Note

Report:

- Files created or updated.
- Validation run and results.
- Known caveats.
- Any substitutions.
- Any follow-up review needed.
