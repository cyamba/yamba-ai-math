from collections import Counter
import helpers as hp

# Let's check the uncovered U and C in KR1 for N <= 16
# First let's see all U and C for N = 0..12
print("=== KR1: ALL U (with decoded heights H and conjugate W) AND ALL C FOR N <= 10 ===")
for n in range(11):
    ws = list(hp.weighted_partitions(n))
    us = [hp.weighted_columns(w) for w in ws]
    cs = list(hp.cluster_data(n))
    as_ = list(hp.gap_partitions(n))
    print(f"\n--- Weight N = {n} (count = {len(us)}) ---")
    for w, u in sorted(zip(ws, us), key=lambda x: x[1]):
        h = tuple(hp.inverse_prefix(c) for c in u)
        print(f"  U={str(u):20s} H={str(h):18s} W={w}")
    for c in sorted(cs):
        print(f"  C=(a={c.a}, b={c.b}, mu={c.mu}, nu={c.nu})")
