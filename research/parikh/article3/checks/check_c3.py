#!/usr/bin/env python3
"""Checks for notes/proof-c3.md and for Sections 6-8 of Article 3, version 2
(paper3/article3.tex): Conjecture C at n = 3 (counts of length at most 4 determine the Parikh
matrix when the inner letters occur at most three times), by the pivot-letter method.

Copyright (c) 2026 Christopher Yamba. All rights reserved.

Standard library only; imports nothing from notes/. Exits non-zero on the first failure.
Letters are 0-based inside a window [0, k-1]; a content is a tuple (n_0, ..., n_{k-1}).
Each block names the article's numbering first and the proof note's in brackets.

  [1] Lemma 6.6, the chain lemma [note Lemma 3.3]: for all bounds (alpha, beta) in [0,3]^2
      every rigid chain is the only chain with its signature; the 16 rigid signatures for
      (3,3); all 144 entries and the bold entries of Table 1 [note Table 1]; the failure counts
      at bounds (3,4), (4,3) and (4,4), the (3,7,3) example after Table 1, and the lemma at
      bounds (2,4) and (4,2).
  [2] Lemmas 6.1, 6.2, 6.4, 6.7 and Theorem 6.8 [note Lemmas 2.1-3.4, Theorem 4.1] on every
      projection tuple of the listed contents, at every admissible pivot.
  [3] Theorem 6.8 under its first hypothesis [note Theorem 4.1(a)]: a pivot occurring at most
      twice, with large other multiplicities.
  [4] Literal words: the projection model, the copy data and Theorem 6.8 on every word of
      small contents.
  [5] Corollaries 1.2 and 1.3 [note Corollaries 4.3, 4.4]: on every projection tuple of the
      listed contents, the entries of length at most 4 determine all entries.
  [6] Example 4.5 and Proposition 7.1 [note Proposition 4.5]: every printed witness pair agrees
      on all counts but the corner; the example after Lemma 6.4 (Delta = 12).
  [7] Theorem 6.8 under its second hypothesis on the 27 contents (1,x,y,z,1), x, y, z in [1,3];
      with the reduction at the end of Section 8 [note Remark 7.1] this covers every window.

Usage: python3 checks/check_c3.py [--full]
"""
from __future__ import annotations

import itertools
import sys
import time
from fractions import Fraction

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


def words(content):
    """Every word of the content, without repetition."""
    k, total, rem, w = len(content), sum(content), list(content), []

    def rec():
        if len(w) == total:
            yield tuple(w)
            return
        for x in range(k):
            if rem[x]:
                rem[x] -= 1
                w.append(x)
                yield from rec()
                w.pop()
                rem[x] += 1

    yield from rec()


def word_projections(w, k):
    """lams[e][s] = number of letters e before the s-th letter e+1."""
    lams = []
    for e in range(k - 1):
        seen, lam = 0, []
        for x in w:
            if x == e:
                seen += 1
            elif x == e + 1:
                lam.append(seen)
        lams.append(tuple(lam))
    return lams


# ---------------------------------------------------------------- projections (trace classes)
def projections(a, b):
    return list(itertools.combinations_with_replacement(range(a + 1), b))


def tuples(c):
    return itertools.product(*[projections(c[e], c[e + 1]) for e in range(len(c) - 1)])


def window_entries(c, lams):
    """All entries E_{i,l} (0-based letters) of the window with projections lams."""
    k = len(c)
    ent = {}
    for i in range(k):
        v = [1] * c[i]
        ent[(i, i)] = c[i]
        for l in range(i + 1, k):
            pre = [0]
            for t in v:
                pre.append(pre[-1] + t)
            v = [pre[h] for h in lams[l - 1]]
            ent[(i, l)] = sum(v)
    return ent


