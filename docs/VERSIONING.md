# Canon versioning and approvals

The character bible uses semantic versioning.

| Change | Version | Approval |
| --- | --- | --- |
| Typo, clearer wording, metadata correction | Patch | Editor |
| New approved expression, prop, pose, or non-default wardrobe | Minor | Character owner |
| Face, silhouette, anatomy, default wardrobe, role, or signature accessory | Major | Character owner |

## Asset status

- **Canonical**: approved and usable as a generation reference.
- **Candidate**: under review; never used as identity input for production.
- **Retired**: preserved for history but excluded from generation.

## Change procedure

1. Describe the desired change in words.
2. Identify every file and sheet it affects.
3. Update `character.json` and written canon first.
4. Regenerate or edit all conflicting canonical sheets.
5. Run continuity checks.
6. Add a dated changelog entry.
7. Increment the version.

An asset cannot be canonical if it conflicts with the current machine-readable lock.
