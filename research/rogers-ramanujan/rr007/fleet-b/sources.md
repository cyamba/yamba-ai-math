# Fleet B source handoff

2026-10-24, completed at about 20:50 UTC. Author: source scout, dispatch proxy 2.
This is a construction handoff, not a separate semantic review. No new finite
enumeration, provider call, dependency, external message, or publication ran.

**Result.** Konan supplies an explicit general flat/regular algorithm. Its
natural five-color specialization gives the already known **U/B endpoint**.
An intrinsic exact encoding of full C into a compatible colored family is
still missing. The simplest sector-to-one-word proposal is refuted below.
Recent primary preprints claim analytic proofs of the exact KR1 sum/product
identity; this limited search did not locate a full explicit KR1 partition
bijection. Neither absence nor novelty has been established.

## Source record B-S1 and inspection boundary

I. Konan, *Weighted words at degree two, II: flat partitions, regular
partitions, and application to level one perfect crystals*,
[arXiv:2002.00300v2](https://arxiv.org/html/2002.00300v2), journal version
EJC 29(1), P1.54 (2022). Inspected: grounding and flat/regular definitions;
Definition 2.1; Theorem 2.8; degree-one construction in sections 4.1–4.3,
including formulas (4.3)–(4.17), size double counting, and most validity
argument. **The final section-4.3 tail, HTML lines approximately 893–919,
was not exposed by the allotted opens.** No complete independent proof audit
or degree-two proof inspection is claimed. The formulas below are
mathematical data for the next author, with notation normalized to avoid
the displayed indexing ambiguities. Applicability to C remains unverified.

## Exact degree-one interface

Choose a finite color set G, ground g, epsilon:G^2->{0,1}, and delta in
{0,1}, satisfying

```
epsilon(g,g)=0;
epsilon(g,c)=delta;
epsilon(c,g)=1-delta                 (c != g).
```

A grounded sequence ends in 0_g, with no preceding 0_g. Flat means adjacent
size differences equal epsilon; regular means differences at least epsilon
and all nonterminal colors differ from g. The theorem preserves raw total
size and the **ordered word after deleting g**, not merely color counts.
The trivial sequence (0_g) represents empty. Zero sizes of nonground colors
can occur; for delta=1 this prevents interpreting raw size as a positive
literal KR1 grading without a color specialization.

Let the retained word be c_0,...,c_(s-1), and put c_s=g. Define

```
M_i = sum_{j=i}^{s-1} epsilon(c_j,c_(j+1)).
```

Every regular sequence on that word has sizes R_i=M_i+nu_i, where nu is an
ordinary partition with at most s parts, padded with zeros. This is both
the canonical regular encoding and its inverse. Keep s=0 separate.

### Flat to regular: executable formulas

Given a valid flat sequence, let b_i be the number of ground-colored parts
immediately before c_i (b_0 includes the leading block). There is no ground
block after the final nonground color: it would consist of forbidden 0_g.
For s>=1 set

```
D = {i: 1<=i<s and epsilon(c_(i-1),c_i)=0};
J = {i in D: b_i>0};
L_i = #{j: i<=j<s and (j not in D or j in J)}.
```

Construct a multiset p as follows. For i not in D, insert b_i copies of L_i.
For i in J, insert b_i-1 copies of L_i and one copy of L_i+i. For i in D\J,
insert nothing. Sort p in decreasing order; set nu to its conjugate, padded
to length s. Output R_i=M_i+nu_i in colors c_i, followed by 0_g. The
nonground sizes of the input equal
M_i+#{j in J:j>i}; ground size in occupied slot i is L_i. These equalities
are useful direct validity checks rather than additional state.

### Regular to flat: executable formulas

Compute nu=R-M and p=conjugate(nu). Index p from u=0. Set

```
T_i = delta+M_i+i;
z_u = p_u-u-1;
M'_i = M_i + #{u: z_u>=T_i};
t_u = p_u - #{i: T_i<=z_u}.
```

Retain the word c_i with sizes M'_i. Insert ground-colored parts of sizes
t_u in the unique positions compatible with their epsilon inequalities,
preserving the nonground word, then append 0_g. Equal ground parts are
indistinguishable. Do not globally reorder nonground colors under an
assumed transitive order: arbitrary epsilon need not define one. The
source proves the resulting sequence is flat. Both maps use finite sums,
counts, conjugation and insertion, so their algorithms terminate. Weight
conservation follows by cancellation of the same threshold incidences.
Mutual inversion and full validity are the remaining imported proof audit
obligations, including the uninspected tail identified above.

For s=0 both sides contain exactly (0_g). Never compute nu_0 or p from an
empty word using the nonempty formulas.

## A completely specified specialization already gives U/B

The following derivation is author-only, with Konan's generic theorem
imported as stated. It is not a candidate solution of the missing bridge.

Take colors 0,1,2,3,4, ground 0, and epsilon(r,t)=1 if r<t and 0 otherwise.
Then delta=1. For a U column height h=5k+r, use the colored part k_r.
Append 0_0. A terminal drop and every adjacent drop in 0..4 are exactly
the flat equations in these variables. Conversely h=5k+r recovers the
entire U object intrinsically, including ground-colored positive heights.

Write alpha=(0,1,3,6,8), and specialize a colored part's literal weight to
9k+alpha_r. This is exactly the cumulative periodic column weight
F(5k+r) for row weights (1,2,3,2,1). Konan preserves sum(k) and the
nonground word, so it preserves this literal weight. Regular output has
only r=1,2,3,4, with k>=0. Replacing k_r by 9k+alpha_r produces precisely
all parts in residues 1,3,6,8 modulo 9, with no extra restrictions.
The inverse recovers r uniquely from that residue and k by subtraction
and division by 9, then uses regular-to-flat and h=5k+r. Empty maps to
empty. This is the existing endpoint mechanism attributed in RR006 to
Andrews–Keith/Stockhofe, now exposed through Konan's degree-one interface.
It adds no C encoding and no F_U/F_C map.

Cross-fleet clue supplied by the root, not a literature result: A-context's
lossless three-column row for h=5k+r has entries
P_t=3k+clamp(r-t+1,0,3), t=1,2,3. Its five residue patterns retain the
same intrinsic residue r used above. A-context reports volume F(h) and
the U-drop criterion min_t(row difference)<=2, including terminal zero.
This may be a convenient geometric carrier for the five-color word, but
the full rows/word must remain recoverable; their reported area-only
compression already collides at weight 12. No new C specialization is
inferred here, and the A-context proof retains its own assurance level.

## A precise obstruction to the easiest C specialization

**Proved, author-only elementary argument; separate review required.**
Suppose each fixed (a,b) C-sector is encoded onto the *whole* regular
fiber for one finite nonground color word, with ordinary raw size as its
literal weight. This cannot work. The sector (a,b)=(0,1) consists of
nu=(n), n>=0, with weights 3+3n. A nonempty regular fiber has its
staircase M and also M+(1,0,...,0), whose weights differ by one. An empty
word has only one object. Neither fiber can equal that infinite sector.

The same contradiction survives a common affine specialization
w(k,c)=d*k+alpha_c, where d is a fixed positive integer. A fixed word
contributes a fixed offset and its residual weights attain all nonnegative
multiples of d. The (1,0) sector has weights 1+n and forces d=1; the
(0,1) sector has weights 3+3n and forces d=3. Therefore **a C encoding
must allow varying nonground words inside at least one sector, a proper
subfamily with proved closure, a more elaborate grading, or a different
theorem**. This lemma does not exclude any of those possibilities.
It is symbolic; no finite trial or large legacy witness was used.

## Current primary analytic leads: records B-S2 and B-S3

**B-S2.** Ernest X. W. Xia, *The modulo 9 Kanade–Russell identities and
their Nahm-sum duals*, [arXiv:2609.08816v1](https://arxiv.org/html/2609.08816),
8 September 2026. Inspected the primary HTML abstract, introduction start
and contents. It claims all five modulo-nine sum/product identities.
Contents describe recurrences, residue representations, certificates and
boundary estimates. **Proof not inspected or independently audited.**
No bijective algorithm was extracted. This is a current analytic proof
claim, not evidence of our construction or an audited theorem.

**B-S3.** Yuma Mizuno, *The three Kanade–Russell identities modulo nine*,
[arXiv:2609.09653v3](https://arxiv.org/html/2609.09653), dated 5 October 2026
(initial submission 9 September 2026). Inspected primary Theorem 1.1,
the following A-side equivalence paragraph, and contents. The displayed
first identity is exactly sum q^(a^2+3ab+3b^2)/((q;q)_a(q^3;q^3)_b) =
1/(q,q^3,q^6,q^8;q^9)_infinity. It attributes the difference-side sum to
Kurşungöz. Contents list bilinear identities, a Casoratian and a connection
formula. **Proof not inspected or independently audited.** No finite path
encoding or partition bijection was extracted.

Only two retained theorem leads: (1) use the explicit Konan interface while
actually constructing its C encoding; (2) inspect the new analytic proofs
for finite identities that may inspire such an encoding. Do not label a
new bijection novel from this limited search. The strongest competing
explanation for a purported colored-energy advance remains rediscovering
the U/B endpoint while leaving C unencoded.

Next author questions: can an intrinsic finite-color parser of C have an
exact, source-compatible image without smuggling a trace into its colors;
and does its proposed literal grading match both sides term by term,
including nonground zeros, terminal ground, and the empty object?
