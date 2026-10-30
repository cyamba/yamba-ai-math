"""Certified lower bounds for min rank(I - M), M supported on the routing pattern P.

If T is a set of indices with (u,u) not in P for u in T, and the digraph
{u -> w : (u,w) in P, u != w} restricted to T is acyclic, then (I - M)[T,T] is
triangular (after ordering T topologically) with unit diagonal, so
rank(I - M) >= |T| for EVERY M supported on P.  We maximise |T| with CP-SAT.
"""
import itertools, sys
import numpy as np
from ortools.sat.python import cp_model
from routing_minrank_experiment import pattern, commutative_opt

def max_triangular(P, time_limit=600):
    D = P.shape[0]
    V = [u for u in range(D) if not P[u, u]]
    m = cp_model.CpModel()
    x = {u: m.NewBoolVar(f"x{u}") for u in V}
    p = {u: m.NewIntVar(0, len(V), f"p{u}") for u in V}
    for u in V:
        for w in V:
            if u != w and P[u, w]:
                # u -> w edge: if both chosen then p_u < p_w
                m.Add(p[u] < p[w]).OnlyEnforceIf([x[u], x[w]])
    m.Maximize(sum(x.values()))
    s = cp_model.CpSolver(); s.parameters.max_time_in_seconds = time_limit; s.parameters.num_workers = 2
    st = s.Solve(m)
    return int(s.ObjectiveValue()), int(s.BestObjectiveBound()), s.StatusName(st)

if __name__ == "__main__":
    for (Q, R, r) in [(2, 2, 2), (3, 2, 2), (3, 3, 2), (2, 2, 3)]:
        c_comm, D = commutative_opt(Q, R, r)
        P, _ = pattern(Q, R, r)
        lb, ub, st = max_triangular(P)
        print(f"Q={Q} R={R} r={r} D={D}: commutative={c_comm}  certified lower bound={lb} "
              f"(triangular-bound ceiling {ub}, {st})", flush=True)
