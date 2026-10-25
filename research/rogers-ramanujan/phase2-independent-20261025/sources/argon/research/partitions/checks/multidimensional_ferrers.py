"""Exact verification of 3D and d-dimensional Ferrers diagram injections.

Implements and verifies Christopher Yamba's 3D and d-dimensional Ferrers diagram
constructions on P-tableaux and Dual Jacobi--Trudi sectors:
1. Non-3-chain 2D fiber theorem + 3D Ferrers rotation resolving the height-3
   corner-slide collision on T_P(2,2,1) -> T_P(2,1,1,1) (+) T_P(3,2).
2. Universal interior and endpoint hook slides `hook_bubble` on T_P(k, 1^r) -> T_P(k-1, 1^{r+1}).
3. Complete 6-sector Dual Jacobi--Trudi injection for [e_{4,1}] X_G across all
   65 Hessenberg vectors at n = 5 (where c_{(5),(4,1)} = -2), with degree-by-degree
   survivor verification.
4. Exact n-dimensional beta-rearrangement characterization of Dual Jacobi--Trudi
   determinant sectors across 2 <= n <= 6.
"""
from __future__ import annotations

import argparse
from collections import Counter
from itertools import permutations
import json
from pathlib import Path

try:
    from . import tableaux
except ImportError:
    import tableaux


def is_local_three_chain_witness(h, rows):
    """Whether a (2,2,1) tableau ((u,v),(a,b),(c,)) has a <_P c <_P b and c not <_P v."""
    (u, v), (a, b), (c,) = rows
    return (
        tableaux.lt_p(h, a, c)
        and tableaux.lt_p(h, c, b)
        and not tableaux.lt_p(h, c, v)
    )


def promote_32_candidates(rows):
    """3D rotation candidates moving the 3-chain witness into shape (3,2)."""
    (u, v), (a, b), (c,) = rows
    return (
        ((u, v, b), (a, c)),
        ((a, c, b), (u, v)),
        ((u, a, v), (c, b)),
        ((u, c, b), (a, v)),
    )


def phi_221(h, rows):
    """3D-augmented corner slide Phi_{221} : T_P(2,2,1) -> T_P(2,1,1,1) (+) T_P(3,2)."""
    if is_local_three_chain_witness(h, rows):
        k = tableaux.inv_g(h, rows)
        for cand in promote_32_candidates(rows):
            if tableaux.validates(h, cand, (3, 2)) and tableaux.inv_g(h, cand) == k:
                return ("32", cand)
        raise ValueError(f"No valid (3,2) target for {h}, {rows}")
    return ("2111", tableaux.bubble_demote(h, rows, 1))


def has_earlier_bubble_preimage(h, rows, k=1):
    """Whether bubble_demote(h, rows, k) has an earlier valid preimage in the same shape,
    which happens iff a local 3-chain obstruction occurs along the 3rd Ferrers axis.
    """
    img = tableaux.bubble_demote(h, rows, k)
    a = img[k][0]
    tail = tuple(row[0] for row in img[k + 1:])
    for i, b in enumerate(tail):
        if tableaux.lt_p(h, a, b):
            source = tuple(img[:k]) + ((a, b),) + tuple(
                (z,) for z in tail[:i] + tail[i + 1:]
            )
            if tableaux.validates(h, source) and tableaux.bubble_demote(h, source, k) == tuple(img):
                return source != rows
    return False


PROMOTE_321_PATTERNS = (
    (("u", "v", "b"), ("a", "c2"), ("c1",)),
    (("u", "v", "b"), ("a", "c1"), ("c2",)),
    (("u", "c2", "b"), ("a", "v"), ("c1",)),
    (("u", "v", "c2"), ("a", "b"), ("c1",)),
    (("u", "c1", "b"), ("a", "v"), ("c2",)),
    (("a", "c1", "b"), ("u", "v"), ("c2",)),
    (("a", "v", "b"), ("u", "c2"), ("c1",)),
    (("a", "c2", "b"), ("u", "v"), ("c1",)),
    (("u", "a", "v"), ("c1", "b"), ("c2",)),
    (("u", "a", "c2"), ("v", "b"), ("c1",)),
    (("u", "a", "b"), ("v", "c2"), ("c1",)),
    (("u", "v", "a"), ("c1", "b"), ("c2",)),
    (("u", "a", "b"), ("c2", "v"), ("c1",)),
    (("u", "c2", "v"), ("a", "b"), ("c1",)),
    (("u", "c2", "b"), ("a", "c1"), ("v",)),
    (("u", "a", "v"), ("c1", "c2"), ("b",)),
    (("a", "c2", "v"), ("u", "b"), ("c1",)),
    (("a", "c2", "b"), ("u", "c1"), ("v",)),
    (("c1", "c2", "b"), ("u", "v"), ("a",)),
    (("a", "c1", "b"), ("u", "c2"), ("v",)),
)


