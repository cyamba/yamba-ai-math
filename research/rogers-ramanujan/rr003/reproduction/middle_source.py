"""RR003 verification-only positive middle-source model; no branch map.

Enumeration checks coefficients, never defines a bijection. See the frozen
middle-source-model.md for the source-derived universal series interpretation.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'research/rogers-ramanujan/checks'))
import kr1
import rr003_second_product as second


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def is_two_cut(j, k, parts):
    if type(j) is not int or type(k) is not int or not 0 <= j <= k:
        return False
    if (not isinstance(parts, (tuple, list)) or any(type(x) is not int or x <= 0 for x in parts)
            or any(x > y for x, y in zip(parts, parts[1:]))):
        return False
    for x in parts:
        if x % 9 in (3, 6):
            if x in (3, 6):
                return False
            continue
        allowed = False
        for base, low, high in ((5, 0, j), (13, 0, j), (8, j, k), (10, j, k), (11, k, None), (7, k, None)):
            difference = x - base
            if difference >= 0 and difference % 9 == 0:
                index = difference // 9
                allowed = low <= index and (high is None or index <= high)
                break
        if not allowed or x == 5:
            return False
    return True


def verify(ceiling):
    require(type(ceiling) is int and 0 <= ceiling <= 30, 'actual source ceiling must be in [0,30]')
    freeze_path = ROOT / 'research/rogers-ramanujan/rr003/middle-source-freeze.json'
    sources = json.loads(freeze_path.read_text())['frozen_sha256']
    for name, digest in sources.items():
        require(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, ('frozen source changed', name))
    require(is_two_cut(0, 0, ()), 'empty two-cut source')
    require(is_two_cut(0, 0, (7, 8, 10, 11, 12, 13)), 'inclusive coincident boundaries')
    require(not is_two_cut(0, 0, (5,)), 'literal5 must cancel')
    require(not is_two_cut(0, 0, (3, 6)), 'common3/6 must cancel')
    require(not is_two_cut(0, 1, (7,)), 'suffix lower bound')
    require(not is_two_cut(1, 0, ()), 'ordered cuts')
    expected_x = [0] * (ceiling + 1)
    expected_middle = [0] * (ceiling + 1)
    for base_weight in range(ceiling + 1):
        for c in kr1.cluster_data(base_weight):
            n = base_weight + 6 * c.a + 12 * c.b
            if n <= ceiling:
                expected_x[n] += 1
            n = base_weight + 4 * c.a + 9 * c.b
            if n <= ceiling:
                expected_middle[n] += 1
    rows = []
    total_x = total_middle = 0
    x_counts = []
    for n in range(ceiling + 1):
        actual = {(j, k, p) for k in range(n // 9 + 1) for j in range(k + 1)
                  if 9 * (j + k) <= n
                  for p in kr1.ordinary_partitions(n - 9 * (j + k))
                  if is_two_cut(j, k, p)}
        require(len(actual) == expected_x[n], ('two-cut/shifted-cluster coefficient', n, len(actual), expected_x[n]))
        x_counts.append(len(actual))
        row = {'weight': n, 'two_cut_objects': len(actual), 'S_6_12_cluster_objects': expected_x[n]}
        total_x += len(actual)
        # Normalize L by7 but cap the actual L weight, never sweeping above30.
        if n + 7 <= ceiling:
            literal_l = {second.Cut(j, p) for j in range(n // 9 + 1)
                         for p in kr1.ordinary_partitions(n - 9 * j)
                         if second.is_cut(second.Cut(j, p))}
            middle = len(literal_l) + (x_counts[n - 5] if n >= 5 else 0)
            require(middle == expected_middle[n], ('middle/shifted-cluster coefficient', n, middle, expected_middle[n]))
            row.update(normalized_L_objects=len(literal_l), middle_objects=middle, S_4_9_cluster_objects=expected_middle[n])
            total_middle += middle
        rows.append(row)
    for name, digest in sources.items():
        require(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, ('source changed during verification', name))
    return {'program': 'RR003', 'status': 'source_model_coefficients_checked_no_branch_bijection',
            'actual_source_weight_ceiling': ceiling, 'middle_normalized_weight_ceiling': max(-1, ceiling - 7),
            'two_cut_objects': total_x, 'middle_objects': total_middle, 'cases': rows,
            'full_bijection': 'unresolved', 'novelty': 'unverified',
            'assurance': 'finite coefficient checks and attributed author algebraic interpretation; no separate semantic review or branch map',
            'source_sha256': sources}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ceiling', type=int, default=12)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error('refusing to overwrite evidence')
    report = verify(args.ceiling)
    report['finished_utc'] = datetime.now(timezone.utc).isoformat()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ('status', 'actual_source_weight_ceiling', 'middle_normalized_weight_ceiling', 'two_cut_objects', 'middle_objects')}))


if __name__ == '__main__':
    main()
