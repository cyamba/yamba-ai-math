"""P015 semantic invariants and resource gates, not a unimodality proof."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from research.partitions.checks import forest_exchange as ex
from research.partitions.checks import forest_surgery as fs
from research.partitions.checks import forest_transport as tr
from research.partitions.checks import forest_triples as ft
from research.partitions.checks import height_three as h3


class ForestExchangeTests(unittest.TestCase):
    def test_retained_hall_compositions_have_distinct_exact_exchange_inverses(self):
        geo = fs.Geometry(ex.DEVELOPMENT[-1])
        prior = json.loads((tr.PHASE / "evidence.json").read_text())["round_two"]["verification"]
        targets = set()
        for value in prior["negatives"]:
            source = tr.state_from_record(geo, value)
            dest = ex.transpose(geo, source, 2, 3)
            self.assertIsNotNone(dest)
            self.assertEqual(dest.parents, (2, 4, 5, 6, 7, 0, 8, 0))
            self.assertEqual(dest.compositions, source.compositions)
            self.assertEqual(dest.marks, (1, 1))
            self.assertEqual((dest.inversion, dest.epsilon, dest.degree, dest.sign), (2, 1, 3, 1))
            self.assertEqual(ex.transpose(geo, dest, 2, 3).record(), source.record())
            self.assertEqual(ex.adjacent_defect(geo, source, 2), (-1, 0))
            targets.add(dest)
        self.assertEqual(len(targets), 2)

    def test_payloads_follow_vertex_sets_when_component_minima_reorder(self):
        geo = fs.Geometry((4, 4, 4, 4))
        source = geo.build((0, 3, 0, 0), {
            frozenset((1,)): ((1,), 1), frozenset((2, 3)): ((1, 1), 1),
            frozenset((4,)): ((1,), 1)}, 1)
        dest = ex.transpose(geo, source, 1, 2)
        self.assertIsNotNone(dest)
        self.assertEqual(dest.compositions, ((1, 1), (1,), (1,)))
        self.assertEqual(geo.payload(dest)[frozenset((1, 3))], ((1, 1), 1))
        self.assertEqual(ex.transpose(geo, dest, 1, 2).record(), source.record())
        with self.assertRaisesRegex(ValueError, "Component order changes"):
            ex.adjacent_defect(geo, source, 1)

    def test_invalid_edges_and_same_component_are_rejected(self):
        geo = fs.Geometry((2, 3, 4, 4))
        source = geo.build((2, 0, 4, 0), {
            frozenset((1, 2)): ((2,), 1), frozenset((3, 4)): ((2,), 1)}, 0)
        self.assertIsNone(ex.transpose(geo, source, 1, 2))
        self.assertIsNone(ex.transpose(geo, source, 1, 4))
        with self.assertRaises(ValueError):
            ex.transpose(geo, source, 0, 2)

    def test_fixed_label_exchange_invariants_on_small_nonclique_forests(self):
        accepted = 0
        for h in h3.tab.hessenberg_vectors(4):
            geo = fs.Geometry(h)
            for parents in ft.forests(h, 4, h3.Budget()):
                words, _ = geo.data(parents)
                payload = {frozenset(w): ((len(w),), 1) for w in words}
                for epsilon in (0, 1):
                    source = geo.build(parents, payload, epsilon)
                    for a in range(1, 4):
                        for b in range(a+1, 5):
                            dest = ex.transpose(geo, source, a, b)
                            if dest is None:
                                continue
                            accepted += 1
                            self.assertEqual((dest.sign, dest.degree), (-source.sign, source.degree))
                            self.assertEqual(sorted(map(sum, dest.compositions)), sorted(map(sum, source.compositions)))
                            self.assertEqual(ex.transpose(geo, dest, a, b).record(), source.record())
        self.assertGreater(accepted, 0)

    def test_adjacent_defect_formula_includes_distinguishing_neighbors(self):
        nonzero_defects = 0
        for h in h3.tab.hessenberg_vectors(4):
            geo = fs.Geometry(h)
            for parents in ft.forests(h, 4, h3.Budget()):
                words, inversion = geo.data(parents)
                source = geo.build(parents, {frozenset(w): ((len(w),), 1) for w in words}, 0)
                for a in range(1, 4):
                    try:
                        delta, defect = ex.adjacent_defect(geo, source, a)
                    except ValueError:
                        continue
                    nonzero_defects += defect > 0
                    moved = tuple(a+1 if v == a else a if v == a+1 else v for w in words for v in w)
                    positions = {v: i for i, v in enumerate(moved)}
                    actual = sum(positions[v] < positions[u] for u, v in geo.edges)
                    self.assertEqual(delta, actual-inversion)
        self.assertGreater(nonzero_defects, 0)

    def test_candidate_budget_is_charged_before_transposition(self):
        geo = fs.Geometry(ex.DEVELOPMENT[0])
        with patch.object(ex, "transpose", side_effect=AssertionError("must not execute")):
            with self.assertRaises(h3.Capped):
                list(ex.exchange_operations(geo, None, h3.Budget(candidates=0)))

    def test_old_hall_certificate_is_rejected_for_the_enlarged_grammar(self):
        geo = fs.Geometry(ex.DEVELOPMENT[-1])
        prior = json.loads((tr.PHASE / "evidence.json").read_text())["round_two"]["verification"]
        diagnostic = copy.deepcopy(prior); diagnostic["status"] = "Hall deficiency"
        with self.assertRaisesRegex(ValueError, "Complete-neighborhood deficiency failed"):
            ex.verify_failure(geo, diagnostic, h3.Budget())

    def test_incomplete_development_cannot_lock_selector(self):
        selectors = [dict(id=i, unpaired=0) for i in range(4)]
        complete = dict(status="complete", moves=dict(selectors=selectors))
        self.assertTrue(ex.selection_decision([complete])["eligible"])
        incomplete = ex.selection_decision([complete, dict(status="capped")])
        self.assertFalse(incomplete["eligible"])
        self.assertIsNone(incomplete["candidate_selector"])

    def test_exhausted_case_and_existing_output_do_not_execute_enumeration(self):
        with patch.object(fs, "enumerate_states", side_effect=AssertionError("must not execute")):
            case = ex.run_case(ex.DEVELOPMENT[0], h3.Budget(candidates=0))
        self.assertEqual(case["status"], "capped")
        self.assertNotIn("signed_space", case)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/"result.json"; path.write_text("preserve me")
            with patch.object(ex, "verify_protocol", side_effect=AssertionError("must not execute")):
                with self.assertRaisesRegex(ValueError, "before execution"):
                    ex.run_round(1, path)
            self.assertEqual(path.read_text(), "preserve me")

    def test_fresh_heldout_metadata_excludes_every_prior_split(self):
        excluded = set(h3.development()+h3.HELDOUT+fs.DEVELOPMENT+fs.heldout()+tr.DEVELOPMENT+tr.heldout())
        values = ex.heldout()
        self.assertEqual(tuple(map(len, values)), (9, 10))
        self.assertFalse(set(values) & excluded)
        self.assertTrue(all(h3.height(h) == 3 for h in values))

    def test_component_sets_are_unique_and_ordered_by_minima(self):
        partitions = tuple(ex.component_sets(4, 3, h3.Budget()))
        self.assertEqual(len(partitions), 14)
        self.assertEqual(len(set(partitions)), 14)
        for blocks in partitions:
            self.assertEqual(tuple(map(min, blocks)), tuple(sorted(map(min, blocks))))
            self.assertEqual(sorted(v for block in blocks for v in block), [1, 2, 3, 4])

    def test_component_product_check_uses_no_forest_enumeration(self):
        geo = fs.Geometry((2, 3, 3))
        with patch.object(ft, "forests", side_effect=AssertionError("independent method")):
            first = ex.partword_block_polynomial(geo, (1, 2), h3.Budget())
            second = ex.partword_block_polynomial(geo, (2, 1), h3.Budget())
        self.assertEqual(first["coefficient"], (0, 1))
        self.assertEqual(second["coefficient"], ())
        with self.assertRaises(ValueError):
            ex.partword_block_polynomial(geo, (2, 2), h3.Budget())

    def test_capacity_readout_keeps_different_partwords_separate(self):
        geo = fs.Geometry(ex.DEVELOPMENT[0])
        negative = geo.build((2, 3, 0, 5, 6, 7, 0), {
            frozenset((1, 2, 3)): ((3,), 1), frozenset((4, 5, 6, 7)): ((3, 1), 1)}, 0)
        positive = geo.build((2, 3, 4, 5, 6, 7, 0), {
            frozenset(range(1, 8)): ((3, 1, 3), 1)}, 0)
        census = ex.partword_census((negative, positive), len(geo.edges), h3.Budget())
        self.assertEqual(sum(s["signed"][0] for s in census["sectors"]), 0)
        self.assertEqual(census["minimum_deficit"]["partword"], (3, 3, 1))
        self.assertEqual(census["minimum_deficit"]["signed"], -1)


if __name__ == "__main__":
    unittest.main()
