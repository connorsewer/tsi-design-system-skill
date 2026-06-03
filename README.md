# TSI Design System 2.0 — Agent Skill

A Claude / agent **skill** that produces premium, unmistakably-TSI brand work (landing pages, decks, product visuals, UI prototypes, marketing copy, generated-image prompts, logo overlays, sales collateral) for Transworld Systems Inc. and its sub-brands (ARM, Loan Servicing, CXBPO, Healthcare RCM, DebtNext, UAS, CollectX, PULSE).

> **Proprietary / internal.** This repository contains TSI's Brand Identity Guide, official logos, and licensed people photography. It is private and intended for TSI and authorized collaborators only. Do not redistribute or make public without TSI brand/legal approval. See `NOTICE.md`.

## What makes 2.0 different

1.0 was a conservative rulebook. 2.0 keeps every brand anchor but adds an **anti-slop execution engine** (grafted from production design-skill practice) so output stops collapsing into generic B2B SaaS:

- **Design Read first.** Before any output the agent states one line — surface, audience, brand family, visual mode, and one concrete structural idea — so it commits to a direction instead of defaulting to one look.
- **Three anchored dials.** `VARIANCE (4–7) / MOTION (2–6) / DENSITY (3–6)`, tuned for a regulated B2B brand. Variance lives in layout and composition, never in the fixed anchors.
- **Match-and-refuse bans + pre-flight gate.** A concrete banned-trope list (the house template, hero-metric grids, eyebrow-on-every-section, rainbow rails, gradient text, default glass, identical card grids, buzzwords, em dashes) with a 10-point gate run before delivery. See `references/anti-slop-engine.md`.
- **Examples that teach range, not a template.** The three bundled examples each demonstrate a different design read (light-premium landing, multi-mode deck, dense product operating layer).

Fixed brand anchors (never traded for variance): TSI blue `#001E41` / `#4396F6`, Poppins, official logos (placed, never generated), regulated-industry credibility, and synthetic-data-only safety.

## Install

This is an agent skill, not an app. Install it where your agent looks for skills.

**Claude Code (and npx-style agents):**
```bash
# clone, then copy the skill folder into your skills dir
git clone git@github.com:connorsewer/tsi-design-system-skill.git
cp -R tsi-design-system-skill ~/.claude/skills/tsi-design-system
# (and/or) ~/.agents/skills/tsi-design-system
```
Start a fresh session so the skill loads, then prompt with any TSI work
("build an ARM landing page", "a Healthcare RCM closing slide"). The skill
triggers on TSI / Transworld / sub-brand / receivables-domain language.

**Validate a copy before shipping:**
```bash
python3 scripts/validate_package.py .
```

## Structure

| Path | Purpose |
|---|---|
| `SKILL.md` | Entry point: Design Read, dials, core rules, workflow (read first). |
| `DESIGN.md` | Normative tokens — color, type, shape, spacing, motion (fixed anchors). |
| `references/anti-slop-engine.md` | The teeth: banned-trope list + pre-flight gate. |
| `references/` | Brand foundations, logo/assets, visual modes, imagery, components, motion, surface contracts, QA. |
| `assets/official/` | Official logos, symbols, sub-brand marks, people illustrations, portraits. |
| `assets/generated-v2/` | Directional generated-asset previews + prompt sidecars. |
| `examples/` | Single-file HTML examples — each a different design read. |
| `scripts/` | `validate_package.py` (package checks), `overlay_tsi_logo.py` (deterministic logo compositing), `inline_assets.py` (embed assets for portable shared files), `check_logo_integrity.py` (audit logo aspect-ratio before delivery). |
| `uploads/` | Source brand guide PDF, PowerPoint template, extracted brand text. |
| `evals/` | Evaluation prompts for regression and taste testing. |

## License

Proprietary. All rights reserved by Transworld Systems Inc. See `NOTICE.md`.
