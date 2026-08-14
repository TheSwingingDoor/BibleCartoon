# Image-generation workflow

## Input order

1. Master model sheet.
2. One specialist sheet matching the shot.
3. Immutable character block.
4. Scene-only instructions.
5. Negative block.

Reference order matters. The master establishes identity; the specialist sheet establishes local anatomy or action. Adding unrelated reference images increases accidental trait blending.

## Scene request contract

Before generation, write a compact request with:

- `character_id` and `canon_version`;
- setting and time;
- camera/framing;
- pose/action;
- expression;
- interacting characters and props;
- dialogue or required text, if any;
- intentional deviations, which require approval.

The request may change scene variables only. It may not rewrite immutable identity.

## Generation pass

- Use the immutable block verbatim.
- Describe one focal action.
- Ask for hands and held objects explicitly when visible.
- State which side of the bar Abby occupies.
- Repeat `no tail` whenever the rear silhouette is visible.
- Repeat the eye construction whenever the face is larger than a quarter of the frame.
- Keep text outside the art unless the scene requires a sign, chalkboard, TV, or caption.

## Review pass

Review at 100% size, not only as a thumbnail. Use the checklist and mark each item pass/fail. A single failure in identity, anatomy, wardrobe, jewelry, or role position makes the image a revision candidate, not a final.

## Correction pass

Change one category at a time and restate invariants. Example: “Change only the missing pearl collar; preserve face, eyes, expression, pose, hands, clothes, background, labels, and line style exactly.” Broad rewrites create more drift.

## Archive pass

Record the canon version, prompt, references, scene request, final filename, and reviewer. Do not let an unreviewed generation become a new visual reference.
