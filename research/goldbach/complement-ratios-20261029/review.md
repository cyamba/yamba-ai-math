# Independent review of moving complement-ratio averaging

29 October 2026. Registry role: Independent Critic, `GOLDBACH-RATIOS-007`. This is a separate host-agent mathematical audit. It is not formal verification, external peer review, or numerical certification of the asymptotic estimates. No usage measurements are available.

## Verdict and frozen inputs

**Supported:** the self-contained complete Kloosterman bound with its displayed divisor factor; the interval completion including large H divisors; the Ramanujan main term and frequency-divisor costs; the improved primitive both-unit mass estimate; the stated polynomial-frequency cancellation range; the Fejer discrepancy inequality; and the normalized bounded-variation consequence. The balanced saving H^(-1/8+o(1)) follows in the declared asymptotic regime.

One normalization clarification is recommended when passing to an **unnormalized** leading-mass formula: its mass-error term must also be multiplied by the absolute mean of the test function. The normalized statement (11) itself is correct.

**Incomplete:** any prime-weighted, prescribed-list or path-moment extension, and any Goldbach lower bound or demonstrated breakthrough. This is a classical-method specialization for unweighted primitive positions. Novelty is unverified.

| Frozen input | SHA256 |
| --- | --- |
| `statement.md` | `dbd7f89da164cf2dba56a9b6ef877d083e936d3caee912e70390218e0a6a6699` |
| `closest-work.md` | `95e4c94980157c3faf2530aab65d30d91a1b06c03f19b8f3857e6d862a130f71` |
| `survey.md` | `56933082bc0c3a30d16e3df466b1591fdd2557987f070bbecd1833ad73079bf6` |

The populated counterexample packet supplied the completed statement-stage response. I changed none of these inputs.

## Source and priority checks

