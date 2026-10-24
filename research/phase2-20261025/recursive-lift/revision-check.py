"""Reserved correction of candidate 3, preserving every initial frozen file."""
import argparse
from collections import Counter
import json
from pathlib import Path
import sys

from triadic import C, step
from u_candidates import cuts, kr1

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'kr-sectors'))
import bridge


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bound', type=int, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.bound not in (12, 30, 40):
        parser.error('frozen gates are 12,30,40')
    counts = Counter()
    child3_preimages = []
    for n in range(args.bound + 1):
        for w in kr1.weighted_partitions(n):
            u = kr1.weighted_columns(w)
            h = tuple(kr1.inverse_prefix(x) for x in u)
            child = cuts(u)[2]
            q = tuple(kr1.inverse_prefix(x) for x in child)
            counts['U_inputs'] += 1
            if q:
                counts['nonempty_children'] += 1
                assert q[-1] <= 2
                assert all(x - y <= 2 for x, y in zip(q, q[1:]))
                if q[-1] == 2:
                    counts['terminal_quotient_two'] += 1
                    positive = sum(x >= 3 for x in h)
                    assert h[positive - 1] == 6
                    assert positive < len(h) and h[positive] == 2
                else:
                    counts['terminal_quotient_one'] += 1
            assert child != (6,)
            if child == (3,):
                child3_preimages.append({'parent': u, 'weight': n})
                assert n >= 13
    witness = (10, 3)
    if args.bound >= 13:
        kr1.decode_columns(witness)
        assert cuts(witness)[2] == (3,)
        assert min(x['weight'] for x in child3_preimages) == 13
        assert any(tuple(x['parent']) == witness for x in child3_preimages)
    else:
        assert not child3_preimages
    parent9 = C(3, 0, (0, 0, 0), ())
    _, child9 = step(parent9)
    assert child9 == C(0, 1, (), (0,)) and parent9.weight == 9
    child9_old = kr1.ClusterData(child9.a, child9.b, child9.mu, child9.nu)
    assert bridge.g2.reconstruct_columns(child9_old) == (3,)
    assert bridge.h1_forward(child9_old) == (3,)
    parent18 = C(0, 2, (), (1, 1))
    _, child18 = step(parent18)
    assert child18 == C(2, 0, (1, 1), ()) and parent18.weight == 18
    child18_old = kr1.ClusterData(child18.a, child18.b, child18.mu, child18.nu)
    assert bridge.g2.reconstruct_columns(child18_old) == (6,)
    assert bridge.h1_forward(child18_old) == (6,)
    result = {'status': 'corrected finite checks; universal proof in revision.md',
              'bound': args.bound, 'counts': dict(counts),
              'old_terminal_le_one_claim': 'refuted; dropped zeros can expose quotient two',
              'true_terminal_bound': 2, 'internal_drop_bound': 2,
              'minimal_child3_parent_weight': 13 if args.bound >= 13 else 'not reached',
              'child3_parent_witness': witness if args.bound >= 13 else None,
              'child3_preimage_count': len(child3_preimages),
              'child3_minimal_parents': [x for x in child3_preimages if x['weight'] == 13],
              'weight9_commutation_failure': True,
              'child6_globally_excluded': True,
              'retained_H1_child6_demanded_at_parent18': True,
              'no_full_U_C_claim': True}
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
