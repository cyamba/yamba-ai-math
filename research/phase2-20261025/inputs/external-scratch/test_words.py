import test_djt_3d as td

h_total = (1, 2, 3, 4, 5)
states = td.get_djt_states(h_total, (4, 1))
by_word = td.defaultdict(list)
for sh, cols, sig, alpha, sgn, inv, t in states:
    w = tuple(x for row in t for x in row)
    by_word[w].append((sh, sgn, alpha, t))

print("=== GROUPED BY ROW-MAJOR WORD w(T) ===")
for w, items in sorted(by_word.items()):
    net = sum(x[1] for x in items)
    print(f"Word {w}: net_sign={net:+d}, count={len(items)}")
    for sh, sgn, alpha, t in items:
        print(f"   {sgn:+d} shape={str(sh):12s} alpha={str(alpha):15s} T={t}")
