#!/usr/bin/env python3
"""Build or verify deterministic SHA-256 manifests for all indexed characters."""

from __future__ import annotations

import argparse
import hashlib
import json
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "characters" / "index.json"


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


def load_index() -> list[dict]:
    data = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    return data["characters"]


def build_manifest(character_id: str) -> dict:
    assets_dir = ROOT / "characters" / character_id / "assets"
    catalog_path = assets_dir / "asset-catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    if catalog.get("character_id") != character_id:
        raise ValueError(f"catalog character mismatch: {catalog_path.relative_to(ROOT)}")
    output = {
        "schema_version": "1.0.0",
        "character_id": character_id,
        "canon_version": catalog["canon_version"],
        "assets": [],
    }
    seen_ids: set[str] = set()
    for item in catalog["assets"]:
        asset_id = item["id"]
        if asset_id in seen_ids:
            raise ValueError(f"duplicate asset id: {asset_id}")
        seen_ids.add(asset_id)
        path = assets_dir / item["path"]
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
    parser.add_argument("--character", help="process one indexed character ID")
    args = parser.parse_args()
    try:
        indexed = load_index()
        ids = [item["id"] for item in indexed]
        if args.character:
            if args.character not in ids:
                raise ValueError(f"character is not indexed: {args.character}")
            ids = [args.character]
        for character_id in ids:
            expected = serialize(build_manifest(character_id))
            manifest_path = ROOT / "characters" / character_id / "assets" / "asset-manifest.json"
            if args.check:
                if not manifest_path.exists():
                    raise FileNotFoundError(
                        f"asset manifest does not exist: {manifest_path.relative_to(ROOT)}"
                    )
                if manifest_path.read_text(encoding="utf-8") != expected:
                    raise ValueError(
                        f"asset manifest is stale: {manifest_path.relative_to(ROOT)}"
                    )
                print(f"Asset manifest is current for {character_id}.")
            else:
                manifest_path.write_text(expected, encoding="utf-8")
                print(f"Wrote {manifest_path.relative_to(ROOT)}")
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"manifest error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
