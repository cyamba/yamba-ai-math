"""Frozen H-family version2 and dimension-reduction checks through40 only."""
import argparse
from collections import Counter
from dataclasses import asdict
import hashlib
import json
from pathlib import Path

import bridge as m
import extension as e
import reductions as r
import rr003_cluster_merge as gap
import rr003_stockhofe as product

HERE = Path(__file__).resolve().parent


def encode(value):
    if isinstance(value, m.kr1.ClusterData):
        return asdict(value)
    raise TypeError(type(value).__name__)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('bound', type=int, choices=(12, 30, 40))
    bound = parser.parse_args().bound
    states = sorted((c for n in range(bound + 1) for c in m.kr1.cluster_data(n)),
                    key=lambda c: (c.weight, c.a, c.b, c.mu, c.nu))
    us = set(m.kr1.weighted_columns(w) for n in range(bound + 1)
             for w in m.kr1.weighted_partitions(n))
    mapped, aux = {}, {}
    new_planes, cohorts_A, cohorts_B, reductions, sectors = Counter(), Counter(), Counter(), Counter(), Counter()
    first_missing = first_rejected = None
    max_fwd = max_rev = 0
    for c in states:
        if c.a in (3, 4, 5):
            child, boundary, excess = r.forward(c)
            assert r.inverse(child, boundary) == c
            assert c.weight == child.weight + excess and 0 <= child.weight <= c.weight <= bound
            reverse_child, reverse_boundary, _ = r.forward(r.inverse(child, boundary))
            assert (reverse_child, reverse_boundary) == (child, boundary)
            reductions[(c.a, c.b)] += 1
        if not e.extended_domain(c):
            if first_missing is None:
                first_missing = c
            continue
        gu = e.auxiliary_forward(c)
        assert gu in us and sum(gu) == c.weight
        assert e.auxiliary_inverse(gu) == c and gu not in aux
        aux[gu] = c
        u, steps = e.forward(c, steps=True)
        assert u in us and sum(u) == c.weight and u not in mapped
        back, rev_steps = e.inverse(u, steps=True)
        assert back == c
        if m.domain(c):
            assert u == m.h1_forward(c)
        if e.plane(c):
            new_planes[c.a] += 1
        assert not e.tail(c), 'large-b objects are outside the40 boundary'
        mapped[u] = c
        sectors[(c.a, c.b)] += 1
        max_fwd, max_rev = max(max_fwd, steps), max(max_rev, rev_steps)
        A = gap.cluster_to_gap(c)
        B = product.columns_to_residue(u)
        assert m.kr1.is_gap(A) and gap.gap_to_cluster(A) == c and sum(A) == c.weight
        assert m.kr1.is_residue(B) and product.residue_to_columns(B) == u and sum(B) == c.weight
        cohorts_A['distinct' if len(A) == len(set(A)) else 'repeated'] += 1
        cohorts_B['distinct' if len(B) == len(set(B)) else 'repeated'] += 1
    recovered = set()
    for u in sorted(us, key=lambda u: (sum(u), u)):
        try:
            c, steps = e.inverse(u, steps=True)
        except m.Outside:
            if first_rejected is None:
                first_rejected = u
        else:
            assert e.extended_domain(c) and e.forward(c) == u and mapped[u] == c
            recovered.add(u)
            max_rev = max(max_rev, steps)
    assert set(mapped) == recovered
    out = {'status': 'finite_H2_and_reduction_pass_not_full_KR1', 'bound': bound,
           'all_C_U': len(states), 'H2_mapped': len(mapped), 'H2_rejected': len(us) - len(mapped),
           'H2_sectors': {str(k): v for k, v in sorted(sectors.items())},
           'new_plane_states': dict(new_planes),
           'A_cohorts': dict(cohorts_A), 'B_cohorts': dict(cohorts_B),
           'first_missing_C': first_missing, 'first_rejected_U': first_rejected,
           'max_forward_path': max_fwd, 'max_reverse_path': max_rev,
           'dimension_reductions': {str(k): v for k, v in sorted(reductions.items())},
           'large_b_theorem_not_numerically_exercised': {a: e.tail_threshold(a) for a in (3, 4, 5)},
           'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'extension_sha256': hashlib.sha256((HERE / 'extension.py').read_bytes()).hexdigest(),
           'reductions_sha256': hashlib.sha256((HERE / 'reductions.py').read_bytes()).hexdigest()}
    target = HERE / f'extension-result-{bound}.json'
    if target.exists():
        raise FileExistsError(target)
    target.write_text(json.dumps(out, default=encode, indent=2) + '\n')
    print(json.dumps(out, default=encode, sort_keys=True))


if __name__ == '__main__':
    main()
