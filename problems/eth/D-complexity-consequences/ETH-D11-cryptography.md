---
id: ETH-D11
source: sheet "10 consequences" item 10; sheet "Refuting ETH" consequence 9; preprint Appendix F.2
category: complexity-consequences
status: audited
---

# ETH-D11: Local PRGs, MQ and parameter scaling

* **Established in the preprint.** Inverting any constant-locality map `G : {0,1}^n -> {0,1}^m` and counting
  preimages in `(n+m)^{O_d(1)} 2^{O_d(rho(n))}` (Cor. F.2), covering Goldreich's candidate one-way functions.
  This rules out `2^{Omega(n)}` inversion hardness, not polynomial-time one-wayness.
* **Correct in kind.** AES, SHA-3, lattice schemes: CNF encodings have unbounded width or `N >> key length`
  variables; no practical impact.
* **Corrected numbers.** The sheet's re-parameterisation `n = Theta(lambda log lambda)` assumes a
  `2^{n / log n}` attack. With `2^{c n / sqrt(log n)}` (up to `log log`), security `2^lambda` needs
  `n >~ lambda sqrt(log lambda)` for schemes whose security reduction is a linear-variable 3-SAT encoding.
  Multivariate quadratic systems over `F_2` are degree-2 equations, i.e. the preprint's sparse-polynomial
  setting only when each equation has polylogarithmically many monomials (Theorem "sparse polynomials").
  Dense MQ is outside.

## Open

Concrete security estimates for local PRGs with output stretch `n^{1+eps}` at `n` in the thousands, using the
explicit constants of [ETH-B06](../B-exponent-frontier/ETH-B06-crossover-constant.md). Expectation: no
practical effect, since the asymptotics start at astronomically large `n`.
