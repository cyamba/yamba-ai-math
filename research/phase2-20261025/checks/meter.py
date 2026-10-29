"""Attempt-only serialized subprocess meter; standard library, no shell."""
import argparse
import datetime as dt
import fcntl
import json
import os
from pathlib import Path
import resource
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
RAW = ROOT / '.runs' / 'phase2-20261025'
LIMIT = 1200.0
DEADLINE = dt.datetime(2026, 10, 25, 0, 11, 44, tzinfo=dt.timezone.utc)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--label', required=True)
    parser.add_argument('--timeout', type=float, default=120)
    parser.add_argument('command', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    command = args.command[1:] if args.command[:1] == ['--'] else args.command
    if not command or not 0 < args.timeout <= 180:
        parser.error('command required; timeout must be in (0,180]')
    RAW.mkdir(parents=True, exist_ok=True)
    ledger = RAW / 'subprocess.jsonl'
    with (RAW / 'meter.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        prior = [json.loads(x) for x in ledger.read_text().splitlines()] if ledger.exists() else []
        charged = sum(x['wall_seconds'] for x in prior)
        now = dt.datetime.now(dt.timezone.utc)
        allowance = min(args.timeout, LIMIT - charged, (DEADLINE - now).total_seconds())
        if allowance <= 0:
            raise SystemExit('Fresh subprocess or elapsed budget exhausted')
        index = len(prior) + 1
        stem = RAW / f'{index:03d}-{args.label}'
        start = time.monotonic()
        before = resource.getrusage(resource.RUSAGE_CHILDREN)
        failure = None
        with stem.with_suffix('.stdout').open('w') as output, stem.with_suffix('.stderr').open('w') as errors:
            try:
                result = subprocess.run(command, cwd=ROOT, stdout=output, stderr=errors,
                                        timeout=allowance, check=False)
                code = result.returncode
            except subprocess.TimeoutExpired:
                code, failure = 124, 'timeout'
            except OSError as exc:
                code, failure = 127, repr(exc)
        after = resource.getrusage(resource.RUSAGE_CHILDREN)
        elapsed = time.monotonic() - start
        row = {'index': index, 'label': args.label, 'started_utc': now.isoformat(),
               'command': command, 'cwd': str(ROOT), 'timeout_seconds': allowance,
               'wall_seconds': elapsed, 'cpu_seconds': after.ru_utime + after.ru_stime - before.ru_utime - before.ru_stime,
               'peak_rss_bytes': after.ru_maxrss if sys.platform == 'darwin' else after.ru_maxrss * 1024,
               'exit_code': code, 'failure': failure, 'stdout': str(stem.with_suffix('.stdout')),
               'stderr': str(stem.with_suffix('.stderr')),
               'cumulative_wall_seconds': charged + elapsed}
        with ledger.open('a') as handle:
            handle.write(json.dumps(row) + '\n')
        print(json.dumps(row))
        print(stem.with_suffix('.stdout').read_text()[-14000:])
        if code:
            print(stem.with_suffix('.stderr').read_text()[-10000:], file=sys.stderr)
        return code


if __name__ == '__main__':
    raise SystemExit(main())
