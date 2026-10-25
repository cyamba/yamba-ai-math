from __future__ import annotations
from collections import Counter, defaultdict
from itertools import permutations
import helpers as hp

def conjugate(shape: tuple[int, ...]) -> tuple[int, ...]:
    if not shape:
        return ()
    return tuple(sum(1 for r in shape if r > j) for j in range(shape[0]))

def test_djt_involution(n: int, h: tuple[int, ...], lam: tuple[int, ...]):
    lam_pad = lam + (0,) * (n - len(lam))
    distinct_betas = sorted(set(permutations(lam_pad)))
    
    states = []
    for beta in distinct_betas:
        kappas = [beta[j] - j for j in range(n)]
        if len(set(kappas)) < n:
            continue
        order = sorted(range(n), key=lambda j: kappas[j], reverse=True)
        mu_conj = tuple(kappas[order[i]] + i for i in range(n))
        if any(c < 0 for c in mu_conj):
            continue
        mu_conj_pos = tuple(c for c in mu_conj if c > 0)
        mu = conjugate(mu_conj_pos)
        inv_count = sum(1 for a in range(n) for b in range(a + 1, n) if order[a] > order[b])
        sign = -1 if (inv_count % 2) else 1
        
        for tab in hp.tableaux(h, mu):
            inv_val = hp.inv_g(h, tab)
            word = tuple(u for row in tab for u in row)
            states.append({
                "beta": beta,
                "mu": mu,
                "sign": sign,
                "tab": tab,
                "word": word,
                "inv": inv_val,
            })
    return states

for h_name, h in [
    ("Total order (1,2,3,4,5)", (1,2,3,4,5)),
    ("Connected height-2 (3,4,4,5,5)", (3,4,4,5,5)),
    ("Height-3 (2,3,5,5,5)", (2,3,5,5,5))
]:
    states = test_djt_involution(5, h, (4, 1))
    pos_by_inv = defaultdict(list)
    neg_by_inv = defaultdict(list)
    for s in states:
        if s["sign"] > 0:
            pos_by_inv[s["inv"]].append(s)
        else:
            neg_by_inv[s["inv"]].append(s)
    print(f"=== {h_name}: total states = {len(states)} ===")
    all_invs = sorted(set(pos_by_inv.keys()) | set(neg_by_inv.keys()))
    for k in all_invs:
        print(f"  q^{k}: +{len(pos_by_inv[k])} - {len(neg_by_inv[k])} = {len(pos_by_inv[k]) - len(neg_by_inv[k])}")
        pos_words = Counter(s["word"] for s in pos_by_inv[k])
        neg_words = Counter(s["word"] for s in neg_by_inv[k])
        common_words = sum((pos_words & neg_words).values())
        print(f"    Same-word reblocking pairs: {common_words} / {len(neg_by_inv[k])} negatives")
        p_used = [False] * len(pos_by_inv[k])
        n_used = [False] * len(neg_by_inv[k])
        for ni, ns in enumerate(neg_by_inv[k]):
            for pi, ps in enumerate(pos_by_inv[k]):
                if not p_used[pi] and ps["word"] == ns["word"]:
                    p_used[pi] = True
                    n_used[ni] = True
                    break
        unpaired_neg = [neg_by_inv[k][ni] for ni in range(len(neg_by_inv[k])) if not n_used[ni]]
        unpaired_pos = [pos_by_inv[k][pi] for pi in range(len(pos_by_inv[k])) if not p_used[pi]]
        if unpaired_neg:
            print("    Unpaired Negatives after same-word reblocking:")
            for s in unpaired_neg:
                print(f"      beta={s['beta']} mu={s['mu']} tab={s['tab']} word={s['word']}")
            print("    Available Positives after same-word reblocking:")
            for s in unpaired_pos:
                print(f"      beta={s['beta']} mu={s['mu']} tab={s['tab']} word={s['word']}")
