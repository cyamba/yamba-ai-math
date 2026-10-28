---
name: visualize-math
description: Choose and build faithful mathematical visualizations (diagrams, plots, tables, interactive pages, animations, proof and dependency maps) computed from code, with a caption that says what to notice and what the picture does not show. Use for figures in explanations, articles, talks and teaching.
---

# Visualize mathematics

A figure is an argument the eye can check. It must be computed from the mathematics, not drawn
from memory.

## Pick the picture from the object

| Object | Faithful pictures |
| --- | --- |
| Partitions, compositions, words | Ferrers or Young diagrams; part-frequency tables; a bijection shown as before and after with parts colored by role |
| Bijections and algorithms | A state trace step by step; a slider or stepper through the steps; arrows between matched objects for small sizes |
| Sequences, generating functions, q-series | Coefficient tables; difference tables; growth on a log scale; residue or parity color maps |
| Groups and symmetry | Cayley graphs; multiplication tables as heat maps; subgroup lattices; orbit pictures |
| Recursions and induction | Recursion trees; the induction step as a picture of n against n + 1 |
| Large proofs and formalizations | Dependency graphs and proof maps, nodes colored by status |
| Inequalities and analysis | Plots with the extremal case marked; regions where a bound is tight |
| Matrices, attention, models | Heat maps, spectra, low-rank factor pictures |

## Tools, lightest first

- **Markdown on GitHub**: Mermaid for flows and dependency graphs; tables for small data.
- **Static figures**: Python with matplotlib, saved as SVG and PNG, or SVG written by a script.
- **Papers**: TikZ or pgfplots in the article's LaTeX.
- **Interactive**: one self-contained HTML file with inline SVG and script; sliders for n, q
  or the step index.
- **Animation**: an HTML stepper or a frame sequence first; heavier tools only when needed.

Keep the generator beside the output (`figures/make_<name>.py`) and note the command that
produced each figure.

## Rules

1. **Data from definitions.** The plotting code calls the same functions as the examples. For a
   bijection, check on the displayed cases that the maps are mutually inverse.
2. **One message per figure.** Write the caption first ("Notice that ..."). If the caption is
   hard to write, the figure is wrong.
3. **Small and complete beats large and blurry.** Show sizes up to where the pattern is visible
   and every object is legible.
4. **Encoding**: position first, then shape, then color. Use a colorblind-safe palette, never
   rely on color alone, label directly instead of through a legend where possible, and make
   the figure readable on light and dark backgrounds.
5. **Show status**: proved versus conjectured nodes in a proof map; the checked range versus
   extrapolation in a plot.
6. **Alt text states the takeaway**, not just the content.
7. **Say what it does not show**: for example "checked for n at most 12" or "the drawing
   suggests a continuity the discrete object does not have".

## Deliverable

Generator script and command, figure files (SVG preferred), caption, alt text, checked range,
and a pointer to the definitions used.
