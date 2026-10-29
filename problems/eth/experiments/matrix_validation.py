#!/usr/bin/env python3
"""Validate the reduction from point-dependent swap designs to the cube polynomial problem.

For small r and Q we build the actual auxiliary matrices of openai/math result 378, Section 4:
labels u = (a_u, d_u) in [r]^Q x [r]^Q, commuting swaps Pi_s, and from a cube family
p_eps(T) (eps in {0,1}^Q) the matrix polynomial

    P(T) = sum_S c_S(T) Pi_S,   c_S(T) = 2^-Q sum_eps p_eps(T) chi_S(eps).

At node t the *nonlocal* part N_t keeps the entries (u, w) of the full matrix P(x_t) with
a_w(t) != d_u(t) (computed by masking); its rank bounds the measurements needed at t. SR-02 predicts

    rank N_t = r(r-1) * sum over bad edges (eps', eps' + e_t) of m(eps'),
    m(eps') = prod_{s != t} (r(r+1)/2)^(1 - eps'_s) (r(r-1)/2)^(eps'_s),

and SR-03 (Lean) predicts sum_{i in T} rank N_{t_i} >= |A||B| for any R nodes T.
Ranks are computed exactly over the rationals by working modulo two large primes (the rank
over Q is at least the rank modulo p, and agreement for two primes is reported).

Families tested: the slab family of SR-04 (built from Fourier coefficients of the slab
interpolants), the preprint's single-window family, and families solved exactly from the
optimal good-edge sets found by cube_polynomial.py when its log is present.
"""

from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction
from pathlib import Path

PRIMES = (2_147_483_647, 1_000_000_007)


def popcount(v: int) -> int:
    return bin(v).count("1")


def lagrange_poly_values(points, values, at):
    """Value at `at` of the interpolant through (points, values), exact."""
    total = Fraction(0)
    for i, (xi, yi) in enumerate(zip(points, values)):
        term = Fraction(yi)
        for j, xj in enumerate(points):
            if j != i:
                term *= Fraction(at - xj, xi - xj)
        total += term
    return total


def slab_family_values(Q, R, s0, nodes):
    """p_eps(x_t) for the slab family, via the global-formula construction of SR-04."""
    def slab(w):
        return (w + s0) // R
    # f_k interpolates (-1)^w on slab k; g_k(eps) = f_k(|eps|); gamma^k = Fourier coeffs
    vals = {}
    slabs = sorted({slab(w) for w in range(Q + 1)})
    gamma = {}
    for k in slabs:
        pts = [w for w in range(Q + 1) if slab(w) == k]
        g = [lagrange_poly_values(pts, [(-1) ** w for w in pts], popcount(e)) for e in range(1 << Q)]
        gamma[k] = {S: sum(g[e] * (-1) ** popcount(S & e) for e in range(1 << Q)) / (1 << Q)
                    for S in range(1 << Q)}
        assert all(gamma[k][S] == 0 for S in range(1 << Q) if popcount(S) > R - 1)
    for e in range(1 << Q):
        k = slab(popcount(e))
        sigma = (-1) ** popcount(e)
        for t in range(Q):
            x = nodes[t]
            total = Fraction(0)
            for S, gS in gamma[k].items():
                if gS == 0:
                    continue
                phi = Fraction(1)
                for s in range(Q):
                    if (S >> s) & 1:
                        phi *= 1 - x / nodes[s]
                total += gS * phi * (-1) ** popcount(S & e)
            vals[(e, t)] = sigma * total
    return vals


def solve_family_values(Q, R, nodes, good):
    """Particular solution (free variables zero) for a feasible good-edge set; returns p_v(x_t)."""
    nvar = (1 << Q) * (R - 1)
    rows = []
    for (v, t) in good:
        w = v | (1 << t)
        row = {}
        for k in range(1, R):
            for u in (v, w):
                key = u * (R - 1) + k - 1
                row[key] = row.get(key, Fraction(0)) + nodes[t] ** k
        rows.append((row, Fraction(-2)))
    pivots = {}
    order = []
    for row, rhs in rows:
        row = {k: c for k, c in row.items() if c != 0}
        while row:
            col = min(row)
            if col in pivots:
                prow, prhs = pivots[col]
                f = row[col]
                for k, c in prow.items():
                    nv = row.get(k, Fraction(0)) - f * c
                    if nv == 0:
                        row.pop(k, None)
                    else:
                        row[k] = nv
                rhs -= f * prhs
            else:
                lead = row[col]
                pivots[col] = ({k: c / lead for k, c in row.items()}, rhs / lead)
                order.append(col)
                break
        else:
            if rhs != 0:
                raise ValueError("infeasible good-edge set")
    sol = [Fraction(0)] * nvar
    for col in sorted(pivots, reverse=True):
        prow, prhs = pivots[col]
        sol[col] = prhs - sum(c * sol[k] for k, c in prow.items() if k != col)
    vals = {}
    for e in range(1 << Q):
        for t in range(Q):
            vals[(e, t)] = 1 + sum(sol[e * (R - 1) + k - 1] * nodes[t] ** k for k in range(1, R))
    return vals


