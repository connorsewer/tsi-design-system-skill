---
name: TSI Design System 2.0
colors:
  primary: "#001E41"
  accent: "#4396F6"
  white: "#FFFFFF"
  blueTint10: "#ECF4FE"
  blueTint20: "#DAE9FD"
  success: "#66CC00"
  warning: "#FF8300"
  ink900: "#001E41"
  ink700: "#1F3D6B"
  ink500: "#5E7493"
  ink200: "#D7DCE5"
  ink050: "#F6F7FA"
  coolSurface: "#F7FAFF"
  coolMist: "#EEF6FF"
  warmPaper: "#F7F3EC"
  warmStone: "#ECE4D8"
  warmInk: "#2B2A27"
  glassWhite: "rgba(255,255,255,0.72)"
  glassBlue: "rgba(236,244,254,0.72)"
typography:
  display-xl:
    fontFamily: Poppins
    fontSize: 4.5rem
    fontWeight: 300
    lineHeight: 1.02
  display-lg:
    fontFamily: Poppins
    fontSize: 3.5rem
    fontWeight: 300
    lineHeight: 1.05
  h1:
    fontFamily: Poppins
    fontSize: 2.75rem
    fontWeight: 300
    lineHeight: 1.1
  h2:
    fontFamily: Poppins
    fontSize: 2rem
    fontWeight: 400
    lineHeight: 1.18
  body-lg:
    fontFamily: Poppins
    fontSize: 1.125rem
    fontWeight: 400
    lineHeight: 1.58
  body:
    fontFamily: Poppins
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: Poppins
    fontSize: 0.78rem
    fontWeight: 600
    lineHeight: 1.2
  mono:
    fontFamily: JetBrains Mono
    fontSize: 0.875rem
    fontWeight: 500
    lineHeight: 1.4
rounded:
  xs: 2px
  sm: 6px
  md: 10px
  lg: 16px
  xl: 24px
  pill: 999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 64px
  section: 96px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.white}"
    rounded: "{rounded.sm}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  panel-light:
    backgroundColor: "{colors.white}"
    textColor: "{colors.primary}"
    rounded: "{rounded.lg}"
  panel-warm:
    backgroundColor: "{colors.warmPaper}"
    textColor: "{colors.warmInk}"
    rounded: "{rounded.lg}"
  panel-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.white}"
    rounded: "{rounded.lg}"
  panel-cool:
    backgroundColor: "{colors.coolSurface}"
    textColor: "{colors.ink900}"
    rounded: "{rounded.lg}"
  status-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.primary}"
    rounded: "{rounded.pill}"
  status-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.primary}"
    rounded: "{rounded.pill}"
---

## Overview

TSI Design System 2.0 is a light-premium brand system for Transworld Systems Inc. It should feel like a modern operating-infrastructure company: precise, executive, calm, and capable of expressive generated assets without losing regulated-industry credibility.

The system expands beyond the conservative 1.0 rulebook. It keeps TSI's logos, colors, typography, sub-brand structure, and compliance posture intact, while allowing subtle gradients, refined depth, warm editorial neutrals, motion-led product storytelling, and newly generated support imagery.

## Brand Anchor

The recognizably TSI layer is built from:

- TSI dark blue `#001E41` for trust, structure, headlines, CTAs, and dark anchor panels.
- TSI bright blue `#4396F6` for active state, proof, links, rails, glow edges, and signal.
- White and bright-blue tints for clean surfaces and scannable enterprise layouts.
- Poppins as the primary identity typeface.
- Official logos and symbols placed as final assets, never generated or approximated.

## Palette Lanes

Use three palette lanes instead of one fixed mood.

**Light premium system** is the default. It uses white, cool blue-white, TSI blue accents, hairline borders, subtle shadow, and soft brand-derived gradients. This lane should power landing pages, decks, product pages, and most executive collateral.

**Warm editorial system** supports thought leadership, reports, premium explainers, and campaign pages. Warm paper and stone neutrals may become foundations, but TSI blue still leads CTAs, data, logo placement, and navigation.

**Dark feature system** is for product panels, final CTAs, motion artifacts, data moments, and dramatic contrast. Do not default every premium output to a dark command center.

## Gradients And Depth

Gradients are allowed when subtle and brand-derived. Prefer white-to-blue-tint, blue atmospheric edge light, and quiet radial blooms behind product artifacts. Avoid rainbow, purple SaaS, neon haze, and unrelated color clouds.

Depth should feel refined, not puffy. Use layered panels, soft shadows, translucent white/glass surfaces, and clear hierarchy. Keep official logo geometry crisp and never blur, recolor, or glow the logo.

## Typography

Use Poppins for the TSI voice. Display sizes use Light or Regular; body text uses Regular; labels, eyebrows, tabs, and buttons use SemiBold.

Optional pairing lanes:

- UI/data lane: pair Poppins with JetBrains Mono, IBM Plex Mono, or SF Mono for telemetry, tables, metrics, and product artifacts.
- Editorial lane: pair Poppins with a refined serif such as Source Serif, Charter, or Georgia for long-form premium pages or reports. Use the serif for limited editorial texture, not for core UI.

## Shape

TSI 2.0 can be softer than 1.0, but not consumer-rounded. Use 6-16px radii for premium cards and product panels, 24px only for large atmospheric feature surfaces, and pills for status only.

## Motion

Motion should reveal structure: sequence, state change, progress, routing, validation, or emphasis. Use transform and opacity first. Include `prefers-reduced-motion: reduce` handling in HTML, CSS, and component examples.

## Imagery

Use official TSI people illustrations and portraits when the surface needs continuity with the established brand or a human moment. Do not force them into every artifact.

Generate new imagery for light hero atmospheres, abstract product systems, diagrams, motion layers, spot assets, and editorial visuals. Never generate official marks, fake UI with sensitive data, fake customer/account/patient records, shame, panic, legal intimidation, or distressed consumers.

## Voice

Write as an executive-modern operating partner. Copy should be direct, premium, product-literate, and compliance-aware. Avoid exclamation points, vague superlatives, AI cadence, and inflated claims.

Use the current tagline `Revenue recovery, reimagined.` only where a tagline belongs. Italicize `reimagined` in display contexts when supported.
