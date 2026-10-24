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
    return {
        "status": "passed",
        "n5_hessenberg_vectors": six_sector_checked,
        "phi221_tableaux_checked": phi221_checked,
        "phi221_3d_promoted_witnesses": phi221_promoted,
        "six_sector_e41_negative_tableaux_cancelled": total_negative_cancelled,
        "six_sector_e41_positive_survivors": total_survivors,
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
