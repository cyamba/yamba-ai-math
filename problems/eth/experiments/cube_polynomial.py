#!/usr/bin/env python3
"""Exact small cases of the cube polynomial problem CP(Q, R).

Point-dependent designs in the swap algebra of openai/math result 378 reduce to the following
problem (subresult SR-02). Attach to every vertex v of the cube {0,1}^Q a polynomial

    p_v(T) = 1 + a_{v,1} T + ... + a_{v,R-1} T^{R-1}        (degree < R, p_v(0) = 1).

Direction t has an evaluation node x_t (distinct, nonzero). The edge {v, v + e_t} is *good* when
p_v(x_t) + p_{v+e_t}(x_t) = 0 and *bad* otherwise. Bad edges in direction t are exactly the
measurements the design needs at node t (SR-02, SR-03), so the quantity that matters for the
algorithm is beta = max_t (bad edges in direction t) / 2^(Q-1).

This script computes, for small Q and R,
  * hit(Q,R): the minimum number of edges meeting every R-dimensional subcube (a relaxation,
    hence a lower bound, by the subcube obstruction proved in Lean);
  * opt(Q,R): the true minimum number of bad edges over all polynomial families, by a mixed
    integer program whose optimal good-edge set is then re-checked in exact rational
    arithmetic (a floating-point solution is never trusted on its own);
  * the same two quantities for the max-over-directions objective;
  * the slab and window constructions of SR-04 (bad-edge counts, each re-checked exactly).

Usage:  python3 cube_polynomial.py --out results/cube_polynomial.json
"""

from __future__ import annotations

import argparse
import itertools
import json
import time
from fractions import Fraction
from math import comb
from pathlib import Path

import numpy as np
from scipy.optimize import LinearConstraint, Bounds, milp
from scipy.sparse import lil_matrix


# ----------------------------------------------------------------------------- cube helpers

def edges(Q: int) -> list[tuple[int, int]]:
    """Edges as (v, t) with bit t of v equal to 0; the other endpoint is v | (1 << t)."""
    return [(v, t) for t in range(Q) for v in range(1 << Q) if not (v >> t) & 1]


def subcube_edge_sets(Q: int, R: int, index: dict) -> list[list[int]]:
    """For every R-dimensional subcube, the indices of its R * 2^(R-1) edges."""
    result = []
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
            result.append(ids)
    return result


def parity(v: int) -> int:
    return bin(v).count("1") & 1


# ----------------------------------------------------------------------------- exact check

def exact_feasible(Q: int, R: int, nodes: list[Fraction], good: list[tuple[int, int]]) -> bool:
    """Exact rational test: is there a family with every edge in `good` good?

    Unknowns a_{v,k} (k = 1..R-1). Each good edge (v, t) gives
        sum_k (a_{v,k} + a_{v',k}) x_t^k = -2.
    Gaussian elimination over Q with Fractions; returns False iff the system is inconsistent.
    """
    if R == 1:
        return not good  # p_v = 1 constant; every edge has sum 2 != 0
    rows = []
    for (v, t) in good:
        w = v | (1 << t)
        row = {}
        for k in range(1, R):
            c = nodes[t] ** k
            for u in (v, w):
                key = u * (R - 1) + (k - 1)
                row[key] = row.get(key, Fraction(0)) + c
        rows.append((row, Fraction(-2)))
    pivots: dict[int, tuple[dict, Fraction]] = {}
    for row, rhs in rows:
        row = {k: c for k, c in row.items() if c != 0}
        # reduce against existing pivots
        while row:
            col = min(row)
            if col in pivots:
                prow, prhs = pivots[col]
                factor = row[col]
                for k, c in prow.items():
                    nv = row.get(k, Fraction(0)) - factor * c
                    if nv == 0:
                        row.pop(k, None)
                    else:
                        row[k] = nv
                rhs = rhs - factor * prhs
            else:
                lead = row[col]
                row = {k: c / lead for k, c in row.items()}
                rhs = rhs / lead
                pivots[col] = (row, rhs)
                break
        else:
            if rhs != 0:
                return False
    return True


# ----------------------------------------------------------------------------- MILPs

