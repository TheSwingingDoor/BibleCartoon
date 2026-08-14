# Contributing

This is a controlled production bible, not an open character-design exercise.

## Change categories

| Category | Example | Approval |
|---|---|---|
| Patch | typo, broken link, missing checksum | maintainer review |
| Controlled expansion | approved new expression or gesture | visual review required |
| Canon revision | anatomy, age, proportions, eyes, beak, bow tie | explicit owner approval and version bump |
| Scene addition | new outfit, prop, or location | review against existing canon |

## Workflow

1. Open the character-change issue template.
2. Identify the exact canon tier affected.
3. Add versioned files; do not overwrite locked references.
4. Update the asset catalog and rebuild the manifest.
5. Run validation.
6. Use the pull-request checklist and attach visual comparisons.

## Versioning

Character canon uses semantic versioning:

- **Major** — recognizable identity or anatomy changes.
- **Minor** — approved expansion such as new expression, pose, or scene rule.
- **Patch** — clarification that does not change appearance or behavior.
