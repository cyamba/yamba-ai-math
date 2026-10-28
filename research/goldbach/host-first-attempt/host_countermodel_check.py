"""Finite toy checks for the density-one prime-subset countermodel.

Each row uses an independently constructed finite deletion set, not the
single infinite nested A defined in host_prover.md.
"""
from math import isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def factors(n):
    result = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            result.append(d)
            n //= d
        d += 1
    if n > 1:
        result.append(n)
    return result


def cube_root(n):
    z = 0
    while (z + 1) ** 3 <= n:
        z += 1
    return z


def check(r):
    assert prime(r) and r >= 3
    n = 2 * r * r
    z = cube_root(n)
    removed = {max(p, n-p) for p in range(2, n-1)
               if prime(p) and prime(n-p)}
    counts = {"PP": 0, "PS": 0, "SP": 0, "SS": 0}
    for a in range(z+1, n-z):
        b = n-a
        fa, fb = factors(a), factors(b)
        assert fa and fb
        if min(fa + fb) <= z or any(p in removed for p in fa + fb):
            continue
        assert 1 <= len(fa) <= 2 and 1 <= len(fb) <= 2
        name = ("P" if len(fa) == 1 else "S") + ("P" if len(fb) == 1 else "S")
        counts[name] += 1
    assert r not in removed and counts["PP"] == 0 and counts["SS"] >= 1
    assert counts["PS"] == counts["SP"]
    return n, z, removed, counts


if __name__ == "__main__":
    for r in [3, 5, 7, 11, 13]:
        n, z, removed, counts = check(r)
        print(f"r={r} N={n} z={z} deletions={len(removed)} "
              f"PP={counts['PP']} PS={counts['PS']} SP={counts['SP']} "
              f"SS={counts['SS']} T={counts['SS']-counts['PP']}")