I inspected the [Lue-Wang-Wu appendix estimate (A.2)](https://arxiv.org/html/2610.20242v1) and independently checked the finite argument reconstructed here. The proof below does not require acceptance of that manuscript's full theorem or root-averaging result.

I also inspected the introduction and equation (1.4) of [Blomer-Risager-Shparlinski, arXiv:2411.17823v3](https://arxiv.org/html/2411.17823v3). It explicitly records the stronger classical square-root Weil bound with gcd and divisor factors and studies inverse-distribution problems. No filtered moving-H consequence of its theorems is imported here. This supports the closest-work document's priority boundary: the present method is established methodology, not a claimed new general inverse-distribution theorem.

## Complete-sum proof

Fourth-moment additive orthogonality gives m^2 times the specified unit-quadruple count. Eliminating y2 and clearing the invertible denominators gives divisibility by m of

    (x1+x2)*(y1-x1)*(y1-x2).

The three-factor linear map has kernel (t,-t,t) with 2t=0 modulo m. Its fibers therefore have at most two points, including when m is even. Enlarge from the permitted unit tuples to all residue triples satisfying that product divisibility. For every such triple, prime-by-prime allocation of the prime-power factors of m gives d1*d2*d3=m with each di dividing its respective entry. For each allocation the number of residue triples is m^2. There are tau3(m) allocations, so the union bound and the factor-two fiber bound prove (2).

Unit scaling leaves the sum unchanged as claimed. Its stabilizer imposes both h(s-1)=0 and a(s-1)=0 modulo m, equivalently s=1 modulo m/g with g=gcd(h,a,m). Reduction of units to a divisor modulus is surjective, so the orbit has phi(m/g) elements. Its contribution to the fourth moment yields the displayed bound. The inequality

    1/phi(m/g) <= g/phi(m)

follows from the Euler products for phi. This gives exactly C(m)*m^(3/4)*g^(1/4), not a bound requiring unit frequencies or odd moduli. Zero-frequency cases, including g=m, are allowed. Elementary divisor estimates make C(m) subpower with a constant depending on the chosen exponent.

## Completion, endpoints and large divisors

For each admitted u, both H and every d dividing rad(H) are units modulo u. The inverse coefficient -k*H*d^(-1) therefore has gcd with u equal to gcd(k,u). Its Ramanujan sum equals c_u(k), since multiplying the frequency by a unit or by -1 preserves that sum. This is the precise reason the moving multiplier does not add a new gcd cost.

Finite Fourier completion over an integer interval is valid at every length. Its zero mode is the integer cardinality times c_u(k)/u, and its nonzero modes are the stated complete sums times geometric sums. The latter have normalized l1 norm O(log(2u)), even over many periods, because a complete period cancels at every nonzero mode. The gcd in their complete-sum bound is at most gcd(k,u), as used.

Replacing interval cardinality by V/d costs O(|c_u(k)|/u)=O(1). This uniformly handles d>V, including empty intervals for d>2V. No H divisor is omitted. Summing all squarefree H-divisor contributions produces phi(H)/H in the main term and tau_H=2^omega(H) in the error. Formula (3) follows with an absolute implied constant.

The Ramanujan main term is essential. For example, H=2, u=3 and k=3 give identically unit phase on the admitted v and an interval sum of order V. An error depending only on u cannot absorb it as V grows. The statement retains this main term instead of incorrectly assuming a nonzero reduced frequency.

## Summing the modulus and tracking frequencies

The bound gcd(k,u)^(1/4)<=sum_{d|k,d|u}d^(1/4) is valid for nonzero k. For d<=16U the number of multiples in [U,16U] is at most 31U/d. This gives the exact sigma_(-3/4)(|k|) cost in (5). The C(u) and logarithmic factors can be bounded uniformly over that interval by their U versions, with the claimed eta-dependent constant.

Expanding the Ramanujan sum gives its absolute main-term cost O(tau(|k|)). For each divisor of k, the resulting harmonic sum is on a fixed-ratio interval; when its lower endpoint is below one its upper endpoint is at most 16. Thus this cost has an absolute constant and does not assume k coprime to u.

The frequency bound is correctly restricted to 1<=|k|<=H^A for each fixed A. In that range, divisor factors are uniformly H^o(1), with constants depending on the requested slack and fixed A. No uniform statement over all integer frequencies can hold: taking k to be a multiple of all the admitted first coordinates makes every phase equal to one. Such enormous frequencies are not covered by the stated polynomial range. The zero frequency is likewise explicitly excluded.

## Primitive both-unit mass without a squared H-divisor loss

For fixed u coprime to H, inclusion-exclusion over rad(uH) gives the count of v with the stated density and error O(tau_H*tau(u)). Summing tau(u) over [U,16U] costs O(Ulog(2U)).

For the main sum, expand phi(u)/u exactly. Its divisor d is automatically coprime to H, and counting the remaining multiples coprime to H gives the displayed main term plus O(tau_H) before the 1/d weight. The error sum is O(tau_H log(2U)); extending the reciprocal-square main series costs O(1), already absorbed. The product of its Euler factors and two phi(H)/H factors is exactly kappa_b(H).

Multiplying by V*phi(H)/H, rather than multiplying two independent inclusion-exclusion error bounds, gives the claimed O(tau_H*(U+V)*log(2U)) mass error. No tau_H^2 term is needed. This is uniform in H,U,V within the stated domains.

## Asymptotic exponent and discrepancy

For U comparable to H^a and V comparable to H^b, the mass error is o(UV*kappa_b(H)) for any fixed a,b>0. The count is therefore positive eventually. After division by that mass, the Ramanujan cost is H^(-a+o(1)); the completed-sum error is H^(3a/4-b+o(1)), where the freely chosen eta is absorbed in any requested fixed exponent slack. This proves gamma=min(a,b-3a/4)>0 under b>3a/4, uniformly in the stated polynomial frequency range. With a=b=1/2 the exponent is 1/8. The H^o(1) notation and its parameter-dependent constants are accurately specified and do not give a numerical threshold.

The Fejer argument also checks out. Its normalized tail outside delta is O(1/(J*delta)). At delta=J^(-1/2), an interval enlarged by delta has a convolution at least one minus that tail at every original interval point. Dividing by this quantity gives a genuine pointwise trigonometric majorant for sufficiently large J; bounded small J are handled by the trivial discrepancy bound. Its constant coefficient differs from the interval length by O(J^(-1/2)), and its nonzero coefficients are O(1/|k|). A complementary-interval majorant gives the minorant. Averaging the finite polynomials proves (9), with the half-open convention handled consistently.

Taking J comparable to H^(2gamma), for example rounded down for large H, fits the polynomial frequency range with a fixed sufficiently large A. The harmonic factor is H^o(1), proving (10). It is permissible to choose that A once for this step; no enormous-frequency uniformity is used.

The normalized bounded-variation result (11) follows by integrating interval discrepancies against the signed derivative measure of a right-continuous periodic BV function. The complex-valued case is controlled by the total variation of that measure. Its constants do not depend on the particular function except through its variation. Constants in the function cancel in this normalized formulation.

## One normalization clarification for the revision

If the final synthesis presents an unnormalized leading-mass formula, let M=15UV*kappa_b(H) and let E_mass denote the error bound in (7). Combining the accepted statements gives

    |sum_P g(x_P) - M*integral(g)|
      <= O(N0*Var(g)*D + E_mass*|integral(g)|).

Both costs must be retained for H-dependent functions. Bounded variation alone does not bound their mean: g_H(t)=H^100 has variation zero, but replacing N0 by M in its unnormalized sum still incurs H^100*(N0-M). This is not a counterexample to normalized (11), which is exact for constants. It is a clarification of the following paragraph's proposed recombination with (7).

## Findings and remaining scope

1. **P3, unnormalized test-function costs.** Add the displayed mean-times-mass-error term when using the leading mass instead of the actual normalization N0. Continue to multiply the discrepancy by Var(g) for H-dependent functions. The constant-function example above shows why those are separate costs.
2. **P1, missing arithmetic extension.** The proved averaging is over unweighted primitive both-unit positions. No bound for prime weights, prescribed list lines, selected endpoint coefficients or high moments follows without explicit joint estimates and their modulus/variation/frequency costs. In particular, the changed denominator-H major-arc estimate from the earlier sector construction remains open.
3. **P3, quantifiers and priority.** Preserve nonzero polynomially bounded frequencies, fixed box exponents, the condition b>3a/4, and unspecified asymptotic constants. The stronger classical Weil input and extensive inverse-distribution prior work preclude treating this as a new general theorem or a demonstrated Goldbach breakthrough without further evidence. The full LWW theorem remains unverified here.

No correction is required to equations (1)-(11) as normalized and quantified. The proof supplies a genuine limited cancellation estimate, with the elementary finite input independently reconstructed. It does not supply the missing Goldbach prime-correlation lower bound.
