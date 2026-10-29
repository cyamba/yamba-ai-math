# ETH-E01. Circuit lower bounds through Williams's program

| Field | Value |
| --- | --- |
| Category | Circuits |
| Source items | "Circuit lower bounds (Williams' program): new frontiers for $\mathrm E^{\mathrm{NP}}$ vs circuit classes" |
| Status | **Conditional result in the preprint; improvement open** |
| Depends on the upstream theorem | Yes |
| Score (I/B/T/L/Lean) | 4 / 3 / 3 / 3 / 1, composite **3.1** |
| Subresults | [SR-04](../subresults/SR-04-slab-construction.md) (exponent target), [SR-09](../subresults/SR-09-coverage-map.md) |

## Statement

The preprint proves $\mathrm E^{\mathrm{NP}}\not\subseteq\mathrm{SIZE}(O(n))$ (Cor. C.1, via Williams,
SICOMP 2013, Thm 6.1: "if ETH is false then $\mathrm E^{\mathrm{NP}}$ does not have linear-size
circuits") and, quantitatively, a language in $\mathrm E^{\mathrm{NP}}$ with $C_L(n)>c\,n\sqrt{\log n}$
infinitely often (Cor. 1.4), using the local reduction of Jahanjou, Miles and Viola.

## Task

1. **Exponent transfer.** The proof uses only the bounded-density decision exponent
   $V/a(V)$ with $a(V)=\sqrt{\log V}$; an exponent $V/(\log V)^{\alpha}$ gives
   $C_L(n)>c\,n(\log n)^{\alpha}$. Any progress on [ETH-A01](../01-algorithmic-core/ETH-A01-break-the-sqrt-log-barrier.md)
   transfers directly; record the exact transfer lemma.
2. **Beyond near-linear size.** Williams's method needs SAT algorithms for circuits of size $s$
   with $n$ inputs beating $2^n$ by superpolynomial factors; the tensor route counts over all
   $s$ wires. Is there a version whose cost depends on $n$ (inputs) rather than $s$ (gates) for
   $s=n^{1+\varepsilon}$? That would give $\mathrm E^{\mathrm{NP}}\not\subseteq\mathrm{SIZE}(n^{1+\varepsilon})$.
3. **Correction.** No consequence for $\mathrm{NC}^1$ or $\mathrm{TC}^0$ follows
   ([SR-08](../subresults/SR-08-corrections-to-gemini-summaries.md), row 16).

## Closest work

Williams 2013 (level T, theorem quoted by the citation check); Jahanjou, Miles, Viola, ICALP
2015 (level T); Li and Yang, STOC 2022 ($3.1n$ lower bounds for $\mathrm E^{\mathrm{NP}}$; level T,
to inspect).

## Resource boundary

One agent for the transfer lemma; item 2 is a research problem for a later iteration.
