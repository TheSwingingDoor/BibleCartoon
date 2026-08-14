# Drew Change Control

## Locked versus expandable

Locked identity includes age, species, head, eyes, beak, neck, build, wing-arm anatomy, feather-hand construction, legs, feet, bow tie, base presentation, and rendering style.

Expandable material includes additional approved expressions, gestures, poses, scene wardrobes, props, locations, and relationships. Expansion must demonstrate the existing character; it cannot redesign him.

## Required process for a canon revision

1. State the problem in one sentence.
2. Identify every locked field affected.
3. Preserve the current master as a historical version.
4. Create a versioned candidate reference.
5. Compare candidate and current master side by side.
6. Update `character.json`, written guides, prompt block, and forbidden-drift list together.
7. Regenerate every dependent approved sheet.
8. Rebuild the asset manifest and run validation.
9. Obtain explicit owner approval.
10. Bump the canon version and changelog.

## Prohibited shortcuts

- overwriting the master image;
- changing prose without updating machine-readable canon;
- treating one attractive generation as an approved redesign;
- mixing two competing eye, beak, neck, or hand systems;
- using scene clothing to redefine the base body;
- removing failed history to hide a decision.

## Deprecation

Superseded assets remain in version history and are marked `retired` in the catalog. Prompts and production systems must reference only one locked canon version at a time.