def window_family_values(Q, R, low, nodes):
    """Preprint's single window: global formula on the window, constant correction outside."""
    pts = list(range(low, low + R))
    g = [lagrange_poly_values(pts, [(-1) ** w for w in pts], popcount(e)) for e in range(1 << Q)]
    gamma = {S: sum(g[e] * (-1) ** popcount(S & e) for e in range(1 << Q)) / (1 << Q)
             for S in range(1 << Q)}
    vals = {}
    for e in range(1 << Q):
        sigma = (-1) ** popcount(e)
        for t in range(Q):
            x = nodes[t]
            total = Fraction(0)
            for S, gS in gamma.items():
                if gS == 0:
                    continue
                phi = Fraction(1)
                for s in range(Q):
                    if (S >> s) & 1:
                        phi *= 1 - x / nodes[s]
                total += gS * phi * (-1) ** popcount(S & e)
            # p_eps(T) = 1 - sigma g(eps) + sigma G(T, eps)
            vals[(e, t)] = 1 - sigma * g[e] + sigma * total
    return vals


def bad_edges(Q, vals):
    return [(v, t) for t in range(Q) for v in range(1 << Q)
            if not (v >> t) & 1 and vals[(v, t)] + vals[(v | (1 << t), t)] != 0]


def rank_mod_p(mat, p):
    """Rank of an integer matrix (list of rows or numpy array) modulo the prime p."""
    import numpy as np
    m = np.array(mat, dtype=np.int64) % p
    rows, cols = m.shape if m.size else (0, 0)
    rank = 0
    for c in range(cols):
        if rank == rows:
            break
        nz = np.nonzero(m[rank:, c])[0]
        if nz.size == 0:
            continue
        piv = rank + nz[0]
        if piv != rank:
            m[[rank, piv]] = m[[piv, rank]]
        inv = pow(int(m[rank, c]), p - 2, p)
        m[rank] = (m[rank] * inv) % p
        others = np.nonzero(m[:, c])[0]
        others = others[others != rank]
        if others.size:
            f = m[others, c].reshape(-1, 1)
            m[others] = (m[others] - (f * m[rank]) % p) % p
        rank += 1
    return rank


def to_mod(q: Fraction, p: int) -> int:
    return (q.numerator % p) * pow(q.denominator % p, p - 2, p) % p


def validate(r, Q, R, vals, nodes, label):
    """Build the full matrix P(x_t) = sum_S c_S(x_t) Pi_S for every node, keep exactly the
    entries (u, w) with a_w(t) != d_u(t) (the nonlocal part N_t, by masking, not by the formula
    of the proof), and compare rank N_t with the prediction of SR-02, Proposition 1. Also report
    the rank of the stacked matrix [N_1; ...; N_Q], the number of rows a single measurement
    matrix serving every node needs before the split into groups."""
    labels = list(itertools.product(itertools.product(range(r), repeat=Q), repeat=2))
    index = {u: i for i, u in enumerate(labels)}
    D = len(labels)

    def swap(u, S):
        a, d = list(u[0]), list(u[1])
        for s in range(Q):
            if (S >> s) & 1:
                a[s], d[s] = d[s], a[s]
        return (tuple(a), tuple(d))

    bad = bad_edges(Q, vals)
    result = {"family": label, "r": r, "Q": Q, "R": R, "D": D, "bad_edges": len(bad), "nodes": []}
    ranks = []
    stacked = {p: [] for p in PRIMES}
    for t in range(Q):
        coeffs = {}
        for S in range(1 << Q):
            c = sum(vals[(e, t)] * (-1) ** popcount(S & e) for e in range(1 << Q)) / (1 << Q)
            if c != 0:
                coeffs[S] = c
        predicted = 0
        for e in range(1 << Q):
            if (e >> t) & 1:
                continue
            if vals[(e, t)] + vals[(e | (1 << t), t)] != 0:
                m = 1
                for s in range(Q):
                    if s != t:
                        m *= r * (r - 1) // 2 if (e >> s) & 1 else r * (r + 1) // 2
                predicted += r * (r - 1) * m
        rk = []
        for p in PRIMES:
            mat = [[0] * D for _ in range(D)]
            for u in labels:
                i = index[u]
                for S, c in coeffs.items():
                    w = swap(u, S)
                    if w[0][t] != u[1][t]:          # nonlocal entry at node t
                        mat[i][index[w]] = (mat[i][index[w]] + to_mod(c, p)) % p
            rk.append(rank_mod_p(mat, p))
            stacked[p].extend(row for row in mat if any(row))
        ranks.append(rk[0])
        result["nodes"].append({"t": t, "rank_mod_p": rk, "predicted": predicted,
                                "match": rk[0] == rk[1] == predicted})
    result["single_matrix_rows"] = [rank_mod_p(stacked[p], p) if stacked[p] else 0 for p in PRIMES]
    result["max_node_rank"] = max(ranks)
    # SR-03 check for every R-subset of nodes, with the best balanced split H of [r]
    h = r // 2
    bound = (h ** R) * ((r - h) ** R) * r ** (2 * (Q - R))
    worst = min(sum(ranks[t] for t in T) for T in itertools.combinations(range(Q), R))
    result["sr03_bound"] = bound
    result["min_sum_over_R_nodes"] = worst
    result["sr03_holds"] = worst >= bound
    return result


