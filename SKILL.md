---
name: tsi-design-system
description: Create, critique, or upgrade Transworld Systems Inc. (TSI) brand work across landing pages, decks, product visuals, UI prototypes, marketing copy, generated-image prompts, atmospheric backgrounds, accent images, logo overlays, and sales collateral. Use whenever the user mentions TSI, Transworld Systems, tsico.com, ARM, Loan Servicing, CXBPO, Healthcare RCM, DebtNext, UAS, CollectX, PULSE, receivables, collections, loan servicing, revenue cycle, customer experience BPO, asks to add a TSI logo to an image, or asks for "our" TSI-branded design/copy/assets.
---

# TSI Design System 2.0

Produce premium, unmistakably-TSI work that does not collapse into generic B2B SaaS. TSI's brand anchors are **fixed** (TSI blue, Poppins, official logos, regulated-industry credibility, synthetic-data safety). Everything that makes output feel generic is a **choice you control** — layout, composition, density, rhythm, imagery, mode. Variance lives there, never in the anchors.

> The failure mode this skill exists to prevent: every TSI artifact looking like the same template (light hero → glass stat card → warm band → dark CTA). If your output could be guessed from the category alone, it has failed. Read the brief, commit to a direction, and earn every element.

## Do this in order

1. **Write the Design Read** (Section 0 below). One line, before any code or prompt. Non-negotiable — skipping it is why output goes generic.
2. **Set the three dials** (Section 1). They gate layout, motion, and density.
3. Read `DESIGN.md` for tokens (color, type, shape, spacing, motion). These are the fixed anchors.
4. Read only the reference that matches the task:
   - `references/anti-slop-engine.md` — **read before building any surface.** The banned-trope match-and-refuse list and the pre-flight gate. This is the teeth.
   - `references/brand-foundations.md` — positioning, voice, sub-brands, hard rails.
   - `references/logo-and-assets.md` — before placing any logo, person, portrait, sub-brand mark, or the PPTX.
   - `references/visual-modes.md` — light-premium, warm-editorial, product-system, dark-feature. Your variance vehicle.
   - `references/generated-imagery.md` — before writing image prompts or making assets.
   - `references/adventurous-backgrounds-and-accents.md` — atmospheric backgrounds / accent imagery.
   - `references/components-and-patterns.md` — UI and page primitives.
   - `references/motion.md` — animation vocabulary and reduced-motion rules.
   - `references/surface-contracts.md` — per-surface structure for pages, decks, product visuals, dashboards, social, prompt books.
   - `references/qa-rubric.md` — run the pre-flight before delivery.
5. Use official assets from `assets/official/`. Use `uploads/` PDF + PPTX as provenance and deck starting points.
6. HTML deliverables: single-file, inline CSS, relative asset paths, Google Fonts with fallbacks.

## 0. Design Read (before anything)

Most AI design is bad because the model jumps to a default aesthetic instead of reading the brief. Before generating, state one line:

**"Reading this as: \<surface> for \<audience>, brand family \<TSI parent / ARM / Loan Servicing / CXBPO / Healthcare RCM / DebtNext / UAS / CollectX / PULSE>, in \<visual mode> mode, leaning \<one concrete structural idea>."**

Examples:
- *"Reading this as: a sales landing page for bank revenue-cycle buyers, ARM family, light-premium mode, leaning a left-aligned editorial hero with a single product-artifact column (no stat-card grid)."*
- *"Reading this as: a closing deck slide for a hospital CFO, Healthcare RCM family, dark-feature mode, leaning one large outcome statement over a deep-blue light-curtain plate."*
- *"Reading this as: a thought-leadership report cover, TSI parent, warm-editorial mode, leaning a serif-accented headline with wide margins and one restrained proof block."*

If the brief genuinely diverges and you cannot infer, ask **exactly one** question, then proceed. If you can infer, do not ask — declare the read and build.

### Anti-default discipline
Do not reflex-reach for: the light-hero + glass-stat-card + warm-band + dark-CTA template; three equal feature cards; a tiny uppercase tracked eyebrow above every section; `01 / 02 / 03` markers on every section; a rainbow/multi-hue progress rail; gradient-clipped text; glassmorphism on everything; meaningless metrics ("3 / 12 / 1"). These are the house slop. Each is enumerated with its fix in `references/anti-slop-engine.md`.

## 1. The three dials

Set after the Design Read. TSI is a regulated B2B operating-infrastructure brand, so the range is **anchored, not chaotic** — variance escapes monoculture without ever reading as Awwwards-experimental.

