# KR1 structural bijection: bounded construction result

Date: 2026-10-23 UTC / 2026-10-24 Stockholm. Branch:
`codex/rogers-ramanujan-bijections`. Contract:
[RR002](../../../programs/rogers-ramanujan-construction.json).

**The proposed new KR1 bijection remains unresolved.** Two author–critic
rounds produced exact obstructions and checked infrastructure. They did
not produce a W-to-C map with an inverse. The agreed two-round limit is
the stopping condition; no full Lean or article phase has started.

## Objects and attribution

The four sets are defined literally in the
[frozen contract](construction-contract.md): gap partitions A, residue
partitions B, positional-weight partitions W and zero-padded cluster
data C. In particular, W uses weights (1,2,3,2,1) periodically and C uses

```text
N = a*a + 3*a*b + 3*b*b + sum(mu) + 3*sum(nu).
```

The intended new contribution is the missing structural W-to-C bridge.
The A-to-C cluster construction is attributed to Kurşungöz and the B-to-W
endpoint to Andrews–Keith/Stockhofe. Their actual endpoint algorithms
have not been implemented or Lean-verified here. The counting identity
has reported proofs; these tests do not establish a new counting theorem.
Novelty of a possible structural bridge remains **unverified**. Versions
and inspection depths are in the [primary-source audit](source-audit.md).

## Exact obstruction to forgetting the row positions

For the first candidate, form R(W) by multiplying each row by its
positional weight, then sorting and forgetting the positions. At N=4,
R((2,1))=(2,2), which violates A's adjacent-pair condition.

A stronger obstruction holds for every positive integer t:

```text
W_left  = (4t,t),     W_right = (2t,2t),
weight  = 6t,        R(W_left) = R(W_right) = (2t,4t).
```

The inputs are distinct valid W objects. Thus every deterministic map
whose entire downstream state is determined by R(W) and N is
noninjective. This is a proved obstruction to that exact factorization,
not to all local KR1 bijections. Requiring W's row count to equal a+2b
also fails: W=(1,1,1) has weight six, whereas a+2b=3 forces C's base
weight to be at least seven. Full arguments and minimality at N=4 and
N=6 are in the [first review](round-1-review.md).

## A lossless input representation

Let h be the descending conjugate column heights of W. Multiplicity at
most four is equivalent to 0<=h_j-h_(j+1)<=4, **including the final
step to zero**. Set s=(0,1,3,6,8) and

```text
F(5q+r) = 9q+s_r,   0<=r<5,
U(W) = (F(h_1), F(h_2), ...).
```

Each column value determines its height: D(9q+s_r)=5q+r. Decode heights
and conjugate to recover W. Double counting Ferrers boxes gives
sum_i(w_i*pi_i)=sum_j F(h_j). This is an attributed column interpretation
with a written inverse argument, not a new KR1 endpoint. The terminal
height constraint is essential; for example U=(9) is outside the domain.

## Second proposal: normalization succeeds, bijectivity fails

The [second proposal](round-2-proposal.md) freezes the arithmetic rules,
scan order, priority and four Boolean switches. Profile bits, in order,
are `plateau_first`, `residue_guard`, `plateau_spread`, `merge_upper`.
The original proposal is 0111. The sixteen profiles were fixed before
their family evaluation; the family was informed by the original
candidate's weight-eight failure and is not held-out validation.

Each update preserves weight and strictly raises E(p)=sum(p_i*p_i):

| Update | Increase in E |
| --- | --- |
| (x,y) -> (x+y) | 2xy |
| (x,y) -> (x-1,y+1) | 2(y-x)+2 |
| (x,y,z) -> (x,y+z) | 2yz |
| (x,y,z) -> (x+y,z) | 2xy |
| (x,y,y) -> (x-1,y-1,y+2) | 2(y-x)+6 |

All entries remain positive after explicit zero deletion. The pair
spread guard excludes x=1. Since E<=N*N and each increase is at least
two, at most N*N/2 rewrites occur. On termination, no defining A defect
remains. This gives a universal written proof of total, weight-preserving
normalization. Counting scans, comparisons, sorting and arithmetic fits
the contracted quartic unary work and quadratic auxiliary space bounds.
Diagnostic full traces are outside that space bound and are not part
of the proposed map's output. There is no confluence or inverse claim.

