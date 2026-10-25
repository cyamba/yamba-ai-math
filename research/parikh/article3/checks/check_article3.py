#!/usr/bin/env python3
"""Checks for Article 3 (paper3/article3.tex, version 2): completeness of Parikh matrices when
letters occur at most twice or three times. Sections 6 and 7 are checked by check_c3.py.

Copyright (c) 2026 Christopher Yamba. All rights reserved.

Standard library only. Exits non-zero on the first failure.

  [1] Lemma 3.1 (rectangle rule) and Theorem 4.2 (cases (i)-(iii)) on every word of every
      content with 3 <= k <= 5, n_i <= 3 and at most 9 letters.
  [2] Example 4.5: 21332 / 32123, and the three-letter criterion for a, b, c <= 4.
  [3] Lemma 5.1 (ballot numbers) and Theorem B for n <= 30, the Catalan value, and the
      printed words A_n, B_n for n = 2, 3, 4.
  [4] Corollary 4.6: the Parikh classes of (2^k) are the fibres of the third and fourth
      diagonals, with the printed numbers, for 3 <= k <= 8 (k <= 7 by default).
  [5] Table 2, small entries: contents with n_i <= 2, sum <= 11 and k <= 8; the (a,3,3,c) rule
      of Section 7 (a, c <= 3; <= 6 with --full); and
      five-letter windows with n = 3, 4 and small ends; --full adds every content of the
      first two n = 3 rows and the n = 4 five-letter rows. The six-letter rows are computed
      by notes/completeness-scripts/c/corner.c (ancillary corner.c).

Usage: python3 checks/check_article3.py [--full]
"""
from __future__ import annotations

import itertools
import sys
from math import comb

FULL = "--full" in sys.argv


def fail(msg: str) -> None:
    print("FAIL:", msg)
    sys.exit(1)


# ---------------------------------------------------------------- word-level counting
def count(w, pat) -> int:
    """Occurrences of pat as a scattered subword of w."""
    dp = [1] + [0] * len(pat)
    for x in w:
        for i in range(len(pat), 0, -1):
            if pat[i - 1] == x:
                dp[i] += dp[i - 1]
    return dp[-1]


def E(w, j, l) -> int:
    return count(w, list(range(j, l + 1)))


def words(content):
    letters = [i + 1 for i, c in enumerate(content) for _ in range(c)]
    return sorted(set(itertools.permutations(letters)))


# ---------------------------------------------------------------- [1]
def check_1() -> None:
    contents = [c for k in (3, 4, 5) for c in itertools.product(range(1, 4), repeat=k)
                if sum(c) <= 9]
    n_rect = n_thm = 0
    for c in contents:
        k = len(c)
        for w in words(c):
            for e in range(1, k):
                if count(w, [e, e + 1, e, e + 1]) == 0:
                    for j in range(1, e + 1):
                        for l in range(e + 1, k + 1):
                            if E(w, j, l) * E(w, e, e + 1) != E(w, j, e + 1) * E(w, e, l):
                                fail(f"rectangle rule {w} j={j} e={e} l={l}")
                            n_rect += 1
            for j in range(1, k + 1):
                for l in range(j + 3, k + 1):
                    if any(c[m - 1] > 2 for m in range(j + 1, l)):
                        continue
                    inner = range(j + 1, l - 1)
                    x = {e: E(w, e, e + 1) for e in inner}
                    if any(x[e] == 0 for e in inner):
                        val = 0
                    else:
                        cross = [e for e in inner if not (c[e - 1] == 2 and c[e] == 2 and x[e] == 3)]
                        if cross:
                            e = cross[0]
                            num = E(w, j, e + 1) * E(w, e, l)
                            if num % x[e]:
                                fail(f"case (b) not integral {w} {j} {l}")
                            val = num // x[e]
                        else:
                            X, Y = E(w, j, j + 1), E(w, j, j + 2)
                            Xp, Yp = E(w, l - 1, l), E(w, l - 2, l)
                            p = l - j - 2
                            val = (Y - X) * (2 * Xp - Yp) + p * (Y - X) * (Yp - Xp) + (2 * X - Y) * (Yp - Xp)
                    if val != E(w, j, l):
                        fail(f"Theorem 4.2 {w} window [{j},{l}]")
                    n_thm += 1
    print(f"[1] rectangle rule: {n_rect} instances; Theorem 4.2: {n_thm} windows "
          f"({len(contents)} contents) -- ok")


