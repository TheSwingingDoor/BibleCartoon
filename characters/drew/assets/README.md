# Drew Asset System

## Status meanings

- `locked` — primary identity authority.
- `approved` — production reference that expands the locked identity.
- `review` — candidate awaiting human approval; never use as sole reference.
- `retired` — historical only.

## Required reference use

Every Drew generation uses the locked master. Add at most one or two approved secondary references relevant to the task. Too many unrelated references increase drift.

## Files

| Asset | Role | Status |
|---|---|---|
| `reference/drew-master-model-v1.png` | identity and turnaround authority | locked |
| `generated/drew-expression-library-v1.png` | facial performance | review |
| `generated/drew-wing-hand-anatomy-v1.png` | wing-arm and feather-hand construction | review |
| `generated/drew-pose-library-v1.png` | whole-body acting and silhouettes | review |
| `generated/drew-wardrobe-fit-v1.png` | scene-variable clothing fit | review |
| `generated/drew-scene-continuity-v1.png` | identity across environments | review |
| `generated/drew-proportion-style-v1.png` | proportion and rendering control | review |

`asset-catalog.json` records creative metadata. `asset-manifest.json` records file size, image dimensions, and SHA-256 fingerprints generated from the actual files.
