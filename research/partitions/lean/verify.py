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
import tempfile
import time
from datetime import datetime, timezone


ROOT = Path(__file__).resolve().parent
ALLOWED_AXIOMS = {"propext", "Quot.sound", "Classical.choice"}
SOURCES = ["CornerSlide.lean", "TableauFamilies.lean", "WeightedCancellation.lean", "SignedArrays.lean", "AlternantSubsets.lean", "MultidimensionalFerrers.lean"]
CONFIGURATION = ["lean-toolchain", "lakefile.toml", "lake-manifest.json"]
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
    "CornerSlide.mem_family",
    "CornerSlide.family_nodup",
    "CornerSlide.bubbleAt_family",
    "CornerSlide.bubbleAt_family_injective",
    "CornerSlide.bubbleAt_family_weight",
    "CornerSlide.degreewise_cancellation",
    "CornerSlide.two_column_degreewise_cancellation",
    "CornerSlide.height_two_degreewise_cancellation",
    "CornerSlide.finite_height_two_degreewise_cancellation",
    "CornerSlide.mem_survivorFamily",
    "CornerSlide.empty_vertex_degree_count",
    "CornerSlide.single_vertex_degree_count",
    "CornerSlide.survivorFamily_empty_source",
}
STATEMENT_DECLARATIONS = [
    "Tableau", "NoThreeChain", "demote_valid_iff", "flatten_before_after",
    "tableau_graph_inversions_eq_word", "bubble_tableau_valid",
    "bubble_tableau_graph_inversions", "extract_bubble_inverse_height_two",
    "bubble_tableau_injective", "mem_family", "family_nodup", "bubbleAt_family",
    "bubbleAt_family_injective", "bubbleAt_family_weight", "degreeCount",
    "degreewise_cancellation", "columnFamily", "mem_columnFamily",
    "survivorFamily", "mem_survivorFamily", "height_two_degreewise_cancellation",
    "finiteRelation", "finite_height_two_degreewise_cancellation",
    "empty_vertex_degree_count", "single_vertex_degree_count",
    "survivorFamily_empty_source",
]
SIGNED_DECLARATIONS = [
    "ChainArray", "SignedArray", "Partition", "PaddedTableau", "permutationSign",
    "shiftKey_injective", "adjacent_length_exclusion", "height_two_row_length_le_two",
    "togglePair_involution", "bottommost_pivot_stable", "move_involution",
    "move_signedArray", "move_tableauGraphInversions", "move_fixed_iff_good",
    "columns_iff_good", "signedArray_fixed_iff_padded", "fixed_labels_identity",
    "fixed_row_lengths", "move_sign_reversing", "signedArray_bad_sign_reversing",
    "fixed_permutationSign",
]
REQUIRED_THEOREMS.update(
    "SignedArrays." + name for name in SIGNED_DECLARATIONS[5:]
)
ALTERNANT_DECLARATIONS = [
    "NoRise", "ones", "exponent", "candidate", "noRise_iff_prefix",
    "adjacent_exponent_collision", "adjacent_exponent_weakly_decreasing",
    "candidate_length", "candidate_ones", "candidate_injective",
    "two_block_classification",
]
REQUIRED_THEOREMS.update(
    "AlternantSubsets." + name for name in ALTERNANT_DECLARATIONS[4:]
)
MULTIDIM_DECLARATIONS = [
    "NoLocalThreeChain", "promote32", "promote321", "hookBefore", "hookBubbleEnd", "hookBubbleMid", "kr1Q",
    "bubble_injective_local_fiber", "promote32_tableau_valid", "promote32_tableau_graph_inversions",
    "collision_witness_promoted_valid", "promote321_tableau_valid", "promote321_tableau_graph_inversions",
    "hookBubbleEnd_tableau_valid", "hookBubbleEnd_tableau_graph_inversions",
    "hookBubbleMid_tableau_valid", "hookBubbleMid_tableau_graph_inversions",
    "cascade_split_preserves_all", "kr1_scale3_self_similarity", "kr1_scale3_divisible",
    "kr1_head_offset_identity", "kr1_a3_core_weight", "kr1_a3_b0_octant_weight",
    "kr1_a3_b0_6d_cone_routing_weight", "kr1_higher_octant_weight", "kr1_a4_a5_a6_apex_weights",
]
REQUIRED_THEOREMS.update(
    "MultidimensionalFerrers." + name for name in MULTIDIM_DECLARATIONS[7:]
)


