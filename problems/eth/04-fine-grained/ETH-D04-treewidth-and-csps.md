# ETH-D04. Treewidth and CSPs: Marx's "Can you beat treewidth?"

| Field | Value |
| --- | --- |
| Category | Fine-grained / parameterized |
| Source items | "Marx's 'Can You Beat Treewidth?': subexponential CSPs beyond bounded treewidth" |
| Status | **Open** (fixed domains trivial, growing domains open) |
| Depends on the upstream theorem | Yes |
| Score (I/B/T/L/Lean) | 3 / 3 / 2 / 2 / 1, composite **2.5** |
| Subresults | relates to [ETH-A08](../01-algorithmic-core/ETH-A08-width-dependence-and-uw-seth.md) |

## Statement

Marx (Theory of Computing 6 (2010)) shows under ETH that binary CSP on any class of primal
graphs of unbounded treewidth $k$ has no $f(G)\,n^{o(k/\log k)}$ algorithm, where $n$ includes the
domain size. For a **fixed** domain $D$, encoding values in $\lceil\log_2|D|\rceil$ bits gives a
fixed-width CNF with $O(n)$ variables and $2^{o(n)}$ time; this beats $|D|^{\mathrm{tw}}$ only when
$\mathrm{tw}=\Theta(n)$. The lower bound's regime is **growing domains**, where clauses have width
$2\log|D|$.

## Task

Does Theorem 1.1 (or its tensor route) give $|D|^{o(\mathrm{tw})}\mathrm{poly}(n)$ for binary CSPs
with $|D|=n^{\Theta(1)}$ on expanders? Equivalently, can the clause-width frontier
([ETH-A08](../01-algorithmic-core/ETH-A08-width-dependence-and-uw-seth.md)) reach width
$\Theta(\log n)$ for CSP-structured formulas?

## Obstruction

Width $2\log|D|$ is far beyond the $\log\log n$ frontier; binary CSPs with large domains have
$|D|^2$ forbidden pairs per edge, so the tensor network has entries but few wires: a direct
contraction with $\log|D|$-bit wires might work better than SAT.

## Smallest falsifier

A tensor network for binary CSP with $O(n\log|D|)$ wires and degree $\le s^{9/10}$, if it exists,
gives $2^{O(n\log|D|/\sqrt{\log n})}=|D|^{O(n/\sqrt{\log n})}$, which is $|D|^{o(\mathrm{tw})}$ on
expanders.

## Resource boundary

One agent to check the tensor encoding against Theorem D.1's hypotheses (entry computation
time, degree), one critic.