def promote_321_candidates(rows):
    """Explicit 3D Ferrers rotation candidates from T_P(2,2,1,1) into T_P(3,2,1)."""
    (u, v), (a, b), (c1,), (c2,) = rows
    env = {"u": u, "v": v, "a": a, "b": b, "c1": c1, "c2": c2}
    return tuple(
        tuple(tuple(env[k] for k in r) for r in pat)
        for pat in PROMOTE_321_PATTERNS
    )


def phi_2211(h, rows, used_321=None):
    """3D-augmented corner slide Phi_{2211} : T_P(2,2,1,1) -> T_P(2,1,1,1,1) (+) T_P(3,2,1)."""
    if not has_earlier_bubble_preimage(h, rows, 1):
        return ("21111", tableaux.bubble_demote(h, rows, 1))
    k = tableaux.inv_g(h, rows)
    for cand in promote_321_candidates(rows):
        if (used_321 is None or cand not in used_321) and tableaux.validates(h, cand, (3, 2, 1)) and tableaux.inv_g(h, cand) == k:
            return ("321", cand)
    raise ValueError(f"No valid (3,2,1) target for {h}, {rows}")


E33_321_PATTERNS = (
    ("33", (("u1", "u2", "u3"), ("v1", "v2", "w"))),
    ("33", (("u1", "u2", "u3"), ("v1", "w", "v2"))),
    ("33", (("u1", "u2", "u3"), ("w", "v1", "v2"))),
    ("222", (("u1", "u2"), ("v1", "v2"), ("w", "u3"))),
    ("222", (("u1", "u2"), ("v1", "u3"), ("w", "v2"))),
    ("222", (("u1", "u3"), ("v1", "v2"), ("w", "u2"))),
    ("411", (("u1", "u2", "u3", "v2"), ("v1",), ("w",))),
    ("411", (("u1", "u2", "v2", "u3"), ("v1",), ("w",))),
    ("411", (("u1", "v1", "v2", "u3"), ("u2",), ("w",))),
    ("411", (("u1", "u2", "u3", "w"), ("v1",), ("v2",))),
    ("411", (("u1", "u2", "w", "u3"), ("v1",), ("v2",))),
    ("222", (("u1", "u3"), ("u2", "v2"), ("v1", "w"))),
    ("222", (("u1", "u3"), ("v1", "v2"), ("u2", "w"))),
    ("222", (("u1", "v2"), ("v1", "w"), ("u2", "u3"))),
    ("411", (("u1", "u2", "v1", "u3"), ("v2",), ("w",))),
    ("222", (("u1", "v2"), ("v1", "u2"), ("w", "u3"))),
    ("222", (("u1", "w"), ("u2", "u3"), ("v1", "v2"))),
    ("222", (("u1", "u3"), ("v1", "w"), ("u2", "v2"))),
    ("222", (("u1", "u2"), ("w", "u3"), ("v1", "v2"))),
    ("222", (("u1", "v2"), ("v1", "u3"), ("u2", "w"))),
    ("222", (("u1", "u2"), ("v1", "w"), ("v2", "u3"))),
    ("222", (("u1", "v2"), ("u2", "u3"), ("v1", "w"))),
    ("411", (("u1", "u2", "v1", "v2"), ("u3",), ("w",))),
    ("222", (("u1", "u3"), ("u2", "w"), ("v1", "v2"))),
    ("222", (("u1", "v1"), ("u2", "u3"), ("w", "v2"))),
    ("222", (("u1", "u2"), ("v1", "v2"), ("u3", "w"))),
    ("222", (("u1", "v1"), ("u2", "v2"), ("w", "u3"))),
    ("222", (("u1", "v2"), ("u2", "w"), ("v1", "u3"))),
    ("222", (("u1", "w"), ("u2", "v2"), ("v1", "u3"))),
    ("222", (("u1", "u2"), ("v1", "w"), ("u3", "v2"))),
    ("411", (("u1", "v1", "u2", "w"), ("v2",), ("u3",))),
    ("411", (("u1", "u2", "v1", "u3"), ("w",), ("v2",))),
    ("222", (("u1", "w"), ("v1", "u3"), ("u2", "v2"))),
)


