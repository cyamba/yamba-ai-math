# Independent review of two local constructions

## Residue lane carries

**Verdict: supported on the stated domain; no global product-to-gap map follows.** The six nonzero non-3-divisible residue classes split into the three pairs ±1, ±2, ±4; together with ±3 they comprise the eight nonzero classes. If `n≡±2` and n is even, then n/2≡±1 mod 9. If `n≡±4` and n is divisible by 4, then n/4≡±1. Thus all present lane parts have unique parents, and the residue pairs are disjoint. Euclidean division of each multiplicity by 4 uniquely gives q,d,e, preserving `m_s s=(4q+2d+e)s`. The unrestricted ±3 lane is unchanged. These facts prove both inverse identities for finite partitions.

For the general split collisions with admissible `4|s`, `7s/2` and `5s/4` are both positive integers in the ±1 source lanes: modulo 9, `7/2≡5/4≡8≡−1`. In each example, the comparator's two-bit carry yields the same two output parts, while it has no 4-lane pair eligible for a repair. The `(4s,4s)` branch fails the equal-adjacent sum condition because s is not divisible by 3. These are counterexamples only to the specifically described unchanged-context, uncolored, proportional operations.

For a pair of multiplicities, writing `m_s=rq+d` shows directly that `T_r(rq+d,m)=(rm+d,q)` and applying the same rule again returns `(rq+d,m)`; weight is preserved. Every ±1 source value belongs to a unique chain `8^k u` with u not divisible by 8 and is paired by even/odd k. Every ±3 source value has a unique odd root under powers of 2 and is paired similarly. These disjoint pairs stay in B, so simultaneous operations form a finite-support involution. The normalization impossibility at pair weight rs follows because `(r,0)` and `(0,1)` have the same weight and exactly one pair of nonnegative output multiplicities with lower count <r has that weight.

The bounded script ran successfully on 5,461 objects through weight 40 and the listed collisions. This check is not the proof. Reviewed SHA-256: `lane_carries.md` `9f443cad2cc7b7aa3e0669027cc1d36fc37a30dc99ed8e003d7da4f16eb43c4c`; script `ac0167bdafa3d33b2227a84145c154ba894016f5284757acf68194e68fdaa6d9`.

## Local surgery

**Verdict: supported for nonnegative integer triples and labeled output branches; incomplete as a global KR1 construction.** Fix bidegree (X,Y). The input coordinate c runs through every integer `0≤c≤min(floor(X/2),Y)`. Type 0 is in bijection with the parity progression `f≡X (mod 2)`, `0≤f≤min(X,Y)`, and type 1 is in bijection with `g≡X−1−Y (mod 2)`, `0≤g≤min(Y,X−1−Y)`. In type 1 the bound may be negative, in which case the progression is empty. The first progression has p entries, so the forward map sends c<p to its c-th member and c≥p to the (c−p)-th member of the second. Inverse formulas recover that index and then a=X−2c, b=Y−c.

The number of outputs equals the number of inputs in all parameter regimes: for Y≥X, all inputs go to type 0; for Y≤floor(X/2), both progressions are bounded by Y and their parity counts sum to Y+1 (opposite parities when Y is even, equally many of each parity when Y is odd); in the intermediate regime their lengths add to `floor(X/2)+1`. These cases include empty progressions and p=0. The two exponents are unchanged, and specialization `x=q^(9j+2)`, `y=q^(9k+3)` yields the displayed species. Branch markers and context labels must be retained to make the local inverse meaningful where different operations share species.

The script completed its stated 27,000 source cases and bounded output cases. **Implementation limitation:** `forward` and `backward` test nonnegativity but do not strictly validate integer types; floating values and Boolean values are outside the mathematical domain but can pass the input checks. Callers must enforce nonnegative integer inputs if the functions are used as a public API. This does not invalidate the theorem on its stated domain. Reviewed SHA-256: `local_surgery.md` `2712b7f1137e0eb9498377f31483f8967c5fa00dbfc340c4cbdda490fd8134cd`; script `b0ecccc30e440172872653f4c064e48d0c0b6e137fe17047173846cfe1bc0a67`.

## Generic cancellation certificate

`lean/Cancellation.lean` defines finite ordered lists of `(Bool,Nat)` cells, scans from the left for the first nonzero cell, and toggles one marker against one gap unit there. Lean 4.34.0 checks involution, preservation of `Σh(η_h+δ_h)` from any starting coefficient, preservation of the requested `9h` weight, marker-parity reversal when any cell is eligible, and equivalence between fixed points and every cell being `(false,0)`. This supplies the cancellation only: a proposed flattening must separately establish that the coordinates and markers are valid, recoverable, and have these weights. The Lean output reports `[propext]` for the toggle/involution/parity/fixed Boolean theorems and `[propext, Quot.sound]` for the weighted and explicit all-zero theorems; no `sorryAx`. Command:

```
/tmp/lean-4.34.0-linux/bin/lean research/rogers-ramanujan/terra2026/lean/Cancellation.lean
```

Exit 0. SHA-256 `baa9fb7874c5fec739631ab3137dee59e36d1c3befc7c635a41be3002685c2a5`.
