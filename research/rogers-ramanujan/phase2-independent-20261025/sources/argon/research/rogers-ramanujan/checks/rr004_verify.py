"""RR004 exact obstruction certificate checks; no KR1 maps are implemented.

The universal obstruction is the written proof, not the finite sweep.
"""
import argparse
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time
import kr1

ROOT = Path(__file__).resolve().parents[3]
PHASE = ROOT / 'research/rogers-ramanujan/rr004'
FORCED = {(1, 0): 0, (2, 0): 1, (2, 1): 0, (3, 1): 1, (3, 2): -1}


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def check_freeze(root=ROOT, freeze_path=None):
    path = freeze_path or root / 'research/rogers-ramanujan/rr004/round-1-freeze.json'
    freeze = json.loads(path.read_text())
    for name, expected in freeze['source_sha256'].items():
        actual = hashlib.sha256((root / name).read_bytes()).hexdigest()
        require(actual == expected, 'frozen source changed: ' + name)
    return freeze


def forced_pair_charge(columns):
    """Diagnostic forced formula, NOT a cluster extraction; may return -1."""
    kr1.decode_columns(columns)
    heights = tuple(kr1.inverse_prefix(v) for v in columns)
    result = 0
    for h, k in zip(heights, heights[1:] + (0,)):
        if h == k:
            continue  # the written universal diagonal lemma is a premise
        if (h, k) not in FORCED:
            raise ValueError('transition not forced by this certificate')
        result += FORCED[h, k]
    return result


def independently_literal_u(parts):
    if not isinstance(parts, tuple) or any(type(v) is not int or v <= 0 for v in parts):
        return False
    if any(x < y for x, y in zip(parts, parts[1:])):
        return False
    prefix = (0, 1, 3, 6, 8)
    heights = []
    for value in parts:
        quotient, residue = divmod(value, 9)
        if residue not in prefix:
            return False
        heights.append(5 * quotient + prefix.index(residue))
    return all(0 <= h - k <= 4 for h, k in zip(heights, heights[1:] + [0]))


def verify(ceiling=12):
    if type(ceiling) is not int or not 10 <= ceiling <= 12:
        raise ValueError('certificate ceiling must be an integer from ten through twelve')
    freeze = check_freeze()
    report = {'program': 'RR004', 'ceiling': ceiling,
              'started_utc': datetime.now(timezone.utc).isoformat(),
              'full_bijection': 'unresolved',
              'candidate_status': 'transition_additive_pair_count_refuted',
              'map_pilot': 'not_applicable_no_candidate_maps',
              'assurance': 'finite certificate checks; written argument and separate review required',
              'source_sha256': freeze['source_sha256'], 'cases': []}
    domains = {}
    for n in range(ceiling + 1):
        from_w = {kr1.weighted_columns(w) for w in kr1.weighted_partitions(n)}
        literal = {tuple(reversed(p)) for p in kr1.ordinary_partitions(n)
                   if independently_literal_u(tuple(reversed(p)))}
        require(from_w == literal, 'independent literal U mismatch at weight ' + str(n))
        clusters = tuple(kr1.cluster_data(n))
        require(all(c.weight == n for c in clusters), 'cluster weight mismatch')
        domains[n] = from_w, clusters
        report['cases'].append({'weight': n, 'actual_U': len(from_w),
                                'actual_C': len(clusters),
                                'C_with_b_positive': sum(c.b > 0 for c in clusters)})
        # Count agreement is descriptive and never promotes completion.
    expected_u = {
        1: {(1,)},
        3: {(3,), (1, 1, 1)},
        4: {(3, 1), (1,) * 4},
        7: {(1,) * 7, (3,) + (1,) * 4, (3, 3, 1), (6, 1)},
    }
    for n, expected in expected_u.items():
        require(domains[n][0] == expected, 'written small U list mismatch')
    expected_pairs = {
        3: [kr1.ClusterData(0, 1, (), (0,))],
        4: [],
        7: [kr1.ClusterData(1, 1, (0,), (0,))],
        9: [kr1.ClusterData(0, 1, (), (2,)), kr1.ClusterData(1, 1, (2,), (0,))],
    }
    for n, expected in expected_pairs.items():
        require([c for c in domains[n][1] if c.b] == expected, 'written C fiber mismatch')
    witnesses = ((3, 3, 3), (6, 1, 1, 1), (6, 3), (6, 3, 1))
    require([forced_pair_charge(u) for u in witnesses] == [1, 1, 0, -1],
            'forced signed-charge contradiction changed')
    for u in witnesses:
        require(u in domains[sum(u)][0], 'obstruction witness outside actual U')
    require(kr1.ClusterData(3, 0, (0, 0, 0), ()).weight == 9,
            'first omitted zero core changed')
    for malformed in ((9,), (10,), (10, 1), (11,), (3, 6), (True,)):
        try:
            forced_pair_charge(malformed)
        except ValueError:
            pass
        else:
            raise AssertionError('malformed U accepted: ' + repr(malformed))
    report.update(status='obstruction_certificate_checks_passed_KR1_unresolved',
                  forced_charges=[{'heights': edge, 'charge': value} for edge, value in FORCED.items()],
                  witnesses=[{'U': u, 'weight': sum(u),
                              'forced_b': forced_pair_charge(u)} for u in witnesses],
                  weight9_pair_targets=[asdict(c) for c in expected_pairs[9]],
                  universal_diagonal_lemma='written argument only, not established by finite checks',
                  weight30_sweep='not_run_no_viable_map_candidate')
    check_freeze()
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ceiling', type=int, default=12)
    parser.add_argument('--require-bijection', action='store_true')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error('refusing to overwrite evidence')
    start = time.monotonic()
    try:
        report = verify(args.ceiling)
        code = 2 if args.require_bijection else 0
        if code:
            report['required_completion_failure'] = 'No U-C maps or full KR1 proof; obstruction only'
    except (AssertionError, ValueError, OSError, KeyError) as exc:
        report = {'program': 'RR004', 'status': 'failed', 'error': str(exc)}
        code = 1
    report['elapsed_seconds'] = time.monotonic() - start
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as output:
        output.write(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ('status', 'elapsed_seconds')}))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
