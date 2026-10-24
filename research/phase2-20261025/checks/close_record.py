"""Administrative accounting and receipt copy; does not run research code."""
import datetime as dt
import hashlib
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[3]
ATTEMPT = ROOT / 'research' / 'phase2-20261025'
RAW = ROOT / '.runs' / 'phase2-20261025'


def main():
    execution = json.loads((ATTEMPT / 'execution.json').read_text())
    assert execution['status'] == 'closed_with_scoped_results'
    destination = ATTEMPT / 'verification' / 'receipts'
    destination.mkdir(parents=True, exist_ok=True)
    if (destination / 'subprocess.jsonl').exists():
        raise SystemExit('Refusing to replace a closed receipt archive')
    receipts = [p for p in RAW.iterdir() if p.suffix in ('.jsonl', '.stdout', '.stderr')]
    for path in receipts:
        shutil.copyfile(path, destination / path.name)
    rows = [json.loads(line) for line in (RAW / 'subprocess.jsonl').read_text().splitlines()]
    end = dt.datetime.now(dt.timezone.utc)
    start = dt.datetime.fromisoformat(execution['start_utc'])
    seconds = (end - start).total_seconds()
    wall = sum(row['wall_seconds'] for row in rows)
    units = sum(row['cost_units'] for row in execution['dispatches'])
    assert seconds <= 7200 and wall <= 1200
    assert len(execution['dispatches']) == 10 and units == 26
    size = lambda base: sum(p.stat().st_size for p in base.rglob('*')
                            if p.is_file() and '__pycache__' not in p.parts)
    artifact_bytes = size(ATTEMPT) + size(RAW)
    assert artifact_bytes + 1024 * 1024 < 1024 ** 3
    ledger_hash = hashlib.sha256((RAW / 'subprocess.jsonl').read_bytes()).hexdigest()
    result = {
        'status': 'closed_with_scoped_results', 'captured_utc': end.isoformat(),
        'start_utc': execution['start_utc'], 'elapsed_seconds_to_accounting': seconds,
        'elapsed_limit_seconds': 7200, 'elapsed_includes_preparation': True,
        'old_30_minute_preparation_charge_not_reused': True,
        'child_invocations': len(execution['dispatches']), 'invocation_cap': 10,
        'dispatch_proxy_units': units, 'proxy_cap': 30, 'distinct_child_profiles': 5,
        'maximum_observed_concurrent_children': 3,
        'numeric_subprocesses': len(rows), 'subprocess_wall_seconds': wall,
        'subprocess_cpu_seconds': sum(row['cpu_seconds'] for row in rows),
        'subprocess_wall_limit_seconds': 1200,
        'peak_observed_numeric_process_rss_bytes': max(row['peak_rss_bytes'] for row in rows),
        'rss_note': 'Post-exit observation, not a hard transient memory guarantee; excludes model/service memory.',
        'failed_subprocesses': [{k: row[k] for k in ('index', 'label', 'exit_code', 'wall_seconds')}
                                for row in rows if row['exit_code']],
        'incremental_artifact_bytes_at_capture': artifact_bytes,
        'artifact_capture_note': 'Includes canonical copied receipts and ignored fresh raw receipts; excludes copied closed RR007 baseline and caches. Final small accounting/manifest writes follow capture.',
        'incremental_artifact_cap_bytes': 1024 ** 3,
        'model_service_compute_tokens_and_cost': 'unmeasured',
        'paid_providers_or_new_dependencies': False,
        'raw_ledger': '.runs/phase2-20261025/subprocess.jsonl', 'raw_ledger_sha256': ledger_hash,
        'archived_ledger': str((destination / 'subprocess.jsonl').relative_to(ROOT)),
        'existing_engineering_tests_passed': {'harness': 29, 'partition_positivity': 15, 'verification_protocol': 10},
        'full_legacy_suite_run': False,
        'full_suite_qualification': 'Contains explicit KR fixtures above40; no harness behavior was changed.',
        'mathematical_bounds': 'KR<=40, tableau<=6; infinite high-b/high-gap families symbolic only.',
        'pilot_qualification': 'Recursive author correction bound12 additionally constructed the already-exposed fixed C18 witness; critic final pilot is strict12.',
        'formal_checker_run': False, 'new_external_source_or_novelty_certification': False,
    }
    (ATTEMPT / 'resource-use.json').write_text(json.dumps(result, indent=2) + '\n')
    failed = ', '.join(f"{row['label']} (exit {row['exit_code']})" for row in rows if row['exit_code'])
    text = f'''# Closed Phase 2 resource use

Captured {end.isoformat()}. Elapsed preparation and execution to accounting:
{seconds / 60:.2f} of120 authorized minutes. The inherited30-minute charge and
the closed RR006/RR007 time/dispatch ledgers were not reused.

- 10/10 child stages;26/30 dispatch proxy units;five distinct profiles;
  at most three concurrent children. The unused four units do not authorize
  another discovery round. Same-model role separation does not imply
  independent errors. Proxy units are not money or tokens.
- {len(rows)} serialized verification subprocesses; {wall:.6f}s wall of1200s;
  {result['subprocess_cpu_seconds']:.6f}s CPU. All calls have saved commands,
  timeout, exit status, stdout and stderr in `verification/receipts/`.
- Peak observed numerical-process RSS was
  {result['peak_observed_numeric_process_rss_bytes']:,} bytes
  ({result['peak_observed_numeric_process_rss_bytes'] / 1024 ** 2:.2f}MiB).
  This post-exit measurement is not a hard transient guarantee and excludes
  model/service memory. Target was512MiB per numerical child.
- Fresh artifacts at capture were {artifact_bytes:,} bytes, including both
  canonical and ignored copies of fresh receipts, below1GiB. The copied closed
  RR007 raw baseline and caches are excluded; small final manifest/accounting
  writes follow this measurement.

Failed charged subprocesses: {failed}. The geometry failure exposed the
false quotient terminal<=1 claim. The first closure repository check ran
before the resource file existed and flagged its missing local link. Its
corrected rerun is retained; no failed command was discarded. Candidate
collisions, bad formulas and historical pin qualifications are additional
research findings, not necessarily nonzero process exits.

The29 harness,15 partition and10 verification-protocol tests passed. Final
repository and current acceptance-pin checks passed as recorded at closure.
The full legacy suite was not run because it constructs KR fixtures above40;
no harness behavior changed. Initial census gates were12,30,40 and tableau
through5 then6. The recursive author's correction call labeled12 additionally
replayed its fixed C18 witness after40 was exposed; the critic's final pilot
is strict12. No object exceeded the overall40/six bounds. High-b/high-gap
claims received symbolic review without above40 instances.

Model/service compute, tokens and monetary cost are unmeasured. There was no
new paid provider, dependency, web retrieval, publication, push or external
message. No formal proof checker ran; novelty remains unverified.

See `resource-use.json` for exact values and the archived/raw ledger SHA-256.
Old closed ledgers and immutable input pins are checked separately. This is
the final accounting for this attempt; do not append new runs to it.
'''
    (ATTEMPT / 'resource-use.md').write_text(text)
    print(json.dumps({k: result[k] for k in ('elapsed_seconds_to_accounting', 'child_invocations', 'dispatch_proxy_units', 'numeric_subprocesses', 'subprocess_wall_seconds', 'peak_observed_numeric_process_rss_bytes')}))


if __name__ == '__main__':
    main()
