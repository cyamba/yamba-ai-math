# Audit of the other supplied partition targets

Checked **2026-10-20**. The supplied problem notes are research suggestions,
not instructions or evidence of prior mathematical progress. The local
`Math/partition-of-integers/` directory contained no files, and the supplied
local integer-partition notes concerned notation and resources rather than
a proof. None of the rankings establishes tractability or novelty.

## Status and concrete corrections

| Note | Finding | Consequence for this investigation |
| --- | --- | --- |
| 01: Rogers--Ramanujan bijections | **Established in inspected literature:** Schur's theorem already has direct bijective proofs. **Reported proved in September 2026 preprints:** the five modulo-nine Kanade--Russell sum-product identities, and the remaining six modulo-twelve identities. A public Lean development covers the three symmetric modulo-nine identities. | Equality of the partition counts must not be advertised as our new theorem. A genuinely new natural bijection would be a different, substantial target; the supplied note does not specify one. |
| 02: congruence cranks | **Established in inspected literature:** Mahlburg's 2005 theorem already supplies infinitely many congruence families for the ordinary crank for every prime at least five. | This does not give exact equidistribution for every specified progression. A new exact crank requires a concrete triple `(A,B,M)` and a statistic, which the note does not provide. |
| 03: parity density | **Conjecture:** Parkin--Shanks equidistribution. **Established in inspected literature:** both parities occur infinitely often in every arithmetic progression. **Refuted as written:** the proposed series uses `p((24n+1)/24)`, whose argument is never an integer. | The proposed Hecke computation is not a defined experiment. A Sturm bound certifies an appropriate modular-form identity after its hypotheses are proved; it does not by itself certify the claimed general nonvanishing or density conclusion. |
| 04: Kronecker coefficients | **Unverified:** broad positive counting rules and unrestricted Saxl positivity are not supplied with proofs by the note. A recent claimed Saxl proof contains a material confusion between simple composition multiplicities and projective indecomposable multiplicities. | A claimed preprint result must be audited before it changes the target's status. The requested general positivity problem cannot be replaced by a finite base-case check. |
| 05: plane partitions | **Established in inspected literature:** the classical ten symmetry-class enumerations are known. **Open in current specialist descriptions:** a meaningful general ASM--TSSCPP bijection. | An unspecified puncture or boundary family is not a theorem statement. Smooth prime factors in a few counts do not imply a product formula. |

## Sources and inspection depth

The following are primary papers, author repositories, or specialist event
descriptions. “Theorem inspected” means the statement and nearby argument
were read; it does **not** mean the whole proof was independently audited.

- **01, theorem inspected:** Y. Mizuno, [*The three Kanade--Russell identities
  modulo nine*](https://arxiv.org/html/2609.09653v1), Theorem 1.1 and the
  partition definitions following it. For `i = 1,2,3`, the source equates
  partitions with minimum part `i`, distance-two gap at least three, and
  adjacent close-pair sum divisible by three, with residue-restricted
  partitions modulo nine. The proof uses cubic norm rigidity together with
  coefficient inequalities, not a direct partition bijection.
- **01, theorem inspected:** E. X. W. Xia, [*The modulo 9 Kanade--Russell
  identities and their Nahm-sum duals*](https://arxiv.org/html/2609.08816v1),
  Theorem 1.1 and recurrence/certificate structure. No independent full
  proof audit or local formal rebuild was performed here.
- **01, theorem inspected:** L. Wang, [*Proofs of Some Kanade--Russell Mod 12
  Conjectures*](https://arxiv.org/html/2609.07822v1), Theorems 1.1--1.2 and
  Corollary 1.3. This reports proofs of the six formerly remaining cases.
- **01, formal project README inspected:** Mizuno's
  [KR-mod9-lean](https://github.com/yuma-mizuno/KR-mod9-lean) formalizes
  identities of integer formal power series, including double-sum convergence.
  [Palomar's immutable v1 record](https://palomar-registry.org/entry?id=PALOMAR-2026-09-10-000002&version=1)
  reports checking commit `d8b921339ecc` with Lean 4.31.0 and NanoDa. That is
  upstream verification evidence; it is **not** a local build performed by
  this investigation. The upstream repository uses Apache-2.0 licensing.
- **01, published abstract and introduction inspected:** A. Y. Z. Wang and
  Y. Yang, [*A combinatorial proof of the Andrews--Alladi--Schur
  theorem*](https://doi.org/10.1016/j.disc.2026.115089). This also identifies
  earlier direct bijections for refinements of Schur's theorem.
- **02, theorem inspected:** K. Mahlburg, [*Partition congruences and the
  Andrews--Garvan--Dyson crank*](https://pmc.ncbi.nlm.nih.gov/articles/PMC1266116/),
  Theorem 1.1 and its stated relation to Ono's conjecture.
- **03, introduction and theorem inspected:** K. Ono, [*Parity of the
  partition function in quadratic
  progressions*](https://uva.theopenscholar.com/files/ken-ono/files/documents/pofnborcherds2025finaldraft.pdf).
  This records the remaining parity-density gap and states a theorem for
  certain square-free discriminants in quadratic progressions.
- **04, claimed proof selectively audited:** S. K. Lee, [*Staircase
  Minimality and a Proof of Saxl's
  Conjecture*](https://arxiv.org/html/2512.15035v1), Definition 2.6 and
  Proposition 4.2. For an ordinary multiplicity vector `g` and decomposition
  matrix `D`, the vector `g D` records **simple composition multiplicities**
  after reduction. It is not the vector of projective indecomposable
  multiplicities; a Cartan matrix separates these two vectors. Thus the
  displayed identification cannot justify the claimed saturation inference.
  This finding concerns that argument, not a disproof of Saxl's conjecture.
- **05, published introduction inspected:** V. Holmlund and J. Striker,
  [*Totally Symmetric Self-Complementary Plane Partition Matrices and
  Related Polytopes*](https://doi.org/10.1007/s00026-024-00723-0), Section 2.
  The [specialist talk abstract scheduled for 2026-10-22](https://www.esi.ac.at/events/t3502/)
  also describes the missing meaningful bijection. The talk had not yet
  occurred on the inspection date.

## Bounded recommendation

For a complete **existing** theorem plus a reusable formal proof, the
symmetric modulo-nine Kanade--Russell identities are a precise option,
with explicit upstream attribution. For an **original** solution, none of
notes 01--05 currently supplies a sufficiently narrow, verified open
statement whose full proof is justified by the available progress. The
selected poset-positivity investigation therefore retains its exact open
target and reports finite computations and proved local results separately.
