"""Finite impossibility certificate for fixed transition-additive pair count.

This is a checked transcription of a written obstruction, not a KR1 map.
"""
import argparse
from dataclasses import asdict
import json
from pathlib import Path
import time
import kr1
import rr004_verify as first

ROOT = Path(__file__).resolve().parents[3]
PHASE = ROOT / 'research/rogers-ramanujan/rr004'
WITNESSES = (
    (1,), (1, 1), (1, 1, 1), (3,), (3, 1), (3, 3), (3, 3, 3),
    (1,) * 7, (3,) + (1,) * 4, (3, 3, 1), (6, 1), (6, 1, 1, 1),
    (6, 3), (6, 3, 1),
)
CHARGES = {(1, 0): 0, (1, 1): 0, (2, 0): 1, (2, 1): 0,
           (2, 2): 0, (3, 1): 1, (3, 2): -1}


def candidate_pair_charge(u, charges):
    kr1.decode_columns(u)
    heights = tuple(kr1.inverse_prefix(value) for value in u)
    return sum(charges[h, k] for h, k in zip(heights, heights[1:] + (0,)))


def verify():
    freeze = first.check_freeze(freeze_path=PHASE / 'round-2-freeze.json')
    first.require(len(set(WITNESSES)) == 14 and max(map(sum, WITNESSES)) == 10,
                  'finite source set changed')
    for u in WITNESSES:
        kr1.decode_columns(u)
        first.require(first.independently_literal_u(u), 'nonliteral source witness')
    fibers = {n: tuple(kr1.cluster_data(n)) for n in (1, 2, 3, 4, 6, 7, 9)}
    first.require(all(c.b == 0 for n in (1, 2, 4) for c in fibers[n]),
                  'zero-b fiber premise changed')
    first.require({c.b for c in fibers[6]} == {0, 1}, 'weight-six bound changed')
    first.require(sum(c.b == 0 for c in fibers[3]) == 1 and
                  sum(c.b == 1 for c in fibers[3]) == 1, 'weight-three capacity changed')
    first.require(sum(c.b == 0 for c in fibers[7]) == 3 and
                  sum(c.b == 1 for c in fibers[7]) == 1, 'weight-seven capacity changed')
    expected9 = (kr1.ClusterData(0, 1, (), (2,)), kr1.ClusterData(1, 1, (2,), (0,)))
    first.require(tuple(c for c in fibers[9] if c.b) == expected9,
                  'weight-nine positive-b fiber changed')
    alternatives = tuple(b - 1 for b in {c.b for c in fibers[6]})
    surviving = tuple(g for g in alternatives if 2*g + 1 >= 0)
    first.require(set(alternatives) == {-1, 0} and surviving == (0,),
                  'diagonal case split incomplete')
    values = {u: candidate_pair_charge(u, CHARGES) for u in WITNESSES}
    first.require(all(values[u] == 0 for u in ((1,) * 7, (3,) + (1,) * 4, (3, 3, 1))),
                  'weight-seven capacity witnesses changed')
    first.require(values[(3, 3, 3)] == values[(6, 1, 1, 1)] == 1,
                  'weight-nine occupied targets changed')
    first.require(values[(6, 3)] == 0 and values[(6, 3, 1)] == -1,
                  'negative pair-count witness changed')
    report = {'program': 'RR004', 'status': 'finite_injection_obstruction_checks_passed',
              'full_bijection': 'unresolved', 'candidate_maps': 'absent',
              'assurance': 'exact certificate transcription; written proof and separate review control the theorem',
              'source_sha256': freeze['source_sha256'],
              'source_count': 14, 'maximum_source_weight': 10,
              'witnesses': [{'U': u, 'weight': sum(u), 'forced_b': values[u]} for u in WITNESSES],
              'diagonal_cases': [{'e22': g, 'b_333': 2*g + 1,
                                  'rejected': 2*g + 1 < 0} for g in sorted(alternatives)],
              'weight9_pair_targets': [asdict(c) for c in expected9],
              'not_claimed': ['minimal witness set', 'complete KR1', 'novelty',
                              'formal certification', 'successful bijection pilot']}
    first.check_freeze(freeze_path=PHASE / 'round-2-freeze.json')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--require-bijection', action='store_true')
    args = parser.parse_args()
    if args.output.exists():
        parser.error('refusing to overwrite evidence')
    start = time.monotonic()
    try:
        report = verify()
        code = 2 if args.require_bijection else 0
        if code:
            report['required_completion_failure'] = 'No U-C maps or full KR1 proof; finite obstruction only'
    except (AssertionError, ValueError, KeyError, OSError) as exc:
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
