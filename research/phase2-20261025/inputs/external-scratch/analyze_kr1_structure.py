from collections import Counter, defaultdict
import helpers as hp

# Let's inspect C=(a,b,mu,nu) and U and B and A for N=0..20
# Wait: in B (parts 1, 3, 6, 8 mod 9), every part is either:
# - 3, 6 mod 9 (multiples of 3 not divisible by 9)
# - 1, 8 mod 9 (non-multiples of 3)
#Wait: what is the generating function of parts 3, 6 mod 9?
# prod_{k>=0} 1/((1 - q^{9k+3})(1 - q^{9k+6})) = prod_{m>=1} (1 + q^{3m} + q^{6m})!
# And what is the generating function of parts 1, 8 mod 9?
# prod_{k>=0} 1/((1 - q^{9k+1})(1 - q^{9k+8}))!
# WAIT A SECOND!
# Look at prod_{k>=0} 1/((1 - q^{9k+1})(1 - q^{9k+8}))!
# By Euler's / Schur's / Jacobi's or Bressoud's theorem, or in C = (a, b, mu, nu):
# Let's check what C = (a, b, mu, nu) looks like when we group by (a, b)!

print("Weight | #B | #C by (a,b)")
for n in range(16):
    cs = list(hp.cluster_data(n))
    by_ab = Counter((c.a, c.b) for c in cs)
    print(f"N={n:2d} | {len(cs):2d} | {dict(sorted(by_ab.items()))}")
