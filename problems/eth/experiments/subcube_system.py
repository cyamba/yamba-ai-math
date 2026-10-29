#!/usr/bin/env python3
"""The subcube system of CP(Q, R) (subresult SR-11): exact checks and convex relaxations.

SR-11 proves that an edge function d is the defect function e -> p_u(x_t) + p_{u+e_t}(x_t) of a
family (polynomials of degree < R with p(0) = 1) if and only if every R-dimensional subcube Gamma
with direction set T satisfies

    sum_{e in E(Gamma)} lambda^T_{t(e)} d_e = 2^R,   lambda^T_t = prod_{s in T, s != t} x_s / (x_s - x_t).

So a set B of edges can be the bad set of a family (all other edges good) iff the subcube system
has a solution supported on B. This script

  * compares that criterion, in exact rational arithmetic, with the original polynomial system
    (cube_polynomial.exact_feasible) on random edge sets and on every optimal and slab bad set
    recorded in results/cube_polynomial.jsonl, together with one-edge modifications of them;
  * runs iteratively reweighted l1 minimization (total and worst-direction weights) on the
    system, to test whether convex relaxations find sparse, direction-balanced solutions.

Usage: python3 subcube_system.py --out results/subcube_system.json
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
import time
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix, csr_matrix, hstack

from cube_polynomial import edges, exact_feasible, slab_bad

HERE = Path(__file__).parent


def lagrange_weights(T, nodes):
    weights = {}
    for t in T:
        w = Fraction(1) if isinstance(nodes[0], Fraction) else 1.0
        for s in T:
            if s != t:
                w *= nodes[s] / (nodes[s] - nodes[t])
        weights[t] = w
    return weights


def subcubes(Q, R):
    """Yield (T, list of edges (v, t) of the subcube) for every R-dimensional subcube."""
    for T in itertools.combinations(range(Q), R):
        others = [s for s in range(Q) if s not in T]
        for bits in range(1 << len(others)):
            base = sum(1 << others[i] for i in range(len(others)) if (bits >> i) & 1)
            cube_edges = []
            for t in T:
                rest = [s for s in T if s != t]
                for sub in range(1 << len(rest)):
                    v = base | sum(1 << rest[i] for i in range(len(rest)) if (sub >> i) & 1)
                    cube_edges.append((v, t))
            yield T, cube_edges


def consistent(rows, rhs) -> bool:
    """Exact Gaussian elimination on sparse rows (dict column -> Fraction)."""
    pivots = {}
    for row, b in zip(rows, rhs):
        row = {k: v for k, v in row.items() if v != 0}
        while row:
            k = min(row)
            if k not in pivots:
                break
            prow, pb = pivots[k]
            f = row[k] / prow[k]
            for kk, vv in prow.items():
                row[kk] = row.get(kk, 0) - f * vv
                if row[kk] == 0:
                    del row[kk]
            b -= f * pb
        if not row:
            if b != 0:
                return False
            continue
        pivots[min(row)] = (row, b)
    return True


def subcube_feasible(Q, R, nodes, bad) -> bool:
    """Is there a solution of the subcube system supported on the edge set `bad`?"""
    index = {e: i for i, e in enumerate(sorted(set(bad)))}
    rows, rhs = [], []
    for T, cube_edges in subcubes(Q, R):
        lam = lagrange_weights(T, nodes)
        row = {}
        for e in cube_edges:
            if e in index:
                row[index[e]] = row.get(index[e], 0) + lam[e[1]]
        rows.append(row)
        rhs.append(Fraction(2) ** R)
    return consistent(rows, rhs)


def compare(seed: int = 1) -> dict:
    rng = random.Random(seed)
    records = {}
    log = HERE / "results/cube_polynomial.jsonl"
    for line in log.read_text().splitlines():
        r = json.loads(line)
        records[(r["Q"], r["R"])] = r
    total = agree = 0
    mismatches = []
    for Q, R in sorted(records):
        nodes = [Fraction(t + 1, Q) for t in range(Q)]
        E = edges(Q)
        tests = []
        for _ in range(25 if Q <= 5 else 10):
            k = rng.randint(1, len(E))
            tests.append(rng.sample(E, k))
        named = [[tuple(e) for e in records[(Q, R)][key]["bad_edges"]]
                 for key in ("realizable_total", "realizable_max_direction")
                 if records[(Q, R)][key].get("bad_edges")]
        named += [[tuple(e) for e in slab_bad(Q, R, s)] for s in range(R)]
        for bad in named:
            tests.append(bad)
            for _ in range(3):
                if len(bad) > 1:
                    i = rng.randrange(len(bad))
                    tests.append(bad[:i] + bad[i + 1:])
        for bad in tests:
            bad_set = set(bad)
            good = [e for e in E if e not in bad_set]
            a = exact_feasible(Q, R, nodes, good)
            b = subcube_feasible(Q, R, nodes, bad)
            total += 1
            agree += a == b
            if a != b:
                mismatches.append({"Q": Q, "R": R, "bad": bad})
    return {"tests": total, "agree": agree, "mismatches": mismatches}


def float_system(Q, R, nodes):
    E = edges(Q)
    index = {e: i for i, e in enumerate(E)}
    rows, cols, vals = [], [], []
    for r, (T, cube_edges) in enumerate(subcubes(Q, R)):
        lam = lagrange_weights(T, nodes)
        for e in cube_edges:
            rows.append(r)
            cols.append(index[e])
            vals.append(lam[e[1]])
    M = coo_matrix((vals, (rows, cols)), shape=(r + 1, len(E))).tocsr()
    return E, M


def reweighted_l1(Q, R, objective: str, iters: int = 15, eps: float = 1e-3, seed: int = 0):
    nodes = [(t + 1) / Q for t in range(Q)]
    E, M = float_system(Q, R, nodes)
    m, n = M.shape
    b = np.full(m, 2.0 ** R)
    dirs = np.array([e[1] for e in E])
    w = np.ones(n) * (1 + 0.05 * np.random.default_rng(seed).random(n))
    best = None
    for _ in range(iters):
        if objective == "total":
            c = np.concatenate([w, w])
            res = linprog(c, A_eq=hstack([M, -M]).tocsr(), b_eq=b, bounds=(0, None), method="highs")
            x = res.x
        else:
            c = np.concatenate([1e-4 * w, 1e-4 * w, [1.0]])
            r_, c_, v_ = [], [], []
            for t in range(Q):
                for i in np.where(dirs == t)[0]:
                    r_ += [t, t]
                    c_ += [i, n + i]
                    v_ += [w[i], w[i]]
                r_.append(t)
                c_.append(2 * n)
                v_.append(-1.0)
            A_ub = coo_matrix((v_, (r_, c_)), shape=(Q, 2 * n + 1)).tocsr()
            A_eq = hstack([M, -M, csr_matrix((m, 1))]).tocsr()
            res = linprog(c, A_ub=A_ub, b_ub=np.zeros(Q), A_eq=A_eq, b_eq=b, bounds=(0, None),
                          method="highs")
            x = res.x
        if res.status != 0:
            break
        d = x[:n] - x[n:2 * n]
        support = np.abs(d) > 1e-7 * max(1.0, np.abs(d).max())
        per = [int(support[dirs == t].sum()) for t in range(Q)]
        candidate = (max(per), int(support.sum()), per)
        if best is None or candidate[:2] < best[:2]:
            best = candidate
        w = 1.0 / (np.abs(d) + eps)
    return best


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=HERE / "results/subcube_system.json")
    args = parser.parse_args()
    t0 = time.time()
    result = {"comparison": compare()}
    print("exact comparison:", result["comparison"]["agree"], "of", result["comparison"]["tests"])
    relax = []
    for Q, R in [(4, 3), (5, 3), (5, 4), (6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 4)]:
        slab = min((max(sum(1 for e in slab_bad(Q, R, s) if e[1] == t) for t in range(Q)),
                    len(slab_bad(Q, R, s))) for s in range(R))
        row = {"Q": Q, "R": R, "slab_max_total": slab}
        for objective in ("total", "max"):
            best = min((reweighted_l1(Q, R, objective, seed=s) for s in range(3)), key=lambda b: b[:2])
            row[objective] = {"max": best[0], "total": best[1], "per_direction": best[2]}
        print(row, flush=True)
        relax.append(row)
    result["reweighted_l1"] = relax
    result["seconds"] = round(time.time() - t0, 1)
    args.out.write_text(json.dumps(result, indent=1) + "\n")


if __name__ == "__main__":
    main()
