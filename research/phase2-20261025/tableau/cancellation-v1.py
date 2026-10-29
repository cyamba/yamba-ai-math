"""Frozen bounded candidate graph tests, not a universal positivity algorithm.

Family 1: one cell is deleted from a row, inserted into another or a new row;
row blocks may be permuted to obtain a partition shape. Family 2: add recuts
of the unchanged reading word after permuting whole source row blocks.
Family 3: unrestricted inversion-fiber matching, a diagnostic only.
Every graph candidate must pass literal tableau validity and inv_G equality.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import permutations
import argparse
import hashlib
import json
from pathlib import Path
import sys

from inventory import occurrences, tb


def signed_sectors(n, target):
    """Cancel opposite raw sigma copies with the same shape by identity."""
    positive, negative, identity = [], [], []
    all_raw = []
    for shape in tb.partitions(n):
        raw = [s for s in occurrences(shape) if s['target'] == target]
        all_raw.extend(raw)
        pos = [s for s in raw if s['sign'] > 0]
        neg = [s for s in raw if s['sign'] < 0]
        cancel = min(len(pos), len(neg))
        identity.extend(zip(pos[:cancel], neg[:cancel]))
        positive.extend(pos[cancel:])
        negative.extend(neg[cancel:])
    return positive, negative, identity, all_raw


def sector_key(s):
    return (s['shape'], s['sigma'])


def row_orders(rows):
    """All whole-row permutations with partition lengths, without duplicates."""
    return sorted({p for p in permutations(rows)
                   if all(len(a) >= len(b) for a, b in zip(p, p[1:]))})


@lru_cache(None)
def one_cell(rows):
    result = set()
    for i, row in enumerate(rows):
        for j, label in enumerate(row):
            remainder = row[:j] + row[j+1:]
            base = list(rows[:i]) + ([remainder] if remainder else []) + list(rows[i+1:])
            # A new singleton row, or any insertion position in another row.
            result.update(row_orders(tuple(base) + ((label,),)))
            for k, dest in enumerate(base):
                for index in range(len(dest)+1):
                    out = tuple(base[:k]) + (dest[:index] + (label,) + dest[index:],) + tuple(base[k+1:])
                    result.update(row_orders(out))
    result.discard(rows)
    return tuple(sorted(result))


@lru_cache(None)
def word_recuts(rows, shapes):
    result = set()
    for permuted_rows in set(permutations(rows)):
        word = sum(permuted_rows, ())
        for shape in shapes:
            start, out = 0, []
            for length in shape:
                out.append(word[start:start+length])
                start += length
            result.add(tuple(out))
    result.discard(rows)
    return tuple(sorted(result))


def maximum_matching(adjacency, sources):
    """Deterministic finite augmenting paths; reverse dictionary is its inverse.

    This operation enumerates a complete finite family and is NOT a proposed
    universal structural injection. A failed search returns an exact Hall
    witness from its alternating reachable sets.
    """
    owner = {}
    def augment(source, seen_positive, seen_negative):
        seen_negative.add(source)
        for target in adjacency[source]:
            if target in seen_positive:
                continue
            seen_positive.add(target)
            previous = owner.get(target)
            if previous is None or (previous not in seen_negative and
                                    augment(previous, seen_positive, seen_negative)):
                owner[target] = source
                return True
        return False
    failed = None
    for source in sources:
        seen_p, seen_n = set(), set()
        if not augment(source, seen_p, seen_n) and failed is None:
            # This witness is relative to the partial matching at failure;
            # the reachable set has fewer neighbors than negative vertices.
            neighbors = {t for s in seen_n for t in adjacency[s]}
            assert len(neighbors) < len(seen_n)
            failed = {'source': source, 'negative_vertices': sorted(seen_n),
                      'positive_neighbors': sorted(neighbors)}
    mapping = {source: target for target, source in owner.items()}
    assert len(mapping) == len(owner)
    return mapping, failed


def serialize_object(obj, sectors):
    sector, rows = obj
    return {'sector': sectors[sector], 'tableau': rows}


def test_h(h, target):
    n = len(h)
    pos, neg, identity, raw = signed_sectors(n, target)
    shapes = set(s['shape'] for s in pos + neg)
    tabs = {shape: tuple(tb.tableaux(h, shape)) for shape in shapes}
    degree = {t: tb.inv_g(h, t) for family in tabs.values() for t in family}
    positives = tuple((i, t) for i, s in enumerate(pos) for t in tabs[s['shape']])
    negatives = tuple((i, t) for i, s in enumerate(neg) for t in tabs[s['shape']])
    positive_index = defaultdict(list)
    for obj in positives:
        positive_index[obj[1]].append(obj)
    positive_shapes = tuple(sorted({s['shape'] for s in pos}, reverse=True))
    by_degree = defaultdict(list)
    for obj in positives:
        by_degree[degree[obj[1]]].append(obj)
    family_stats = []
    for family in (1, 2, 3):
        adjacency = {}
        for source in negatives:
            rows = source[1]
            if family == 3:
                candidates = by_degree[degree[rows]]
            else:
                candidates = []
                generated = set(one_cell(rows))
                if family == 2:
                    generated.update(word_recuts(rows, positive_shapes))
                for out in sorted(generated):
                    if out in positive_index and degree[out] == degree[rows]:
                        candidates.extend(positive_index[out])
            adjacency[source] = tuple(candidates)
        # Finite greedy comparison is useful because external reports used it.
        greedy, used = {}, set()
        for source in negatives:
            out = next((t for t in adjacency[source] if t not in used), None)
            if out is not None:
                greedy[source] = out
                used.add(out)
        matched, failure = maximum_matching(adjacency, negatives)
        for src, out in matched.items():
            assert degree[src[1]] == degree[out[1]]
            assert tb.validates(h, src[1], neg[src[0]]['shape'])
            assert tb.validates(h, out[1], pos[out[0]]['shape'])
        failure_serialized = None
        if failure:
            failure_serialized = {
                'source': serialize_object(failure['source'], neg),
                'negative_vertices': [serialize_object(o, neg) for o in failure['negative_vertices']],
                'positive_neighbors': [serialize_object(o, pos) for o in failure['positive_neighbors']],
            }
        digest = hashlib.sha256(json.dumps(sorted(matched.items()), sort_keys=True).encode()).hexdigest()
        family_stats.append({'family': family, 'negative_objects': len(negatives),
                             'positive_objects': len(positives), 'matched': len(matched),
                             'greedy_matched': len(greedy),
                             'edges': sum(map(len, adjacency.values())),
                             'mapping_sha256': digest, 'first_failure': failure_serialized})
    return {'h': h, 'target': target, 'raw_sectors': len(raw),
            'identity_sector_pairs': len(identity),
            'identity_object_pairs': sum(len(tuple(tb.tableaux(h, p['shape']))) for p, _ in identity),
            'families': family_stats}


def run(max_n):
    sizes, all_results = [], []
    for n in range(2, max_n+1):
        target = (n-1, 1)
        data = [test_h(h, target) for h in tb.hessenberg_vectors(n)]
        summary = {'n': n, 'hessenberg_vectors': len(data), 'families': []}
        for family in (1, 2, 3):
            rows = [r['families'][family-1] for r in data]
            failed = [(r['h'], r['families'][family-1]['first_failure']) for r in data
                      if r['families'][family-1]['first_failure'] is not None]
            summary['families'].append({
                'family': family, 'negative_objects': sum(r['negative_objects'] for r in rows),
                'positive_objects': sum(r['positive_objects'] for r in rows),
                'matched': sum(r['matched'] for r in rows),
                'greedy_matched': sum(r['greedy_matched'] for r in rows),
                'failed_vectors': len(failed), 'first_failure': failed[0] if failed else None})
        sizes.append(summary)
        all_results.extend(data)
    return {'status': 'finite_candidate_graph_evidence', 'maximum_n': max_n,
            'scope': 'e_(n-1,1); n<=6 natural unit interval orders; literal signed DJT sectors',
            'families': {'1': 'one cell transfer plus whole row permutations',
                         '2': 'family1 plus unchanged word recuts after whole row permutations',
                         '3': 'unrestricted inversion-fiber matching, diagnostic only'},
            'universal_structural_injection': False,
            'summary': sizes, 'all_results': all_results}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-n', type=int, required=True, choices=range(2, 7))
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = run(args.max_n)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result['summary'], indent=2))
