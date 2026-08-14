# Image Prompt Pack

These blocks are designed to be copied, not paraphrased. Paraphrasing permanent traits is a common source of drift.

## Reference order

1. Primary identity: `assets/reference/drew-master-model-v1.png`
2. One approved secondary reference for expression, pose, wing-hand anatomy, wardrobe, or scene continuity
3. Optional scene/background reference that must not influence character design

## Locked invariant block

```text
IDENTITY LOCK — SAME DREW, NOT A REDESIGN:
Drew is the exact 46-year-old male anthropomorphic flamingo shown in the primary master-model reference. Preserve his compact mature flamingo head; expressive but avian eyes with controlled visible white, distinct iris and pupil, and one small catchlight; pale-and-dark strongly downturned flamingo beak; long slim pronounced S-curved neck; average healthy build; long bird legs and webbed flamingo feet; articulated wing-arms made from layered contour and flight feathers; and three small feather-digits per wing-hand, consisting of one thumb-feather and two finger-feathers with tiny pale understated avian nail tips. His solid black bow tie is permanent and always visible. His entire body is covered in natural feathers and presented as a wholesome, G-rated editorial-cartoon character. Keep the same proportions, age, facial construction, feather pattern, and silhouette as the master reference.
```

## Style block

```text
STYLE LOCK:
Single-frame mature American editorial cartoon, completely hand-drawn in black pen with graphite-like line variation, fine feather strokes, selective crosshatching, restrained gray ink wash, and warm off-white paper. Clear visual hierarchy, readable silhouettes, dry sophisticated tone. Black and white only. No glossy digital rendering, 3D, anime, photorealism, flat vector art, color, or watermark.
```

## Negative block

```text
FORBIDDEN DRIFT:
Do not change Drew into another bird species. No duck bill, parrot hook, pelican pouch, human head, human nose, lips, teeth, hair, human ears, giant alien eyes, all-black bead eyes, oversized whites, fully human eyes, straight or thick neck, human arms, palms, five fingers, bare human hands, extra wings, long claws, talons, manicured nails, black fingertips, muscular body, extreme thinness, child proportions, permanent suit, missing bow tie, patterned bow tie, extra olives, color, or modern glossy cartoon styling.
```

## Scene template

```text
Use case: identity-preserve
Asset type: final single-frame Swinging Door editorial cartoon
Input images: Image 1 is Drew's primary identity reference; Image 2 is the approved [expression/pose/anatomy/wardrobe] reference; Image 3, if present, is background-only.

[PASTE LOCKED INVARIANT BLOCK]
[PASTE STYLE BLOCK]

SCENE VARIABLES — CHANGE ONLY THESE:
Location: [location]
Action and pose: [action]
Expression: [approved expression]
Clothing beyond bow tie: [scene-required clothing or none]
Props: [props or none]
Other characters: [names and their own reference roles]
Camera and crop: [shot]
Caption space: [placement]

[PASTE NEGATIVE BLOCK]
```

## Model-sheet prompt

```text
Use case: identity-preserve
Asset type: character-production reference sheet
Primary request: show the exact same Drew from the master reference in a clean, evenly spaced study of [expressions/poses/gestures/clothing fits]. Preserve identity and anatomy in every panel. Use a plain warm off-white paper background with no scene décor. Label each study clearly and keep all figures at consistent scale.
[PASTE LOCKED INVARIANT BLOCK]
[PASTE STYLE BLOCK]
[PASTE NEGATIVE BLOCK]
```

## Edit template

```text
Use case: precise-object-edit
Asset type: corrected Swinging Door production art
Primary request: change only [named element]. Preserve all other pixels, character identity, pose, expression, anatomy, wardrobe, props, composition, lettering, line style, and wash placement.
[PASTE LOCKED INVARIANT BLOCK]
[PASTE NEGATIVE BLOCK]
```

## Multi-character rule

Never use Drew's reference as a styleless global reference. Label it `Drew — identity`. Give every other recurring character a separate identity reference and invariant block. A shared style block may apply to the entire frame; anatomy blocks may not.
