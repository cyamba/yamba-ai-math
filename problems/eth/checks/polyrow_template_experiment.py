"""ETH-B03: general polynomial-row template vs. the M_0 form (tiny instances).

Unknowns: rows P_u(T) = e_u + sum_{k=1}^{R-1} T^k C_{u,k} in Q^D (degree <= R-1, P_u(0) = e_u),
a c-dimensional space Rs = span(B), and for each node t in 1..Q a vector rho_{u,t} = B z_{u,t}
with P_u(t) = rho_{u,t} on the forbidden coordinates N_{t,u} = {w : a_w(t) != d_u(t)}.
(The M_0 form is the special case P_u(T) = ((I-M_0)e_u) + sum_w M_0[u,w] phi_{u,w}(T) e_w.)
We minimise the masked residual by alternating least squares and report the smallest c reaching ~0.
"""
import itertools, sys
import numpy as np

def setup(Q, r):
    labels = list(itertools.product(range(r), repeat=2 * Q))
    a = np.array([l[:Q] for l in labels]); d = np.array([l[Q:] for l in labels])
    # forb[t][u, w] = True if a_w(t) != d_u(t)
    forb = np.array([d[:, None, t] != a[None, :, t] for t in range(Q)])
    return len(labels), forb

def als(Q, R, r, c, iters=400, seed=0):
    D, forb = setup(Q, r)
    rng = np.random.default_rng(seed)
    nodes = np.arange(1, Q + 1, dtype=float)
    V = np.vander(nodes, R, increasing=True)          # Q x R, columns t^0..t^{R-1}
    Cf = rng.standard_normal((D, R - 1, D)) * 0.3     # C_{u,k}[w]
    B = rng.standard_normal((D, c))
    def P_at():
        # P[u, t, w] = delta_uw + sum_k t^k C[u,k,w]
        base = np.zeros((D, Q, D)); base[np.arange(D), :, np.arange(D)] = 1.0
        return base + np.einsum('tk,ukw->utw', V[:, 1:], Cf)
    for it in range(iters):
        P = P_at()
        # z step
        Z = np.zeros((D, Q, c))
        for u in range(D):
            for t in range(Q):
                m = forb[t, u]
                Z[u, t] = np.linalg.lstsq(B[m], P[u, t, m], rcond=None)[0]
        # B step (rows decouple)
        for w in range(D):
            mask = forb[:, :, w].T                      # (u, t) where w forbidden
            zz = Z[mask]; yy = P[:, :, w][mask]
            if len(zz): B[w] = np.linalg.lstsq(zz, yy, rcond=None)[0]
        # P step (u, w decouple): fit C[u,:,w] to targets on forbidden nodes, free nodes unconstrained
        tgt = np.einsum('wc,utc->utw', B, Z)
        for u in range(D):
            for w in range(D):
                ts = np.where(forb[:, u, w])[0]
                if len(ts) == 0: continue
                y = tgt[u, ts, w] - (1.0 if u == w else 0.0)
                Cf[u, :, w] = np.linalg.lstsq(V[ts][:, 1:], y, rcond=None)[0]
        if it % 100 == 99:
            P = P_at()
            res = sum(np.sum((P[u, t, forb[t, u]] - (B @ Z[u, t])[forb[t, u]]) ** 2) for u in range(D) for t in range(Q))
            sc = np.linalg.svd(B, compute_uv=False)
    P = P_at()
    res = sum(np.sum((P[u, t, forb[t, u]] - (B @ Z[u, t])[forb[t, u]]) ** 2) for u in range(D) for t in range(Q))
    return res

if __name__ == "__main__":
    Q, R, r = 3, 2, 2
    for c in [9, 8, 6, 4, 2]:
        best = min(als(Q, R, r, c, iters=300, seed=s) for s in range(3))
        print(f"Q={Q} R={R} r={r}: c={c}  best masked residual {best:.2e}", flush=True)
