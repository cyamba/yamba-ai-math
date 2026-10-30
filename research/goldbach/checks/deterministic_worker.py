#!/usr/bin/env python3
"""A real, finite, deterministic Yamba worker; it is not an LLM proof agent.

Consumes a Yamba dispatch packet and emits the adapter's JSON result. Research
scope is deliberately narrow and responses never claim an unbounded theorem.
"""
from __future__ import annotations
import json
import math
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MAX_N = 2000


def floor_cuberoot(n):
    z = int(n ** (1 / 3))
    while (z + 1) ** 3 <= n:
        z += 1
    while z ** 3 > n:
        z -= 1
    return z


def factors_trial(n):
    out = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            out.append(d)
            n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def smallest_factors(limit):
    spf = list(range(limit + 1))
    for d in range(2, math.isqrt(limit) + 1):
        if spf[d] == d:
            for x in range(d * d, limit + 1, d):
                if spf[x] == x:
                    spf[x] = d
    return spf


def factors_sieve(n, spf):
    out = []
    while n > 1:
        out.append(spf[n])
        n //= spf[n]
    return out


def pair_classes(n, z, factor):
    counts = [0, 0, 0, 0]
    signed = 0
    for a in range(z + 1, n - z):
        b = n - a
        fa, fb = factor(a), factor(b)
        if not fa or not fb or fa[0] <= z or fb[0] <= z:
            continue
        if len(fa) > 2 or len(fb) > 2:
            raise AssertionError((n, a, b, z, fa, fb))
        counts[2 * (len(fa) - 1) + len(fb) - 1] += 1
        signed += (-1) ** len(fa)
    return counts, signed


def half_pair_counts(n, z):
    pp = ss = other = 0
    for a in range(z + 1, n // 2 + 1):
        b = n - a
        fa, fb = factors_trial(a), factors_trial(b)
        if not fa or not fb or fa[0] <= z or fb[0] <= z:
            continue
        if len(fa) == len(fb) == 1:
            pp += 1
        elif len(fa) == len(fb) == 2:
            ss += 1
        else:
            other += 1
    return pp, ss, other


def counterexamples():
    ties, negatives = [], []
    for n in range(6, 502, 2):
        z = math.isqrt(math.isqrt(n))
        pp, ss, _ = half_pair_counts(n, z)
        if pp == ss:
            ties.append(n)
        if pp < ss:
            negatives.append(n)
    if 8 not in ties or 12 not in ties:
        raise AssertionError(('quarter-root ties', ties))
    return {'quarter_root_even_range': [6, 500], 'ties': ties,
            'negative_margins': negatives,
            'convention': 'unordered half-interval, trial division',
            'falsifies': 'PP > SS for every even N >= 6'}


def finite_checks():
    spf = smallest_factors(MAX_N + 2)
    max_margin = 0
    cases = 0
    for n in range(6, MAX_N + 1, 2):
        z = floor_cuberoot(n)
        cells, t = pair_classes(n, z, lambda x: factors_sieve(x, spf))
        if cells[1] != cells[2] or t != cells[3] - cells[0]:
            raise AssertionError(('reflection', n, cells, t))
        max_margin = max(max_margin, abs(t))
        cases += 1
    # Independently calculate common prime summands by the sieve.
    checked = 0
    for n in range(38, MAX_N + 1, 30):
        assert n % 30 == 8
        shared = [p for p in range(2, n - 1) if spf[p] == p and
                  spf[n - p] == n - p and spf[n + 2 - p] == n + 2 - p]
        if shared:
            raise AssertionError(('adjacent-target progression', n, shared))
        checked += 1
    return {'cube_even_range': [6, MAX_N], 'cube_targets': cases,
            'exact_reflection_identity_failures': 0,
            'max_absolute_signed_value': max_margin,
            'adjacent_progression_targets': checked,
            'adjacent_progression_failures': 0,
            'method': 'integer smallest-factor sieve and exact counting'}


def response(stage, packet):
    claims = []
    if stage == 'survey':
        summary = ('Read the local research brief and its list of primary references. '
                   'No new literature fetch or independent source inspection occurred in this deterministic stage.')
        claims = [{'text': 'The brief records source candidates that require exact theorem and hypothesis verification.',
                   'status': 'unverified', 'source': 'research/goldbach/orchestrated-prompt.md'}]
    elif stage == 'statement':
        summary = ('Precisely identified the signed-rough research target T(N)<0. '
                   'This stage is scripted and does not provide a formal proof or mathematical review.')
        claims = [{'text': 'A proposed pointwise inequality T(N)<0 for all sufficiently large even N remains open.',
                   'status': 'conjecture', 'source': 'research/goldbach/orchestrated-prompt.md'}]
    elif stage == 'counterexample':
        result = counterexamples()
        summary = 'Executed the trial-division quarter-root counterexample scan. ' + json.dumps(result, sort_keys=True)
        claims = [{'text': 'The universal strict claim PP > SS for all even N >= 6 fails at N=8 and N=12 under the half-interval convention.',
                   'status': 'refuted', 'source': 'research/goldbach/checks/deterministic_worker.py'}]
    elif stage == 'finite-check':
        result = finite_checks()
        summary = 'Executed integer-sieve exact finite checks. ' + json.dumps(result, sort_keys=True)
        claims = [{'text': 'For the stated finite range, direct counting checked T=SS-PP and the adjacent-summand progression.',
                   'status': 'empirical', 'source': 'research/goldbach/checks/deterministic_worker.py'}]
    elif stage == 'revise':
        upstream = packet.get('upstream', {})
        summary = ('The candidate remains unproved and requires a model-backed author and independent human review. '
                   'This deterministic stage records the two upstream results; it does not perform a conceptual proof revision. '
                   'Upstream keys: ' + ', '.join(sorted(item['step_id'] for item in upstream)))
        claims = [{'text': 'Finite observations do not imply the pointwise inequality for all sufficiently large N.',
                   'status': 'established', 'source': 'research/goldbach/orchestrated-prompt.md'}]
    elif stage == 'integrate':
        upstream = packet.get('upstream', {})
        summary = ('Deterministic finite checks completed; no language-model proof search, independent semantic critic, '
                   'or proof of Goldbach has been performed by this adapter. Upstream keys: ' + ', '.join(sorted(item['step_id'] for item in upstream)))
        claims = [{'text': 'The principal pointwise inequality remains unresolved by this run.',
                   'status': 'unverified', 'source': 'research/goldbach/orchestrated-prompt.md'}]
    else:
        raise ValueError('Unsupported stage ' + stage)
    return {'summary': summary, 'claims': claims,
            'artifacts': ['research/goldbach/orchestrated-prompt.md',
                          'research/goldbach/checks/deterministic_worker.py']}


def main():
    packet = json.load(sys.stdin)
    if packet.get('protocol_version') != '1':
        raise ValueError('Unsupported protocol version')
    stage = packet['step']['stage_id']
    start = time.monotonic()
    out = response(stage, packet)
    out['summary'] += ' Worker type: deterministic Python, not an LLM; measured seconds: %.3f.' % (time.monotonic() - start)
    print(json.dumps(out, ensure_ascii=False))


if __name__ == '__main__':
    main()
