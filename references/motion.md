# Motion

Use motion to communicate structure, not decoration.

## Motion Vocabulary

Useful prompt words from common animation vocabulary:

- Reveal: disclose hierarchy or content in order.
- Stagger: sequence related items.
- Draw-on: show lines, rails, or paths forming.
- Crossfade: transition between states without directional distraction.
- Morph: connect related states in the same object.
- Pulse: indicate live status, sparingly.
- Scrub: tie animation to scroll or timeline position.
- Count-up: animate synthetic metrics when it helps emphasis.
- Loop: repeat ambient state only when quiet and non-distracting.

## Timing

- Micro interactions: 120-180ms.
- UI state changes: 180-260ms.
- Section reveal: 320-700ms.
- Showcase sequences: up to 1200ms for first entrance, then quieter loops.

Use easing that feels composed: `cubic-bezier(.2,.7,.2,1)` or similar.

## Implementation Rules

- Animate `transform` and `opacity` first.
- Avoid animating layout-heavy properties like `top`, `left`, `width`, or large filters when avoidable.
- Include `@media (prefers-reduced-motion: reduce)` in HTML examples.
- Keep inline JS small and readable.
- Pause or simplify continuous motion for reduced-motion users.

## TSI-Specific Motion

Good uses:

- A rail draws from intake to resolution.
- Status tokens move through validation gates.
- A proof metric counts up once.
- A product panel cycles between routing, review, and reporting states.
- A final CTA subtly reveals the logo and action.

Bad uses:

- Bouncy consumer springs.
- Parallax for its own sake.
- Infinite glowing particles that distract from message.
- Animated gradients that become the main content.
- Motion that implies urgency, panic, or threat.
