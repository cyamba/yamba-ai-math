"""Read-only lexical inventory of a pinned external certificate; never builds it."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile


PIN = "adc7f1241b42e322a6451854ab7e4b4c146bf78a"
MAIN_BLOB = "12abe371e589d0b2ca4548b3c90631afb030aa7f"
ENTRY = "OAI.Combinatorics.Chromatic.Main"
KEY_FILES = [
    "LICENSE", "lean/lean-toolchain", "lean/lakefile.lean",
    "lean/OAI/Combinatorics/Chromatic/Main.lean",
    "lean/OAI/Combinatorics/Chromatic/Model.lean",
    "lean/OAI/Combinatorics/Chromatic/Witness/ElementaryAlphabetRigidity.lean",
    "lean/OAI/Combinatorics/Chromatic/Witness/HistoryMainWitness.lean",
    "lean/OAI/Combinatorics/Chromatic/Witness/ElementaryProductDegree.lean",
]


def git(root: Path, *arguments: str) -> str:
    return subprocess.check_output(["git", "-C", str(root), *arguments], text=True).strip()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.source_root.resolve()
    if git(root, "rev-parse", "HEAD") != PIN or git(root, "status", "--porcelain"):
        raise SystemExit("Inventory requires the clean, pinned upstream checkout.")
    main_bytes = (root / KEY_FILES[3]).read_bytes()
    main_blob = hashlib.sha1(b"blob " + str(len(main_bytes)).encode() + b"\0" + main_bytes).hexdigest()
    if main_blob != MAIN_BLOB:
        raise SystemExit("Main.lean differs from the official GitHub blob inspected at this pin.")
    pending = [ENTRY]
    seen = set()
    local = {}
    external = set()
    line_count = 0
    while pending:
        module = pending.pop()
        if module in seen:
            continue
        seen.add(module)
        relative = "lean/" + module.replace(".", "/") + ".lean"
        path = root / relative
        if not path.is_file():
            if module.startswith("OAI."):
                raise SystemExit(f"Missing local import: {module}")
            external.add(module)
            continue
        data = path.read_bytes()
        source = data.decode()
        local[relative] = hashlib.sha256(data).hexdigest()
        line_count += len(source.splitlines())
        for line in source.splitlines():
            match = re.match(r"^import\s+(.+)", line)
            if match:
                pending.extend(match[1].split("--", 1)[0].split())
    manifest = "".join(f"{path}\0{digest}\n" for path, digest in sorted(local.items()))
    configuration = (root / "lean/lakefile.lean").read_text()
    mathlib = re.search(r'require mathlib from git\s+"[^"]+" @ "([0-9a-f]+)"', configuration)
    usage = shutil.disk_usage(tempfile.gettempdir())
    report = {
        "schema_version": 1,
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "source inventory only; external build not attempted",
        "official_repository": "https://github.com/openai/math",
        "commit": PIN,
        "official_main_git_blob_verified": MAIN_BLOB,
        "license": "Apache-2.0; official LICENSE header inspected",
        "toolchain": (root / "lean/lean-toolchain").read_text().strip(),
        "mathlib_commit": mathlib[1] if mathlib else None,
        "local_mathlib_checkout_present": (root / "lean/.lake/packages/mathlib").is_dir(),
        "lexical_inventory": {
            "entry_module": ENTRY,
            "local_file_count": len(local),
            "local_line_count": line_count,
            "external_import_modules": sorted(external),
            "sorted_path_nul_sha256_newline_manifest_sha256": hashlib.sha256(manifest.encode()).hexdigest(),
            "limitation": "Line-based import traversal, not a compiler dependency or semantic audit.",
        },
        "inspected_file_sha256": {
            path: hashlib.sha256((root / path).read_bytes()).hexdigest() for path in KEY_FILES
        },
        "available_temporary_filesystem_bytes": usage.free,
        "build_process_seconds": 0,
        "build_attempts": 0,
        "provisioning_or_build_download_bytes": 0,
        "new_toolchains_or_dependencies_installed": [],
        "decision": "Conservatively defer provisioning with limited free disk, absent required toolchain and local mathlib. The 15 GiB storage ceiling is not a demonstrated minimum requirement.",
        "formal_build_assurance": "unverified",
        "mathematical_assurance": "partial source inspection only",
    }
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(f"Inventoried {len(local)} local files and {line_count} lines; no external build attempted.")


if __name__ == "__main__":
    main()
