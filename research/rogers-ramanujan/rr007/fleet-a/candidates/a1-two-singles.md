# A1 frozen partial bijection: all two-single C data

Version A1, frozen before any trial. Author-only assurance pending the
reserved critic. This is one of the at most three Fleet A rule variants.
It is an infinite partial bijection, not a proposed full-root parser.

## Exact forward and inverse definitions

The C domain is exactly
`C(k,s)=(2,0,(k,k+s),())`, integers k,s>=0. Its weight is4+2k+s.
Define the C-to-U direction by this disjoint arithmetic case split:

| k condition | U output |
| --- | --- |
| k=0 | `(3,1^(s+1))` |
| k=3m-2, m>=1 | `(6^m,1^s)` |
| k=3m+2, m>=0 | `(8,6^m,1^s)` |
| k=3, m=0 | `(9,1^(s+1))` |
| k=3m+3, m>=1 | `(10,6^m,1^s)` |

Every displayed U is sorted descending and superscripts mean literal
multiplicities. The U domain/image is exactly the union of those five
intrinsic predicates: respectively one3 with at least one1 and no others;
at least one6 and otherwise1; one8 and otherwise6/1; one9 with at least
one1 and no others; one10, at least one6, and otherwise1. The displayed
exceptional8/9/10 occurs exactly once. All other multiplicities are as
stated. The five predicates are disjoint.

The U-to-C direction recognizes its sole branch, counts sixes and ones,
and reverses the row formula. In branches1/4 the number of ones is s+1;
in the others it is s. In branches2/3/5 the six-count is m and k is the
displayed linear expression. Objects outside the stated domain are
rejected, not matched by enumeration or silently filtered.

## Universal author proof

**Proved, author-only elementary argument.** The k cases partition all
nonnegative integers:0 separately, then residues1,2,0 modulo3 with the
displayed lower bounds. Each output is literal U. The decoded heights of
1,3,6,8,9,10 are1,2,3,4,5,6. Branches1/2/3 have consecutive nonzero levels
among4,3,2,1 with largest gap at most3 and terminal gap at most4. Branch4
has the gap5-1=4. Branch5 has the gap6-3=3 and at least one height3, so its
terminal gap is at most3; optional ones preserve validity. This proves
validity including the tail and every repeated case.

The U weights in the five branches are `4+s`, `6m+s`, `8+6m+s`, `10+s`,
and `10+6m+s`; substitution gives4+2k+s in every case. The disjoint U
image predicates recover the branch, and the literal multiplicities recover
m,s uniquely. The arithmetic inverse therefore recovers k,s and reconstructs
every stated U exactly. This proves both inverse identities and exhaustive
coverage of precisely the stated partial domains, without a counting
identity. Both algorithms terminate by scanning at most the literal input
length and writing the finite output; counts and arithmetic require no
search or saved path.

## Relation to the reviewed strip normal forms

For k=0 the strip counts are `(n1,n3,n6)=(s+1,1,0)` and the F_C root is
empty. For k=3m-2 they are `(s,0,m)`, again empty. For k=3m+2 the root is
`(2,0,(2,2),())` and the counts are `(s,0,m)`. For k=3m+3 the root is
`(2,0,(3,3),())` and counts are `(s,0,m)`. On U the displayed branches are
exactly the R6/R1 reconstructions from empty, (8), or (9,1), with the
specified exceptional k=0 R3 step. Thus this is consistent with the
reviewed empty-root map where they overlap; it adds two root correspondences
and yields an intrinsic full two-single family, not a union with RR003
incompatible assignments. Including empty, three root pairs are recognized;
all complementary roots, already `(9,3)` at12, remain unresolved.

The exact boundary slide `(8,1,1)<->(9,1)` from context.md corresponds here
to `(2,0,(2,4),()) <-> (2,0,(3,3),())`: a weight-preserving balancing
of the two mu entries. This is a local structural check, not the derivation
of a full U/C insertion algorithm.

Distinctness is side-specific. In C(k,s) the two increments repeat exactly
when s=0. In U, repetition depends independently on the one/six counts.
For example k=2,s=2 has repeated U `(8,1,1)` but unequal increments(2,4);
k=1,s=0 has distinct U `(6)` but repeated increments(1,1). No literal
A/B distinctness-preserving theorem is proposed.

Smallest global falsifier of calling this a full map: the F_U root `(9,3)`
and F_C root `(0,2,(),(0,0))` at12, outside the two-single domain/image.
Smallest branch-boundary falsifier if branch4 omitted its extra one is
k=3,s=0: output(9) would fail literal terminal validity and have wrong weight.

## Frozen trial and resource boundary

Named script: `.runs/rr007/a1-two-singles.py`. Initial pilot enumerates
complete literal U/C inputs through12, tests both maps on precisely their
domains, exact image predicates, weights, validity, both inverses and the
reviewed normal forms, and reports distinct/repeated cohorts. Every actual
input/output is at most12. Higher symbolic branches are not executed by
the pilot. No extension is authorized in this file; root must record a
named unchanged extension through30 after a passing pilot. No above30
execution, new dependency, provider, retrieval or external action.
