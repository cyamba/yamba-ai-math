# Illustration assets

Each illustration has a 1200 × 700 SVG and a matching 1800 × 1050 PNG fallback. The graphics are intended for a responsive article; keep the aspect ratio and use the SVG as the preferred source.

## 01_problem_route

**Caption:** The KR1 objective links residue partitions with gap partitions. Flat columns and cluster coordinates give a second representation of the problem. The all-index positive cut-word theorem supplies auxiliary models; the global bridge and the object-level recurrence maps remain open.

**Alt text:** A diagram shows residue partitions with parts congruent to 1, 3, 6, or 8 modulo 9 above flat columns U, and gap partitions above cluster coordinates. A dashed coral line between the lower boxes is labeled open. A separate box describes positive cut-word models and says the recurrence maps to the gap class remain unresolved.

## 02_marker_cancellation

**Caption:** For n = 6, the word ||α|β||| has intrinsic particle weights 28 and 32. Removing the negative marker of weight 18 and increasing δ₇ by one raises the final two cut indices by one. Both signed partners have weight 78.

**Alt text:** Eight word cells read cut, cut, alpha, cut, beta, cut, cut, cut. The initial indices are all zero. A negative weight-18 marker is removed as δ₇ increases by one; the final two indices change from zero to one, contributing 9 each. The intrinsic weights are alpha 28 and beta 32, and the total weight is 78 on either side.

## 03_particle_count_obstruction

**Caption:** In the n = 0 row at weight 8, a C₀ object has one colored particle and a common part of weight 3. The only target objects at weight 8 have either two colored particles in A₁ or none in the shifted A₂ branch. The two shifted C₁ branches contain no object at weight 8.

**Alt text:** The left column lists two weight-8 C₀ objects: beta of weight 5 with a common part 3, and two alpha particles of weight 4 each. The right column lists two beta particles of weight 4 in A₁ and an empty A₂ object with shift 8. A note says the shifted C₁ branches have no weight-8 objects. The conclusion states that no target has exactly one colored particle.

## 04_evidence_scope

**Caption:** The all-index positive-model theorem, selected Lean lemmas, and bounded tests provide different kinds of evidence. The complete KR1 product-to-gap bijection remains an open construction.

**Alt text:** Four stacked panels distinguish the all-index written theorem on positive cut-word models, selected Lean lemmas, finite independent checks, and the open full KR1 bijection. Each panel briefly states the scope of its result or verification.

## Regeneration

Run `python3 render_figures.py` from this directory or `python3 research/rogers-ramanujan/terra2026/publication/assets/render_figures.py` from the repository root. The script uses Inkscape for PNG export.
