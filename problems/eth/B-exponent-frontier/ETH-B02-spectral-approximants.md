---
id: ETH-B02
source: YAMBA-378-06 ("Sharpening the exponent via Chebyshev / Pade spectral approximants")
category: exponent-frontier
status: answered negatively inside the commutative algebra; rounding variant open but blocked
---

# ETH-B02: Spectral approximants for `f(W)`

## Sheet question

Replace the interval interpolant `f(j) = (-1)^j` on `I = [a, a+b]` by a Chebyshev/Zolotarev, multi-node Pade,
or Krawtchouk-optimal approximant, possibly allowing a small error `|1 - (-1)^j f(j)| <= delta` on `I` and
rounding `H(0)` to the nearest integer at the end.

## Answer

1. **Exact versions: no gain (proved).** Any such `f` gives `M_0 = V_0 f(W_0)`, an element of the commuting
   swap algebra. By [ETH-B01](ETH-B01-sqrt-log-barrier.md) every element of that algebra needs degree
   `R >= c sqrt(Q log(1/eps))` to fix a `1 - eps` fraction of directions, and the interval interpolant already
   achieves `R = O(sqrt(Q log(1/eps)))`. Even non-symmetric (non-polynomial-in-`W_0`) choices of `gamma_S`
   cannot do better.
2. **Approximate versions: blocked by the algorithm's structure (unverified analysis).** An approximate
   `M_0` with `M_0 xi ~ xi` on `ker C` breaks the identity `<P_u(0), zeta> = zeta_u` only by a small rational
   error per occurrence, but `H` is a product of `Theta(n)` clause polynomials evaluated on these forms, so
   per-factor relative errors `delta` compound to `(1 + delta)^{Theta(n)}` and to absolute errors far above
   `1/2` unless `delta <= 1/n`. Since `log(1/delta) ~ log n` is already the regime of the paper
   (`log(1/eps) ~ log log n` to `log n`), the rounding idea does not change the degree requirement. A careful
   proof of this "no rounding gain" statement is a small open item.

## Remaining open item

State and prove a quantitative version of 2 (error propagation through the product of clause polynomials
and through Hermite weights, which themselves have size `exp(O(QJ log Q))`).
