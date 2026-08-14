#!/usr/bin/env python3
"""Dependency-free structural validation for every indexed character bible."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_ROOT = [
    "README.md",
    "AGENTS.md",
    "RIGHTS.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "schema/character.schema.json",
    "characters/index.json",
]

REQUIRED_CHARACTER = [
    "README.md",
    "character.json",
    "prompts.json",
    "CANON.md",
    "VISUAL-SPEC.md",
    "EXPRESSIONS.md",
    "ANATOMY-AND-GESTURE.md",
    "WARDROBE.md",
    "VOICE-AND-BEHAVIOR.md",
    "RELATIONSHIPS.md",
    "SCENE-RULES.md",
    "PROMPT-PACK.md",
    "QUALITY-CONTROL.md",
    "CHANGE-CONTROL.md",
    "assets/asset-catalog.json",
    "assets/asset-manifest.json",
    "assets/REFERENCE-GENERATION-SPECS.md",
    "assets/QA-REVIEW.md",
]

REQUIRED_CHARACTER_KEYS = {
    "schema_version",
    "character_id",
    "canon_version",
    "status",
    "identity",
    "locked_visual",
    "controlled_performance",
    "scene_variables",
    "forbidden_drift",
    "reference_assets",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def validate_character(index_item: dict, errors: list[str]) -> int:
    character_id = index_item["id"]
    base = ROOT / "characters" / character_id
    missing_files = [relative for relative in REQUIRED_CHARACTER if not (base / relative).is_file()]
    for relative in missing_files:
        fail(f"{character_id}: missing file: {relative}", errors)
    if missing_files:
        return 0

    character = load_json(base / "character.json")
    prompts = load_json(base / "prompts.json")
    catalog = load_json(base / "assets" / "asset-catalog.json")
    manifest = load_json(base / "assets" / "asset-manifest.json")

    missing_keys = REQUIRED_CHARACTER_KEYS - set(character)
    if missing_keys:
        fail(f"{character_id}: character.json missing {sorted(missing_keys)}", errors)
    if character.get("character_id") != character_id:
        fail(f"{character_id}: character_id mismatch", errors)
    if index_item.get("path") != f"{character_id}/character.json":
        fail(f"{character_id}: index path mismatch", errors)
    if index_item.get("canon_version") != character.get("canon_version"):
        fail(f"{character_id}: character index canon version is stale", errors)
    if index_item.get("status") != character.get("status"):
        fail(f"{character_id}: character index status is stale", errors)
    if character.get("status") != "locked":
        fail(f"{character_id}: production character must be locked", errors)
    if character.get("identity", {}).get("name") != index_item.get("name"):
        fail(f"{character_id}: index name mismatch", errors)
    if not character.get("locked_visual"):
        fail(f"{character_id}: locked_visual is empty", errors)
    if len(character.get("forbidden_drift", [])) < 10:
        fail(f"{character_id}: forbidden_drift needs at least ten safeguards", errors)

    reference_ids = character.get("reference_assets", [])
    catalog_ids = [item["id"] for item in catalog.get("assets", [])]
    manifest_ids = [item["id"] for item in manifest.get("assets", [])]
    if reference_ids != catalog_ids or catalog_ids != manifest_ids:
        fail(f"{character_id}: character, catalog, and manifest asset IDs differ", errors)
    if len(set(catalog_ids)) != len(catalog_ids):
        fail(f"{character_id}: asset IDs are not unique", errors)
    if not catalog.get("assets") or catalog["assets"][0].get("status") != "locked":
        fail(f"{character_id}: first asset must be the locked master", errors)
    if catalog.get("canon_version") != character.get("canon_version"):
        fail(f"{character_id}: asset catalog canon version mismatch", errors)
    if manifest.get("canon_version") != character.get("canon_version"):
        fail(f"{character_id}: asset manifest canon version mismatch", errors)
    for item in manifest.get("assets", []):
        if item.get("width", 0) < 1000 or item.get("height", 0) < 700:
            fail(f"{character_id}: asset resolution too small: {item.get('id')}", errors)
        if len(item.get("sha256", "")) != 64:
            fail(f"{character_id}: invalid SHA-256: {item.get('id')}", errors)

    if prompts.get("character_id") != character_id:
        fail(f"{character_id}: prompt character mismatch", errors)
    if prompts.get("canon_version") != character.get("canon_version"):
        fail(f"{character_id}: prompt canon version mismatch", errors)
    for key in ("invariant", "style", "negative"):
        if len(prompts.get(key, "")) < 100:
            fail(f"{character_id}: prompt {key} is too short", errors)
    if index_item.get("name", "").lower() not in prompts.get("invariant", "").lower():
        fail(f"{character_id}: invariant prompt omits character name", errors)

    locked = character.get("locked_visual", {})
    if character_id == "drew":
        if locked.get("permanent_accessory") != "solid black bow tie":
            fail("drew: bow-tie rule mismatch", errors)
        if "S-curve" not in locked.get("neck", ""):
            fail("drew: neck lock missing", errors)
        if "wing-arms" not in locked.get("arms", ""):
            fail("drew: wing-arm rule missing", errors)
    if character_id == "abby":
        if "human-style" not in locked.get("eyes", "") or "sclera" not in locked.get("eyes", ""):
            fail("abby: human-style eye lock missing", errors)
        if "none" not in locked.get("tail", ""):
            fail("abby: no-tail lock missing", errors)
        neckpiece = locked.get("neckpiece", "")
        if "pearls" not in neckpiece or "gemstone" not in neckpiece:
            fail("abby: pearl-and-gemstone lock missing", errors)

    return len(catalog_ids)


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED_ROOT:
        if not (ROOT / relative).is_file():
            fail(f"missing root file: {relative}", errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    index = load_json(ROOT / "characters" / "index.json")
    entries = index.get("characters", [])
    ids = [item.get("id") for item in entries]
    if not entries:
        fail("character index is empty", errors)
    if len(ids) != len(set(ids)):
        fail("character index contains duplicate IDs", errors)

    asset_count = 0
    for item in entries:
        asset_count += validate_character(item, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    names = ", ".join(f"{item['name']} {item['canon_version']}" for item in entries)
    print(f"Bible validation passed for {names} ({asset_count} assets total).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
