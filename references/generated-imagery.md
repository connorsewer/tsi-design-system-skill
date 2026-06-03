# Generated Imagery

Use this reference for image-generation prompts and generated asset QA.

For atmospheric backgrounds and accent-image directions inspired by the May 2026 adventurous visual batch, read `references/adventurous-backgrounds-and-accents.md` before prompting.

The bundled `assets/generated-v2/` library is intentionally compact for upload portability: it contains WebP previews, a contact sheet, and JSON prompt metadata rather than production-resolution PNGs. Use previews for taste calibration and examples; regenerate production assets from the prompts when final resolution matters.

## Prompt Structure

Use this shape:

```text
Goal:
[What the asset should accomplish and where it will be used.]

Visual mode:
[Light premium, warm editorial, product artifact, dark feature panel, or another named mode.]

Scene / structure:
[Concrete composition, layout, mechanism, spatial arrangement, and logo-safe area.]

Subject:
[Product system, abstract workflow, portrait/human moment, atmosphere, data object, icon, or diagram.]

Style:
[TSI palette anchors, typography feel, material treatment, lighting, texture, and depth.]

Composition:
[Aspect ratio, focal point, negative space, text-safe areas, and responsive cropping intent.]

Constraints:
[No generated logos, no fake sensitive data, no stock-photo cliches, no shame/threat imagery.]
```

## Ten Directional Asset Briefs

The 2.0 mini-library should cover these briefs:

1. Light premium revenue recovery hero atmosphere.
2. Warm editorial compliance-and-care visual field.
3. Light product operating layer with rails and validation gates.
4. Borrower servicing journey map with clean light UI surfaces.
5. Healthcare RCM denial recovery assembly flow.
6. CXBPO quality-and-routing visual system.
7. Abstract customer relationship preservation scene.
8. Minimal spot icon for compliant omnichannel outreach.
9. Premium data monument with large synthetic metrics.
10. Motion-ready layered background with separate foreground/midground feel.

Treat these as taste calibration, not a restrictive house style.

## Logo Placement After Generation

Do not ask an image model to generate, redraw, or edit TSI logos into the image. Generate the visual without marks, then place the official transparent PNG in HTML, slides, design software, or with `scripts/overlay_tsi_logo.py`.

Recommended interaction:

1. Generate the image without logos and save metadata.
2. Recommend one or two logo placements based on contrast and safe area.
3. Ask the user whether to add a logo and which placement they prefer.
4. Use `scripts/overlay_tsi_logo.py` with an official logo from `assets/official/`.
5. Save a new branded derivative; keep the raw generated original unchanged.

## OpenAI Image Guidance Summary

For GPT Image 2 or similar models, be specific about intent, subject, layout, palette, constraints, and desired editability. Use reference images selectively for style or composition, but do not pass official logos when the model might reproduce them. Prefer generating image areas without final body copy when text accuracy matters; add final text later in HTML, slides, or design tools.

## Safety

Never generate:

- Official TSI, sub-brand, DebtNext, UAS, CollectX, or PULSE logos.
- Fake client names, account numbers, patient data, borrower data, payment records, or legal notices.
- Distressed consumers or patients.
- Court, threat, shame, panic, or intimidation imagery.
- Stock photography tropes, handshake cliches, robot brains, glowing AI heads, or generic SaaS blobs.

## QA

Approve generated images only when:

- The visual has one clear purpose.
- It fits at least one 2.0 visual mode.
- TSI blue remains an identity anchor.
- The output is premium and subtle enough for executive/regulatory audiences.
- It leaves room for official logo placement when needed.
- It does not overfit to the older duotone style or the recent dark 27-image batch.
- It includes metadata with prompt, source path, generation mode, date, and review status.
