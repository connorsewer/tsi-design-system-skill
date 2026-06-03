# Logo And Asset Use

Use this reference before placing any official assets from `assets/official/` or using source uploads.

## Official Assets

Use assets from `assets/official/`:

- Parent logos: `logo-primary-on-white.png`, `logo-primary-white.png`, `logo-primary-on-brightblue.png`, `logo-primary-black.png`.
- Symbols: `symbol-rgb.png`, `symbol-white.png`, `symbol-black.png`.
- Vertical lockups: `logo-vertical-on-white.png`, `logo-vertical-white.png`, `logo-vertical-black.png`.
- Sub-brand lockups: `sub-arm-*`, `sub-loanservicing-*`, `sub-cxbpo-*`, `sub-healthcare-*`.
- Sub-brand icons: `icon-arm.png`, `icon-loanservicing.png`, `icon-cxbpo.png`, `icon-healthcare.png`.
- People illustrations: `people-01.png` through `people-10.png`.
- Portraits: `portrait-1.png`, `portrait-2.png`.
- Social references: `social-linkedin-banner.png`, `social-facebook-banner.png`.

## Uploads

Use `uploads/TSI_BrandIdentityGuide_FINAL_022123.pdf` for original brand provenance and `uploads/brand_guide_text.txt` for searchable text. Use `uploads/TSI_PPT_Widescreen_Poppins.pptx` as the PowerPoint starting point for `.pptx` decks.

## Logo Integrity (Absolute Rule)

Every official logo, symbol, sub-brand lockup, and brand mark keeps its **true aspect ratio at all times**. It is **never stretched, squashed, cropped, skewed, rotated, or otherwise distorted** — on any surface, at any size, in any deliverable, no matter what. This rule does not bend for layout convenience.

**Safe sizing (do this):**

- Constrain ONE dimension, let the other compute: `height: 32px; width: auto;` (or set width, height auto). This guarantees the ratio.
- If a mark must fit inside a fixed box, use `object-fit: contain` and accept the letterboxing. The mark stays whole.
- Give the mark a `min-height` floor for legibility (sub-brand lockups ~ a 32px floor); scale down only proportionally.
- Preserve clear space. Do not crowd the mark with text, UI chrome, or borders.

**Distortion (never do this):**

- `width: 100%` + `height: 100%` on a mark, or any pairing of two fixed dimensions that does not match the asset's native ratio.
- `object-fit: cover`, `object-fit: fill`, or `background-size: 100% 100% / cover` on a logo.
- Non-uniform transforms: `transform: scale(1.4, 0.8)`, single-axis `scaleX()/scaleY()`, or `skew`.
- Cropping the mark with a tight container + `overflow: hidden`, masking, blur, glow, recolor, or drop shadows.

**Enforce it.** Before delivering any HTML, run `python3 scripts/check_logo_integrity.py <file.html>`. It flags fills, covers, non-uniform scales, dual-pinned dimensions, and logo-selector `object-fit` distortions. Fix every FAIL before shipping.

## Logo Placement

- Light backgrounds: use `logo-primary-on-white.png` or RGB sub-brand assets.
- Dark blue backgrounds: use `logo-primary-white.png` or white sub-brand assets.
- Bright blue backgrounds: use `logo-primary-on-brightblue.png` where appropriate.
- Preserve clear space. Do not crowd the mark with UI chrome, text, or borders.

Never:

- Recreate or trace the logo.
- Ask an image model to generate the logo.
- Distort, recolor, blur, glow, rotate, crop, mask, or add shadows to the logo (see Logo Integrity above).
- Place an on-white logo on a dark background or a white logo on a light background.

## People And Portraits

Use official people illustrations when the surface needs an established TSI human moment, a testimonial, a service narrative, or continuity with existing brand materials.

Use portraits only for testimonial/quote framing. Do not use them as generic avatars.

For new generated portraits, use the knockout logic documented in the workspace: open negative space, sparse blue/black ink, no skin tones, no smooth gray shading. Place generated portraits as supporting assets, not as replacements for official people illustrations.

## Generated Assets And Official Assets

Generated assets can expand the system: hero atmospheres, product mechanisms, data visuals, editorial illustrations, icons, and motion layers. Keep official marks separate and place them afterward in HTML, slides, or design tools.

If an asset is missing, flag the gap and choose a close analog. Do not silently invent a new official-looking TSI symbol.

## Adding Logos To Generated Images

This is feasible and low-bloat when done as deterministic compositing. It is risky when done by asking an image model to "add the logo" because the model may distort, redraw, blur, or hallucinate the mark.

Use this workflow:

1. Generate the background/accent image without any logo.
2. Inspect the composition for safe placement zones and contrast.
3. Recommend placements to the user, usually top-left, top-right, bottom-left, or bottom-right.
4. Ask the user to approve logo addition and placement.
5. Composite an official transparent logo PNG over the image with `scripts/overlay_tsi_logo.py`.
6. Save the branded derivative separately from the raw generated image.

Placement recommendations:

- Light or warm background: use `assets/official/logo-primary-on-white.png` or `assets/official/symbol-rgb.png`.
- Dark blue background: use `assets/official/logo-primary-white.png` or `assets/official/symbol-white.png`.
- Bright blue field: use `assets/official/logo-primary-on-brightblue.png` if the full lockup is needed.
- Busy or midtone background: add a subtle white or dark-blue plaque behind the logo only if needed for contrast. Keep plaque radius small and opacity restrained.

Example:

```bash
python3 scripts/overlay_tsi_logo.py \
  --input assets/generated-v2/previews/tsi-v2-10-motion-ready-layered-bg-preview.webp \
  --logo assets/official/logo-primary-on-white.png \
  --output outputs/branded/tsi-v2-10-motion-ready-layered-bg-logo.png \
  --position top-left \
  --logo-width-percent 16 \
  --margin-percent 4
```

Never overwrite the generated original.
