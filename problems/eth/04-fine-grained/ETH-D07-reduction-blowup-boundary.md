# ETH-D07. The reduction-blowup boundary: why NP ⊆ SUBEXP does not follow

| Field | Value |
| --- | --- |
| Category | Fine-grained complexity |
| Source items | "The sharp structural boundary: why P ≠ NP and NP ⊆ SUBEXP remain open"; "superlinear reduction barrier" |
| Status | **Open**, with one reported follow-up to inspect |
| Depends on the upstream theorem | Yes |
| Score (I/B/T/L/Lean) | 4 / 3 / 2 / 3 / 1, composite **2.9** |
| Subresults | [SR-09](../subresults/SR-09-coverage-map.md) |

## Statement

A $2^{o(n)}$ algorithm transfers only through reductions with $O(n)$ variables. Cook–Levin style
reductions from $\mathrm{NTIME}(T)$ produce 3-CNFs with $T\,\mathrm{polylog}(T)$ variables (Jahanjou,
Miles, Viola, ICALP 2015), so a 3-SAT exponent $N/(\log N)^{1/2+o(1)}$ gives
$\mathrm{NTIME}(T)\subseteq\mathrm{DTIME}(2^{T\,\mathrm{polylog}(T)/\sqrt{\log T}})$, which is
subexponential in $T$ only if the polylog factor is below $\sqrt{\log T}$. A blog post by
Fortnow (2026-10-28, level T) reports a result of Subercaseaux:
$\mathrm{NTIME}(T)\subseteq\mathrm{DTIME}(2^{O(T(\log\log T)^3/\sqrt{\log T})})$. To inspect.

## Tasks

1. Inspect and record the Subercaseaux result and its reduction overhead.
2. State the exact "blowup exponent" condition: which reduction size $T\,g(T)$ keeps the
   simulation subexponential, as a function of the 3-SAT exponent $n/(\log n)^{\alpha}$.
3. Consequences for circuit lower bounds through Williams's connection
   ([ETH-E01](../05-circuits-proofs-space/ETH-E01-circuit-lower-bounds-williams-program.md)).

## Resource boundary

One agent; literature and a short derivation.
