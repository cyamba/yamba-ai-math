from itertools import permutations
import helpers as hp

lam = (4, 1, 0, 0, 0)
for beta in sorted(set(permutations(lam)), reverse=True):
    keys = [beta[j] - j for j in range(5)]
    if len(set(keys)) == 5:
        # Sort keys descending
        order = sorted(range(5), key=lambda j: keys[j], reverse=True)
        cols = tuple(keys[order[i]] + i for i in range(5))
        shape = hp.conjugate(tuple(c for c in cols if c > 0))
        invs = sum(order[i] > order[j] for i in range(5) for j in range(i+1, 5))
        sign = (-1) ** invs
        print(f"beta={beta}  keys={keys}  cols={cols}  shape={str(shape):12s}  sigma={tuple(order)}  sign={sign:+d}")
