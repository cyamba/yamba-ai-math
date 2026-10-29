# ETH-F02. Cryptographic parameter scaling and concrete security

| Field | Value |
| --- | --- |
| Category | Cryptography |
| Source items | "Cryptographic immunity at fixed parameters"; "Invalidation of naive linear-reduction security margins" |
| Status | **Answered for concrete sizes** (SR-06); asymptotic bookkeeping open |
| Depends on the upstream theorem | Yes |
| Score (I/B/T/L/Lean) | 2 / 1 / 4 / 2 / 1, composite **2.0** |
| Subresults | [SR-06](../subresults/SR-06-galactic-thresholds.md) |

## Statement

No instance of practical size is affected: in the preprint's own cost model the algorithm beats
$2^n$ only for $n\gtrsim2^{160000}$ variables, and any cryptographic instance encoded as CNF has
fewer than $2^{300}$ variables. Asymptotically, a primitive whose security proof reduced from
fixed-width SAT with linear blowup and assumed $2^{\Omega(n)}$ hardness must be re-parameterized
against $2^{O(n\log\log n/\sqrt{\log n})}$ attacks.

## Corrections

The claim that MQ and syndrome-decoding schemes must move to $n=\Theta(\lambda\log\lambda)$ is wrong
for dense schemes (SR-08 row 17); the claimed "Tseitin blowup $10^3$ to $10^5$" figures are
unsourced.

## Task

Produce a table of primitives whose security reductions start from fixed-width SAT or ETH (if
any exist in the literature), with the reduction size and the new asymptotic key-size rule.

## Resource boundary

One literature agent.
