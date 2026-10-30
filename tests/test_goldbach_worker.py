"""Focused checks for the deterministic Goldbach harness adapter."""
from __future__ import annotations
import importlib.util
from pathlib import Path
import unittest

WORKER = Path(__file__).resolve().parents[1] / 'research' / 'goldbach' / 'checks' / 'deterministic_worker.py'
spec = importlib.util.spec_from_file_location('goldbach_deterministic_worker', WORKER)
worker = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(worker)


class GoldbachDeterministicWorkerTests(unittest.TestCase):
    def test_exact_cube_root_around_cubes(self):
        for k in range(1, 30):
            self.assertEqual(worker.floor_cuberoot(k**3), k)
            self.assertEqual(worker.floor_cuberoot(k**3 - 1), k - 1)

    def test_trial_division_quarter_root_boundary_ties(self):
        result = worker.counterexamples()
        self.assertIn(8, result['ties'])
        self.assertIn(12, result['ties'])

    def test_sieve_and_trial_division_agree(self):
        spf = worker.smallest_factors(201)
        for x in range(2, 202):
            self.assertEqual(worker.factors_trial(x), worker.factors_sieve(x, spf))

    def test_cube_counts_match_independent_factorization(self):
        spf = worker.smallest_factors(300)
        for n in range(6, 301, 2):
            z = worker.floor_cuberoot(n)
            trial = worker.pair_classes(n, z, worker.factors_trial)
            sieved = worker.pair_classes(n, z, lambda x: worker.factors_sieve(x, spf))
            self.assertEqual(trial, sieved)

    def test_exact_reflection_and_shared_progression(self):
        result = worker.finite_checks()
        self.assertEqual(result['cube_targets'], 998)
        self.assertEqual(result['exact_reflection_identity_failures'], 0)
        self.assertEqual(result['adjacent_progression_failures'], 0)
        self.assertEqual(result['adjacent_progression_targets'], 66)

    def test_revision_reads_list_upstream_without_claiming_proof(self):
        packet = {'upstream': [{'step_id': 'counterexample'}, {'step_id': 'finite-check'}]}
        response = worker.response('revise', packet)
        self.assertIn('counterexample, finite-check', response['summary'])
        self.assertIn('remains unproved', response['summary'])


if __name__ == '__main__':
    unittest.main()
