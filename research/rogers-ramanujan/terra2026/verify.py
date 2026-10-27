#!/usr/bin/env python3
"""Reproduce selected KR1 research checks with exact source hashes and logs.

Python 3.11+ standard library; Lean 4.34.0 for the four formal certificates.
Finite checks do not certify a full KR1 bijection. This runner never downloads
dependencies, changes Lean sources, or uses enumeration to define a bijection.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone


ROOT = Path(__file__).resolve().parent
LEAN_NAMES = ("Blocks", "Cancellation", "Entropy", "MergeBounds")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def execute(name: str, argv: list[str], out: Path, sources: list[Path]) -> dict:
    started = time.monotonic()
    try:
        process = subprocess.run(
            argv, cwd=ROOT, text=True, capture_output=True, timeout=600,
            encoding="utf-8", errors="replace",
        )
        code = process.returncode
        output = process.stdout + process.stderr
    except (OSError, subprocess.TimeoutExpired) as error:
        code = -1
        output = repr(error) + "\n"
    logfile = out / (name + ".log")
    logfile.write_text(output, encoding="utf-8")
    row = {
        "name": name,
        "command": argv,
        "cwd": str(ROOT),
        "returncode": code,
        "seconds": round(time.monotonic() - started, 6),
        "log": logfile.name,
        "log_sha256": digest(logfile),
        "source_sha256": {
            str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path): digest(path)
            for path in sources
        },
    }
    if name.startswith("lean-") and name != "lean-version":
        row["sorryAx_in_output"] = "sorryAx" in output
        if row["sorryAx_in_output"] and code == 0:
            row["returncode"] = -2
    print(f"{name}: {'PASS' if row['returncode'] == 0 else 'FAIL'}", flush=True)
    if output.strip():
        print(output.strip(), flush=True)
    return row


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", help="path to the Lean 4.34.0 executable")
    parser.add_argument("--only", choices=("all", "lean", "python"), default="all")
    parser.add_argument("--full", action="store_true",
                        help="also repeat the 3,178,008-state independent word check")
    parser.add_argument("--out", type=Path, default=ROOT / "verification-local")
    args = parser.parse_args()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    report = {
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Selected universal Lean lemmas and finite mathematical regressions",
        "full_kr1_bijection": False,
        "full_word_encoding_formalized": False,
        "novelty_verified": False,
        "runner_sha256": digest(Path(__file__).resolve()),
        "python": sys.version,
        "mode": args.only,
        "full_finite_check_requested": args.full,
        "runs": [],
    }
    jobs = []
    if args.only in ("all", "lean"):
        lean = args.lean or shutil.which("lean")
        if not lean:
            parser.error("Lean is required; pass --lean /path/to/lean or --only python")
        resolved_lean = shutil.which(lean)
        if not resolved_lean:
            parser.error(f"Lean executable not found: {lean}")
        jobs.append(("lean-version", [resolved_lean, "--version"], []))
        report["lean_sources"] = {}
        for name in LEAN_NAMES:
            source = ROOT / "lean" / (name + ".lean")
            content = source.read_text(encoding="utf-8")
            report["lean_sources"][name] = {
                "sha256": digest(source),
                "theorem_declarations": len(re.findall(r"^\s*theorem\s", content, re.M)),
                "axiom_report_commands": len(re.findall(r"^\s*#print axioms\s", content, re.M)),
                "sorry_or_admit_token": bool(re.search(r"\b(sorry|admit)\b", content)),
                "added_axiom_declaration": bool(re.search(r"^\s*axiom\s", content, re.M)),
            }
            jobs.append(("lean-" + name, [resolved_lean, str(source)], [source]))
    if args.only in ("all", "python"):
        for name, relative in (
            ("local-surgery", "theory/local_surgery.py"),
            ("staircase-toggle", "theory/staircase_toggle.py"),
            ("lane-carries", "construction/check_lane_carries.py"),
            ("height-blocks", "construction/check_blocks.py"),
            ("recurrence-final", "construction/check_recurrence_final.py"),
        ):
            source = ROOT / relative
            sources = [source]
            if name in ("lane-carries", "height-blocks"):
                sources.append(ROOT.parent / "checks" / "kr1.py")
            jobs.append((name, [sys.executable, str(source)], sources))
        source = ROOT / "positive_coefficients.py"
        jobs.append(("positive-coefficients",
                     [sys.executable, str(source), "--output", str(out / "positive-coefficients.json")],
                     [source]))
        if args.full:
            source = ROOT / "construction" / "check_alln_word.py"
            jobs.append(("independent-word-full", [sys.executable, str(source)], [source]))
    for name, argv, sources in jobs:
        report["runs"].append(execute(name, argv, out, sources))
    report["passed"] = all(row["returncode"] == 0 for row in report["runs"])
    if "lean_sources" in report:
        report["passed"] = report["passed"] and not any(
            row["sorry_or_admit_token"] or row["added_axiom_declaration"]
            for row in report["lean_sources"].values()
        )
    report["finished_utc"] = datetime.now(timezone.utc).isoformat()
    (out / "verification.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Receipt: {out / 'verification.json'}", flush=True)
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
