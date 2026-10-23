#!/usr/bin/env python3
"""Run repository checks and both fresh Lean certificates; never infer H3 closure."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
import uuid

ROOT = Path(__file__).resolve().parents[2]


def snapshot_sources(root: Path) -> dict[str, str]:
    result = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        cwd=root, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True,
    )
    snapshot = {}
    for raw in result.stdout.split(b"\0"):
        if not raw:
            continue
        name = raw.decode("utf-8", errors="surrogateescape")
        path = root / name
        if path.is_file():
            snapshot[name] = hashlib.sha256(path.read_bytes()).hexdigest()
    return snapshot


def run_suite(root: Path, artifacts: Path, *, runner=subprocess.run,
              snapshotter=snapshot_sources) -> dict:
    artifacts.mkdir(parents=True, exist_ok=True)
    report = {"schema_version": 1, "checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "status": "failed", "h3_status": "incomplete", "final_h3_declaration": None,
              "natural_h3_declaration": None,
              "checks": [], "certificates": {}}
    try:
        before = snapshotter(root)
    except (OSError, subprocess.SubprocessError) as error:
        report["failure"] = "Cannot bind checks to source: " + str(error)
        return report
    stages = [
        ("repository_tests", [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"]),
        ("repository_checker", [sys.executable, "scripts/check_repository.py"]),
        ("std_certificate", [sys.executable, "research/partitions/lean/verify.py", "--output",
                             str(artifacts / "std.json")]),
        ("mathlib_certificate", [sys.executable, "research/partitions/mathlib/verify.py", "--output",
                                 str(artifacts / "mathlib.json")]),
    ]
    for name, command in stages:
        started = time.perf_counter()
        record = {"name": name, "command": command, "status": "failed"}
        try:
            result = runner(command, cwd=root, text=True, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, check=False, timeout=900)
            record.update(exit_code=result.returncode, output=result.stdout,
                          status="passed" if result.returncode == 0 else "failed")
        except (OSError, subprocess.SubprocessError) as error:
            record["failure"] = str(error)
        record["elapsed_seconds"] = round(time.perf_counter() - started, 3)
        report["checks"].append(record)

    for name in ["std", "mathlib"]:
        path = artifacts / (name + ".json")
        try:
            certificate = json.loads(path.read_text())
            if not isinstance(certificate, dict) or certificate.get("status") != "passed":
                raise ValueError("Certificate did not record a passed fresh source check.")
            report["certificates"][name] = {
                "status": "passed", "path": str(path),
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "source_sha256": certificate.get("sha256", {}),
                "theorem_reports": len(certificate.get("axioms", {})),
                "h3_status": certificate.get("h3_status", "incomplete"),
                "final_h3_declaration": certificate.get("final_h3_declaration"),
                "natural_h3_declaration": certificate.get("natural_h3_declaration"),
            }
        except (OSError, ValueError) as error:
            report["certificates"][name] = {"status": "failed", "failure": str(error)}
    try:
        after = snapshotter(root)
        stable = before == after
        report.update(source_sha256=before, source_unchanged_during_checks=stable)
    except (OSError, subprocess.SubprocessError) as error:
        stable = False
        report["failure"] = "Cannot verify final source state: " + str(error)
    if (stable and all(c["status"] == "passed" for c in report["checks"])
            and all(c["status"] == "passed" for c in report["certificates"].values())):
        report["status"] = "passed"
        bridge = report["certificates"]["mathlib"]
        if (bridge["h3_status"] == "lean_checked" and bridge["final_h3_declaration"] ==
                "PartitionH3.height_two_survivor_expansion" and bridge["natural_h3_declaration"] ==
                "PartitionH3.height_two_survivor_expansion_nat"):
            report["h3_status"] = "lean_checked"
            report["final_h3_declaration"] = bridge["final_h3_declaration"]
            report["natural_h3_declaration"] = bridge["natural_h3_declaration"]
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=ROOT / ".runs/partition-verification/latest.json")
    args = parser.parse_args()
    artifacts = ROOT / ".runs/partition-verification" / uuid.uuid4().hex
    report = run_suite(ROOT, artifacts)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(f"Repository and certificates: {report['status']}. H3: {report['h3_status']}.")
    print(f"Source-bound report: {args.output}")
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
