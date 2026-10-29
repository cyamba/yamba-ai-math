# Distinct Phase 2 tableau review

Date: 25 October 2026, Europe/Stockholm. Role: distinct mathematical critic,
not an author of this packet. Frozen author SHA-256:
`9e02329dfc61090275361070503328219a287d9f1f5f720de2e1842a71c3dd42`.
All 17 dependencies listed by the author freeze were verified before and
after the independent checks. No author file was edited. Distinct identity
does not guarantee independent model errors; no formal checker was run.

Overall verdict: **incomplete** for a full structural n=6 cancellation;
**supported** for Theorem A, **supported on its stated conditional domain**
for Theorem B, and **supported empirical finite evidence** for the enumerations
and matchings. The ordinary proof assurance below comes from checking the
full arguments, not from the numerical pass. Novelty remains **unverified**.

## 1. Full structural cancellation remains incomplete

**Severity:** milestone blocker. **Target:** cancellation of every negative
literal determinant object for `[e_(5,1)]` at n=6. **Verdict:** incomplete.

The structural union has 151 sources against 3,980 negative objects on the
132 natural unit interval orders. It covers all 19 hook sources, all 96
two-row sources, and 36 conditional `(2,2,1,1)` sources. The 3,829 remaining
sources have shapes `(3,1,1,1)` or the complement of the conditional domain
in `(2,2,1,1)`. These counts were reconstructed independently.

The finite family permitting three moved labels matches all 3,980 sources,
as reproduced from the frozen code. That algorithm enumerates the complete
positive families, uses a global matching state, and retains a reverse
dictionary. It does not supply the intrinsic structural map required by the
research objective. Also, complete matching in that graph does not by itself
prove that the prescribed 151 structural pairs extend to a complete matching
in the graph after deleting their endpoints. The author correctly disclaims
this extension; the review does not silently assert it.

**Decisive repair:** give entrywise rules on the remaining two source domains,
with image recognition in the complement of the 151 recognized tagged images,
or give and prove a different coherent structural rule on the entire source.
Finite matching alone does not close this obligation.

## 2. Theorem A survives full semantic review

**Severity:** informational, valid scoped result. **Target:** the weighted-set
injection for every strict finite poset on n>=6 distinctly numbered labels.
**Verdict:** supported; **status:** proved with distinct ordinary semantic
review, without formal certification. This statement uses the stated tableau
and graph-inversion definitions and does not require a natural labeling.

I checked forward validity, degree, disjointness, exact image predicates, and
both literal round trips in all cases of the supplied argument:

- For the hook, if the prefix endpoint x is below z and y,z are comparable,
  the union is one chain. Its two possible hook antecedents belong in the two
  distinguished one-row copies. Their printed entry formulas recover exactly
  those two antecedents. Outside that case, the leg insertion changes graph
  order only across pairs already comparable in P.
- On a valid `(n-2,1,1)` target `(A;s;t)`, the H1 conditions reconstruct
  `(A,t);s` and exclude the one-row branch by `not x<s`. The H2 conditions
  reconstruct `(A,s);t`. In H2, a hypothetical `t<A[0]` would imply `t<s`,
  contradicting incomparability, so the recovered source's first-column
  condition really follows. These are the only two possible hook extractions.
- Splitting `(A);(a,b)` collides with that hook image precisely when
  `x<b` and `not x<a`. Its separate second-column condition `not b<A[1]`
  is retained by the inverse; it is not implied merely by target validity.
- In the `a<x` branch, the rotation to `(A[:-1]);(a,x);b` is valid and crosses
  only comparable pairs. The recognizer `R[-1]<t<z` reconstructs the original
  chain and the branch condition from target validity and transitivity.
- In the incomparable branch, the rotation to
  `(A[:-2],b);(w,x);a` keeps the possibly incomparable pairs `(a,w)` and `(a,x)`
  in their original strict row order. Every other changed pair is comparable.
  For its inverse, `R[-2]<s`, `t<R[-1]`, `z<R[-1]`, and `z` incomparable with
  `t` reconstruct the arm chain, the bottom pair, and both source columns.
  In particular, `z<R[0]` would force `z<s`, contradicting target validity.
  The prefix contains at least two entries for n>=6; this ensures the recovered
  second-column condition against b. The proof does not extend this branch
  through n=5.

The two `(n-3,2,1)` image languages are disjoint because one requires `t<z`
and the other incomparability. The hook and ordinary split languages are
disjoint by their explicit collision condition. All formulas terminate after
bounded entry operations. The executable implementation agrees with these
formulas on its declared valid domains; invalid arbitrary arrays are outside
the theorem's input contract.

