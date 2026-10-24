# RR003 middle source state: a source-derived positive model

**Proved algebraic interpretation at author-only assurance; not a branch
bijection.** Reinspection of [Xia, Lemma2.2 and (3.6)-(3.7)](https://arxiv.org/html/2609.08816v1)
gives the following specialization. This is existing source machinery,
not a new analytic identity or third mechanism.

Let X consist of (j,k,D), 0<=j<=k, weight9(j+k)+|D|. D permits:

* common residue parts3,6 modulo9, except literal3 and6;
* parts9i+5,9i+13 for0<=i<=j, except literal5;
* parts9i+8,9i+10 forj<=i<=k;
* parts9i+11,9i+7 fori>=k.

The six non-common residue classes are distinct; repeated cuts introduce
no hidden colors. Empty D and j=k=0 are permitted.

In Lemma2.2 set n=2,d=9,c=18 and r=(5,8,11). Its three denominator
ranges are exactly those above. In (3.6), the factors1-q3 and1-q6 cancel
from the common denominator;1-q5 cancels because the first range always
contains its literal5. The charge is9(j+k). Thus g.f.(X)=A2 universally.
By (3.7), normalized L disjoint-union a five-unit shift of X is a positive
literal model for B1, the desired middle source state H_(1,2).

A verification-only enumerator in reproduction/middle_source.py checks
source coefficients; no branch map is implemented or separately audited.
No matching map into the P3 complement, decreasing all-n recursion or complete KR1
bijection follows. The next branch obligation now starts from an explicit
middle source family, rather than an unspecified series.
