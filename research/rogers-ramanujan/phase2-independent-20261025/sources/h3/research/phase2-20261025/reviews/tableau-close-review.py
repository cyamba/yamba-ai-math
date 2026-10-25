"""Close the distinct review by rechecking frozen dependencies and evidence."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PACKET = HERE.parent/'tableau'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    freeze = json.loads((PACKET/'freeze.json').read_text())
    assert len(freeze['sha256']) == 17
    assert all(sha(PACKET/name) == pin for name,pin in freeze['sha256'].items())
    independent = json.loads((HERE/'tableau-result.json').read_text())
    assert independent['failure_count'] == 0
    assert independent['structural_n6']['sources'] == 151
    assert independent['structural_n6']['all_negative'] == 3980
    assert independent['vector_total'] == 197
    assert json.loads((HERE/'tableau-matching-reproduction.json').read_text()) == json.loads((PACKET/'candidates-through6.json').read_text())
    hall = json.loads((HERE/'tableau-hall-result.json').read_text())
    assert hall['Hall_counts'] == {'negative_vertices':2,'positive_neighbors':1}
    deps = json.loads((HERE/'tableau-dependencies.json').read_text())
    assert all(sha(ROOT/name) == pin for name,pin in deps.items())
    extra = [PACKET/'freeze.json',
             ROOT/'research/phase2-20261025/inputs/external-scratch/test_clean_6sector.py']
    deps.update({str(p.relative_to(ROOT)):sha(p) for p in HERE.glob('tableau-*')
                 if p.is_file() and p.name != 'tableau-review-final-pins.json'})
    deps.update({str(p.relative_to(ROOT)):sha(p) for p in extra})
    result = {'status':'closed_distinct_ordinary_semantic_review',
              'author_frozen_dependencies':17,
              'verdict':'incomplete overall; supported Theorem A and stated conditional Theorem B',
              'claims':{'TheoremA':'proved; distinct ordinary semantic review; not formally certified',
                        'TheoremB':'proved on stated conditional domain; distinct ordinary semantic review; not formally certified',
                        'full_structural_n6_cancellation':'incomplete; 3829 negative sources remain',
                        'finite_matching_and_oracle_agreement':'empirical finite exact evidence'},
              'sha256':deps}
    (HERE/'tableau-review-final-pins.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'sha256'},indent=2))


if __name__ == '__main__':
    main()
