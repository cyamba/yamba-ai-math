"""Check saved Goldbach artifact identity, without validating mathematics."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


def verify_manifest(root: Path, manifest: Path) -> tuple[int, list[str]]:
    root = root.resolve()
    entries = json.loads(manifest.read_text(encoding="utf-8-sig"))["files"]
    if isinstance(entries, dict):
        entries = [
            {"path": name, "sha256": value if isinstance(value, str) else value["sha256"]}
            for name, value in entries.items()
        ]
    errors = []
    for entry in entries:
        name = entry["path"]
        target = (root / name).resolve()
        if not target.is_relative_to(root):
            errors.append(f"outside repository: {name}")
        elif not target.is_file():
            errors.append(f"missing: {name}")
        elif hashlib.sha256(target.read_bytes()).hexdigest() != entry["sha256"]:
            errors.append(f"hash mismatch: {name}")
    return len(entries), errors


def main() -> int:
    root = Path(__file__).resolve().parents[3]
    research = root / "research" / "goldbach"
    manifests = [research / "continuation-20261029" / "input-provenance.json"]
    manifests.extend(sorted(research.glob("*/artifact-manifest.json")))
    manifests.extend(sorted(research.glob("handoff-manifest-*.json")))
    checked = 0
    errors = []
    for manifest in manifests:
        count, failures = verify_manifest(root, manifest)
        checked += count
        errors.extend(failures)
    print(json.dumps({"manifests": len(manifests), "file_checks": checked,
                      "errors": errors, "research_validated": False}, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
