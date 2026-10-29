# ETH-D06. Hardness of approximation built on ETH and Gap-ETH

| Field | Value |
| --- | --- |
| Category | Fine-grained / approximation |
| Source items | "Collapse of ETH-hard approximation barriers" (Dense k-Subgraph, approximate Nash) |
| Status | **Open** (map needed) |
| Depends on the upstream theorem | Yes |
| Score (I/B/T/L/Lean) | 3 / 2 / 3 / 2 / 1, composite **2.4** |
| Subresults | none |

## Task

Classify ETH- and Gap-ETH-based inapproximability results into (a) those whose reductions blow
up instance size polynomially or quasi-polynomially, which survive under the weaker hypothesis
"3-SAT needs $2^{n/\mathrm{polylog}(n)}$" with mild losses, and (b) those that needed exactly
$2^{\Omega(n)}$.

## Example

Quasi-polynomial lower bounds proved from ETH by birthday repetition (approximate Nash,
Dense $k$-Subgraph style results, e.g. Braverman, Ko, Weinstein; Manurangsi; level T) map 3-SAT on $N$
variables to instances of size $n=2^{\tilde O(\sqrt N)}$. A lower bound $2^{N/(\log N)^{c}}$ for
3-SAT still gives $n^{\Omega(\log n/(\log\log n)^{O(1)})}$: the quasi-polynomial barrier survives
up to $\log\log$ factors under polylog-ETH ([ETH-D08](ETH-D08-polylog-eth-and-surviving-lower-bounds.md)).

## Resource boundary

One literature agent; deliver a table with each result, its reduction size and its fate.