Independent finite support: all 132 natural unit interval orders at n=6,
including every positive target for exact image recognition, passed. An
additional 248 distinct relabeled general posets at n=6 passed 772 structural
source checks. These extra sanity cases support implementation agreement;
they do not replace the n>=6 argument above.

## 3. The conditional three-label triangle also survives review

**Severity:** informational, valid conditional result. **Target:** Theorem B
under every printed relation, incomparability, and numerical inequality.
**Verdict:** supported on its stated conditional domain; **status:** proved
with distinct ordinary semantic review, without formal certification.

For `S0`, the only newly separated row pair is comparable, so its image K is
valid with unchanged degree. For `S1`, transitivity gives the chain `u<c<b`
and the second-row chain `a<v`. The incomparable pair c,v validates column
two. If `d<a`, then `d<c`, contradicting the assumed column boundary, so the
new final row is valid as well.

The only changed incomparable-edge orders are `{c,v}` and `{v,b}`. With
`c<v<b` numerically, the former removes one inversion and the latter adds
one. All other moved crossings are comparable, or remain in the same strict
row order; d remains below every other entry. Thus the numerical hypothesis
is load-bearing and is preserved in both the proof and code.

Both source branches and both target languages recover all six named labels
directly. The source branches cannot overlap, because they require opposite
strict P-orders between the second-row endpoint and the third-row entry.
The target J avoids Theorem A's first rotation language since it would
require `b<v`, and avoids its second language since it would require `c<a`.
Both contradict the stated hypotheses. K has a separate target shape.

The smallest displayed Hall component was checked independently by deleting
the same single label from source and target and comparing the retained
ordered row blocks, allowing all whole-row permutations. At
`h=(1,2,4,5,6,6)`, both degree-one sources
`14/23/5/6` and `14/25/3/6` have exactly the same sole positive neighbor
`14/2/3/5/6`. Hence the one-label family fails by the exact inequality 1<2,
regardless of greedy choices. The extra target `135/24/6` is valid, has degree
one, and is outside that neighborhood. This supports the specific three-label
routing clue. It establishes no universal multidimensional Ferrers cut/glue.

**Decisive extension test:** any enlarged triangle domain must reprove the
two-edge inversion balance and exact image exclusion. Dropping the numerical
or incomparability conditions without that proof is not justified.

## 4. The finite inventory and external count correction are supported

**Severity:** informational, scope and provenance. **Verdict:** supported
empirical finite exact evidence; no universal positivity conclusion.

The critic independently implemented row/column tableau backtracking,
incomparability inversion counting, and recursive signed determinant expansion.
It reconstructed all raw sectors through six, including all 85 raw n=6
occurrences and precisely nine for e51. The two T6 sectors have the printed
distinct permutations; removing the copy tag would change the problem.

Comparison with the pre-existing direct proper-coloring/subset oracle agreed
for all 197 vectors through n=6, with nonnegative coefficient polynomials in
this finite range. Counts by size are 1,1,2,5,14,42,132. Inspection of the
external script confirms that it loops over size five while printing “ALL
65”; the correct statements are 42 at five and 65 through five. Its global
`used_pos` set is present in the code. Its successful finite assertions cannot
be relabeled as a structural inverse or a size-six verification.

The unchanged candidate program reproduced 3,955/3,980 matches for the
one-label family (25 unmatched across 12 vectors), and 3,980/3,980 for both
the three-label family and unrestricted degree-fiber family. The independent
structural reconstruction found 151 valid, degree-preserving, distinct images
and exactly 151 recognized positive targets. Discovery already exposed these
inputs; no held-out evaluation is claimed.

## Reproduction and resources

- `tableau-check.py` and `tableau-result.json`: independent finite reconstruction.
- `tableau-hall-check.py` and `tableau-hall-result.json`: independent Hall witness.
- `tableau-matching-reproduction.json`: unchanged frozen matching-code rerun;
  this is reproduction, not an independent implementation of its matcher.
- `tableau-dependencies.json`: frozen dependencies and independent checker pins.

All numerical calls used the fresh meter, labels `tableau-critic-independent`,
`tableau-critic-matching`, and `tableau-critic-hall`, and were confined to n<=6.
Those three subprocesses charged 4.3350 wall seconds, with no failures and peak
observed RSS below 31 MiB. Integrity closure is recorded separately if run.
All earlier closed ledgers remain untouched.

No correction pass is required for the presently stated Theorems A or B.
The full structural objective remains open for the explicit gap in finding 1.
