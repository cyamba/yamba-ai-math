"""Frozen Phase 2 sector checks. Finite output is not a universal proof."""
import argparse
import ast
from collections import Counter
from dataclasses import asdict
import hashlib
import json
from pathlib import Path

import bridge as m
import rr003_cluster_merge as gap
import rr003_stockhofe as product


HERE = Path(__file__).resolve().parent
BASE = HERE.parent


def encode(value):
    if isinstance(value, m.kr1.ClusterData):
        return asdict(value)
    raise TypeError(type(value).__name__)


def external_functions():
    """Only named function AST nodes; no import or module top-level runs."""
    namespace = {'hp': m.kr1, 'Counter': Counter}
    sources = {
        'verify_a3_b0_universal.py': ['step_one', 'reconstruct_a3_b0'],
        'test_complete_n26.py': ['reconstruct_a3_b1', 'reconstruct_a4_b0', 'reconstruct_a5_b0']}
    for name, chosen in sources.items():
        path = BASE / 'inputs/external-scratch' / name
        tree = ast.parse(path.read_text())
        nodes = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in chosen]
        assert len(nodes) == len(chosen)
        module = ast.Module(body=nodes, type_ignores=[])
        exec(compile(module, str(path), 'exec'), namespace)
    return namespace


def first_external_failures(bound, states):
    env = external_functions()
    failures, totals, images = {}, Counter(), {}
    functions = {(3, 0): 'reconstruct_a3_b0', (3, 1): 'reconstruct_a3_b1',
                 (4, 0): 'reconstruct_a4_b0', (5, 0): 'reconstruct_a5_b0'}
    # Separate exact per-sector internal validity from proposed g2/g3 union.
    for c in states:
        key = c.a, c.b
        if key not in functions:
            continue
        label = functions[key]
        totals[label] += 1
        u = env[label](c)
        failures_for = failures.setdefault(label, {})
        if sum(u) != c.weight:
            failures_for.setdefault('weight', {'c': c, 'u': u, 'actual_weight': sum(u)})
        try:
            m.kr1.decode_columns(u)
        except ValueError as error:
            failures_for.setdefault('literal', {'c': c, 'u': u, 'error': str(error)})
        previous = images.setdefault(label, {}).get(u)
        if previous is not None and previous != c:
            failures_for.setdefault('internal_collision', {'c': c, 'other_c': previous, 'u': u})
        images[label][u] = c
        try:
            other = m.g_inverse(u)
        except (m.Outside, ValueError):
            other = None
        if other is not None and other != c:
            failures_for.setdefault('g2_g3_collision', {'c': c, 'other_c': other, 'u': u})
    return {'checked_by_function': dict(totals), 'first_failures': failures}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('bound', type=int, choices=(12, 30, 40))
    bound = parser.parse_args().bound
    states = sorted((c for n in range(bound + 1) for c in m.kr1.cluster_data(n)),
                    key=lambda c: (c.weight, c.a, c.b, c.mu, c.nu))
    all_u = set(u for n in range(bound + 1) for w in m.kr1.weighted_partitions(n)
                for u in [m.kr1.weighted_columns(w)])
    all_B = set(p for n in range(bound + 1) for p in m.kr1.residue_partitions(n))
    all_A = set(p for n in range(bound + 1) for p in m.kr1.gap_partitions(n))
    assert len(states) == len(all_u) == len(all_B) == len(all_A)
    mapped, g_images, f_images = {}, {}, {}
    counts, a_cohorts, b_cohorts, full_a, full_b = Counter(), Counter(), Counter(), Counter(), Counter()
    sector_counts, missing, max_forward, max_reverse = Counter(), None, 0, 0
    phase_count = 0
    for c in states:
        A = gap.cluster_to_gap(c)
        assert A in all_A and gap.gap_to_cluster(A) == c
        ac = 'distinct' if len(set(A)) == len(A) else 'repeated'
        full_a[ac] += 1
        if c.a == 3:
            child, y, k = m.bounded_phase_forward(c)
            assert child.weight <= c.weight <= bound
            assert m.bounded_phase_inverse(child, y, k) == c
            assert c.weight == child.weight + 2 + 2 * y + 3 * k
            phase_count += 1
        if not m.domain(c):
            if missing is None:
                missing = c
            sector_counts[(c.a, c.b)] += 1
            continue
        gu = m.g_forward(c)
        assert gu in all_u and sum(gu) == c.weight and m.g_inverse(gu) == c
        assert gu not in g_images
        g_images[gu] = c
        if m.retained_domain(c):
            fu = m.f1_forward(c)
            assert fu in all_u and m.f1_inverse(fu) == c
            assert fu not in f_images
            f_images[fu] = c
        u, steps = m.h1_forward(c, steps=True)
        assert u in all_u and sum(u) == c.weight
        back, back_steps = m.h1_inverse(u, steps=True)
        assert back == c and u not in mapped
        if m.retained_domain(c):
            assert u == m.f1_forward(c)
        max_forward, max_reverse = max(max_forward, steps), max(max_reverse, back_steps)
        mapped[u] = c
        counts[(c.a, c.b)] += 1
        a_cohorts[ac] += 1
        B = product.columns_to_residue(u)
        assert B in all_B and product.residue_to_columns(B) == u
        b_cohorts['distinct' if len(set(B)) == len(B) else 'repeated'] += 1
    image_reverse = set()
    rejected, first_rejected = 0, None
    for u in sorted(all_u, key=lambda u: (sum(u), u)):
        try:
            c, steps = m.h1_inverse(u, steps=True)
        except m.Outside:
            rejected += 1
            if first_rejected is None:
                first_rejected = u
        else:
            assert m.domain(c) and m.h1_forward(c) == u and mapped[u] == c
            image_reverse.add(u)
            max_reverse = max(max_reverse, steps)
    assert set(mapped) == image_reverse
    for B in all_B:
        bc = 'distinct' if len(set(B)) == len(B) else 'repeated'
        full_b[bc] += 1
        u = product.residue_to_columns(B)
        assert u in all_u and product.columns_to_residue(u) == B
    out = {'status': 'finite_pass_not_full_KR1', 'bound': bound, 'all_C_A_U_B': len(states),
           'H1_C_domain_and_U_image': len(mapped), 'H1_rejected_U': rejected,
           'H1_sectors': {str(k): v for k, v in sorted(counts.items())},
           'missing_C_sectors': {str(k): v for k, v in sorted(sector_counts.items())},
           'first_missing_C': missing, 'first_rejected_U': first_rejected,
           'H1_A_cohorts': dict(a_cohorts), 'H1_B_cohorts': dict(b_cohorts),
           'full_A_cohorts': dict(full_a), 'full_B_cohorts': dict(full_b),
           'max_forward_path': max_forward, 'max_reverse_path': max_reverse,
           'bounded_phase_a3_states': phase_count,
           'external_candidate_falsifiers': first_external_failures(bound, states),
           'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'bridge_sha256': hashlib.sha256((HERE / 'bridge.py').read_bytes()).hexdigest()}
    target = HERE / f'result-{bound}.json'
    if target.exists():
        raise FileExistsError(target)
    target.write_text(json.dumps(out, default=encode, indent=2) + '\n')
    print(json.dumps(out, default=encode, sort_keys=True))


if __name__ == '__main__':
    main()
