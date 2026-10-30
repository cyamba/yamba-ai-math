"""Independent literal-model checks for the Argon continuation statements."""
from pathlib import Path
import sys
import unittest

CHECKS = Path(__file__).resolve().parents[1] / 'research/rogers-ramanujan/checks'
sys.path.insert(0, str(CHECKS))
import kr1
import rr003_a2
import rr004_multidim_cones
from six_weight_cones import ConeCoordinates, ConeOctant


class ArgonConeTests(unittest.TestCase):
    def test_original_cone_and_unbounded_z_use_actual_decoder(self):
        for p in [ConeCoordinates(0, 1, 1), ConeCoordinates(1, 2, 0, c1=1),
                  ConeCoordinates(20, 7, 0, c3=1), ConeCoordinates(5, 10, 2, 9, 8, 7)]:
            u = p.columns()
            kr1.decode_columns(u)
            self.assertEqual(sum(u), p.weight)
            self.assertEqual(ConeCoordinates.from_columns(u), p)
            self.assertIsNone(p.lower_preimage())
            with self.assertRaises(rr003_a2.OutsideRestrictedDomain):
                rr003_a2.decompose_columns(u)

    def test_exact_first_lower_overlap_and_preimage(self):
        p = ConeCoordinates(0, 3, 1, 2, 2, 0)
        self.assertEqual(p.weight, 53)
        c = p.lower_preimage()
        self.assertEqual(c, kr1.ClusterData(2, 3, (2, 2), (0, 0, 0)))
        self.assertEqual(rr003_a2.reconstruct_columns(c), p.columns())
        self.assertEqual(rr003_a2.decompose_columns(p.columns()), c)
        for p in [ConeCoordinates(3, 9, 4, 6, 7, 8), ConeCoordinates(1, 3, 0, 2, 2, 0)]:
            self.assertEqual(rr003_a2.reconstruct_columns(p.lower_preimage()), p.columns())

    def test_lower_free_does_not_mean_unused_by_higher_sectors(self):
        p = ConeCoordinates(1, 2, 0, c3=1)
        self.assertIsNone(p.lower_preimage())
        owner = kr1.ClusterData(4, 0, (0, 0, 5, 10), ())
        self.assertEqual(rr004_multidim_cones.reconstruct_full(owner), p.columns())
        self.assertEqual(owner.weight, 31)

    def test_terminal_condition_is_stronger_than_not_divisible_by_five(self):
        for u in [(10,), (10, 9), (10, 10, 9, 9)]:
            with self.assertRaises(ValueError):
                kr1.decode_columns(u)
            with self.assertRaises(ValueError):
                ConeCoordinates.from_columns(u)

    def test_safe_current_point_is_not_necessarily_a_safe_full_octant(self):
        p = ConeCoordinates(1, 3, 1)
        self.assertIsNone(p.lower_preimage())
        self.assertFalse(p.entire_increment_octant_avoids_lower_image())
        self.assertIsNotNone(ConeOctant(p).at(2, 2, 0).lower_preimage())
        self.assertTrue(ConeCoordinates(4, 3, 1).entire_increment_octant_avoids_lower_image())

    def test_same_head_offset_octants_must_overlap(self):
        a = ConeOctant(ConeCoordinates(1, 2, 1, 0, 5, 0))
        b = ConeOctant(ConeCoordinates(1, 2, 1, 3, 0, 4))
        p = a.intersection_witness(b)
        self.assertEqual(p.tail, (3, 5, 4))
        self.assertEqual(a.at(*a.recover(p.columns())), p)
        self.assertEqual(b.at(*b.recover(p.columns())), p)
        c = ConeOctant(ConeCoordinates(2, 2, 1))
        self.assertIsNone(a.intersection_witness(c))

    def test_invalid_coordinates_and_noncanonical_columns_rejected(self):
        for args in [(True, 1, 1), (-1, 1, 1), (1, 0, 1), (0, 1, 0)]:
            with self.assertRaises(ValueError):
                ConeCoordinates(*args)
        for u in [(9, 10, 1), (10, 9, 7, 1), (10, 9, True)]:
            with self.assertRaises(ValueError):
                ConeCoordinates.from_columns(u)


if __name__ == '__main__':
    unittest.main()
