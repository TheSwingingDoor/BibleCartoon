# Adding a character

Use this process for the two upcoming characters and every character after them.

## 1. Establish the identity lock

Decide and write down the character's species, adult age class, role, silhouette, body ratios, face geometry, eyes, hands or paws, clothing, signature accessories, default expression, and explicit forbidden changes. Resolve contradictions before generating art.

## 2. Create the minimum visual set

Every production-ready character needs:

1. Five-view master turnaround: front, 3/4 front, profile, 3/4 back, back.
2. Face and eye construction sheet.
3. Expression library with at least twelve distinct emotions.
4. Hands, gestures, and signature props.
5. Wardrobe and accessory construction.
6. Role-specific actions.
7. Environment blocking and scale.

The sheets must use the same anchor image and repeat every immutable trait. A pretty image that contradicts another sheet is not canon.

## 3. Write the machine-readable canon

Copy `characters/_template/character.template.json`, validate it against `schema/character.schema.json`, and fill every locked field. Give each character a stable lowercase `character_id` that will never be reused.

## 4. Write the human bible

Copy the template README. Add canonical appearance, personality and voice, prompt kit, scene recipes, continuity checklist, and changelog. State which older decisions are superseded.

## 5. Run a drift test

Generate at least six test scenes:

- neutral close-up;
- full-body neutral;
- profile action;
- seated or leaning pose;
- strong emotion;
- two-character interaction.

Reject any test that changes identity, proportions, eyes, clothing, signature accessories, or rendering style. Fix the written lock or add a specialist reference before accepting the character.

## 6. Version the canon

- Patch version: clearer wording or corrected label, no design change.
- Minor version: approved new pose, prop, or outfit variant.
- Major version: silhouette, anatomy, face, primary wardrobe, or role change.

Never silently replace a canonical asset. Record the change and its reason.
