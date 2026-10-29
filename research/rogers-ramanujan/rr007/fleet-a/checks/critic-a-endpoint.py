"""Bounded, independent literal audit of the old RR003 gap--C endpoint.

Only the critic's own guarded literal definitions are imported. The old
endpoint and its transitive research dependencies are read, never imported.
This script is not a U--C candidate or an endpoint source-equivalence claim.
"""
import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    'critic_literal', Path(__file__).with_name('critic-a-literal.py'))
lit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lit)


def gap(parts):
    return (all(type(x) is int and x > 0 for x in parts)
            and tuple(sorted(parts)) == parts
            and all(parts[i + 2] - parts[i] >= 3 for i in range(len(parts) - 2))
            and all(y - x > 1 or (x + y) % 3 == 0 for x, y in zip(parts, parts[1:])))


def all_gap(bound):
    out = set()
    def visit(parts, low, left):
        if gap(parts):
            out.add(parts)
        for x in range(low, left + 1):
            visit(parts + (x,), x, left - x)
    visit((), 1, bound)
    return out


def pair(level):
    r, parity = divmod(level, 2)
    return (3 * r + 1, 3 * r + 2) if parity == 0 else (3 * r + 3, 3 * r + 3)


def L(level):
    r, parity = divmod(level, 2)
    return 3 * r - 1 + parity


def merge(c):
    a, b, mu, nu = c
    i = j = 0
    out = []
    while i + j < a + b:
        if i == a:
            take_single = False
        elif j == b:
            take_single = True
        else:
            single = mu[i] + 3 * j + 2 * i + 1
            level = nu[j] + 2 * j + i
            take_single = single <= L(level + 1)
        if take_single:
            out.append(mu[i] + 3 * j + 2 * i + 1)
            i += 1
        else:
            out.extend(pair(nu[j] + 2 * j + i))
            j += 1
    return tuple(out)


def extract(parts):
    assert gap(parts)
    mu, nu, at = [], [], 0
    while at < len(parts):
        x = parts[at]
        if at + 1 < len(parts) and parts[at + 1] - x <= 1:
            level = (x + parts[at + 1]) // 3 - 1
            assert pair(level) == parts[at:at + 2]
            nu.append(level - 2 * len(nu) - len(mu))
            at += 2
        else:
            mu.append(x - 3 * len(nu) - 2 * len(mu) - 1)
            at += 1
    return len(mu), len(nu), tuple(mu), tuple(nu)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('bound', choices=(12, 30), type=int)
    bound = parser.parse_args().bound
    gaps, cs = all_gap(bound), lit.all_c(bound)
    seen, rows, gap_cohort, c_cohort = {}, [], Counter(), Counter()
    for c in sorted(cs, key=lambda c: (lit.cw(c), c)):
        parts = merge(c)
        assert parts in gaps and gap(parts) and sum(parts) == lit.cw(c) <= bound
        assert extract(parts) == c and parts not in seen
        seen[parts] = c
        gap_cohort['distinct' if len(set(parts)) == len(parts) else 'repeated'] += 1
        repeated = any(len(set(v)) < len(v) for v in c[2:])
        c_cohort['repeated' if repeated else 'distinct'] += 1
        rows.append({'c': c, 'gap': parts, 'weight': sum(parts)})
    for parts in gaps:
        c = extract(parts)
        assert lit.literal_c(c) and c in cs and lit.cw(c) == sum(parts) <= bound
        assert merge(c) == parts
    assert set(seen) == gaps
    stats = {'status': 'finite_endpoint_pass_not_source_equivalence_or_full_KR1',
             'bound': bound, 'gap_count': len(gaps), 'c_count': len(cs),
             'gap_cohorts': dict(gap_cohort), 'c_increment_cohorts': dict(c_cohort),
             'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'literal_dependency_sha256': hashlib.sha256(Path(lit.__file__).read_bytes()).hexdigest()}
    out = Path(f'.runs/rr007/critic-a-endpoint-{bound}.json')
    if out.exists():
        raise FileExistsError(out)
    out.write_text(json.dumps(dict(stats, rows=rows), indent=2) + '\n')
    print(json.dumps(stats, sort_keys=True))


if __name__ == '__main__':
    main()
