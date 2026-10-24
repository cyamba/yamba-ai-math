"""Three frozen proposed U cuts; no cross-domain map is claimed."""
import argparse
from collections import Counter
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'rogers-ramanujan' / 'checks'))
import kr1


def sheets(height):
    q, r = divmod(height, 5)
    return tuple(3 * q + min(3, max(r - t, 0)) for t in range(3))


def u_valid(parts):
    try:
        kr1.decode_columns(parts)
    except ValueError:
        return False
    return True


def cuts(parts):
    heights = tuple(kr1.inverse_prefix(v) for v in parts)
    lower = tuple(sheets(h)[2] for h in heights if sheets(h)[2])
    triple = tuple(kr1.prefix_weight(h) for h in heights[2::3])
    quotient = tuple(kr1.prefix_weight(h // 3) for h in heights if h // 3)
    return lower, triple, quotient


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bound', type=int, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.bound not in (12, 30, 40):
        parser.error('frozen gates are 12,30,40')
    stats = [Counter() for _ in range(3)]
    failures = [None] * 3
    images = [set() for _ in range(3)]
    seen = []
    for n in range(args.bound + 1):
        for w in kr1.weighted_partitions(n):
            parts = kr1.weighted_columns(w)
            assert sum(parts) == n and u_valid(parts)
            seen.append(parts)
            heights = tuple(kr1.inverse_prefix(v) for v in parts)
            p = tuple(sheets(h) for h in heights)
            assert all(sum(row) == v for row, v in zip(p, parts))
            assert all(row[0] >= row[1] >= row[2] >= 0 for row in p)
            assert all(all(x >= y for x, y in zip(p[i], p[i + 1])) for i in range(len(p) - 1))
            for k, child in enumerate(cuts(parts)):
                stats[k]['inputs'] += 1
                if u_valid(child):
                    stats[k]['valid_child'] += 1
                    images[k].add(child)
                else:
                    stats[k]['invalid_child'] += 1
                    if failures[k] is None:
                        failures[k] = {'reason': 'invalid child U', 'parent': parts,
                                       'parent_weight': n, 'child': child}
                residual = n - 3 * sum(child)
                stats[k]['negative_residual'] += residual < 0
                if residual < 0 and failures[k] is None:
                    failures[k] = {'reason': 'negative residual', 'parent': parts,
                                   'parent_weight': n, 'child': child, 'residual': residual}
            # The complete remainder word, including zeros, recovers every h.
            quotient_padded = tuple(h // 3 for h in heights)
            remainders = tuple(h % 3 for h in heights)
            assert tuple(3 * q + r for q, r in zip(quotient_padded, remainders)) == heights
    # Inclusion obstruction: enumerate all valid targets two units above U0.
    u0 = (6, 3, 3, 1)
    if args.bound >= 15:
        h0 = tuple(kr1.inverse_prefix(v) for v in u0)
        additions = []
        for w in kr1.weighted_partitions(15):
            u = kr1.weighted_columns(w)
            hs = tuple(kr1.inverse_prefix(v) for v in u)
            if len(hs) >= len(h0) and all(x >= y for x, y in zip(hs, h0)):
                additions.append(u)
        assert set(additions) == {(8, 3, 3, 1), (6, 3, 3, 3), (6, 3, 3, 1, 1, 1)}
    else:
        additions = None
    named = []
    for k, name in enumerate(('lower-sheet-core-v1', 'triple-row-v1', 'ternary-height-v1')):
        named.append({'name': name, 'counts': dict(stats[k]), 'smallest_observed_failure': failures[k],
                      'distinct_valid_children': len(images[k])})
    result = {'bound': args.bound, 'literal_U_count': len(seen), 'families': named,
              'sheet_lift_volume_order_and_losslessness': True,
              'height_quotient_with_full_padded_remainder_identity': True,
              'weight13_inclusion_targets_at15': additions,
              'status': 'candidate falsification only; no U/C bridge'}
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
