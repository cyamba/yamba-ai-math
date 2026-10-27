# A rigorous restricted result from the lookup-free KR1 proposal

Date: 27 October 2026. Author: Christopher Yamba, with ChatGPT assistance.
Research base: `4ccc4fe`, the verified head of draft PR16.

**Useful independent component obtained; complete KR1 remains unresolved.**
The literal proposed generator fails at weight10. Its exact safe domain,
intrinsic image, explicit inverse and positive generating function now have
written proofs supported by a separate mathematical review. Novelty is
**NOT VERIFIED**; no Lean certificate is claimed.

## The retained theorem

Use the supplied descending cluster coordinates
\((a,b,\mu,\nu)\), with \(m=\nu/3\), and
\(Q(a,b)=a^2+3ab+3b^2\). The proposal appends lifted pairs to a block of
singletons. For \(a,b>0\), its output satisfies the KR1 conditions **if and
only if**

\[
\boxed{\mu_a\;\ge\;\left\lceil\frac{3m_1}{2}\right\rceil
             =\left\lceil\frac{\nu_1}{2}\right\rceil.}
\]

Pure-singleton and pure-pair sectors need no additional condition.
On this exact domain, the map is a weight- and dimension-preserving bijection
onto gap partitions whose descending atom word is \(S^aP^b\): all unpaired
singletons lie above all close pairs. Close pairs are intrinsic and cannot
overlap, so the inverse recovers \(a,b\) without source tags or lookup tables.

The forward map, inverse and all-parameter arguments are in [proof.md](proof.md).
The executable maps in [separated_pairs.py](../checks/separated_pairs.py)
reject inputs outside the proved domain. They do not change the existing global
map or silently sort invalid outputs.

## A positive generating function for this image

Let \(F_{a,b}(q)\) count these separated partitions by weight. Then

\[
F_{a,b}(q)=
\frac{q^{a^2+3ab+3b^2}}
{(q;q)_a\prod_{i=1}^{b}(1-q^{6i+3a})}
\sum_{j=0}^{b}
q^{\frac{3j(j+1)}2+a\left\lceil\frac{3j}2\right\rceil}
{b\brack j}_{q^3}.
\]

Here \({b\brack j}_{q^3}\) is a Gaussian polynomial. The proof splits the
successive differences of \(m\) into even parts and parity bits. This gives
a positive numerator and independent geometric-series factors, including the
empty and pure-sector cases. For example,

\[
F_{1,1}(q)=\frac{q^7(1+q^5)}{(1-q)(1-q^9)}.
\]

The value is an exact, recognizable safe component and a benchmark for future
crossing rules. This is a refinement of an existing cluster endpoint, not a new
proof of the residue-product identity. The broader cluster-to-gap merge already
exists in [RR003](../rr003/endpoint-cluster-merge.md). Its assurance is unchanged.

## What the proposed harness actually establishes

The proposal's boundary fold is a `pass`; `carry_lift` never changes.
The first failure is

\[
(a,b,\mu,\nu)=(1,1,(0),(3))\quad\longmapsto\quad(4,3,3),
\]

of weight10. It violates the adjacent-sum and distance-two conditions.
The formula nevertheless preserves weight, dimension and raw-tuple injectivity
at **every** weight. Thus zero collisions cannot establish a KR1 bijection.

| Scope | Cluster inputs | Invalid raw outputs | Collisions | Safe separated outputs |
| --- | ---: | ---: | ---: | ---: |
| Weights0 through60 | 55,403 | 13,727 | 0 | 41,676 |
| Requested weights41 through60 | 49,942 | 12,787 | 0 | 37,155 |
| Weight60 alone | 5,602 | 1,550 | 0 | 4,052 |

The attached note's claimed counts, including 31,180 inputs at weight60,
are incorrect for its own definitions. The original code actually counts 5,602.
It also calls the mixed-sector counter an \(U_{a\le2}\) check, although it never
constructs the repository's U objects or U-to-cluster map. No U-C disjointness
theorem follows from that counter. DP equality through60 is finite evidence.

Our independent target enumeration finds exactly the stated safe image, verifies
both inverse identities, and checks the positive series separately in every
reachable \((a,b)\) sector through60. It also confirms the safe formula agrees
with the existing broader merge, after reversing coordinates and scaling nu.
The source binding and complete per-weight table are in [evidence.json](evidence.json).

## Assurance, attribution and next obligation

The [separate critic](review.md) supports all three corrected written theorems.
Its independently written [check](critic_check.py) corroborates the criterion
through36, target image through30 and sector series through36. Three initial
proof transcription slips were corrected and preserved in the review history.
These are manually reasoned and reviewed proofs, not formal certificates.
All **115 repository tests pass**, including eight new regressions, and the
repository integrity check passes. Commands and resource accounting are in
[validation.json](validation.json); input provenance is recorded without the
private transcript in [input_provenance.json](input_provenance.json).

Kurşungöz's [Theorem7 and base configuration(3), pp5-6](https://arxiv.org/pdf/1808.01432)
already supply the general cluster series and staircase. We inspected that
statement/base and the nearby free-pair/crossing rules, not the whole paper's
proof. The finite subset expansion above was derived here; priority has not
been established. See the source-inspection ledger in the repository.

The missing work in the supplied formula is pair-singleton crossing; the existing
broader endpoint already addresses it. The central KR1 research gap remains the
residue/weighted-column-to-cluster bridge with an intrinsic inverse and global
disjoint exhaustive coverage. This restricted result does not close that gap.

## Reproduce

From the repository root:

```sh
python3 research/rogers-ramanujan/separated-2026-10-27/audit.py
python3 research/rogers-ramanujan/separated-2026-10-27/critic_check.py
python3 -m unittest discover -s tests -v
python3 scripts/check_repository.py
```

The audit returns success when its restricted assertions pass. To test the
supplied **full** compiler's validity explicitly, add
`--require-full-compiler`; it exits2 on the known counterexample, including
under optimized Python. `--original /path/to/extracted_harness.py` optionally
compares every output against the supplied code. Original private text was
not copied into the repository. Evidence output is optional and refuses overwrite.

The original investigation was committed locally on
`research/kr1-separated-pair-subresult`; its execution records describe that
local checkpoint. Christopher subsequently authorized a remote PR and merge.
See [release.md](release.md) for the publication follow-up and fresh checks.
