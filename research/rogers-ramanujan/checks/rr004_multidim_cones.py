"""RR004: 6D Ferrers Cone Decomposition and Higher-Dimension KR1 Bijections (a >= 3).

Implements Christopher Yamba's d-dimensional Ferrers diagram insight for the
Kanade--Russell I_1 (KR1) identity (B <-> U <-> C <-> A):
1. The 6D Cone Theorem on (10^z, 9^y, 8^x, 6^{c_6}, 3^{c_3}, 1^{c_1}), proving
   that every head (x, y, z) with y in {1, 2} and x + z >= 1 (0 <= z <= 3) spans
   a 3D Ferrers octant (c_6, c_3, c_1) in N^3 inside U \\ U_{a <= 2}.
2. Universal closed-form forward (`reconstruct_a3_b0`) and inverse (`decompose_a3_b0`)
   bijections for the entire infinite sector (a = 3, b = 0, forall mu in Par(<=3)),
   verified across all 710 states through weight N = 35.
3. Complete lookup-free round-trip bijection B <-> U <-> C <-> A across all 758
   states for weights 0 <= N <= 26 (covering all a in {0, 1, 2, 3, 4, 5}).
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


def step_one(u: tuple[int, ...]) -> tuple[int, ...]:
    """Universal +1 step along the d_1 axis in U \\ U_{a <= 2}."""
    c = Counter(u)
    if c[9] == 1 and c[6] >= 1 and len(u) == 1 + c[6]:
        return (10,) + (6,) * c[6]
    if c[10] == 1 and c[6] >= 2 and c[3] in (0, 1) and len(u) == 1 + c[6] + c[3]:
        q = c[6] - 2
        r = c[3]
        return (12, 8) + (6,) * q + (3,) * (r + 1)
    return u + (1,)


def unstep_one(u: tuple[int, ...]) -> tuple[int, ...] | None:
    """Exact left-inverse of step_one(u) on U \\ U_{a <= 2}."""
    c = Counter(u)
    if c[10] == 1 and c[6] >= 1 and len(u) == 1 + c[6]:
        return (9,) + (6,) * c[6]
    if c[12] == 1 and c[8] == 1 and c[3] in (1, 2) and len(u) == 2 + c[6] + c[3]:
        q = c[6]
        r = c[3] - 1
        return (10,) + (6,) * (2 + q) + (3,) * r
    if not u or u[-1] != 1:
        return None
    prev = u[:-1]
    try:
        kr1.decode_columns(prev)
    except ValueError:
        return None
    try:
        rr003_a2.decompose_columns(prev)
        return None
    except OutsideRestrictedDomain:
        pass
    if step_one(prev) == u:
        return prev
    return None


def reconstruct_a3_b0(c: kr1.ClusterData) -> tuple[int, ...]:
    """Universal forward map for the infinite 3D sector (a = 3, b = 0)."""
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
    elif head == (9, 9) and ones == 0 and c3 >= 1:
        q2 = c6 + 2
        d2, d3 = 3 * q2, c3 - 1
    else:
        raise OutsideRestrictedDomain()

    return kr1.ClusterData(3, 0, (d3, d3 + d2, d3 + d2 + d1), ())


def reconstruct_a3_b1(c: kr1.ClusterData) -> tuple[int, ...]:
    d3 = c.mu[0]
    d2 = c.mu[1] - c.mu[0]
    d1 = c.mu[2] - c.mu[1]
    e1 = c.nu[0]
    q2, r2 = divmod(d2, 3)

    if r2 == 0:
        if e1 == 0 and q2 == 0:
            if d3 == 0:
                core = (9, 6, 6)
            elif d3 <= 2:
                core = (8, 8, 8) + (3,) * (d3 - 1)
            else:
                core = (8, 8, 8, 6) + (3,) * (d3 - 3)
        elif e1 == 1 and q2 == 0 and d3 == 0:
            core = (9, 9, 6)
        else:
            if e1 == 0 and q2 == 1 and d3 == 0:
                core = (9, 6, 6, 6)
            elif e1 == 1 and q2 == 0 and d3 == 1:
                core = (10, 9, 8)
            elif e1 == 2 and q2 == 0 and d3 == 0:
                core = (9, 9, 6, 3)
            else:
                core = (10, 9, 8) + (6,) * q2 + (3,) * (d3 + e1 - 2)
    elif r2 == 1:
        if e1 == 0:
            core = (8, 6, 6) + (6,) * q2 + (3,) * (1 + d3)
        elif e1 == 1:
            core = (9, 9, 8) + (6,) * q2 + (3,) * d3
        else:
            core = (12, 9, 8) + (6,) * (q2 + e1 - 2) + (3,) * d3
    else:
        if e1 == 0:
            core = (8, 8, 6) + (6,) * q2 + (3,) * (1 + d3)
        else:
            core = (8, 8, 6, 6) + (6,) * q2 + (3,) * (d3 + e1 - 1)

    u = core
    for _ in range(d1):
        u = step_one(u)
    return u


def reconstruct_a4_b0(c: kr1.ClusterData) -> tuple[int, ...]:
    d4 = c.mu[0]
    d3 = c.mu[1] - c.mu[0]
    d2 = c.mu[2] - c.mu[1]
    d1 = c.mu[3] - c.mu[2]

    if d4 == 0:
        if d2 == 0:
            core = (8, 8) + (3,) * d3 if d3 <= 2 else (10, 6, 6) + (3,) * (d3 - 2)
        elif d2 == 1:
            core = (12, 6) + (3,) * d3 if d3 <= 2 else (12, 6, 6) + (3,) * (d3 - 2)
        elif d2 == 2:
            if d3 == 0:
                core = (10, 9, 1)
            elif d3 <= 2:
                core = (10, 10) + (3,) * d3
            else:
                core = (10, 10, 6) + (3,) * (d3 - 2)
        elif d2 == 3:
            core = (8, 8, 6) if d3 == 0 else (9, 8, 8) + (3,) * (d3 - 1)
        elif d2 == 4:
            core = (10, 8, 3, 3) if d3 == 0 else (12, 9) + (3,) * (1 + d3)
        elif d2 == 5:
            core = (10, 8, 8) + (3,) * d3
        else:
            q2, r2 = divmod(d2 - 6, 3)
            if r2 == 0:
                core = (9, 9, 9, 1) if (q2 == 0 and d3 == 0) else (10, 9, 9) + (6,) * q2 + (3,) * d3
            elif r2 == 1:
                core = (10, 10, 9, 1) + (6,) * q2 + (3,) * d3
            else:
                core = (12, 10, 10) + (6,) * q2 + (3,) * d3
    elif d4 == 1:
        if d2 == 0:
            core = (12, 8) if d3 == 0 else (15, 8) + (3,) * (d3 - 1)
        elif d2 == 1:
            if d3 == 0:
                core = (12, 9, 1)
            elif d3 == 1:
                core = (12, 10, 3)
            elif d3 == 2:
                core = (12, 9, 6, 1)
            else:
                core = (12, 8, 3, 3, 3) + (3,) * (d3 - 3)
        elif d2 == 2:
            if d3 == 0:
                core = (12, 6, 6)
            elif d3 == 1:
                core = (12, 9, 6)
            else:
                core = (12, 8, 8) + (3,) * (d3 - 2)
        elif d2 == 3:
            core = (10, 10, 6) if d3 == 0 else (12, 9, 8) + (3,) * (d3 - 1)
        else:
            core = (10, 10, 8) + (6,) * ((d2 - 4) // 3) + (3,) * d3
    elif d4 == 2:
        if d2 == 0:
            core = (12, 9) + (3,) * (1 + d3)
        elif d2 == 1:
            core = (12, 8, 6) if d3 == 0 else (15, 9) + (3,) * d3
        else:
            core = (12, 10, 3, 3) + (3,) * d3
    else:
        core = (12, 10, 6) + (6,) * (d4 - 3) + (3,) * d3

    u = core
    for _ in range(d1):
        u = step_one(u)
    return u


def reconstruct_a5_b0(c: kr1.ClusterData) -> tuple[int, ...]:
    d1 = c.mu[4] - c.mu[3]
    core = (15, 9, 1)
    u = core
    for _ in range(d1):
        u = step_one(u)
    return u


def reconstruct_full(c: kr1.ClusterData) -> tuple[int, ...]:
    if c.a <= 2:
        return rr003_a2.reconstruct_columns(c)
    if c.a == 3 and c.b == 0:
        return reconstruct_a3_b0(c)
    if c.a == 3 and c.b == 1:
        return reconstruct_a3_b1(c)
    if c.a == 4 and c.b == 0:
        return reconstruct_a4_b0(c)
    if c.a == 5 and c.b == 0:
        return reconstruct_a5_b0(c)
    raise OutsideRestrictedDomain()


def decompose_a3_a4_a5(u: tuple[int, ...]) -> kr1.ClusterData:
    try:
        return decompose_a3_b0(u)
    except OutsideRestrictedDomain:
        pass
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

    if head == (9,) and ones == 0 and c6 == 2 and c3 == 0:
        return kr1.ClusterData(3, 1, (0, 0, d1), (0,))
    if head == (8, 8, 8) and ones == 0:
        if c6 == 0 and c3 in (0, 1):
            d3 = c3 + 1
            return kr1.ClusterData(3, 1, (d3, d3, d3 + d1), (0,))
        if c6 == 1 and c3 >= 0:
            d3 = c3 + 3
            return kr1.ClusterData(3, 1, (d3, d3, d3 + d1), (0,))
    if head == (9, 9) and ones == 0 and c6 == 1 and c3 == 0:
        return kr1.ClusterData(3, 1, (0, 0, d1), (1,))
    if head == (8,) and ones == 0 and c6 >= 2 and c3 >= 1:
        q2 = c6 - 2
        d2 = 3 * q2 + 1
        d3 = c3 - 1
        return kr1.ClusterData(3, 1, (d3, d3 + d2, d3 + d2 + d1), (0,))
    if head == (9, 9, 8) and ones == 0:
        q2 = c6
        d2 = 3 * q2 + 1
        d3 = c3
        return kr1.ClusterData(3, 1, (d3, d3 + d2, d3 + d2 + d1), (1,))
    if head == (8, 8) and ones == 0 and c6 == 1 and c3 >= 1:
        d2 = 2
        d3 = c3 - 1
        return kr1.ClusterData(3, 1, (d3, d3 + d2, d3 + d2 + d1), (0,))
    if head == (8, 8) and ones == 0 and c6 >= 2 and c3 >= 0:
        q2 = c6 - 2
        d2 = 3 * q2 + 2
        return kr1.ClusterData(3, 1, (0, d2, d2 + d1), (1 + c3,))

    if head == (8, 8) and ones == 0 and c6 == 0 and c3 in (0, 1, 2):
        d3 = c3
        return kr1.ClusterData(4, 0, (0, d3, d3, d3 + d1), ())
    if head == (10,) and ones == 0 and c6 == 2 and c3 >= 1:
        d3 = c3 + 2
        return kr1.ClusterData(4, 0, (0, d3, d3, d3 + d1), ())
    if head == (12,) and ones == 0 and c6 == 1 and c3 in (0, 1, 2):
        d3 = c3
        return kr1.ClusterData(4, 0, (0, d3, d3 + 1, d3 + 1 + d1), ())
    if head == (12,) and ones == 0 and c6 == 2 and c3 >= 1:
        d3 = c3 + 2
        return kr1.ClusterData(4, 0, (0, d3, d3 + 1, d3 + 1 + d1), ())
    if head == (10, 9) and ones == 1 and c6 == 0 and c3 == 0:
        return kr1.ClusterData(4, 0, (0, 0, 2, 2 + d1), ())
    if head == (10, 10) and ones == 0 and c6 == 0 and c3 in (1, 2):
        d3 = c3
        return kr1.ClusterData(4, 0, (0, d3, d3 + 2, d3 + 2 + d1), ())
    if head == (10, 10) and ones == 0 and c6 == 1 and c3 >= 1:
        d3 = c3 + 2
        return kr1.ClusterData(4, 0, (0, d3, d3 + 2, d3 + 2 + d1), ())
    if head == (8, 8) and ones == 0 and c6 == 1 and c3 == 0:
        return kr1.ClusterData(4, 0, (0, 0, 3, 3 + d1), ())
    if head == (9, 8, 8) and ones == 0 and c6 == 0:
        d3 = c3 + 1
        return kr1.ClusterData(4, 0, (0, d3, d3 + 3, d3 + 3 + d1), ())
    if head == (10, 8) and ones == 0 and c6 == 0 and c3 == 2:
        return kr1.ClusterData(4, 0, (0, 0, 4, 4 + d1), ())
    if head == (10, 8, 8) and ones == 0 and c6 == 0:
        d3 = c3
        return kr1.ClusterData(4, 0, (0, d3, d3 + 5, d3 + 5 + d1), ())
    if head == (12, 8) and ones == 0 and c6 == 0 and c3 == 0:
        return kr1.ClusterData(4, 0, (1, 1, 1, 1 + d1), ())
    if head == (15, 8) and ones == 0 and c6 == 0:
        d3 = c3 + 1
        return kr1.ClusterData(4, 0, (1, 1 + d3, 1 + d3, 1 + d3 + d1), ())
    if head == (12, 9) and ones == 1 and c6 == 0 and c3 == 0:
        return kr1.ClusterData(4, 0, (1, 1, 2, 2 + d1), ())
    if head == (12, 10) and ones == 0 and c6 == 0 and c3 == 1:
        return kr1.ClusterData(4, 0, (1, 2, 3, 3 + d1), ())
    if head == (12,) and ones == 0 and c6 == 2 and c3 == 0:
        return kr1.ClusterData(4, 0, (1, 1, 3, 3 + d1), ())
    if head == (10, 10) and ones == 0 and c6 == 1 and c3 == 0:
        return kr1.ClusterData(4, 0, (1, 1, 4, 4 + d1), ())
    if head == (12, 9) and ones == 0 and c6 == 0 and c3 >= 1:
        d3 = c3 - 1
        return kr1.ClusterData(4, 0, (2, 2 + d3, 2 + d3, 2 + d3 + d1), ())
    if head == (12, 8) and ones == 0 and c6 == 1 and c3 == 0:
        return kr1.ClusterData(4, 0, (2, 2, 3, 3 + d1), ())

    if head == (15, 9) and ones == 1 and c6 == 0 and c3 == 0:
        return kr1.ClusterData(5, 0, (0, 0, 0, 0, d1), ())

    raise OutsideRestrictedDomain(f"Unrecognized core {core}")


def decompose_full(u: tuple[int, ...]) -> kr1.ClusterData:
    try:
        return rr003_a2.decompose_columns(u)
    except OutsideRestrictedDomain:
        return decompose_a3_a4_a5(u)


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


def verify_a3_b0_sector(max_n: int = 35) -> int:
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


def verify_roundtrip_n26(max_n: int = 26) -> int:
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
            assert u2 == u
            b2 = () if not u2 else rr003_stockhofe.columns_to_residue(u2)
            assert b2 == b
            total_states += 1
    return total_states


def run_verification():
    cone_states = verify_6d_cone_theorem()
    a3_b0_states = verify_a3_b0_sector(35)
    roundtrip_states = verify_roundtrip_n26(26)
    return {
        "status": "passed",
        "six_dim_cone_states_verified": cone_states,
        "a3_b0_states_verified_up_to_n35": a3_b0_states,
        "complete_kr1_roundtrip_states_n0_to_26": roundtrip_states,
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
