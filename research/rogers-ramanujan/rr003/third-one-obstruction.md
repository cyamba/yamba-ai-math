# RR003 exploratory third-one continuation: refuted

The frozen repaired map stops at t=2. A natural t=3 continuation was
examined algebraically, before selection or any purported validation run.
The attempted rules below are **refuted**, not implemented fallback rules.
They stay within mechanism B and do not constitute a third mechanism.

For a three-divisible gap core, all nonempty mu have minimum at least two
and all nonempty nu have minimum at least one. At a proposed cost-three
insertion try:

* If mu has minimum two or nu has minimum one, increase a by one, insert
  2 into the sorted vector mu-2, and replace nu by nu-1.
* Otherwise increase b by one, replace mu by mu-3, and insert zero before
  nu-2. Empty vectors are allowed in either formula where appropriate.

Both cost identities are exact. The first changes Q by 2a+3b+1 and
increment weight by 2-2a-3b. The second changes Q by 3a+6b+3 and
increment weight by -3a-6b. Nevertheless inverse branches overlap.
C=(0,1,(),(1,)), whose gap core is (3,3), takes the first branch to
C'=(1,1,(2,),(0,)). C=(1,0,(5,),()), whose core is (6), takes the second
branch to the same C'. Thus distinct residue inputs (1,1,1,3,3) and
(1,1,1,6), both weight nine, would produce the same gap partition (1,2,6).
The metered direct symbolic witness is discovery-third-one-obstruction.json;
no enumeration above 30 or final-map lookup was used.

Separately sending the a=0 cores elsewhere avoids this first witness but
not the overlap generally: at target C'=(2,1,(2,3),(0,)), the candidate
preimages C=(1,1,(5,),(1,)) and C=(2,0,(5,6),()) have pure-three gap cores
(3,3,9) and (6,9). Both acquire weight three and reach the same C'. The
obstruction is information loss between a new singleton and a new pair,
not a failure of weight or literal validity. This second statement is a
symbolic calculation, not an independently reviewed or swept computation.

The narrow next lemma must distinguish these two source branches without
an inverse transcript, while retaining the already assigned t=0,1,2
images or explicitly replacing the entire restricted assignment. Another
numerical pilot cannot repair the overlap. Workflow hypothesis,
**unvalidated**: compare reverse branch formulas before writing extension
code; exact cost identities alone conceal collisions. The full objective
and the frozen successful restricted map remain unchanged.