def min_hitting(Q: int, R: int, objective: str = "total", time_limit: float = 600.0) -> dict:
    E = edges(Q)
    index = {e: i for i, e in enumerate(E)}
    sets = subcube_edge_sets(Q, R, index)
    n = len(E)
    extra = 1 if objective == "max" else 0
    A = lil_matrix((len(sets) + (Q if extra else 0), n + extra))
    for r_, ids in enumerate(sets):
        for i in ids:
            A[r_, i] = 1
    lo = [1] * len(sets)
    hi = [np.inf] * len(sets)
    if extra:
        for t in range(Q):
            row = len(sets) + t
            for i, (v, tt) in enumerate(E):
                if tt == t:
                    A[row, i] = 1
            A[row, n] = -1
            lo.append(-np.inf)
            hi.append(0)
    c = np.zeros(n + extra)
    if extra:
        c[n] = 1
    else:
        c[:n] = 1
    integrality = np.ones(n + extra)
    bounds = Bounds(np.zeros(n + extra), np.r_[np.ones(n), [np.inf] * extra])
    t0 = time.time()
    res = milp(c, constraints=LinearConstraint(A.tocsr(), lo, hi), integrality=integrality,
               bounds=bounds, options={"time_limit": time_limit})
    z = np.round(res.x[:n]).astype(int) if res.x is not None else None
    value = int(round(res.fun)) if res.x is not None else None
    return {"value": value, "status": res.status, "message": res.message,
            "seconds": round(time.time() - t0, 2),
            "bad": [E[i] for i in range(n) if z is not None and z[i] == 1]}


def min_bad_realizable(Q: int, R: int, nodes: list[Fraction], objective: str = "total",
                       big_m: float = 1e4, coef_bound: float = 200.0,
                       time_limit: float = 900.0) -> dict:
    """MILP over families p_v; returns the optimal bad-edge set and its exact verification."""
    E = edges(Q)
    n = len(E)
    nv = (1 << Q) * (R - 1)
    extra = 1 if objective == "max" else 0
    nz = n
    ncols = nv + nz + extra
    A = lil_matrix((2 * n + (Q if extra else 0), ncols))
    lo, hi = [], []
    xs = [float(x) for x in nodes]
    for i, (v, t) in enumerate(E):
        w = v | (1 << t)
        for sign_row, (l, h) in ((0, (-np.inf, -2.0)), (1, (-2.0, np.inf))):
            row = 2 * i + sign_row
            for k in range(1, R):
                c = xs[t] ** k
                A[row, v * (R - 1) + k - 1] += c
                A[row, w * (R - 1) + k - 1] += c
            # defect d = 2 + sum(...) ; need -M z <= d <= M z
            A[row, nv + i] = -big_m if sign_row == 0 else big_m
            lo.append(l)
            hi.append(h)
    if extra:
        for t in range(Q):
            row = 2 * n + t
            for i, (v, tt) in enumerate(E):
                if tt == t:
                    A[row, nv + i] = 1
            A[row, nv + nz] = -1
            lo.append(-np.inf)
            hi.append(0)
    c = np.zeros(ncols)
    if extra:
        c[nv + nz] = 1
    else:
        c[nv:nv + nz] = 1
    integrality = np.r_[np.zeros(nv), np.ones(nz), np.ones(extra)]
    lb = np.r_[-coef_bound * np.ones(nv), np.zeros(nz), np.zeros(extra)]
    ub = np.r_[coef_bound * np.ones(nv), np.ones(nz), np.inf * np.ones(extra)]
    t0 = time.time()
    res = milp(c, constraints=LinearConstraint(A.tocsr(), lo, hi), integrality=integrality,
               bounds=Bounds(lb, ub), options={"time_limit": time_limit, "mip_rel_gap": 0})
    out = {"status": res.status, "message": res.message, "seconds": round(time.time() - t0, 2)}
    if res.x is None:
        return out
    z = np.round(res.x[nv:nv + nz]).astype(int)
    bad = [E[i] for i in range(n) if z[i] == 1]
    good = [E[i] for i in range(n) if z[i] == 0]
    out.update(value=int(round(res.fun)), bad=bad,
               exact_good_set_feasible=exact_feasible(Q, R, nodes, good),
               mip_dual_bound=getattr(res, "mip_dual_bound", None))
    return out


# ----------------------------------------------------------------------------- constructions

def slab_bad(Q: int, R: int, shift: int) -> list[tuple[int, int]]:
    """SR-04 slab construction: slabs of R consecutive Hamming weights starting at `shift`
    (mod R); an edge is bad iff its endpoints lie in different slabs."""
    def slab(w):
        return (w - shift) // R
    return [(v, t) for (v, t) in edges(Q)
            if slab(bin(v).count("1")) != slab(bin(v).count("1") + 1)]


