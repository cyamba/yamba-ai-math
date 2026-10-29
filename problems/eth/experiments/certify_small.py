#!/usr/bin/env python3
"""Exact certification of small optima of CP(Q, R) (total number of bad edges).

Written by the separate review agent of 2026-10-29 and kept here for reproducibility. The MILP
of cube_polynomial.py boxes the polynomial coefficients and runs in floating point, so its
optimality and lower bounds hold only inside that box. This script has no box: it enumerates
edge sets B of increasing size that meet every R-dimensional subcube (necessary by the subcube
obstruction of SR-02) and tests, in exact rational arithmetic, whether all other edges can be
made good. The first size with a feasible complement is the exact optimum.

Nodes x_t = (t+1)/Q, uniform measure. Exhaustive, so only tiny cases are feasible.

Usage: python3 certify_small.py
"""

from __future__ import annotations

import itertools
from fractions import Fraction


def edges(Q):
    return [(v, t) for t in range(Q) for v in range(1 << Q) if not (v >> t) & 1]


def subcubes(Q, R, index):
    out = []
    for T in itertools.combinations(range(Q), R):
        others = [s for s in range(Q) if s not in T]
        for bits in range(1 << len(others)):
            base = sum(1 << others[i] for i in range(len(others)) if (bits >> i) & 1)
            ids = []
            for t in T:
                rest = [s for s in T if s != t]
                for sub in range(1 << len(rest)):
                    v = base | sum(1 << rest[i] for i in range(len(rest)) if (sub >> i) & 1)
                    ids.append(index[(v, t)])
            out.append(frozenset(ids))
    return out


def feasible(Q, R, nodes, good):
    """Exact consistency of p_u(x_t) + p_w(x_t) = 0 on the good edges, p(0) = 1, deg < R."""
    if R == 1:
        return not good
    pivots = {}
    for (v, t) in good:
        w = v | (1 << t)
        row = {}
        for k in range(1, R):
            c = nodes[t] ** k
            for u in (v, w):
                key = u * (R - 1) + k - 1
                row[key] = row.get(key, 0) + c
        rhs = Fraction(-2)
        row = {k: c for k, c in row.items() if c != 0}
        while row:
            col = min(row)
            if col not in pivots:
                lead = row[col]
                pivots[col] = ({k: c / lead for k, c in row.items()}, rhs / lead)
                break
            prow, prhs = pivots[col]
            f = row[col]
            for k, c in prow.items():
                nv = row.get(k, 0) - f * c
                if nv == 0:
                    row.pop(k, None)
                else:
                    row[k] = nv
            rhs -= f * prhs
        else:
            if rhs != 0:
                return False
    return True


def certify(Q, R):
    nodes = [Fraction(t + 1, Q) for t in range(Q)]
    E = edges(Q)
    index = {e: i for i, e in enumerate(E)}
    cubes = subcubes(Q, R, index)
    for size in range(len(E) + 1):
        for B in itertools.combinations(range(len(E)), size):
            Bs = set(B)
            if any(not (c & Bs) for c in cubes):
                continue
            good = [E[i] for i in range(len(E)) if i not in Bs]
            if feasible(Q, R, nodes, good):
                return size, [E[i] for i in B]
    return None


if __name__ == "__main__":
    for Q, R in [(2, 2), (3, 2), (3, 3), (4, 3), (4, 4)]:
        size, bad = certify(Q, R)
        print((Q, R), "exact minimum number of bad edges:", size, "example:", bad, flush=True)
