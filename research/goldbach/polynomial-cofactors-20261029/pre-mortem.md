# Separate pre-mortem for polynomial cofactor states

29 October 2026. Independent Critic, supplemental preparatory dispatch for `GOLDBACH-COFACTORS-015`. I read the brief, survey and actual statement-stage packet as framing, and the accepted LABELS-005 revision and its limitations. This is not a main review or acceptance of an unseen cofactor construction. Only this file is owned. The pending TYPEI-013 main critic has priority when dispatched. Usage is unknown.

This preview deliberately does not repackage LABELS-005's displayed retuning failure or scalar-padding identity as a new result. It asks what a genuinely different h-retaining state rule must prove. Failure of an old available bound is not a lower bound on an actual norm and does not rule out a new arithmetic argument.

## 1. P1: fixed h does not bound the union of selected prime values

The local capacity bound Omega(q)<=3 restricts the factors of one q. It does not restrict how many different a can occur in different q=a*h with the same h. A transition definition is needed before any path-wide introduction bound can be inferred.

Here is a concrete witness in the raw cofactor-incidence graph of actual prime complements. Let N=30 and h=1. The four states

    (a,p)=(7,23),(11,19),(13,17),(17,13)

all have p+a=N, with p and q=a prime. Each q exceeds N^alpha for every alpha in [0.3,1/3), since 7 exceeds the cube root of 30. Each is squarefree with Omega(q)=nu(q)=1; every selected a is a unit modulo N. The raw fixed-h quadratic block connects all these states. Its closed path

    7 -> 11 -> 13 -> 17 -> 7

uses four distinct selected prime values while h is unchanged. Two vertices already refute the stronger assertion that fixed h forces one selected value. The four-vertex cycle refutes a path-wide capacity-three assertion on this exact graph.

This is not an asymptotic Vaughan Type-II counterexample: representing these prime p as mn uses m=1 and does not satisfy two long sifted factors. It refutes only an invariant claimed for this raw prime/cofactor incidence domain. A new rule restricted to genuine Type-II states might have a different invariant, but must prove that restriction and preserve the exact desired quadratic form and the h=1 boundary. A finite toy graph alone cannot decide its asymptotic arithmetic norm.

Decisive author check: specify state vertices, legal transitions and endpoint closure first. Either prove the global introduction bound from those transitions, or give the shortest admitted counterpath and explain the corrected candidate. Local factor capacity alone is not that proof.

## 2. P1: raw fixed-h rank one is not centered cancellation

For configurations i in one h block, the scalar square has form

    Q_h=|sum_i c_i*f_i|^2.

On a specified positive Hilbert measure it is the quadratic form of a rank-one positive Gram operator. Its nonzero eigenvalue is the actual squared norm of its representing vector, including every arithmetic and list weight. For two unit-weight configurations with c_i=1, its matrix is [[1,1],[1,1]], with norm two. Dividing by two gives a projection of norm one, not a small contraction. Rank one therefore does not by itself yield a logarithmic or polynomial cancellation gain.

Subtracting a comparison kernel requires a separate calculation. It need not preserve h, commute with this Gram operator, or be the orthogonal expectation relevant to the arithmetic population. Subtracting the whole raw rank-one block makes the centered operator zero but transfers all Q_h to the comparison term. At h=1 that comparison can contain precisely the unknown prime-complement count. No progress follows unless that major term is independently evaluated with its required nonzero center and error.

A further definition issue is positivity of the state measure. A Mobius sign mu(h) cannot be used as a Hilbert weight when it is negative; h=7 already gives a negative value. This cofactor occurs in the original finite rough domain at N=200,p=109,q=91=13*7: both factors exceed N^(1/3), so every stated alpha below 1/3 is allowed. Keep a positive measure and place any Mobius/parity sign in an explicit diagonal multiplier or kernel. Cauchy and positive trace powers then have their actual domains and cannot be inferred from an indefinite quadratic form.

Decisive author check: define the Hilbert space and measure, compute the raw and centered operators exactly, and state an independently sufficient estimate for the changed comparison. Do not infer a centered norm from the raw rank or a zero kernel obtained by subtraction.

## 3. P1: retain the prime atom, nonzero centers and squarefree semantics

The accepted LABELS-005 identities already give the exact three-cell reconstruction and its coefficient cost. A new cofactor mechanism must connect to those identities rather than alter them. On squarefree q=a*h, selecting each genuine prime once gives mu(q)=-mu(h), including h=1. That atom contributes -R to every Z_rho. A theorem only for long h, or a state projection deleting h=1, would omit the original unknown prime contribution.

