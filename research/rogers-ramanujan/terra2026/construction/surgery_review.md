# Independent semantic review of local bidegree surgery

Reviewed 27 October 2026: `theory/local_surgery.md`, SHA256 `61498d5b52d31955071efc510044c7e11398b75119be8cb9ab8905ab50b85c03`, and `theory/local_surgery.py`, SHA256 `b0ecccc30e440172872653f4c064e48d0c0b6e137fe17047173846cfe1bc0a67`.

**Conclusion:** the advertised local bijection, inverse, weight preservation and stated residue specialization are sound as written, subject to integer/nonnegative domains and visibly retained branch/context. This is a written semantic review, not Lean certification and not a review of novelty. It does not establish a global KR1 map. I did not independently validate the manuscript's literature claims or the all-n C_n expansion, whose source-derived cut denominators need a separate primary-source check.

## Independent argument

Fix bidegree (X,Y). A source has c in the entire interval 0,...,min(floor(X/2),Y), with a=X−2c and b=Y−c. For type 0, admissible f has parity r=X mod 2 and lies in [0,min(X,Y)], yielding p=max(0,floor((min(X,Y)−r)/2)+1) choices. Hence c=0,...,p−1 produces all and only type-0 states, uniquely. Given f, the nonnegative d=Y−f and e=(X−f)/2 are forced.

For type 1, the output bidegree equations force f=Y−g and 2e=X−1−Y−g. Thus admissible g lies in [0,min(Y,X−1−Y)] and has parity h=(X−1−Y) mod 2. Its count equals the number of unused source c's: if Y≥X both counts vanish; if Y≤floor(X/2), the admissible f and g parities partition the Y+1 integers 0,...,Y (or have equal counts when Y is odd); if floor(X/2)<Y<X, direct parity calculation gives p plus the type-1 count equal to floor(X/2)+1. This covers X=0, Y=0 and empty type-1 intervals. Consequently g=h+2(c−p) is valid precisely for the remaining c and traverses every type-1 state once. The inverse reads c from the progression index, then uniquely reconstructs a,b. Both x- and y-exponents match termwise, so any fixed positive integer specialization is weight preserving. Every call uses finitely many arithmetic operations.

Under x=q^(9j+2), y=q^(9k+3), the manuscript's three input values and four possible output values follow by direct addition. The theorem assumes separate labeled context for any overlapping species and the output branch bit. It therefore does not show that sequential applications admit an untagged global inverse or terminate under a global schedule. In particular, no coverage of the KR1 gap class follows.

## Executable check and limitations

I ran `python3 research/rogers-ramanujan/terra2026/theory/local_surgery.py`; output was `checked 27000 source triples and both output branches with bounded coordinates`. The script validates both compositions on its enumerated boxes and the two degrees on its source box. The source proof, not this finite execution, supplies the all-parameter result. The unreviewed remaining manuscript sections make separate automaton, asymptotic, source-comparison and C_n statements; no acceptance of those follows from this review.