def pivot_data(c, lams, m):
    """Copy data at the pivot m of the window [0, k-1] (Section 1 of the note).

    a[r]: letters m-1 before the r-th m;  b[r]: letters m+1 after it;
    F[r] = Phi(a[r]): occurrences of 0..m-1 before it;  G[r] = Psi(b[r]): occurrences of
    m+1..k-1 after it.  Phi[h] sums the first h left weights, Psi[h] the last h right weights.
    """
    k = len(c)
    a = list(lams[m - 1])
    b = [sum(1 for h in lams[m] if h >= r + 1) for r in range(c[m])]
    v = [1] * c[0]
    for e in range(0, m - 1):
        pre = [0]
        for t in v:
            pre.append(pre[-1] + t)
        v = [pre[h] for h in lams[e]]
    Phi = [0]
    for t in v:
        Phi.append(Phi[-1] + t)
    g = [1] * c[k - 1]
    for e in range(k - 2, m, -1):
        lam = lams[e]
        g = [sum(g[u] for u in range(c[e + 1]) if lam[u] >= r + 1) for r in range(c[e])]
    Psi = [0]
    for t in reversed(g):
        Psi.append(Psi[-1] + t)
    return a, b, [Phi[h] for h in a], [Psi[h] for h in b], Phi, Psi


def det3(M):
    (a, b, c), (d, e, f), (g, h, i) = M
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


# ---------------------------------------------------------------- [1] the chain lemma
def chains(alpha, beta):
    A = list(itertools.combinations_with_replacement(range(alpha + 1), 3))
    B = [tuple(reversed(t)) for t in itertools.combinations_with_replacement(range(beta + 1), 3)]
    return [(a, b) for a in A for b in B]


def signature(a, b):
    return (sum(a), sum(b), sum(x * y for x, y in zip(a, b)))


def is_rigid(a, b):
    return len(set(a)) == 3 and len(set(b)) == 3


def rigid_table(alpha, beta):
    """(signature -> the rigid chain, list of colliding signatures)."""
    by_sig = {}
    for a, b in chains(alpha, beta):
        by_sig.setdefault(signature(a, b), []).append((a, b))
    table, collisions = {}, []
    for s, lst in by_sig.items():
        rig = [ch for ch in lst if is_rigid(*ch)]
        if rig:
            if len(lst) == 1:
                table[s] = rig[0]
            else:
                collisions.append(s)
    return table, collisions


RIGID = {}

# Table 1 of the note: (sum a, sum b) -> rows a', columns b', entries sum a'b' (* = rigid chain).
TABLE1 = """
3 3 | 003 012 111 | 300 210 111 | 0 0 3 / 0 1* 3 / 3 3 3
3 4 | 003 012 111 | 310 220 211 | 0 0 3 / 1* 2 3 / 4 4 4
3 5 | 003 012 111 | 320 311 221 | 0 3 3 / 2* 3 4 / 5 5 5
3 6 | 003 012 111 | 330 321 222 | 0 3 6 / 3 4* 6 / 6 6 6
4 3 | 013 022 112 | 300 210 111 | 0 1* 4 / 0 2 4 / 3 3 4
4 4 | 013 022 112 | 310 220 211 | 1* 2 4 / 2 4 4 / 4 4 5
4 5 | 013 022 112 | 320 311 221 | 2* 4 5 / 4 4 6 / 5 6 6
4 6 | 013 022 112 | 330 321 222 | 3 5* 8 / 6 6 8 / 6 7 8
5 3 | 023 113 122 | 300 210 111 | 0 2* 5 / 3 3 5 / 3 4 5
5 4 | 023 113 122 | 310 220 211 | 2* 4 5 / 4 4 6 / 5 6 6
5 5 | 023 113 122 | 320 311 221 | 4* 5 7 / 5 7 7 / 7 7 8
5 6 | 023 113 122 | 330 321 222 | 6 7* 10 / 6 8 10 / 9 9 10
6 3 | 033 123 222 | 300 210 111 | 0 3 6 / 3 4* 6 / 6 6 6
6 4 | 033 123 222 | 310 220 211 | 3 6 6 / 5* 6 7 / 8 8 8
6 5 | 033 123 222 | 320 311 221 | 6 6 9 / 7* 8 9 / 10 10 10
6 6 | 033 123 222 | 330 321 222 | 9 9 12 / 9 10* 12 / 12 12 12
"""