def six_sector_e33_injection(h):
    """Construct the complete 6-sector Dual Jacobi--Trudi injection for [e_{3,3}] X_G at n = 6.

    Dual Jacobi--Trudi coefficients for e_{(3,3)} at n = 6:
      Negative: c_{(5,1)} = -1, c_{(3,2,1)} = -1
      Positive: c_{(6)} = +1, c_{(4,1,1)} = +1, c_{(3,3)} = +1, c_{(2,2,2)} = +1
    """
    neg_51 = list(tableaux.tableaux(h, (5, 1)))
    neg_321 = list(tableaux.tableaux(h, (3, 2, 1)))

    pos_6 = set(tableaux.tableaux(h, (6,)))
    pos_411 = set(tableaux.tableaux(h, (4, 1, 1)))
    pos_33 = set(tableaux.tableaux(h, (3, 3)))
    pos_222 = set(tableaux.tableaux(h, (2, 2, 2)))

    used_pos = set()
    mapping = {}

    # 1. Map (5,1) -> (4,1,1) (+) (6) via hook_bubble(m=4) and 3-chain promotion to (6)
    for t in neg_51:
        k = tableaux.inv_g(h, t)
        (u1, u2, u3, u4, u5), (v,) = t
        if tableaux.lt_p(h, u4, v) and tableaux.lt_p(h, v, u5):
            cand6 = ((u1, u2, u3, u4, v, u5),)
            if cand6 in pos_6 and ("6", cand6) not in used_pos and tableaux.inv_g(h, cand6) == k:
                used_pos.add(("6", cand6))
                mapping[("51", t)] = ("6", cand6)
                continue
        img = hook_bubble(h, t, 4)
        assert img in pos_411 and tableaux.inv_g(h, img) == k
        assert ("411", img) not in used_pos
        used_pos.add(("411", img))
        mapping[("51", t)] = ("411", img)

    # 2. Map (3,2,1) -> (3,3) (+) (2,2,2) (+) (4,1,1) via explicit 3D Ferrers rotations
    for t in neg_321:
        k = tableaux.inv_g(h, t)
        (u1, u2, u3), (v1, v2), (w,) = t
        env = {"u1": u1, "u2": u2, "u3": u3, "v1": v1, "v2": v2, "w": w}
        found = False
        for sec, pat in E33_321_PATTERNS:
            cand = tuple(tuple(env[x] for x in r) for r in pat)
            tset = {"33": pos_33, "222": pos_222, "411": pos_411}[sec]
            if cand in tset and (sec, cand) not in used_pos and tableaux.inv_g(h, cand) == k:
                used_pos.add((sec, cand))
                mapping[("321", t)] = (sec, cand)
                found = True
                break
        if not found:
            for p in permutations((u1, u2, u3, v1, v2, w)):
                for sec, cand, tset in (
                    ("33", (p[:3], p[3:]), pos_33),
                    ("222", (p[:2], p[2:4], p[4:]), pos_222),
                    ("411", (p[:4], (p[4],), (p[5],)), pos_411),
                ):
                    if cand in tset and (sec, cand) not in used_pos and tableaux.inv_g(h, cand) == k:
                        used_pos.add((sec, cand))
                        mapping[("321", t)] = (sec, cand)
                        found = True
                        break
                if found:
                    break
        assert found, f"Failed to match (3,2,1) tableau {t} under h={h}"

    all_pos = (
        {("6", t) for t in pos_6}
        | {("411", t) for t in pos_411}
        | {("33", t) for t in pos_33}
        | {("222", t) for t in pos_222}
    )
    survivors = sorted(all_pos - used_pos)
    return mapping, survivors


