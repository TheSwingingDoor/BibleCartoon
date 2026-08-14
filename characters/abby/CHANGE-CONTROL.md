# Abby — change control

## Version policy

- Patch: wording, label, metadata, or non-visual correction.
- Minor: approved new expression, gesture, prop, pose, or explicit alternate wardrobe.
- Major: face, eye system, silhouette, anatomy, default wardrobe, role, or signature jewelry.

## Required change sequence

1. State the desired change in words.
2. Identify whether it is locked, controlled, or scene-variable.
3. Update `character.json`, written canon, and `prompts.json`.
4. Create versioned successor assets; never silently replace a locked reference.
5. Update catalog and manifest.
6. Run both repository validation commands.
7. Record approval and the new canon version.

An attractive generation that breaks a locked rule is still wrong. Do not rewrite canon to excuse an image accident.