**All sixteen bijection candidates are refuted.** Here `?` means either
bit. The disjoint groups cover all profiles:

| Profiles | Number | Weight | Distinct W inputs | Common A image |
| --- | ---: | ---: | --- | --- |
| ??0? | 8 | 7 | (2,1,1), (3,2) | (1,6) |
| 1?1? | 4 | 3 | (1,1), (3) | (3) |
| 001? | 2 | 8 | (1,1,1,1), (8) | (8) |
| 011? | 2 | 8 | (4,2), (8) | (3,5) |

For example, the original profile sends the intrinsic columns of (4,2)
through (1,1,3,3) -> (2,3,3) -> (3,5). It sends (8) through
(1,1,1,1,1,1,1,1) -> ... -> (2,2,2,2) -> (2,2,4) -> (4,4) -> (3,5).
The [verification record](verification-30.json) preserves every first
collision and its complete traces. These witnesses disprove only the
specified finite rule family; the full structural problem remains
unresolved in this investigation. See the separate
[second review](round-2-review.md) and [author revision](round-2-revision.md).

## Verification and assurance

The verifier generates all four actual families by separate paths,
compares literal ordinary-partition searches for A and B, checks W against
a different ordinary-size search and a column-path DP, and checks C
against a denominator-coefficient DP. These paths share some mathematical
constants and definitions; they are algorithmic cross-checks, not
independent source audits. It also checks the A/C length refinement.
The endpoints themselves are not assumed to be executable adapters.

Through N=30, the four counts agree at every weight. There are 195
objects in each family at weight thirty and 1,393 W objects in total
over weights zero through thirty. Their column round trips pass. All
22,288 profile/input normalizations land in A at the exact input weight;
131,431 rewrites were checked, with at most 33 for one input. These are
**empirical finite results**, not a universal counting or bijection proof.

The critic used a separate implementation for A/B/W, columns and the
rewrite rules through thirty, then compared outputs. Its agreement does
not constitute an independent C audit or Lean checking.

| Claim | Assurance and implementation in `checks/kr1.py` | Lean declaration |
| --- | --- | --- |
| Literal A/B/W/C finite definitions | Executable predicates/generators, reviewed against source conventions | None |
| R-factorization cannot be injective | Written universal argument; first review; `row_projection` retains witnesses | None |
| W-to-U is lossless and preserves weight | Written conjugation argument; `weighted_columns`, `decode_columns`; finite round trips | None |
| R2 terminates and preserves weight | Written energy argument; separate review; `column_straighten` | None |
| All 16 specified R2 profiles are noninjective | Exact collision certificates; `first_straightening_falsifier`; independent reproduction | None |
| Full W-to-C bijection and composed B-to-A map | **Unresolved**; no forward/inverse algorithms or proofs | None |
| Novelty of a future structural construction | **Unverified** | Not applicable |

The [source-bound finite receipt](verification-30.json) identifies exact
inputs by SHA256. The [execution receipt](execution-receipt.json) records
manual stages, repository checks, resource accounting and unknowns.
`verify.py --require-bijection` deliberately exits with failure code two
while the actual maps and Lean certificate are absent. Missing required
source files also fail. Finite agreement cannot certify completion.

## Precise remaining obligation

A useful next contract would design the inverse first. In the exact U
domain, seek intrinsic cores U_(a,b) of weight a*a+3*a*b+3*b*b and
canonical recoverable raising operations of costs i (1<=i<=a) and 3j
(1<=j<=b). These correspond to the nonnegative differences encoding the
ascending vectors mu and nu. Prove every U has one ordered construction
from one core, and that the inverse recovers the core and all move counts
from U alone. This is a proposed research route, **not a constructed
decomposition** or an additional assumption about the objects.

After a bridge survives criticism, the actual attributed endpoints must
still be implemented and checked, then all maps and inverse identities
proved in Lean. Only then do the full illustrated article and publication
gates become available. No new dependency, bulk cache, user-file deletion,
paid adapter or publication was used in RR002.
