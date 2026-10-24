from collections import Counter, defaultdict
import helpers as hp

# Let's inspect the 4D decomposition of B (parts congruent to 1, 3, 6, 8 mod 9)
# Wait: every partition in B consists of 4 independent partitions:
# - B_1: parts = 9k + 1 (k >= 0)
# - B_3: parts = 9k + 3 (k >= 0)
# - B_6: parts = 9k + 6 (k >= 0)
# - B_8: parts = 9k + 8 (k >= 0)
# Notice that B_3 and B_6 together are ALL multiples of 3 not divisible by 9:
# 3 * (parts = 3k + 1 or 3k + 2)!
# By Glaisher's theorem, 3 * (parts != 0 mod 3) is in exact weight-preserving bijection with:
# A_3 = partitions into multiples of 3 with multiplicity <= 2!
# Now what about B_1 and B_8 (parts = 9k + 1 and 9k + 8)??
# Wait: what is a partition into parts 9k + 1 and 9k + 8?
# Or what if we group B or U differently?
# Let's check the generating function of (B_1, B_8) vs (a, b, mu, nu)!

# Wait: in C = (a, b, mu, nu), the generating function at fixed (a, b) is:
# q^{a^2 + 3ab + 3b^2} / ((q; q)_a (q^3; q^3)_b).
# Let's check if there is a direct multi-dimensional decomposition of U into (a, b, mu, nu)!
# Wait: in U = (u_1, ..., u_l), each column u_k = F(h_k) is in {1, 3, 6, 8, 9, 10, 12, 15, 17, 18, ...}.
# Let's look at ALL U of weight N = 0..15 and see which U are NOT covered by RR003's a=0,1 rule (`rr003_columns.py`),
# or what a clean, UNIFORM core U_{a,b} for ALL (a, b) looks like!

print("=== CHECKING POSSIBLE CORES U_{a,b} OF WEIGHT Q(a,b) = a^2 + 3ab + 3b^2 ===")
for a in range(5):
    for b in range(4):
        q = a*a + 3*a*b + 3*b*b
        if q <= 25:
            us = [hp.weighted_columns(w) for w in hp.weighted_partitions(q)]
            print(f"(a={a}, b={b}) -> Q={q:2d} (#U={len(us)})")
            for u in sorted(us)[:8]:
                h = tuple(hp.inverse_prefix(x) for x in u)
                print(f"    U={str(u):25s} H={h}")
