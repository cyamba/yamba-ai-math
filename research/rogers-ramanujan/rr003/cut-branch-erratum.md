# RR003 erratum to the rejected L proposal

The frozen cut-branch.md contains an index error in its final rejected
proposal: “suffix10 by(next4,6)” is not weight-preserving. Literally,
9i+10 -> (9(i+1)+4,6) increases weight by nine. For the actual L cut
j=0,D=(10), normalized weight10, appending the cost6 threes and applying
that written replacement yields weight25 instead of16. Thus the literal
written proposal already fails the weight invariant on this direct object.
The sentence claiming all its replacements preserve weight is incorrect.

The intended weight-preserving variant uses the **same-level** four:

    9i+10 -> (9i+4,6).

The other proposed replacements and compulsory 3j+2 threes are unchanged.
Its two displayed collision witnesses contain no suffix10, so they remain
exactly valid: L cuts (0,(6,6,6,8,8,8)) and (1,(11,11,11)) have actual
weight49, normalized weight42, and both give
(3,3,3,3,3,5,5,5,6,6,6), weight48 after the stated cost6.
The verifier now directly computes both corrected conversions as well as
the literal next-level weight failure. The weight-preserving variant is
still refuted for information loss; neither version is a final algorithm.

The K-to-P3 forward map, its intrinsic interval inverse, its universal
argument and all its implementation rules are unaffected. The original
frozen file and pilot receipt are preserved rather than silently rewritten.
This is an author correction, not another critic review or mechanism.
