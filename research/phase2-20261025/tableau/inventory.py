"""Literal Dual Jacobi--Trudi sector inventory. Standard library only."""
from __future__ import annotations
from collections import Counter, defaultdict
from itertools import permutations
import argparse
import json
from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / 'research/partitions/checks'))
import tableaux as tb


def occurrences(shape):
    """Keep sigma, e-index sequence and sign, including canceled copies."""
    if not shape:
        yield {'shape': (), 'sigma': (), 'indices': (), 'target': (), 'sign': 1}
        return
    columns = tuple(sum(x > j for x in shape) for j in range(shape[0]))
    for sigma in permutations(range(len(columns))):
        indices = tuple(x - i + sigma[i] for i, x in enumerate(columns))
        if min(indices) < 0:
            continue
        degree = sum(a > b for i, a in enumerate(sigma) for b in sigma[i+1:])
        yield {'shape': shape, 'sigma': sigma, 'indices': indices,
               'target': tuple(sorted((x for x in indices if x), reverse=True)),
               'sign': (-1) ** degree}


def inventory(n):
    result = defaultdict(list)
    check = {}
    for shape in tb.partitions(n):
        aggregate = Counter()
        for sector in occurrences(shape):
            result[sector['target']].append(sector)
            aggregate[sector['target']] += sector['sign']
        assert {k: v for k, v in aggregate.items() if v} == tb.djt_terms(shape)
        check[str(shape)] = {str(k): v for k, v in aggregate.items() if v}
    return {'n': n, 'hessenberg_vectors': sum(1 for _ in tb.hessenberg_vectors(n)),
            'targets': {str(k): v for k, v in sorted(result.items(), reverse=True)},
            'coalesced': check}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-n', type=int, required=True, choices=range(7))
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = [inventory(n) for n in range(args.max_n + 1)]
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'vectors': [(r['n'], r['hessenberg_vectors']) for r in result],
                      'main_sectors': result[-1]['targets'].get(str((args.max_n-1, 1)), [])}, indent=2))
