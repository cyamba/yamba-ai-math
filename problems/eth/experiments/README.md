# Experiments of the `eth` set

Exact computations behind the subresults. Every script uses exact rational arithmetic (or
modular arithmetic re-checked exactly) for any claim that enters a subresult; floating point is
used only inside solvers whose answers are then re-verified. Results are written to
[`results/`](results/).

| Script | What it computes | Used by | Results |
| --- | --- | --- | --- |
| [`cube_polynomial.py`](cube_polynomial.py) | Optima of the cube polynomial problem CP(Q, R) by mixed-integer programming (scipy/HiGHS), the subcube-hitting relaxation, and the slab and window families, with exact re-checks of every good-edge set | [SR-02](../subresults/SR-02-cube-polynomial-designs.md), [SR-04](../subresults/SR-04-slab-construction.md) | `cube_polynomial.jsonl` (one line per instance), `cube_polynomial.json` |
| [`subcube_system.py`](subcube_system.py) | Exact comparison of the subcube-identity criterion of SR-11 with the polynomial system, and reweighted $\ell_1$ relaxations of the subcube system | [SR-11](../subresults/SR-11-subcube-identities-characterize-defects.md) | `subcube_system.json` |
| [`matrix_validation.py`](matrix_validation.py) | Builds the actual swap-algebra matrices $P(T)$ for small $(r,Q,R)$ and checks the predicted ranks of the nonlocal parts modulo two primes | [SR-02](../subresults/SR-02-cube-polynomial-designs.md), [SR-03](../subresults/SR-03-point-dependent-rank-barrier.md) | `matrix_validation.json` |
| [`hermite_weights.py`](hermite_weights.py) | Closed-form Hermite weights against linear algebra, and their denominators | [ETH-B04](../02-algebraic-identities/ETH-B04-hermite-weights-and-bit-lengths.md) | `hermite_weights.json` |
| [`galactic_thresholds.py`](galactic_thresholds.py) | The preprint's cost bound with exact binomial tails, for its explicit parameters and optimized ones | [SR-06](../subresults/SR-06-galactic-thresholds.md) | `galactic_thresholds.json` |

Reproduce (Python 3.11+, numpy and scipy):

```sh
cd problems/eth/experiments
python3 cube_polynomial.py --min-q 2 --max-q 6 --time-limit 240 \
    --log results/cube_polynomial.jsonl --out results/cube_polynomial.json
python3 matrix_validation.py
python3 subcube_system.py --out results/subcube_system.json
python3 hermite_weights.py
python3 galactic_thresholds.py --out results/galactic_thresholds.json
```

The MILP stops proving optimality at $Q=6$ within 240 s per instance; entries that hit the time
limit are reported as upper bounds with the solver's proven lower bound.