def check_table1() -> None:
    """Every entry and star of Table 1, and that the rows and columns list all chains."""
    for line in TABLE1.strip().splitlines():
        head, rows, cols, body = (part.split() for part in line.split("|"))
        sa, sb = int(head[0]), int(head[1])
        A = [tuple(map(int, t)) for t in rows]
        B = [tuple(map(int, t)) for t in cols]
        allA = [a for a in itertools.combinations_with_replacement(range(4), 3) if sum(a) == sa]
        allB = [tuple(reversed(b)) for b in itertools.combinations_with_replacement(range(4), 3)
                if sum(b) == sb]
        if sorted(A) != sorted(allA) or sorted(B) != sorted(allB):
            fail(f"Table 1 cell ({sa},{sb}): rows or columns incomplete")
        cells = [x for x in body if x != "/"]
        stars, values = [], []
        for idx, x in enumerate(cells):
            a, b = A[idx // 3], B[idx % 3]
            if int(x.rstrip("*")) != sum(p * q for p, q in zip(a, b)):
                fail(f"Table 1 cell ({sa},{sb}) entry {a}, {b}")
            if x.endswith("*"):
                stars.append((a, b))
            values.append(int(x.rstrip("*")))
        if len(stars) != 1 or not is_rigid(*stars[0]):
            fail(f"Table 1 cell ({sa},{sb}): star")
        star_val = sum(p * q for p, q in zip(*stars[0]))
        if values.count(star_val) != 1:
            fail(f"Table 1 cell ({sa},{sb}): rigid value not unique")


def check_1() -> None:
    for alpha in range(4):
        for beta in range(4):
            table, collisions = rigid_table(alpha, beta)
            if collisions:
                fail(f"chain lemma, bounds ({alpha},{beta}): {collisions}")
            RIGID[(alpha, beta)] = table
    t33 = RIGID[(3, 3)]
    if len(t33) != 16:
        fail(f"expected 16 rigid signatures for (3,3), got {len(t33)}")
    # The printed table of the note: rigid E_{m-1,m+1} by (x_{m-1}, x_m).
    expected = {3: (1, 1, 2, 4), 4: (1, 1, 2, 5), 5: (2, 2, 4, 7), 6: (4, 5, 7, 10)}
    for (sa, sb, sab), _ in t33.items():
        if expected[sa][sb - 3] != sab:
            fail(f"rigid table entry ({sa},{sb})")
    check_table1()
    # Where the lemma fails (Section 3.3): (rigid chains, distinct rigid signatures, colliding).
    for bounds, expect in (((3, 4), (40, 40, 4)), ((4, 3), (40, 40, 4)), ((4, 4), (100, 95, 19))):
        rig = [ch for ch in chains(*bounds) if is_rigid(*ch)]
        table, col = rigid_table(*bounds)
        got = (len(rig), len({signature(*ch) for ch in rig}), len(col))
        if got != expect or len(table) + len(col) != got[1]:
            fail(f"chain lemma failure counts at {bounds}: {got}, expected {expect}")
    # ... while it still holds at bounds (2,4) and (4,2), with 10 rigid chains each.
    for bounds in ((2, 4), (4, 2)):
        rig = [ch for ch in chains(*bounds) if is_rigid(*ch)]
        if len(rig) != 10 or rigid_table(*bounds)[1]:
            fail(f"chain lemma at {bounds}")
    # The example after Table 1: at bounds (3,4) the signature (3,7,3) has exactly these chains.
    with_373 = sorted(ch for ch in chains(3, 4) if signature(*ch) == (3, 7, 3))
    if with_373 != sorted([((0, 0, 3), (3, 3, 1)), ((0, 0, 3), (4, 2, 1)), ((0, 1, 2), (4, 3, 0))]):
        fail(f"(3,7,3) example at bounds (3,4): {with_373}")
    print("[1] Lemma 6.6 [note 3.3]: no collisions for bounds in [0,3]^2; 16 rigid signatures at "
          "(3,3); Table 1 (144 entries); fails at (3,4), (4,3) (40 rigid, 4 colliding; the "
          "(3,7,3) example) and (4,4) (100 rigid chains, 95 signatures, 19 colliding); holds at "
          "(2,4), (4,2) -- ok")


# ---------------------------------------------------------------- Theorem 4.1
def corner_formula(c, E, m):
    """The corner E[(0, k-1)] from the shorter entries of the window, pivot m in [2, k-3].

    Returns (value, case), case in {'i', 'ii', 'iii'}, or (None, 'n/a') when neither hypothesis
    (a) n_m <= 2 nor (b) n_{m-1}, n_m, n_{m+1} <= 3 holds. The corner itself is never read.
    """
    k = len(c)
    j, l = 0, k - 1
    n_m, al, be = c[m], c[m - 1], c[m + 1]
    if not (n_m <= 2 or max(al, n_m, be) <= 3):
        return None, "n/a"
    xa, xb, Eab = E[(m - 1, m)], E[(m, m + 1)], E[(m - 1, m + 1)]
    D = xa * xb - n_m * Eab
    Ejm, Ejm1, Eml, Em1l = E[(j, m)], E[(j, m + 1)], E[(m, l)], E[(m - 1, l)]
    if D == 0:
        return Fraction(Ejm * Eml, n_m), "i"
    rig = rigid_values(c, E, m)
    if rig is not None:
        _, F, G = rig
        return sum(f * g for f, g in zip(F, G)), "ii"
    num = Ejm * xb * Em1l + Ejm1 * xa * Eml - Ejm * Eab * Eml - n_m * Ejm1 * Em1l
    return Fraction(num, D), "iii"


def rigid_values(c, E, m):
    """(chain, F, G) as recovered in case (ii) (Lemmas 3.3, 3.4); None if the signature at the
    pivot is not rigid. Uses only the shorter entries of the window."""
    k = len(c)
    j, l = 0, k - 1
    n_m, al, be = c[m], c[m - 1], c[m + 1]
    xa, xb, Eab = E[(m - 1, m)], E[(m, m + 1)], E[(m - 1, m + 1)]
    ch = RIGID.get((al, be), {}).get((xa, xb, Eab)) if n_m == 3 else None
    if ch is None:
        return None
    (a0, a1, a2), (b0, b1, b2) = ch
    Ejm, Ejm1, Eml, Em1l = E[(j, m)], E[(j, m + 1)], E[(m, l)], E[(m - 1, l)]
    Ftop, Gtop = E[(j, m - 1)], E[(m + 1, l)]
    if a0 == 0:
        F2 = Fraction(Ejm1 - b1 * Ejm, b2 - b1)
        F = (0, Ejm - F2, F2)
    else:
        F1 = Fraction((Ejm1 - b2 * Ftop) - b0 * (Ejm - Ftop), b1 - b0)
        F = (Ejm - Ftop - F1, F1, Ftop)
    if b2 == 0:
        G1 = Fraction(Em1l - a0 * Eml, a1 - a0)
        G = (Eml - G1, G1, 0)
    else:
        G2 = Fraction((Em1l - a0 * Gtop) - a1 * (Eml - Gtop), a2 - a1)
        G = (Gtop, Eml - Gtop - G2, G2)
    return ch, F, G


def check_copy_data(c, lams, E, m, where):
    """Lemmas 2.1, 2.2, 3.1, 3.2 and 3.4 at pivot m; returns the case of Theorem 4.1."""
    k = len(c)
    j, l = 0, k - 1
    a, b, F, G, Phi, Psi = pivot_data(c, lams, m)
    n_m = c[m]
    if any(a[r] > a[r + 1] or b[r] < b[r + 1] for r in range(n_m - 1)):
        fail(f"Lemma 2.2 monotonicity {where}")
    if Phi[0] != 0 or Phi[c[m - 1]] != E[(j, m - 1)] or Psi[0] != 0 or Psi[c[m + 1]] != E[(m + 1, l)]:
        fail(f"Lemma 2.2 boundary values {where}")
    rows = [(F[r], a[r], 1) for r in range(n_m)]
    cols = [(1, b[r], G[r]) for r in range(n_m)]
    M = [[E[(j, m)], E[(j, m + 1)], E[(j, l)]],
         [E[(m - 1, m)], E[(m - 1, m + 1)], E[(m - 1, l)]],
         [E[(m, m)], E[(m, m + 1)], E[(m, l)]]]
    for x in range(3):
        for y in range(3):
            if M[x][y] != sum(rows[r][x] * cols[r][y] for r in range(n_m)):
                fail(f"Lemma 2.1 entry ({x},{y}) {where}")
    D = M[1][0] * M[2][1] - M[2][0] * M[1][1]
    if D != sum((a[q] - a[p]) * (b[p] - b[q]) for p in range(n_m) for q in range(p + 1, n_m)):
        fail(f"Lemma 3.1 identity {where}")
    if (D == 0) != (len(set(a)) <= 1 or len(set(b)) <= 1):
        fail(f"Lemma 3.1 equality case {where}")
    dm = det3(M)
    cb = sum(det3([rows[p], rows[q], rows[s]]) * det3([cols[p], cols[q], cols[s]])
             for p, q, s in itertools.combinations(range(n_m), 3))
    if dm != cb or dm < 0:
        fail(f"Lemma 3.2 Cauchy-Binet / sign {where}")
    val, case = corner_formula(c, E, m)
    if case == "n/a":
        return case
    if val != E[(j, l)]:
        fail(f"Theorem 4.1 case ({case}) {where}: formula {val}, corner {E[(j, l)]}")
    if case == "ii":
        ch, Fr, Gr = rigid_values(c, E, m)
        if ch != (tuple(a), tuple(b)) or tuple(Fr) != tuple(F) or tuple(Gr) != tuple(G):
            fail(f"Lemma 3.3/3.4 rigid recovery {where}")
    elif case == "iii" and dm != 0:
        fail(f"case (iii) with nonzero pivot minor {where}")
    return case


def run_contents(contents, label):
    stats, total = {}, 0
    for c in contents:
        for lams in tuples(c):
            E = window_entries(c, lams)
            total += 1
            for m in range(2, len(c) - 2):
                case = check_copy_data(c, lams, E, m, f"{c} {lams} pivot {m}")
                stats[case] = stats.get(case, 0) + 1
    return total, stats


# ---------------------------------------------------------------- [2]
def check_2() -> None:
    contents = [(1, 3, 3, 3, 1), (2, 3, 3, 3, 2), (3, 3, 3, 3, 3), (3, 2, 3, 3, 3),
                (2, 3, 2, 3, 2), (4, 3, 3, 3, 1), (1, 3, 1, 3, 2), (1, 2, 3, 3, 2),
                (1, 3, 3, 3, 3, 1), (1, 2, 3, 3, 2, 1)]
    if FULL:
        contents += [c for c in itertools.product((1, 2), (1, 2, 3), (1, 2, 3), (1, 2, 3), (1, 2))
                     if c not in contents]
        contents += [(6, 3, 3, 3, 6), (2, 3, 3, 3, 3, 2), (1, 3, 2, 3, 3, 2)]
    total, stats = run_contents(contents, "[2]")
    if stats.get("n/a"):
        fail(f"[2] a listed content outside the hypotheses: {stats}")
    print(f"[2] Lemmas 6.1-6.7, Theorem 6.8 [note 2.1-3.4, 4.1]: {len(contents)} contents, {total} "
          f"projection tuples, cases {dict(sorted(stats.items()))} -- ok")


# ---------------------------------------------------------------- [3]
def check_3() -> None:
    contents = [(2, 4, 2, 4, 2), (1, 5, 2, 5, 1), (3, 4, 1, 4, 3), (1, 6, 2, 6, 1),
                (1, 4, 2, 5, 1), (2, 2, 2, 5, 1)]
    if FULL:
        contents += [(4, 4, 2, 3, 4), (1, 4, 2, 4, 4, 1), (2, 5, 2, 4, 3)]
    total, stats = 0, {}
    for c in contents:
        for lams in tuples(c):
            E = window_entries(c, lams)
            total += 1
            case = check_copy_data(c, lams, E, 2, f"{c} {lams} pivot 2")
            if case not in ("i", "iii"):
                fail(f"[3] unexpected case {case} for {c}")
            stats[case] = stats.get(case, 0) + 1
    print(f"[3] Theorem 6.8, first hypothesis [note 4.1(a)], large neighbours: "
          f"{len(contents)} contents, "
          f"{total} tuples, cases {dict(sorted(stats.items()))} -- ok")


# ---------------------------------------------------------------- [4]
def check_4() -> None:
    contents = [(1, 2, 3, 2, 1), (1, 3, 2, 3, 1), (2, 1, 3, 1, 2), (1, 2, 2, 2, 1, 1)]
    if FULL:
        contents += [(1, 3, 3, 3, 1), (2, 2, 3, 2, 1)]
    nw = 0
    for c in contents:
        k = len(c)
        for w in words(c):
            nw += 1
            lams = word_projections(w, k)
            E = window_entries(c, lams)
            for i in range(k):
                for l in range(i, k):
                    if E[(i, l)] != count(w, list(range(i, l + 1))):
                        fail(f"[4] projection model {w} ({i},{l})")
            for m in range(2, k - 2):
                pos = [p for p, x in enumerate(w) if x == m]
                a = [sum(1 for x in w[:p] if x == m - 1) for p in pos]
                b = [sum(1 for x in w[p + 1:] if x == m + 1) for p in pos]
                F = [count(w[:p], list(range(0, m))) for p in pos]
                G = [count(w[p + 1:], list(range(m + 1, k))) for p in pos]
                a2, b2, F2, G2, _, _ = pivot_data(c, lams, m)
                if (a, b, F, G) != (a2, b2, F2, G2):
                    fail(f"[4] copy data {w} pivot {m}")
                check_copy_data(c, lams, E, m, f"word {w} pivot {m}")
    print(f"[4] literal words: {nw} words of {len(contents)} contents; projection model, "
          f"copy data and Theorem 6.8 -- ok")


# ---------------------------------------------------------------- [5]
def check_5() -> None:
    # Corollary 4.3, then Corollary 4.4 (letters 2 and k-1 unbounded, k >= 6).
    contents = [(1, 3, 3, 3, 3, 1), (1, 2, 3, 3, 2, 1), (2, 3, 3, 3, 2), (3, 3, 2, 3, 3),
                (1, 5, 2, 2, 5, 1), (1, 3, 2, 2, 2, 3, 1)]
    if FULL:
        contents += [(2, 3, 3, 3, 3, 2), (1, 3, 3, 2, 3, 3, 1), (2, 4, 2, 2, 4, 2),
                     (3, 4, 1, 2, 3, 2)]
    for c in contents:
        k = len(c)
        seen, n = {}, 0
        for lams in tuples(c):
            E = window_entries(c, lams)
            n += 1
            key = tuple(E[(i, l)] for i in range(k) for l in range(i, min(k, i + 4)))
            val = tuple(E[(i, l)] for i in range(k) for l in range(i, k))
            if seen.setdefault(key, val) != val:
                fail(f"[5] Corollary 4.3 fails on {c}")
        print(f"    {c}: {n} tuples, {len(seen)} classes of the first five diagonals")
    print(f"[5] Corollaries 1.2, 1.3 [note 4.3, 4.4] (entries of length <= 4 determine all): "
          f"{len(contents)} "
          f"contents -- ok")


# ---------------------------------------------------------------- [6]
# Example 4.5 and Proposition 7.1 [note Proposition 4.5]: (part, w, w', content, corners).
# Letters are 1-based in the strings; "note only" pairs are printed in the note, not the article.
WITNESSES = [
    ("Ex 4.5 [note (a)] A_3/B_3", "3221443234", "2343212443", (1, 3, 3, 3), (1, 0)),
    ("Ex 4.5 [note (a)] Sal06 n=3", "1432432111432", "4321114324321", (4, 3, 3, 3), (1, 0)),
    ("7.1(ii) [note (b)] A_4/B_4", "32245432132554345", "23432215454323554", (1, 4, 4, 4, 4), (1, 0)),
    ("7.1(ii) [note (b)] Sal06 n=4", "154325432111111543254321", "543211115432543211115432",
     (8, 4, 4, 4, 4), (1, 0)),
    ("7.1(iii) [note (c)]", "4321324443", "3214443234", (1, 2, 3, 4), (0, 1)),
    ("note only [note (c)]", "44432132111114443", "44321444321111134", (6, 2, 3, 6), (0, 1)),
    ("note only [note (c)]", "443232121111144443", "324444432121111134", (6, 3, 3, 6), (0, 1)),
    ("7.1(iii) [note (c)]", "543214325555554345", "432155554324355554", (1, 2, 3, 4, 8), (1, 0)),
    ("note only [note (c)]", "54321433255554345", "43215554332435554", (1, 2, 4, 4, 6), (1, 0)),
    ("7.1(i) [note (d)]", "5432143255555543245", "4321555543243255554", (1, 3, 3, 4, 8), (1, 0)),
    ("note only [note (d)]", "54321432555555432245", "43215555432432255554", (1, 4, 3, 4, 8), (1, 0)),
    ("7.1(i) [note (d)]", "543212154321243545", "123214543255454321", (3, 4, 3, 4, 4), (9, 10)),
    ("7.1(ii) [note (e)]", "32543213325554345", "23343215555432354", (1, 3, 5, 3, 5), (1, 0)),
]


def reverse_complement(s: str, k: int) -> str:
    return "".join(str(k + 1 - int(ch)) for ch in reversed(s))


def check_witness(part, A, B, content, corners) -> None:
    k = len(content)
    a, b = tuple(int(ch) - 1 for ch in A), tuple(int(ch) - 1 for ch in B)
    if tuple(a.count(i) for i in range(k)) != content or sorted(a) != sorted(b):
        fail(f"[6] {part} content of {A}, {B}")
    for i in range(k):
        for l in range(i, k):
            ea, eb = count(a, list(range(i, l + 1))), count(b, list(range(i, l + 1)))
            if (i, l) == (0, k - 1):
                if (ea, eb) != corners:
                    fail(f"[6] {part} corners of {A}, {B}: {(ea, eb)}")
            elif ea != eb:
                fail(f"[6] {part} {A}, {B} differ at ({i},{l})")


def check_6() -> None:
    n = 0
    for part, A, B, content, corners in WITNESSES:
        check_witness(part, A, B, content, corners)
        k = len(content)
        # The reverse complement (letter c -> k+1-c, word reversed) is also a witness.
        check_witness(part + " rc", reverse_complement(A, k), reverse_complement(B, k),
                      tuple(reversed(content)), corners)
        n += 2
    # The example after Lemma 6.4: for n_m >= 4 two equal a-values do not force Delta = 0.
    w = tuple(int(ch) - 1 for ch in "43342312515243")
    c = tuple(w.count(i) for i in range(5))
    lams = word_projections(w, 5)
    E = window_entries(c, lams)
    a, b, _, _, _, _ = pivot_data(c, lams, 2)
    M = [[E[(0, 2)], E[(0, 3)], E[(0, 4)]], [E[(1, 2)], E[(1, 3)], E[(1, 4)]],
         [E[(2, 2)], E[(2, 3)], E[(2, 4)]]]
    if (c, a, b, det3(M)) != ((2, 3, 4, 3, 2), [0, 0, 1, 3], [2, 2, 1, 0], 12):
        fail(f"[6] example after Lemma 6.4: {c}, {a}, {b}, {det3(M)}")
    print(f"[6] Example 4.5, Proposition 7.1 [note 4.5]: {n} witness pairs (with reverse "
          f"complements) agree on every count but the corner; Delta = 12 example -- ok")


# ---------------------------------------------------------------- [7]
def check_7() -> None:
    contents = list(itertools.product((1,), (1, 2, 3), (1, 2, 3), (1, 2, 3), (1,)))
    total, stats = run_contents(contents, "[7]")
    if stats.get("n/a"):
        fail(f"[7] a content outside hypothesis (b): {stats}")
    print(f"[7] Theorem 6.8, second hypothesis, on the 27 contents (1,x,y,z,1), x,y,z <= 3 "
          f"(Section 8 reduction [note Remark 7.1]): {total} "
          f"tuples, cases {dict(sorted(stats.items()))} -- ok")


def main() -> None:
    t0 = time.perf_counter()
    check_1()
    check_2()
    check_3()
    check_4()
    check_5()
    check_6()
    check_7()
    print(f"check_c3: all checks passed{' (--full)' if FULL else ''} "
          f"({time.perf_counter() - t0:.1f} s)")


if __name__ == "__main__":
    main()
