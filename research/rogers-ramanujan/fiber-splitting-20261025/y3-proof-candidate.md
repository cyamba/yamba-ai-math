# Second frozen variant: the whole y=3 slab

Author argument before enumeration; separate review pending. Christopher
Yamba's fiber-splitting intuition is the originating approach. Novelty is
unverified. Frozen y2 files and first composition are retained unchanged.

Write C=(4,0,(x,x+t,x+t+3,x+t+3+z),()), x,t,z>=0, of weight
22+4x+3t+z. With x=2q+r the new exact outputs are:

| Branch | U |
| --- | --- |
| x=0 | 12,6,3^(t+1),1^(z+1) |
| x=1 | 12,8,6,3^t,1^z |
| x>=2,r=0 | 10,8^q,6^2,3^t,1^z |
| x>=3,r=1 | 10^2,8^q,6,3^t,1^z |

All supports are literal U: heights 12,10,8,6,3,1 are 7,6,4,3,2,1.
Every adjacent and terminal drop is <=4; mandatory intermediate columns
bridge each large height. The respective totals are 22+3t+z,
26+3t+z,22+8q+3t+z,26+8q+3t+z, as required.

The four languages are disjoint. For support contained in {12,6,3,1},
n12=n6=1,n3,n1>=1, recover (x,t,z)=(0,n3-1,n1-1).
For support contained in {12,8,6,3,1}, n12=n8=n6=1, recover
(1,n3,n1). For support contained in {10,8,6,3,1}, n8>=1 and
(n10,n6)=(1,2) or (2,1), recover (2*n8+n10-1,n3,n1).
Substitution proves both inverse laws and exact recognition.

Disjointness from retained H3 needs the actual earlier languages:

* The x=0 language has a 12 but no 9,8,10. Ordinary full multiple-of-3
  contours require 9 between 6 and 12. The sole relevant missing-level
  contour has 12 as its single top and requires at least two 6s; here
  there is just one. Mixed-marker and special-hole languages require
  8/10 or 17/19/26, absent here. Prior g3 has no 12. H2's additional
  planes have 15/17 or 8; its tails have 28. H3's low slabs containing
  12 also contain 8,9 or10, while its high-gap slab has >=2 twelves.
* The x=1 language has a single 12 and an 8, but lacks 9 and10 and
  has only one 6. In g2 the mixed contour would require the missing 9;
  isolated carriers cannot contain12. f1 and g3 with an8 contain only
  6/3/1 (or a mandatory9/10), not12. The H3 low slab with12+8 has no6;
  the other low slab has9/10. Again the high slab has>=2 twelves.
* For x>=2, the marker set contains both8 and10, the maximum multiple
  is6 and its count is just1 or2. The g2 mixed contour requires>=3
  sixes. Its special holes lack8. f1 has no simultaneous8+10;
  g3's simultaneous8+10 case has exactly one10 and at most one6,
  unlike either new branch. H3's simultaneous8+10 low slab has no6;
  its other slabs require12/9. H2's extra planes/tails and H3's high
  slab have larger mandatory markers absent here.

The y2 extension has no12 and never simultaneous8+10, so is disjoint.
The funded encoding for 4<=y<=17 has at least six tens, so is disjoint.

Thus H3 plus whole y2 plus whole y3 plus the funded band y=4..17
is a coherent restricted extension. To enforce this, V2 excludes alternate
funded y=3 images in BOTH directions. The older V1 map remains a separate
valid restricted alternative; V2 retains all H3 and y2 assignments.

## Failed naive variant retained

Before this construction, the natural even-x formula
8^(q+2),6,3^t,1^z was rejected algebraically: whenever z>=2, it equals
the y2 output with x'=2q+1,t'=t,z'=z-2. At weight24, sources
(0,0,3,5) and (1,1,3,3) would both give (8,8,6,1,1).
Adding a name/dimension erased by flattening cannot separate them.
The successful new y3 formulas change the literal column language instead.
