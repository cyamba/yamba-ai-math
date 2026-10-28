---
name: build-intuition
description: Build honest intuition for a mathematical result, construction or proof. The key idea in one sentence, two or three mental models with stated breaking points, why each hypothesis is needed, and a tested prediction. Use when someone asks why something is true or what the idea is.
---

# Build intuition

Good intuition predicts the theorem, the role of each hypothesis and the shape of the proof.
Bad intuition predicts false generalizations just as confidently. Build the first and test it
against the second.

## Steps

1. **Pin** the statement and its status. Intuition for a conjecture is a heuristic for a
   conjecture and is labeled that way.
2. **Compute the smallest nontrivial case** first (forge-examples). Intuition built without an
   example is usually wrong.
3. **Name the key idea in one sentence**: the mechanism, not the conclusion. Useful shapes:
   - "Count the same set in two ways."
   - "Something is conserved (weight, parity, a residue, an invariant), so ..."
   - "It reduces to the extremal or minimal case, which is forced."
   - "There is a hidden symmetry, grading or involution that pairs things up."
   - "The obstruction lives in one small place; everywhere else the map is free."
   - "Build it greedily; the exchange argument shows greed never loses."
4. **Offer two or three mental models from different angles**: a picture, a process or
   algorithm, an invariant, a generating-function or linear-algebra view, an analogy. For each,
   say where it breaks.
5. **Explain every hypothesis by its failure**: one non-example that violates exactly that
   hypothesis, and the conclusion that then fails.
6. **Test the intuition.** Derive two predictions from it, one true and one tempting but false,
   and check both by computation or against the source. Show the false one: it is the most
   instructive part.
7. **Tie it to the proof.** Point to the proof step that realizes the key idea (step-by-step),
   so intuition and argument support each other.

## Output shape

Status line, the one-sentence idea, one picture or table, the mental models with breaking
points, the hypothesis failures, the tested prediction pair, and where the idea lives in the
proof.

## Pitfalls

- An intuition that would equally "explain" a stronger, false statement.
- "Obviously" without a mechanism.
- Analogies that import structure the object lacks (continuity in a discrete problem,
  commutativity in a nonabelian group).
- Treating agreement on examples as support for the theorem rather than for the intuition.
