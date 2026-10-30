---
id: ETH-A02
source: YAMBA-378-02; preprint Sec. 2.6 Step 2, Lemmas "swaps-matrix" and "swaps-support"
category: algebraic-core
status: open (formalisation)
---

# ETH-A02: Commuting-swap algebra and support localisation

## Statement

Let `Pi_1, ..., Pi_Q` be commuting involutions (`Pi_s^2 = I`) in a commutative `Q`-algebra, `V_0 = prod_s Pi_s`,
`W_0 = (1/2) sum_s (I - Pi_s)`. For every polynomial `f` of degree `<= R-1`,

`V_0 f(W_0) = sum_{S subset [Q], |S| <= R-1} gamma_S prod_{s not in S} Pi_s`  for some rationals `gamma_S`.

Consequently, in the coordinate space `B = ([r] x [r])^Q` with `Pi_s` the swap of pair `s`, an entry
`M_0[u,w]` can be nonzero only if `a_w(s) = d_u(s)` for all but at most `R-1` positions `s`.

Also: `C(W_0, j) = sum_{|J| = j} prod_{t in J} (I - Pi_t)/2` (the elementary symmetric functions of the
commuting idempotents), and `V_0 = sum_j (-2)^j C(W_0, j)`.

## Known

**Established** in the preprint (proved there). The second identity is the operator version of
`(1 - 2)^W = sum_j (-2)^j C(W, j)` applied to the idempotents `P_t = (I - Pi_t)/2`; it holds because
`prod_t (I - 2 P_t) = sum_J (-2)^{|J|} prod_{t in J} P_t` and products of commuting idempotents over a set `J`
are the elementary symmetric terms.

## Formalisation plan (Lean)

1. Work in an arbitrary `CommRing A` with `P : Fin Q -> A`, `P t * P t = P t`. Prove
   `prod_t (1 - 2 P t) = sum_{J : Finset (Fin Q)} (-2)^{|J|} prod_{t in J} P t` (`Finset.prod_one_add` style,
   `Finset.prod_add`).
2. Prove `W^j` lies in the span of `{prod_{t in J} P t : |J| <= j}` (induction on `j`, idempotence).
3. Multiply by `V_0 = prod (1 - 2 P t)`; use `(1 - 2P)P = -P` to get `V_0 prod_{t in J} P_t = (-1)^{|J|}
   prod_{t in J} P_t`, and expand `prod_{t in J} P_t = 2^{-|J|} prod_{t in J}(1 - Pi_t)` to read off
   that only products missing at most `|J|` swaps from `V_0` appear.

Mathlib pieces: `Finset.prod_add`, `Finset.prod_sub_ordered`, `Submodule.span`, `Algebra.adjoin`.

## Why it matters

This is the exact algebraic interface that [ETH-B03](../B-exponent-frontier/ETH-B03-polynomial-row-routing.md)
wants to break: everything in the span above is diagonal in one common eigenbasis, which is what makes the
Smolensky barrier of [ETH-B01](../B-exponent-frontier/ETH-B01-sqrt-log-barrier.md) apply.
