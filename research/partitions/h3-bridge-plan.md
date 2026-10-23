# H3: actual colorings and survivor coefficients

Execution contract accepted by the user on 2026-10-22. Baseline is
`b989eb12376c0276d99aba349aedd9ba956d286b`, verified with `git rev-parse HEAD`.
At entry H1/H2 were checked and H3 was incomplete. This document preserves
the original specification and historical progress. The [23 October continuation](h3-continuation-20261023.md) and [claim index](evidence/claim-to-theorem-index.md) record the later all-alphabet proof, checks and reviews; no novelty is claimed.

## Exact public target

For all natural `n,r`, a monotone extensive Hessenberg function on `Fin n`
defines `i <_P j` by `h(i) < j` and graph edges `i < j <= h(i)`. Assume no
strict three-element chain. In actual finite multivariate polynomials prove

```text
X(h,r) = sum k=0..floor(n/2), C(W(S_k)) * e_(n-k) * e_k.
```

`X` sums over proper functions `Fin n -> Fin r`, with ascent weights and
actual color monomials. `S_k` is exactly the complement of the bubble image
inside the existing complete `columnFamily`, not an unspecified positive
witness. Prove any relabeling to the existing Nat vertices and inversion
statistic. The final theorem must not assume a coloring expansion.

## Proposed finite proof (written argument, not Lean-checked)

This derives a restricted version of Shareshian--Wachs, arXiv:1405.4629v2,
Sections 4 and 6, then uses the attributed Cho--Huh injection already checked.

1. Use `MvPolynomial (Fin m) (Polynomial Int)`, initially `m >= n`.
   Actual color classes are chains, hence have size at most two. Prove
   symmetry by swapping the multiplicities of adjacent colors. Equal sizes
   permit identity; an empty class permits a complete swap. For sizes 1,2,
   one induced edge requires changing the isolated vertex; two edges permit
   swapping all three vertices and preserve one ascent. Natural labeling
   puts the singleton between the two chain endpoints. Prove involutivity,
   properness and unchanged outside-color comparisons. Prove pointwise
   coloring descents = row-array inversions; color reversal and symmetry
   then identify the ascent and descent polynomials.
2. Arrays have exactly `m` rows, allow empty rows, have bijective fillings
   and chain rows. For padded partition `lambda` and permutation `pi`, impose
   `(length row_i : Int) = lambda_(pi i) - pi i + i`. Interpret the right
   side in integers. Negative lengths mean an empty sector, never truncated
   subtraction. The shifted lengths are pairwise distinct; adjacent lengths
   0,1 and 1,2 are excluded. Every non-tableau has a first-column defect.
   At the bottommost such boundary the only cases are

   ```text
   [] / [b,a] <--> [a] / [b],   b <_P a.
   ```

   Swap the two adjacent permutation images too. The lower first entry is
   unchanged, so the bottommost pivot is stable. The flattened words differ
   only by one comparable swap. Prove sign reversal, weight preservation,
   involutivity and the padded-tableau fixed sector, including `pi = id`.
3. Let `A(gamma)` be the signed monomial alternant, `delta_i=m-1-i`, and
   `Delta=A(delta)`. Coefficient extraction from `Delta*X` first gives
   `beta_i=lambda_i-i+pi(i)`. Proved symmetry and inverse-permutation
   reindexing are required to get the array shape above. Signed-array
   cancellation identifies its dominant coefficients with actual tableaux.
4. Symmetry of elementary polynomials gives
   `A(delta+nu)*e_b = sum_(|S|=b) A(delta+nu+1_S)`.
   When `nu=0`, non-prefix subsets have repeated adjacent exponents and
   vanish. For `nu=(1^a)`, subsets must be prefixes separately in the first
   `a` and last `m-a` positions. If `b<=a` and `a+b=n<=m`, this proves
   `Delta*e_a*e_b = sum_(j<=b) A(delta+(2^j,1^(n-2j)))`.
   Subtract the `(a+1,b-1)` identity, handling `b=0` separately.
5. Alternating coefficients at repeated exponents vanish over `Int[q]`.
   Every exponent in `Delta*X` is at most `m+1`. Sorting distinct exponents
   therefore gives `delta+lambda` with `lambda_1<=2`. Prove reconstruction,
   `Delta != 0` from its coefficient at `delta`, and valid cancellation.
   Lift H2 to polynomials and telescope. Specialize from `m=max(n,r)` by
   sending extra variables to zero. Transfer the equality to natural
   coefficients by an injective coefficient map. Handle `n=0` and `r=0`.

## Ownership and handoffs

The root leads coloring, mathematical integration, repository verification
and exposition. One Lean/algebra worker authors the signed-array pilot and
then bounded algebra lemmas. A distinct critic reviews exact statements and
sources. No recursive agents. Global concurrency is at most three workers.
P007/P008/P009 each use the existing pair profile, two review rounds, and
16 dispatch proxy units (48 total); these are neither money nor tokens.
Only stages with ready dependencies may proceed. Handoffs contain exact
statements, hashes, proof/check status, outstanding obligations and sources.

