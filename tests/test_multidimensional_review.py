"""Regressions for PR15 mathematical review: test the maps, not only image sets."""
import unittest
from research.partitions.checks import multidimensional_ferrers as m
from research.partitions.checks import tableaux as t


class ReviewRegressions(unittest.TestCase):
    def test_second_rotation_loses_weight_and_fourth_repairs_it(self):
        h = (2, 2, 4, 5, 5)
        source = ((1, 4), (2, 5), (3,))
        candidates = m.promote_32_candidates(source)
        self.assertTrue(t.validates(h, source, (2, 2, 1)))
        self.assertTrue(m.is_local_three_chain_witness(h, source))
        self.assertEqual(t.inv_g(h, source), 1)
        self.assertEqual(t.inv_g(h, candidates[1]), 2)
        self.assertEqual(m.phi_221(h, source), ('32', ((1, 3, 5), (2, 4))))
        self.assertEqual(t.inv_g(h, candidates[3]), 1)

    def test_recover_tau_not_inverse(self):
        beta = (0, 0, 3)
        cols, sigma = m.beta_to_djt(beta)
        self.assertEqual((cols, sigma), ((1, 1, 1), (2, 0, 1)))
        self.assertEqual(m.djt_to_beta(cols, sigma), beta)
        inverse = tuple(sigma.index(j) for j in range(3))
        self.assertEqual(tuple(cols[i] - i + inverse[i] for i in range(3)), (2, 2, -1))

    def test_all_beta_sectors_both_directions_and_sign_through_six(self):
        report = m.verify_beta_rearrangement_bijection(6)
        self.assertEqual([x['n'] for x in report], list(range(1, 7)))

    def test_kr1_N41_counterexample_is_preserved(self):
        # A passing test records a refuted extension, not a successful bijection.
        import sys
        sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parents[1]
                               / 'research/rogers-ramanujan/checks'))
        import rr004_multidim_cones as cones
        high = cones.kr1.ClusterData(5, 0, (0, 1, 2, 6, 7), ())
        low = cones.kr1.ClusterData(2, 2, (5, 5), (0, 1))
        u = (19, 12, 6, 3, 1)
        self.assertEqual(cones.reconstruct_full(high), u)
        self.assertEqual(cones.reconstruct_full(low), u)
        self.assertEqual(cones.decompose_full(u), low)
        self.assertNotEqual(high, low)

    def test_beta_rejects_repeated_keys_and_wrong_total(self):
        for beta in ((1, 2, 0), (0, 0, 0)):
            with self.assertRaises(ValueError):
                m.beta_to_djt(beta)


if __name__ == '__main__':
    unittest.main()
