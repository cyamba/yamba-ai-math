# Checks for the ETH program

Run from this directory (`python3 <script>`). Dependencies: `numpy`; `sympy` and `ortools` where noted.
Large intermediate arrays go to `$ETH_SCRATCH` (default `.runs/eth/`, ignored by git).

| Script | Supports | Result (2026-10-30) |
| --- | --- | --- |
| `parity_interpolant_check.py` | ETH-A01 | interval identity and telescoped defect hold; sheet formula fails in 243 cases |
| `smolensky_biased_check.py` | ETH-B01 Lemma B | exact minimum error `>=` bound for all `Q <= 4`, all `d`, five `p` |
| `routing_minrank_experiment.py` | ETH-B03 | commutative optimum vs alternating projections at four small sizes |
| `routing_minrank_lowerbound.py` (`ortools`) | ETH-B03 | certified triangular-block lower bounds (CP-SAT optimal) |
| `routing_altproj_hard.py`, `routing_rank9_probe.py` | ETH-B03 | rank-9 completion at `(3,2,2)`: `sigma_10/sigma_1 ~ 1e-14`, bounded entries (empirical) |
| `routing_rank9_structure.py`, `routing_rank9_sparsify.py` | ETH-B03 | eigen-level profile and sparsified support (129 free nonzeros) |
| `routing_exact_correction.py` (`sympy`) | ETH-B03 | no one-step correction of the commutative optimum reaches rank 9 (exact) |
| `routing_rank9_exactify.py` | ETH-B03 | rounding to small rationals failed for 16 seeds (informative failure) |
| `routing_product_set_bound.py` | ETH-B01 Theorem A | zero block verified exactly; asymptotic comparison with the swap construction |
| `polyrow_template_experiment.py` | ETH-B03 general rows | ALS heuristic; inconclusive (does not recover the known `c = 9`) |
| `template_barrier_numeric.py` | ETH-B01 Theorem B | minimised cost model stays above `log log n / sqrt(log n)` at `log2 n in {64, 256}` (slow beyond) |
