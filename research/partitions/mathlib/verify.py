#!/usr/bin/env python3
"""Rebuild bridge proofs from source, reusing only pinned dependency products."""

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
MODULES = ["Foundations", "Coloring", "Alternant", "Vandermonde", "SubsetBridge",
           "ElementaryProduct", "Reconstruction", "ColorSymmetry", "ColorCoefficients",
           "SignedCancellation",
           "PermutationSign", "ArrayColorBridge", "FamilyPadding", "FamilyReindex", "SurvivorAlgebra", "DominantShape", "ChromaticArrays", "FiniteH3", "AlphabetSpecialization", "H3",
           "NaturalCoefficients"]
SOURCES = ["PartitionH3.lean", *[f"PartitionH3/{m}.lean" for m in MODULES]]
CONFIGURATION = ["lean-toolchain", "lakefile.toml", "lake-manifest.json"]
STD_SOURCES = ["CornerSlide.lean", "TableauFamilies.lean", "WeightedCancellation.lean",
               "AlternantSubsets.lean", "SignedArrays.lean"]
DECLARATIONS = [
    "chromatic", "elementary", "tableauCoefficient", "survivorCoefficient",
    "elementary_zero", "elementary_isSymmetric", "chromatic_empty", "chromatic_zero_alphabet",
    "edge_iff_incomparable", "same_color_comparable", "colorClass_card_le_two",
    "reverseColors_involutive", "proper_reverseColors_iff", "ascents_reverseColors",
    "descents_reverseColors", "descents_eq_colorRowInversions",
    "alternant", "alternant_eq_sum", "powerMonomial_mul_elementary",
    "alternant_mul_elementary", "alternant_eq_zero_of_eq", "delta_injective",
    "coeff_signed_delta", "vandermonde_delta_coefficient", "vandermonde_ne_zero",
    "vandermonde_cancel", "vandermonde_empty", "subsetBits_ones", "subsetBits_injective",
    "subsetBits_fromBits", "fromBits_subsetBits", "twoBlockSubset_card",
    "twoBlockSubset_classification",
    "bump_prefix_adjacent_collision", "alternant_bump_prefix_eq_zero",
    "vandermonde_mul_elementary", "bump_prefix_twoBlockSubset",
    "prefix_alternant_mul_elementary", "vandermonde_mul_two_elementary",
    "vandermonde_mul_two_elementary_empty", "vandermonde_mul_two_elementary_zero",
    "rename_antisymmetrize", "alternant_isAlternating", "alternating_coefficient_eq_zero_of_eq",
    "alternating_eq_of_dominant_coeff", "dominant_permutation_eq_iff",
    "alternant_dominant_coefficient", "vandermonde_mul_isAlternating",
    "dominantReconstruction_isAlternating", "dominantReconstruction_coefficient",
    "alternating_reconstruction",
    "toggleColors_involutive", "swap_lt_outside", "proper_toggleColors_iff",
    "middle_of_two_edges", "path_internal_edges", "toggleColors_ascents",
    "unflipped_balanced", "colorMonomial_toggleColors", "chromatic_adjacent_swap",
    "isSymmetric_of_adjacent", "chromatic_isSymmetric",
    "colorMonomial_eq_powerMonomial", "weightedChromatic_power_coefficient", "coeff_rename_at",
    "vandermonde_weighted_coefficient", "chromaticDesc_eq_rename_reverse",
    "chromaticDesc_eq_chromatic", "shifted_color_shape", "vandermonde_chromatic_coefficient",
    "mem_finiteLists", "mem_signedArrayUniverse", "signedArrayWeight_move",
    "signedArray_moved_sum_zero", "signedArray_sum_eq_fixed", "signedArray_sum_eq_padded",
    "signedArray_universe_cancellation", "heightTwo_natLt_noThreeChain",
    "natural_signed_array_cancellation",
    "ofFn_adjacent_swap",
    "permutationLabels_adjacent_sign",
    "permutationSign_permutationLabels",
    "colorRows_contents",
    "colorArray_chain",
    "shapeAt_iff_get",
    "colorArray_signed_iff",
    "colorArray_sign",
    "colorArray_inverse",
    "colorArray_injective",
    "signedColorUniverse_image",
    "signedArray_sum_reindex",
    "graphScore_natLt",
    "colorArray_inversions",
    "rows_padding_decomposition",
    "padded_rows_iff_complete_family",
    "tableauGraphInversions_padding",
    "paddedIdentityArray_mem",
    "paddedSignedArrays_eq_image",
    "sum_toFinset_map",
    "signedArray_sum_eq_complete_family",
    "list_weight_coefficient",
    "natLt_asymm",
    "tableauCoefficient_eq_next_add_survivor",
    "tableauCoefficient_after_last",
    "survivorCoefficient_eq_sub",
    "sum_differences_mul_prefix",
    "vandermonde_mul_survivorExpansion",
    "dominant_ge_delta",
    "dominantPartition_partition",
    "delta_add_dominantPartition",
    "delta_add_partition_strictAnti",
    "twoColumnPartition_partition",
    "twoColumnShape_strictAnti",
    "bounded_partition_three_blocks",
    "partition_range_three_blocks",
    "twoColumnPartition_range",
    "fixed_signedArray_shape",
    "range_map_eq_iff",
    "twoColumn_exponent_eq_iff",
    "chromatic_signedArray_coefficient",
    "chromatic_twoColumn_coefficient",
    "chromatic_other_partition_coefficient_zero",
    "tableauAlternantExpansion_isAlternating",
    "tableauAlternantExpansion_twoColumn_coefficient",
    "vandermonde_mul_chromatic_eq_tableauAlternantExpansion",
    "height_two_survivor_expansion_large_alphabet",
    "liftColor_injective",
    "proper_liftColor",
    "specialize_colorMonomial_lift",
    "specialize_colorMonomial_zero",
    "specialize_chromatic",
    "specialize_elementary",
    "specialize_survivorExpansion",
    "height_two_survivor_expansion",
    "coefficientCast_injective", "naturalCast_injective", "naturalCast_colorMonomial",
    "naturalCast_chromatic", "naturalCast_elementary", "coefficientCast_tableauWeight",
    "coefficientCast_survivorCoefficient", "height_two_survivor_expansion_nat",
]
REQUIRED = {"PartitionH3." + name for name in DECLARATIONS
            if name not in {"chromatic", "elementary", "tableauCoefficient",
                            "survivorCoefficient", "alternant"}}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require_dependencies(elan: str) -> dict:
    listing = subprocess.run([elan, "toolchain", "list"], text=True, capture_output=True, check=True)
    if TOOLCHAIN not in {line.split()[0] for line in listing.stdout.splitlines()}:
        raise RuntimeError(f"Missing installed toolchain {TOOLCHAIN}; verifier never installs it.")
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
        dirty = subprocess.run(["git", "status", "--porcelain", "--untracked-files=no"],
                               cwd=path, text=True, capture_output=True, check=True).stdout
        if actual != expected or dirty:
            raise RuntimeError(f"Dependency {name} differs from its pinned clean source.")
        revisions[name] = actual
    if revisions.get("mathlib") != MATHLIB_REV:
        raise RuntimeError("Mathlib does not match the accepted revision.")
    return revisions


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    commands = []
    inputs = {name: ROOT / name for name in [*SOURCES, *CONFIGURATION, "verify.py"]}
    inputs.update({"../lean/" + name: ROOT.parent / "lean" / name for name in STD_SOURCES})
    report = {"schema_version": 1, "checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "status": "failed", "h3_status": "incomplete", "final_h3_declaration": None,
              "natural_h3_declaration": None}
    try:
        lake = shutil.which("lake") or str(Path.home() / ".elan/bin/lake")
        elan = shutil.which("elan") or str(Path.home() / ".elan/bin/elan")
        if not Path(lake).is_file() or not Path(elan).is_file():
            raise RuntimeError("Installed elan and the pinned Lean toolchain are required.")
        hashes = {name: digest(path) for name, path in inputs.items()}
        for name in [*SOURCES, *["../lean/" + n for n in STD_SOURCES]]:
            forbidden = re.findall(r"\b(?:sorry|admit|sorryAx|unsafe|native_decide|axiom)\b",
                                   inputs[name].read_text())
            if forbidden:
                raise RuntimeError(f"Forbidden proof tokens in {name}: {sorted(set(forbidden))}")
        if (ROOT / "lean-toolchain").read_text().strip() != TOOLCHAIN:
            raise RuntimeError("Bridge toolchain pin changed.")
        revisions = require_dependencies(elan)
        inventory = "import PartitionH3\n" + "\n".join(
            f"#check @PartitionH3.{name}" for name in DECLARATIONS) + "\n"
        env = os.environ.copy()
        env["MATHLIB_NO_CACHE_ON_UPDATE"] = "1"
        env["ELAN_TOOLCHAIN"] = TOOLCHAIN

        def run(arguments: list[str], workspace: Path) -> None:
            started = time.perf_counter()
            result = subprocess.run([lake, *arguments], cwd=workspace, env=env, text=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                    check=False, timeout=600)
            commands.append({"command": ["lake", *arguments], "exit_code": result.returncode,
                             "elapsed_seconds": round(time.perf_counter() - started, 3),
                             "output": result.stdout})
            if result.returncode or re.search(r"\b(?:warning|error):", result.stdout):
                raise RuntimeError("Source check failed or returned a diagnostic: lake " +
                                   " ".join(arguments))

        with tempfile.TemporaryDirectory(prefix="partition-mathlib-certificate-") as temporary:
            workspace = Path(temporary) / "research/partitions/mathlib"
            workspace.mkdir(parents=True)
            for name, path in inputs.items():
                target = workspace / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(path, target)
            (workspace / ".lake").mkdir()
            (workspace / ".lake/packages").symlink_to((ROOT / ".lake/packages").resolve(),
                                                      target_is_directory=True)
            run(["env", "lean", "--version"], workspace)
            if "version 4.34.1," not in commands[-1]["output"]:
                raise RuntimeError("Unexpected checker version.")
            run(["--no-cache", "--wfail", "build"], workspace)
            for module in MODULES:
                run(["env", "lean", f"PartitionH3/{module}.lean"], workspace)
            (workspace / "StatementInventory.lean").write_text(inventory)
            run(["env", "lean", "StatementInventory.lean"], workspace)

        output = "\n".join(c["output"] for c in commands[2:-1])
        axioms = {name: [a.strip() for a in values.split(",") if a.strip()]
                  for name, values in re.findall(
                      r"'([^']+)' depends on axioms: \[([^]]*)\]", output)}
        for name in re.findall(r"'([^']+)' does not depend on any axioms", output):
            axioms[name] = []
        if REQUIRED - axioms.keys():
            raise RuntimeError(f"Missing dependency reports: {sorted(REQUIRED - axioms.keys())}")
        if {a for values in axioms.values() for a in values} - ALLOWED_AXIOMS:
            raise RuntimeError("Nonstandard axiom in bridge dependency reports.")
        if any(digest(path) != hashes[name] for name, path in inputs.items()):
            raise RuntimeError("Source changed during verification.")
        if require_dependencies(elan) != revisions:
            raise RuntimeError("Dependency revisions changed during verification.")
        report.update(status="passed", h3_status="lean_checked",
                      final_h3_declaration="PartitionH3.height_two_survivor_expansion",
                      natural_h3_declaration="PartitionH3.height_two_survivor_expansion_nat",
                      sha256=hashes, dependency_revisions=revisions,
                      statement_inventory_source=inventory, axioms=axioms,
                      clean_build={"fresh_temporary_workspace": True,
                                   "project_build_products_reused": False,
                                   "pinned_dependency_products_reused": True},
                      scope="Actual finite coloring/subset/tableau polynomial definitions; color-class "
                            "bounds, actual adjacent-color symmetry and signed integer coefficient "
                            "extraction; alternant multiplication, vanishing, Vandermonde cancellation, "
                            "two-elementary specialization and actual-support reconstruction; complete "
                            "finite signed-array cancellation; complete coloring/array and padding/family bijections; "
                            "unconditional height-two survivor expansion for every finite alphabet, including zero; "
                            "actual natural-coefficient sums and injective coefficient transport. "
                            "Semantic review is recorded separately.")
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
        report["failure"] = str(error)
    report["commands"] = commands
    rendered = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    else:
        print(rendered, end="")
    print(f"Bridge certificate {report['status']}; H3: {report['h3_status']}.", file=sys.stderr)
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
