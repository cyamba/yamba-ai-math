"""P014 representation and transport checks; finite tests are not the theorem."""
from itertools import product
import copy
import unittest

from research.partitions.checks import forest_surgery as fs
from research.partitions.checks import forest_transport as tr
from research.partitions.checks import forest_triples as ft
from research.partitions.checks import height_three as h3


class ForestTransportTests(unittest.TestCase):
    def test_insertion_coordinates_round_trip_nonclique_tree_lists(self):
        for h in h3.tab.hessenberg_vectors(4):
            geo = fs.Geometry(h)
            for parents in ft.forests(h, 4, h3.Budget()):
                for word in ft.tree_words(parents):
                    bounds, point = tr.encode_word(geo, word)
                    self.assertEqual(tr.decode_word(geo, word, point), word)
                    self.assertTrue(all(0 <= x <= b for b, x in zip(bounds, point)))
                    positions = {u: i for i, u in enumerate(word)}
                    inv = sum(positions[v] < positions[u] for u, v in geo.edges if u in positions and v in positions)
                    self.assertEqual(sum(point), inv)
        with self.assertRaises(ValueError):
            tr.decode_word(fs.Geometry((1, 2, 3)), (1, 2, 3), (0, 0))

    def test_symmetric_chain_labels_partition_boxes_with_rank_offsets(self):
        for bounds in product(range(4), repeat=3):
            chains = {}
            for point in product(*(range(b+1) for b in bounds)):
                label, t, bottom, length = tr.chain_encode(bounds, point)
                self.assertEqual(tr.chain_decode(bounds, label, t), point)
                self.assertEqual(sum(point), bottom+t)
                self.assertEqual(2*bottom+length, sum(bounds))
                chains.setdefault(label, []).append(t)
            for positions in chains.values():
                self.assertEqual(sorted(positions), list(range(len(positions))))
        with self.assertRaises(ValueError):
            tr.chain_decode((2,), (1,), 0)

    def test_p013_witness_is_singleton_chain_and_cross_block_fork_pair(self):
        geo = fs.Geometry(tr.DEVELOPMENT[1])
        source = fs.State((2, 5, 5, 5, 7, 7, 0), ((3, 1, 3),), (3,), 1, 3)
        bounds, point = tr.block_coordinates(geo, source)
        self.assertEqual(bounds, (0, 1, 1, 2, 3, 1, 2))
        self.assertEqual(point, (0, 0, 0, 2, 0, 1, 2))
        self.assertEqual(tr.chain_encode(bounds, point)[1:], (0, 5, 0))
        target = fs.State((2, 3, 0, 5, 7, 7, 0), ((3,), (3, 1)), (3, 3), 1, 1)
        self.assertEqual((source.sign, target.sign, source.degree, target.degree), (-1, 1, 6, 6))
        self.assertIn(target, tr.neighbors(geo, source, h3.Budget(), False)[3])
        self.assertIn(source, tr.neighbors(geo, target, h3.Budget(), False)[3])

    def test_fork_relation_recovers_same_primitive_on_all_small_clique_states(self):
        geo = fs.Geometry((4, 4, 4, 4))
        count = 0
        for parents in ft.forests(geo.h, 3, h3.Budget()):
            words, inv = geo.data(parents)
            for comps in ft.composition_assignments(tuple(map(len, words)), (2, 1, 1), h3.Budget()):
                for marks in product(*(range(1, a[0]+1) for a in comps)):
                    for eps in (0, 1):
                        source = fs.State(parents, comps, marks, eps, inv)
                        for dest in tr.neighbors(geo, source, h3.Budget(), False)[3]:
                            count += 1
                            self.assertEqual(dest.sign, -source.sign)
                            self.assertEqual(dest.degree, source.degree)
                            self.assertEqual(dest.epsilon, source.epsilon)
                            self.assertIn(source, tr.neighbors(geo, dest, h3.Budget(), False)[3])
        self.assertGreater(count, 0)

    def test_digit_step_is_valid_inverse_with_exact_global_weight(self):
        geo = fs.Geometry(tr.DEVELOPMENT[1])
        source = fs.State((2, 5, 5, 5, 7, 7, 0), ((3, 1, 3),), (3,), 1, 3)
        targets = tr.neighbors(geo, source, h3.Budget(), True)[4]
        self.assertTrue(targets)
        for dest in targets:
            self.assertEqual(dest.compositions, source.compositions)
            self.assertEqual(dest.marks, source.marks)
            self.assertEqual(dest.degree, source.degree)
            self.assertEqual(dest.sign, -source.sign)
            self.assertEqual(dest.inversion, source.inversion+1)
            self.assertIn(source, tr.neighbors(geo, dest, h3.Budget(), True)[4])

    def test_new_candidates_charged_before_rejection(self):
        geo = fs.Geometry(tr.DEVELOPMENT[1])
        source = fs.State((2, 5, 5, 5, 7, 7, 0), ((3, 1, 3),), (3,), 1, 3)
        for operation in (tr.fork_operations, tr.digit_operations):
            with self.assertRaises(h3.Capped):
                next(operation(geo, source, h3.Budget(candidates=0)))

    def test_hard_cap_at_case_entry_has_no_enumeration_or_comparison(self):
        case = tr.run_case(tr.DEVELOPMENT[0], h3.Budget(candidates=0))
        self.assertEqual(case['status'], 'capped')
        self.assertNotIn('signed_space', case)
        self.assertNotIn('comparison', case)
        self.assertEqual(case['resources']['extensions'], 0)

    def test_holdouts_disjoint_from_all_previous_frozen_cases(self):
        prior = set(h3.development()+h3.HELDOUT+fs.DEVELOPMENT+fs.heldout()+tr.DEVELOPMENT)
        fresh = tr.heldout()
        self.assertEqual([len(h) for h in fresh], [9, 10])
        self.assertFalse(set(fresh) & prior)
        self.assertTrue(all(h3.height(h) == 3 for h in fresh))
        self.assertTrue(all(h[i] > i+1 for h in fresh for i in range(len(h)-1)))

    def test_direct_hall_verification_rejects_false_neighborhood_and_statistic(self):
        geo = fs.Geometry(tr.DEVELOPMENT[3])
        parents = (3, 5, 4, 6, 7, 0, 8, 0)
        a = fs.State(parents, ((1, 3), (4,)), (1, 1), 0, 3)
        b = fs.State(parents, ((3, 1), (4,)), (1, 1), 0, 3)
        dest = fs.State((3, 5, 4, 0, 7, 0, 8, 0), ((3,), (4,), (1,)), (1, 1, 1), 0, 3)
        certificate = dict(status='Hall deficiency', negative_count=2, neighbor_count=1,
                           negatives=[a.record(), b.record()], neighbors=[dest.record()])
        checked = tr.verify_hall_certificate(geo, certificate, h3.Budget(), repair=True)
        self.assertEqual(checked['status'], 'verified Hall deficiency')
        self.assertTrue(checked['complete_neighborhood_verified'])
        self.assertEqual([r['neighbors_by_primitive'][-1] for r in checked['per_state']], [0, 0])
        missing = copy.deepcopy(certificate)
        missing['neighbors'] = []; missing['neighbor_count'] = 0
        with self.assertRaises(ValueError):
            tr.verify_hall_certificate(geo, missing, h3.Budget(), repair=True)
        forged = copy.deepcopy(certificate)
        forged['negatives'][0]['inversion'] = 2
        with self.assertRaises(ValueError):
            tr.verify_hall_certificate(geo, forged, h3.Budget(), repair=True)


if __name__ == '__main__':
    unittest.main()
