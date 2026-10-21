#!/usr/bin/env python3
"""Rebuild this Std-only certificate and record source-bound assurance evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone


ROOT = Path(__file__).resolve().parent
ALLOWED_AXIOMS = {"propext", "Quot.sound", "Classical.choice"}
REQUIRED_THEOREMS = {
    "CornerSlide.demote_valid_iff",
    "CornerSlide.counterexample_source",
    "CornerSlide.counterexample_target_invalid",
    "CornerSlide.bubble_tableau_valid",
    "CornerSlide.extract_bubble_inverse_height_two",
    "CornerSlide.bubble_tableau_injective",
    "CornerSlide.graph_inversions_comparable_swap",
    "CornerSlide.tableau_graph_inversions_eq_word",
    "CornerSlide.bubble_tableau_graph_inversions",
    "CornerSlide.collision_without_height_two",
}


def run(lake: str, arguments: list[str]) -> dict:
    result = subprocess.run(
        [lake, *arguments], cwd=ROOT, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False,
    )
    record = {
        "command": ["lake", *arguments],
        "exit_code": result.returncode,
        "output": result.stdout,
    }
    if result.returncode:
        sys.stderr.write(result.stdout)
        raise SystemExit(f"Command failed: lake {' '.join(arguments)}")
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    lake = shutil.which("lake")
    if lake is None:
        fallback = Path.home() / ".elan/bin/lake"
        if not fallback.is_file():
            raise SystemExit("An installed Lean 4.34.0 toolchain and lake are required.")
        lake = str(fallback)

    source = (ROOT / "CornerSlide.lean").read_text()
    forbidden = re.findall(r"\b(?:sorry|admit|sorryAx|unsafe|native_decide|axiom)\b", source)
    if forbidden:
        raise SystemExit(f"Forbidden proof tokens in source: {sorted(set(forbidden))}")

    commands = [run(lake, ["env", "lean", "--version"])]
    if "version 4.34.0," not in commands[0]["output"]:
        raise SystemExit("This certificate is pinned to Lean 4.34.0.")
    commands.append(run(lake, ["build"]))
    commands.append(run(lake, ["env", "lean", "CornerSlide.lean"]))
    output = commands[-1]["output"]
    axioms = {}
    for name, values in re.findall(r"'([^']+)' depends on axioms: \[([^]]*)\]", output):
        axioms[name] = [value.strip() for value in values.split(",") if value.strip()]
    for name in re.findall(r"'([^']+)' does not depend on any axioms", output):
        axioms[name] = []
    if REQUIRED_THEOREMS - axioms.keys():
        raise SystemExit(f"Missing axiom reports: {sorted(REQUIRED_THEOREMS - axioms.keys())}")
    disallowed = {a for values in axioms.values() for a in values} - ALLOWED_AXIOMS
    if disallowed:
        raise SystemExit(f"Unexpected axioms: {sorted(disallowed)}")
    if "warning:" in output or "error:" in output:
        raise SystemExit("Direct source check returned a diagnostic; inspect it before recording success.")

    filenames = ["CornerSlide.lean", "lean-toolchain", "lakefile.toml", "lake-manifest.json"]
    report = {
        "schema_version": 1,
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed",
        "scope": "Actual tableau validity, height-two bubbling injection, and graph-inversion preservation; no symmetric-function coefficient bridge.",
        "sha256": {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in filenames},
        "source_forbidden_token_scan": "passed",
        "axioms": axioms,
        "commands": commands,
    }
    rendered = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output is not None:
        args.output.write_text(rendered)
        print(f"Verified {len(axioms)} printed theorem reports; saved {args.output}.")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
