---
id: ETH-A05
source: YAMBA-378-05 (Minc permanent jet identity); preprint Lemma "boolean-differences"
category: algebraic-core
status: open
---

# ETH-A05: Bounded-scope Taylor extraction

## Statement (corrected)

The sheet attributes the Taylor step to Minc's permanent expansion. The preprint instead uses: every entry of
`Delta P_{e,v}(z) = P_{e,v}(t+z) - P_{e,v}(t)` is divisible by `z`, so `[z^j] G_x(X, z)` has degree `<= j` in
the formal vector `X`, and the order-`<J` jet of `sum_x G_x(x, z)` is a signed sum of `sum_{|E| <= q} 2^{|E|}`
restricted sums with `X` fixed to indicators (see [ETH-A06](ETH-A06-boolean-differences.md)).

Minc's formula `per(X + Y) = sum_k sum_{|I|=|K|=k} per(Y[I,K]) per(X[I^c,K^c])` gives the same truncation
for permanents: if every entry of `Y` is divisible by `u`, terms with `k >= J` vanish mod `u^J`.

## Problems

1. **Lean**: prove the degree truncation `deg_X [z^j] G <= j` for products of polynomials in linear forms
   whose `z`-parts are divisible by `z` (MvPolynomial over `Polynomial`).
2. **Lean**: Minc's expansion for `Matrix.permanent` and its `u^J` truncation. Mathlib has
   `Matrix.permanent`; the expansion is not there (checked in this Mathlib revision by name search only, so
   novelty of a formal proof is NOT VERIFIED).
3. **Cost question**: the Taylor-data factor `sum_{j <= q} 2^j C(n,j)` dominates the exponent in the paper's
   template. Can the `2^{|E|}` inclusion-exclusion be replaced by `O(1)` evaluations per `E` (for instance with
   `X` set to a generic point of a small field extension, as in Hasse-derivative decoding)? This would not
   change the exponent order but would change constants; the order is controlled by `q ~ nR/Q`,
   see [ETH-B01](../B-exponent-frontier/ETH-B01-sqrt-log-barrier.md).