- **`VARIANCE: 5`** — 1 = perfect symmetry, 10 = artsy chaos. TSI range **4–7**. Drives layout asymmetry and structural diversity, never font/color changes.
- **`MOTION: 4`** — 1 = static, 10 = cinematic. TSI range **2–6**. Reveals state, sequence, proof; never urgent or ornamental.
- **`DENSITY: 4`** — 1 = airy gallery, 10 = packed cockpit. TSI range **3–6**. Product/data artifacts run denser; marketing runs airier.

| Surface | VARIANCE | MOTION | DENSITY |
|---|---|---|---|
| Landing / marketing page | 6 | 4 | 4 |
| Executive / sales deck | 5 | 4 | 3 |
| Product visual / dashboard / operating layer | 5 | 5 | 6 |
| Thought-leadership / report (warm-editorial) | 5 | 3 | 3 |
| Closing CTA / data moment (dark-feature) | 6 | 5 | 4 |
| Compliance-sensitive / legal-reviewed surface | 4 | 2 | 5 |

Override conversationally when the brief calls for it; do not ask the user to edit this file. "Anchored, can flex" means: go to 7 variance or 6 motion when the brief earns it; do not exceed the range for a regulated surface.

## Core rules (brand anchors — fixed)

- **Light premium is the default mode, not the only mode.** Dark-feature, warm-editorial, and product-system modes are first-class. Pick per the Design Read; do not make every premium output a dark command center *or* the same light template.
- **Color anchors are TSI-blue-led:** `#001E41`, `#4396F6`, white, approved blue tints, green `#66CC00`, orange `#FF8300`. One accent logic per artifact — lock it and audit every component. Warm neutrals may *support* editorial surfaces, but CTAs, data color, marks, and key accents stay blue. Gradients only subtle and brand-derived (white→blue-tint, blue edge light, quiet radial bloom). No rainbow, purple-SaaS, neon, or multi-hue rails.
- **Poppins is the anchor typeface.** Add a mono lane (JetBrains/IBM Plex/SF Mono) for telemetry/data, or a restrained serif lane (Source Serif, Charter) for editorial — only when the surface benefits and fallbacks are defined. Emphasis within a headline uses italic/bold of the *same* family, never a injected foreign font.
- **Logos are placed, never generated.** Keep official marks out of image prompts. Composite with `scripts/overlay_tsi_logo.py`; never ask an image model to draw or edit the logo. Never blur, recolor, glow, or distort the mark.
- **Synthetic data only.** Never invent client names, account/patient/borrower records, payment data, or legal threats. No shame, panic, intimidation, or distressed-consumer imagery. Regulated-industry respect is non-negotiable.
- **Voice:** executive-modern operating partner — direct, premium, product-literate, compliance-aware. No exclamation points, no vague superlatives ("best-in-class," "world-class," "seamless," "supercharge"), no em dashes, no AI cadence. Tagline `Revenue recovery, reimagined.` only where a tagline belongs; italicize `reimagined` in display contexts.

## Workflow

1. Write the Design Read; set the dials.
2. Pick a visual mode (`references/visual-modes.md`). Default light-premium only if the brief does not point elsewhere.
3. Select official assets deliberately. If none fits, prompt/generate a support image — do not force people illustrations into every layout.
4. Build with concrete hierarchy: one primary message, one supporting mechanism/proof, one clear next action. Earn every section.
5. Add motion only to clarify state/sequence/hierarchy/product behavior. Always include `prefers-reduced-motion: reduce`.
6. Run the pre-flight gate in `references/anti-slop-engine.md` and the `references/qa-rubric.md` checklist before delivery. Flag substitutions, assumptions, and any TSI legal/product/COI review needs.

## Bundled resources

- `DESIGN.md` — normative tokens and design rationale (fixed anchors).
- `references/` — engine, brand, logo/assets, visual modes, imagery, components, motion, surface contracts, QA.
- `assets/official/` — logos, symbols, sub-brand marks, people illustrations, portraits, social.
- `assets/generated-v2/` — WebP previews, contact sheet, prompt sidecars for directional generated assets.
- `assets/reference/adventurous-visual-system-contact-sheet.png` — atmospheric lane reference.
- `uploads/` — brand guide PDF, PPTX template, extracted brand text.
- `examples/` — single-file HTML examples (each a *different* design read; study them for range, do not clone one).
- `scripts/validate_package.py` — package/artifact validation. `scripts/overlay_tsi_logo.py` — deterministic logo compositing.
- `evals/evals.json` — evaluation prompts for regression and taste testing.
