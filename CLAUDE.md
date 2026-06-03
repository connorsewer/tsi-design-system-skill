# Claude Instructions For TSI Design System 2.0

When this package is present, use `$tsi-design-system` for TSI work before generic design, copywriting, slide, UI, or image-generation skills.

Read `DESIGN.md` first, then load only the reference file needed for the task. Keep `SKILL.md` concise in context and use progressive disclosure.

For HTML, write single-file deliverables with inline CSS. Do not rely on an external project stylesheet for the file's own styling.

**Portability is the default for anything the user will share.** A `.html` that references `../assets/...` only renders next to the package; emailed or uploaded on its own, the logos and images break. So when the output is a deliverable (not an in-repo example), embed every local asset as a base64 data URI so the single file renders anywhere with no asset folder. Do not hand-encode base64; run `python3 scripts/inline_assets.py <file.html>` (writes a `*.portable.html`, or use `--in-place`). Relative `../assets/...` paths are acceptable only for the bundled `examples/` that ship inside this package. Always embed the official logo and any marks/icons; embed photographic/people images too for shareable files (the script warns on large ones). Google Fonts `<link>` tags stay remote and keep working.

For decks, use `uploads/TSI_PPT_Widescreen_Poppins.pptx` as the PowerPoint starting point when creating `.pptx` deliverables. For HTML decks, borrow its brand rhythm and use official logos from `assets/official/`.

For image generation, never ask the model to create TSI logos or sensitive data. Generate supporting visual assets, then place official logos afterward.

**Logo aspect ratio is locked, always, no matter what.** Never stretch, squash, crop, or skew an official logo or brand mark. Set one dimension and let the other compute (`height: 32px; width: auto;`), or use `object-fit: contain`; never `cover`/`fill`/`width:100%`+`height:100%` or a non-uniform `scale()`. Audit before delivery with `python3 scripts/check_logo_integrity.py <file.html>` (must return zero FAILs). See `references/logo-and-assets.md`.
