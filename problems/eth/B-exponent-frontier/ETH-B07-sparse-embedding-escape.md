---
id: ETH-B07
source: new (this program)
category: exponent-frontier
status: open; raised in priority (referee observation, 2026-10-30)
---

# ETH-B07: Rank savings on zero-filled coordinates

## Idea

The measurement count in the template is `r h c` where `c = rank(I - M_0)` on the full auxiliary space
`Q^B`. After the substitution step most coordinates of the `h` copies of `B` hold either an original variable
or zero. What matters for the algorithm is the rank of the measurement matrix *restricted to filled
coordinates*, `rank(C|_F)`, which can be far smaller than `c` if the filled set `F` is chosen with the spectral
structure in mind. The routing rigidity lower bound ([ETH-B01](ETH-B01-sqrt-log-barrier.md)) is proved for the
full space; it does not apply to `rank(C|_F)`.

## Questions

1. With `D >> n` auxiliary coordinates and a filled set `F` of size `O(n)` (schedules chosen so that labels
   avoid the exceptional block structure), how small can `rank(C|_F)` be? A zero-block argument still applies
   inside `F`: `rank >= |F ∩ T|` for every product block `T`. So `F` must meet all product blocks thinly; is
   that compatible with balanced groups `|S_{t,g}| <= 2n/r`?
2. The schedules `a_v, d_e` are chosen by conditional expectations to balance loads. Replace this by an
   adversarial-to-the-blocks choice (labels from a code avoiding the sets `A x D'`), and recompute the cost.

## Observation (referee pass, 2026-10-30)

The design condition in the preprint (`(r,tau,D)`-design, condition 4, and Step 4) constrains the transferred
rows only on the labels actually used, so the relevant quantity is `rank((I - M_0)[U, U])` for the used-label
set `U`. Theorem A's product blocks can miss `U` entirely: with **type-balanced** schedules (every string uses
each symbol exactly `Q/r` times, chosen uniformly so group marginals stay balanced) every `a_u` has exactly
`x_r Q` symbols in any `X` of size `x_r r`, so `T ∩ U` is empty. The barrier therefore says nothing about this
relaxation. Next step: prove a used-label rigidity bound with blocks defined by type classes over position
subsets, or construct `M_0` with `rank((I - M_0)[U,U]) << D e^{-R^2/Q}` for type-balanced `U`.

## Smallest falsifier

If every balanced labeling meets some product block `A x D'` in `>= |F| e^{-O(R^2/Q)}` coordinates, this route
is closed. Random labelings meet it in exactly that proportion, so the question is about structured labelings.
