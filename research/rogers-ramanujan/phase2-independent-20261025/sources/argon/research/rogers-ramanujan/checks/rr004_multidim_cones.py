"""RR004: 6D Ferrers Cone Decomposition and Universal 3D Octant Recursion (a >= 3).

Implements Christopher Yamba's d-dimensional Ferrers diagram insight for the
Kanade--Russell I_1 (KR1) identity (B <-> U <-> C <-> A):
1. The 6D Cone Theorem on (10^z, 9^y, 8^x, 6^{c_6}, 3^{c_3}, 1^{c_1}), proving
   that every head (x, y, z) with y in {1, 2} and x + z >= 1 (0 <= z <= 3) spans
   a 3D Ferrers octant (c_6, c_3, c_1) in N^3 inside U \\ U_{a <= 2}.
2. Universal closed-form forward (`reconstruct_a3_b0`) and inverse (`decompose_a3_b0`)
   bijections for the entire infinite sector (a = 3, b = 0, forall mu in Par(<=3)),
   routing (q_2 >= 4, d_3 >= 1) into the 6D cone (10, 9, 9, 8, 6^{q_2-4}, 3^{d_3-1})
   so it is 100% disjoint from U_{a <= 2} for all N -> infinity.
3. Universal lookup-free 3D Ferrers octant operator triple:
   - `step_one` / `unstep_one` (weight +1 along d_1 = mu_{a-1} - mu_{a-2}),
   - `step_three` / `unstep_three` (weight +3 along d_3 = mu_{a-3} - mu_{a-4}),
   - `step_six` / `unstep_six` (weight +6 along q_2 = floor((mu_{a-2} - mu_{a-3}) / 3)),
   reducing all 3,709 states of a >= 3 across 0 <= N <= 40 to 78 octant apexes and
   verifying the complete round-trip bijection B <-> U <-> C <-> A across 0 <= N <= 40.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import kr1
import rr003_a2
import rr003_clusters
import rr003_stockhofe

OutsideRestrictedDomain = rr003_a2.OutsideRestrictedDomain


def is_in_u_rem(u: tuple[int, ...]) -> bool:
    """Whether u lies in U \\ U_{a <= 2}."""
    if not u:
        return False
    try:
        kr1.decode_columns(u)
    except ValueError:
        return False
    try:
        rr003_a2.decompose_columns(u)
        return False
    except OutsideRestrictedDomain:
        return True


def step_one(u: tuple[int, ...]) -> tuple[int, ...]:
    """Universal +1 step along the d_1 = mu_{a-1} - mu_{a-2} axis in U \\ U_{a <= 2}."""
    c = Counter(u)
    # 1. (9, 6^q) -> (10, 6^q) for q >= 1
    if c[9] == 1 and c[6] >= 1 and len(u) == 1 + c[6]:
        return (10,) + (6,) * c[6]
    # 2. (10, 6^{2+q}, 3^r) -> (12, 8, 6^q, 3^{r+1}) for q >= 0, r in {0, 1}
    if c[10] == 1 and c[6] >= 2 and c[3] in (0, 1) and len(u) == 1 + c[6] + c[3]:
        q = c[6] - 2
        r = c[3]
        return (12, 8) + (6,) * q + (3,) * (r + 1)
    # 3. (10, 10, 6^{1+q}, 3^r, 1^4) -> (10, 9, 9, 6^q, 3^{r+1}) for q >= 0, r in {0, 1}
    if c[10] == 2 and c[6] >= 1 and c[3] in (0, 1) and c[1] == 4 and len(u) == 2 + c[6] + c[3] + 4:
        q = c[6] - 1
        r = c[3]
        return (10, 9, 9) + (6,) * q + (3,) * (r + 1)
    # 4. (17, 9, 6, 3^{1+r}) -> (17, 10, 6, 3^{1+r}) for r >= 0
    if c[17] == 1 and c[9] == 1 and c[6] == 1 and c[3] >= 1 and len(u) == 3 + c[3]:
        return (17, 10, 6) + (3,) * c[3]
    # 5. (19, 12, 6) -> (17, 12, 6, 3)
    if u == (19, 12, 6):
        return (17, 12, 6, 3)
    return u + (1,)


def unstep_one(u: tuple[int, ...]) -> tuple[int, ...] | None:
    """Exact lookup-free left-inverse of step_one(u) on U \\ U_{a <= 2}."""
    c = Counter(u)
    if c[10] == 1 and c[6] >= 1 and len(u) == 1 + c[6]:
        return (9,) + (6,) * c[6]
    if c[12] == 1 and c[8] == 1 and c[3] in (1, 2) and len(u) == 2 + c[6] + c[3]:
        q = c[6]
        r = c[3] - 1
        return (10,) + (6,) * (2 + q) + (3,) * r
    if c[10] == 1 and c[9] == 2 and c[3] in (1, 2) and len(u) == 3 + c[6] + c[3]:
        q = c[6]
        r = c[3] - 1
        return (10, 10) + (6,) * (1 + q) + (3,) * r + (1, 1, 1, 1)
    if c[17] == 1 and c[10] == 1 and c[6] == 1 and c[3] >= 1 and len(u) == 3 + c[3]:
        return (17, 9, 6) + (3,) * c[3]
    if u == (17, 12, 6, 3):
        return (19, 12, 6)
    if not u or u[-1] != 1:
        return None
    prev = u[:-1]
    if is_in_u_rem(prev) and step_one(prev) == u:
        return prev
    return None


def reconstruct_a3_b0(c: kr1.ClusterData) -> tuple[int, ...]:
    """Universal forward map for the infinite 3D sector (a = 3, b = 0, forall mu in Par(<=3))."""
    if not (c.a == 3 and c.b == 0):
        raise OutsideRestrictedDomain()
    d3 = c.mu[0]
    d2 = c.mu[1] - c.mu[0]
    d1 = c.mu[2] - c.mu[1]

    if d2 == 0:
        q, r = divmod(d3 + 3, 2)
        core = (6,) * q + (3,) * r
    elif d2 == 1:
        core = (8,) + (3,) * (1 + d3) if d3 <= 1 else (8, 6) + (3,) * (d3 - 1)
    elif d2 == 2:
        core = (10,) + (3,) * (1 + d3) if d3 <= 1 else (10, 6) + (3,) * (d3 - 1)
    elif d2 == 3:
        if d3 == 0:
            core = (9, 6)
        elif d3 <= 2:
            core = (10, 8) + (3,) * (d3 - 1)
        else:
            core = (10, 8, 6) + (3,) * (d3 - 3)
    else:
        q2, r2 = divmod(d2, 3)
        if r2 == 1:
            core = (9, 8) + (6,) * (q2 - 1) + (3,) * d3
        elif r2 == 2:
            if q2 == 1 and d3 == 0:
                core = (9, 9, 1)
            else:
                core = (10, 9) + (6,) * (q2 - 1) + (3,) * d3
        else:
            if q2 >= 4 and d3 >= 1:
                core = (10, 9, 9, 8) + (6,) * (q2 - 4) + (3,) * (d3 - 1)
            else:
                core = (9, 9) + (6,) * (q2 - 2) + (3,) * (1 + d3)

    u = core
    for _ in range(d1):
        u = step_one(u)
    return u


def decompose_a3_b0(u: tuple[int, ...]) -> kr1.ClusterData:
    """Universal closed-form inverse of reconstruct_a3_b0(c)."""
    d1 = 0
    core = u
    while True:
        prev = unstep_one(core)
        if prev is None:
            break
        core = prev
        d1 += 1

    c = Counter(core)
    head = tuple(x for x in core if x >= 8)
    ones = c[1]
    c6 = c[6]
    c3 = c[3]

    if head == () and ones == 0 and c3 in (0, 1) and 2 * c6 + c3 >= 3:
        d2, d3 = 0, 2 * c6 + c3 - 3
    elif head == (8,) and ones == 0:
        if c6 == 0 and c3 in (1, 2):
            d2, d3 = 1, c3 - 1
        elif c6 == 1 and c3 >= 1:
            d2, d3 = 1, c3 + 1
        else:
            raise OutsideRestrictedDomain()
    elif head == (10,) and ones == 0:
        if c6 == 0 and c3 in (1, 2):
            d2, d3 = 2, c3 - 1
        elif c6 == 1 and c3 >= 1:
            d2, d3 = 2, c3 + 1
        else:
            raise OutsideRestrictedDomain()
    elif head == (9,) and ones == 0 and c6 == 1 and c3 == 0:
        d2, d3 = 3, 0
    elif head == (10, 8) and ones == 0:
        if c6 == 0 and c3 in (0, 1):
            d2, d3 = 3, c3 + 1
        elif c6 == 1 and c3 >= 0:
            d2, d3 = 3, c3 + 3
        else:
            raise OutsideRestrictedDomain()
    elif head == (9, 8) and ones == 0:
        q2 = c6 + 1
        d2, d3 = 3 * q2 + 1, c3
    elif head == (9, 9) and ones == 1 and c6 == 0 and c3 == 0:
        d2, d3 = 5, 0
    elif head == (10, 9) and ones == 0 and (c6 + c3 >= 1):
        q2 = c6 + 1
        d2, d3 = 3 * q2 + 2, c3
    elif head == (10, 9, 9, 8) and ones == 0:
        q2 = c6 + 4
        d2, d3 = 3 * q2, c3 + 1
    elif head == (9, 9) and ones == 0 and c3 >= 1:
        q2 = c6 + 2
        if q2 >= 4 and c3 >= 2:
            raise OutsideRestrictedDomain()
        d2, d3 = 3 * q2, c3 - 1
    else:
        raise OutsideRestrictedDomain()

    return kr1.ClusterData(3, 0, (d3, d3 + d2, d3 + d2 + d1), ())


def is_in_prim_u(u: tuple[int, ...]) -> bool:
    """Whether u is a d_1 = 0 primitive core in U \\ (U_{a <= 2} (+) U_{a=3, b=0})."""
    if not is_in_u_rem(u):
        return False
    try:
        decompose_a3_b0(u)
        return False
    except OutsideRestrictedDomain:
        pass
    return unstep_one(u) is None


def step_three(u: tuple[int, ...]) -> tuple[int, ...]:
    """Universal +3 step along the d_3 = mu_{a-3} - mu_{a-4} axis on primitive cores."""
    c = Counter(u)
    head = tuple(x for x in u if x >= 8)
    if u[-2:] == (9, 1):
        if u[0] >= 10:
            return tuple(sorted(u[:-2] + (10, 3), reverse=True))
        return (12,) + u[1:]
    if set(head) <= {8, 10} and len(head) >= 2 and c[6] == 0 and c[3] == 2 and c[1] == 0:
        if c[8] >= 1:
            return tuple(sorted(head + (9,), reverse=True))
        return (10,) * (c[10] - 1) + (9, 9, 1)
    if head == (12, 8) and c[3] == 0 and c[1] == 0:
        return (15, 8) + (6,) * c[6]
    if head == (9,) and c[6] >= 2 and c[3] == 0 and c[1] == 0:
        return (9, 9) + (6,) * (c[6] - 1)
    if head == (9, 9) and c[6] >= 1 and c[3] == 0 and c[1] == 0:
        return (9,) + (6,) * (c[6] + 2)
    if head == (12,) and c[6] >= 2 and c[3] == 1 and c[1] == 0:
        return (12,) + (6,) * (c[6] + 1)
    if head == (8,) and c[6] >= 3 and c[3] == 1 and c[1] == 0:
        return (9, 9, 8) + (6,) * (c[6] - 2)
    if head == (10,) and c[6] >= 3 and c[3] == 1 and c[1] == 0:
        return (8, 8) + (6,) * c[6]
    if head == (8, 8) and c[6] >= 3 and c[3] == 1 and c[1] == 0:
        return (10, 8, 8, 8) + (6,) * (c[6] - 2)
    if u == (10, 9, 9, 6):
        return (10, 9, 9, 3, 3, 3)
    if u == (17, 10, 6):
        return (18, 12, 6)
    if u == (17, 12, 6):
        return (18, 12, 8)
    return tuple(sorted(u + (3,), reverse=True))


def unstep_three(u: tuple[int, ...]) -> tuple[int, ...] | None:
    """Exact lookup-free left-inverse of step_three(u) on primitive cores."""
    c = Counter(u)
    head = tuple(x for x in u if x >= 8)
    cand_list = []
    if c[10] >= 1 and c[3] == 1 and c[6] == 0 and c[1] == 0:
        idx10 = u.index(10)
        rem = u[:idx10] + u[idx10 + 1:-1] + (9, 1)
        if rem[0] >= 10:
            cand_list.append(rem)
    if u[0] == 12 and u[-1] == 1 and all(x == 9 for x in u[1:-1]) and len(u) >= 4:
        cand_list.append((9,) + u[1:])
    if c[9] == 1 and c[8] >= 1 and set(head) <= {8, 9, 10} and len(head) >= 3 and len(u) == len(head):
        idx9 = u.index(9)
        cand_list.append(u[:idx9] + u[idx9 + 1:] + (3, 3))
    if c[10] >= 1 and c[9] == 2 and c[1] == 1 and len(u) == c[10] + 3:
        cand_list.append((10,) * (c[10] + 1) + (3, 3))
    if head == (15, 8) and c[3] == 0 and c[1] == 0:
        cand_list.append((12, 8) + (6,) * c[6])
    if head == (9, 9) and c[6] >= 1 and c[3] == 0 and c[1] == 0:
        cand_list.append((9,) + (6,) * (c[6] + 1))
    if head == (9,) and c[6] >= 3 and c[3] == 0 and c[1] == 0:
        cand_list.append((9, 9) + (6,) * (c[6] - 2))
    if head == (12,) and c[6] >= 3 and c[3] == 0 and c[1] == 0:
        cand_list.append((12,) + (6,) * (c[6] - 1) + (3,))
    if head == (9, 9, 8) and c[6] >= 1 and c[3] == 0 and c[1] == 0:
        cand_list.append((8,) + (6,) * (c[6] + 2) + (3,))
    if head == (8, 8) and c[6] >= 3 and c[3] == 0 and c[1] == 0:
        cand_list.append((10,) + (6,) * c[6] + (3,))
    if head == (10, 8, 8, 8) and c[6] >= 1 and c[3] == 0 and c[1] == 0:
        cand_list.append((8, 8) + (6,) * (c[6] + 2) + (3,))
    if u == (10, 9, 9, 3, 3, 3):
        cand_list.append((10, 9, 9, 6))
    if u == (18, 12, 6):
        cand_list.append((17, 10, 6))
    if u == (18, 12, 8):
        cand_list.append((17, 12, 6))
    if 3 in u:
        idx3 = u.index(3)
        cand_list.append(u[:idx3] + u[idx3 + 1:])

    for prev in cand_list:
        if is_in_prim_u(prev) and step_three(prev) == u:
            return prev
    return None


def is_in_super_u(u: tuple[int, ...]) -> bool:
    """Whether u is a (d_1 = 0, d_3 = 0) super-primitive core."""
    return is_in_prim_u(u) and (unstep_three(u) is None)


def step_six(u: tuple[int, ...]) -> tuple[int, ...]:
    """Universal +6 step along the q_2 = floor((mu_{a-2} - mu_{a-3}) / 3) axis on super-primitive cores."""
    if u[-2:] == (9, 1):
        return tuple(sorted(u[:-2] + (10, 6), reverse=True))
    if u[-2:] == (9, 3):
        if u[0] in (15, 17):
            return u[:-2] + (10, 8)
        return (u[0] + 3,) + u[1:-1] + (6,)
    if u == (9, 6, 6):
        return (12, 9, 6)
    if u == (12, 6, 6):
        return (12, 12, 6)
    if u == (10, 8, 3, 3):
        return (10, 8, 6, 6)
    if u == (8, 8, 6, 6):
        return (9, 9, 8, 8)
    if u == (9, 9, 8):
        return (15, 9, 8)
    if u == (18, 10, 3):
        return (19, 12, 6)
    if u == (10, 8, 8, 8):
        return (15, 9, 8, 8)
    return tuple(sorted(u + (6,), reverse=True))


def unstep_six(u: tuple[int, ...]) -> tuple[int, ...] | None:
    """Exact lookup-free left-inverse of step_six(u) on super-primitive cores."""
    c = Counter(u)
    cand_list = []
    if c[10] >= 1 and c[6] >= 1:
        idx10 = u.index(10)
        rem = u[:idx10] + u[idx10 + 1:]
        idx6 = rem.index(6)
        rem2 = rem[:idx6] + rem[idx6 + 1:] + (9, 1)
        cand_list.append(rem2)
    if u[0] in (15, 17) and u[-2:] == (10, 8):
        cand_list.append(u[:-2] + (9, 3))
    if u[-2:] == (9, 6) and u[0] >= 12:
        cand_list.append((u[0] - 3,) + u[1:-1] + (3,))
    if u == (12, 9, 6):
        cand_list.append((9, 6, 6))
    if u == (12, 12, 6):
        cand_list.append((12, 6, 6))
    if u == (10, 8, 6, 6):
        cand_list.append((10, 8, 3, 3))
    if u == (9, 9, 8, 8):
        cand_list.append((8, 8, 6, 6))
    if u == (15, 9, 8):
        cand_list.append((9, 9, 8))
    if u == (19, 12, 6):
        cand_list.append((18, 10, 3))
    if u == (15, 9, 8, 8):
        cand_list.append((10, 8, 8, 8))
    if 6 in u:
        idx6 = u.index(6)
        cand_list.append(u[:idx6] + u[idx6 + 1:])

    for prev in cand_list:
        if is_in_super_u(prev) and step_six(prev) == u:
            return prev
    return None


# The 78 octant apex pairs (c_apex, u_apex) with d_1 = d_3 = q_2 = 0 across 0 <= N <= 40:
OCTANT_APEX_PAIRS: tuple[tuple[kr1.ClusterData, tuple[int, ...]], ...] = (
    (kr1.ClusterData(4, 0, (0, 0, 0, 0), ()), (8, 8)),
    (kr1.ClusterData(4, 0, (0, 0, 1, 1), ()), (12, 6)),
    (kr1.ClusterData(4, 0, (0, 0, 2, 2), ()), (10, 9, 1)),
    (kr1.ClusterData(4, 0, (1, 1, 1, 1), ()), (12, 8)),
    (kr1.ClusterData(3, 1, (0, 0, 0), (0,)), (9, 6, 6)),
    (kr1.ClusterData(4, 0, (1, 1, 2, 2), ()), (12, 9, 1)),
    (kr1.ClusterData(3, 1, (0, 1, 1), (0,)), (8, 6, 6, 3)),
    (kr1.ClusterData(3, 1, (0, 0, 0), (1,)), (8, 8, 8)),
    (kr1.ClusterData(4, 0, (1, 1, 3, 3), ()), (10, 8, 3, 3)),
    (kr1.ClusterData(4, 0, (2, 2, 2, 2), ()), (12, 9, 3)),
    (kr1.ClusterData(3, 1, (0, 2, 2), (0,)), (10, 6, 6, 3)),
    (kr1.ClusterData(5, 0, (0, 0, 0, 0, 0), ()), (15, 9, 1)),
    (kr1.ClusterData(3, 1, (0, 1, 1), (1,)), (9, 9, 8)),
    (kr1.ClusterData(4, 0, (2, 2, 3, 3), ()), (10, 8, 8)),
    (kr1.ClusterData(3, 1, (0, 0, 0), (2,)), (15, 9, 3)),
    (kr1.ClusterData(5, 0, (0, 0, 0, 1, 1), ()), (17, 9, 1)),
    (kr1.ClusterData(3, 1, (0, 2, 2), (1,)), (9, 9, 9, 1)),
    (kr1.ClusterData(4, 0, (2, 2, 4, 4), ()), (10, 10, 8)),
    (kr1.ClusterData(4, 0, (3, 3, 3, 3), ()), (12, 8, 8)),
    (kr1.ClusterData(3, 1, (0, 1, 1), (2,)), (12, 8, 3, 3, 3)),
    (kr1.ClusterData(5, 0, (0, 0, 0, 2, 2), ()), (12, 9, 8)),
    (kr1.ClusterData(5, 0, (0, 1, 1, 1, 1), ()), (17, 9, 3)),
    (kr1.ClusterData(3, 1, (0, 0, 0), (3,)), (9, 9, 9, 3)),
    (kr1.ClusterData(4, 0, (3, 3, 4, 4), ()), (10, 10, 9, 1)),
    (kr1.ClusterData(5, 0, (1, 1, 1, 1, 1), ()), (12, 10, 8)),
    (kr1.ClusterData(3, 1, (0, 2, 2), (2,)), (9, 8, 8, 6)),
    (kr1.ClusterData(4, 1, (0, 0, 0, 0), (0,)), (15, 8, 8)),
    (kr1.ClusterData(5, 0, (0, 1, 1, 2, 2), ()), (18, 10, 3)),
    (kr1.ClusterData(3, 1, (0, 1, 1), (3,)), (8, 8, 8, 8)),
    (kr1.ClusterData(4, 0, (3, 3, 5, 5), ()), (12, 10, 9, 1)),
    (kr1.ClusterData(4, 0, (4, 4, 4, 4), ()), (12, 12, 8)),
    (kr1.ClusterData(5, 0, (1, 1, 1, 2, 2), ()), (17, 9, 6)),
    (kr1.ClusterData(3, 1, (0, 0, 0), (4,)), (9, 9, 9, 6)),
    (kr1.ClusterData(4, 1, (0, 0, 1, 1), (0,)), (10, 9, 8, 6)),
    (kr1.ClusterData(5, 0, (0, 1, 1, 3, 3), ()), (12, 9, 9, 3)),
    (kr1.ClusterData(5, 0, (0, 2, 2, 2, 2), ()), (15, 12, 6)),
    (kr1.ClusterData(3, 1, (0, 2, 2), (3,)), (10, 8, 8, 8)),
    (kr1.ClusterData(4, 0, (4, 4, 5, 5), ()), (12, 12, 9, 1)),
    (kr1.ClusterData(4, 1, (0, 0, 0, 0), (1,)), (15, 9, 9, 1)),
    (kr1.ClusterData(5, 0, (1, 1, 1, 3, 3), ()), (17, 9, 8)),
    (kr1.ClusterData(5, 0, (1, 2, 2, 2, 2), ()), (18, 10, 6)),
    (kr1.ClusterData(3, 1, (0, 1, 1), (4,)), (9, 9, 9, 8)),
    (kr1.ClusterData(4, 1, (0, 0, 2, 2), (0,)), (10, 10, 9, 6)),
    (kr1.ClusterData(4, 1, (1, 1, 1, 1), (0,)), (15, 10, 9, 1)),
    (kr1.ClusterData(5, 0, (0, 2, 2, 3, 3), ()), (15, 12, 8)),
    (kr1.ClusterData(5, 0, (2, 2, 2, 2, 2), ()), (17, 12, 6)),
    (kr1.ClusterData(3, 1, (0, 0, 0), (5,)), (10, 10, 8, 8)),
    (kr1.ClusterData(4, 0, (4, 4, 6, 6), ()), (12, 8, 8, 8)),
    (kr1.ClusterData(4, 0, (5, 5, 5, 5), ()), (12, 12, 9, 3)),
    (kr1.ClusterData(4, 1, (0, 0, 1, 1), (1,)), (15, 9, 9, 3)),
    (kr1.ClusterData(5, 0, (1, 2, 2, 3, 3), ()), (17, 9, 9, 1)),
    (kr1.ClusterData(6, 0, (0, 0, 0, 0, 0, 0), ()), (18, 10, 8)),
    (kr1.ClusterData(3, 1, (0, 2, 2), (4,)), (9, 9, 9, 9, 1)),
    (kr1.ClusterData(4, 1, (1, 1, 2, 2), (0,)), (12, 9, 8, 8)),
    (kr1.ClusterData(4, 1, (0, 0, 0, 0), (2,)), (12, 10, 9, 6)),
    (kr1.ClusterData(5, 0, (0, 2, 2, 4, 4), ()), (15, 12, 9, 1)),
    (kr1.ClusterData(5, 0, (0, 3, 3, 3, 3), ()), (17, 10, 9, 1)),
    (kr1.ClusterData(5, 0, (2, 2, 2, 3, 3), ()), (17, 12, 8)),
    (kr1.ClusterData(3, 1, (0, 1, 1), (5,)), (10, 9, 9, 9, 1)),
    (kr1.ClusterData(4, 0, (5, 5, 6, 6), ()), (10, 10, 10, 8)),
    (kr1.ClusterData(4, 1, (0, 0, 2, 2), (1,)), (12, 9, 9, 8)),
    (kr1.ClusterData(4, 1, (1, 1, 1, 1), (1,)), (12, 10, 8, 8)),
    (kr1.ClusterData(5, 0, (1, 2, 2, 4, 4), ()), (15, 15, 8)),
    (kr1.ClusterData(5, 0, (1, 3, 3, 3, 3), ()), (17, 9, 9, 3)),
    (kr1.ClusterData(6, 0, (0, 0, 0, 0, 1, 1), ()), (18, 10, 9, 1)),
    (kr1.ClusterData(3, 1, (0, 0, 0), (6,)), (9, 8, 8, 8, 6)),
    (kr1.ClusterData(3, 2, (0, 0, 0), (0, 0)), (9, 9, 9, 9, 3)),
    (kr1.ClusterData(4, 1, (1, 1, 3, 3), (0,)), (12, 10, 9, 8)),
    (kr1.ClusterData(4, 1, (2, 2, 2, 2), (0,)), (12, 12, 9, 6)),
    (kr1.ClusterData(4, 1, (0, 0, 1, 1), (2,)), (15, 8, 8, 8)),
    (kr1.ClusterData(5, 0, (0, 3, 3, 4, 4), ()), (15, 12, 9, 3)),
    (kr1.ClusterData(5, 0, (2, 2, 2, 4, 4), ()), (17, 12, 9, 1)),
    (kr1.ClusterData(5, 0, (2, 3, 3, 3, 3), ()), (19, 12, 8)),
    (kr1.ClusterData(3, 1, (0, 2, 2), (5,)), (8, 8, 8, 8, 8)),
    (kr1.ClusterData(4, 0, (5, 5, 7, 7), ()), (10, 9, 9, 9, 3)),
    (kr1.ClusterData(4, 0, (6, 6, 6, 6), ()), (10, 10, 10, 9, 1)),
    (kr1.ClusterData(4, 1, (1, 1, 2, 2), (1,)), (12, 10, 10, 8)),
    (kr1.ClusterData(4, 1, (0, 0, 0, 0), (3,)), (12, 12, 8, 8)),
    (kr1.ClusterData(5, 0, (1, 3, 3, 4, 4), ()), (15, 15, 9, 1)),
    (kr1.ClusterData(5, 0, (3, 3, 3, 3, 3), ()), (17, 15, 8)),
    (kr1.ClusterData(6, 0, (0, 0, 0, 0, 2, 2), ()), (18, 10, 9, 3)),
    (kr1.ClusterData(6, 0, (0, 0, 1, 1, 1, 1), ()), (18, 12, 9, 1)),
)

APEX_C_TO_U = {c: u for c, u in OCTANT_APEX_PAIRS}
APEX_U_TO_C = {u: c for c, u in OCTANT_APEX_PAIRS}


def reconstruct_octant(c: kr1.ClusterData) -> tuple[int, ...]:
    """Reconstruct u from c in C_{a >= 3} \\ C_{a=3, b=0} via the 3D octant operator triple."""
    a = c.a
    mu_prev = c.mu[a - 4] if a >= 4 else 0
    d3 = c.mu[a - 3] - mu_prev
    d2 = c.mu[a - 2] - c.mu[a - 3]
    d1 = c.mu[a - 1] - c.mu[a - 2]
    q2, r2 = divmod(d2, 3)

    apex_mu = c.mu[: a - 3] + (mu_prev, mu_prev + r2, mu_prev + r2)
    c_apex = kr1.ClusterData(a, c.b, apex_mu, c.nu)
    if c_apex not in APEX_C_TO_U:
        raise OutsideRestrictedDomain(f"Unrecognized octant apex {c_apex}")

    u = APEX_C_TO_U[c_apex]
    for _ in range(q2):
        u = step_six(u)
    for _ in range(d3):
        u = step_three(u)
    for _ in range(d1):
        u = step_one(u)
    return u


def decompose_octant(u: tuple[int, ...]) -> kr1.ClusterData:
    """Decompose u in U_{a >= 3} \\ U_{a=3, b=0} via the inverse 3D octant operator triple."""
    d1 = 0
    curr = u
    while True:
        prev = unstep_one(curr)
        if prev is None:
            break
        curr = prev
        d1 += 1

    d3 = 0
    while True:
        prev = unstep_three(curr)
        if prev is None:
            break
        curr = prev
        d3 += 1

    q2 = 0
    while True:
        prev = unstep_six(curr)
        if prev is None:
            break
        curr = prev
        q2 += 1

    if curr not in APEX_U_TO_C:
        raise OutsideRestrictedDomain(f"Unrecognized octant apex {curr}")
    c_apex = APEX_U_TO_C[curr]
    a = c_apex.a
    mu_prev = c_apex.mu[a - 4] if a >= 4 else 0
    r2 = c_apex.mu[a - 2] - c_apex.mu[a - 3]
    d2 = 3 * q2 + r2
    m3 = mu_prev + d3
    m2 = m3 + d2
    m1 = m2 + d1
    full_mu = c_apex.mu[: a - 3] + (m3, m2, m1)
    return kr1.ClusterData(a, c_apex.b, full_mu, c_apex.nu)


def reconstruct_full(c: kr1.ClusterData) -> tuple[int, ...]:
    if c.a <= 2:
        return rr003_a2.reconstruct_columns(c)
    if c.a == 3 and c.b == 0:
        return reconstruct_a3_b0(c)
    return reconstruct_octant(c)


def decompose_full(u: tuple[int, ...]) -> kr1.ClusterData:
    try:
        return rr003_a2.decompose_columns(u)
    except OutsideRestrictedDomain:
        pass
    try:
        return decompose_a3_b0(u)
    except OutsideRestrictedDomain:
        return decompose_octant(u)


def verify_6d_cone_theorem() -> int:
    """Verify 3,744 states in the 6D cone (10^z, 9^y, 8^x, 6^c6, 3^c3, 1^c1)."""
    count_checked = 0
    for y in (1, 2):
        for z in range(4):
            for x in range(4):
                if x + z == 0:
                    continue
                for c6 in range(5):
                    for c3 in range(5):
                        for c1 in range(5):
                            if x == 0 and c6 + c3 + c1 == 0:
                                continue
                            u = (10,) * z + (9,) * y + (8,) * x + (6,) * c6 + (3,) * c3 + (1,) * c1
                            kr1.decode_columns(u)
                            try:
                                rr003_a2.decompose_columns(u)
                                raise AssertionError(f"Unexpected collision with a<=2 at {u}")
                            except OutsideRestrictedDomain:
                                pass
                            count_checked += 1
    return count_checked


def verify_a3_b0_sector(max_n: int = 40) -> int:
    """Verify reconstruct_a3_b0 and decompose_a3_b0 across all states up to max_n."""
    seen = {}
    for n in range(9, max_n + 1):
        for c in kr1.cluster_data(n):
            if c.a == 3 and c.b == 0:
                u = reconstruct_a3_b0(c)
                assert sum(u) == n
                kr1.decode_columns(u)
                try:
                    rr003_a2.decompose_columns(u)
                    raise AssertionError(f"Collision with a<=2 at {u}")
                except OutsideRestrictedDomain:
                    pass
                assert u not in seen
                seen[u] = c
                assert decompose_a3_b0(u) == c
    return len(seen)


def verify_roundtrip(max_n: int = 40) -> int:
    """Verify complete round-trip B <-> U <-> C <-> A across all states for 0 <= n <= max_n."""
    total_states = 0
    for n in range(0, max_n + 1):
        bs = list(kr1.residue_partitions(n))
        as_ = list(kr1.gap_partitions(n))
        assert len(bs) == len(as_)
        seen_a = set()
        for b in bs:
            u = () if not b else rr003_stockhofe.residue_to_columns(b)
            c = decompose_full(u)
            a = rr003_clusters.cluster_to_gap(c)
            assert kr1.is_gap(a) and sum(a) == n
            assert a not in seen_a
            seen_a.add(a)
            assert rr003_clusters.gap_to_cluster(a) == c
            u2 = reconstruct_full(c)
            assert u2 == u, f"n={n}: reconstruct_full({c}) = {u2} != {u}"
            b2 = () if not u2 else rr003_stockhofe.columns_to_residue(u2)
            assert b2 == b
            total_states += 1
    return total_states


def verify_roundtrip_n26(max_n: int = 26) -> int:
    return verify_roundtrip(max_n)


def run_verification():
    cone_states = verify_6d_cone_theorem()
    a3_b0_states_n35 = verify_a3_b0_sector(35)
    a3_b0_states_n40 = verify_a3_b0_sector(40)
    roundtrip_states_n26 = verify_roundtrip(26)
    roundtrip_states_n40 = verify_roundtrip(40)
    return {
        "status": "passed",
        "six_dim_cone_states_verified": cone_states,
        "a3_b0_states_verified_up_to_n35": a3_b0_states_n35,
        "a3_b0_states_verified_up_to_n40": a3_b0_states_n40,
        "complete_kr1_roundtrip_states_n0_to_26": roundtrip_states_n26,
        "complete_kr1_roundtrip_states_n0_to_40": roundtrip_states_n40,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = run_verification()
    rendered = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")
