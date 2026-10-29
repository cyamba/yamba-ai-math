# Reserved correction: the quotient cut's exposed bottom boundary

25 October 2026, Europe/Stockholm. This supersedes only the erroneous
terminal-bound/range sentences concerning candidate 3 in the initial
`author.md` and `notebook.md`. Those files, their initial scripts, results
and freezes remain unchanged. The exact C grammar, lower-sheet failure,
triple-row failure and lattice norm statement are unchanged.

**Refuted initial claim.** I incorrectly said that after taking
`floor(h_i/3)` and dropping zeros the child's terminal decoded height must
be at most one, and therefore that child U=`(3)` was globally impossible.
The distinct KR critic found the counterexample parent U=`(10,3)`, decoded
heights `(6,2)`, weight 13. It is valid five-flat, including its terminal
two. Its quotient heights are `(2,0)`, so after dropping zero its child is
exactly `(3)`. I overlooked that removing the zero quotient tail can expose
an earlier positive quotient. The original 40-bound numerical checks did
not assert the false terminal bound and do not validate it.

## Correct intrinsic bounds and exact minimum

**Proved, author correction, pending distinct final review.** Every nonempty
quotient child has terminal decoded height at most **two**. If the source
has no vanished quotient rows, its last original height is at most four,
so its last quotient is at most one. Otherwise let H be the source's last
height at least three, followed by vanished height K in `{1,2}`. Source
flatness gives `H-K<=4`, hence `H<=6`, so `floor(H/3)<=2`. Equality can occur
only at `H=6,K=2`. Thus the correct boundary includes the precisely
recoverable exposed pair `(6,2)`. Adjacent positive child quotient drops
remain at most two because the source drops are at most four; removal of
zeros changes only the bottom boundary.

In particular, the **minimum parent weight for child U=`(3)` is 13**. This
child has exactly one positive quotient row, of quotient two. Its original
height must be H=6 and must be followed by K=2 as just proved. Their literal
U row weights are F(6)=10 and F(2)=3, giving a lower bound 13. The critic's
parent `(10,3)` attains it. Other lower rows can only increase the weight.
This is an exact paper minimum, not an inference from a finite absence.

The weight-nine commutation obstruction therefore survives in this narrower
form. C parent `(3,0,(0,0,0),())` has weight nine and exact triadic child
`(0,1,(),(0))`, whose retained g2 and H1 images are U=`(3)`. No parent U of
weight nine can quotient to `(3)`, since every such preimage has weight at
least thirteen. The former assertion of global exclusion of `(3)` is
withdrawn.

## A genuine global exclusion for this fixed cut

The distinct KR critic also proposed the following stronger replacement;
I independently checked the actual g2 and H1 values and the C edge.
The quotient child's terminal decoded height at most two **globally excludes
U=`(6)`**, whose decoded height is three. C parent
`(0,2,(),(1,1))`, of weight eighteen, has exact child
`(2,0,(1,1),())` of weight six and zero boundary residual. Both the actual
reviewed g2 implementation and the retained H1 implementation send this
child to `(6)`. Consequently no parent U at any weight can make the fixed
quotient cut produce the required retained child in this C edge. This
globally refutes this particular cut as the requested compatible recursive
lift. It does not exclude other cuts, boundary transport, a changing
embedding, or a different U/C construction.

The quotient plus full ordered remainder word is still an exact one-sided
carrier: retain the original row count, reconstruct positive quotients from
the child and pad their trailing zeros, then set `h_i=3q_i+r_i`. Admission
requires the restored positive heights to be descending and five-flat,
including the terminal. The original child/ordered remainder word is then
recovered exactly. Its large boundary language has not been identified with
the C grammar's nonthree gaps and trits.

## Verification, preservation and assurance

`revision-check.py` is a new check of the **same** frozen candidate family;
no new cut family was added. It checks all literal U through 12, then 30,
then 40, including the true terminal bound, the exact exposed `(6,2)`
condition when quotient tail is two, child `(3)` minimum, and the genuine
global child `(6)` exclusion. It directly verifies both C edges above and
their actual g2/H1 child values. Maximum input/output weight is forty.
It preserves every earlier numerical result and explicitly records the
initial false claim. `revision-prepilot-freeze.json` pins this correction
and its script before those checks. `revision-freeze.json` pins the final
correction artifacts and verifies all original handoff hashes unchanged.

Universal assurance of these repaired arguments remains ordinary author
proof pending the distinct critic's reserved final review; no formal prover,
new source retrieval, external service, dependency or additional cut was used.
