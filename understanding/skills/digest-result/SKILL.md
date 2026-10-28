---
name: digest-result
description: Turn a newly generated or newly found mathematical result (a solver output, a Lean formalization, an external paper or an AI-generated manuscript) into understanding. A statement card, status and provenance, dependency map, key idea, verified small examples, what is new, consequences, risks, and new questions routed to the right place. Use after a result appears and before building on it.
---

# Digest a result

Understanding a result is how it becomes usable: for intuition, for applications and for the
next question. A digest is short enough to read in ten minutes and links to everything longer.

## Produce the digest

1. **Statement card**: the exact statement or construction with its definitions; the source
   (file and commit, or citation and version). For a formal result, the declaration name, what it
   imports and which axioms it uses.
2. **Status and provenance**: the claim label; who or what produced it (human, model, agent
   swarm, mixed); what checked it (proof checker and version, separate review, nothing yet).
   Generated and external results default to `unverified`.
3. **Dependency map**: what it uses and what uses it. Draw it once there are more than five nodes
   (visualize-math).
4. **Key idea** in one sentence and a skeleton of three to seven moves (build-intuition,
   step-by-step).
5. **Smallest examples, computed** (forge-examples), including one case where the result is
   sharp or a hypothesis visibly matters.
6. **What is new**, compared with the closest known result. Keep "Novelty status: NOT VERIFIED"
   unless the closest work was actually inspected.
7. **Consequences**: what it lets us do, especially in current projects (apply-theorem).
8. **Questions it raises**: generalizations, converses, constructive versions, sharper bounds,
   formalization targets, each labeled as a question or a conjecture.
9. **Risks**: suspected gaps, unclear definitions, reliance on unchecked material, a formal
   statement that may not match the informal one.

## Route what you find

| Finding | Route (paths from the repository root) |
| --- | --- |
| Suspected error or gap in a repository result | The owning research folder's feedback or review files; `audit-theorem` |
| New conjecture or direction | A proposed `explore/` brief through `explore-angle`, only with authorization |
| External lead (paper, tool, venue) | `novelty_radar/` |
| Durable explainer | `understanding/explainers/<slug>/` |

## Output

Use the [explainer template](../../templates/explainer.md).
