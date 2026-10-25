# Repair after the third-12 collision

Status before checking: author mathematical argument; separate review pending.
The previous `y3_extension.py` is REFUTED by U=(12,6,3,1), weight22.
Old H3 C=(3,0,(2,5,6),()) and proposed new C=(4,0,(0,0,3,3),())
both map there. The omitted old f1 third-12 language invalidates every
previous x=0 branch. It is retained unchanged as failure evidence.

Keep only the three x>=1 branches that the separate critic supported.
For x=0, C=(4,0,(0,t,t+3,t+3+z),()), weight22+3t+z, replace the
refuted branch with:

| Branch | U |
| --- | --- |
| t=0,z<=1 | 8^2,6,1^z |
| t=0,z>=2 | 9^2,6,1^(z-2) |
| t=1,z=0 | 8^2,6,3 |
| t=1,z>=1 | 10^2,3^2,1^(z-1) |
| t=2 | 9^3,1^(z+1) |
| t>=3 | 12,9^2,3^(t-3),1^(z+1) |

All are valid literal U: heights of12,10,9,8,6,3,1 are7,6,5,4,3,2,1.
Mandatory6/3/1 bridge every drop to at most4, including the terminal drop.
Weights are respectively22+z,24+z-2,25,26+z-1,27+z+1,
30+3(t-3)+z+1; these are exactly22+3t+z.

The exact inverse is given by mutually disjoint support/count languages:

* n8=2,n6=1, support8/6/3/1: n3=0,n1<=1 gives(t,z)=(0,n1);
  n3=1,n1=0 gives(1,0).
* n9=2,n6=1, support9/6/1 gives(0,n1+2).
* n10=n3=2, support10/3/1 gives(1,n1+1).
* n9=3,n1>=1, support9/1 gives(2,n1-1).
* n12=1,n9=2,n1>=1, support12/9/3/1 gives(n3+3,n1-1).

Substitution proves both inverse laws. Each x=0 language is disjoint from
the x>=1 languages (which have either12+8+6, or10+8). Disjointness from
the first y2 extension: its 8^>=2+6 branch requires at least two ones,
unlike the small uncarried language; its other 8 branch has two6s. Its
double10+3 branch has exactly one3, unlike two here; its other double10
branch requires6. Its 9-languages require10. Funded y4..17 has>=6 tens.

Exclusion from H3, checking the previously omitted f1 branch explicitly:

1. The 8^2+6 language cannot be any single8 f1/g3 carrier. Mixed g2
   at top6 requires>=3 sixes, unlike one. Old low slabs with only8/3/1
   have no6. Other H3 slabs require12 or10.
2. The 9^2+6 language has no3. f1 A2/wall require a full lower contour,
   f1 third-9 has no6, and third-12 requires12. Corrected b1 at q=0
   requires exactly one9 when6 is present. g3's multiple9+6 branch
   requires at least one3. g2's relevant9+6 hole needs>=2 threes;
   its other9 carrier has one9. Additional H3 slabs require8,10,12.
3. The 10^2+3^2 language has too few3s for a g2 mixed top3 contour
   (requires>=3), and no6 for its double10 hole. f1/g3 have at most
   one10. H3 low slabs also have one10 with8 or12; high requires12.
4. The 9^3+ones language lacks the full lower3/6 contour and has
   neither the one9 of f1 nor the two9s of the special b1/g3 language.
   Mixed/hole g2 requires absent markers or lower columns.
5. The 12+9^2 language has no6, excluding f1 third-12 explicitly;
   it lacks the full lower multiple contour. All g2 special holes have
   compulsory17/19/26 or6, absent here, and g3 has no12. H3's low
   12+9 slab has exactly one9; high has>=2 twelves.

For all five cases, H2's additional a5 planes have15/17, its large-b
tail has28, and its a4 plane has8; all are absent or otherwise excluded.
Thus the repaired x=0 languages and the separately supported x>=1 rules
give the entire y=3 slab disjoint from H3 and y2. The V3 composition
excludes the old refuted x=0 language and alternate funded y2/y3 images
in both directions. This is still a restricted theorem, not full KR1.
