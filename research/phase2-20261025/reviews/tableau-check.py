"""Distinct critic: independent finite reconstruction, restricted to n <= 6.

The author map is a black box; this file does not import its tableau,
Hessenberg, inversion, determinant, or validity generators. The separate
pre-existing coloring oracle supplies the other polynomial calculation.
"""
from collections import Counter, defaultdict
from itertools import combinations
import hashlib
import importlib.util
import json
from pathlib import Path
import random
import sys

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
PACKET = HERE.parent / 'tableau'
sys.path.insert(0, str(PACKET))
import structural as author
sys.path.insert(0, str(ROOT / 'research/partitions/checks'))
import coloring_oracle


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_pins():
    freeze = json.loads((PACKET / 'freeze.json').read_text())
    found = {name: digest(PACKET / name) for name in freeze['sha256']}
    assert found == freeze['sha256'], {'frozen_dependency_mismatch': found}
    assert found['author.md'] == '9e02329dfc61090275361070503328219a287d9f1f5f720de2e1842a71c3dd42'
    return found


def partitions(n, cap=None):
    if not n:
        yield ()
        return
    for first in range(min(n, n if cap is None else cap), 0, -1):
        for tail in partitions(n-first, first):
            yield (first,) + tail


def vectors(n, prefix=()):
    if len(prefix) == n:
        yield prefix
        return
    lower = max(len(prefix)+1, prefix[-1] if prefix else 1)
    for value in range(lower, n+1):
        yield from vectors(n, prefix+(value,))


def determinant(shape):
    """Recursive determinant expansion retaining each chosen-column word."""
    column_heights = tuple(sum(row >= col for row in shape)
                           for col in range(1, max(shape, default=0)+1))
    width = len(column_heights)
    def visit(row, chosen, indices, sign):
        if row == width:
            yield {'shape': shape, 'sigma': chosen, 'indices': indices,
                   'target': tuple(sorted((x for x in indices if x), reverse=True)),
                   'sign': sign}
            return
        for col in range(width):
            if col in chosen:
                continue
            index = column_heights[row] - row + col
            if index < 0:
                continue
            new_sign = sign * (-1 if sum(old > col for old in chosen) % 2 else 1)
            yield from visit(row+1, chosen+(col,), indices+(index,), new_sign)
    yield from visit(0, (), (), 1)


def canonical_sector(s):
    return (tuple(s['shape']), tuple(s['sigma']), tuple(s['indices']),
            tuple(s['target']), s['sign'])


def tableaux(relation, n, shape):
    """Backtrack cells with independent row and adjacent-column conditions."""
    if not shape:
        yield ()
        return
    positions = tuple((r,c) for r, length in enumerate(shape) for c in range(length))
    rows = [[] for _ in shape]
    def visit(index, remaining):
        if index == n:
            yield tuple(tuple(row) for row in rows)
            return
        r, c = positions[index]
        for entry in remaining:
            if c and (rows[r][-1], entry) not in relation:
                continue
            if r and (entry, rows[r-1][c]) in relation:
                continue
            rows[r].append(entry)
            yield from visit(index+1, tuple(x for x in remaining if x != entry))
            rows[r].pop()
    yield from visit(0, tuple(range(1, n+1)))


def valid(relation, n, rows, shape):
    if tuple(map(len, rows)) != shape or sorted(sum(rows, ())) != list(range(1,n+1)):
        return False
    if any((a,b) not in relation for row in rows for a,b in zip(row,row[1:])):
        return False
    return not any((below, above) in relation for top, bottom in zip(rows,rows[1:])
                   for above, below in zip(top,bottom))


def inversion(relation, rows):
    row_index = {x: r for r, row in enumerate(rows) for x in row}
    return sum(row_index[b] < row_index[a]
               for a,b in combinations(sorted(row_index), 2)
               if (a,b) not in relation and (b,a) not in relation)


def check_structure(relation, tables):
    author.lt = lambda _h, a, b: (a,b) in relation
    seen, counts = {}, Counter()
    for tag, shape in [('hook',(5,1)), ('two',(4,2)), ('triangle',(2,2,1,1))]:
        for source in tables[shape]:
            actual = author.triangle_source(None, source) if tag == 'triangle' else tag
            if actual is None:
                continue
            output = author.forward(None, actual, source)
            outtag, image = output
            outshape = author.destination_shape(6, outtag)
            assert valid(relation, 6, image, outshape), ('invalid_image',source,output)
            assert inversion(relation,source) == inversion(relation,image), ('degree',source,output)
            assert author.inverse(None,outtag,image) == (actual,source), ('inverse',source,output)
            assert output not in seen, ('collision',source,seen.get(output),output)
            seen[output] = (actual,source)
            counts['source_'+tag] += 1
            counts['destination_'+outtag] += 1
    for tag in ['row0','row1','411','321','21111']:
        for image in tables[author.destination_shape(6,tag)]:
            recovered = author.inverse(None,tag,image)
            assert (recovered is not None) == ((tag,image) in seen), ('image_language',tag,image,recovered)
            if recovered is not None:
                srctag, source = recovered
                shape = {'hook':(5,1),'two':(4,2),'triangle0':(2,2,1,1),'triangle1':(2,2,1,1)}[srctag]
                assert valid(relation,6,source,shape), ('invalid_inverse',tag,image,recovered)
                assert author.forward(None,srctag,source) == (tag,image), ('forward_again',tag,image,recovered)
                counts['recognized_images'] += 1
    counts['sources'] = len(seen)
    return counts


