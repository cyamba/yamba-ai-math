"""Distinct final critic: independently reconstruct all finite n=6 obligations.

No author verification enumerator is used. Entry maps are tested as black
boxes, with every source and tagged positive independently generated.
"""
from collections import Counter
from itertools import combinations
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PACKET = HERE.parent/'tableau'
sys.path.insert(0,str(PACKET))
spec = importlib.util.spec_from_file_location('initial_critic',HERE/'tableau-check.py')
independent = importlib.util.module_from_spec(spec)
spec.loader.exec_module(independent)
import revision_layers as layers
import structural as original

EXPECTED_FREEZE = '4916798c10b6d26d5fad6abe3691f5aa6a97156a986f7db6e055ce6482b392d4'
NEGATIVE = ((5,1),(4,2),(3,1,1,1),(2,2,1,1))
POSITIVE = (('row0',(6,)),('row1',(6,)),('411',(4,1,1)),
            ('321',(3,2,1)),('21111',(2,1,1,1,1)))
SHAPES = dict(POSITIVE)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pins():
    assert sha(PACKET/'revision-freeze.json') == EXPECTED_FREEZE
    freeze = json.loads((PACKET/'revision-freeze.json').read_text())
    assert len(freeze['sha256']) == 80
    assert all(sha(ROOT/name) == pin for name,pin in freeze['sha256'].items())
    independent.verify_pins()
    initial_critic = json.loads((HERE/'tableau-review-final-pins.json').read_text())
    assert all(sha(ROOT/name) == pin for name,pin in initial_critic['sha256'].items())
    historical = json.loads((PACKET/'structural-freeze.json').read_text())
    assert sha(PACKET/'structural-freeze.json') == 'ab63370a9324cc714b03b49d53666b010d0ed11af15712a96f3691a7203c19be'
    mismatches = []
    for name,pin in historical['sha256'].items():
        if sha(PACKET/name) != pin:
            mismatches.append(name)
    assert sorted(mismatches) == ['structural.py','verify_structural.py']
    assert sha(PACKET/'structural-initial.py') == historical['sha256']['structural.py']
    assert sha(PACKET/'revision-recovered-initial-verifier.py') == historical['sha256']['verify_structural.py']
    failed_receipt = json.loads((HERE.parent/'integrity-progress.json').read_text())
    assert failed_receipt['status'] == 'fail'
    assert len(failed_receipt['failures']) == 2
    return freeze['sha256'], mismatches


def clear():
    for f in (layers.forward,layers.inverse,layers.preimages):
        f.cache_clear()


def retained(rows,moved):
    return Counter(tuple(x for x in row if x not in moved) for row in rows
                   if any(x not in moved for x in row))


def moves(source,target):
    for count in range(7):
        for subset in combinations(range(1,7),count):
            if retained(source,set(subset)) == retained(target,set(subset)):
                return count
    raise AssertionError('all-label deletion must agree')


def previous_assignment(h,source):
    shape = tuple(map(len,source))
    if shape == (5,1):
        return original.forward(h,'hook',source)
    if shape == (4,2):
        return original.forward(h,'two',source)
    if shape == (2,2,1,1):
        branch = original.triangle_source(h,source)
        return original.forward(h,branch,source) if branch is not None else None
    return None


