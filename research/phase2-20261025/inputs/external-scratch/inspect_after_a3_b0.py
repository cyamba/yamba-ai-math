from __future__ import annotations
import helpers as hp
from inspect_complement import a2_reconstruct
from verify_a3_b0_universal import reconstruct_a3_b0, step_one

for n in range(16, 30):
    us = sorted(hp.weighted_columns(w) for w in hp.weighted_partitions(n))
    used_u = {a2_reconstruct(c) for c in hp.cluster_data(n) if c.a <= 2}
    used_u |= {reconstruct_a3_b0(c) for c in hp.cluster_data(n) if c.a == 3 and c.b == 0}
    rem_u = [u for u in us if u not in used_u]
    rem_c = [c for c in hp.cluster_data(n) if not (c.a <= 2 or (c.a == 3 and c.b == 0))]
    assert len(rem_u) == len(rem_c), f"Mismatch at n={n}: {len(rem_u)} vs {len(rem_c)}"
    
    # Filter to primitive cores (d1 = mu[-1] - mu[-2] == 0):
    prev_used = {a2_reconstruct(c) for c in hp.cluster_data(n-1) if c.a <= 2} | {reconstruct_a3_b0(c) for c in hp.cluster_data(n-1) if c.a == 3 and c.b == 0}
    prev_rem = [hp.weighted_columns(w) for w in hp.weighted_partitions(n-1) if hp.weighted_columns(w) not in prev_used]
    prev_step = {step_one(u) for u in prev_rem}
    
    prim_u = [u for u in rem_u if u not in prev_step]
    prim_c = [c for c in rem_c if c.mu[-1] == c.mu[-2]]
    assert len(prim_u) == len(prim_c), f"Prim mismatch at n={n}: {len(prim_u)} vs {len(prim_c)}"
    print(f"=== n={n:2d}: |prim_C| = |prim_U| = {len(prim_c):2d} ===")
    for c, u in zip(prim_c, prim_u):
        diffs = [c.mu[0]] + [c.mu[i] - c.mu[i-1] for i in range(1, c.a - 1)]
        print(f"  a={c.a} b={c.b} diffs={tuple(diffs)} nu={c.nu}  <-->  {u}")