def trim(poly):
    while poly and not poly[-1]:
        poly.pop()
    return tuple(poly)


def sample_general_posets():
    """Deterministic n=6 sanity cases beyond the natural-unit-interval class."""
    rng = random.Random(20261025)
    seen = set()
    for i in range(256):
        labels = list(range(1,7))
        rng.shuffle(labels)
        relation = {(a,b) for a,b in combinations(range(6),2)
                    if rng.random() < (0.2,0.4,0.6,0.8)[i%4]}
        for middle in range(6):
            relation |= {(a,c) for a in range(6) for c in range(6)
                         if (a,middle) in relation and (middle,c) in relation}
        relabeled = frozenset((labels[a],labels[b]) for a,b in relation)
        if relabeled not in seen:
            seen.add(relabeled)
            yield relabeled


def run():
    before = verify_pins()
    baseline = json.loads((PACKET/'inventory-through6.json').read_text())
    inventories = {}
    e51_sectors = None
    for n in range(7):
        sectors = [s for shape in partitions(n) for s in determinant(shape)]
        saved = [s for value in baseline[n]['targets'].values() for s in value]
        assert Counter(map(canonical_sector,sectors)) == Counter(map(canonical_sector,saved))
        inventories[n] = len(sectors)
        if n == 6:
            e51_sectors = [s for s in sectors if s['target'] == (5,1)]
            assert len(e51_sectors) == 9
    structure = Counter()
    sizes = []
    for n in range(7):
        count = 0
        all_sectors = {shape: list(determinant(shape)) for shape in partitions(n)}
        for h in vectors(n):
            count += 1
            relation = frozenset((a,b) for a in range(1,n+1) for b in range(1,n+1)
                                 if h[a-1] < b)
            tables = {shape: tuple(tableaux(relation,n,shape)) for shape in all_sectors}
            polynomial = defaultdict(Counter)
            for shape, family in tables.items():
                weights = Counter(inversion(relation,t) for t in family)
                terms = Counter()
                for sector in all_sectors[shape]:
                    terms[sector['target']] += sector['sign']
                for target, sign in terms.items():
                    for degree, coefficient in weights.items():
                        polynomial[target][degree] += sign*coefficient
            expansion = {target:p for target, coeff in polynomial.items()
                         if (p := trim([coeff[d] for d in range(max(coeff,default=-1)+1)]))}
            assert expansion == coloring_oracle.elementary_expansion(h), ('coloring_disagreement',h)
            assert all(v >= 0 for poly in expansion.values() for v in poly), ('negative_coefficient',h)
            if n == 6:
                counts = check_structure(relation,tables)
                structure.update(counts)
                for sector in e51_sectors:
                    structure['all_negative' if sector['sign'] < 0 else 'all_positive'] += len(tables[sector['shape']])
        sizes.append({'n':n,'vectors':count,'coloring_agreements':count})
    general = Counter()
    shapes = [(5,1),(4,2),(2,2,1,1),(6,),(4,1,1),(3,2,1),(2,1,1,1,1)]
    for relation in sample_general_posets():
        tabs = {shape: tuple(tableaux(relation,6,shape)) for shape in shapes}
        general.update(check_structure(relation,tabs))
        general['distinct_posets'] += 1
    after = verify_pins()
    assert before == after
    dependencies = {str((PACKET/name).relative_to(ROOT)): pin for name,pin in before.items()}
    dependencies.update({str(p.relative_to(ROOT)):digest(p) for p in [PACKET/'freeze.json',
        ROOT/'research/partitions/checks/coloring_oracle.py',Path(__file__)]})
    result = {'status':'finite_exact_passed', 'failure_count':0,
              'proof_assurance':'Independent ordinary semantic review is recorded separately; no formal checker.',
              'sizes':sizes, 'vector_total':sum(x['vectors'] for x in sizes),
              'literal_sector_counts':inventories,'e51_raw_sectors':e51_sectors,
              'structural_n6':dict(structure),'general_poset_n6_sanity':dict(general),
              'frozen_dependencies_unchanged':True}
    (HERE/'tableau-result.json').write_text(json.dumps(result,indent=2)+'\n')
    (HERE/'tableau-dependencies.json').write_text(json.dumps(dependencies,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    run()
