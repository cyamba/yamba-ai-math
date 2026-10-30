"""Finite check of the reviewed even-target fixed-determinant corollary."""
from collections import Counter
import hashlib
import json
from math import gcd
from pathlib import Path
import platform
import time


def main():
    started = time.perf_counter()
    failures = []
    evaluations = 0
    groups = 0
    maximum = 0
    for target in range(2, 31, 2):
        for u_scale in (1, 2, 3):
            for v_scale in (1, 3, 8):
                points = [(u, v) for u in range(u_scale, 16 * u_scale + 1)
                          for v in range(v_scale, 2 * v_scale + 1)
                          if gcd(u, target) == 1]
                sectors = {}
                for u, v in points:
                    sectors.setdefault(v * pow(u, -1, target) % target, []).append((u, v))
                for candidates in sectors.values():
                    for u, v in candidates:
                        if gcd(u, v) != 1:
                            continue
                        counts = Counter(u * b - v * a for a, b in candidates)
                        evaluations += len(candidates)
                        groups += len(counts)
                        current = max(counts.values(), default=0)
                        maximum = max(maximum, current)
                        if current > 1:
                            failures.append({'H': target, 'U': u_scale, 'V': v_scale,
                                             'P': [u, v], 'count': current})
    path = Path(__file__)
    result = {'status': 'passed_exact_unit_edge_check' if not failures else 'failed',
              'H_even_range': [2, 30], 'U_values': [1, 2, 3], 'V_values': [1, 3, 8],
              'pair_evaluations': evaluations, 'determinant_groups': groups,
              'maximum_unit_first_partner_count': maximum, 'failures': failures,
              'source_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
              'python': platform.python_version(), 'elapsed_seconds': time.perf_counter() - started,
              'scope': 'Both endpoints have first coordinate coprime to H. This differs from the larger endpoint pool in the frozen main checker. No operator cancellation or infinite conclusion follows from a finite check.'}
    path.with_name('edge-unit-results.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