def window_counts():
    """Bad edges of the actual window family (best window), against the rule 'good iff both
    weights lie in the window' (nodes x_t = (t+1)/Q, uniform measure)."""
    from cube_polynomial import per_direction, window_bad
    out = []
    for Q in range(2, 7):
        for R in range(2, Q + 1):
            nodes = [Fraction(t + 1, Q) for t in range(Q)]
            fam = min(((len(b), max(per_direction(Q, b))) for b in
                       (bad_edges(Q, window_family_values(Q, R, lo, nodes)) for lo in range(Q - R + 2))))
            rule = min(((len(b), max(per_direction(Q, b))) for b in
                        (window_bad(Q, R, lo) for lo in range(Q - R + 2))))
            out.append({"Q": Q, "R": R, "family_total_max": fam, "rule_total_max": rule})
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path(__file__).parent / "results/matrix_validation.json")
    parser.add_argument("--milp-log", type=Path, default=Path(__file__).parent / "results/cube_polynomial.jsonl")
    args = parser.parse_args()
    out = []
    for (r, Q, R) in [(2, 3, 2), (2, 3, 3), (3, 2, 2), (2, 4, 2), (2, 4, 3), (3, 3, 2)]:
        nodes = [Fraction(t + 1, Q) for t in range(Q)]
        for s0 in range(R):
            out.append(validate(r, Q, R, slab_family_values(Q, R, s0, nodes), nodes, f"slab s0={s0}"))
        p = Fraction(r - 1, 2 * r)
        low = min(max(0, int(Q * p - Fraction(R - 1, 2))), Q - R + 1)   # window around Qp
        out.append(validate(r, Q, R, window_family_values(Q, R, low, nodes), nodes, f"window low={low}"))
    if args.milp_log.exists():
        for line in args.milp_log.read_text().splitlines():
            row = json.loads(line)
            Q, R = row["Q"], row["R"]
            if Q > 4:
                continue
            nodes = [Fraction(t + 1, Q) for t in range(Q)]
            for key in ("realizable_total", "realizable_max_direction"):
                entry = row.get(key, {})
                if not entry.get("exact_good_set_feasible"):
                    continue
                bad = {(v, t) for v, t in entry["bad_edges"]}
                good = [(v, t) for t in range(Q) for v in range(1 << Q)
                        if not (v >> t) & 1 and (v, t) not in bad]
                vals = solve_family_values(Q, R, nodes, good)
                for r in (2,):
                    out.append(validate(r, Q, R, vals, nodes, f"milp {key}"))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps({"validations": out, "window_family_counts": window_counts()},
                                   indent=1) + "\n")
    for res in out:
        print(res["family"], "r", res["r"], "Q", res["Q"], "R", res["R"], "bad", res["bad_edges"],
              "ranks", [n["rank_mod_p"][0] for n in res["nodes"]],
              "match", all(n["match"] for n in res["nodes"]),
              "single-C rows", res["single_matrix_rows"], "max node rank", res["max_node_rank"],
              "SR03", res["sr03_holds"], res["min_sum_over_R_nodes"], ">=", res["sr03_bound"])


if __name__ == "__main__":
    main()
