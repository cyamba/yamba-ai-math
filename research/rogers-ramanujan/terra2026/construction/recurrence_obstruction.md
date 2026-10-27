# Color and layer obstructions to a cut-insertion recurrence

Status: **proved elementary obstructions and node symmetry**, author argument, independent review pending. Novelty NOT VERIFIED. This does not give the requested object-level recurrence and does not establish a KR1 bijection.

Consider the proposed recurrence

    C_n = A_{n+1} + q^(3n+3) C_{n+1}
          + q^(6n+6) C_{n+1} + q^(6n+8) A_{n+2}.

The algebraic recurrence and A-family admissibility are external hypotheses here, not proved by this note. From the given node weights,

    C_n:       α_i(j)=3n+4+3i+9j,  β_i(j)=6n+5−3i+9j,
    A_{n+1}:   α_i(j)=3n+2+3i+9j,  β_i(j)=6n+7−3i+9j,
    A_{n+2}:   α_i(j)=3n+5+3i+9j,  β_i(j)=6n+13−3i+9j.

The cuts contribute 9 times their indices. These calculations apply even if the construction moves existing cuts or particle indices arbitrarily, provided it retains each particle's color and number and leaves common-tail context unchanged. The number of particles of colors α and β is denoted a,b.

## Residue obstruction for preserving the color word

Every α in A_{n+1} weighs 1 more than the corresponding C_n α modulo 3; every β weighs 1 less. Thus the first branch can preserve weight only if a−b≡0 mod 3. For A_{n+2}, the node-color differences are likewise +1 and −1 modulo 3, but the branch shift 6n+8 contributes 2; this branch requires a−b≡1 mod 3. Both C_{n+1} branches have shifts divisible by 3 and impose no such residue obstruction.

For every n≥1, take all n cuts at zero and a single α at index 0 in layer 0. This is an actual C survivor: its flattened word has no β→α descent, all its indices and gap coordinates are zero, and there are no markers. Its weight is 3n+4. It cannot go to the unshifted A_{n+1} branch while preserving the particle's color, by the residue test. Nor can either shifted C_{n+1} branch contain it while preserving the one particle: the smallest C_{n+1} particle has weight 3n+7, and the smaller branch shift adds 3n+3. The fourth branch's shift 6n+8 itself already exceeds 3n+4. Therefore no four-branch recipe that retains the color word and common context can be total, even if it is allowed to modify cut and particle indices. This is not a no-go theorem for changing colors, splitting/merging particles, or changing context.

## Exact weight duality and its obstruction

For all n≥1, i=0,...,n, and j≥0, direct substitution gives

    C_n α_i(j) = A_{n+1} β_(n+1−i)(j),
    C_n β_i(j) = A_{n+1} α_(n+1−i)(j).

Thus flipping colors and reversing the layer index carries every node weight to exactly the same weight, but uses A layers 1,...,n+1 and leaves layer 0 empty. The one-α example indeed has a weight-matching A object obtained by placing a β at index 0 in the terminal layer; whether it obeys any additional A-side survivor/exclusion rule must be checked separately.

The layer reversal cannot in general be implemented by merely inserting one cut while retaining the old cut values and all particle indices. Take n=2, cuts (0,0), and one α in terminal layer i=2 at j=1. This is a valid C cut state and has weight 25; Here m=floor(2/3)=0, so the source is a survivor. Its layer-reversed image would require a β at j=1 in A_3 layer 1. Among three cuts formed by inserting one nonnegative value into (0,0), the second cut is still 0, so layer 1 only admits indices ≤0. Hence the target is invalid. This refutes exactly this fixed layer-reversal and unchanged-cut recipe; allowing a broader rearrangement remains open.

As a limited constructive check, if every source cut and particle index is zero, insert an additional zero cut, reverse layers via i↦n+1−i and swap colors. This gives a direct weight-preserving bijection onto the similarly zero-index target states with A layer 0 empty; its inverse deletes that empty layer, reverses and swaps back. The statement is about the underlying colored cut states, pending any extra A exclusions. The corresponding general recurrence still needs an explicit branch selector, all-source coverage, and inverse on the actual A and C survivor classes.

## Reverse-complement words and strictness drift

A stronger candidate takes the source cut word w of length N, reverses it, swaps α and β, and places a new cut first: w'=| + reverse(swap(w)). This reverses particle layers i↦n+1−i and therefore preserves intrinsic particle weights exactly. A β→α strict descent ending at source position t (2≤t≤N) becomes a β→α descent ending at target position N−t+3. Its source minimum-index contribution is 9(N−t+1), and its target contribution is 9(t−1). Therefore

    minimum_weight(w')−minimum_weight(w)
       = 9 Σ_{source descents at t} (2t−N−2).

All cut and particle gap coordinates are nonnegative; restrictions such as survivor conditions can only further raise minimum weight. Consequently, a positive value of this difference blocks any weight-preserving unshifted map for that fixed target word, regardless of how its gaps are chosen.

For the smallest concrete example take n=1 and w=|βα. Its minimal indices are (0,0,1), and the two source particle intrinsic weights are 8 and 10, for total 27. The target word is |βα|. Its particle intrinsic weights are 10 and 8, while the mandatory β→α step increases both the α and final cut index by one, so its minimum weight is 36. Thus the reverse-complement word alone cannot map this source into the unshifted A_2 branch. Since n=1 has no C marker, the source is a survivor. The calculation is independent of A-side additional exclusions; it is a lower bound even before imposing them.

This failure does not rule out a transformation changing the word, intrinsic colors, using a different branch, or borrowing weight through other context. A general solution would need an invertible transport of the major–comajor drift together with the n-dependent survivor and A-side exclusion conditions.