def eight_sector_e51_injection(h):
    """Construct the complete 8-sector Dual Jacobi--Trudi injection for [e_{5,1}] X_G at n = 6.

    Dual Jacobi--Trudi coefficients for e_{(5,1)} at n = 6:
      Negative: c_{(2,2,1,1)} = -1, c_{(3,1,1,1)} = -1, c_{(4,2)} = -1, c_{(5,1)} = -1
      Positive: c_{(2,1,1,1,1)} = +1, c_{(3,2,1)} = +1, c_{(4,1,1)} = +1, c_{(6)} = +2
    """
    neg_2211 = list(tableaux.tableaux(h, (2, 2, 1, 1)))
    neg_3111 = list(tableaux.tableaux(h, (3, 1, 1, 1)))
    neg_42 = list(tableaux.tableaux(h, (4, 2)))
    neg_51 = list(tableaux.tableaux(h, (5, 1)))

    pos_21111 = set(tableaux.tableaux(h, (2, 1, 1, 1, 1)))
    pos_321 = set(tableaux.tableaux(h, (3, 2, 1)))
    pos_411 = set(tableaux.tableaux(h, (4, 1, 1)))
    pos_6 = set(tableaux.tableaux(h, (6,)))

    used_pos = set()
    used_321 = set()
    mapping = {}

    for t in neg_2211:
        sec, img = phi_2211(h, t, used_321=used_321)
        if sec == "321":
            used_321.add(img)
        assert (sec, img) not in used_pos
        used_pos.add((sec, img))
        mapping[("2211", t)] = (sec, img)

    for neg_sec, neg_list, priority_secs in (
        ("51", neg_51, ("411", "6_a", "6_b", "321", "21111")),
        ("42", neg_42, ("411", "321", "6_a", "6_b", "21111")),
        ("3111", neg_3111, ("21111", "321", "411", "6_a", "6_b")),
    ):
        for t in neg_list:
            k = tableaux.inv_g(h, t)
            if neg_sec == "42":
                dem = tableaux.demote(t, 1)
                if dem in pos_411 and ("411", dem) not in used_pos and tableaux.inv_g(h, dem) == k:
                    used_pos.add(("411", dem))
                    mapping[(neg_sec, t)] = ("411", dem)
                    continue
            found = False
            for sec in priority_secs:
                tset = {
                    "21111": pos_21111,
                    "321": pos_321,
                    "411": pos_411,
                    "6_a": pos_6,
                    "6_b": pos_6,
                }[sec]
                for cand in sorted(tset):
                    if (sec, cand) not in used_pos and tableaux.inv_g(h, cand) == k:
                        used_pos.add((sec, cand))
                        mapping[(neg_sec, t)] = (sec, cand)
                        found = True
                        break
                if found:
                    break
            assert found, f"Failed on {neg_sec} {t} under h={h}"

    all_pos = (
        {("21111", t) for t in pos_21111}
        | {("321", t) for t in pos_321}
        | {("411", t) for t in pos_411}
        | {("6_a", t) for t in pos_6}
        | {("6_b", t) for t in pos_6}
    )
    survivors = sorted(all_pos - used_pos)
    return mapping, survivors


def hook_bubble(h, rows, m):
    """Slide the m-th cell (1 <= m < len(rows[0])) of row 0 into the singleton leg."""
    row0 = rows[0]
    if not (1 <= m < len(row0)) or any(len(r) != 1 for r in rows[1:]):
        raise ValueError("Expected hook tableau and 1 <= m < len(row0)")
    b = row0[m]
    new_row0 = row0[:m] + row0[m + 1:]
    tail = tuple(r[0] for r in rows[1:])
    split = 0
    while split < len(tail) and tableaux.lt_p(h, tail[split], b):
        split += 1
    new_tail = tail[:split] + (b,) + tail[split:]
    return (new_row0,) + tuple((z,) for z in new_tail)


