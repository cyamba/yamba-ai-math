"""Regression checks of the exact restricted KR1 endpoint and its failure gate."""
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'research/rogers-ramanujan/checks'))
import separated_pairs as sp


class SeparatedPairTests(unittest.TestCase):
    def test_first_counterexample_preserves_weight_but_is_rejected(self):
        source = sp.SeparatedCluster(1, 1, (0,), (1,))
        output = sp.literal_compile(source)
        self.assertEqual(output, (4, 3, 3))
        self.assertEqual(sum(output), source.weight)
        self.assertEqual(len(output), source.dimension)
        self.assertFalse(sp.is_gap(output))
        with self.assertRaises(ValueError):
            sp.compile_separated(source)

    def test_sharp_boundary_in_both_pair_phases(self):
        for m, threshold in [(0, 0), (1, 2), (2, 3), (3, 5), (4, 6), (5, 8)]:
            c = sp.SeparatedCluster(2, 2, (threshold+7, threshold), (m, 0))
            out = sp.compile_separated(c)
            self.assertEqual(sp.extract_separated(out), c)
            if threshold:
                bad = sp.SeparatedCluster(2, 2, (threshold+7, threshold-1), (m, 0))
                self.assertFalse(sp.is_gap(sp.literal_compile(bad)))

    def test_empty_and_pure_blocks(self):
        for c in [sp.SeparatedCluster(0, 0, (), ()),
                  sp.SeparatedCluster(3, 0, (10, 5, 0), ()),
                  sp.SeparatedCluster(0, 3, (), (9, 2, 2))]:
            out = sp.compile_separated(c)
            self.assertEqual(sp.extract_separated(out), c)
            self.assertEqual(sum(out), c.weight)

    def test_nonseparated_valid_gap_is_outside_the_restricted_image(self):
        # The existing broad cluster merge handles this crossed pair/single case.
        target = (5, 4, 1)
        self.assertTrue(sp.is_gap(target))
        self.assertEqual(tuple(k for k, _ in sp.split_atoms(target)), ('P', 'S'))
        self.assertFalse(sp.is_separated(target))
        with self.assertRaises(ValueError):
            sp.extract_separated(target)

    def test_malformed_coordinates_and_targets_are_rejected(self):
        for args in [(True, 0, (0,), ()), (1, 0, (), ()),
                     (2, 0, (0, 1), ()), (0, 1, (), (-1,)),
                     (0, 1, (), (1.0,))]:
            with self.assertRaises(ValueError):
                sp.SeparatedCluster(*args)
        for target in [(4, 3, 3), (1, 2), (True,), (0,), (2, 2)]:
            self.assertFalse(sp.is_gap(target))
            with self.assertRaises(ValueError):
                sp.extract_separated(target)

    def test_independent_small_target_coverage_and_two_inverses(self):
        for n in range(23):
            sources = [c for c in sp.clusters(n) if c.admitted]
            images = {sp.compile_separated(c) for c in sources}
            targets = {p for p in sp.gap_partitions(n) if sp.is_separated(p)}
            self.assertEqual(len(images), len(sources))
            self.assertEqual(images, targets)
            for target in targets:
                self.assertEqual(sp.compile_separated(sp.extract_separated(target)), target)

    def test_positive_series_matches_explicit_mixed_sector(self):
        series = sp.separated_series(1, 1, 22)
        observed = [sum(c.a == c.b == 1 and c.admitted for c in sp.clusters(n))
                    for n in range(23)]
        self.assertEqual(series, observed)
        self.assertEqual([series[n] for n in (7, 10, 12, 16)], [1, 1, 2, 3])

    def test_full_compiler_gate_fails_even_under_optimized_python(self):
        process = subprocess.run([
            sys.executable, '-O',
            str(ROOT/'research/rogers-ramanujan/separated-2026-10-27/audit.py'),
            '--maximum', '10', '--require-full-compiler'],
            capture_output=True, text=True, timeout=15, cwd=ROOT)
        self.assertEqual(process.returncode, 2, process.stdout+process.stderr)
        self.assertIn('first_invalid_literal_output', process.stdout)


if __name__ == '__main__':
    unittest.main()
