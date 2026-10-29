# ETH-C01. The #ETH collapse: exact #k-SAT, sparse permanents and perfect matchings

| Field | Value |
| --- | --- |
| Category | Counting |
| Source items | "Total collapse of the IPZ sequence and #ETH"; "Counting complexity: exact #k-SAT and sparse {0,1}-permanent are subexponential" |
| Status | **Conditional consequence** of the preprint (Thm 1.1, Cor. 1.3) |
| Depends on the upstream theorem | Yes |
| Score (I/B/T/L/Lean) | 3 / 1 / 4 / 3 / 3, composite **2.6** |
| Subresults | [SR-09](../subresults/SR-09-coverage-map.md); Lean bijection `IndependentSets.card_indepSets_eq_card_satAssignments` |

## Statement

If Theorem 1.1 holds: $\#3$-SAT is solvable in deterministic $2^{o(n)}$ time and polynomial space,
refuting #ETH (Dell, Husfeldt, Marx, Taslaman, Wahlén, TALG 2014); perfect matchings in graphs
with $O(v)$ edges, and hence permanents of 0/1 matrices with $O(n)$ nonzeros, are countable in
$2^{o(v)}$, refuting the conditional lower bound of Curticapean (ICALP 2015, block
interpolation); #IS and $\#q$-colourings ($q$ fixed) in $2^{o(v)}$.

## Precision

DHMTW's 0/1-permanent lower bound under #ETH is $\exp(o(m/\log n))$; Curticapean's
interpolation removes the $\log n$. Both now lose their justification. The exponents are
$O(v\log\log v/\sqrt{\log v})$, not $O(v/\log v)$ as the source says
([SR-08](../subresults/SR-08-corrections-to-gemini-summaries.md), row 1).

## Open parts

1. Dense permanents and matchings in dense graphs: [ETH-C05](ETH-C05-counting-beyond-linear-encodings.md).
2. Counting with parity tests in polynomial space without the parity lift: a simpler route for
   #3-SAT at bounded occurrence is the overview algorithm; record its exact space bound.

## Closest work

Preprint Cor. 1.3 (level T; R039); DHMTW 2014 and Curticapean 2015 (level T).

## Resource boundary

No fleet needed beyond keeping the map in SR-09 current.
