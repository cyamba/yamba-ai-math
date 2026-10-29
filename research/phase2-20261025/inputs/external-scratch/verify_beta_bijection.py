from itertools import permutations
import test_djt_3d as td
import helpers as hp

# Let's check the bijection between DJT sectors (shape, sigma) for lam and rearrangements beta of (lam_1, ..., lam_k, 0, ..., 0)!
for n in range(2, 7):
    for lam in hp.partitions(n):
        # 1. Sectors from DJT
        djt_secs = []
        for shape in hp.partitions(n):
            cols = tuple(sum(x > j for x in shape) for j in range(shape[0]))
            for sigma in permutations(range(len(cols))):
                alpha = tuple(cols[i] - i + sigma[i] for i in range(len(cols)))
                if any(x < 0 for x in alpha):
                    continue
                if tuple(sorted((x for x in alpha if x > 0), reverse=True)) != lam:
                    continue
                # Pad cols, sigma, alpha to length n
                cols_pad = cols + (0,) * (n - len(cols))
                sigma_pad = sigma + tuple(range(len(cols), n))
                alpha_pad = alpha + (0,) * (n - len(cols))
                beta = [0] * n
                for i in range(n):
                    beta[sigma_pad[i]] = alpha_pad[i]
                djt_secs.append((shape, sigma_pad, tuple(beta)))
        
        # 2. Rearrangements beta of lam + (0,)*(n - len(lam)) with distinct beta_j - j
        padded_lam = lam + (0,) * (n - len(lam))
        distinct_betas = sorted(set(permutations(padded_lam)))
        valid_betas = []
        for beta in distinct_betas:
            keys = [beta[j] - j for j in range(n)]
            if len(set(keys)) == n:
                valid_betas.append(beta)
        assert len(djt_secs) == len(valid_betas), f"Mismatch at n={n}, lam={lam}: {len(djt_secs)} vs {len(valid_betas)}"
        assert sorted(x[2] for x in djt_secs) == sorted(valid_betas)
print("100% EXACT BIJECTION VERIFIED FOR ALL n=2..6 AND ALL PARTITIONS lam!")
