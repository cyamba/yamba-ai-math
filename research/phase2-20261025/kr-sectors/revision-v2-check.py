"""Frozen H3 refinement checks with an exhaustive literal image test <=40."""
import argparse
from collections import Counter
from dataclasses import asdict
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('revision_bridge', HERE / 'revision-v2-bridge.py')
h = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)
m, e = h.m, h.e
import rr003_cluster_merge as gap
import rr003_stockhofe as product


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
    state_set = set(states)
    us = {m.kr1.weighted_columns(w) for n in range(bound + 1)
          for w in m.kr1.weighted_partitions(n)}
    mapped, aux_cohorts = {}, Counter()
    new_classes, source_sectors = Counter(), Counter()
    cohorts_A, cohorts_B, component_samples = Counter(), Counter(), []
    first_missing = first_rejected = None
    preserved = 0
    for c in states:
        if not h.domain(c):
            if first_missing is None:
                first_missing = c
            continue
        u = h.forward(c)
        assert u in us and sum(u) == c.weight and u not in mapped
        assert h.inverse(u) == c
        mapped[u] = c
        source_sectors[(c.a, c.b)] += 1
        if e.extended_domain(c):
            assert e.forward(c) == u and e.inverse(u) == c
            preserved += 1
        else:
            label = 'middle_equality_t_positive' if h.slab(c) else 'delta2_one_slab'
            new_classes[label] += 1
            try:
                e.inverse(u)
            except m.Outside:
                pass
            else:
                raise AssertionError(('new target already in H2', c, u))
            if h.y1(c) and c.mu[0] == 0 and c.mu[1] <= 1:
                d = m.g_inverse(u)
                v = m.f1_forward(d)
                assert d == m.kr1.ClusterData(3, 0, (c.mu[1] + 1, c.mu[1] + 4, c.mu[1] + 4 + c.mu[3] - c.mu[2]), ())
                assert v == (12, 6) + (3,) * c.mu[1] + (1,) * (c.mu[3] - c.mu[2])
                try:
                    m.g_inverse(v)
                except m.Outside:
                    pass
                else:
                    raise AssertionError(('target-only component did not reject', u, d, v))
                component_samples.append({'u': u, 'g_inverse': d, 'f1_image': v})
        A, B = gap.cluster_to_gap(c), product.columns_to_residue(u)
        assert m.kr1.is_gap(A) and gap.gap_to_cluster(A) == c and sum(A) == c.weight
        assert m.kr1.is_residue(B) and product.residue_to_columns(B) == u and sum(B) == c.weight
        cohorts_A['distinct' if len(A) == len(set(A)) else 'repeated'] += 1
        cohorts_B['distinct' if len(B) == len(set(B)) else 'repeated'] += 1
    accepted = set()
    for u in sorted(us, key=lambda u: (sum(u), u)):
        try:
            c = h.inverse(u)
        except m.Outside:
            if first_rejected is None:
                first_rejected = u
        else:
            assert c in state_set and h.domain(c) and h.forward(c) == u and mapped[u] == c
            accepted.add(u)
    assert accepted == set(mapped)
    naive = None
    if bound >= 25:
        c = m.kr1.ClusterData(4, 0, (0, 3, 3, 3), ())
        u = (8, 8, 3, 3, 3)
        other = m.g_inverse(u)
        assert other == m.kr1.ClusterData(2, 1, (6, 6), (0,))
        assert m.g_forward(other) == u and c.weight == sum(u) == 25
        naive = {'status': 'refuted_naive_append_threes_before_carry', 'source': c,
                 'u': u, 'other_g_source': other, 'repaired_u': h.forward(c)}
    out = {'status': 'finite_H3_pass_not_full_KR1', 'bound': bound, 'all_C_U': len(states),
           'H3_mapped': len(mapped), 'H3_rejected': len(us) - len(mapped),
           'H2_preserved': preserved, 'new_classes': dict(new_classes),
           'source_sectors': {str(k): v for k, v in sorted(source_sectors.items())},
           'A_cohorts': dict(cohorts_A), 'B_cohorts': dict(cohorts_B),
           'first_missing_C': first_missing, 'first_rejected_U': first_rejected,
           'q0_target_only_components': component_samples,
           'naive_append_threes_failure': naive,
           'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'bridge_sha256': hashlib.sha256((HERE / 'revision-v2-bridge.py').read_bytes()).hexdigest()}
    path = HERE / f'revision-v2-result-{bound}.json'
    if path.exists():
        raise FileExistsError(path)
    path.write_text(json.dumps(out, default=encode, indent=2) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k != 'q0_target_only_components'}, default=encode, sort_keys=True))


if __name__ == '__main__':
    main()
