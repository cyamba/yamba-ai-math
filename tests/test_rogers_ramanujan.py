"""Independent definitions and retained counterexamples for the KR1 attempt."""

from collections import Counter
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
CHECKS = ROOT / "research/rogers-ramanujan/checks"
SPEC = importlib.util.spec_from_file_location("kr1_research_checks", CHECKS / "kr1.py")
kr1 = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = kr1
SPEC.loader.exec_module(kr1)


class KR1DefinitionsTests(unittest.TestCase):
    def test_empty_partition_and_unique_empty_encoding(self):
        for generator in (kr1.gap_partitions, kr1.residue_partitions, kr1.weighted_partitions):
            self.assertEqual(list(generator(0)), [()])
        self.assertEqual(list(kr1.cluster_data(0)), [kr1.ClusterData(0, 0, (), ())])
        self.assertEqual(kr1.weighted_columns(()), ())
        self.assertEqual(kr1.decode_columns(()), ())

    def test_literal_gap_boundaries(self):
        for parts in ((), (1,), (1, 2), (3, 3), (1, 3), (1, 2, 4)):
            self.assertTrue(kr1.is_gap(parts), parts)
        for parts in ((0,), (2, 1), (1, 1), (2, 2), (2, 3), (1, 2, 3)):
            self.assertFalse(kr1.is_gap(parts), parts)

    def test_weighted_order_multiplicity_and_ordinary_size(self):
        self.assertTrue(kr1.is_weighted((1, 1, 1, 1)))
        self.assertFalse(kr1.is_weighted((1, 1, 1, 1, 1)))
        self.assertEqual(kr1.weighted_size((2, 1)), 4)
        self.assertEqual(kr1.weighted_size((1, 1, 1, 1)), 8)
        with self.assertRaises(ValueError):
            kr1.weighted_size((1, 2))

    def test_zero_padding_and_extreme_cluster_parameters(self):
        self.assertEqual(list(kr1.nonnegative_vectors(3, 0)), [(0, 0, 0)])
        self.assertEqual(list(kr1.nonnegative_vectors(0, 1)), [])
        self.assertEqual(kr1.ClusterData(0, 2, (), (0, 0)).weight, 12)
        self.assertEqual(kr1.ClusterData(2, 0, (0, 3), ()).weight, 7)
        self.assertEqual(kr1.ClusterData(1, 1, (0,), (2,)).weight, 13)
        for args in ((1, 0, (), ()), (0, 1, (), ()), (2, 0, (1, 0), ())):
            with self.assertRaises(ValueError):
                kr1.ClusterData(*args)

    def test_independent_generators_and_coefficient_oracles_through_twelve(self):
        product = kr1.residue_counts(12)
        clusters = kr1.cluster_counts(12)
        columns = kr1.flat_column_counts(12)
        for n in range(13):
            with self.subTest(n=n):
                gap = tuple(kr1.gap_partitions(n))
                self.assertEqual(set(gap), {p for p in kr1.ordinary_partitions(n) if kr1.is_gap(p)})
                residue = tuple(kr1.residue_partitions(n))
                self.assertEqual(set(residue), {p for p in kr1.ordinary_partitions(n) if kr1.is_residue(p)})
                weighted = tuple(kr1.weighted_partitions(n))
                brute = {p[::-1] for s in range(n + 1) for p in kr1.ordinary_partitions(s)
                         if kr1.is_weighted(p[::-1]) and kr1.weighted_size(p[::-1]) == n}
                self.assertEqual(set(weighted), brute)
                cluster = tuple(kr1.cluster_data(n))
                self.assertEqual((len(gap), len(residue), len(weighted), len(cluster)),
                                 (product[n],) * 4)
                self.assertEqual((clusters[n], columns[n]), (product[n], product[n]))
                self.assertEqual(Counter(map(len, gap)), Counter(c.gap_length for c in cluster))

    def test_column_round_trips_and_weight_through_twelve(self):
        for n in range(13):
            for parts in kr1.weighted_partitions(n):
                encoded = kr1.weighted_columns(parts)
                self.assertEqual(sum(encoded), n)
                self.assertEqual(kr1.decode_columns(encoded), parts)
                self.assertEqual(kr1.weighted_columns(kr1.decode_columns(encoded)), encoded)

    def test_column_tail_and_residue_boundaries(self):
        for h in range(101):
            self.assertEqual(kr1.inverse_prefix(kr1.prefix_weight(h)), h)
        for value in (2, 4, 5, 7):
            with self.assertRaises(ValueError):
                kr1.inverse_prefix(value)
        for columns in ((0,), (9,), (8, 9), (10, 1)):
            with self.assertRaises(ValueError):
                kr1.decode_columns(columns)
        self.assertEqual(kr1.decode_columns((9, 8)), (2, 2, 2, 2, 1))

    def test_refuted_projection_and_length_refinement(self):
        witnesses = kr1.first_projection_falsifiers(12)
        self.assertEqual(witnesses["invalid_projection"],
                         {"weight": 4, "input": (2, 1), "projection": (2, 2)})
        self.assertEqual(witnesses["projection_collision"],
                         {"weight": 6, "inputs": ((2, 2), (4, 1)), "projection": (2, 4)})
        self.assertEqual(witnesses["length_mismatch"],
                         {"weight": 6, "weighted_lengths": {1: 1, 2: 2, 3: 1},
                          "cluster_gap_lengths": {1: 1, 2: 3}})
        for t in range(1, 20):
            self.assertEqual(kr1.row_projection((4*t, t)), kr1.row_projection((2*t, 2*t)))

    def test_complete_frozen_rule_family_has_exact_collision_witnesses(self):
        self.assertEqual([p.name for p in kr1.RULE_PROFILES],
                         [f"{i:04b}" for i in range(16)])
        for profile in kr1.RULE_PROFILES:
            result = kr1.first_straightening_falsifier(12, profile)
            self.assertEqual(result["status"], "refuted_collision", profile.name)
            left, right = result["inputs"]
            self.assertNotEqual(left, right)
            self.assertEqual(kr1.weighted_size(left), result["weight"])
            self.assertEqual(kr1.weighted_size(right), result["weight"])
            self.assertEqual(kr1.column_straighten(left, profile=profile)[0], result["image"])
            self.assertEqual(kr1.column_straighten(right, profile=profile)[0], result["image"])
            self.assertTrue(kr1.is_gap(result["image"]))

    def test_normalization_validity_and_energy_bound_for_all_profiles(self):
        for n in range(13):
            for parts in kr1.weighted_partitions(n):
                for profile in kr1.RULE_PROFILES:
                    image, steps, trace = kr1.column_straighten(parts, profile=profile,
                                                               capture_trace=True)
                    self.assertEqual(sum(image), n)
                    self.assertTrue(kr1.is_gap(image))
                    self.assertEqual(len(trace), steps)
                    self.assertLessEqual(2 * steps, n * n)
                    for step in trace:
                        before, after = step["before"], step["after"]
                        self.assertEqual(sum(before), sum(after))
                        self.assertGreater(sum(p*p for p in after), sum(p*p for p in before))
                    self.assertFalse(kr1.column_straighten(parts, profile=profile)[2])

    def test_default_column_candidate_has_retained_weight_eight_collision(self):
        self.assertEqual(kr1.DEFAULT_PROFILE.name, "0111")
        result = kr1.first_straightening_falsifier(12)
        self.assertEqual((result["weight"], result["inputs"], result["image"]),
                         (8, ((4, 2), (8,)), (3, 5)))

    def test_invalid_weights_and_boolean_parts(self):
        for n in (-1, True, 1.5, "3"):
            with self.assertRaises(ValueError):
                list(kr1.weighted_partitions(n))
        self.assertFalse(kr1.is_gap((True,)))
        self.assertFalse(kr1.is_residue((True,)))
        self.assertFalse(kr1.is_weighted((True,)))

    def test_full_bijection_gate_fails_when_only_finite_checks_exist(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "receipt.json"
            result = subprocess.run(
                [sys.executable, str(CHECKS / "verify.py"), "--ceiling", "2",
                 "--require-bijection", "--output", str(output)],
                cwd=ROOT, capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 2, result.stderr)
            report = json.loads(output.read_text())
            self.assertEqual(report["status"], "finite_checks_passed_bridge_unresolved")
            self.assertIsNone(report["bridge"]["lean_certificate"])
            self.assertIn("actual W<->C", report["required_completion_failure"])
            self.assertTrue(report["source_sha256"])

    def test_finite_verifier_fails_closed_when_required_contract_is_missing(self):
        with tempfile.TemporaryDirectory() as directory:
            copied = Path(directory) / "research/rogers-ramanujan/checks"
            copied.mkdir(parents=True)
            for name in ("kr1.py", "verify.py"):
                shutil.copyfile(CHECKS / name, copied / name)
            result = subprocess.run([sys.executable, str(copied / "verify.py"),
                                     "--ceiling", "2"], cwd=directory,
                                    capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(json.loads(result.stdout)["status"], "failed")
            self.assertIn("required source unavailable", result.stdout)


if __name__ == "__main__":
    unittest.main()
