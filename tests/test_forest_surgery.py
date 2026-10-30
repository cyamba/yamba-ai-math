"""P013 tests of representation, conditional surgery and honest failure receipts."""
from itertools import permutations
from pathlib import Path
import tempfile
import unittest

from research.partitions.checks import forest_surgery as fs
from research.partitions.checks import forest_triples as ft
from research.partitions.checks import height_three as h3


class ForestSurgeryTests(unittest.TestCase):
    def test_value_rank_maps_are_inverse_on_arbitrary_labels(self):
        for word in permutations((1, 3, 4, 6)):
            normalized, rank = fs.startmin(word)
            self.assertEqual(normalized[0], min(word))
            self.assertEqual(fs.startr(normalized, rank), word)
        self.assertEqual(fs.startmin((6, 1, 7, 4, 3)), ((1, 3, 7, 6, 4), 4))

    def test_tree_decoder_round_trips_every_small_decreasing_forest(self):
        for h in h3.tab.hessenberg_vectors(4):
            geo = fs.Geometry(h)
            for parents in ft.forests(h, 4, h3.Budget()):
                for word in ft.tree_words(parents):
                    decoded = geo.decode(word)
                    self.assertIsNotNone(decoded)
                    self.assertEqual(dict(decoded), {u: parents[u-1] for u in word})
        self.assertIsNone(fs.Geometry((2, 3, 3)).decode((1, 3, 2)))
        self.assertIsNone(fs.Geometry((3, 3, 3)).decode((2, 1, 3)))

    def test_checked_word_relation_is_reversible_on_small_clique(self):
        geo = fs.Geometry((4, 4, 4, 4))
        for parents in ft.forests(geo.h, 3, h3.Budget()):
            words, inv = geo.data(parents)
            for comps in ft.composition_assignments(tuple(map(len, words)), (2, 1, 1), h3.Budget()):
                from itertools import product
                for marks in product(*(range(1, a[0]+1) for a in comps)):
                    source = fs.State(parents, comps, marks, 0, inv)
                    for group in fs.neighbors(geo, source, h3.Budget()):
                        for dest in group:
                            self.assertEqual(dest.sign, -source.sign)
                            self.assertEqual(dest.degree, source.degree)
                            self.assertTrue(any(source in g for g in fs.neighbors(geo, dest, h3.Budget())))

    def test_old_degree_zero_boundary_is_repaired_by_word_split(self):
        geo = fs.Geometry(fs.DEVELOPMENT[0])
        source = fs.State((0, 3, 4, 5, 6, 7, 0), ((1,), (3, 3)), (1, 1), 0, 0)
        self.assertFalse(fs.neighbors(geo, source, h3.Budget())[0])
        targets = fs.neighbors(geo, source, h3.Budget())[1]
        expected = fs.State((0, 3, 4, 0, 6, 7, 0), ((1,), (3,), (3,)), (1, 1, 1), 0, 0)
        self.assertIn(expected, targets)
        self.assertIn(source, fs.neighbors(geo, expected, h3.Budget())[1])

    def test_complete_state_census_matches_preexisting_forest_aggregator(self):
        geo = fs.Geometry(fs.DEVELOPMENT[0])
        states, census = fs.enumerate_states(geo, h3.Budget())
        previous = ft.coefficient(geo.h, (3, 3, 1), h3.Budget(), diagnostics=True)
        for field in ('coefficient', 'first_differences', 'forest_triples', 'composition_blocks', 'census'):
            self.assertEqual(census[field], previous[field])
        self.assertEqual(sum(s.sign < 0 for s in states), 258)
        self.assertEqual(len(states), len(set(states)))

    def test_saturated_critic_case_is_development_not_heldout(self):
        h = (3, 6, 6, 6, 7, 7, 7)
        self.assertIn(h, fs.DEVELOPMENT)
        self.assertEqual(h3.height(h), 3)
        self.assertEqual(len(h3.tab.graph_edges(h)), 14)

    def test_edge_relation_compensates_marks_and_recovers_inverse(self):
        geo = fs.Geometry((4, 4, 4, 4))
        from itertools import product
        for parents in ft.forests(geo.h, 3, h3.Budget()):
            words, inv = geo.data(parents)
            for comps in ft.composition_assignments(tuple(map(len, words)), (2, 1, 1), h3.Budget()):
                for marks in product(*(range(1, a[0]+1) for a in comps)):
                    source = fs.State(parents, comps, marks, 0, inv)
                    for dest in fs.neighbors(geo, source, h3.Budget(), repair=True)[2]:
                        self.assertEqual(dest.degree, source.degree)
                        self.assertEqual(dest.sign, -source.sign)
                        self.assertEqual(dest.epsilon, source.epsilon)
                        self.assertEqual(sorted(x for a in dest.compositions for x in a), [1, 1, 2])
                        self.assertIn(source, fs.neighbors(geo, dest, h3.Budget(), repair=True)[2])

    def test_edge_candidates_are_charged_before_rejecting(self):
        geo = fs.Geometry(fs.DEVELOPMENT[0])
        source = fs.State((0, 3, 4, 5, 6, 7, 0), ((1,), (3, 3)), (1, 1), 0, 0)
        with self.assertRaises(h3.Capped):
            next(fs.edge_operations(geo, source, h3.Budget(candidates=0)))

    def test_heldout_is_fresh_connected_and_disjoint(self):
        cases = fs.heldout()
        self.assertEqual([len(h) for h in cases], [9, 9, 10, 10])
        self.assertFalse(set(cases) & set(h3.development()+h3.HELDOUT+fs.DEVELOPMENT))
        self.assertTrue(all(h3.height(h) == 3 for h in cases))
        self.assertTrue(all(all(h[i] > i+1 for i in range(len(h)-1)) for h in cases))

    def test_hall_witness_checks_complete_grammar_neighbors(self):
        a = fs.State((0,), ((1,),), (1,), 1, 0)
        b = fs.State((0,), ((1,),), (1,), 0, 1)
        c = fs.State((0,), ((1,),), (2,), 1, -1)
        graph = {a: ((b,), (), ()), b: ((a, c), (), ()), c: ((b,), (), ())}
        result = fs.hall_diagnostic((a, b, c), graph, h3.Budget())
        self.assertEqual(result['status'], 'Hall deficiency')
        self.assertEqual((result['negative_count'], result['neighbor_count']), (2, 1))
        complete = fs.hall_diagnostic((a, b), {a: ((b,),), b: ((a,),)}, h3.Budget())
        self.assertEqual(complete['status'], 'grammar saturates negatives')

    def test_capped_case_is_never_complete_or_oracle_checked(self):
        result = fs.run_case(fs.DEVELOPMENT[0], h3.Budget(extensions=0))
        self.assertEqual(result['status'], 'capped')
        self.assertNotIn('comparison', result)
        exhausted = fs.run_case(fs.DEVELOPMENT[0], h3.Budget(candidates=0))
        self.assertEqual(exhausted['status'], 'capped')
        self.assertNotIn('signed_space', exhausted)
        self.assertEqual(exhausted['resources']['extensions'], 0)
        with self.assertRaises(h3.Capped):
            fs.neighbors(fs.Geometry(fs.DEVELOPMENT[0]),
                fs.State((0, 3, 4, 5, 6, 7, 0), ((1,), (3, 3)), (1, 1), 0, 0),
                h3.Budget(candidates=0))


if __name__ == '__main__':
    unittest.main()
