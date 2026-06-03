# Adventurous Backgrounds And Accent Images

Use this reference when the user wants more images like the May 2026 adventurous visual system batch, or when a landing page, deck, video frame, or campaign asset needs an expressive atmospheric background.

Bundled visual reference:

- `assets/reference/adventurous-visual-system-contact-sheet.png`

Local full-resolution source set, when available in this workspace:

- `/Users/connorlaughlin/Desktop/TSI Images/tsi-image-generation/outputs/adventurous-visual-system-2026-05-29/`

The contact sheet is bundled to avoid adding the full 32 MB source batch to the skill. Use the full-resolution source folder when working in this local workspace and the user wants to reuse an existing background directly.

## What This Lane Adds

This lane gives TSI a more atmospheric and cinematic visual range:

- Textured horizon plates for title slides, hero backplates, and video chapter cards.
- Luminous corporate gradients for website section backgrounds and slide interstitials.
- Deep-blue light curtains for closing slides, analytics sections, and command-center moments.
- Portal threshold scenes for innovation narratives and keynote openers.
- Atmospheric motion studies for video transitions and relationship-preservation stories.
- Data nebula fields for AI, analytics, and orchestration narratives.

Use these as optional expressive lanes, not as the default 2.0 style.

## Prompt Recipes

### Textured Horizon Plate

```text
Goal:
Create a premium TSI background plate for a title slide or website hero.

Visual mode:
Adventurous textured horizon.

Scene / structure:
Layered abstract blue-white horizon, mist bands, low ridge forms, dark-blue grounding band, bright-blue rim light, and broad copy-safe space.

Style:
TSI dark blue #001E41, TSI bright blue #4396F6, pale blue haze, subtle paper/canvas tooth, cinematic but restrained.

Constraints:
No logos, no text, no fake data, no people, no sci-fi spaceship mood, no rainbow gradient.
```

### Luminous Corporate Gradient

```text
Goal:
Create a light premium section background for TSI web or deck use.

Visual mode:
Luminous corporate gradient.

Scene / structure:
Airy white-to-blue field with translucent overlapping blue light planes, subtle lower or corner anchor, gentle bright-blue bloom, and clean text-safe region.

Style:
OpenAI-adjacent subtle gradient atmosphere, but brand-derived from TSI blue, white, and blue tints.

Constraints:
No generic purple SaaS gradient, no generated logos, no readable UI, no fake data.
```

### Atmospheric Motion Study

```text
Goal:
Create a motion-ready transition background for a TSI video, deck, or dynamic page section.

Visual mode:
Atmospheric motion study.

Scene / structure:
Soft blurred signal band sweeping across a pale blue or deep-blue field, with clean negative space and one directional movement cue.

Style:
Cinematic blue motion, limited warm edge light, dark-blue shadow, fine grain, subtle energy.

Constraints:
No logos, no text, no people, no frantic speed, no consumer neon.
```

### Deep Blue Light Curtain

```text
Goal:
Create a dark feature-panel background for analytics, closing CTA, or command-center storytelling.

Visual mode:
Deep blue light curtain.

Scene / structure:
TSI dark-blue field with vertical or diagonal luminous blue curtains, restrained particles, and a calm dark lower area for typography.

Style:
Executive, cinematic, high contrast, enterprise infrastructure, not sci-fi spectacle.

Constraints:
No logos, no fake dashboards, no starfield, no cyberpunk palette.
```

### Data Nebula Field

```text
Goal:
Create an abstract data-orchestration accent image for AI, analytics, or platform narratives.

Visual mode:
Data nebula field.

Scene / structure:
Flowing wave of small data points, bright-blue signal paths, sparse green/orange status sparks, and dark-blue depth.

Style:
Premium analytics, elegant, controlled, no literal brain/cloud/server cliches.

Constraints:
No logos, no fake data labels, no rainbow particle cloud.
```

## Reuse Guidance

When using existing adventurous images:

- Prefer them as backgrounds, backplates, interstitials, or accent layers.
- Add official logos afterward with HTML, slides, design software, or `scripts/overlay_tsi_logo.py`.
- Add final typography outside the image so text remains crisp and editable.
- Do not crop away the main atmospheric movement; use `object-fit: cover` only for abstract backgrounds, not people or logos.
- Keep a raw unbranded source and save branded derivatives separately.

## QA

Approve when:

- The image is atmospheric but still recognizably TSI-blue-led.
- Warm light is secondary and controlled.
- The composition has clear copy/logo-safe space.
- It feels premium and executive, not sci-fi, crypto, cyberpunk, or generic SaaS.
- It does not replace the light-premium default; it extends the system for the right moments.
