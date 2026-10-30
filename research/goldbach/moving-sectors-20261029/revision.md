# Moving-target sectors: accepted scope and revised exact-edge bound

29 October 2026. Registry role: Mathematician, `GOLDBACH-SECTORS-006`, revision stage. This record accepts the separate critic and finite-check branches in the populated revise packet. The frozen statement and survey are unchanged. The statement SHA256 is `622e03bca08c00023894cfb98c892c7831a8aef6980cf00775aa6d7aa78291f9`; the survey SHA256 is `a414c745de82d8ddc3b0d4cfc06791b16d77d9ff53251f2c3ba245b30192b21e`.

**Proved, with separate agent review:** the defined whole-centered-operator conjugacy, its coprimality and original small-label primitivity conditions, the elementary point counts and their stated errors. The exact-domain partner bound below sharpens the frozen conservative bound. Assurance is an explicit elementary argument plus separate mathematical review, supported by bounded exact checks. It is not formal verification or external peer review. Inference usage and monetary cost are unknown.

**Unverified:** the required actual-prime cancellation, a moving-target extension of the source's analytic theorem, novelty, and any Goldbach lower bound or demonstrated breakthrough.

## Accepted conjugacy and its required hypotheses

For primitive positions in `[U,16U] times [V,2V]` with first coordinate coprime to H, retain the sector `c=v/u mod H` and use

\[
 T_c(u,v)=(u,(v-cu)/H),\qquad
 \Omega'_c=\{(u,w):U\le u\le16U,\ V\le cu+Hw\le2V\}.
\]

The map preserves primitivity because `gcd(u,cu+Hw)=gcd(u,w)` when u is a unit modulo H. Its inverse is integral on the exact sector. Sector copies must remain distinguished, and the parallelogram must retain its possibly negative second coordinates.

For a common first-coordinate divisor D, `gcd(D,H)=1`. With `t=det(P,Q)/D` and sector residues c,c', the identity

