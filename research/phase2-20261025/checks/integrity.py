"""Verify saved SHA-256 maps without importing or executing research code."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ATTEMPT = ROOT / 'research' / 'phase2-20261025'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--manifest', action='append',
                        help='Explicit current acceptance manifest; may be repeated')
    args = parser.parse_args()
    manifests = [ATTEMPT / 'baseline-pins.json',
                 ATTEMPT / 'supplemental-input-pins.json']
    manifests += sorted(ATTEMPT.rglob('*freeze*.json'))
    manifests += sorted((ATTEMPT / 'reviews').glob('*pins.json'))
    if args.manifest:
        manifests = [ROOT / name for name in args.manifest]
    records, failures = [], []
    for manifest in dict.fromkeys(manifests):
        data = json.loads(manifest.read_text())
        checked = 0
        for field in ('files', 'sha256', 'upstream_dependency_sha256'):
            entries = data.get(field, {})
            if not isinstance(entries, dict):
                continue
            for name, expected in entries.items():
                if not isinstance(expected, str) or len(expected) != 64:
                    continue
                path = Path(name)
                if not path.is_absolute():
                    base = ROOT if path.parts[0] in ('research', '.runs') else manifest.parent
                    path = base / path
                actual = hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None
                checked += 1
                if actual != expected:
                    failures.append({'manifest': str(manifest.relative_to(ROOT)),
                                     'field': field, 'path': str(path),
                                     'expected': expected, 'actual': actual})
        records.append({'manifest': str(manifest.relative_to(ROOT)),
                        'sha256': hashlib.sha256(manifest.read_bytes()).hexdigest(),
                        'checked_entries': checked})
    result = {'kind': 'file_integrity_only_not_mathematical_verification',
              'status': 'pass' if not failures else 'fail',
              'checked_entries': sum(r['checked_entries'] for r in records),
              'manifests': records, 'failures': failures}
    output = ROOT / args.output
    if output.exists():
        raise SystemExit('Refusing to overwrite an integrity receipt')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'checked_entries': result['checked_entries'],
                      'failures': failures, 'output': str(output)}))
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
