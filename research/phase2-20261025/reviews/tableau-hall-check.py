"""Independent finite Hall witness by deleting one named label on both sides."""
from collections import Counter
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('critic_tableau_check', HERE/'tableau-check.py')
critic = importlib.util.module_from_spec(spec)
spec.loader.exec_module(critic)


def retained(rows, moved):
    return Counter(tuple(x for x in row if x not in moved) for row in rows
                   if any(x not in moved for x in row))


def one_label_neighbor(source, target):
    return any(retained(source,{x}) == retained(target,{x}) for x in range(1,7))


def main():
    critic.verify_pins()
    h = (1,2,4,5,6,6)
    relation = frozenset((a,b) for a in range(1,7) for b in range(1,7) if h[a-1] < b)
    sources = [((1,4),(2,3),(5,),(6,)), ((1,4),(2,5),(3,),(6,))]
    expected = ('21111', ((1,4),(2,),(3,),(5,),(6,)))
    positives = [(tag,t) for tag,shape in [('row0',(6,)),('row1',(6,)),
                  ('411',(4,1,1)),('321',(3,2,1)),('21111',(2,1,1,1,1))]
                 for t in critic.tableaux(relation,6,shape)]
    result = []
    union = set()
    for source in sources:
        assert critic.valid(relation,6,source,(2,2,1,1))
        neighbors = [out for out in positives if
                     critic.inversion(relation,out[1]) == critic.inversion(relation,source)
                     and one_label_neighbor(source,out[1])]
        assert neighbors == [expected], neighbors
        union.update(neighbors)
        result.append({'source':source,'degree':critic.inversion(relation,source),
                       'neighbors':neighbors})
    assert len(union) == 1 < len(sources)
    extra = ((1,3,5),(2,4),(6,))
    assert critic.valid(relation,6,extra,(3,2,1))
    assert critic.inversion(relation,extra) == 1
    assert not one_label_neighbor(sources[1],extra)
    critic.verify_pins()
    output = {'status':'finite_exact_passed','h':h,'sources':result,
              'Hall_counts':{'negative_vertices':2,'positive_neighbors':1},
              'triangle_extra_image':extra,'triangle_extra_degree':1,
              'scope':'Only this fixed n=6 component; the author proof supplies the conditional tuple family.'}
    (HERE/'tableau-hall-result.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))


if __name__ == '__main__':
    main()