def run():
    before,mismatches = pins()
    sectors = [s for shape in independent.partitions(6)
               for s in independent.determinant(shape)]
    assert len(sectors) == 85
    e51 = [s for s in sectors if s['target'] == (5,1)]
    assert len(e51) == 9
    assert Counter((s['shape'],s['sign']) for s in e51) == Counter({
        ((6,),1):2,((5,1),-1):1,((4,2),-1):1,((4,1,1),1):1,
        ((3,2,1),1):1,((3,1,1,1),-1):1,((2,2,1,1),-1):1,
        ((2,1,1,1,1),1):1})
    saved_inventory = json.loads((PACKET/'inventory-through6.json').read_text())[6]
    saved_sectors = [s for value in saved_inventory['targets'].values() for s in value]
    assert Counter(map(independent.canonical_sector,sectors)) == Counter(map(independent.canonical_sector,saved_sectors))
    totals,layer_counts,first_layer = Counter(),Counter(),Counter()
    reports = []
    for h in independent.vectors(6):
        clear()
        relation = frozenset((a,b) for a in range(1,7) for b in range(1,7) if h[a-1] < b)
        source_tables = {shape:tuple(independent.tableaux(relation,6,shape)) for shape in NEGATIVE}
        positive_tables = {shape:tuple(independent.tableaux(relation,6,shape)) for _,shape in POSITIVE}
        sources = tuple(s for shape in NEGATIVE for s in source_tables[shape])
        source_set = set(sources)
        positives = tuple((tag,t) for tag,shape in POSITIVE for t in positive_tables[shape])
        per_h = Counter({'negative':len(sources),'positive':len(positives)})
        final = {}
        for level in range(23):
            images = {}
            for source in reversed(sources):
                output = layers.forward(h,source,level)
                if output is None:
                    continue
                tag,target = output
                assert tag in SHAPES
                assert independent.valid(relation,6,target,SHAPES[tag]), ('invalid_image',h,level,source,output)
                assert independent.inversion(relation,source) == independent.inversion(relation,target), ('degree',h,level,source,output)
                assert output not in images, ('collision',h,level,source,images.get(output),output)
                images[output] = source
                assert layers.inverse(h,tag,target,level) == source, ('left_inverse',h,level,source,output)
                if level == 22:
                    final[source] = output
            layer_counts[level] += len(images)
            for tag,target in positives:
                recovered = layers.inverse(h,tag,target,level)
                assert (recovered is not None) == ((tag,target) in images), ('recognition',h,level,tag,target,recovered)
                if recovered is not None:
                    assert recovered in source_set, ('not_negative',h,level,recovered)
                    assert layers.forward(h,recovered,level) == (tag,target), ('right_inverse',h,level,tag,target,recovered)
            if level:
                for source in sources:
                    prescribed = layers.prescribed(h,source,level)
                    if (prescribed is not None and layers.forward(h,source,level-1) is None
                            and layers.inverse(h,*prescribed,level-1) is None):
                        extracted = layers.preimages(h,*prescribed,level)
                        assert source in extracted, ('incomplete_slot_reconstruction',h,level,source,prescribed)
                        assert len(extracted) <= 36
            if level == 22:
                assert len(final) == len(sources), ('unmapped_negative',h)
        for shape,family in source_tables.items():
            totals['source_'+''.join(map(str,shape))] += len(family)
        for tag,shape in POSITIVE:
            totals['positive_'+tag] += len(positive_tables[shape])
        for source,output in final.items():
            old = previous_assignment(h,source)
            if old is not None:
                assert output == old, ('changed_original',h,source,old,output)
                per_h['original_preserved'] += 1
            count = moves(source,output[1])
            assert 1 <= count <= 3, ('outside_frozen_movement_family',h,source,output,count)
            per_h['moved_'+str(count)] += 1
            for level in range(23):
                if layers.forward(h,source,level) is not None:
                    first_layer[level] += 1
                    break
        # Erase every memoized answer and reverse public call order: inverse
        # first, then forward. This tests warm-order and cold-order agreement.
        expected = {output:source for source,output in final.items()}
        clear()
        for tag,target in reversed(positives):
            assert layers.inverse(h,tag,target) == expected.get((tag,target)), ('cache_order_inverse',h,tag,target)
        for source in sources:
            assert layers.forward(h,source) == final[source], ('cache_order_forward',h,source)
        per_h['mapped'] = len(final)
        per_h['recognized'] = len(expected)
        per_h['unmatched_positive'] = len(positives)-len(expected)
        totals.update(per_h)
        reports.append({'h':h,**per_h})
    after,_ = pins()
    assert before == after
    assert len(reports) == 132
    assert totals['negative'] == totals['mapped'] == totals['recognized'] == 3980
    assert totals['positive'] == 6800
    assert totals['original_preserved'] == 151
    assert [totals['moved_'+str(i)] for i in (1,2,3)] == [3242,712,26]
    result = {'status':'finite_exact_passed','n':6,'h_vectors':132,
              'independent_enumeration':True,'failure_count':0,
              'totals':dict(totals),'domain_size_by_layer':dict(sorted(layer_counts.items())),
              'first_assigned_layer_counts':dict(sorted(first_layer.items())),
              'all_results':reports,'raw_djt_occurrences_n6':85,'e51_occurrences':9,
              'cache_clearing_and_reversed_call_order_agreed':True,
              'revision_80_pins_and_initial17_pins_unchanged':True,
              'historical_preliminary_mismatches':mismatches,
              'historical_original_bytes_recovered':True,
              'historical_failure_receipt_preserved':True,
              'assurance':'Ordinary partial-injection proof reviewed separately; totality here is exhaustive n=6 evidence, not symbolic totality or formal certification.'}
    (HERE/'tableau-final-result.json').write_text(json.dumps(result,indent=2)+'\n')
    deps = dict(before)
    deps.update({str(p.relative_to(ROOT)):sha(p) for p in [
        PACKET/'revision-freeze.json',HERE/'tableau-check.py',Path(__file__),
        HERE.parent/'historical-pin-recovery.json',HERE.parent/'integrity-progress.json',
        PACKET/'structural-freeze.json']})
    (HERE/'tableau-final-dependencies.json').write_text(json.dumps(deps,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'all_results'},indent=2))


if __name__ == '__main__':
    run()
