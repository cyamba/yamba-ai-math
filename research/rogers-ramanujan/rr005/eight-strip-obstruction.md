# A tentative cost-eight continuation loses its branch

**Proposed exact refutation of two specified partial rules; review pending.**
This is a failed discovery continuation of the U–C strip route, not a
refutation of every cost-eight operator or the existence of a KR1 bijection.
No such operator was implemented or accepted. The rules and symbolic
falsifier below are frozen for the second review. Novelty is NOT VERIFIED.

On the F_C roots defined by the second proposal, consider the following
partial cost-eight rules, leaving any unlisted coordinates unchanged.

* P: from a=2,b>=2,mu=(1,1),nu=(t,tau), return
  (4,b-1,(1,t+2,t+2,t+2),tau), provided the result is a literal F_C root.
* Q: from a=3,b>=1,mu=(u,u,u),u>=b+1, return
  (4,b,(1,u-b,u-b,u-b),nu), provided the result is a literal F_C root.

Both have the intended cost eight. For P,
Q(4,b-1)-Q(2,b)=3, mu's sum changes by 3t+5 and 3|nu| by -3t.
For Q the base changes by 7+3b and mu's sum by 1-3b.
Sorted nonnegative coordinates alone do not make their images disjoint.

Two distinct **weight-thirty** F_C inputs are

    X=(2,2,(1,1),(0,0)),
    Y=(3,1,(3,3,3),(0,)).

They are roots by the literal predecessor tests: final mu entries and
final nu entries are equal, and the gap before the final mu pair is zero
(or k=1 at a=2,b>0), preventing a six predecessor. The exceptional empty
six image has b=0, so X is not that exception.

P(X) and Q(Y) are the same literal F_C datum

    Z=(4,1,(1,2,2,2),(0,)),  weight 38.

Z has equal final mu/nu entries and zero gap before its final mu pair,
so it is also an F_C root. Explicit weights are
Q(2,2)+2=28+2=30, Q(3,1)+9=21+9=30 and Q(4,1)+7=31+7=38.
Thus no union of exactly these two rules can be injective while retaining
both inputs. No scan priority repairs the overlap because their domains
are already disjoint. A replacement needs another recoverable distinction
or a coherent change to one/both rules and their global images.

The collision extends symbolically. Let r>=1 and let tau be a nonnegative
ascending length-r vector whose final entry equals its predecessor (use
zero for r=1). Choose 0<=t<=tau_1. Then

    (2,r+1,(1,1),(t,tau))
    (3,r,(r+t+2,r+t+2,r+t+2),tau)

are distinct F_C roots with the same weight, and the two tentative rules
both produce (4,r,(1,t+2,t+2,t+2),tau). All stated root tests and cost
identities follow from the same formulas. This is a written infinite-family
argument, not an enumeration, executable high-weight pilot or formal proof.

No corrected complete cost-eight operator or F_U/F_C matching was selected.
Even a valid injective cost-eight strip on both sides would only remove
another free count: its residual roots would still require a universally
invertible exhaustive match. The complete objective is unchanged.
