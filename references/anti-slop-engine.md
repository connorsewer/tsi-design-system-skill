# Anti-Slop Engine

Read this before building any TSI surface. It is the enforcement layer behind the Design Read and dials in `SKILL.md`. Adapted for TSI from production anti-slop practice (taste-skill, impeccable) and reconciled with TSI's fixed brand anchors.

The premise: TSI's anchors (blue, Poppins, logos, compliance) are constraints you keep. Generic-ness comes from *structure*, and structure is fully in your control. Every rule below has a concrete fix, not just a prohibition.

## How the dials drive structure

- **VARIANCE** governs layout only — asymmetry, column ratios, where the artifact sits, whether sections share a grid. It never changes the typeface or the accent color. At VARIANCE 6 a centered hero with three equal cards is a fail; force a split, an offset, or a single dominant element.
- **MOTION** governs reveal and state. At MOTION 4, one or two intentional reveals that clarify sequence — not an entrance animation cloned onto every section (the uniform reflex is the tell).
- **DENSITY** governs how much breathes. Marketing low (airy), product/data high (packed, but still legible). Do not run a marketing hero at cockpit density or a data panel at gallery density.

## Match-and-refuse bans

If you are about to write any of these, stop and rebuild that element with the fix. These are reconciled with TSI — where TSI legitimately uses a pattern, the precise line is drawn.

1. **The house template.** light hero → glass stat card → warm band → dark CTA, in that order, again. *Fix:* let the Design Read pick the structure; at least one TSI artifact in three should open dark, editorial, or product-artifact-first.
2. **The hero-metric template.** Big number + small label + supporting stats + accent. *Fix:* if a metric matters, give it a sentence and a source caption; do not grid three meaningless figures ("3 / 12 / 1"). Real synthetic proof or none.
3. **Identical card grids.** Three (or N) equal cards, each icon + heading + text. *Fix:* vary weight — one lead item plus supporting, or `border-t`/`divide-y` rows, or a single composed panel. Cards only when elevation maps real hierarchy. Never nest cards.
4. **Eyebrow on every section.** Tiny uppercase tracked kicker above each heading. *Fix:* TSI's one tagline-eyebrow (`Revenue recovery, reimagined`) in the hero is voice; the same device on every section is AI grammar. Use at most one, in one place.
5. **Numbered section markers (`01 / 02 / 03`) as scaffolding.** *Fix:* numbers only when the section IS an ordered sequence the reader needs (a real 3-step flow). Otherwise drop them.
6. **Rainbow / multi-hue rails and progress bars.** e.g. dark→bright→green gradient. Violates TSI color logic. *Fix:* single TSI-blue fill, or blue→blue-tint. Green/orange are status-only, never decorative gradient stops.
7. **Gradient-clipped text** (`background-clip: text`). Decorative, never meaningful. *Fix:* solid color; emphasis via weight/size/italic.
8. **Glassmorphism by default.** Frosted cards everywhere. *Fix:* rare and purposeful (one floating caption over an image is fine); never the page's repeating material. Provide a solid fallback for reduced-transparency.
9. **Fake dashboards / decorative AI brains / interchangeable gradient blobs.** *Fix:* if you show product, show a real mechanism with synthetic-but-plausible state; if you show atmosphere, use the generated-imagery lanes, not a purple blob.
10. **Marketing buzzword copy.** streamline / empower / supercharge / leverage / unleash / seamless / world-class / best-in-class / next-generation / mission-critical. *Fix:* name the specific noun and the verb of what TSI literally does (recover, service, route, validate, resolve).
11. **Em dashes and AI cadence.** No `—` or `--`; no "serious statement, then punchy negation" rhythm repeated down the page. *Fix:* commas, colons, periods; specific sentences, not aphorisms.
12. **Centered everything at VARIANCE > 4.** *Fix:* split-screen, left-content/right-artifact, asymmetric whitespace, or pinned structure. Centered is allowed only for a manifesto/announcement where the line IS the design.
13. **Distorted logo (absolute, never).** A stretched, squashed, cropped, or skewed brand mark — `object-fit: cover/fill`, `width:100%`+`height:100%`, non-uniform `scale(x,y)`, or two mismatched fixed dimensions on a logo/symbol/sub-brand lockup. *Fix:* lock the ratio — set one dimension, other `auto`; or `object-fit: contain`. Run `scripts/check_logo_integrity.py`. This one never has an exception.

## Contrast and shape locks (a11y, mandatory)

- Body text ≥ 4.5:1 against its background; large/bold text ≥ 3:1; placeholders too. The recurring AI failure is muted gray on tinted near-white — push body toward `--ink-700`/`#001E41` if it is even close.
- Every CTA: text readable on its fill (no white-on-white, no borderless ghost on a busy background). Primary CTA label ≤ 3 words, one line at desktop, verb + object ("Explore the platform", "Request a review").
- One radius scale per artifact (TSI: 6–16px cards/panels, 24px only for large atmospheric surfaces, pill for status only). Mixed radii only under a documented rule applied everywhere.
- One accent logic per artifact; do not introduce a new hue in section 7.

## Design-read examples (TSI, by mode)

- **Light-premium landing, ARM, bank buyer:** left editorial hero, single right-column product artifact (a real routing/validation mechanism with synthetic state), no stat grid; VARIANCE 6 / MOTION 4 / DENSITY 4.
- **Dark-feature closing slide, Healthcare RCM, hospital CFO:** one outcome sentence over a deep-blue light-curtain plate, white logo bottom-left, single bright-blue signal; VARIANCE 6 / MOTION 5 / DENSITY 3.
- **Warm-editorial report cover, TSI parent:** serif-accented headline, wide margins, one restrained proof line, blue only on the mark and a single rule; VARIANCE 5 / MOTION 3 / DENSITY 3.
- **Product-system operating layer, DebtNext:** denser control surface, mono data details, status rows (green/orange status only), motion reveals flow state; VARIANCE 5 / MOTION 5 / DENSITY 6.

## Pre-flight gate (run before delivery)

Block delivery until all pass. If any fails, fix and re-check; do not ship with a known fail.

1. Did I state a Design Read and does the output match it?
2. Could someone guess the layout from "TSI + \<category>" alone? If yes, the structure is the first-order reflex — rework it.
3. Zero items from the match-and-refuse list present?
4. Brand anchors intact: TSI blue leads, Poppins anchor, official logo correct variant + undistorted + correct clear space?
5. One accent logic, one radius scale, one type system across the whole artifact?
6. Contrast: body ≥ 4.5:1, large ≥ 3:1, every CTA legible and ≤ 3 words on one line?
7. Motion clarifies state/sequence and has a `prefers-reduced-motion` path? No uniform entrance reflex?
8. Copy: no buzzwords, no em dashes, no aphoristic cadence, no duplicate-intent CTAs?
9. Compliance: synthetic data only, no shame/panic/threat, claims supportable or clearly illustrative, review caveats flagged?
10. The AI slop test: if a stranger saw this, would they say "AI made that" without doubt? If yes, it failed.
11. Portable if shared: a deliverable the user will send has every local asset embedded (data URIs via `scripts/inline_assets.py`), zero `../assets/...` paths remaining, and renders standalone. In-repo examples are exempt.
12. Logo integrity (absolute): every brand mark keeps its true aspect ratio — no stretch, squash, crop, or skew. `scripts/check_logo_integrity.py` returns zero FAILs. Never an exception.