\[
 t=H\det(P',Q')/D+(c'-c)uu'/D
\]

has `uu'/D` a unit modulo H. Thus H divides t exactly for equal sectors. More importantly, defining the **complete** arc pullback `M_H={theta:H theta in M_1}` gives, for every integer k,

\[
 \int_{M_H}e(k\theta)\,d\theta
 =\mathbf1_{H\mid k}\int_{M_1}e((k/H)\phi)\,d\phi.
\]

The H inverse branches cancel the factor 1/H in the nonzero case. Hence both the exact-edge term and the comparison integral vanish across unequal sectors. Within a sector the centered bracket is exactly the coefficient-one bracket with frequency `det(P',Q')/D-(b-a)`. The explicitly defined cutoff `psi_1(t/(HY))` becomes `psi_1(t'/Y)`.

First coordinates, prime lists, the factors involving D,a,b, damping, and the original discrete state weights are unchanged. The pullback is a counting-space isometry without an area factor. A determinant-one complement `(r,s)` becomes `(Hr,s-cr)`, so `r_{P'}=H r_P mod 1`. Good-state conditions must therefore use `H r_P`. List permutations, these projections, adjoints and finite moments respect the direct sum. The norm of the defined operator is the maximum block norm. This is an identity and supplies no bound for that maximum.

Removing actual prime inputs dividing H costs at most `omega(H)` counts, or `omega(H) log H` with the stated logarithmic weights. The analogous von Mangoldt prime-power cost has the same bound. Multiplying an exact multiplicative decomposition by the unit indicator carries it into every factor. In that deliberately restricted decomposition, labels dividing `H-mn` are also units, and positions `(Dbm,s)` and `(Dar,n)` have both coordinates units. This justifies using only unit sectors for that construction. It does not justify discarding arbitrary nonunit endpoint mass from an abstract operator.

Primitivity for nonzero centered terms remains conditional on the original small-label/sift separation: list primes below Z, coefficient factors Z-rough and units modulo H, `b>1`, `gcd(a,b)=1`, and `|t/H|<Z`. A common endpoint prime divisor then exceeds Z, is coprime to H and D, and divides `t/H`. It forces t=0, which `gcd(b,ars)=1` excludes. This argument applies before assuming endpoint primitivity and uses the full-pullback support. Polynomial labels do not meet this separation automatically.

## Accepted quantitative counts and the sharper partner estimate

For `U,V>=2`, `B=min(16U,2V)` and `tau_H=2^{omega(H)}`, the reviewed elementary counts are

\[
 N_c=\frac{15UV}{H}\kappa_u(H)
 +O\!\left((U+\tau_H V/H)\log(2B)+B+UV/(HB)\right),
\]

\[
 N_{\rm both}=15UV\kappa_b(H)
 +O\!\left(\tau_H(U+V)\log(2B)+\tau_H^2 B+UV/B\right),
\]

where

\[
 \kappa_u(H)=\zeta(2)^{-1}\prod_{\ell\mid H}\frac\ell{\ell+1},\qquad
 \kappa_b(H)=\zeta(2)^{-1}\prod_{\ell\mid H}\frac{\ell-1}{\ell+1}.
\]

These follow from exact gcd Mobius inversion and interval inclusion-exclusion. The density relation `(phi(H)/H) kappa_u(H)=kappa_b(H)` matches the unit sectors and their areas. The aggregate estimate is a relative asymptotic if `H^delta<=U,V<=H^C` for fixed positive delta,C. The per-sector error may dominate when V/H is small. Neither assertion counts prescribed list lines, inverse-ratio intervals, or high-moment paths.

The exact image has area `15UV/H` and slice height `V/H`. Its bounding rectangle has area ratio `1+15cU/V`, so replacing the exact domain can lose a large factor. This geometric restriction gives a better exact-edge bound than the frozen statement's safe constant 17.

**Proved, reviewed sharpening.** Fix a primitive P', a sector, and D,a,b, and impose the exact determinant `det(P',Q')=D(b-a)`. There are at most two partner positions Q' in the exact domain. If H is even and both endpoints have first coordinate coprime to H, there is at most one.

To prove it, all integer solutions are `Q'=Q'_0+jP'`, because P' is primitive. The inverse sector map is linear, so their original positions satisfy `Q=Q_0+jP`. Their second coordinates lie in `[V,2V]` and are separated by `v_P>=V`. This interval of length V contains at most two such values. If two occur, they are consecutive, and equality forces `v_P=V`. For even H, u_P and every allowed u_Q are odd. Consecutive candidates have first coordinates differing by the odd number u_P, so only one can be a unit modulo H. This proves the sharper bound. It counts positions for a fixed transition, rather than lists or the nonexact comparison term.

## What the independent computations establish

The main finite branch checked 772 primitive forward/complement cases, 28,400 inverse-lattice cases, 40,632 ordered position pairs with 48,299 common-divisor cases, 975 character sums, 960 nonzero-frequency full-pullback identities, 15 zero-frequency measures, and 2,160 exact sector/Mobius counts. All reported checks passed. Its larger partner pool allowed nonunit first coordinates for Q and observed a largest partner group of two; this does not contradict the even-H unit-first-coordinate bound of one.

The supplemental `edge_unit_check.py`, with source hash `abc70eede4c1429cfcc9422112a2ce75a85eb89f0e4d73fe07c89c85b2489173`, restricts both endpoints to unit first coordinates. For even H from 2 through 30 and the recorded U,V values, its 103,228 evaluated pairs had maximum partner count one and zero failures. These are bounded empirical checks of the argument, not the proof of its uniform conclusion. The displayed big-O scales in the main branch are diagnostics and do not certify asymptotic constants.

The assertion that ordinary arcs force cross-sector vanishing is **refuted** by the finite branch's exact witness: `H=6`, `P=(5,1)`, `Q=(7,1)`, `a=7`, `b=5` has frequency 10, with integral `-sqrt(2)/(20 pi)` on `[-1/16,1/16]`, whereas its complete six-fold pullback integral is zero. The witness itself is an established finite calculation; it is the ordinary-arc assertion that is refuted.

## The arithmetic obligation remains

The complete pullback of an arc around zero contains centers j/H, with width divided by H and reduced denominator H for unit j. A center a/k similarly produces `(a+jk)/(Hk)`. At moving `H` of ambient size these are new large-denominator arcs. Equal measure does not bound prime exponential sums on them. Keeping ordinary small-denominator arcs instead can leave nonzero cross-sector comparison terms. Thus the accepted conjugacy is for the deliberately changed centered operator. Its comparison term has not been identified with an already controlled Goldbach major part.

The inspected source equations (4.18)-(4.28) motivate the finite map, but no full Lue-Wang-Wu theorem or extension of its prescribed-modulus root averaging is imported. No uniform centered-operator bound on the exact H-dependent domains, list-constrained root moment, or actual-prime cancellation is obtained. The polynomial-label limitations and h=1 prime boundary from LABELS-005 also remain.

RATIOS-007 is an in-progress arithmetic follow-up on unweighted complement-ratio sums. Its author statement is frozen for separate review, and it is not an accepted dependency of this revision. Any future use must distinguish unweighted position distribution from the actual prime coefficients, prescribed lists, paths and required high moments. The research objective stays open: a new arithmetic estimate with the true H and list-modulus costs is required before this reduction can yield a Goldbach lower bound. No proof, demonstrated breakthrough or novelty claim follows from this stage.
