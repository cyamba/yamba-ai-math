---
name: understand-math
description: Understand, explain, illustrate and teach the mathematics in this repository (results, proofs, constructions, generated outputs) through intuition, visualizations, verified examples, step-by-step walkthroughs, explanations at several abstraction levels, theorem applications, answers to questions, and articles or textbook chapters. Use to make results understandable and usable, not to prove new ones.
---

# Understand mathematics

This folder is the exposition layer. The solver layer (`agents/`, `skills/`, `research/`)
produces and checks mathematics. This layer makes it understandable and usable for a reader, a
student, the operator, or another agent that needs intuition to take the next step. Explaining a
result often reveals the next question; this layer captures those questions and routes them
back to the solver.

Read [AGENTS.md](AGENTS.md) in this folder before writing anything durable.

## Non-negotiables

1. **Carry the status.** Open every explanation with the claim's status and source:
   `established`, `proved`, `conjecture`, `empirical`, `unverified` or `refuted`, plus the
   inspection level or proof assurance. Explaining never upgrades a status.
2. **Compute, do not invent.** Every number, table, example and figure comes from code that
   implements the definitions, or from a hand check written out so a reader can redo it.
3. **Label the informal.** Intuitions, analogies and pictures are labeled as such, and every
   analogy says where it breaks.
4. **Route, do not solve.** A gap, an error or a new idea found while explaining is recorded and
   routed (see "Feed the solver"), never silently patched inside the explanation.

## Choose the workflow

| The request sounds like | Load |
| --- | --- |
| "Why is this true?", "What is the idea?" | [build-intuition](skills/build-intuition/SKILL.md) |
| "Show me", "draw it", figures for a paper or talk | [visualize-math](skills/visualize-math/SKILL.md) |
| "Walk me through the proof, derivation or algorithm" | [step-by-step](skills/step-by-step/SKILL.md) |
| "Explain it simply", "for an expert", several audiences | [abstraction-levels](skills/abstraction-levels/SKILL.md) |
| "Give examples", "edge cases", "is there a counterexample?" | [forge-examples](skills/forge-examples/SKILL.md) |
| "How do I use this?", "where does it apply?" | [apply-theorem](skills/apply-theorem/SKILL.md) |
| A direct question about a concept or result | [answer-question](skills/answer-question/SKILL.md) |
| An article, blog post, lecture notes, textbook chapter, course | [write-exposition](skills/write-exposition/SKILL.md) |
| "What did we, or they, just prove, and what does it give us?" | [digest-result](skills/digest-result/SKILL.md) |

Real requests combine two or three. A typical explainer runs digest-result, then forge-examples,
then visualize-math, then abstraction-levels. Load only what the request needs.

Shared material: the [levels ladder](references/levels.md), [exposition styles](references/styles.md),
the [quality checklist](references/quality-checklist.md), and templates for an
[explainer](templates/explainer.md) and a [worked example](templates/worked-example.md).

## Default flow

1. **Pin the object**: exact statement or construction, its source file or citation, its status.
2. **Choose** audience, goal, level range and style.
3. **Build** verified examples first, then pictures, then the idea, then the steps.
4. **Check** against the quality checklist.
5. **Deliver**: in the conversation for one-off answers; as files under
   `understanding/explainers/<slug>/` (or the owning project's paper or publication folder) for
   durable material, with the scripts that produced every example and figure.

## Feed the solver

| Found while explaining | Route (paths from the repository root) |
| --- | --- |
| A suspected error or gap in a repository result | The owning research folder's feedback or review files (for KR1, `research/rogers-ramanujan/feedback.md`); the `audit-theorem` workflow in `skills/` |
| A new conjecture, generalization or direction | Label it `conjecture`, novelty NOT VERIFIED; propose an `explore/` brief with `explore-angle` only with authorization |
| An external lead (paper, tool, venue) | `novelty_radar/` |
| A reusable explanation | `understanding/explainers/<slug>/` |

Explanation is not publication: posting or submitting anything needs the operator's separate
authorization.
