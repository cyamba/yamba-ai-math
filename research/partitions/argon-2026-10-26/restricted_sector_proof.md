# An all-parameter theorem for the existing a=3,b=0 sector

Status: **written proof, supported by [separate semantic review](review-round1.md)**. Novelty is **not
verified**. This proves a restricted bijection onto an explicit image, not a
bijection from all clusters to all encoded columns and not KR1 itself.

## Exact definitions and statement

Use the literal definitions in `checks/kr1.py` and the composite lower-sector
map in `rr003_a2.py`. Let `U` be the descending positive column tuples whose
inverse prefix heights, including the final transition to zero, have every
drop strictly less than five. The column values 1,3,6,8,9,10 correspond to
heights 1,2,3,4,5,6 respectively.

For `C=(3,0,(s,s+t,s+t+d),())`, where `s,t,d` are arbitrary nonnegative
integers, its weight is `9+3s+2t+d`. Let `F` be exactly
`rr004_multidim_cones.reconstruct_a3_b0`, not a new repair. Define the core
`K(s,t)` by the following table. Exponents denote multiplicities, zero
multiplicities are omitted, and tuples are descending.

| Case | Domain | K(s,t) |
| --- | --- | --- |
| A | t=0 | `(6^u,3^v)`, with `2u+v=s+3`, `v` in `{0,1}` |
| B0 | t=1, s<=1 | `(8,3^(s+1))` |
| B1 | t=1, s>=2 | `(8,6,3^(s-1))` |
| C0 | t=2, s<=1 | `(10,3^(s+1))` |
| C1 | t=2, s>=2 | `(10,6,3^(s-1))` |
| D0 | t=3, s=0 | `(9,6)` |
| D1 | t=3, s in `{1,2}` | `(10,8,3^(s-1))` |
| D2 | t=3, s>=3 | `(10,8,6,3^(s-3))` |
| E | t=3q+1, q>=1 | `(9,8,6^(q-1),3^s)` |
| F0 | t=5, s=0 | `(9,9,1)` |
| F1 | t=3q+2, q>=1, `(q,s)!=(1,0)` | `(10,9,6^(q-1),3^s)` |
| G0 | t=3q, q>=2, `q<=3` or `s=0` | `(9,9,6^(q-2),3^(s+1))` |
| G1 | t=3q, q>=4, s>=1 | `(10,9,9,8,6^(q-4),3^(s-1))` |

**Theorem.** For every `s,t,d>=0`,

1. If `(s,t)!=(0,3)`, then `F(C)=(K(s,t),1^d)`.
2. If `(s,t)=(0,3)`, then `F(C)=(9,6)` for `d=0`, and
   `F(C)=(10,6,1^(d-1))` for `d>=1`.
3. These outputs are in `U`, have weight `9+3s+2t+d`, and are disjoint
   from the entire image of the specified lower-sector map for `a<=2`.
4. `F` is a bijection onto exactly the image family defined by (1)-(2).
   The existing `decompose_a3_b0` returns `C` on every output.

No assertion is made that this image exhausts `U` outside the lower sectors.
No assertion is made that other `a>=3` constructions avoid this image.

## Proof of the closed formula and validity

Inspect the five exceptional guards of `step_one` on the displayed cores.
The first guard, a tuple supported on exactly one 9 and positive 6s, is
satisfied only in D0: `(9,6)`. It changes this to `(10,6)`. None of the other
four guards is satisfied by any displayed core or any of its appended-one
successors. In particular, the guard with one 10, two 9s and small 3-count
requires *no 8*, while G1 has an 8. The guard with two 10s cannot occur.
The guards involving 17/19 cannot occur. The guard with one 10 and at least
two 6s cannot occur: C and D have at most one 6, and F1/G1 contain a 9.
After the exceptional D0 move, `(10,6)` has only one 6, so all subsequent
moves append a one. Every other case simply appends ones from the start.
This proves (1)-(2) directly from the code for arbitrary parameter values.

Every table core is valid. Heights are descending. All adjacent drops among
heights 1 through 6 are below five except potentially 6 to 1. That exceptional
jump never occurs: every core containing 10 also contains 8, 6 or 3 below it.
A core terminating at height 5 would also be invalid. D0 has a 6 below its 9;
E has an 8; F0 has a 1; F1 has a 6 or 3 because `(q,s)!=(1,0)`; G0 has a 3;
and G1 has an 8. Thus every core ends at a height below five. Appending ones
preserves validity. The exceptional `(10,6)` has heights `(6,3)` and is valid.

Summing each table row gives `sum(K)=9+3s+2t`. For A, use `2u+v=s+3`.
For E/F/G, substitute `t=3q+r`. In D0 the first exceptional move changes
weight 15 to 16 and later moves add one. This proves the weight statement.

## Exhaustive exclusion from the lower-sector image

We use the *forward* lower-sector families, so no assumption that an arbitrary
inverse recognizer is complete is needed. Inspection of `rr003_columns.py`,
`rr003_revision.py` and the additional templates in `rr003_a2.py` gives the
following exhaustive possibilities. Extra increments only increase the
stated multiplicities.

1. `a=0,1` have pure multiples `3,6,...,3b`, with at least two copies of
   each nontop level. `a=1` additionally has ones.
2. `a=2,mu[0]=0` has the same baseline plus one `3(b+1)` and ones.
   `a=2,mu[0]=1` has the baseline plus one `3(b+2)`.
3. `a=2,b=0,mu[0]>=2` has exactly one carrier 8 or 9, plus 6s and ones;
   the 9 carrier either has a positive one-count or exactly one 3.
