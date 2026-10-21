"""Small exact research checks; finite agreement is not the general conjecture."""

import itertools
import unittest

from research.partitions.checks import coloring_oracle


def all_hessenberg_vectors(n):
    for h in itertools.product(*(range(i + 1, n + 1) for i in range(n))):
        if all(a <= b for a, b in zip(h, h[1:])):
            yield h


class ColoringOracleTests(unittest.TestCase):
    def test_four_vertex_path_expansion(self):
        self.assertEqual(
            coloring_oracle.elementary_expansion((2, 3, 4, 4)),
            {
                (4,): (1, 1, 1, 1),
                (3, 1): (0, 1, 1),
                (2, 2): (0, 1, 1),
            },
        )

    def test_empty_edgeless_and_complete_graphs(self):
        self.assertEqual(coloring_oracle.elementary_expansion(()), {(): (1,)})
        for n in range(1, 6):
            self.assertEqual(
                coloring_oracle.elementary_expansion(tuple(range(1, n + 1))),
                {(1,) * n: (1,)},
            )
        self.assertEqual(
            coloring_oracle.elementary_expansion((4, 4, 4, 4)),
            {(4,): (1, 3, 5, 6, 5, 3, 1)},
        )

    def test_named_monomial_symmetry_on_all_four_vertex_graphs(self):
        vectors = tuple(all_hessenberg_vectors(4))
        self.assertEqual(len(vectors), 14)
        for h in vectors:
            for shape in coloring_oracle.partitions(4):
                coefficient = coloring_oracle.named_monomial_coefficient(h, shape)
                for multiplicities in set(itertools.permutations(shape)):
                    with self.subTest(h=h, multiplicities=multiplicities):
                        self.assertEqual(
                            coloring_oracle.named_monomial_coefficient(h, multiplicities),
                            coefficient,
                        )

    def test_subset_expansion_of_elementary_products(self):
        # e_2 e_1 has coefficients 1 at x_1^2 x_2 and 3 at x_1 x_2 x_3.
        self.assertEqual(
            coloring_oracle.elementary_monomial_coefficient((2, 1), (2, 1)), 1
        )
        self.assertEqual(
            coloring_oracle.elementary_monomial_coefficient((2, 1), (1, 1, 1)), 3
        )
        self.assertEqual(
            coloring_oracle.elementary_monomial_coefficient((3,), (2, 1)), 0
        )

    def test_invalid_inputs(self):
        for h in ((0,), (2,), (3, 2, 3), (1, "2"), (True,)):
            with self.subTest(h=h), self.assertRaises(ValueError):
                coloring_oracle.elementary_expansion(h)
        with self.assertRaises(ValueError):
            coloring_oracle.named_monomial_coefficient((2, 2), (1,))
        with self.assertRaises(ValueError):
            coloring_oracle.named_monomial_coefficient((2, 2), (2, 0))

    def test_independent_tableau_comparison_through_five_vertices(self):
        from research.partitions.checks import tableaux

        count = 0
        for n in range(6):
            for h in all_hessenberg_vectors(n):
                with self.subTest(h=h):
                    self.assertEqual(
                        tableaux.elementary_expansion(h),
                        coloring_oracle.elementary_expansion(h),
                    )
                count += 1
        self.assertEqual(count, 65)

    def test_connected_slide_obstruction_and_independent_coefficients(self):
        from research.partitions.checks import tableaux

        h = (3, 4, 4, 5, 5)
        source = ((1, 4), (2, 5), (3,))
        target = ((1, 4), (2,), (5,), (3,))
        self.assertTrue(tableaux.validates(h, source, (2, 2, 1)))
        self.assertEqual(tableaux.demote(source, 1), target)
        self.assertFalse(tableaux.validates(h, target, (2, 1, 1, 1)))
        self.assertFalse(tableaux.suffix_admissible(h, source, 1))
        self.assertEqual(tableaux.inv_g(h, source), tableaux.inv_g(h, target))
        expected = {
            (5,): (1, 3, 4, 4, 4, 3, 1),
            (4, 1): (0, 1, 3, 4, 3, 1),
            (3, 2): (0, 0, 1, 2, 1),
        }
        self.assertEqual(coloring_oracle.elementary_expansion(h), expected)
        self.assertEqual(tableaux.elementary_expansion(h), expected)

    def test_unrestricted_slide_injection_has_a_cardinality_obstruction(self):
        from research.partitions.checks import tableaux

        total_order = (1, 2, 3, 4, 5)
        source_count = len(tuple(tableaux.tableaux(total_order, (2, 2, 1))))
        target_count = len(tuple(tableaux.tableaux(total_order, (2, 1, 1, 1))))
        self.assertEqual((source_count, target_count), (5, 4))

    def test_bubble_insertion_repairs_the_connected_slide(self):
        from research.partitions.checks import tableaux

        h = (3, 4, 4, 5, 5)
        source = ((1, 4), (2, 5), (3,))
        image = ((1, 4), (2,), (3,), (5,))
        self.assertTrue(tableaux.height_two(h))
        self.assertEqual(tableaux.bubble_demote(h, source, 1), image)
        self.assertTrue(tableaux.validates(h, image, (2, 1, 1, 1)))
        self.assertEqual(tableaux.recover(h, image, 1), source)
        self.assertEqual(tableaux.inv_g(h, image), tableaux.inv_g(h, source))

    def test_three_chain_causes_a_bubble_collision(self):
        from research.partitions.checks import tableaux

        h = (1, 2, 3)
        first, second = ((1, 2), (3,)), ((1, 3), (2,))
        self.assertFalse(tableaux.height_two(h))
        self.assertTrue(tableaux.validates(h, first))
        self.assertTrue(tableaux.validates(h, second))
        self.assertNotEqual(first, second)
        self.assertEqual(
            tableaux.bubble_demote(h, first, 0),
            tableaux.bubble_demote(h, second, 0),
        )

    def test_all_height_two_bubble_inverses_through_five_vertices(self):
        from research.partitions.checks.verify import _verify_bubble

        sizes, failures = _verify_bubble(5)
        self.assertEqual(failures, [])
        self.assertEqual([row["sources"] for row in sizes], [1, 5, 36, 282])
        for row in sizes:
            self.assertEqual(row["sources"], row["recovered_sources"])
            self.assertEqual(row["sources"], row["distinct_images"])
            self.assertEqual(row["sources"], row["valid_images"])
            self.assertEqual(row["sources"], row["inversion_preserved"])


if __name__ == "__main__":
    unittest.main()