# ---------------------------------------------------------------- projections (trace classes)
def projections(a, b):
    return list(itertools.combinations_with_replacement(range(a + 1), b))


def window_entries(c, lams):
    """All entries E_{i,j} (0-based letters) of the window with projections lams."""
    m = len(c)
    ent = {}
    for i in range(m):
        v = [1] * c[i]
        ent[(i, i)] = c[i]
        for l in range(i + 1, m):
            lam = lams[l - 1]
            pre = [0]
            for t in v:
                pre.append(pre[-1] + t)
            v = [pre[h] for h in lam]
            ent[(i, l)] = sum(v)
    return ent


def corner_independent(c) -> bool:
    m = len(c)
    seen = {}
    for lams in itertools.product(*[projections(c[e], c[e + 1]) for e in range(m - 1)]):
        ent = window_entries(c, lams)
        corner = ent.pop((0, m - 1))
        key = tuple(sorted(ent.items()))
        if seen.setdefault(key, corner) != corner:
            return True
    return False


# ---------------------------------------------------------------- [2]
def check_2() -> None:
    u, v = (2, 1, 3, 3, 2), (3, 2, 1, 2, 3)
    if not (E(u, 1, 2) == E(v, 1, 2) and E(u, 2, 3) == E(v, 2, 3)
            and (E(u, 1, 3), E(v, 1, 3)) == (0, 1)):
        fail("Example 4.5, 21332 / 32123")
    for a, b, c in itertools.product(range(1, 5), repeat=3):
        if corner_independent((a, b, c)) != (b >= 2 and max(a, c) >= 2):
            fail(f"three-letter criterion at {(a, b, c)}")
    print("[2] Example 4.5 and the three-letter criterion for a, b, c <= 4 -- ok")


# ---------------------------------------------------------------- [3]
def realise(content, lams):
    """A word (letters 1..k) with the given projections, by the insertion of Section 2."""
    w = [1] * content[0]
    for e, lam in enumerate(lams, start=1):
        pos = [i for i, x in enumerate(w) if x == e]
        ins = sorted(((pos[h] if h < len(pos) else len(w)), t) for t, h in enumerate(lam))
        out, k = [], 0
        for i in range(len(w) + 1):
            while k < len(ins) and ins[k][0] == i:
                out.append(e + 1)
                k += 1
            if i < len(w):
                out.append(w[i])
        w = out
    return w


def ballot_lhs(n, a, b) -> int:
    v = [1] * n
    for t in range(a, b + 1):
        pre, s = [], 0
        for x in v:
            s += x
            pre.append(s)
        pre[t - 1] -= v[t - 1]
        v = pre
    return sum(v)


def family(n):
    L = lambda t: tuple(s if s != t else t - 1 for s in range(1, n + 1))
    e1 = tuple([0] * (n - 1) + [1])
    content = [1] + [n] * n
    A = realise(content, [e1] + [L(t) for t in range(1, n)])
    B = realise(content, [e1] + [L(t) for t in range(2, n + 1)])
    return A, B


def all_entries(w, k):
    return {(j, l): E(w, j, l) for j in range(1, k + 1) for l in range(j, k + 1)}