## Resource and assurance gates

Do not provision local Mathlib until at least 20 GiB is free. Delete no user
files. Cap new dependencies/builds at 15 GiB; stop provisioning below 5 GiB
free. Initial provisioning/build budget is 60 cumulative process minutes,
one initial attempt and one diagnosed retry. Existing installed Std may be
used without new provisioning. Record remote CI checks separately from local
checks; the user-authorized CI jobs do not establish a local reproduction.

The first decisive gates are the universal signed-array involution and the
generic alternant identity. Final acceptance requires an unconditional
actual-coloring theorem, clean source-bound checking, exact axiom reports,
separate semantic review, independent small coloring regressions, repository
checks, and an in-place article update compiled in its existing editor.
Missing dependencies, unexecuted code and failed checks cannot be success.
Preserve all original counterexamples. No general positivity or new theorem
priority is claimed. A failed gate retains its exact unresolved obligation.

## Recorded progress, 2026-10-22

The universal list-based signed-array involution is now **proved and checked**
in `lean/SignedArrays.lean`, with integer shape preservation, actual filling,
permutation-sign reversal, inversion preservation, and the padded-tableau
fixed sector. The [author handoff](evidence/h3-signed-array-handoff.md) and
[separate final review](evidence/h3-signed-array-review.md) pin the exact source
and hypotheses. The two signed-array implementation review rounds are used;
no third round is implied. This manual collaboration is not an executed
harness provider run.

The Std verifier now builds five modules freshly, including the Boolean
subset classification in `lean/AlternantSubsets.lean`. Its
[record](lean/verification.json) contains 54 principal dependency reports.

The generic alternant identity is now **proved and checked** in the separate
[Mathlib bridge](mathlib/README.md). Its 28 principal reports also cover
repeated-exponent vanishing, Vandermonde coefficient/nonzero/cancellation,
actual subset classification and coloring preliminaries. The
[second and final algebra review](evidence/h3-algebra-review-r2.md) supports
the exact declarations and retains the corrected color-row orientation
counterexample. It does not certify the remaining two-elementary
specialization or reconstruction. The P007 manual dispatch account is
**16 of 16** proxy units, including the failed specialist attempt and final
wording correction; both review rounds are used. These are not tokens or
monetary costs. No third algebra or signed-array review is implied.

The original Std certificate still needs no external library. Optional
Mathlib provisioning began after the selected 20 GiB entry buffer was met;
the buffer was not a requirement of Lean itself. Selected imports and their
transitive dependencies were provisioned within the 15 GiB additional-storage,
5 GiB free-space and initial time bounds. The single diagnosed cache retry
and a monitor measurement failure are retained in the
[author receipt](evidence/h3-algebra-revision-r1.md). No user files were deleted
for dependency provisioning.

`verify_all.py` runs repository tests/checker and both fresh certificates,
binds its report to the repository source snapshot and rejects missing
dependencies or any failed check. Separate pinned CI jobs check the two Lean
projects, caching dependency products but rebuilding project proofs.
The [claim-to-theorem index](evidence/claim-to-theorem-index.md) distinguishes
written, checked, reviewed and absent conclusions.

**H3 and whole contracts P007/P008 remain incomplete; P009 has not begun.**
Remaining obligations are the two-elementary specialization, dominant
coefficient reconstruction, adjacent-color symmetry, actual coloring/list
array bijections and statistic conversion, finite signed-sector cancellation,
the permutation-sign interface, canonical padding/family bijections, the H2
polynomial lift/telescope and specialization to every alphabet. The two
first acceptance gates are closed, but their checked compatible integration
interfaces are not complete. The bounded run therefore retains these exact
obligations rather than starting P009 on an assumed expansion.

## Continuation, 2026-10-23

The actual all-alphabet theorem now directly checks as
`PartitionH3.height_two_survivor_expansion`, with only `HeightTwo` beyond the
natural unit interval structure. The new module
`NaturalCoefficients.lean` also directly checks
`height_two_survivor_expansion_nat`: the actual natural-semiring sums are
identified under proved injective coefficient maps and the equality is pulled
back. Thus the transport requested in step 5 is an explicit theorem.

The algebra and coloring continuation contracts preserve the exhausted
historical bounds; their exact source packets and two reviews are separate.
P009 joins actual colorings, complete signed arrays, signs, statistics, zero
padding and the complete original tableau families; it lifts H2, reconstructs
the actual coloring alternant, telescopes and specializes from max(n,r).
The [first integration review](evidence/h3-integration-review-r1.md) supports
the ten frozen integration sources and independently checks the final
integer-coefficient theorem. The auxiliary natural transport has a separate
final review. Fresh source checking of the complete 21-module bridge now passed with
137 principal standard-only reports, alongside a fresh 54-report Std check.
The final combined source snapshot is recorded by the entry point and
reported with the follow-up PR, not inferred from the direct checks or reviews. The original general-height objective and external
general certificate audit remain outside this result.
