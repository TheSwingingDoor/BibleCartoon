# Instructions for AI and Human Production Agents

These instructions apply to every file and image in this repository.

## Required reading order

Before generating or editing Drew, read:

1. `characters/drew/character.json`
2. `characters/drew/CANON.md`
3. `characters/drew/VISUAL-SPEC.md`
4. the guide relevant to the requested scene
5. `characters/drew/PROMPT-PACK.md`
6. `characters/drew/QUALITY-CONTROL.md`

Always attach `characters/drew/assets/reference/drew-master-model-v1.png` as the primary identity reference.

## Non-negotiable rules

- Treat locked fields as immutable.
- Treat clothing, scenery, pose, action, and non-signature props as scene variables.
- Change only what the request names.
- Never infer a permanent trait from one production scene.
- Never replace a locked asset in place. Add a versioned successor and document the decision.
- Never mark generated artwork `approved` without human visual review.
- Do not merge visual traits from other characters.
- Do not use a written description as a substitute for the master image when image-reference input is available.
- Run both validation commands before publishing.

## Canon conflict rule

If instructions conflict, stop the generation and report the conflict. Do not average competing designs. The source-of-truth order in the root README decides which rule wins.

## Image-generation discipline

Use one explicit reference role per image:

- **Primary identity reference** — locks Drew's appearance.
- **Secondary performance reference** — expression, wing-hand anatomy, pose, or wardrobe fit.
- **Scene reference** — background or prop only; it must not alter Drew.

Keep the invariant prompt block unchanged across scenes. Put all requested changes under a separate `SCENE VARIABLES` heading.

## Pull requests

Any canon change must state:

- what changed;
- whether it is locked, controlled, or scene-variable;
- which references were regenerated;
- why existing scenes remain valid or need replacement;
- who approved the new canon version.