4. Other ordinary mixed `a=2,b>0` families have markers `8^x,10^z`, with
   `x+z>=1,0<=z<=3`, and every level `3,...,3b`; the top level has at
   least three copies and every lower level at least two.
5. The additional hole templates either have a marker 17,19 or26, or are
   one of the following three small families:
   - one 9, one 6, at least two 3s;
   - one 10, at least two 6s, at most one 3, and positive ones;
   - two 10s, positive 6-count, at most one 3, and at least five ones.

Our image has no marker 17,19 or26 and never two 10s. It cannot equal the
last two small templates because its one-10-only families have at most one
6. It cannot equal the first because D0 has no 3, and every other family
with a 9 has another marker or two 9s.

For the remaining families, sort by the multiset of markers >=8:

- A has at least one 6, at most one 3, and `2c6+c3>=3`. A pure baseline
  reaching level 6 needs at least two 3s, except the exceptional pure 6
  output of `a=2,b=0,mu[0]=1`, which has exactly one 6. Neither matches A.
- B has one 8, positive 3-count, and either no 6 with at most two 3s, or
  exactly one 6. A b=0 carrier 8 has no 3. A mixed b=1 family needs at
  least three 3s; a mixed b=2 family needs at least three 6s; b>=3 needs
  a 9 or a larger multiple. None matches.
- C has one 10 and the same small 6-count pattern, so the same mixed
  baseline exclusions apply. No b=0 lower-sector family has a 10.
- D0 has `(9,6)` with no ones or 3s. It matches neither of the lower
  b=0 9 regimes and cannot contain a full lower baseline. Its successors
  `(10,6,1^(d-1))` also fail the mixed and hole-template baselines.
- D1/D2 have 10 and 8. When no 6 is present there are at most one 3;
  when a 6 is present its multiplicity is one. These again fail the b=1
  and b=2 mixed baselines, while larger b needs a 9 or larger multiple.
- E, F1 and G1 have both a 9 and a marker 8 or10. A mixed lower family
  producing a 9 has b>=3 and therefore needs at least three 9s (if b=3)
  or at least two 9s and a larger multiple (if b>3). E/F1 have one 9;
  G1 has two and no multiple larger than 6. None matches.
- F0 and its successors have two 9s and positive ones but no 3 or6.
  Every pure lower baseline producing two 9s needs both lower levels.
  The single-carrier and hole cases have exactly one 9.
- G0 has two 9s, positive 3-count, and either `c6<=1` or `c3=1`.
  A pure baseline reaching 9 with top multiplicity two needs both
  `c6>=2` and `c3>=2`. The separated-top `a=2` regimes and the hole
  template have exactly one 9, so those also cannot match.

This exhausts all forward lower families. Appended ones do not change any
of the exclusions, except the D0 distinction already treated explicitly.
Thus (3) holds for all parameters.

## Explicit recovery, injectivity and the code's inverse

All image rows have distinct multisets of entries >=8, except the following
pairs, which the listed conditions separate:

- C versus D0 successors: C has a positive 3-count; D0 successors do not.
- F0 versus G0: F0 has no 3 or6 and positive ones; G0 has a positive 3-count.
- B0/B1, C0/C1 and D1/D2: their 6-count separates them.

The marker-free family A has `d=c1`, `s=2c6+c3-3`, `t=0`.
B/C have `d=c1`; if `c6=0`, recover `s=c3-1`, otherwise `s=c3+1`.
The D0 source has `(s,t,d)=(0,3,0)`. Its successors have
`(s,t,d)=(0,3,c1+1)`. The other D families recover `s=c3+1` with no 6,
or `s=c3+3` with one 6, and always `t=3,d=c1`.
E has `q=c6+1,s=c3,t=3q+1,d=c1`.
F0 has `s=0,t=5,d=c1-1`.
F1 has `q=c6+1,s=c3,t=3q+2,d=c1`.
G0 has `q=c6+2,s=c3-1,t=3q,d=c1`.
G1 has `q=c6+4,s=c3+1,t=3q,d=c1`.
Each rule recovers a unique valid triple in its stated table domain and
reconstructs the original tuple. This proves injectivity and surjectivity
onto the *defined image family*.

Finally consider the existing greedy `decompose_a3_b0` implementation.
The [review soundness lemma](review-round1.md#appendix-soundness-of-the-literal-lower-inverse)
proves that whenever the literal lower recognizer accepts a valid tuple, its
returned cluster reconstructs that same tuple. Hence forward-image exclusion
also guarantees rejection by that recognizer; no global inverse completeness
is assumed here.
For every appended-one successor, `unstep_one` removes one: the predecessor
is in `U` outside the lower image by (3), and `step_one` reconstructs the
successor. It stops at the displayed primitive core. None of its exceptional
inverse guards applies to those cores, except the D0 successor `(10,6)`,
which is first reversed to `(9,6)`. In F0, removing the primitive terminal
one would yield `(9,9)`, which is not in U because its terminal height is5;
therefore the inverse correctly stops with one one still present. The
remaining branch table is exactly the recovery table above. Consequently
`decompose_a3_b0(F(C))=C` for every triple, proving (4).

## Computational support and limit

`sector_checks.py` independently transcribes the closed formula and inverse,
then compares them with the existing implementation on a bounded coordinate
box. It also checks validity, weight and lower-sector exclusion. This guards
against transcription mistakes; it is not the all-parameter proof.

The theorem concerns the literal lower-sector map in this repository, not a
canonical lower-sector notion for every possible KR1 bijection. Extending to
other a,b, compatibility with all other higher families, and exhaustive global
coverage remain open. No Lean formalization of this theorem has been supplied.
