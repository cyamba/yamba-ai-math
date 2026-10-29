#!/usr/bin/env python3
"""Reproduce finite audit; universal conclusions come from proof.md and review."""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import resource
import sys
import time

CHECKS = Path(__file__).resolve().parents[1]/'checks'
sys.path.insert(0, str(CHECKS))
import separated_pairs as sp
import kr1
import rr003_cluster_merge as merge


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def residue_counts(maximum):
    dp = [1]+[0]*maximum
    for part in range(1, maximum+1):
        if part % 9 in (1, 3, 6, 8):
            for n in range(part, maximum+1):
                dp[n] += dp[n-part]
    return dp


def cluster_counts(maximum):
    """Unrestricted cluster series, using finite reciprocal-product DP."""
    dp = [0]*(maximum+1)
    for a in range(maximum+1):
        for b in range(maximum+1):
            base = sp.quadratic(a, b)
            if base > maximum:
                break
            poly = [1]+[0]*(maximum-base)
            for part in (*range(1, a+1), *range(3, 3*b+1, 3)):
                for n in range(part, len(poly)):
                    poly[n] += poly[n-part]
            for n, coefficient in enumerate(poly):
                dp[base+n] += coefficient
    return dp


def algebraic_checks():
    # These polynomial identities are also proved by expansion in proof.md.
    for c in range(31):
        for r in range(3):
            a = 3*c+r
            for b in range(31):
                require(sp.quadratic(a,b) == r*r+3*r*(b+2*c)+3*sp.quadratic(b,c),
                        'scale3 transcription')
                require(sp.quadratic(a,b+1)-sp.quadratic(a,b) == 3*a+6*b+3,
                        'first difference transcription')
                require(sp.quadratic(a,b+2)-2*sp.quadratic(a,b+1)+sp.quadratic(a,b) == 6,
                        'second difference transcription')


def run(maximum=60, original=None):
    started = time.perf_counter()
    resource.setrlimit(resource.RLIMIT_AS, (2*1024**3, 2*1024**3))
    original_module = None
    if original:
        import importlib.util
        spec = importlib.util.spec_from_file_location('supplied_kr1_harness', original)
        original_module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = original_module
        spec.loader.exec_module(original_module)
    algebraic_checks()
    b_counts, c_counts = residue_counts(maximum), cluster_counts(maximum)
    sector_series = {(a,b): sp.separated_series(a,b,maximum)
                     for a in range(maximum+1) for b in range(maximum+1)
                     if sp.quadratic(a,b) <= maximum}
    reports = []
    first_failure = None
    for n in range(maximum+1):
        seen, safe = {}, set()
        sectors = Counter()
        invalid = collisions = merge_checked = 0
        for c in sp.clusters(n):
            out = sp.literal_compile(c)
            require(sum(out) == n and len(out) == c.dimension, 'weight/dimension')
            if original_module:
                oc = original_module.ClusterState(c.a,c.b,c.mu,tuple(3*x for x in c.m))
                require(out == original_module.lookup_free_kr1_compile(oc),
                        'literal compiler differs from attachment')
            valid = sp.is_gap(out)
            require(valid == c.admitted, 'exact validity theorem transcription')
            if out in seen:
                collisions += 1
            seen[out] = c
            if valid:
                require(sp.extract_separated(out) == c, 'source roundtrip')
                safe.add(out)
                sectors[(c.a,c.b)] += 1
            else:
                invalid += 1
                if first_failure is None:
                    first_failure = {'weight':n, 'a':c.a, 'b':c.b,
                                     'mu':c.mu, 'nu':tuple(3*x for x in c.m), 'output':out}
            # Compatibility comparison only, not a new proof of the broad endpoint.
            rc = kr1.ClusterData(c.a,c.b,tuple(reversed(c.mu)),tuple(reversed(c.m)))
            corrected = merge.cluster_to_gap(rc)
            require(kr1.is_gap(corrected) and sum(corrected) == n, 'existing merge validity')
            require(merge.gap_to_cluster(corrected) == rc, 'existing merge roundtrip')
            if valid:
                require(tuple(reversed(corrected)) == out, 'safe restriction of existing merge')
            merge_checked += 1
        targets = set(sp.gap_partitions(n))
        separated_targets = {p for p in targets if sp.is_separated(p)}
        require(safe == separated_targets, 'independent target coverage')
        for target in separated_targets:
            require(sp.compile_separated(sp.extract_separated(target)) == target,
                    'target roundtrip')
        for sector, coefficients in sector_series.items():
            require(sectors[sector] == coefficients[n], f'separated GF: {sector} at {n}')
        require(len(seen)+collisions == merge_checked == c_counts[n] == b_counts[n]
                == len(targets), 'independent cardinality counts')
        require(collisions == 0, 'raw injectivity transcription')
        reports.append({'n':n, 'cluster_count':merge_checked, 'gap_count':len(targets),
                        'invalid_literal_outputs':invalid, 'raw_collisions':collisions,
                        'separated_count':len(safe), 'nonseparated_target_count':len(targets-safe)})
    hashes = {str(path.relative_to(CHECKS.parents[2])):hashlib.sha256(path.read_bytes()).hexdigest()
              for path in (Path(__file__), CHECKS/'separated_pairs.py',
                           CHECKS/'kr1.py', CHECKS/'rr003_cluster_merge.py')}
    result = {
        'date':'2026-10-27', 'scope':'finite audit of restricted cluster-to-gap endpoint',
        'novelty':'NOT VERIFIED', 'formal_certificate':False,
        'maximum_weight':maximum,
        'first_invalid_literal_output':first_failure,
        'totals': {key:sum(r[key] for r in reports) for key in
                   ('cluster_count','gap_count','invalid_literal_outputs',
                    'raw_collisions','separated_count','nonseparated_target_count')},
        'window_41_60': {key:sum(r[key] for r in reports if 41 <= r['n'] <= 60)
                         for key in ('cluster_count','invalid_literal_outputs','raw_collisions',
                                     'separated_count')},
        'exact_checks': ['literal compiler vs attachment' if original else 'attachment comparison not run',
                         'three independent counts B, C, gap targets',
                         'exact validity iff boundary inequality', 'raw injectivity',
                         'both restricted inverse identities', 'intrinsic image coverage',
                         'positive series per (a,b) sector',
                         'safe restriction equals existing merge; broad merge finite roundtrip'],
        'elapsed_seconds':round(time.perf_counter()-started,6),
        'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'source_sha256':hashes, 'reports':reports,
    }
    if original:
        result['original_harness_sha256'] = hashlib.sha256(Path(original).read_bytes()).hexdigest()
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--maximum', type=int, default=60)
    parser.add_argument('--original', type=Path, help='optional locally extracted supplied harness')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--require-full-compiler', action='store_true',
                        help='exit 2 if the supplied global compiler is refuted')
    args = parser.parse_args()
    if not 0 <= args.maximum <= 60:
        parser.error('this bounded audit supports maximum in 0..60')
    if args.output and args.output.exists():
        parser.error('refusing to overwrite an existing evidence record')
    result = run(args.maximum, args.original)
    if args.output:
        with args.output.open('x') as stream:
            json.dump(result, stream, indent=2)
            stream.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'reports'}, indent=2))
    if args.require_full_compiler and result['first_invalid_literal_output'] is not None:
        raise SystemExit(2)
