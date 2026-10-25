"""Source-bound finite verification of RR003's restricted column theorem.

Successful execution certifies finite checks only, never a full bijection.
"""
import argparse
from collections import Counter
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import time
import kr1
import rr003_columns as maps
ROOT = Path(__file__).resolve().parents[3]

def require(condition, message='RR003 finite check failed'):
    if not condition:
        raise AssertionError(message)
PHASE = ROOT / 'research/rogers-ramanujan/rr003'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def verify(ceiling):
    freeze = json.loads((PHASE / 'round-1-freeze.json').read_text())
    require(sha(PHASE / 'round-1-proposal.md') == freeze['proposal_sha256'], 'frozen proposal changed')
    paths = [Path(__file__), Path(maps.__file__), Path(kr1.__file__), PHASE / 'round-1-proposal.md', PHASE / 'round-1-freeze.json']
    sources = {str(p.relative_to(ROOT)): sha(p) for p in paths}
    report = {'program': 'RR003', 'round': 1, 'ceiling': ceiling, 'claim_status': 'empirical finite verification; written theorem separate', 'full_bijection': 'unresolved', 'source_sha256': sources, 'started_utc': datetime.now(timezone.utc).isoformat(), 'cases': []}
    totals = Counter()
    first_uncovered_u = first_unsupported_c = None
    for n in range(ceiling + 1):
        actual_u = {kr1.weighted_columns(w) for w in kr1.weighted_partitions(n)}
        images = set()
        supported_clusters = recognized = 0
        for c in kr1.cluster_data(n):
            if not maps.supported(c):
                if first_unsupported_c is None:
                    first_unsupported_c = {'weight': n, 'cluster': asdict(c)}
                continue
            supported_clusters += 1
            u = maps.reconstruct_columns(c)
            require(u in actual_u and sum(u) == c.weight == n, 'RR003 finite check failed')
            require(u not in images, ('collision', c, u))
            images.add(u)
            require(maps.decompose_columns(u) == c, 'RR003 finite check failed')
            for j in range(1, c.b + 1):
                raised = maps.reconstruct_columns(maps.raise_nu_suffix(c, j))
                require(raised == tuple(sorted(u + (3 * j,), reverse=True)), 'RR003 finite check failed')
                require(sum(raised) == n + 3 * j, 'RR003 finite check failed')
                totals['nu_operation_checks'] += 1
            if c.mu:
                raised = maps.reconstruct_columns(maps.raise_last_mu(c))
                require(raised == tuple(sorted(u + (1,), reverse=True)), 'RR003 finite check failed')
                totals['unit_operation_checks'] += 1
            if c.a == 2 and c.mu[0] == 0:
                raised = maps.reconstruct_columns(maps.merge_raise(c))
                changed = list(u)
                changed.remove(3 * (c.b + 1))
                changed.remove(1)
                changed.append(3 * (c.b + 2))
                require(raised == tuple(sorted(changed, reverse=True)) and sum(raised) == n + 2, 'RR003 finite check failed')
                require(maps.decompose_columns(raised) == maps.merge_raise(c), 'RR003 finite check failed')
                totals['merge_operation_checks'] += 1
        recognized_set = set()
        for u in sorted(actual_u):
            try:
                c = maps.decompose_columns(u)
            except maps.OutsideRestrictedDomain:
                if first_uncovered_u is None:
                    first_uncovered_u = {'weight': n, 'columns': u}
                continue
            recognized += 1
            require(c.weight == n and maps.supported(c), 'RR003 finite check failed')
            require(maps.reconstruct_columns(c) == u, 'RR003 finite check failed')
            recognized_set.add(u)
        require(images == recognized_set and len(images) == supported_clusters, 'RR003 finite check failed')
        report['cases'].append({'weight': n, 'actual_U': len(actual_u), 'supported_C': supported_clusters, 'recognized_U': recognized, 'uncovered_U': len(actual_u) - recognized})
        totals['cluster_round_trips'] += supported_clusters
        totals['column_round_trips'] += recognized
    report.update(status='restricted_finite_checks_passed_full_bridge_unresolved', totals=dict(totals), first_uncovered_U=first_uncovered_u, first_unsupported_C=first_unsupported_c)
    require(sources == {str(p.relative_to(ROOT)): sha(p) for p in paths}, 'sources changed during execution')
    return report

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ceiling', type=int, default=12)
    parser.add_argument('--require-bijection', action='store_true')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if not 0 <= args.ceiling <= 30:
        parser.error('ceiling must lie between zero and thirty')
    if args.output.exists():
        parser.error('refusing to overwrite evidence')
    start = time.monotonic()
    try:
        report = verify(args.ceiling)
        code = 2 if args.require_bijection else 0
        if code:
            report['required_completion_failure'] = 'Full residue-to-gap maps and universal proof absent; restricted theorem is progress only'
    except (AssertionError, ValueError, OSError) as exc:
        report = {'program': 'RR003', 'status': 'failed', 'error': str(exc)}
        code = 1
    report['elapsed_seconds'] = time.monotonic() - start
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ('status', 'elapsed_seconds')}))
    return code
if __name__ == '__main__':
    raise SystemExit(main())
