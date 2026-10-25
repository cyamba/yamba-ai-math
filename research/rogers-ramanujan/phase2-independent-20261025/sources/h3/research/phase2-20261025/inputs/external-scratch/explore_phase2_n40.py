from __future__ import annotations
import sys
from pathlib import Path
from collections import Counter

sys.path.insert(0, "/Users/christopheryamba/YambaCode/Math/yamba-ai-math-rogers-ramanujan/research/rogers-ramanujan/checks")
import kr1
import rr003_a2
import rr004_multidim_cones as rr4

# Check how many states exist in C_{a >= 3} and U_{rem} up to N = 40!
sector_counts = Counter()
total_c_ge3 = 0
for n in range(9, 41):
    cs = [c for c in kr1.cluster_data(n) if c.a >= 3]
    for c in cs:
        sector_counts[(c.a, c.b)] += 1
        total_c_ge3 += 1

print("Sector counts for a >= 3 in 9 <= N <= 40:")
for k, v in sorted(sector_counts.items()):
    print(f"  (a={k[0]}, b={k[1]}): {v} states")
print(f"Total a >= 3 states for N <= 40: {total_c_ge3}")