def run(lake: str, arguments: list[str], workspace: Path) -> dict:
    started = time.perf_counter()
    result = subprocess.run(
        [lake, *arguments], cwd=workspace, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False,
    )
    record = {
        "command": ["lake", *arguments],
        "exit_code": result.returncode,
        "elapsed_seconds": round(time.perf_counter() - started, 3),
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

    filenames = [*SOURCES, *CONFIGURATION, "verify.py"]
    hashes = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in filenames}
    for filename in SOURCES:
        source = (ROOT / filename).read_text()
        forbidden = re.findall(r"\b(?:sorry|admit|sorryAx|unsafe|native_decide|axiom)\b", source)
        if forbidden:
            raise SystemExit(f"Forbidden proof tokens in {filename}: {sorted(set(forbidden))}")

    inventory = "import WeightedCancellation\nimport SignedArrays\nimport AlternantSubsets\nimport MultidimensionalFerrers\n" + "\n".join(
        f"#check @CornerSlide.{name}" for name in STATEMENT_DECLARATIONS
    ) + "\n" + "\n".join(
        f"#check @SignedArrays.{name}" for name in SIGNED_DECLARATIONS
    ) + "\n" + "\n".join(
        f"#check @AlternantSubsets.{name}" for name in ALTERNANT_DECLARATIONS
    ) + "\n" + "\n".join(
        f"#check @MultidimensionalFerrers.{name}" for name in MULTIDIM_DECLARATIONS
    ) + "\n"
    with tempfile.TemporaryDirectory(prefix="partition-certificate-") as temporary:
        workspace = Path(temporary)
        for filename in [*SOURCES, *CONFIGURATION]:
            shutil.copyfile(ROOT / filename, workspace / filename)
        commands = [run(lake, ["env", "lean", "--version"], workspace)]
        if "version 4.34.0," not in commands[0]["output"]:
            raise SystemExit("This certificate is pinned to Lean 4.34.0.")
        commands.append(run(lake, ["build"], workspace))
        for filename in SOURCES:
            commands.append(run(lake, ["env", "lean", filename], workspace))
        (workspace / "StatementInventory.lean").write_text(inventory)
        commands.append(run(lake, ["env", "lean", "StatementInventory.lean"], workspace))
    output = "\n".join(command["output"] for command in commands[2:-1])
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
    if any("warning:" in command["output"] or "error:" in command["output"] for command in commands):
        raise SystemExit("Direct source check returned a diagnostic; inspect it before recording success.")
    if any(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != hashes[name] for name in filenames):
        raise SystemExit("Source changed during verification; rerun against the final sources.")

    report = {
        "schema_version": 2,
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed",
        "scope": "Actual tableaux, complete finite families, height-two injection and degreewise survivors; signed-array involution, integer shape/filling and inversion preservation, padded tableau fixed sector, identity labels and inversion-parity sign reversal; unique two-block Boolean subset classification and adjacent integer exponent collisions. No polynomial alternant identity, finite signed-sum theorem or coloring-to-elementary bridge.",
        "clean_build": {
            "fresh_temporary_workspace": True,
            "copied_files": [*SOURCES, *CONFIGURATION],
            "preexisting_build_artifacts": False,
            "external_lean_dependencies": [],
            "installed_toolchain_reused": "Lean 4.34.0 and its bundled Std",
        },
        "sha256": hashes,
        "statement_inventory_source": inventory,
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
