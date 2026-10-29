# Separate unchanged-A3 endpoint composition review

Distinct Fleet B critic, 24 October 2026. This later composition record is
separate from the completed `review-1.md` and its final pins. **Verdict:
supported for the exact partial composition; incomplete for full KR1.**
It changes no A3 definition and freezes no fourth construction variant.

## Universal scope

Let E_A:A→C be the actual RR003 direct extraction/merge endpoint reviewed
by critic A in `../fleet-a/review-1.md`, section 4. Let E_B:U→B be the
actual RR003 Stockhofe endpoint separately reviewed in
`stockhofe-review.md`. Let F:D_C→I_U be exactly the unchanged frozen A3
bijection accepted in critic A's initial review. Its C domain is

- every a in {0,1}, with arbitrary b;
- every a=2,b=0;
- every a=3,b=0;
- every a=2,b>=1 with first mu entry zero.

Define D_A={A:E_A(A) in D_C} and D_B={B:E_B^(-1)(B) in I_U}. These are
intrinsic finite membership tests, using the literal endpoints and the
frozen branch/image predicates. The explicit composition is

`G=E_B ∘ F ∘ E_A : D_A → D_B`,

with inverse `E_A^(-1) ∘ F^(-1) ∘ E_B^(-1)`.

**Proved with separately reviewed ordinary arguments:** each endpoint
and F has exactly its stated full or partial image; therefore the
composition is valid on every member of D_A and its inverse on every
member of D_B. Cancelling the adjacent mutually inverse maps proves
both identities. Each map preserves the same literal sum/Q/F weight and
terminates, so the composition does too. This is a universal exact partial
map, not a theorem inferred from the finite totals below. The assurances
of the component reviews remain ordinary written assurance, without formal
certification or independently verified novelty.

The domain is proper. C=(2,1,(1,1),(0)) has weight fifteen and is excluded
by positive first mu. Direct merging gives its literal A=(1,2,5,7), also
excluded. On the B side, literal B=(15) has Stockhofe inverse U=(9,6),
which fails every retained A3 image branch. These are scope boundaries.
The frozen map does not contain the subsequently proposed wall operator W.

## Frozen implementation and independent literal enumeration

`checks/critic_b_composition.py` invokes the **actual**
`checks/rr003_cluster_merge.py` and `checks/rr003_stockhofe.py` modules
(paths relative to `research/rogers-ramanujan/` for those two files).
For F it uses the already reviewed canonical A3 functions in
`../fleet-a/checks/critic-a-literal.py`, converting only between the C
tuple and the endpoint's `ClusterData`. Thus the A3 mathematical map is
unchanged and the check does not depend on disposable `.runs/` author
imports. The canonical A3 checker retains SHA-256
`6c6be584e6da5c29fb85e95eb749faaa7cda39f26d51b8fdabecca0cf2297984`.
The composition checker itself has SHA-256
`c46a18dfdbb99c7ca543e2ac1df52bee40ed2afffa5d92f13a1736e35763ba6e`.
`composition-freeze.json` pins it, the A3 definition/implementation, the
two actual endpoint modules and their `kr1` dependency before the pilot.
Every execution verifies those pins before importing any mathematical
module. No legacy test module is imported.

The checker independently generates literal positive ascending A and B
objects. For A it tests the adjacent-sum and distance-two conditions; for
B it uses precisely residues 1,3,6,8 modulo nine. It first verifies endpoint
validity/round trips and weight on all enumerated inputs. It then checks
both composed identities, exact admitted domain/image sets, literal
membership and common weight at every intermediate stage. It counts
distinctness on the actual A/B tuples: distinct means no repeated literal
part, with the empty object included as distinct.

Pilot `critic-b-composition-pilot12` passed before any thirty run. Root
explicitly approved unchanged named extension
`critic-b-composition-through30` at 21:26:18 UTC after inspecting the
pilot and hash. The extension also passed. No actual endpoint or
intermediate object exceeded the respective bound.

| Run | All literal A / B | Partial each | A distinct / repeated | B distinct / repeated |
| --- | ---: | ---: | ---: | ---: |
| Pilot 12 | 59 / 59 | 59 | 56 / 3 | 15 / 44 |
| Approved 30 | 1,393 / 1,393 | 874 | 779 / 95 | 32 / 842 |

At thirty the full literal A population is 1,229 distinct/164 repeated;
the full B population is 127 distinct/1,266 repeated. These denominators
are included in the compact result, rather than quietly comparing
different cohorts.

The joint cohort table is for **the same partial composed map**, with A
as source and B as target:

| Literal A cohort / literal B cohort | At most 12 | At most 30 |
| --- | ---: | ---: |
| Distinct / distinct | 15 | 32 |
| Distinct / repeated | 41 | 747 |
| Repeated / distinct | 0 | 0 |
| Repeated / repeated | 3 | 95 |

The zero repeated/distinct cell is only a bounded observation, with no
universal assertion. Literal distinctness is not preserved: for example,
the actual composition maps A=(2) to B=(1,1). All A3 branches are exercised
by thirty. Its 874 cannot be added to A1/A2 totals, the separate B2 cone,
or the older partial assignments. U distinctness and within-C-vector
increment distinctness are different predicates and are not substituted
for any number in these tables.

## Saved evidence and limits

Compact results are `checks/critic_b_composition_12.json` and
`checks/critic_b_composition_30.json`. Full literal rows remain ignored at
`.runs/rr007/critic-b-composition-{12,30}-rows.json`; raw compact outputs
and meter receipts have the matching names. The pilot took
0.09044425000320189 seconds and observed child RSS 24,330,240 bytes; the
extension took 0.32453037501545623 seconds and observed 33,177,600 bytes.
RSS is observed after exit, not a hard transient guarantee.

All subprocesses used the active meter and old ledgers were left closed.
An unquoted search regex caused a shell pipeline failure and a metered
broad import-line search; its child receipt is
`critic-b-compose-imports.receipt.json` (child exit zero, outer shell
exit 127). A corrected search then encountered a wrong guessed filename,
retained in `critic-b-compose-imports-2.receipt.json`. Neither utility
attempt executed tests or changed mathematical inputs. The successful
mathematical runs are exactly the two named composition runs above.

No new source retrieval occurred: the combined source totals remain
8 query strings, 18 opens and three detailed source records. No
additional candidate, provider, dependency, external message, formal
proof-checker run or publication occurred. The completed B core review
and `.runs/rr007/critic-b-final-pins.json` remain unchanged.
`composition-final-pins.json` separately records this new composition's
artifacts and verifies the preserved core pins. The checker can be run
from the repository root within an authorized budget with argument 12
or an explicitly approved 30; it writes into an existing `.runs/rr007/`.
