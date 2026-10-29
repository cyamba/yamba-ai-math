# ETH-E02. Proof complexity: which proof systems capture the algorithm?

| Field | Value |
| --- | --- |
| Category | Proof complexity |
| Source items | "Algebraic vs combinatorial SAT: triumph of non-local polynomial interpolation over DPLL/CDCL" |
| Status | **Open** |
| Depends on the upstream theorem | Yes |
| Score (I/B/T/L/Lean) | 4 / 4 / 2 / 3 / 2, composite **3.3** |
| Subresults | none |

## Task

If Theorem 1.1 holds, every unsatisfiable 3-CNF has a $2^{o(n)}$-length certificate (the
algorithm's run). In which Cook–Reckhow proof systems do refutations of size $2^{o(n)}$ exist for
**all** unsatisfiable 3-CNFs?

## Known boundaries

Resolution needs $2^{\Omega(n)}$ on random 3-CNFs (Chvátal and Szemerédi, J. ACM 1988) and on
Tseitin formulas over expanders (Urquhart, J. ACM 1987); Polynomial Calculus needs linear degree
on random $k$-CNFs (Ben-Sasson and Impagliazzo; Alekhnovich and Razborov) and hence exponential
size via Impagliazzo, Pudlák, Sgall; Cutting Planes has exponential lower bounds as well (level
T). So the algorithm's certificates cannot live in those systems.

## Conjecture to test

Extended Frege (or even Frege) has $2^{O(n\log\log n/\sqrt{\log n})}$-size refutations of every
unsatisfiable 3-CNF. This would follow if the correctness of the counting routine (polynomial
identities over $\mathbb Q$, Hermite interpolation, Lemmas 3.2 and 3.3) is provable in a weak
bounded arithmetic with polynomial overhead in the size of the computation. The algebraic
identities proved in our Lean library are of this kind.

## Alternative target

An Ideal Proof System (Grochow, Pitassi) certificate: the sum over the cube is computed by an
algebraic circuit of size $2^{o(n)}$; turning "the sum of a nonnegative function is zero" into an
ideal-membership certificate needs care.

## Resource boundary

Two agents (bounded arithmetic formalization sketch; IPS encoding), one critic; statements only
in the first iteration.
