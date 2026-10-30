---
id: ETH-C03
source: new (this program), prompted by YMB-ETH-07 and preprint Cor. 1.1
category: counting-extensions
status: open
---

# ETH-C03: Exact Max-k-SAT for superlinear `m`

## Question

Is there a `2^{o(n)} poly(m)` algorithm for **exact** Max-3-SAT (or the full histogram `h_j = #{x : x violates
exactly j clauses}`) when `m` is superlinear in `n`?

## What is known

* Preprint Cor. 1.1: `OPT - eps m` in `2^{O_eps(rho(n))}` (sample `O(n/eps^2)` clauses, threshold circuit).
* Bounded density `m <= Dn`: the histogram is computable in `2^{O_{k,D}(rho(n))}`, proof sketch in
  [ETH-C05](ETH-C05-maxsat-histogram.md).
* Dense case: a threshold circuit on all `m` clauses introduces `Theta(m)` gate variables, so Theorem 1 gives
  only `2^{o(m)}`.

## Ideas

1. **Mod-`2^l` route.** For odd `t = 1 + 2s`, `prod_e (1 + 2 s v_e(x)) = (1+2s)^{u(x)}` (`u` = violations),
   and terms with `>= l` factors `2 s v_e` vanish mod `2^l`, so the truncated product has degree `k(l-1)`.
   This yields the binomial moments `N_i = sum_x C(u(x), i)` modulo `2^{l-i}` for `i < l`. With
   `l = O(n)` we get `N_i` exactly for `i <~ n / log m`. Does knowing `N_0, ..., N_{n / log m}` decide whether
   `min_x u(x) <= j` for small `j`? (Note `N_i` for `i > max u` vanish; for near-satisfiable formulas the
   small moments determine everything.) Gives an exact algorithm for Max-SAT when
   `m - OPT <= c n / log m` (to be verified).
2. **Sparsification for Max-SAT.** Is there a disjoint, histogram-preserving sparsification? Standard
   sparsification only partitions *satisfying* assignments.
3. **Lower-bound side.** Is dense exact Max-3-SAT "harder" in a fine-grained sense (e.g. reduces from a
   problem believed to need `2^{(1-o(1)) n}` such as Max-CSP with large arity)?
