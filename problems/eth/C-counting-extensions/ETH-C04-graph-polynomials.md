---
id: ETH-C04
source: sheet consequences 6 and 9 ("#P-hard graph polynomials", "Ising, Potts, hard-core")
category: counting-extensions
status: partly sketched
---

# ETH-C04: Ising, Potts, Tutte and chromatic evaluations

## Established in the preprint (Cor. 1.2)

Independent sets, proper `q`-colourings (fixed `q`) and perfect matchings counted in `2^{o(v)}` (resp.
`2^{o(v+e)}`) deterministic time and polynomial space.

## Proof sketch: weighted spin systems on bounded-degree graphs

For a graph of maximum degree `Delta` and rational couplings, the partition function
`Z = sum_{sigma in [q]^V} prod_{uv} w(sigma_u, sigma_v) prod_v lambda(sigma_v)` is a sum over one-hot Boolean
encodings of products of degree-`<= 2` factor polynomials with bounded scopes (plus one-hot constraints).
Copying to bounded occurrence uses equality cycles. The interpolation algorithm computes such weighted sums
exactly (see [ETH-C01](ETH-C01-weighted-q-series.md) step 1), so `Z` is computable in
`2^{O_{q,Delta}(rho(v))}` time and polynomial space. Covers antiferromagnetic Ising, Potts, hard-core model
with rational fugacity at every temperature, including the non-uniqueness regime where approximate counting
is NP-hard (Sly; Galanis-Stefankovic-Vigoda). **Novelty: NOT VERIFIED** (likely folklore once Theorem 1 is
accepted).

## Open items

1. **Unbounded degree.** For dense graphs the factor count is `Theta(e)`; does sparsification-style
   branching work for weighted sums? (Same obstacle as [ETH-C03](ETH-C03-dense-exact-maxsat.md).)
2. **Whole polynomials.** The chromatic polynomial has degree `v`; recovering it needs colour counts up to
   `q = v`, whose one-hot encoding has `v^2` variables. Is there a `2^{o(v)}` algorithm for the full
   chromatic polynomial, or for the Tutte polynomial at a fixed non-special point on bounded-degree graphs?
   Dell, Husfeldt, Marx, Taslaman and Wahlen (2014) proved #ETH lower bounds for these; those bounds are now
   void but no algorithm follows automatically.
