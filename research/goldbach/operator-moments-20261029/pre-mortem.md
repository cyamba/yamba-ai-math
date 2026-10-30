# Separate pre-mortem: small-rank collision phases

29 October 2026. Registry role: Independent Critic. This is the supplemental two-unit preparatory source audit for `GOLDBACH-MOMENTS-010`, before reviewing any author statement or populated main critic packet. Ownership is this file only. It neither executes the main critic stage nor accepts the full H2' chain, the claimed LWW theorem, its reflected transfer or a Goldbach conclusion. No usage measurements are available.

I inspected the primary [Lue-Wang-Wu v1, Sections 4.4-4.5, especially (4.61)-(4.62)](https://arxiv.org/html/2610.20242v1#S4.SS5), including the finite measures, tuple operations, Schur estimates, birth-index definition and local phase insertion. The following argument is an independent finite symmetry and norm calculation. It does not validate earlier arithmetic edge estimates merely because the source states them.

## Narrow verdict

**Supported:** ordered birth phases can be collected and symmetrized without changing the collision-conditioned matrix element; tuple-length and fresh-versus-recall activity flags are preserved; bounded phase multipliers preserve the absolute Schur majorants; and a rank-r collection modifies at most 2r of the E factors.

**Conditional:** these facts imply the displayed small-rank moment estimate if the unmodified E operators satisfy the claimed small signed norm, their indicated absolute Schur bounds hold at the actual weights, and the preceding finite history expansion has been proved. This pre-mortem does not establish those other load-bearing inputs. I found no counterexample to the targeted phase/symmetrization step under these exact conditions.

## Exact finite setting needed for the symmetry

For one prime group, the active-list measure is a product of nu(p). Memory coordinates are pairs (p,line), with symmetric functions and product measure lambda^k/k!, where lambda(p,line)=nu(p). Repeated coordinates are permitted and are distinguished when choosing a subset to remove or a coordinate to recall. A newly appended ordered prime tuple of length l carries product nu(p_a)/l!. The memory cap is by total coordinate count. These factorials and repetitions must be retained; replacing ordered tuples by sets would change the calculation.

Write B for the finite universe of potential birth indices. Initial list slots are always active. An E birth index is active only on its fresh-selection branch, not when filling the slot from existing memory. The hth potential birth slot of a G tuple is active exactly when its actual length l reaches h. A collision block C requires all its indices active and the corresponding birth prime values equal. Recalls are not new births.

For each collision block, torus orthogonality expresses equality by a product of phases, one attached to each involved birth index. This is a finite exact identity. All factors attached to the same G birth tuple must be collected into a single multiplier Phi_l before any averaging. Set that multiplier to zero when a required index exceeds l. Its modulus is at most one.

## Why the remaining history is symmetric

Fix the existing memory, active lists and position at a G operation, its removal subset and appended length l. Temporarily remove the phases assigned to this appended tuple, keeping every other collision phase and active-index restriction. Sum the complete continuation over all subsequent histories, including its final vector. Call the resulting function F(p_1,...,p_l).

For every permutation of these l newly appended coordinates, there is a weight-preserving bijection of future histories. Relabel the corresponding existing memory-coordinate indices in every later subset removal and recall choice. If repeated pairs occur, relabel their indices too; the multiplicity of choices is unchanged. A later append is at the end of its own tuple and keeps its own birth indices. Active-list values after a recall are unchanged under this history relabeling. Complete-list restrictions, line tests and position restrictions depend on those values, not on an ancestry label attached to an existing memory coordinate. Caps depend on lengths.

The remaining collision data are also unchanged. A later E slot is either fresh or a recall before and after the bijection. A later G slot is active according to its own tuple length. None of those flags identifies which coordinate of an earlier G tuple is being recalled. All phases belonging to this earlier tuple were already collected into Phi_l. Thus the continuation F is symmetric in its l arguments.

This is the precise history statement needed in place of treating permutations across changing memory lengths as an unexplained fixed-coordinate commutation identity. It follows directly from the stated subset/recall rules and symmetric terminal vector; it would need rechecking if later constraints retained individual birth ancestry as part of the state.

The product tuple measure is permutation invariant. A change of variables therefore gives

    (1/l!) sum_p Phi_l(p) F(p) product_a nu(p_a)
      = (1/l!) sum_p Phi_l^sym(p) F(p) product_a nu(p_a).

The equality remains exact when primes repeat. It is a finite group average, not an assertion that each individual history is unchanged. Its zero value for a missing required slot is independent of the permutation because l is fixed. Applying this argument successively to the relevant birth tuples justifies the source's replacement.

The symmetry condition is essential. On the two ordered tuples (3,5) and (5,3), give each weight nu(3)nu(5)/2. Put Phi(p)=e(p_1/4) and F(p)=1_{p_1=3}. The unsymmetrized sum is -i*nu(3)nu(5)/2, whereas the symmetrized phase vanishes on both tuples. This is a counterexample to an unrestricted phase-symmetrization rule, not to the source step: its continuation must be the symmetric F proved above. One must also average the whole tuple multiplier, rather than multiplying separately averaged phases.

## Norms and the number of affected edges

A bounded multiplier need not preserve the small norm of an arbitrary signed kernel. The valid argument uses elementary absolute majorants for the modified factors. The G proof has just such a majorant: its removal/retention binomial and append exponential are summed in absolute value in both Schur directions. For one group the row and column majorants are respectively

    exp(v0*eta*V*s/theta)
      * (q/theta^2 + eta/(theta*v0))^h,
    exp(v0*eta*s/theta)
      * (q/theta^2 + eta*V/(theta*v0))^h.

Here h counts the matching existing memory coordinates, s=sum_p nu(p), eta=1-q, q<=sqrt(rho), theta^2>sqrt(rho), V<1 and v0 is a sufficiently large fixed Schur weight. Both parentheses are at most one and s is bounded. Thus these absolute bounds are uniform in memory length and remain bounded after multiplying each elementary append choice by Phi_l^sym, whose modulus is at most one. The factorial state measure supplies the reverse-direction subset multiplicities. This reasoning uses an elementary absolute majorant, not the possibly smaller modulus of an already aggregated signed kernel. The memory-cap compression can only decrease its positive row and column sums.

A marked E factor may require a fresh branch and carry a birth phase. Its small signed estimate is not asserted to survive this modification. Instead use the proved polynomial absolute Schur majorant, provided it is valid on the actual symmetric memory space and uniformly in these bounded choice multipliers. Restricting the fresh branch and multiplying its newly selected prime by a phase preserve existing-memory symmetry. Initial birth phases are bounded diagonal multipliers on the initial vector and cannot increase its norm.

The union of collision blocks of rank r contains at most 2r birth indices: each block of size t>=2 has t<=2(t-1). Only factors at those birth indices are modified. An unmarked E factor is the original operator, even if its input vector contains memories carrying earlier phases. An operator-norm estimate applies to every such input vector; no additional conditioning is imposed on that factor. Hence at least 2R-2r of the E factors retain their original L^(-G) bound. All G factors retain a fixed absolute bound, and the at most 2r marked E factors use L^(C_*).

This gives the conditional product estimate

    |I(C_0)| <= C^(2R+1) ||b||^2
                 * L^(-G*(2R-2r)+2*C_*r).

If the weighted count of rank-r collections is at most |B|^(2r), with |B| polynomial in L, and r_0/R=O(log L/L^0.1), then the sum for r<r_0 is L^(-2RG+o(R)), provided ||b||^2 is bounded and all constants were fixed before the limit. The factors C^(2R+1), the number of ranks and |B|^(2r) contribute only o(R) to the exponent in base L. This verifies the algebra of the small-rank conclusion from its stated inputs.

## Prioritized findings and next check

1. **P1, the base signed edge input remains separate.** This audit supports the conditioning mechanism conditional on a genuine uniform unmodified E norm and the stated absolute majorants. It does not establish the clean Fourier estimate, dirty edge estimates, adjoint normalization or memory-history identity. The main author stage must prove those inputs at their actual measures before concluding the moment theorem.
2. **P2, preserve joint tuple phases and history symmetry.** Collect every phase attached to one birth tuple before symmetrizing, retain length-based activity flags and relabel repeated memory indices in the continuation bijection. The explicit nonsymmetric-F example above is a decisive test for any broader use. A future ancestry-sensitive constraint would require a new proof.
3. **P2, preserve the operator-level locality of conditioning.** Only factors with marked birth indices may lose their signed savings. Modified E factors need the absolute polynomial bound; unmodified ones retain the original signed bound on arbitrary input vectors. Entrywise restriction alone is not a general reason that a small signed norm survives.

This preparatory check finds a valid narrow source argument. It supplies no acceptance of the forthcoming author statement, the other moment inputs, the reflected arithmetic replacement or the Goldbach bridge. The next review must use the frozen actual statement and populated critic packet.
