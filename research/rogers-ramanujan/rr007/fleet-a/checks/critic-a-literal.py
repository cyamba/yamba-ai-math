"""Distinct RR007 Fleet A transcription check; no research-module imports.

Independent literal enumeration, not a universal proof. Only frozen A1--A3
and one-sided source representations are exercised. Every actual mathematical
object constructed by a trial has numerical weight at most its bound.
"""
import argparse
from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path


def f(h):
    return 9 * (h // 5) + (0, 1, 3, 6, 8)[h % 5]


def ft(t, h):
    return f(h + (0, 2, 3)[t]) - 3 * t


def decode(t, value):
    h = 1
    while ft(t, h) < value:
        h += 1
    return h if ft(t, h) == value else None


def literal_u(u, t=0):
    if any(type(x) is not int or x <= 0 for x in u):
        return False
    hs = tuple(decode(t, x) for x in u)
    return (None not in hs and all(0 <= x - y <= 4
            for x, y in zip(hs, hs[1:] + (0,))))


def q(a, b):
    return a * a + 3 * a * b + 3 * b * b


def cw(c):
    a, b, mu, nu = c
    return q(a, b) + sum(mu) + 3 * sum(nu)


def literal_c(c):
    a, b, mu, nu = c
    return (type(a) is type(b) is int and a >= 0 and b >= 0
            and len(mu) == a and len(nu) == b
            and all(type(x) is int and x >= 0 for x in mu + nu)
            and tuple(sorted(mu)) == mu and tuple(sorted(nu)) == nu)


def vectors(length, total, low=0):
    if length == 0:
        if total == 0:
            yield ()
        return
    for x in range(low, total // length + 1):
        for tail in vectors(length - 1, total - x, x):
            yield (x,) + tail


def all_c(bound):
    out = []
    for a in range(bound + 1):
        for b in range(bound + 1):
            base = q(a, b)
            if base > bound:
                continue
            for total_nu in range((bound - base) // 3 + 1):
                for nu in vectors(b, total_nu):
                    for total_mu in range(bound - base - 3 * total_nu + 1):
                        for mu in vectors(a, total_mu):
                            out.append((a, b, mu, nu))
    assert len(out) == len(set(out)) and all(literal_c(c) for c in out)
    return set(out)


def all_u(bound, t=0):
    alphabet = []
    h = 1
    while ft(t, h) <= bound:
        alphabet.append(ft(t, h))
        h += 1
    out = set()

    def visit(prefix, limit, remaining):
        if literal_u(prefix, t):
            out.add(prefix)
        for j in range(limit + 1):
            x = alphabet[j]
            if x <= remaining:
                visit(prefix + (x,), j, remaining - x)
    visit((), len(alphabet) - 1, bound)
    return out


def conjugate(parts):
    return tuple(sum(x >= j for x in parts) for j in range(1, max(parts, default=0) + 1))


def ctag(c):
    a, b, mu, nu = c
    if a == 2 and b == 0:
        k = mu[0]
        return ('A1-3' if k == 0 else 'A1-6' if k % 3 == 1 else
                'A1-8' if k % 3 == 2 else 'A1-9' if k == 3 else 'A1-10')
    if a <= 1:
        return 'A2'
    if a == 3 and b == 0:
        x, y = mu[0], mu[1] - mu[0]
        return ('third-8' if y % 3 == 1 else 'third-10' if y % 3 == 2
                else 'third-6' if x == 0 else 'third-9' if y == 0 else 'third-12')
    if a == 2 and b >= 1 and mu[0] == 0:
        return 'wall'
    return None


def c_to_u(c):
    a, b, mu, nu = c
    tag = ctag(c)
    if tag is None:
        raise ValueError(c)
    if tag.startswith('A1'):
        k, s = mu[0], mu[1] - mu[0]
        if k == 0:
            return (3,) + (1,) * (s + 1)
        if k % 3 == 1:
            return (6,) * ((k + 2) // 3) + (1,) * s
        if k % 3 == 2:
            return (8,) + (6,) * ((k - 2) // 3) + (1,) * s
        if k == 3:
            return (9,) + (1,) * (s + 1)
        return (10,) + (6,) * ((k - 3) // 3) + (1,) * s
    if tag == 'A2':
        lam = tuple(2 * j - 1 + a + x for j, x in enumerate(nu, 1))
        return tuple(3 * x for x in conjugate(lam)) + (1,) * (mu[0] + 1 if a else 0)
    if tag == 'wall':
        lam = (1,) + tuple(2 * j + 1 + x for j, x in enumerate(nu, 1))
        return tuple(3 * x for x in conjugate(lam)) + (1,) * (mu[1] + 1)
    x, y, z = mu[0], mu[1] - mu[0], mu[2] - mu[1]
    m = y // 3
    if tag == 'third-8':
        return (8,) + (6,) * m + (3,) * (x + 1) + (1,) * z
    if tag == 'third-10':
        return (10,) + (6,) * m + (3,) * (x + 1) + (1,) * z
    if tag == 'third-6':
        return (6,) * (m + 1) + (3,) + (1,) * z
    if tag == 'third-9':
        return (9,) + (3,) * x + (1,) * z
    return (12,) + (6,) * m + (3,) * (x - 1) + (1,) * z


def utags(u):
    assert literal_u(u)
    n, support, tags = Counter(u), set(u), []
    if support <= {3, 1} and n[3] == 1 and n[1] >= 1:
        tags.append('A1-3')
    if support <= {6, 1} and n[6] >= 1:
        tags.append('A1-6')
    if support <= {8, 6, 1} and n[8] == 1:
        tags.append('A1-8')
    if support <= {9, 1} and n[9] == 1 and n[1] >= 1:
        tags.append('A1-9')
    if support <= {10, 6, 1} and n[10] == 1 and n[6] >= 1:
        tags.append('A1-10')
    if all(x == 1 or x % 3 == 0 for x in u):
        v = tuple(x // 3 for x in u if x != 1)
        freq, B = Counter(v), max(v, default=0)
        complete = all(freq[k] >= 2 for k in range(1, B))
        a = int(n[1] > 0)
        if not B or complete and freq[B] >= a + 1:
            tags.append('A2')
        if B >= 2 and complete and freq[B] == 1 and n[1] >= 1:
            tags.append('wall')
    for marker, tag in ((8, 'third-8'), (10, 'third-10')):
        if support <= {marker, 6, 3, 1} and n[marker] == 1 and n[3] >= 1:
            tags.append(tag)
    if support <= {6, 3, 1} and n[6] >= 1 and n[3] == 1:
        tags.append('third-6')
    if support <= {9, 3, 1} and n[9] == 1 and n[3] >= 1:
        tags.append('third-9')
    if support <= {12, 6, 3, 1} and n[12] == 1 and n[6] >= 1:
        tags.append('third-12')
    return tags


def u_to_c(u):
    tags = utags(u)
    assert len(tags) == 1, (u, tags)
    tag, n = tags[0], Counter(u)
    if tag.startswith('A1'):
        s = n[1] - int(tag in {'A1-3', 'A1-9'})
        k = {'A1-3': 0, 'A1-6': 3 * n[6] - 2,
             'A1-8': 3 * n[6] + 2, 'A1-9': 3,
             'A1-10': 3 * n[6] + 3}[tag]
        return (2, 0, (k, k + s), ())
    if tag in {'A2', 'wall'}:
        v = tuple(x // 3 for x in u if x != 1)
        lam = tuple(reversed(conjugate(v)))
        if tag == 'wall':
            return (2, max(v) - 1, (0, n[1] - 1),
                    tuple(x - (2 * j + 1) for j, x in enumerate(lam[1:], 1)))
        a = int(n[1] > 0)
        return (a, len(lam), (n[1] - 1,) if a else (),
                tuple(x - (2 * j - 1 + a) for j, x in enumerate(lam, 1)))
    t, m, z = n[3], n[6], n[1]
    x, y = {'third-8': (t - 1, 3 * m + 1), 'third-10': (t - 1, 3 * m + 2),
            'third-6': (0, 3 * (m - 1)), 'third-9': (t, 0),
            'third-12': (t + 1, 3 * m)}[tag]
    return (3, 0, (x, x + y, x + y + z), ())


def hook(t, u):
    hs = tuple(decode(t, x) for x in u)
    H, rest, d = hs[0], hs[1:], (2, 1, 2)[t]
    counts = tuple(rest.count(h) for h in range(1, d + 1))
    inner = tuple(ft((t + 1) % 3, h - d) for h in rest if h > d)
    return H, counts, inner


def unhook(t, H, counts, inner):
    hs = [H] + [decode((t + 1) % 3, x) + (2, 1, 2)[t] for x in inner]
    hs += [h for h, n in enumerate(counts, 1) for _ in range(n)]
    if H <= 0 or H < max(hs):
        return None
    u = tuple(ft(t, h) for h in sorted(hs, reverse=True))
    return u if literal_u(u, t) else None


def check_source(bound):
    phase_counts, reverse_counts = [], []
    for t in range(3):
        objects = all_u(bound, t)
        phase_counts.append(len(objects))
        for u in objects:
            if not u:
                continue
            H, counts, inner = hook(t, u)
            assert sum(inner) <= sum(u) <= bound and literal_u(inner, (t + 1) % 3)
            assert unhook(t, H, counts, inner) == u
            assert sum(u) == sum(inner) + ft(t, H) + 3 * len(inner) + sum(
                n * ft(t, h) for h, n in enumerate(counts, 1))
        admitted = set()
        # Enumerate every admissible reverse hook datum by its nonnegative
        # recurrence costs; never construct an object above the trial bound.
        for inner in all_u(bound, (t + 1) % 3):
            available = bound - sum(inner) - 3 * len(inner)
            H = 1
            while ft(t, H) <= available:
                left = available - ft(t, H)
                d = (2, 1, 2)[t]
                ranges = [range(left // ft(t, h) + 1) for h in range(1, d + 1)]
                for counts in itertools.product(*ranges):
                    if sum(n * ft(t, h) for h, n in enumerate(counts, 1)) > left:
                        continue
                    u = unhook(t, H, counts, inner)
                    if u is not None:
                        assert sum(u) <= bound and hook(t, u) == (H, counts, inner)
                        admitted.add((H, counts, inner))
                H += 1
        assert len(admitted) == len(objects) - 1
        reverse_counts.append(len(admitted))
    # Full literal U -> descent-word -> U and calibrated-sheet -> U.
    for u in all_u(bound):
        hs = tuple(decode(0, x) for x in reversed(u))
        word = tuple(h % 5 for h in hs)
        descents, last, recovered = 0, 0, []
        for r in word:
            descents += r < last
            recovered.append(5 * descents + r)
            last = r
        assert tuple(recovered) == hs and (not word or word[0] != 0)
        energy = sum((0, 1, 3, 6, 8)[r] for r in word)
        energy += 9 * sum(len(word) - j for j, r in enumerate(word) if j and r < word[j - 1])
        assert energy == sum(u)
        rows = [tuple(3 * (h // 5) + min(3, max(0, h % 5 - t + 1))
                      for t in (1, 2, 3)) for h in reversed(hs)]
        assert sum(map(sum, rows)) == sum(u)
        assert all(min(x - y for x, y in zip(row, following)) <= 2
                   for row, following in zip(rows, rows[1:] + [(0, 0, 0)]))
        out = []
        patterns = ((0, 0, 0), (1, 0, 0), (2, 1, 0), (3, 2, 1), (3, 3, 2))
        for row in rows:
            block = row[2] // 3
            residue = patterns.index(tuple(x - 3 * block for x in row))
            out.append(f(5 * block + residue))
        assert tuple(out) == u
    return {'phase_all': phase_counts, 'phase_nonempty_reverse': reverse_counts}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('bound', type=int, choices=(12, 30))
    args = parser.parse_args()
    bound = args.bound
    us, cs = all_u(bound), all_c(bound)
    rows, seen, branches = [], {}, Counter()
    cohorts_u, cohorts_c = Counter(), Counter()
    for c in sorted(cs, key=lambda c: (cw(c), c)):
        tag = ctag(c)
        if tag is None:
            continue
        u = c_to_u(c)
        assert literal_u(u) and u in us and sum(u) == cw(c) <= bound
        assert utags(u) == [tag] and u_to_c(u) == c
        assert u not in seen, (c, seen.get(u), u)
        seen[u] = c
        branches[tag] += 1
        cohorts_u['distinct' if len(set(u)) == len(u) else 'repeated'] += 1
        repeated = any(len(set(v)) < len(v) for v in c[2:])
        cohorts_c['repeated' if repeated else 'distinct'] += 1
        rows.append({'c': c, 'u': u, 'weight': cw(c), 'branch': tag})
    one_hook = 0
    for u in us:
        tags = utags(u)
        assert len(tags) <= 1
        D = max([0] + [j for j, value in enumerate(u, 1) if value > 3 * (j - 1)])
        if D <= 1:
            assert tags, u
            one_hook += 1
        if tags:
            c = u_to_c(u)
            assert c in cs and literal_c(c) and ctag(c) == tags[0]
            assert cw(c) == sum(u) <= bound and c_to_u(c) == u and seen[u] == c
    assert set(seen) == {u for u in us if utags(u)}
    stats = {'status': 'finite_pass_not_universal_proof', 'bound': bound,
             'all_u': len(us), 'all_c': len(cs), 'a1': sum(v for k, v in branches.items() if k.startswith('A1')),
             'a2': branches['A2'], 'a3': len(rows), 'branches': dict(branches),
             'one_hook_with_empty': one_hook, 'u_cohorts': dict(cohorts_u),
             'c_increment_cohorts': dict(cohorts_c), 'source': check_source(bound),
             'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    out = Path(f'.runs/rr007/critic-a-literal-{bound}.json')
    if out.exists():
        raise FileExistsError(out)
    out.write_text(json.dumps(dict(stats, rows=rows), indent=2) + '\n')
    print(json.dumps(stats, sort_keys=True))


if __name__ == '__main__':
    main()
