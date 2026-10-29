from __future__ import annotations
from collections import Counter
import helpers as hp
from inspect_complement import a2_reconstruct

# Let's check for n = 9..26 what ALL the remaining U in U_rem (outside the image of a <= 2) look like
# when we strip trailing 1s!
# Wait: if U is in U_rem, is (U with an extra 1 appended) ALWAYS in U_rem?
# Let's check!

rem_by_n = {}
for n in range(1, 26):
    cs = list(hp.cluster_data(n))
    us = sorted(hp.weighted_columns(w) for w in hp.weighted_partitions(n))
    a2_cs = [c for c in cs if c.a <= 2]
    a2_imgs = {a2_reconstruct(c) for c in a2_cs}
    rem_by_n[n] = [u for u in us if u not in a2_imgs]

# Check if appending 1 to u in rem_by_n[n] stays in rem_by_n[n+1]!
exceptions_append_1 = []
for n in range(9, 25):
    for u in rem_by_n[n]:
        u1 = u + (1,)
        if u1 not in rem_by_n[n + 1]:
            exceptions_append_1.append((n, u, u1))

print(f"Exceptions to (u in U_rem[n] => u+(1,) in U_rem[n+1]) for n=9..24: {len(exceptions_append_1)}")
for ex in exceptions_append_1:
    print("  Exception:", ex)

# And what are the "1-primitive" elements of U_rem (those u in U_rem[n] where u[:-1] is NOT in U_rem[n-1])?
print("\n=== 1-Primitive elements of U_rem (new cores appearing at weight n) vs C(a>=3, mu[-1]==mu[-2]) ===")
for n in range(9, 25):
    prim_u = [u for u in rem_by_n[n] if not (u[-1] == 1 and u[:-1] in rem_by_n[n - 1])]
    prim_c = [c for c in hp.cluster_data(n) if c.a >= 3 and c.mu[-1] == c.mu[-2]]
    print(f"Weight n={n:2d}: |prim_C|={len(prim_c):2d}, |prim_U|={len(prim_u):2d}")
    for c, u in zip(prim_c, prim_u):
        print(f"  C: a={c.a} b={c.b} mu={c.mu} nu={c.nu}  <-->  prim_U: {u}")