def check_3() -> None:
    for n in range(2, 31):
        for m in range(1, n + 1):
            for a in range(1, n - m + 2):
                if ballot_lhs(n, a, a + m - 1) != comb(n + m, m + 1) - comb(n + m, m - 1):
                    fail(f"Lemma 5.1 n={n} m={m} a={a}")
            if (comb(n + m, m + 1) - comb(n + m, m - 1)) * (n + 1) != (n - m) * comb(n + m + 1, m + 1):
                fail(f"ballot closed form n={n} m={m}")
        A, B = family(n)
        k = n + 1
        EA, EB = all_entries(A, k), all_entries(B, k)
        for key in EA:
            if key == (1, k):
                continue
            if EA[key] != EB[key]:
                fail(f"Theorem B n={n} entry {key}")
            j, l = key
            if j >= 2 and l > j and EA[key] != comb(n + l - j, l - j + 1) - comb(n + l - j, l - j - 1):
                fail(f"Theorem B ballot value n={n} {key}")
        if (EA[(1, k)], EB[(1, k)]) != (1, 0):
            fail(f"Theorem B corner n={n}")
        if EA[(2, k)] != comb(2 * n, n) // (n + 1):
            fail(f"Catalan n={n}")
    printed = {2: ("32123", "21332"), 3: ("3221443234", "2343212443"),
               4: ("32245432132554345", "23432215454323554")}
    for n, (sa, sb) in printed.items():
        A, B = family(n)
        if "".join(map(str, A)) != sa or "".join(map(str, B)) != sb:
            fail(f"printed words n={n}")
    print("[3] Lemma 5.1 and Theorem B for 2 <= n <= 30, Catalan value, printed words -- ok")


# ---------------------------------------------------------------- [4]
def check_4() -> None:
    expected = {3: (30, 5), 4: (173, 39), 5: (993, 261), 6: (5702, 1577),
                7: (32745, 9049), 8: (188045, 50181)}
    kmax = 8 if FULL else 7
    for k in range(3, kmax + 1):
        c = (2,) * k
        full_of = {}
        by_psi2 = {}
        for lams in itertools.product(projections(2, 2), repeat=k - 1):
            ent = window_entries(c, lams)
            full = tuple(sorted(ent.items()))
            short = tuple(v for (i, j), v in sorted(ent.items()) if j - i <= 2)
            if full_of.setdefault(short, full) != full:
                fail(f"Corollary 4.6 k={k}: diagonals 3-4 do not determine the matrix")
            psi2 = tuple(ent[(i, i + 1)] for i in range(k - 1))
            by_psi2.setdefault(psi2, set()).add(full)
        classes = len(full_of)
        split = sum(1 for s in by_psi2.values() if len(s) > 1)
        if (classes, split) != expected[k]:
            fail(f"Corollary 4.6 numbers k={k}: {(classes, split)}")
    print(f"[4] Corollary 4.6 for 3 <= k <= {kmax} -- ok")


# ---------------------------------------------------------------- [5]
def check_5() -> None:
    n2 = [c for k in range(3, 9) for c in itertools.product((1, 2), repeat=k) if sum(c) <= 11]
    for c in n2:
        # every window of length >= 4 with inner letters <= 2 is determined (Theorem A)
        if len(c) >= 4 and corner_independent(c):
            fail(f"Table 2, n = 2: {c}")
    ends = range(1, 7) if FULL else range(1, 3)
    n3 = 0
    for x, y, z in itertools.product((1, 2, 3), repeat=3):
        if max(x, y, z) != 3:
            continue
        for a, c in itertools.product(ends, repeat=2):
            if (a, x, y, z, c) > (c, z, y, x, a):
                continue
            if corner_independent((a, x, y, z, c)):
                fail(f"Table 2, n = 3: {(a, x, y, z, c)}")
            n3 += 1
    for a, c in itertools.product(range(1, 7 if FULL else 4), repeat=2):
        if corner_independent((a, 3, 3, c)) != (max(a, c) >= 3):
            fail(f"Section 7, (a,3,3,c) at {(a, c)}")
    n4 = 0
    if FULL:
        for a, c in itertools.product(range(1, 5), repeat=2):
            if a > c:
                continue
            if corner_independent((a, 4, 4, 4, c)) != (a + c >= 5):
                fail(f"Table 2, n = 4: {(a, 4, 4, 4, c)}")
            n4 += 1
    print(f"[5] Table 2: {len(n2)} contents with n_i <= 2; (a,3,3,c) rule; {n3} five-letter n = 3 windows"
          + (f"; {n4} five-letter n = 4 windows" if FULL else "") + " -- ok")


if __name__ == "__main__":
    check_1()
    check_2()
    check_3()
    check_4()
    check_5()
    print("check_article3: all checks passed" + (" (--full)" if FULL else ""))
