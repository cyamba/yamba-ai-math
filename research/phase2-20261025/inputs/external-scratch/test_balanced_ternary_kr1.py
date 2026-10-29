from __future__ import annotations
from collections import Counter, defaultdict
import helpers as hp

# Let's inspect the balanced ternary decomposition of U in \mathcal{U} and A in \mathcal{A}!
# For any column weight u in U:
# u = 3 * p + delta, where p = (u + 1) // 3 and delta = u - 3 * p in {-1, 0, +1}.
# Wait: let's check for all allowed column weights u:
for h in range(1, 16):
    u = hp.prefix_weight(h)
    p = (u + 1) // 3
    delta = u - 3 * p
    print(f"h={h:2d}: u={u:2d} = 3*{p:2d} + ({delta:+d})  [p mod 3 = {p % 3}]")
