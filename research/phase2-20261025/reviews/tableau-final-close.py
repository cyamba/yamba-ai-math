"""Pin the final critic record without rewriting earlier review artifacts."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PACKET = HERE.parent/'tableau'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    dependency = json.loads((HERE/'tableau-final-dependencies.json').read_text())
    assert all(sha(ROOT/name) == pin for name,pin in dependency.items())
    initial = json.loads((HERE/'tableau-review-final-pins.json').read_text())
    assert all(sha(ROOT/name) == pin for name,pin in initial['sha256'].items())
    author = json.loads((PACKET/'freeze.json').read_text())
    assert all(sha(PACKET/name) == pin for name,pin in author['sha256'].items())
    result = json.loads((HERE/'tableau-final-result.json').read_text())
    assert result['status'] == 'finite_exact_passed' and not result['failure_count']
    assert result['totals']['negative'] == result['totals']['mapped'] == 3980
    assert result['totals']['positive'] == 6800
    assert result['historical_original_bytes_recovered']
    assert result['historical_failure_receipt_preserved']
    dependency.update({str(p.relative_to(ROOT)):sha(p) for p in [
        HERE/'tableau-final-review.md',HERE/'tableau-final-result.json',
        HERE/'tableau-final-dependencies.json',Path(__file__),
        HERE/'tableau-review-final-pins.json']})
    output = {'status':'closed_distinct_final_review',
              'verdict':'supported within declared finite n=6 e51 scope',
              'assurance':{'partial_injection':'proved by ordinary induction; distinct semantic review',
                           'finite_totality':'independent exhaustive verification on all132 natural unit interval orders at n6',
                           'formal_certification':'not run','novelty':'unverified',
                           'symbolic_larger_class_totality':'not established'},
              'historical_preliminary_pin_qualification_preserved':True,
              'sha256':dependency}
    (HERE/'tableau-final-pins.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k != 'sha256'},indent=2))


if __name__ == '__main__':
    main()
