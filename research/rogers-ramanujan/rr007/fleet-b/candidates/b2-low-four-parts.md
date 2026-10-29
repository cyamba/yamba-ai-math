# Frozen B2: a universal restricted four-part correspondence

Frozen 24 October 2026, about21:06 UTC, before any B2 trial. **Full KR1 is
unresolved.** This is a new, coherent partial assignment, not a union with
Fleet A's partial assignment or every older RR003 assignment.

Let B0 be all ordinary partitions supported on{1,3,6,8}. Write an input as
`(8^m,6^n,3^t,1^s)`, m,n,t,s>=0. Let C be the exact ascending, zero-padded
domain from the contract. The C image I is the following disjoint intrinsic
union; membership also requires literal C validity:

1. Empty.
2. a=1,b=0, arbitrary mu; or a=0,b=1, arbitrary nu; or a=1,b=1, arbitrary
   mu,nu.
3. a=2,b=0 and mu_1=0 or mu_1 mod3 in{1,2}.
4. a=3,b=0 and (mu_2-mu_1) mod3 in{0,1}.
5. a=4,b=0, mu_1 even, and mu_3-mu_2 divisible by3.

## Forward map

* m>=2: K=2m-4; return `(4,0,(K,K+t,K+t+3n,K+t+3n+s),())`.
* m=1,t=0: return `(2,0,(2+3n,2+3n+s),())`.
* m=1,t>=1: return `(3,0,(t-1,3n+t,3n+t+s),())`.
* m=0,n>=1,t=0: return `(2,0,(3n-2,3n-2+s),())`.
* m=0,n>=1,t>=1: return `(3,0,(t-1,3n+t-4,3n+t-4+s),())`.
* m=n=t=0: return empty if s=0; otherwise `(1,0,(s-1,),())`.
* m=n=0,t>=1,s=0: return `(0,1,(),(t-1,))`.
* m=n=0,t=1,s>=1: return `(2,0,(0,s-1),())`.
* m=n=0,t>=2,s>=1: return `(1,1,(s-1,),(t-2,))`.

## Inverse map, using only C

* Empty gives m=n=t=s=0.
* a1,b0: s=mu_1+1 and m=n=t=0.
* a0,b1: t=nu_1+1 and m=n=s=0.
* a1,b1: s=mu_1+1,t=nu_1+2,m=n=0.
* a2,b0, k=mu_1: s=mu_2-k. If k=0 instead use s=mu_2+1,t=1,m=n=0.
  If k=1mod3, use n=(k+2)/3,m=t=0. If k=2mod3, use n=(k-2)/3,m=1,t=0.
* a3,b0: put d=mu_2-mu_1,t=mu_1+1,s=mu_3-mu_2. If d=0mod3 use
  m=0,n=d/3+1; if d=1mod3 use m=1,n=(d-1)/3.
* a4,b0: m=mu_1/2+2,t=mu_2-mu_1,n=(mu_3-mu_2)/3,s=mu_4-mu_3.

Reject C outside I. Form the literal B0 partition from its four counts.

## Universal proof, assurance and first falsifiers

**Proved, author-only.** Every forward vector is ascending and nonnegative;
the potentially tight case m0,n>=1,t>=1 has second-minus-first entry3n-3>=0.
Its exact length is displayed. Substitution into
`Q=a^2+3ab+3b^2+sum(mu)+3sum(nu)` gives `8m+6n+3t+s` in each branch.
For example the a4 branch has Q=16+4K+3t+6n+s=8m+6n+3t+s;
the two a3 branches have respectively Q=8m+6n+3t+s with m=0,1.
The other branches are direct substitutions of one or two entries.

The inverse branch tests are disjoint and exhaustive on I. The displayed
formulas are nonnegative integers by the membership congruences, and their
substitution recovers every input coordinate. Conversely each forward
branch has exactly its named inverse test. This proves both identities
universally, without coefficient counts or any finite/rank matching.
Both algorithms perform a bounded number of integer arithmetic operations
and output a finite literal list, so they terminate.

The construction extends the separately reviewed empty-F-root assignments
on m0. For m1 it uses root `(2,0,(2,2),())`; for m>=2 it uses the uniform
root `(4,0,((2m-4)^4),())`. Their root membership follows from the RR006
grammar, but the direct formulas above do not require the strip theorem
for their correctness. The a4 cone is an artificial choice of an infinite
root family and does not establish a universal or canonical C parser.

Smallest falsifiers: empty; t1,s1 (a2 zero padding); n1,t1 (a3 zero
boundary); m1 atweight8; the first a4 image m2 atweight16. The pilot checks
all actual B0 and C-image objects through12, both identities, exact image,
weight and both distinct/repeated predicates. Weight16 is not executed in
the pilot. Any extension through30 needs explicit root approval after it.
Script: `.runs/rr007/b2-low-four-parts.py`.

## Cross-fleet incompatibility, not an overlay

On the source intersection with Fleet A's a0/1 construction, these formulas
agree: a0,b1,nu=v gives3^(v+1); a1,b0,mu=u gives1^(u+1); a1,b1 gives
3^(nu+2)1^(mu+1). This does **not** justify taking a union of the maps.
Their images collide atweight12: Fleet A maps C=(0,2,(),(0,0)) to
B=(3,3,6), while B2 maps that same B to C=(3,0,(1,1,1),()). The two C
objects are distinct and valid. Thus the A2/B2 union is noninjective.
Preserve both coherent partial results and this exact incompatibility.
