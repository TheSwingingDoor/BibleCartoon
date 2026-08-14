#!/usr/bin/env python3
"""Dependency-free structural validation for the Drew character bible."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DREW = ROOT / "characters" / "drew"

REQUIRED_ROOT = [
    "README.md",
    "AGENTS.md",
    "RIGHTS.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "schema/character.schema.json",
    "characters/index.json",
]

REQUIRED_DREW = [
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


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED_ROOT:
        if not (ROOT / relative).is_file():
            fail(f"missing root file: {relative}", errors)
    for relative in REQUIRED_DREW:
        if not (DREW / relative).is_file():
            fail(f"missing Drew file: {relative}", errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    character = load_json(DREW / "character.json")
    prompts = load_json(DREW / "prompts.json")
    catalog = load_json(DREW / "assets" / "asset-catalog.json")
    manifest = load_json(DREW / "assets" / "asset-manifest.json")
    index = load_json(ROOT / "characters" / "index.json")

    if character.get("character_id") != "drew":
        fail("character_id must be drew", errors)
    if character.get("canon_version") != "1.0.0":
        fail("unexpected Drew canon version", errors)
    if character.get("status") != "locked":
        fail("Drew must be locked", errors)
    identity = character.get("identity", {})
    if identity.get("age") != 46 or identity.get("gender") != "male":
        fail("Drew identity age/gender mismatch", errors)
    if identity.get("species") != "anthropomorphic flamingo":
        fail("Drew species mismatch", errors)
    locked = character.get("locked_visual", {})
    if locked.get("permanent_accessory") != "solid black bow tie":
        fail("Drew bow-tie rule mismatch", errors)
    if "wing-arms" not in locked.get("arms", ""):
        fail("Drew wing-arm rule missing", errors)
    if len(character.get("forbidden_drift", [])) < 10:
        fail("forbidden_drift needs at least ten explicit safeguards", errors)

    reference_ids = character.get("reference_assets", [])
    catalog_ids = [item["id"] for item in catalog.get("assets", [])]
    manifest_ids = [item["id"] for item in manifest.get("assets", [])]
    if reference_ids != catalog_ids or catalog_ids != manifest_ids:
        fail("character, catalog, and manifest asset IDs differ", errors)
    if len(set(catalog_ids)) != len(catalog_ids):
        fail("asset IDs are not unique", errors)
    if not catalog.get("assets") or catalog["assets"][0].get("status") != "locked":
        fail("first asset must be the locked master", errors)
    for item in manifest.get("assets", []):
        if item.get("width", 0) < 1000 or item.get("height", 0) < 700:
            fail(f"asset resolution too small: {item.get('id')}", errors)
        if len(item.get("sha256", "")) != 64:
            fail(f"invalid SHA-256: {item.get('id')}", errors)

    if prompts.get("canon_version") != character.get("canon_version"):
        fail("prompt canon version mismatch", errors)
    if "S-curved neck" not in prompts.get("invariant", ""):
        fail("prompt invariant omits neck lock", errors)
    if "solid black bow tie" not in prompts.get("invariant", ""):
        fail("prompt invariant omits bow tie", errors)
    indexed = {item["id"]: item for item in index.get("characters", [])}
    if indexed.get("drew", {}).get("canon_version") != character.get("canon_version"):
        fail("character index is stale", errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Bible validation passed for Drew {character['canon_version']} ({len(catalog_ids)} assets).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
