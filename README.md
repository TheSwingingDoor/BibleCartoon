# The Swinging Door — Character Bible

This repository is the production source of truth for the recurring characters in **The Swinging Door**, a black-and-white, single-frame American editorial-cartoon series.

The first locked character is **Drew**, a 46-year-old anthropomorphic flamingo: observant, curious, arch, and recognizable by his long S-curved neck, expressive avian eyes, feathered wing-arms, and permanent black bow tie.

## Why this repository exists

Image models drift when permanent identity, temporary scene choices, and artistic style are mixed together. This repository separates them:

1. **Locked identity** — features that never change without an approved canon revision.
2. **Controlled performance** — approved expressions, poses, gestures, and speech patterns.
3. **Scene variables** — clothing, props, setting, weather, camera angle, and action chosen for one cartoon.

Every production image must begin with the locked master reference and the matching prompt block. A generated scene is never allowed to redefine the character.

## Source-of-truth order

When two files appear to conflict, use this order:

1. `characters/<id>/assets/reference/*master-model*`
2. `characters/<id>/character.json`
3. `characters/<id>/CANON.md` and `VISUAL-SPEC.md`
4. expression, gesture, wardrobe, scene, and voice guides
5. generated reference sheets
6. old production scenes

The newest picture is **not** automatically canon. Only files explicitly marked `locked` or `approved` are authoritative.

## Repository map

```text
characters/
  drew/                 Drew's complete locked bible
  _template/            Repeatable structure for future characters
schema/                  Machine-readable character schema
scripts/                 Dependency-free integrity checks
.github/                 Change-control and validation workflow
```

Start with [`characters/drew/README.md`](characters/drew/README.md).

## Production rule in one sentence

**Attach the master model, copy the invariant prompt block unchanged, name only the scene variables, and reject any output that fails the quality-control checklist.**

## Validation

Run:

```bash
python scripts/build_asset_manifest.py --check
python scripts/validate_bible.py
```

The checks verify required files, character data, asset dimensions, and SHA-256 fingerprints so an accidental image replacement cannot silently become canon.

## Adding the next two characters

Copy `characters/_template`, assign a unique lowercase character ID, supply a locked master model, and complete every required guide before changing the character status from `draft` to `locked`. Do not borrow Drew's anatomy, wardrobe, expressions, or personality unless the new character explicitly shares them.

## Rights

The character designs, artwork, written canon, and production system are proprietary. See [`RIGHTS.md`](RIGHTS.md).
