#!/usr/bin/env python3
"""Rebuild the ETH-consequences Lean library freshly and record a verification certificate.

The script copies the sources into a temporary workspace, reuses only the pinned dependency
build products under .lake/packages, rebuilds with warnings treated as errors, prints the
axioms of every public theorem, and writes verification.json with source hashes, dependency
revisions and the axiom report. It never installs a toolchain or fetches dependencies.

Toolchain discovery: `lake` on PATH (elan or a bare Lean release directory). The checker
must report Lean 4.34.1.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parent
TOOLCHAIN = "leanprover/lean4:v4.34.1"
MATHLIB_REV = "d13f23b723b8a846827a245b89c10fc7d3f11612"
ALLOWED_AXIOMS = {"propext", "Quot.sound", "Classical.choice"}
MODULES = ["ParityInterpolation", "BooleanDifferences", "Separation", "HermiteUniqueness",
           "RankBarrier", "SubcubeObstruction", "IndependentSets", "PointDependentBarrier",
           "SlabDesign", "StressDuality", "GradedCounting"]
SOURCES = ["EthConsequences.lean", *[f"EthConsequences/{m}.lean" for m in MODULES]]
CONFIGURATION = ["lean-toolchain", "lakefile.toml", "lake-manifest.json"]
THEOREMS = [
    "ParityInterpolation.S_of_le",
    "ParityInterpolation.S_succ",
    "ParityInterpolation.defect_eq",
    "ParityInterpolation.alternating_sum_bounds",
    "ParityInterpolation.abs_defect_le",
    "BooleanDifferences.mobius_insert",
    "BooleanDifferences.mobius_inversion",
    "BooleanDifferences.boolean_differences",
    "Separation.sum_prod_eq_sum_measurements",
    "Hermite.eq_zero_of_jets_vanish",
    "Hermite.eq_of_jets_eq",
    "RankBarrier.card_le_rank_of_principal_identity",
    "RankBarrier.rank_le_of_ker_le",
    "RankBarrier.barrier",
    "RankBarrier.count_le_count_add_hammingDist",
    "RankBarrier.barrier_threshold",
    "Subcube.eval_zero_eq_sum",
    "Subcube.no_good_subcube",
    "Subcube.card_good_directions_lt",
    "Subcube.subcube_identity",
    "IndependentSets.card_indepSets_eq_card_satAssignments",
    "IndependentSets.card_indepSets_size_eq",
    "PointBarrier.rank_add_le",
    "PointBarrier.card_le_sum_rank",
    "PointBarrier.map_eval_zero_eq_sum",
    "PointBarrier.point_dependent_barrier",
    "PointBarrier.label_barrier",
    "PointBarrier.label_barrier_explicit",
    "SlabDesign.G_edge",
    "SlabDesign.natDegree_G_le",
    "SlabDesign.G_eval_zero",
    "SlabDesign.exists_gamma",
    "SlabDesign.slab_edge_good",
    "SlabDesign.slab_eval_zero",
    "SlabDesign.slab_natDegree",
    "SlabDesign.slab_design_bound",
    "Stress.moment_collapse",
    "Stress.sum_edgeW",
    "Stress.stress_total_eq_zero",
    "Stress.product_edge_good",
    "Stress.natDegree_product_le",
    "Stress.product_eval_zero",
    "Graded.sum_pow_eq",
    "Graded.histogram_identity",
    "Graded.coeff_histogram",
    "Graded.deformation_identity",
    "Graded.weight_identity",
]
FORBIDDEN = re.compile(r"\b(?:sorry|admit|sorryAx|unsafe|native_decide|axiom)\b")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dependency_revisions() -> dict:
    manifest = json.loads((ROOT / "lake-manifest.json").read_text())
    revisions = {}
    for package in manifest["packages"]:
        if package.get("type") != "git":
            raise RuntimeError("Only revision-pinned Git dependencies are supported.")
        name, expected = package["name"], package["rev"]
        path = ROOT / ".lake/packages" / name
        if not path.is_dir():
            raise RuntimeError(f"Missing dependency {name}; provision it explicitly first.")
        actual = subprocess.run(["git", "rev-parse", "HEAD"], cwd=path, text=True,
                                capture_output=True, check=True).stdout.strip()
        if actual != expected:
            raise RuntimeError(f"Dependency {name} is at {actual}, expected {expected}.")
        revisions[name] = actual
    if revisions.get("mathlib") != MATHLIB_REV:
        raise RuntimeError("Mathlib does not match the accepted revision.")
    return revisions


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "verification.json")
    args = parser.parse_args()
    commands: list[dict] = []
    inputs = {name: ROOT / name for name in [*SOURCES, *CONFIGURATION, "verify.py"]}
    report: dict = {"schema_version": 1,
                    "checked_at_utc": datetime.now(timezone.utc).isoformat(),
                    "status": "failed"}
    try:
        lake = shutil.which("lake")
        if lake is None:
            raise RuntimeError("`lake` for Lean 4.34.1 must be on PATH.")
        hashes = {name: digest(path) for name, path in inputs.items()}
        for name in SOURCES:
            found = FORBIDDEN.findall(inputs[name].read_text())
            if found:
                raise RuntimeError(f"Forbidden proof tokens in {name}: {sorted(set(found))}")
        if (ROOT / "lean-toolchain").read_text().strip() != TOOLCHAIN:
            raise RuntimeError("Toolchain pin changed.")
        revisions = dependency_revisions()
        inventory = "import EthConsequences\n" + "\n".join(
            f"#print axioms EthConsequences.{name}" for name in THEOREMS) + "\n"
        env = os.environ.copy()
        env["MATHLIB_NO_CACHE_ON_UPDATE"] = "1"

        def run(arguments: list[str], workspace: Path, strict: bool = True) -> str:
            started = time.perf_counter()
            result = subprocess.run([lake, *arguments], cwd=workspace, env=env, text=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                    check=False, timeout=1800)
            commands.append({"command": ["lake", *arguments], "exit_code": result.returncode,
                             "elapsed_seconds": round(time.perf_counter() - started, 3),
                             "output": result.stdout[-20000:]})
            if result.returncode or (strict and re.search(r"\b(?:warning|error):", result.stdout)):
                raise RuntimeError("Check failed or produced a diagnostic: lake " + " ".join(arguments))
            return result.stdout

        with tempfile.TemporaryDirectory(prefix="eth-consequences-certificate-") as temporary:
            workspace = Path(temporary) / "problems/eth/lean"
            workspace.mkdir(parents=True)
            for name, path in inputs.items():
                target = workspace / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(path, target)
            (workspace / ".lake").mkdir()
            (workspace / ".lake/packages").symlink_to((ROOT / ".lake/packages").resolve(),
                                                      target_is_directory=True)
            version = run(["env", "lean", "--version"], workspace)
            if "version 4.34.1," not in version:
                raise RuntimeError("Unexpected checker version: " + version.strip())
            run(["--wfail", "build"], workspace)
            (workspace / "StatementInventory.lean").write_text(inventory)
            output = run(["env", "lean", "StatementInventory.lean"], workspace, strict=False)

        axioms = {name: [a.strip() for a in values.split(",") if a.strip()]
                  for name, values in re.findall(r"'([^']+)' depends on axioms: \[([^]]*)\]", output)}
        for name in re.findall(r"'([^']+)' does not depend on any axioms", output):
            axioms[name] = []
        required = {"EthConsequences." + name for name in THEOREMS}
        if required - axioms.keys():
            raise RuntimeError(f"Missing axiom reports: {sorted(required - axioms.keys())}")
        if {a for values in axioms.values() for a in values} - ALLOWED_AXIOMS:
            raise RuntimeError("Nonstandard axiom in dependency reports.")
        if any(digest(path) != hashes[name] for name, path in inputs.items()):
            raise RuntimeError("Source changed during verification.")
        report.update(
            status="passed", toolchain=TOOLCHAIN, sha256=hashes,
            dependency_revisions=revisions, theorems=sorted(required), axioms=axioms,
            clean_build={"fresh_temporary_workspace": True,
                         "project_build_products_reused": False,
                         "pinned_dependency_products_reused": True,
                         "warnings_as_errors": True},
            scope=("Kernel-checked statements: Newton parity interpolation and its off-window "
                   "defect (closed form and bound); Boolean-lattice Mobius inversion and the "
                   "Boolean-differences identity of Lemma 3.3 (Mobius-coefficient form); the "
                   "measurement-separation identity of Lemma 3.2 (algebraic core); uniqueness of "
                   "Hermite interpolation; the isoperimetric rank barrier for any auxiliary pair "
                   "(M0, C) with the Hamming support condition, including its threshold form; the "
                   "R-subcube obstruction for point-dependent cube designs; the independent-set "
                   "to 2-CNF counting bijection (all sizes and fixed size). Translations between "
                   "these statements and the preprint, and binomial-tail estimates, are informal; "
                   "see problems/eth/subresults. Added 2026-10-29: the rank barrier for arbitrary "
                   "point-dependent designs (SR-03), global formulas, low Fourier degree of "
                   "symmetric polynomials and the slab construction with its 1/R bound (SR-04), "
                   "soundness of stress certificates and products of designs (SR-05), and the "
                   "graded-counting identities (SR-07)."))
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
        report["failure"] = str(error)
    report["commands"] = commands
    rendered = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered)
    print(f"ETH-consequences certificate {report['status']}.", file=sys.stderr)
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