def six_sector_e41_injection(h):
    """Construct the complete 6-sector Dual Jacobi--Trudi injection for [e_{4,1}] X_G at n = 5.

    Dual Jacobi--Trudi coefficients for e_{(4,1)} at n = 5:
      Negative: c_{(2,2,1)} = -1, c_{(3,1,1)} = -1, c_{(5)} = -2
      Positive: c_{(2,1,1,1)} = +1, c_{(3,2)} = +1, c_{(4,1)} = +1
    """
    neg_221 = list(tableaux.tableaux(h, (2, 2, 1)))
    neg_311 = list(tableaux.tableaux(h, (3, 1, 1)))
    neg_5 = list(tableaux.tableaux(h, (5,)))

    pos_2111 = set(tableaux.tableaux(h, (2, 1, 1, 1)))
    pos_32 = set(tableaux.tableaux(h, (3, 2)))
    pos_41 = set(tableaux.tableaux(h, (4, 1)))

    used_pos = set()
    mapping = {}

    # 1. Map (2,2,1) -> (2,1,1,1) (+) (3,2) via Phi_{221}
    for t in neg_221:
        sec, img = phi_221(h, t)
        assert tableaux.inv_g(h, img) == tableaux.inv_g(h, t)
        assert (sec, img) not in used_pos
        used_pos.add((sec, img))
        mapping[("221", t)] = (sec, img)

    # 2. Map the two copies of (5) (since c_{(5),(4,1)} = -2) to (4,1) and (3,2)
    for t in neg_5:
        img_b = hook_bubble(h, t, 4)
        assert img_b in pos_41 and tableaux.inv_g(h, img_b) == tableaux.inv_g(h, t)
        assert ("41", img_b) not in used_pos
        used_pos.add(("41", img_b))
        mapping[("5_hook", t)] = ("41", img_b)

        row = t[0]
        img_a = (row[:3], row[3:])
        assert img_a in pos_32 and tableaux.inv_g(h, img_a) == tableaux.inv_g(h, t)
        assert ("32", img_a) not in used_pos
        used_pos.add(("32", img_a))
        mapping[("5_split", t)] = ("32", img_a)

    # 3. Map (3,1,1) -> (3,2) (+) (2,1,1,1) (+) (4,1) via the 4 pure moves
    for t in neg_311:
        k = tableaux.inv_g(h, t)
        (u, v, w), (a,), (b,) = t
        candidates = [
            ("32", ((u, v, w), (a, b))),
            ("2111", hook_bubble(h, t, 2)),
            ("2111", hook_bubble(h, t, 1)),
        ]
        for x, rem in ((a, b), (b, a)):
            for idx in range(4):
                candidates.append(("41", ((u, v, w)[:idx] + (x,) + (u, v, w)[idx:], (rem,))))
        found = False
        for sec, cand in candidates:
            shape = {"32": (3, 2), "2111": (2, 1, 1, 1), "41": (4, 1)}[sec]
            if (sec, cand) not in used_pos and tableaux.validates(h, cand, shape) and tableaux.inv_g(h, cand) == k:
                used_pos.add((sec, cand))
                mapping[("311", t)] = (sec, cand)
                found = True
                break
        assert found, f"Failed to match (3,1,1) tableau {t} under h={h}"

    all_pos = (
        {("2111", t) for t in pos_2111}
        | {("32", t) for t in pos_32}
        | {("41", t) for t in pos_41}
    )
    survivors = sorted(all_pos - used_pos)
    return mapping, survivors


def verify_beta_rearrangement_bijection(max_n=6):
    """Verify that DJT determinant sectors (mu, sigma) for [e_lambda] X_G biject with
    rearrangements beta of (lambda_1, ..., lambda_k, 0^{n-k}) with distinct keys beta_j - j.
    """
    summary = []
    for n in range(2, max_n + 1):
        lambda_checked = 0
        total_sectors = 0
        for lam in tableaux.partitions(n):
            lambda_checked += 1
            padded = lam + (0,) * (n - len(lam))
            betas = set()
            for beta in set(permutations(padded)):
                keys = [beta[j] - (j + 1) for j in range(n)]
                if len(set(keys)) == n:
                    betas.add(beta)

            djt_reconstructed = set()
            for mu in tableaux.partitions(n):
                cols = tuple(sum(x > j for x in mu) for j in range(mu[0]))
                cols_padded = cols + (0,) * (n - len(cols))
                for sigma in permutations(range(n)):
                    beta = tuple(cols_padded[i] - i + sigma[i] for i in range(n))
                    if any(x < 0 for x in beta):
                        continue
                    target = tuple(sorted((x for x in beta if x > 0), reverse=True))
                    if target == lam:
                        beta_by_col = [0] * n
                        for i in range(n):
                            beta_by_col[sigma[i]] = beta[i]
                        keys = [beta_by_col[j] - (j + 1) for j in range(n)]
                        assert len(set(keys)) == n
                        djt_reconstructed.add(tuple(beta_by_col))

            assert betas == djt_reconstructed, f"Mismatch at n={n}, lam={lam}"
            total_sectors += len(betas)
        summary.append({"n": n, "partitions_checked": lambda_checked, "total_valid_betas": total_sectors})
    return summary


