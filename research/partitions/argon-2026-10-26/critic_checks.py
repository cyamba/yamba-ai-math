"""Independent bounded transcription checks for the Argon continuation review."""
from pathlib import Path
import itertools
import json
import random
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/rogers-ramanujan/checks'))
import kr1
import rr003_a2
import rr004_multidim_cones as m
from six_weight_cones import ConeCoordinates


def verify():
    if not __debug__:
        raise RuntimeError('Run without -O; this checker uses assertions')
    rng = random.Random(260026)
    cone_checked = valid = intersection = 0
    for _ in range(3500):
        z = rng.choice([0, 1, 2, 3, 4, 5, 17])
        y = rng.choice([1, 2, 3, 4, 9])
        x = rng.choice([0, 1, 2, 6, 19])
        s = rng.choice([0, 1, 2, 3, 11])
        t = rng.choice([0, 1, 2, 3, 13])
        d = rng.choice([0, 1, 8])
        u = (10,)*z + (9,)*y + (8,)*x + (6,)*s + (3,)*t + (1,)*d
        expected_valid = x+s+t+d > 0
        try:
            kr1.decode_columns(u)
            actual_valid = True
        except ValueError:
            actual_valid = False
        assert actual_valid == expected_valid, (z, y, x, s, t, d)
        cone_checked += 1
        if not actual_valid or x+z == 0:
            continue
        valid += 1
        expected = z <= 3 and y >= 3 and s >= 2 and t >= 2
        try:
            c = rr003_a2.decompose_columns(u)
            actual = True
        except rr003_a2.OutsideRestrictedDomain:
            actual = False
        assert actual == expected, (u, expected)
        if expected:
            k = 4*x+5*z-2
            v = kr1.ClusterData(2, 3, (k, k+d), (y-3, y+s-5, y+s+t-7))
            assert rr003_a2.reconstruct_columns(v) == u
            assert c == v
            intersection += 1
        point = ConeCoordinates(z, y, x, s, t, d)
        assert point.columns() == u
        assert (point.lower_preimage() is not None) == expected
    samples = [(0, 3, 0), (0, 3, 1), (0, 3, 9), (0, 5, 0),
               (1, 12, 0), (0, 12, 7), (12, 1, 7), (12, 2, 7)]
    samples += [(rng.randrange(81), rng.randrange(121), rng.randrange(41))
                for _ in range(1200)]
    for s, t, d in samples:
        c = kr1.ClusterData(3, 0, (s, s+t, s+t+d), ())
        u = m.reconstruct_a3_b0(c)
        assert sum(u) == c.weight
        kr1.decode_columns(u)
        assert m.decompose_a3_b0(u) == c
        try:
            low = rr003_a2.decompose_columns(u)
        except rr003_a2.OutsideRestrictedDomain:
            pass
        else:
            raise AssertionError((c, u, low))
    for k in range(1, 11):
        states = set()
        for bits in itertools.product((0, 1), repeat=k):
            acc, nu = 0, []
            for bit in bits:
                acc += bit
                nu.append(acc)
            c = kr1.ClusterData(3, k, (0, 0, 0), tuple(nu))
            assert c.weight <= (9*k*k+21*k+18)//2
            states.add(c)
        assert len(states) == 2**k
    assert 2**128 > 75082**6
    return {'status': 'passed_independent_finite_transcription_checks',
            'seed': 260026, 'cone_samples': cone_checked,
            'valid_marked_cones': valid, 'lower_intersections': intersection,
            'sector_samples': len(samples), 'binary_apex_families_checked_k': [1, 10],
            'exact_capacity_comparison': {'k': 128, 'max_weight': 75081,
                'source_count': str(2**128), 'target_upper_bound': str(75082**6)},
            'assurance': 'Finite checks corroborate transcription. Universal verdict rests on written proofs.'}


if __name__ == '__main__':
    if not __debug__:
        raise SystemExit('Run with assertions enabled; omit -O')
    report = verify()
    Path(__file__).with_name('critic-evidence.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
