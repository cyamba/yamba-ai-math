"""Bounded corroboration of the written all-parameter cone classification.

The theorem is a branch-by-branch argument in cone_proof.md, not inferred from
this finite box. No global KR1 map is defined or repaired here.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
import sys

CHECKS = Path(__file__).resolve().parents[2] / 'rogers-ramanujan' / 'checks'
sys.path.insert(0, str(CHECKS))
import kr1
import rr003_a2


def cone(z, y, x, c6, c3, c1):
    return (10,) * z + (9,) * y + (8,) * x + (6,) * c6 + (3,) * c3 + (1,) * c1


def predicted_lower_cluster(z, y, x, c6, c3, c1):
    if z <= 3 and y >= 3 and c6 >= 2 and c3 >= 2:
        k = 4 * x + 5 * z - 2
        return kr1.ClusterData(2, 3, (k, k + c1),
                               (y - 3, y + c6 - 5, y + c6 + c3 - 7))
    return None


def verify():
    if not __debug__:
        raise RuntimeError('Run without -O: checks use assertions')
    checked = accepted = 0
    for z, y, x, c6, c3, c1 in product(range(6), range(1, 6), range(6),
                                      range(4), range(4), range(3)):
        if x + z == 0 or (x == 0 and c6 + c3 + c1 == 0):
            continue
        u = cone(z, y, x, c6, c3, c1)
        kr1.decode_columns(u)
        expected = predicted_lower_cluster(z, y, x, c6, c3, c1)
        try:
            actual = rr003_a2.decompose_columns(u)
        except rr003_a2.OutsideRestrictedDomain:
            actual = None
        assert actual == expected, (u, actual, expected)
        if actual is not None:
            assert rr003_a2.reconstruct_columns(actual) == u
            assert actual.weight == sum(u)
            accepted += 1
        checked += 1
    return {'status': 'passed_finite_corroboration',
            'bounds': {'x_z_each': [0, 5], 'y': [1, 5],
                       'c6_c3_each': [0, 3], 'c1': [0, 2]},
            'states_checked': checked, 'lower_image_states': accepted,
            'general_assurance': 'written branch proof, separately reviewed in review-round1.md',
            'claim': 'cone valid; lower-image intersection iff z<=3,y>=3,c6>=2,c3>=2'}


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
