# Instructions for AI and Human Production Agents

These instructions apply to every file and image in this repository.

## Required reading order

Before generating or editing any character with ID `<id>`, read:

1. `characters/<id>/character.json`
2. `characters/<id>/CANON.md`
3. `characters/<id>/VISUAL-SPEC.md`
4. the guide relevant to the requested scene
5. `characters/<id>/PROMPT-PACK.md`
6. `characters/<id>/QUALITY-CONTROL.md`

Always attach the character's locked asset under `characters/<id>/assets/reference/` as the primary identity reference. For Abby this is `abby-master-model-v1.png`; for Drew it is `drew-master-model-v1.png`.

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

- **Primary identity reference** — locks the selected character's appearance.
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
