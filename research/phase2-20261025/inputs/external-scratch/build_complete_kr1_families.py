from __future__ import annotations
from collections import Counter
import helpers as hp
from inspect_complement import a2_reconstruct
from inspect_a3_a4_exact import step_one

# Let's see how the primitive cores `prim_C` (where a >= 3 and mu[-1] == mu[-2]) map to `prim_U`!
# Look at the output of `inspect_a3_a4_exact.py` for n = 9..26:
# In `prim_C`, let's look at the coordinates of C:
# For a = 3, b = 0:
#   mu = (d3, d3 + d2, d3 + d2 + d1), where d1 = mu[2] - mu[1] is handled by `step_one`^d1!
#   So a primitive C with a = 3, b = 0 is indexed by (d3, d2) in N^2, with weight:
#     W(d3, d2) = 9 + 3*d3 + 2*d2.
#   Now write d2 = 3*q2 + r2 (where r2 in {0, 1, 2}), OR look at how (d3, d2) maps to `prim_U`:
#   Wait: notice that in W(d3, d2) = 9 + 3*d3 + 2*d2:
#   - When d3 = 0: weight is 9 + 2*d2 (which is 9, 11, 13, 15, 17, 19, 21, 23, 25, ...):
#     - d2 = 0 (wt 9):  (6, 3)
#     - d2 = 1 (wt 11): (8, 3)
#     - d2 = 2 (wt 13): (10, 3)
#     - d2 = 3 (wt 15): (6, 6, 3)
#     - d2 = 4 (wt 17): (8, 6, 3)
#     - d2 = 5 (wt 19): (8, 8, 3)
#     - d2 = 6 (wt 21): (6, 6, 6, 3)
#     - d2 = 7 (wt 23): (8, 6, 3, 3, 3)
#     - d2 = 8 (wt 25): (8, 8, 6, 3)
#   WAIT A SECOND!
#   Look at why (6^q, 3^r) has weight 9 + 3*m (m >= 0),
#   (8, 6^q, 3^r) has weight 11 + 3*m (m >= 0),
#   (10, 3^r) / (8, 8, 6^q, 3^r) has weight 13 + 3*m or 16 + 3*m,
#   (9, 6^q) / (9, 8, ...) / (9, 9, ...) has weight 15 + 3*m or 17 + 3*m or 19 + 3*m!
#
#   HOLD ON!
#   Notice that in ANY family where we add copies of 3 (or 6 = 2*3), each step adds +3 to the weight!
#   And in C = (3, 0, mu, ()), increasing d3 = mu[0] by +1 ALSO adds +3 to the weight!
#   Wait: why did `inspect_a3_a4_exact.py` list multiple (d3, d2) at the same weight n?
#   Because 3*d3 + 2*d2 = n - 9 has solutions (d3, d2) where d2 increases by 3 and d3 decreases by 2!
#   Specifically, every integer n - 9 writes as 3*d3 + 2*d2 where:
#   - d2 = 0, 1, 2 gives a UNIQUE congruence class of (n - 9) mod 3 (for d3 = 0, 1, 2, ...),
#   - d2 = 3, 4, 5 gives a SECOND family at weight 15 + 3*d3, 17 + 3*d3, 19 + 3*d3,
#   - d2 = 6, 7, 8 gives a THIRD family at weight 21 + 3*d3, 23 + 3*d3, 25 + 3*d3!
#
#   STOP EVERYTHING AND READ THAT AGAIN!!
#   Write d2 in base 3:
#     d2 = 3 * k + r2,   where k >= 0 and r2 in {0, 1, 2}!
#   Then:
#     W(d3, d2) = 9 + 3*d3 + 2*(3*k + r2) = (9 + 6*k + 2*r2) + 3*d3!!
#   WAIT A SECOND!
#   Read that formula ten times:
#     W(d3, 3*k + r2) = (9 + 6*k + 2*r2) + 3 * d3!!
#   For EACH fixed pair (k, r2) (with k >= 0, r2 in {0, 1, 2}):
#   As d3 = 0, 1, 2, 3, ... varies, the weight increases in steps of +3:
#     base_weight(k, r2) + 3 * d3,
#   which is a SINGLE 3-step chain (adding 3s / turning 3 -> 6) starting from a base carrier for (k, r2)!!

# Let's check this in Python right now!
for k in range(4):
    for r2 in range(3):
        d2 = 3 * k + r2
        base_wt = 9 + 2 * d2
        print(f"(k={k}, r2={r2}) -> d2={d2:2d}, base weight (at d3=0) = {base_wt:2d}, weights = {base_wt}, {base_wt+3}, {base_wt+6}, ...")
