---
id: ETH-B04
source: YMB-ETH-02 ("Closing the (log log n)^2 / log n -> log log n / log n gap", exponents corrected)
category: exponent-frontier
status: closed on paper by the preprint; Lean gap open; item 2 is a top-ranked open problem
---

# ETH-B04: The extra `log log n` factor

## Corrected statement

The Lean development proves `2^{O_k(n (log log n)^2 / sqrt(log n))}`; the preprint's Theorem 1 proves
`2^{O_k(n log log n / sqrt(log n))}` (and `n / sqrt(log n)` for bounded density) by a different route, the
recursive tensor-contraction appendix with a Cauchy deformation `W_xy(T) = C(T) / (C'(0) (T - (y-x)))`.

The sheet's diagnosis (stop sparsification early at degree `Theta(log n / log log n)`) does not match the
preprint, whose interpolation-route loss comes from `(R/Q) log(Q/R)` with `R/Q ~ (log log n)/sqrt(log n)`.

## Problems

1. **(Lean.)** Formalise the tensor-contraction route, or at least its parameter choice, to bring the
   machine-checked exponent to `n log log n / sqrt(log n)`.
2. **(Top-ranked: which assumption does the tensor route escape?)** By [ETH-B01](ETH-B01-sqrt-log-barrier.md)
   the interpolation template cannot beat `rho(n) = n (log log n)^2 / sqrt(log n)`, yet the tensor-contraction
   route reaches `n log log n / sqrt(log n)` (and `n / sqrt(log n)` at bounded density). In the tensor route,
   `H = s / floor(sqrt(lambda))` leaves and packets of `L = 2^a` slots with labels in `[r]^a` (`r = 64`) play
   roles similar to groups and nodes, but the deformation is Cauchy, `W_xy(T) = C(T) / (C'(0)(T - (y-x)))`, the
   procedure recurses, and interpolation points are lifts of residue-field elements. Determine which template
   assumption fails (degree budget, routing support, measurement accounting or recovery cost), formulate a
   common "routing design" abstraction, and check whether that mechanism can be pushed below `sqrt(log n)`.
3. **(Bounded density.)** Is `n / sqrt(log n)` (no `log log`) achievable for general `m` by better
   sparsification bookkeeping? The leaf count is `2^{sigma n}` with `B = O_k((sigma^{-1} log(2/sigma))^{k-1})`.