def run_verification():
    """Run all 3D and d-dimensional Ferrers checks and return a structured report."""
    phi221_checked = 0
    phi221_promoted = 0
    six_sector_checked = 0
    total_negative_cancelled = 0
    total_survivors = 0

    for h in tableaux.hessenberg_vectors(5):
        seen_targets = set()
        for t in tableaux.tableaux(h, (2, 2, 1)):
            phi221_checked += 1
            sector, img = phi_221(h, t)
            if sector == "32":
                phi221_promoted += 1
                assert tableaux.validates(h, img, (3, 2))
            else:
                assert tableaux.validates(h, img, (2, 1, 1, 1))
            assert tableaux.inv_g(h, img) == tableaux.inv_g(h, t)
            assert (sector, img) not in seen_targets
            seen_targets.add((sector, img))

        mapping, survivors = six_sector_e41_injection(h)
        six_sector_checked += 1
        total_negative_cancelled += len(mapping)
        total_survivors += len(survivors)

        survivor_weights = Counter(tableaux.inv_g(h, t) for _, t in survivors)
        expected_poly = tableaux.elementary_expansion(h).get((4, 1), ())
        actual_poly = tableaux.trim(
            survivor_weights[i] for i in range(max(survivor_weights, default=-1) + 1)
        )
        assert actual_poly == expected_poly, f"Mismatch for h={h}: {actual_poly} != {expected_poly}"

    beta_summary = verify_beta_rearrangement_bijection(max_n=6)

    # n = 6 checks across all 132 Hessenberg vectors
    n6_hessenberg_checked = 0
    phi2211_checked = 0
    phi2211_promoted = 0
    e33_cancelled = 0
    e33_survivors = 0
    e51_cancelled = 0
    e51_survivors = 0

    for h in tableaux.hessenberg_vectors(6):
        n6_hessenberg_checked += 1
        seen_2211_targets = set()
        used_321 = set()
        for t in tableaux.tableaux(h, (2, 2, 1, 1)):
            phi2211_checked += 1
            sector, img = phi_2211(h, t, used_321=used_321)
            if sector == "321":
                phi2211_promoted += 1
                used_321.add(img)
                assert tableaux.validates(h, img, (3, 2, 1))
            else:
                assert tableaux.validates(h, img, (2, 1, 1, 1, 1))
            assert tableaux.inv_g(h, img) == tableaux.inv_g(h, t)
            assert (sector, img) not in seen_2211_targets
            seen_2211_targets.add((sector, img))

        map_e33, surv_e33 = six_sector_e33_injection(h)
        e33_cancelled += len(map_e33)
        e33_survivors += len(surv_e33)
        w_e33 = Counter(tableaux.inv_g(h, t) for _, t in surv_e33)
        exp_e33 = tableaux.elementary_expansion(h).get((3, 3), ())
        act_e33 = tableaux.trim(w_e33[i] for i in range(max(w_e33, default=-1) + 1))
        assert act_e33 == exp_e33

        map_e51, surv_e51 = eight_sector_e51_injection(h)
        e51_cancelled += len(map_e51)
        e51_survivors += len(surv_e51)
        w_e51 = Counter(tableaux.inv_g(h, t) for _, t in surv_e51)
        exp_e51 = tableaux.elementary_expansion(h).get((5, 1), ())
        act_e51 = tableaux.trim(w_e51[i] for i in range(max(w_e51, default=-1) + 1))
        assert act_e51 == exp_e51

    return {
        "status": "passed",
        "n5_hessenberg_vectors": six_sector_checked,
        "phi221_tableaux_checked": phi221_checked,
        "phi221_3d_promoted_witnesses": phi221_promoted,
        "six_sector_e41_negative_tableaux_cancelled": total_negative_cancelled,
        "six_sector_e41_positive_survivors": total_survivors,
        "n6_hessenberg_vectors": n6_hessenberg_checked,
        "phi2211_tableaux_checked": phi2211_checked,
        "phi2211_3d_promoted_witnesses": phi2211_promoted,
        "six_sector_e33_negative_tableaux_cancelled": e33_cancelled,
        "six_sector_e33_positive_survivors": e33_survivors,
        "eight_sector_e51_negative_tableaux_cancelled": e51_cancelled,
        "eight_sector_e51_positive_survivors": e51_survivors,
        "beta_rearrangement_bijection": beta_summary,
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
