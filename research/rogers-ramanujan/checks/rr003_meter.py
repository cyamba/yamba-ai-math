"""RR003-only computation ledger; serializes and accounts discovery/verification.

Not a provider adapter or a general harness change. Run from repository root:
python3 research/rogers-ramanujan/checks/rr003_meter.py LABEL -- python3 SCRIPT
"""
import argparse
from datetime import datetime, timezone
import fcntl
import hashlib
import json
from pathlib import Path
import resource
import shutil
import signal
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
RUNS = ROOT / '.runs/rr003'
LEDGER = RUNS / 'enumeration-ledger.json'
LIMIT_BYTES = 1024 ** 3


def stored_bytes():
    paths = (RUNS, ROOT / 'research/rogers-ramanujan/rr003')
    return sum(p.stat().st_size for folder in paths for p in folder.rglob('*') if p.is_file())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('label')
    parser.add_argument('command', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if not args.label or any(c not in 'abcdefghijklmnopqrstuvwxyz0123456789-_' for c in args.label):
        parser.error('label must contain lowercase letters, digits, hyphen or underscore')
    command = args.command[1:] if args.command[:1] == ['--'] else args.command
    if not command:
        parser.error('command required')
    RUNS.mkdir(parents=True, exist_ok=True)
    with (RUNS / 'enumeration.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        ledger = json.loads(LEDGER.read_text())
        output = RUNS / (args.label + '.json')
        if output.exists():
            parser.error('refusing to overwrite an execution receipt')
        now = datetime.now(timezone.utc)
        deadline = datetime.fromisoformat(ledger['deadline_utc'].replace('Z', '+00:00'))
        remaining = min(ledger['limit_seconds'] - ledger['used_seconds'], (deadline - now).total_seconds())
        if remaining <= 0:
            parser.error('RR003 time budget exhausted')
        if shutil.disk_usage(ROOT).free < 5 * 1024 ** 3 or stored_bytes() >= LIMIT_BYTES:
            parser.error('RR003 storage safeguard')
        sources = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                   for folder in (ROOT / 'research/rogers-ramanujan/checks', ROOT / 'research/rogers-ramanujan/rr003')
                   for p in folder.rglob('*') if p.suffix in ('.py', '.md', '.json')}
        record = {'program': 'RR003', 'label': args.label, 'command': command,
                  'started_utc': now.isoformat(), 'source_sha256': sources,
                  'limit_seconds_remaining_before': remaining,
                  'memory_enforcement': 'peak child RSS checked after execution; not an OS memory reservation'}
        start = time.monotonic()
        process = subprocess.Popen(command, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   start_new_session=True, text=True)
        try:
            stdout, stderr = process.communicate(timeout=remaining)
            record.update(exit_code=process.returncode, stdout=stdout, stderr=stderr)
        except subprocess.TimeoutExpired:
            import os
            os.killpg(process.pid, signal.SIGKILL)
            stdout, stderr = process.communicate()
            record.update(exit_code=124, status='capped', stdout=stdout, stderr=stderr)
        elapsed = time.monotonic() - start
        rss = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
        rss = rss if sys.platform == 'darwin' else rss * 1024
        record.update(elapsed_seconds=elapsed, peak_child_rss_bytes=rss)
        if rss > 2 * 1024 ** 3:
            record.update(status='capped', cap_reason='child peak RSS exceeded 2 GiB', exit_code=125)
        payload = json.dumps(record, indent=2) + '\n'
        if stored_bytes() + len(payload.encode()) > LIMIT_BYTES:
            record.update(status='capped', cap_reason='aggregate RR003 artifact bytes', exit_code=125,
                          stdout='output omitted by artifact cap', stderr='output omitted by artifact cap')
            payload = json.dumps(record, indent=2) + '\n'
        output.write_text(payload)
        ledger['used_seconds'] += elapsed
        ledger['runs'].append({k: record[k] for k in ('label', 'elapsed_seconds', 'peak_child_rss_bytes', 'exit_code')})
        LEDGER.write_text(json.dumps(ledger, indent=2) + '\n')
        print(json.dumps({'receipt': str(output.relative_to(ROOT)), 'exit_code': record['exit_code'],
                          'elapsed_seconds': elapsed, 'cumulative_seconds': ledger['used_seconds'],
                          'peak_child_rss_bytes': rss}))
        if stdout:
            print(stdout)
        if stderr:
            print(stderr, file=sys.stderr)
        return record['exit_code']


if __name__ == '__main__':
    raise SystemExit(main())
