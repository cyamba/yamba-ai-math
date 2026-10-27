# Separate semantic review, 27 October 2026

Reviewer: `separated_critic`, a distinct mathematical critic agent in this session.
One review round, including correction of proof transcription errors before the
final verdict. This is separate review, not independent model errors or a formal
proof checker. **Novelty status: NOT VERIFIED.**

## Verdict

**SUPPORTED for Theorems 1, 2 and 3 as presently scoped.** The exact validity
criterion, raw tuple injectivity, intrinsic separated image, both inverse
identities and positive rational generating function have complete written
arguments after the corrections below. No counterexample was found. The current
proof inspected has SHA-256
`e6db46ff2fa250404ae1b06db761fcdc700b90450b31bcfa3cb38b08f0a16212`.
Cosmetic subsequent edits do not extend this review to changed mathematics.

The supplied universal compiler is **REFUTED** at weight10. The absence of
collisions is compatible with its failing to land in the target set. Theorem1
in fact proves raw injectivity at every weight, so a collision-only stress test
would miss the central defect at all weights.

## Proof checks and initial findings

The initial draft contained three local errors, all reported to the author and
corrected before this verdict:

1. The auxiliary functions satisfy `h(t)-l(t)=-(t mod2)`, not `1-(t mod2)`.
   It is the **full pair** difference `H_i-L_i` that equals `1-r_i`.
2. The interpair boundary is
   `L_i-H_(i+1)=2+l(m_i)-h(m_(i+1))`, not `3+...`. The corrected lower
   bound is still two since `l(x)>=h(x)>=h(y)` for `x>=y`.
3. Ordering gives weak decrease of pair parameter t, not strict decrease.
   Equal t must be excluded using distance-two: the two high entries differ by
   at most one. The revised proof explicitly does so.

These corrections repair the written derivation without changing its theorem
statements. No retained error or unresolved hypothesis remains in these three
theorems.

For validity, all internal block constraints are automatic. The unique remaining
boundary triple forces and is secured by
`S_a-L_1>=3`, exactly `mu_a>=ceil(3m_1/2)`. The other straddling triple has
gap at least `4+r_1`, and the adjacent boundary gap is at least `2+r_1`.
Empty and pure blocks were checked separately.

Raw injectivity is also valid for unordered/malformed outputs: differing pair
counts of equal-length outputs force a prescribed close pair to cover two
singleton positions of the other output, whose difference is at least two.
Once counts agree, singleton coordinates and pair sums recover every source
coordinate. This statement must continue to target **tuples**, without silently
sorting them into partitions.

For target coverage, every close pair is intrinsically marked and cannot overlap
another one. Consecutive pair levels differ by at least two; subtracting their
base levels therefore yields a nonnegative descending m. Singleton offsets
likewise yield nonnegative descending mu, and the actual boundary gives the
required common-shift bound. Direct substitution proves both inverses.

For the generating function, setting `delta_i=m_i-m_(i+1)` gives
`m_1=sum(delta_i)` and `sum(m_i)=sum(i delta_i)`. The binary decomposition
`delta_i=2e_i+epsilon_i` contributes independent denominators
`1-q^(6i+3a)`, with exactly the stated numerator. For a=0 it simplifies to
the standard paired-sector factor; for b=0 the numerator and pair denominator
are empty products. The Gaussian form is the finite subset-weight identity,
so its exponents and positivity follow directly.

## Separate bounded corroboration

`critic_check.py` was written by this reviewer without importing the author's
implementation. It independently constructs integer partitions, cluster inputs,
literal compiler outputs, intrinsic atom inverses and finite series coefficients.
Command, from repository root:

```sh
python3 research/rogers-ramanujan/separated-2026-10-27/critic_check.py
```

Observed output in this review round:

| Check | Scope/result |
| --- | --- |
| Source states | 3,231 through weight36 |
| Valid sources | 2,732; exact criterion agrees for all 3,231 states |
| Raw collisions | Zero across all source states |
| Independently enumerated gap targets | 1,393 through weight30 |
| Separated gap targets | 1,218; exact equality with the restricted source image |
| Inverse identities | Both directions pass on the respective finite domains |
| Generating functions | All 16 sectors with base weight at most36, coefficients through36, agree |
| First invalid source | `(a,b,mu,m)=(1,1,(0,),(1,))`, output `(4,3,3)`, weight10 |
| Enumeration wall time | 1.159327932999986 seconds reported by the script |

The script's SHA-256 is
`083bca2b759bf7c1e081160dfba7d16f17dbadbd8dbc6a341ac8f2bef1648747`.
These finite checks corroborate transcription. Universal assurance comes from
the written arguments above, not from enumeration.

## Relation to existing work and remaining scope

The existing `rr003/endpoint-cluster-merge.md` already describes a more general
cluster-to-gap merge, with author-only assurance for that broader formulation.
On a separated target its ascending extraction uses b earlier pairs for each
singleton and zero earlier singletons for each pair; reversing the order gives
exactly the coordinates in this restricted note. Thus this new restricted proof
does not establish a previously missing residue-to-cluster map, and it does not
upgrade the assurance of the full existing merge.

I inspected that repository argument for this comparison, not every theorem in
Kurşungöz's paper or all prior literature. The general cluster series and base
configuration must retain their existing attribution. No claim of newness,
Lean certification, compatibility with other U-C sectors, complete target
coverage beyond S^a P^b, or a complete KR1 bijection is supported by this review.
