---
id: ETH-B05
source: YMB-ETH-06 ("UW-SETH phase transition")
category: exponent-frontier
status: open
---

# ETH-B05: How large can the clause width `k(n)` grow?

## Question

Theorem 1 hides the `k` dependence in `O_k`. Find explicit `C_k` with time `poly 2^{C_k n log log n / sqrt(log n)}`
and determine the largest `k(n)` for which `k(n)`-SAT stays in `2^{o(n)}`. CNF-SAT with unbounded width
(the hypothesis used by Bringmann, Roditty-Vassilevska Williams, Lokshtanov-Marx-Saurabh, preprint Sec. 1.1.3)
is untouched only if `k(n)` must stay small.

## Known pieces

* Sparsification: `B = O_k((sigma^{-1} log(2/sigma))^{k-1})` occurrences per variable, constants
  `2^{O(k log k)}`-type in the Calabro-Impagliazzo-Paturi analysis (to be checked against the cited thesis).
* OR-gadget conversion: `O(k)` gates per clause, so `N = O_k(B n)` variables after copying.
* Exponent `O(sigma n + B rho(n))` with `rho(n) = n (log log n)^2 / sqrt(log n)` on the interpolation route.

## Heuristic target (unverified)

With `B ~ (k/sigma)^{k}` the optimum `sigma` satisfies `sigma ~ (k/sigma)^k rho(n)/n`, giving subexponential
time while `k log k <~ c log log n`, i.e. `k(n) = Theta(log log n / log log log n)`. Width `k = Theta(log n)`
(where CNF-SAT on `n` variables is as hard as general CNF-SAT with `poly(n)` clauses) is far outside.
The sheet's threshold `k(n) <= ((1-eps)/c) log_2 log_2 n` is of the same flavour; make it precise.

## Tasks

1. Track `k` through the preprint's Lemma "sparsify" and Prop. "interpolation-bound"; produce explicit
   `C_k`.
2. Decide whether a width-adaptive algorithm (sparsify only to bounded degree, never to bounded width) does
   better.
3. Lean (stretch): `(log log n)`-width SAT in `2^{o(n)}` as a corollary of an explicit-constant Theorem 1.
