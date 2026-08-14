# Abby — production prompt kit

## Required references

Always attach `assets/reference/abby-master-model-v1.png` first. Attach exactly one specialist sheet second:

- face or close-up: `assets/generated/abby-eyes-face-construction-v1.png`;
- emotional acting: `assets/generated/abby-expression-library-v1.png`;
- visible hands or props: `assets/generated/abby-hands-gestures-props-v1.png`;
- full-body motion: `assets/generated/abby-bartender-actions-v1.png`;
- clothing or rear view: `assets/generated/abby-wardrobe-details-v1.png`;
- environment and scale: `assets/generated/abby-bar-blocking-v1.png`.

## Immutable identity block

Copy this block without paraphrasing:

> Abby is the same adult female anthropomorphic West Highland White Terrier shown in the attached canonical master model. Preserve her exact identity and proportions: upright triangular ears, detailed layered white Westie facial fur, short canine muzzle, solid black canine nose, expressive medium-sized human-style eyes naturally integrated into the canine face with visible white sclera, medium-gray irises, round black pupils, small catchlights, clear eyelids, refined lashes, and expressive brow-fur. She has a feminine adult hourglass build with a fuller bust, narrow waist, slim hips, smooth hairless shapely legs, a natural thigh gap, five-digit anthropomorphic hands, and absolutely no tail. Her locked work outfit is a fitted light collared blouse with neatly rolled sleeves, only the top button open over a modest scalloped lace inset, a very short dark fitted bartender skirt/apron tied with a large centered back bow, a folded bar towel over one shoulder, a delicate bracelet, black closed-toe mid-height heels, and a close-fitting single strand of small round pearls with one centered oval faceted gemstone in a simple dark metal bezel. She is Abby, owner and bartender of The Swinging Door: intelligent, witty, warm, poised, competent, smiling, and unmistakably in charge.

## Style block

> Render in confident black ink and delicate graphite/ink wash on warm off-white paper, matching the attached reference sheets: refined variable-weight linework, fine directional fur texture, restrained mid-gray washes, generous breathing room, and a dry mid-century American magazine-cartoon sensibility. Strictly monochrome; no color, photorealism, 3D, anime, glossy airbrush, vector-flat shapes, dense cross-hatching, or watermark.

## Scene block template

Replace only bracketed content:

```text
Scene: [specific location and one focal action].
Framing: [close-up / waist-up / full-body / wide], [front / 3/4 / profile / rear 3/4], eye-level unless specified.
Expression: [one named expression from the library], directed toward [gaze target].
Hands and props: [exact action, grip, and object placement].
Continuity: Abby is [behind the bar / at the swinging doors / performing an approved owner task]. The bar counter reaches her upper hip when standing behind it. Preserve the locked outfit and jewelry. No unlisted characters or props.
Text: [none / exact required words in quotation marks].
```

## Negative block

> Do not redesign Abby. No tail, tail tuft, tail slit, or tail bulge. No furry legs, paws for feet, stockings, pants, long skirt, boots, bare feet, or wardrobe substitution. No plain choker; the pearl strand and centered oval gemstone must be present. No missing lace, towel, bracelet, back bow, or heels. No dot eyes, bead eyes, all-black eyes, giant eyes, empty irises, mismatched pupils, crossed gaze, fully human face, human nose, human ears, hairstyle, or exposed human skin. No puppy or child proportions. No exaggerated pin-up anatomy, explicit cleavage, vacant glamour pose, cruelty, incompetence, drunkenness, or submissive behavior. No extra limbs, malformed hands, duplicated fingers, floating props, color, photorealism, 3D, anime, watermark, or unauthorized text.

## Complete prompt template

```text
Use case: identity-preserve
Asset type: final Swinging Door cartoon illustration
Input images: Image 1 is Abby's canonical identity master; Image 2 is the relevant specialist reference.

[PASTE IMMUTABLE IDENTITY BLOCK]
[PASTE STYLE BLOCK]
[PASTE COMPLETED SCENE BLOCK]
[PASTE NEGATIVE BLOCK]
```

## Targeted correction language

Use one correction at a time:

- **Eyes:** “Change only Abby’s eyes to the canonical human-style eye construction; preserve every other mark.”
- **Collar:** “Change only the neckpiece to one close pearl strand with the centered oval gemstone; preserve everything else.”
- **Tail:** “Remove only the tail and any tail opening or bulge; reconstruct the skirt/apron rear as a continuous no-tail silhouette.”
- **Legs:** “Change only the legs to smooth, hairless, slim, shapely adult legs with a natural thigh gap; preserve pose, skirt, and heels.”
- **Hands:** “Correct only hand anatomy and object grip to five readable digits; preserve pose, prop position, and all other details.”

Never ask for a general “improvement” during a correction pass. Name the defect and lock all unaffected features.
