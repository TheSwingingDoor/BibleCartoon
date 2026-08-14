.PHONY: manifest validate

manifest:
	python scripts/build_asset_manifest.py

validate:
	python scripts/build_asset_manifest.py --check
	python scripts/validate_bible.py
