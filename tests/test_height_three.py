"""Meaningful regression checks for the P012 exact signed-space experiment."""
from collections import Counter
import itertools
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from research.partitions.checks import height_three as h3
from research.partitions.checks import tableaux as tab
from research.partitions.checks import forest_triples as forest


class SignedSpaceTests(unittest.TestCase):
    def test_complete_prefix_enumerator_against_existing_permutation_oracle(self):
        for n in range(1, 5):
            for h in tab.hessenberg_vectors(n):
                for shape in tab.partitions(n, 3):
                    actual = set(h3.filling_generator(h, shape, h3.Budget()))
                    self.assertEqual(actual, set(tab.tableaux(h, shape)))

    def test_raw_multiplicity_zero_factors_and_negative_indices(self):
        terms = tuple(h3.determinant_terms((3, 3)))
        self.assertEqual(len(terms), 6)
        same = [s for s in terms if h3.contributes(s, (3, 2, 1))]
        self.assertEqual(len(same), 2)
        self.assertEqual(sum(s.sign for s in same), -2)
        zero = [s for s in terms if h3.contributes(s, (3, 3))]
        self.assertEqual(len(zero), 1)
        self.assertIn(0, zero[0].indices)
        negative = [s for s in h3.determinant_terms((3,)) if min(s.indices) < 0]
        self.assertTrue(negative)
        self.assertTrue(all(not h3.contributes(s, (3,)) for s in negative))

    def test_complete_wang_sectors_including_sorting_boundary(self):
        for n in range(7, 25):
            raw = h3.sectors(n)
            counts = Counter()
            for s in raw:
                counts[s.shape] += s.sign
                self.assertTrue(all(i > 0 for i in s.indices))
            self.assertEqual(dict(counts), h3.wang_sectors(n))
        self.assertEqual([len(h3.sectors(n)) for n in (7, 8, 9, 10)], [2, 3, 4, 5])
        self.assertEqual([s.sigma for s in h3.sectors(8) if s.shape == (3, 3, 2)], [(0, 2, 1)])

    def test_protocol_cases_really_have_height_three_and_selectors_are_distinct(self):
        self.assertEqual(len(set(h3.development())), 8)
        self.assertTrue(all(h3.height(h) == 3 for h in h3.development() + h3.HELDOUT))
        self.assertFalse(set(h3.development()) & set(h3.HELDOUT))
        self.assertEqual(len(set(h3.SELECTORS)), 12)

    def test_doubled_first_differences_and_complete_move_symmetry(self):
        h = (2, 3, 4, 5, 7, 7, 7)
        self.assertEqual(h3.height(h), 3)
        states, census = h3.enumerate_signed(h, h3.Budget())
        self.assertTrue(census["nonnegative_lower_differences"])
        self.assertTrue(states)
        universe = set(states)
        for source in states:
            groups = h3.legal_targets(h, source, h3.sectors(7), h3.Budget())
            for kind, group in enumerate(groups):
                for dest in group:
                    self.assertIn(dest, universe)
                    self.assertEqual(dest.sign, -source.sign)
                    self.assertEqual(dest.degree, source.degree)
                    self.assertTrue(tab.validates(h, dest.rows, dest.shape))
                    self.assertIn(source, h3.legal_targets(h, dest, h3.sectors(7), h3.Budget())[kind])
        self.assertTrue(all(s.degree <= census["edges"] // 2 for s in states))

    def test_reciprocity_required_even_without_negative_collisions(self):
        # A valid directed choice can fail recovery without a negative collision.
        a = h3.State((1,), (0,), ((1,),), 1, 0)
        b = h3.State((1,), (0,), ((1,),), 0, 1)
        c = h3.State((1,), (0,), ((2,),), 1, 0)
        endpoints = {a: ((b, b), (), ()), b: ((c, c), (), ()), c: ((b, b), (), ())}
        self.assertEqual(h3.choose(endpoints[a], 0), b)
        self.assertNotEqual(h3.choose(endpoints[b], 0), a)

    def test_budget_exhaustion_is_not_a_complete_negative_census(self):
        with self.assertRaises(h3.Capped):
            list(h3.filling_generator((1,), (1,), h3.Budget(extensions=0)))
        with self.assertRaises(h3.Capped):
            h3.Budget(candidates=0).tick("candidates")
        with self.assertRaises(h3.Capped):
            h3.Budget(round_seconds=0).check()
        with self.assertRaises(h3.Capped):
            h3.Budget(memory_bytes=0).check()
        case = h3.run_case(h3.development()[0], h3.Budget(extensions=0))
        self.assertEqual(case["status"], "capped")
        self.assertNotIn("moves", case)

    def test_failed_candidate_extractions_are_charged(self):
        budget = h3.Budget()
        h3.bubble_neighbors((1, 2, 3), ((1,), (2,), (3,)), budget)
        self.assertEqual(budget.candidates, 3)

    def test_no_overwrite_of_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "evidence.json"
            h3.write_report(path, {"status": "capped"})
            with self.assertRaises(ValueError):
                h3.write_report(path, {"status": "success"})
            with patch.dict(h3.LIMITS, artifact_bytes=path.stat().st_size + 1):
                with self.assertRaises(h3.Capped):
                    h3.write_report(path.with_name("second.json"), {"status": "capped"})

    def test_invalid_target_and_hypotheses(self):
        with self.assertRaises(ValueError):
            h3.target(6)
        with self.assertRaises(ValueError):
            h3.target(True)
        with self.assertRaises(ValueError):
            h3.enumerate_signed((7,) * 7, h3.Budget())


class ForestTripleTests(unittest.TestCase):
    def test_complete_forest_coefficients_against_independent_colorings(self):
        for n in range(1, 5):
            for h in tab.hessenberg_vectors(n):
                expected = h3.oracle.elementary_expansion(h)
                for lam in h3.oracle.partitions(n):
                    result = forest.coefficient(h, lam, h3.Budget())
                    poly = expected.get(lam, ())
                    padded = list(poly) + [0] * (len(tab.graph_edges(h)) + 1 - len(poly))
                    self.assertEqual(result["coefficient"], padded)

    def test_decreasing_forests_are_distinct_and_exhaustive_on_clique(self):
        actual = tuple(forest.forests((4, 4, 4, 4), 4, h3.Budget()))
        self.assertEqual(len(actual), 24)  # product(1 + number of larger neighbors)
        self.assertEqual(len(set(actual)), 24)
        for parents in actual:
            self.assertEqual(sorted(v for w in forest.tree_words(parents) for v in w), [1, 2, 3, 4])
            self.assertTrue(all(p == 0 or p > i for i, p in enumerate(parents, 1)))

    def test_tree_frontier_reads_smallest_eligible_vertex(self):
        self.assertEqual(forest.tree_words((4, 3, 4, 0)), ((1, 4, 3, 2),))

    def test_repeated_parts_do_not_label_identical_compositions_twice(self):
        assignments = list(forest.composition_assignments((7,), (3, 3, 1), h3.Budget()))
        self.assertEqual(len(assignments), 3)
        self.assertEqual(len(set(assignments)), 3)
        with self.assertRaises(h3.Capped):
            list(forest.forests((2, 2), 1, h3.Budget(extensions=0)))

    def test_comparison_requires_complete_development_obstruction(self):
        with self.assertRaises(ValueError):
            forest.obstruction_case({"cases": []})
        with self.assertRaises(ValueError):
            forest.obstruction_case({"cases": [{"split": "heldout", "status": "complete",
                                               "h": [1], "moves": {"isolated_negative": {"degree": 0}}}]})

    def test_reproduction_may_rebind_input_hash_but_not_change_experiment(self):
        original = {"input_sha256": "old receipt", "h": [2, 2], "diagnostic": "rank-step"}
        self.assertTrue(forest.same_protocol_spec(original, original | {"input_sha256": "new receipt"}))
        self.assertFalse(forest.same_protocol_spec(original, original | {"h": [1, 2]}))


if __name__ == "__main__":
    unittest.main()
