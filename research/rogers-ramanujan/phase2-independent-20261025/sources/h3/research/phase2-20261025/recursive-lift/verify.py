"""Frozen Phase 2 exact grammar verification, maximum input/output weight 40."""
import argparse
from collections import Counter
import json
from pathlib import Path
import sys

from triadic import (Boundary, C, EMPTY, Node, c_exact, decode, depth, encode,
                     grammar_exact, residual_weight, step, tree_weight, unstep)

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'rogers-ramanujan' / 'checks'))
import kr1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bound', type=int, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.bound not in (12, 30, 40):
        parser.error('frozen gates are 12,30,40')
    rows, sector_counts, edge_cases = [], Counter(), Counter()
    maximum_depth = 0
    for n in range(args.bound + 1):
        sources = tuple(c_exact(n))
        canonical = tuple(kr1.cluster_data(n))
        assert {(c.a, c.b, c.mu, c.nu) for c in sources} == {
            (c.a, c.b, c.mu, c.nu) for c in canonical}
        forward = set()
        for source in sources:
            tree = encode(source)
            assert decode(tree) == source
            assert tree_weight(tree) == n
            assert tree not in forward
            forward.add(tree)
            maximum_depth = max(maximum_depth, depth(tree))
            sector_counts[source.a, source.b] += 1
            if source != EMPTY:
                boundary, child = step(source)
                assert unstep(boundary, child) == source
                assert 3 * child.weight + residual_weight(boundary, child) == n
                assert child.a == source.b and child.b == source.a // 3
                edge_cases['nonterminal'] += 1
                edge_cases['zero_residual'] += residual_weight(boundary, child) == 0
                edge_cases['positive_trits'] += any(boundary.trits)
                edge_cases['zero_in_mu'] += 0 in source.mu
                edge_cases['repeated_mu'] += len(set(source.mu)) < len(source.mu)
                edge_cases['repeated_nu'] += len(set(source.nu)) < len(source.nu)
        reverse = grammar_exact(n)
        assert len(reverse) == len(set(reverse))
        assert set(reverse) == forward
        for tree in reverse:
            source = decode(tree)
            assert source.weight == n
            assert encode(source) == tree
        rows.append({'weight': n, 'literal_C': len(sources), 'independent_valid_grammar': len(reverse)})
    bad = (Node(Boundary(0, (), ()), None), Node(Boundary(3, (), ()), None),
           Node(Boundary(1, (), ()), None), Node(Boundary(1, (-1,), ()), None),
           Node(Boundary(1, (0,), (0,)), None))
    rejected = 0
    for tree in bad:
        try:
            decode(tree)
        except ValueError:
            rejected += 1
        else:
            raise AssertionError('malformed grammar accepted')
    result = {'status': 'empirical transcription verification; not a U/C map',
              'bound': args.bound, 'total_literal_C': sum(r['literal_C'] for r in rows),
              'total_independent_valid_grammar': sum(r['independent_valid_grammar'] for r in rows),
              'both_identities': True, 'weight_identity': True,
              'independent_reverse_language_enumeration': True,
              'maximum_depth': maximum_depth, 'malformed_nodes_rejected': rejected,
              'edge_case_counts': dict(edge_cases),
              'sector_counts': [{'a': a, 'b': b, 'count': count}
                                for (a, b), count in sorted(sector_counts.items())],
              'by_weight': rows}
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
