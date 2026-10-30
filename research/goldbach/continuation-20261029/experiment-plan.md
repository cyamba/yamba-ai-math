# Preregistered finite checks

Date: 29 October 2026. Role: independent experimenter. Status at registration: no final evaluation run. The checks target algebra and edge cases; they do not test Goldbach at unbounded size or establish an unspecified asymptotic constant.

## Primary comparisons

1. Compute U, L, H and R independently from exact prime factorizations for every even 6 <= N <= 20,000, at alpha = 3/10, 8/25 and 33/100. Check R=(U-L)/2-H. Count repeated factors, cubes and possible higher-factor survivors. Cross-check every even N <= 200 using separate trial division. Thresholds are integer roots of N raised to the rational numerator, with exact integer comparisons. There are no floating-point cutoff decisions.
2. Check the moving-endpoint divisor swap at every integer 4 <= N <= 160 and eta in {3/2,2,7/3,5/2}. Expand products of prime logarithms into formal monomial coefficient maps, giving an exact integer comparison. Ablation: remove the moving endpoint and preserve the first nonzero formal discrepancy.
3. Check the endpoint Abel estimate numerically on deterministic signed integer sequences, using seed 20261029, every 6 <= N <= 90, eta in the same set, and every admitted coprime modulus. Record numerical tolerance, maximal ratio and any failures separately from the exact integer comparisons.

Include the proposed sharpness witness N=10, k=3, eta=2, f(1)=f(8)=1. Check its full discrepancy vanishes and its moving discrepancy attains the stated bound. Include cube witnesses p=3, q=r^3 for r in {3,5,7,11,13,17,19,23}, with epsilon=1/N, checking r>N^(1/3-1/N) by exact powers. These illustrations test the need for a lower-scale remainder when epsilon moves with N.

## Metrics and decision rules

Any exact-identity discrepancy refutes the implementation or the stated finite identity and must be preserved. For the Abel comparison, fail if excess exceeds 1e-10 times max(1,bound). A successful finite run supplies no infinite theorem. Record an empirical contamination ratio using the proposed normalized scale and a truncated singular-series product; its absolute constant is unspecified and the finite maximum cannot verify a universal inequality.

## Resource boundary and artifacts

Use standard-library Python, deterministic data, no provider calls, and the fixed ranges above. Save Python/platform identification, wall time, source SHA256, ranges, counts, worst cases and failures in finite-results.json. Preserve all failures before raising an error. A smoke run uses the same code at smaller bounds, then a fresh full run overwrites only the owned finite-results.json with the final record. Host inference tokens and monetary cost are unknown. Run only after the statement and endpoint artifacts are available and the dependent packet is supplied.
