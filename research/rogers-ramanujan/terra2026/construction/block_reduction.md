# Variable-length height-block reduction for U–C

Status: **proved elementary representation; global correspondence open**. Written author argument only, not separately reviewed. Novelty NOT VERIFIED. This does not use the refuted finite apex table and does not solve KR1. It gives recoverable, unbounded target coordinates and a concrete transfer-system obligation.

Let F(5k+r)=9k+(0,1,3,6,8)[r] for 0≤r<5. A U object is a descending list of F(h) for positive heights h such that consecutive distinct heights, and the smallest height down to zero, have difference at most 4. Multiplicity of a height is unrestricted. For a nonempty object let L=ceil(max(h)/5), and make L blocks of five nonnegative integers

    M_k=(m_{5k+1},m_{5k+2},m_{5k+3},m_{5k+4},m_{5k+5}),  0≤k<L,

where m_h is the multiplicity of height h. Every block is nonzero. Its mask is the set of positions r with m_{5k+r}>0. Let p(M) and s(M) be the number of initial and final zero entries respectively. Then the exact admissibility rule is

    p(M_0)≤3;  s(M_k)+p(M_{k+1})≤3 for 0≤k<L-1.

There is no restriction on s(M_{L-1}), because zeros beyond the last positive height are outside the object. The two displayed conditions also exclude every internal run of four zeros: such a run in a non-final five-block necessarily touches an end, and is caught by the initial or adjacent-block condition. A run in the final block before its last positive entry can only be a four-zero prefix, likewise excluded.

**Proof and inverse.** A valid U cannot have a missing interval of four heights below its maximum, including 1,...,4. This yields the two inequalities, as every missing interval of four either lies within one five-block or crosses one block boundary; a five-block with four internal zeros has its sole positive at an endpoint, and the relevant prefix or suffix inequality excludes it unless the zeros trail the final positive. Conversely, every such run is excluded by those inequalities, so the positive heights have successive gaps ≤4 and start ≤4. From blocks reconstruct U by taking m_{5k+r} copies of F(5k+r) and sorting decreasing; reverse by counting decoded heights. Both directions clearly terminate and are inverse. Weight is exactly

    wt(M)=Σ_{k,r} m_{5k+r} (9k+w_r),  w=(1,3,6,8,9).

F is strictly increasing, so no ambiguity occurs. The block count L and all multiplicities are recovered, and L is unbounded. This is categorically different from assigning every apex to one of finitely many column values.

## Transfer model

Let a nonempty mask S⊆{1,...,5} have p(S),s(S) as above. Define

    V_k(S;q)= ∏_{r∈S} q^(9k+w_r)/(1-q^(9k+w_r)).

The exact formal series of U is

    1 + Σ_{L≥1} Σ_{S_0,...,S_{L-1} nonempty}
        1[p(S_0)≤3] ∏_{k=0}^{L-2} 1[s(S_k)+p(S_{k+1})≤3]
        ∏_{k=0}^{L-1} V_k(S_k;q).

The coefficient of each q^N is well-defined: all selected heights cost at least one and a block at index k costs at least 9k+1. Note that selecting final mask {1} is legitimate because zeros after the maximum do not matter, while choosing {1} at a non-final block is impossible under the boundary rule.

On C, put x_i=μ_{a-i+1}−μ_{a-i} (μ_0=0), 1≤i≤a, and y_j=ν_{b-j+1}−ν_{b-j} (ν_0=0), 1≤j≤b. Then the fully recoverable source coordinates are (a,b,x_1,...,x_a,y_1,...,y_b) with all coordinates nonnegative, and

    wt(C)=a²+3ab+3b² + Σ_{i=1}^a i x_i + 3Σ_{j=1}^b j y_j.

The inverse is μ_t=Σ_{i=a-t+1}^a x_i, ν_t=Σ_{j=b-t+1}^b y_j. Thus an all-charge bridge is exactly a weight-preserving reversible transducer from these charge-and-increment coordinates to admissible sequences of positive-multiplicity masks satisfying the two boundary rules. It must process unbounded a,b and block length, produce the five multiplicities of each block, and recover all source coordinates. Required proofs remain: (1) every input produces a finite admissible sequence, (2) weight equality, (3) an explicit inverse returns nonnegative coordinates, (4) both compositions are identities on all inputs, and (5) every admissible sequence is reached. The transfer series identity alone cannot provide this transducer or certify an algorithm.

## Failed simplifications and exact scope

1. **Independent blocks fail:** masks {1} in block 0 and {5} in block 1 are separately nonempty with positive multiplicity but violate s+p=4+4>3. They encode heights 1 and 10, which have forbidden gap 9. This refutes any independent-block product that omits boundary state; it does not refute context-sensitive blocks.
2. **Forbidding singleton {1} globally fails:** the valid U with one height 1 has final block (1,0,0,0,0). Trailing zeros are outside the object. An automaton must distinguish terminal truncation from an actual internal gap.
3. **Strict coordinate-root correspondence with adding column 1 fails already at weight 1:** the empty cluster has a=0 and the one-single base cluster (a,b,μ,ν)=(1,0,(0),()) is x_1=0. If each x_1=0 base/root were required to map to a U without height 1 and if the empty maps to empty, the weight-1 root would need a weight-1 U without height 1, but F(1)=1 and F(h)≥3 for h≥2. This only refutes that strict rooted coding convention; a charge-changing boundary rule may still use insertion of a height-1 column.

The next concrete constructive question is whether there is an invertible carry/insertion rule on this *actual* boundary-state language, with charge changes permitted, that realizes the C increment weights. An independently computed finite series comparison is a useful falsifier for proposed refinements, never a proof of coverage.

## Bounded implementation checks

`python3 research/rogers-ramanujan/terra2026/construction/check_blocks.py` checks that a separate four-state zero-run dynamic program agrees with `kr1.cluster_counts` for coefficients through weight 60, and tests block encode/decode for 1,393 weighted-partition objects through weight 30, including both terminal and invalid-boundary examples. This supports the transcription only; it is not a proof of the U–C transducer or an all-weight coefficient identity. The script uses the repository's existing `kr1` primitives and does not use enumeration to define any proposed bridge.
