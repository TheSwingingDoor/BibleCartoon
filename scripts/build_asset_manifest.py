#!/usr/bin/env python3
"""Build or verify deterministic SHA-256 manifests for character assets."""

from __future__ import annotations

import argparse
import hashlib
import json
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS_DIR = ROOT / "characters" / "drew" / "assets"
CATALOG_PATH = ASSETS_DIR / "asset-catalog.json"
MANIFEST_PATH = ASSETS_DIR / "asset-manifest.json"


def png_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        signature = handle.read(24)
    if len(signature) < 24 or signature[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"not a valid PNG: {path}")
    return struct.unpack(">II", signature[16:24])


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def build_manifest() -> dict:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    output = {
        "schema_version": "1.0.0",
        "character_id": catalog["character_id"],
        "canon_version": catalog["canon_version"],
        "assets": [],
    }
    seen_ids: set[str] = set()
    for item in catalog["assets"]:
        asset_id = item["id"]
        if asset_id in seen_ids:
            raise ValueError(f"duplicate asset id: {asset_id}")
        seen_ids.add(asset_id)
        path = ASSETS_DIR / item["path"]
        if not path.is_file():
            raise FileNotFoundError(f"missing catalog asset: {path.relative_to(ROOT)}")
        width, height = png_dimensions(path)
        output["assets"].append(
            {
                "id": asset_id,
                "path": item["path"],
                "role": item["role"],
                "status": item["status"],
                "prompt_id": item["prompt_id"],
                "bytes": path.stat().st_size,
                "width": width,
                "height": height,
                "sha256": sha256(path),
            }
        )
    return output


def serialize(data: dict) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify instead of writing")
    args = parser.parse_args()
    try:
        expected = serialize(build_manifest())
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"manifest error: {exc}", file=sys.stderr)
        return 1
    if args.check:
        if not MANIFEST_PATH.exists():
            print("manifest error: asset-manifest.json does not exist", file=sys.stderr)
            return 1
        if MANIFEST_PATH.read_text(encoding="utf-8") != expected:
            print("manifest error: asset-manifest.json is stale", file=sys.stderr)
            return 1
        print("Asset manifest is current.")
        return 0
    MANIFEST_PATH.write_text(expected, encoding="utf-8")
    print(f"Wrote {MANIFEST_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
