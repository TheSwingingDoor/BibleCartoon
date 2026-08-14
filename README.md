# The Swinging Door — Character Bible

This repository is the production source of truth for the recurring characters in **The Swinging Door**, a black-and-white, single-frame American editorial-cartoon series.

The first two locked characters are **Drew**, a 46-year-old anthropomorphic flamingo with an arch analytical voice, and **Abby**, the adult anthropomorphic Westie who owns and tends bar at The Swinging Door with warmth, wit, and quiet authority.

| Character | Production entry point | Locked master |
|---|---|---|
| Drew | [`characters/drew/README.md`](characters/drew/README.md) | [`drew-master-model-v1.png`](characters/drew/assets/reference/drew-master-model-v1.png) |
| Abby | [`characters/abby/README.md`](characters/abby/README.md) | [`abby-master-model-v1.png`](characters/abby/assets/reference/abby-master-model-v1.png) |

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
  abby/                 Abby's complete locked bible
  _template/            Repeatable structure for future characters
docs/                    Cross-character workflow and versioning
schema/                  Machine-readable character schema
scripts/                 Dependency-free integrity checks
.github/                 Change-control and validation workflow
```

Start with [`characters/README.md`](characters/README.md), then open the selected character's README.

## Production rule in one sentence

**Attach the master model, copy the invariant prompt block unchanged, name only the scene variables, and reject any output that fails the quality-control checklist.**

## Validation

Run:

```bash
python scripts/build_asset_manifest.py --check
python scripts/validate_bible.py
```

The checks verify required files, character data, asset dimensions, and SHA-256 fingerprints so an accidental image replacement cannot silently become canon.

## Adding the next character

Copy `characters/_template`, assign a unique lowercase character ID, supply a locked master model, and complete every required guide before changing the character status from `draft` to `locked`. Follow [`docs/ADDING-A-CHARACTER.md`](docs/ADDING-A-CHARACTER.md). Reuse the production structure, never another character's anatomy, wardrobe, expressions, or personality.

## Rights

The character designs, artwork, written canon, and production system are proprietary. See [`RIGHTS.md`](RIGHTS.md).
