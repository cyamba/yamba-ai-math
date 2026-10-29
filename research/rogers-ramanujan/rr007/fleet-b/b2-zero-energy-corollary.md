# B2 corollary: exact parsing of the entire zero-energy R2 sector

Recorded 24 October 2026 before its finite word-grammar check. This is a
derived endpoint of frozen B2, not a third construction variant and not a
change to its C assignment. **Proved, author-only.** The full positive-energy
R2/C interface remains missing.

Let R20 be the intrinsic R2 subfamily in which every secondary part has
raw size zero. The complete R2 predicate and literal weight are exactly
those in `author.md`; nonterminal00 is forbidden, and the last part is0_00.
Deleting ground letters from the secondary color word gives a word in1..4.

**Claim.** This word is weakly decreasing, and it uniquely determines the
entire R20 object. If its length is even, pair its letters consecutively.
If its length is odd, make the first secondary `(first_letter,0)` and pair
the remaining letters consecutively. Give every part raw size zero and
append0_00. Empty word gives only0_00.

**Proof of exact image.** Raw size zero forces e(i,j)=0, hence i>=j in
every nonterminal colorij. The upper color i is positive. For a next
nonterminal colorl0, the literal correction cases give Ereg(ij,l0)=2,
regardless of i,j. Such a part is consequently impossible except at the
very beginning. For a next colorlm with m>0, the same cases give
Ereg(ij,lm)=0 exactly when j>=l if j>0, or i>=l if j=0; otherwise it is2.
The nonground letters are therefore weakly decreasing. Conversely every
decreasing word grouped by the stated rule satisfies exactly these
inequalities, and its terminal comparison has Ereg(ij,00)=0. The single
possible ground letter is forced to be first-pair lower half; parity
determines its presence. This proves validity, full image and uniqueness.

Read the multiplicities of colors4,3,2,1 as m,n,t,s. The literal weight is
`8m+6n+3t+s`; this is exactly B0's literal weight. Deletion/counting and the
stated grouping are inverse finite algorithms, not a rank assignment.
Composition with frozen B2 is consequently a complete intrinsic C-cone
<-> R20 encoding, with exact image closure, weight and both inverses.
It needs no executable generic Omega2 algorithm.

This sector includes genuine splitting/fusion of A parts through C:
R20 color11 twice has weight4 and decodes to B=1^4, then C=(1,0,(3,),()),
whose A image is(4). R20 color21 decodes to B=(3,1), then C=(2,0,(0,0),()),
whose A image is(1,3). Thus raw literal forgetting is replaced by a real
parser on this full intrinsic sector. The two A endpoint examples follow
directly from the single/pair extraction formulas; full A endpoint
assurance retains its separate-review obligation.

For U supported on{1,3,6,8}, the F2 lift has the same decreasing nonground
word and all raw sizes zero. The R20 rule moves the parity ground pad
to the first pair when necessary. Thus the zero-energy degree-two
flat/regular endpoint is explicit and unique by the source's preserved
word/size invariant, independently of its uninspected generic algorithm.

The first positive-energy examples 1_01 and1_02 have weights10 and12 and
lie outside this sector. An extension must decode arbitrary such energy
and context, allowing b>=2 and higher a. Assigning these two examples
alone would not supply that extension.

Frozen verification: `.runs/rr007/b2-zero-energy.py 12` independently
generates every literal R20 sequence and every B0 input through12,
checks both identities, exact image, literal weights, empty/padding and
repetition cases. All actual inputs/outputs are <=12. No larger run is
requested or authorized for this corollary.