def window_bad(Q: int, R: int, low: int) -> list[tuple[int, int]]:
    """Single window {low, ..., low+R-1} of weights (the preprint's point-independent choice):
    an edge is bad iff an endpoint lies outside the window."""
    win = set(range(low, low + R))
    return [(v, t) for (v, t) in edges(Q)
            if not ({bin(v).count("1"), bin(v).count("1") + 1} <= win)]


def per_direction(Q: int, bad: list[tuple[int, int]]) -> list[int]:
    counts = [0] * Q
    for (_, t) in bad:
        counts[t] += 1
    return counts


# ----------------------------------------------------------------------------- driver

def run(cases, nodes_kind: str, time_limit: float, log: Path | None = None) -> list[dict]:
    rows = []
    for (Q, R) in cases:
        if nodes_kind == "integers":
            nodes = [Fraction(t + 1) for t in range(Q)]
        else:  # scaled to (0, 1] for conditioning
            nodes = [Fraction(t + 1, Q) for t in range(Q)]
        E = edges(Q)
        row = {"Q": Q, "R": R, "edges": len(E), "edges_per_direction": 1 << (Q - 1),
               "nodes": [str(x) for x in nodes],
               "subcube_bound_total": None}
        # averaging bound: every R-subcube needs a bad edge and each edge lies in C(Q-1,R-1) of them
        row["averaging_lower_bound_total"] = -(-comb(Q, R) * 2 ** (Q - R) // comb(Q - 1, R - 1))
        h_tot = min_hitting(Q, R, "total", time_limit)
        h_max = min_hitting(Q, R, "max", time_limit)
        row["hitting_total"] = {k: h_tot[k] for k in ("value", "status", "seconds")}
        row["hitting_max_direction"] = {k: h_max[k] for k in ("value", "status", "seconds")}
        best_slab = min((slab_bad(Q, R, s) for s in range(R)), key=lambda b: max(per_direction(Q, b)))
        good_slab = sorted(set(E) - set(best_slab))
        row["slab"] = {"total": len(best_slab), "max_direction": max(per_direction(Q, best_slab)),
                       "exact_good_set_feasible": exact_feasible(Q, R, nodes, good_slab)}
        best_win = min((window_bad(Q, R, lo) for lo in range(0, Q - R + 2)),
                       key=lambda b: max(per_direction(Q, b)))
        good_win = sorted(set(E) - set(best_win))
        row["window"] = {"total": len(best_win), "max_direction": max(per_direction(Q, best_win)),
                         "exact_good_set_feasible": exact_feasible(Q, R, nodes, good_win)}
        r_tot = min_bad_realizable(Q, R, nodes, "total", time_limit=time_limit)
        r_max = min_bad_realizable(Q, R, nodes, "max", time_limit=time_limit)
        for name, r in (("realizable_total", r_tot), ("realizable_max_direction", r_max)):
            entry = {k: r.get(k) for k in ("value", "status", "seconds", "exact_good_set_feasible",
                                           "mip_dual_bound")}
            if "bad" in r:
                entry["per_direction"] = per_direction(Q, r["bad"])
                entry["bad_edges"] = [[v, t] for (v, t) in r["bad"]]
            row[name] = entry
        rows.append(row)
        if log is not None:
            with log.open("a") as handle:
                handle.write(json.dumps(row, default=str) + "\n")
        summary = {"Q": Q, "R": R, "hit": row["hitting_total"]["value"],
                   "hit_max": row["hitting_max_direction"]["value"],
                   "opt": row["realizable_total"].get("value"),
                   "opt_status": row["realizable_total"].get("status"),
                   "opt_max": row["realizable_max_direction"].get("value"),
                   "opt_max_status": row["realizable_max_direction"].get("status"),
                   "slab": [row["slab"]["total"], row["slab"]["max_direction"]],
                   "window": [row["window"]["total"], row["window"]["max_direction"]]}
        print(json.dumps(summary), flush=True)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path(__file__).parent / "results/cube_polynomial.json")
    parser.add_argument("--max-q", type=int, default=6)
    parser.add_argument("--nodes", choices=["integers", "scaled"], default="scaled")
    parser.add_argument("--time-limit", type=float, default=900.0)
    parser.add_argument("--min-q", type=int, default=2)
    parser.add_argument("--log", type=Path, default=None)
    args = parser.parse_args()
    cases = [(Q, R) for Q in range(args.min_q, args.max_q + 1) for R in range(2, min(Q, 5) + 1)]
    rows = run(cases, args.nodes, args.time_limit, args.log)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps({"description": __doc__.strip().splitlines()[0],
                                    "nodes": args.nodes, "cases": rows}, indent=1, default=str) + "\n")


if __name__ == "__main__":
    main()
