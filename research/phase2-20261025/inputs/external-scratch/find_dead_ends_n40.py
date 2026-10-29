from __future__ import annotations
import sys
sys.path.insert(0, "/Users/christopheryamba/YambaCode/Math/yamba-ai-math-rogers-ramanujan/research/rogers-ramanujan/checks")
from test_primitive_cores import u_rem2

for n in range(16, 40):
    u_next = set(u_rem2[n + 1])
    dead_ends = [u for u in u_rem2[n] if (u + (1,)) not in u_next]
    if dead_ends:
        print(f"n={n:2d} -> {n+1:2d}: {len(dead_ends)} dead ends: {dead_ends}")
