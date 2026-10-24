# RR002 round 1 — independent construction review

Reviewer: `/root/rr_plan_critic`, critic profile. Scope: the frozen
`round-1-proposal.md` under `construction-contract.md`; no permission to
change the target or resource caps. Review performed 2026-10-23 UTC
(2026-10-24 local time). No nested agents, endpoint implementation, Lean
build, dependency installation, or exposition work.

**Verdict: refuted for R1 and R1b; the general W-to-C bridge remains
unresolved.** The obstruction to every deterministic route factoring
through the exact unlabelled row projection is proved below. A lossless
column representation is a supported replacement input, not a completed
bridge or a claimed new partition theorem.

Assurance: the mathematical arguments below are elementary, written out,
and independently checked against a separate small enumeration. They have
not been checked in Lean. Novelty of any general bridge remains
**unverified**.

## 1. Smallest direct-validity failure — proved

Let `w=(1,2,3,2,1)` periodically, with positions starting at one. The
weighted partition `W=(2,1)` has weight `2+2*1=4`, and

```text
R((2,1)) = (2,2).
```

The adjacent gap is zero, but the pair sum is four, not divisible by
three. Thus `R(W)` is not an actual A-partition. This refutes direct
landing in A; by itself it does not refute a later straightening.

It is the smallest possible weight. At weights zero through three, the
complete W families are respectively `()`, `(1)`, `(2)`, and
`(3),(1,1)`. Their projections are empty, singleton partitions, or
`(1,2)`, all valid in A. Completeness follows because three positive rows
already have weighted size at least `1+2+3=6`, and two rows have size
`p+2q` with `p>=q>=1`.

## 2. Smallest collision and exact obstruction — proved

At weight six, both `(4,1)` and `(2,2)` belong to W: they are descending
positive partitions, and neither has a multiplicity exceeding four.
Their weighted-row projections coincide:

```text
R((4,1)) = sort(4,2) = (2,4)
R((2,2)) = sort(2,4) = (2,4).
```

This is the smallest collision. Equal projected lists have the same
number of entries. For `N<6`, W has at most two rows. A one-row object is
uniquely `(N)`. For two rows `(p,q)`, the equation `p+2q=N<6` and `p>=q`
force `q=1`, so there is at most one such object at each weight. Different
row counts cannot collide. The empty case is unique.

More generally, for every positive integer `t`,

```text
W_left  = (4t,t),
W_right = (2t,2t),
weight  = 6t,
R(W_left) = R(W_right) = (2t,4t).
```

**Factorization obstruction.** Fix `N=6t` and any target set X. If a
function `F:W_N -> X` factors as `F=T_N o R`, then the displayed distinct
inputs have equal images. Therefore F is not injective. This remains
true for any number of deterministic local rewrites, any priority order,
any termination measure, and any subsequent A-to-C encoder, provided the
complete downstream state is determined only by R and N. If T is partial
and fails on that projection, it fails totality instead.

Scope matters: this does **not** disprove W-to-C bijections, all local
rewrite methods, or methods retaining additional input information. A
new method that retains labels is outside this exact factorization and
must establish its own inverse. It must not claim to have repaired R
while silently relying on discarded W information.

## 3. Row count cannot be the output gap length — proved

At weight six, W is exactly

```text
(6), (4,1), (2,2), (1,1,1).
```

Its row-count distribution is `{1:1, 2:2, 3:1}`. The actual A family is

```text
(6), (1,5), (2,4), (3,3),
```

with length distribution `{1:1, 2:3}`.

There is also a direct obstruction in C, independent of an endpoint
implementation. Requiring `a+2b=3` permits only `(a,b)=(3,0)` or `(1,1)`.
Their base weights are respectively nine and seven; nonnegative
increments cannot lower either to six. Consequently W's `(1,1,1)` has no
C-image satisfying the proposed refinement.

This first fails at N=6. Below six there are no three-row W objects.
For two-row W objects, there is one at each of N=3,4,5. C has one
length-two object at each of those weights: respectively
`(a,b,mu,nu)=(0,1,(),(0))`, `(2,0,(0,0),())`, and
`(2,0,(0,1),())`. At every positive weight there is exactly one
length-one object, with `a=1,b=0,mu=(N-1)`. The empty weight-zero objects
also agree. Thus the entire refinement, rather than merely a convenient
rule, must be dropped for a full bridge.

## 4. Exact stronger replacement: intrinsic weighted columns

This replacement retains the missing information without an arbitrary
history field. It is an attributed column interpretation consistent with
Andrews–Keith, not a novel endpoint theorem.

For `W=(p_1,...,p_l)`, define the conjugate column heights

```text
h_j = #{i : p_i >= j},  1 <= j <= p_1.
```

They form a descending positive list. Set `h_(p_1+1)=0`. The multiplicity
of the row value j is exactly `h_j-h_(j+1)`. Therefore W's multiplicity
condition is equivalent to

```text
0 <= h_j-h_(j+1) <= 4, including the final step to zero.
```

Define `s=(0,1,3,6,8)` and the strictly increasing cumulative weight

```text
F(5q+r) = 9q+s_r,   q>=0, 0<=r<5.
U(W) = (F(h_1),...,F(h_(p_1))).
```

Here U is descending; do not change the weight convention by treating
the original rows as ordinarily weighted.

