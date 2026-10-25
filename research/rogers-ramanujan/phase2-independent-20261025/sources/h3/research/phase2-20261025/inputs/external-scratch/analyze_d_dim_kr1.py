from __future__ import annotations
from collections import Counter, defaultdict
import helpers as hp
from inspect_complement import a2_reconstruct

# Let's check up to weight n=30:
# 1. What is the exact set of U_rem[n] (all U not in the image of a2_reconstruct)?
# 2. How can we decompose U in U_rem[n] into explicit families indexed by (a, b, mu, nu) for a >= 3?
# Wait: let's also check if there is an even cleaner GLOBAL multi-dimensional bijection U <-> C
# (or if extending a2_reconstruct to a >= 3 is cleaner)!

for n in range(9, 28):
    cs = [c for c in hp.cluster_data(n) if c.a >= 3]
    us = [hp.weighted_columns(w) for w in hp.weighted_partitions(n)]
    a2_imgs = {a2_reconstruct(c) for c in hp.cluster_data(n) if c.a <= 2}
    rem_us = [u for u in us if u not in a2_imgs]
    assert len(cs) == len(rem_us), f"Count mismatch at n={n}: {len(cs)} vs {len(rem_us)}"
print("Verified: |C(a>=3)| == |U_rem| for all n = 9..27!")

# Now let's inspect the exact structure of U_rem!
# Wait: which U in U are used by a2_reconstruct (a <= 2)?
# Let's look at the complement U_rem:
# Why is a column partition u in U NOT in the image of a2_reconstruct?
# Because a2_reconstruct(c) is inverted by a2_decompose(u)!
# Wait: a2_decompose(u) raises OutsideRestrictedDomain on u if and only if u is in U_rem!
# Let's list the EXACT disjoint families of U that raise OutsideRestrictedDomain in a2_decompose!
