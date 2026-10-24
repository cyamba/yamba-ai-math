"""Exhaustive n=6 verification of the independently stated local formulas."""
from collections import Counter
import json
from pathlib import Path
from structural import forward, inverse, destination_shape, tb


def verify():
    all_rows, failures = [], []
    totals = Counter()
    for h in tb.hessenberg_vectors(6):
        seen, counts = {}, Counter()
        for source_tag, shape in [('hook', (5, 1)), ('two', (4, 2))]:
            for source in tb.tableaux(h, shape):
                counts['sources'] += 1
                counts['source_'+source_tag] += 1
                out = forward(h, source_tag, source)
                output_tag, image = out
                counts['destination_'+output_tag] += 1
                if not tb.validates(h, image, destination_shape(6, output_tag)):
                    failures.append({'kind': 'invalid_image', 'h': h, 'source': source, 'out': out})
                if tb.inv_g(h, source) != tb.inv_g(h, image):
                    failures.append({'kind': 'changed_weight', 'h': h, 'source': source, 'out': out})
                if inverse(h, output_tag, image) != (source_tag, source):
                    failures.append({'kind': 'wrong_inverse', 'h': h, 'source': source, 'out': out})
                if out in seen:
                    failures.append({'kind': 'collision', 'h': h, 'source': source,
                                     'prior': seen[out], 'out': out})
                seen[out] = (source_tag, source)
        # Check exact image language on EVERY positive target, not images only.
        for tag in ('row0', 'row1', '411', '321'):
            for image in tb.tableaux(h, destination_shape(6, tag)):
                recovered = inverse(h, tag, image)
                if recovered is not None:
                    counts['recognized_images'] += 1
                    source_tag, source = recovered
                    shape = (5, 1) if source_tag == 'hook' else (4, 2)
                    if not tb.validates(h, source, shape) or forward(h, source_tag, source) != (tag, image):
                        failures.append({'kind': 'false_image_recognition', 'h': h,
                                         'image': image, 'tag': tag, 'recovered': recovered})
                if ((tag, image) in seen) != (recovered is not None):
                    failures.append({'kind': 'image_language_mismatch', 'h': h, 'image': image, 'tag': tag})
        all_rows.append({'h': h, **counts})
        totals.update(counts)
    return {'status': 'finite_exact_passed' if not failures else 'failed',
            'n': 6, 'hessenberg_vectors': len(all_rows), 'totals': totals,
            'failures': failures, 'all_results': all_rows}


if __name__ == '__main__':
    result = verify()
    Path(__file__).with_name('structural-results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'all_results'}, indent=2))
    raise SystemExit(bool(result['failures']))