The exact U domain consists of descending positive lists whose residues
modulo nine lie in `{0,1,3,6,8}` and whose decoded heights satisfy the
displayed gap condition. The intrinsic inverse on a part is

```text
D(9q+s_r)=5q+r,
```

including `D(0)=0` for the terminal boundary. Decode all heights, then
conjugate them to recover W. Every positive U part uniquely determines
its residue label r; labels zero through four are not discretionary
metadata. The roundtrip in both directions follows from strict
monotonicity of F and the ordinary conjugation inverse.

Double counting Ferrers boxes proves weight preservation:

```text
sum_i w_i*p_i = sum_j sum_(i<=h_j) w_i = sum_j F(h_j).
```

In particular, the colliding row-projection inputs remain distinct:

```text
U((4,1)) = (3,1,1,1),
U((2,2)) = (3,3).
```

The decoded-height condition has a finite local form. If consecutive
heights have residues r and r', then

```text
U_j-U_(j+1) = 9*[r<r'] + s_r-s_(r'),
```

where the final part is compared to `(size,residue)=(0,0)`. This follows
because a height drop between zero and four has quotient drop precisely
`[r<r']`. Thus comparisons and allowed boundary transitions can be
expressed by an explicit five-by-five residue table, with every label
recoverable from the numerical part. All representation work can use at
most N Ferrers boxes, since every original row weight is positive.

### Sharply specified next obligation

Use this exact U-domain as input to a candidate, with the terminal ground
state fixed. Freeze a finite table of moves on consecutive intrinsic
residue labels and their quotient levels, allowing singleton/pair
creation and the contracted arithmetic shifts. Each rule must state its
guard, numerical update, weight transferred to mu or `3*nu`, priority,
and exact inverse guard. Derive a and b from the terminal singleton/pair
state; do not set `a+2b=length(W)`.

The first research gate is to produce a canonical decomposition

```text
U -> (a,b,mu,nu)
```

with sorted nonnegative increment vectors of the required lengths and
an inverse that reconstructs U from those four output components alone.
Any persistent label must be a stated function of these components; a
fifth unconstrained component is not a C object. A candidate may merge
or split columns, but it must explain how the inverse recovers every
choice. The representation above gives an exact finite-state interface
for that research question; it does not supply the missing rules.

Replacing W by U is not success on the bridge gate. Likewise, applying
Stockhofe to U and reporting B merely recovers an established endpoint.

## 5. Primary-source re-inspection and limits

* **Established endpoint, inspected construction:** Andrews–Keith,
  [arXiv:2203.05202v2](https://arxiv.org/html/2203.05202v2), §§2–3 and §5
  Theorem 6. The weighted model and conjugation/Stockhofe operations are
  supported. Their historical open-status sentence is not evidence of
  current novelty. The §2 auxiliary normalization discrepancy remains a
  transcription hazard; no endpoint implementation was attempted here.
* **Established constructive parametrization, inspected theorem/proof:**
  Kurşungöz, [arXiv:1808.01432v1](https://arxiv.org/html/1808.01432), §3
  Theorem 7. Its cluster increments include zero padding; the multiples
  of three are normalized as `3*nu` in this contract. This is an
  attributed A-to-C construction, not our proposed new contribution.
* **Relevant generalization, selectively inspected:** Konan,
  [arXiv:2002.00300v2](https://arxiv.org/pdf/2002.00300), §2 Theorems 2.8
  and 2.13, and §6. Theorem 2.8 supplies a color-sequence/energy-preserving
  correspondence under explicit ground-energy hypotheses. The degree-two
  extension has additional definitions and hypotheses. Citing these
  results does not identify the exact KR1 cluster objects with one of
  their domains. Such an application needs an explicit specialization,
  equality of the resulting restrictions, and actual inverse maps.

A bounded additional search did not identify a completed structural
KR1 product-to-gap bridge. This is an **unverified novelty status**, not
an assertion that no bridge exists. None of the inspected generalizations
licenses importing the missing construction as an assumption.

## 6. Independent executed check and resource record

A separate ephemeral Python standard-library program recursively
enumerated W from its weighted row definition and ordinary partitions
from their actual ascending A restrictions for every `0<=N<=12`. It did
not import the author's enumerators or any endpoint map. It compared R
fibres, A-validity, and length distributions. The observed first
failures were N=4, N=6, and N=6 as proved above.

The total W and A counts agreed in this pilot:

```text
N:       0 1 2 3 4 5 6 7 8 9 10 11 12
W and A: 1 1 1 2 2 2 4 4 5 7  8  9 13
```

This finite agreement is **empirical** and is not the evidence for a
universal count identity or a bridge. The elementary arguments in
sections 1–4 establish the stated obstructions and representation facts.

The shell reported approximately 0.94 seconds for the independent pilot.
No files or result tables were generated by that program; this review is
the sole file written by the critic. Peak memory and exact token/tool
costs were not instrumented and are **unknown**, not zero. The pilot did
not approach the stated ten-minute cumulative enumeration allowance.

Required author revision: retain the exact counterexamples, retire R1
and R1b, and either freeze a precise intrinsically labelled replacement
within the existing second-round budget or report the missing U-to-C
decomposition honestly. No class-wide impossibility follows from an
unsuccessful capped search.
