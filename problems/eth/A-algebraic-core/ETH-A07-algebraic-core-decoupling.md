---
id: ETH-A07
source: YMB-ETH-01; openai/math lean/OAI/Algorithms/SubexponentialSAT
category: algebraic-core
status: open (large formalisation)
---

# ETH-A07: Decouple the algebraic core from the machine model

## Goal

State and prove, in Mathlib-only Lean (no Turing machine), the *counting identity* behind the algorithm:

> For a bounded-occurrence 3-CNF `F` on `Fin n`, there are explicitly constructed rational linear forms,
> groups and integer measurement matrices such that `#F` equals an explicit rational linear combination of
> `prod_g B_{t,g}(y)` sums over measurement tuples `y`, with the number of terms bounded by
> `2^{O(n (log log n)^2 / sqrt(log n))}`.

The OpenAI development already proves the end-to-end statement for a `PrimitiveMachine`; the point here is a
reusable algebraic theorem that other problems (weighted counting, Max-SAT histograms, Ising sums) can call.

## Plan

1. Identity layer: `H(0) = #F` (trivial), separation identity (Lemma "measurement-separation"), Taylor layer
   ([ETH-A06](ETH-A06-boolean-differences.md)), Hermite layer ([ETH-A04](ETH-A04-hermite-recovery.md)).
2. Construction layer: swap algebra ([ETH-A02](ETH-A02-swap-algebra-support.md), [ETH-A03](ETH-A03-swap-eigenbasis.md)),
   parity interpolant ([ETH-A01](ETH-A01-parity-interpolant.md), done), schedules by conditional expectation.
3. Counting layer: bound the number of summands, not bit operations.

Inspect `openai/math/lean/OAI/Algorithms/SubexponentialSAT` first and reuse definitions where licensing allows
(openai/math is Apache-2.0; keep its notice on anything copied).

## Known from the sheet (kept)

The deformation `Z_F(t) = sum_x prod_C (1 + t(Phi_C(x) - 1))` with `Z_F(1) = #F` is proved in
[DeformedSum.lean](../lean/EthProblems/DeformedSum.lean). Note it is *not* the paper's deformation (the paper
deforms clause *inputs*, not clause values); it is still the right object for Max-SAT histograms
([ETH-C05](../C-counting-extensions/ETH-C05-maxsat-histogram.md)).