The bound on Omega(q) and the count nu(q) are distinct definitions on repeated factors. Mobius kills nonsquarefree q in the signed reconstruction, whereas a bare distinct-label weight need not. The accepted O(N^(1-alpha)) exceptional count may be useful for a scalar sum, but it does not automatically bound the norm of every state restriction. Any quadratic or path use needs its own coefficient/measure estimate. A positive upper square obtained after discarding cofactor signs can also lose the exact center information; its role in recovering the signed prime margin must be explicit.

For proposed centers C_rho(N), the sufficient final inequality is quantitative. Their reconstructed prime main term must be positive, and the weighted error combination with coefficients -3,3,-1 must be smaller than that main term. The accepted l1 cost seven supplies a propagation bound; it is not a cancellation theorem. Simultaneous zero centers cannot simply be copied from the unrough subpolynomial argument. No new proof of these prior algebraic facts is claimed here.

Decisive author check: write the h=1 term in every state and comparison formula and show where its main contribution is estimated. Define the target centers before announcing contraction or a prime-margin result.

## 4. P1: cofactor integrality, positivity and support cannot be restored by assertion

The raw square first imposes both divisibilities and equality of integer cofactors. For coprime selected a,b this is equivalent to bmn-ars=N(b-a). For shared a,b the reverse implication fails: N=2,a=b=3,m=n=r=s=1 has determinant equality but quotient 1/3. Any new h state must encode the integer quotient, not just that determinant relation. Closed paths also contain diagonal/shared-label configurations, so their removal needs an actual bound rather than a universal distinct-prime declaration.

Positive q=N-p in the original target corresponds to positive h. Enlarging a nonnegative Cauchy square to signed h can be valid, as in PAIRING-011, but does not define mu at negative arguments or preserve an arbitrary signed operator norm under a joint positivity mask. If a modified transition rule is used to force a label budget, its identity with the original positive target or an explicitly sufficient upper/lower bound must be proved. The h=0 boundary must be excluded by its true support hypotheses.

The old small-band primitivity and coprimality arguments cannot be imported for polynomial a. The old sifted support excludes small labels from the long variables; a polynomial label can exceed that sift threshold. Likewise a shared auxiliary divisor need not avoid N without a genuine unit-support argument. The new proof must retain every gcd factor and determine whether its endpoint is primitive in the plane or only in a labelled lattice. Unit exceptions, support extension and normalizers must be counted at the final prime-margin scale.

Decisive author check: prove the arithmetic equivalence for each legal transition, with its exact sign, divisibilities and gcd conditions, then trace every enlargement back to the original target. Finite algebra witnesses should be labeled by the actual domain they satisfy.

## 5. P1: a new path rule needs a new total arithmetic error budget

Any claim that h retention makes polynomial labels cheap must expose the full root and path prescription. A single genuine label a>N^alpha already has log a>alpha*log N. Products of distinct labels introduced along a path can have still larger logarithm, even when each individual complement has three factors. A bounded number of factors in a local finite divisor expansion does not put those prescriptions into the old subpolynomial moment range.

The newer ROOTS-008 result does provide a coarse absolute formula for all squarefree prescribed S coprime to the determinant. This must not be confused with a useful relative asymptotic for every polynomial S: its prescribed main density is 1/product_{p|S}(p+1), while its absolute discrepancy and aspect restrictions remain. A proposed use needs to sum the actual coefficients times the counting error over all retained labels, line patterns and real regions. It cannot cite LABELS-005's old range failure as a universal impossibility, nor substitute polynomial S in a finite formula and silently obtain small relative error.

For the new h-based geometry, identify the ambient determinant and original-box dimensions, all sector multiplicities, endpoint frame/list norms, modulus products and root-region boundaries. Polynomial Y or auxiliary heights can change the aspect range and moment extraction loss. Those costs might be improved by a genuinely new coordinate or cancellation argument, but they need proof rather than a renamed old estimate. Any positive h=1 comparison center must remain after all such normalizations.

Decisive author check: give one complete inequality for the total arithmetic replacement error and the resulting centered moment or prime-margin estimate. If only an algebraic block decomposition or a counterexample to one invariant is established, label it exactly that. No actual norm no-go theorem follows merely from failure of an available upper bound.

These five tests leave room for a corrected cofactor construction while preserving the original objective. They do not accept the forthcoming author claim, establish a polynomial-label theorem, or supply a Goldbach lower bound or novelty result. The next main review must use the frozen actual statement and populated critic packet.
