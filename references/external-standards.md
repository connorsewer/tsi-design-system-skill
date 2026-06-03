# External Standards Summary

This package summarizes external references instead of mirroring them.

## DESIGN.md

Source: https://github.com/google-labs-code/design.md

DESIGN.md combines YAML frontmatter design tokens with Markdown rationale. Tokens provide exact values; prose explains why and how to use them. Validate with:

```bash
npx @google/design.md lint DESIGN.md
```

Use `DESIGN.md` in this package as the normative token source.

## Animation Vocabulary

Source: https://animations.dev/vocabulary

Use shared animation terms such as reveal, stagger, draw-on, morph, pulse, scrub, and loop so agents can describe motion precisely.

## OpenAI Image Guidance

Sources:

- https://developers.openai.com/api/docs/models/gpt-image-2
- https://github.com/openai/openai-cookbook/blob/main/examples/multimodal/image-gen-models-prompting-guide.ipynb

Use structured prompts with goal, subject, visual style, composition, and constraints. Use reference images selectively, avoid generating logos, and add final text/logos outside the image when precision matters.

## Component Gallery

Source: https://component.gallery/

Use it for pattern research across real-world design systems. Do not copy component screenshots or styling directly. Translate patterns into TSI's own palette, typography, motion, and compliance context.
