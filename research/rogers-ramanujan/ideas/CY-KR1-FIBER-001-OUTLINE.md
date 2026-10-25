# Christopher Yamba: reversible permutations in a discrete multidimensional tableau

ID: CY-KR1-FIBER-001-O1. Author of motivating outline: **Christopher Yamba**.
Recorded: 2026-10-25. Status: **SUGGESTED APPROACH; UNTESTED**.
Parent: [original intuition and clarifications](CY-KR1-FIBER-001.md).
The steps below are Codex's operational expansion of Christopher's suggestion,
not a verbatim transcript or an established construction.

## Aim and terminology

Investigate the lost choices in a collision fiber by representing numbered
squares and their assignments in a finite discrete cube or rectangular box
with additional axes. Record reversible operations, analyze the resulting
arrangements, and seek a uniform construction for every fiber.

Christopher calls this a possible "hypergeometric permutation arrangement."
That phrase is preserved as his working description of discrete
higher-dimensional geometry; no connection to hypergeometric functions or
an established named construction is assumed. Existence of one working
procedure comes first. Neither uniqueness of the procedure nor minimum
dimension is required.

## Suggested outline before attempting the construction

1. **Specify the state.** Model the ambient positions as a finite product
   C_d = {0,...,L_1-1} x ... x {0,...,L_d-1}. Record the labels of numbered
   squares, empty positions, axis conventions, and the tableau constraints.
   Distinguish intermediate working states from legal final targets.
   State whether arrangements differing by an axis permutation are distinct.

2. **Express each placement as a reversible move.** At fixed dimension,
   investigate swaps or other explicit permutations of positions, including
   empty positions, rather than an assignment that overwrites information.
   Specify each move's domain and inverse. For a dimension increase, record
   an explicit embedding and its inverse on its image. A swap need not
   preserve tableau validity or the required statistic; check those separately.

3. **Keep an assignment and operation ledger.** For each input and step,
   record: state before and after; ambient dimensions; square labels and
   old/new coordinates; the selected permutation; branch condition; inverse
   rule; and the weight or graph-inversion statistic before and after.
   Record any temporary statistic changes and how they must be compensated.
   Save rejected placements and the exact reason for rejection.

4. **Construct and compare endpoints across the fiber.** Begin with the
   pictured two-input collision. Also formulate Christopher's ten-input,
   ten-extra-directions example, clearly distinguishing an actual fiber
   from a synthetic illustration. Keep the assignments T_i <-> H_i, where
   H_i is the chosen higher-dimensional arrangement. Use a common coordinate
   convention when comparing endpoints, and check collisions across different
   fibers as well as within one fiber.

5. **Analyze the arrangements for a rule.** Look for recurring permutation
   cycles, coordinate orders, roles for additional axes, and branch conditions
   recoverable from the output. Seek a repeatable selection and decoding rule
   using the numbered squares and their arrangement. If a dimension does not
   suffice, investigate adding an axis. Prove eventual success rather than
   inferring it from a finite search; optimize the dimension only afterward.

6. **Decode without relying on an external trace.** First verify that replaying
   the logged moves backward recovers the input. Then ask whether the final
   arrangement itself determines every necessary reverse choice. The ledger
   is a discovery and verification aid: if decoding needs it, either encode
   its necessary information in a permitted final object or leave the inverse
   obligation open. Reversibility of separate local moves does not by itself
   prevent different move sequences from ending at the same arrangement.

7. **Connect to the required target and generalize.** Seek a reversible
   weight/statistic-preserving translation of the selected H_i into distinct
   legal original targets U_i. Literal geometric flattening is optional.
   Simply forgetting the additional coordinates is insufficient. Establish
   exact target coverage, separation between fibers, termination, and both
   inverse identities for all parameters. Keep the KR1 partition bridge and
   the separate signed-tableau cancellation problem distinct.

## First deliverable and stopping rule

A small placement table and reversible trace, with explicit coordinate
conventions, admissibility checks, statistic changes, and endpoint comparison.
Then state the candidate pattern and its first falsifier. Useful failure
witnesses include an invalid target, a wrong final statistic, two paths with
the same endpoint, decoding that requires an unavailable log, or a collision
introduced by the translation back to the original targets.

Related inspected evidence: the previous local shape-routing and
column-encoding [variants and their scope](/Users/christopheryamba/.codex/worktrees/kr1-fiber-splitting/autodidactic-traveler/research/rogers-ramanujan/fiber-splitting-20261025/RESULT.md).
They did not implement this cube/permutation procedure. Closest external
constructions and novelty have not been assessed for this outline.

This document records an approach only. No new search, enumeration, proof run,
or agent dispatch was performed. Preserve closed contracts and frozen evidence;
a subsequent attempt needs its own bounded scope under the existing workflow.
