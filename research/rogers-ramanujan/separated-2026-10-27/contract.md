# Separated pair compiler investigation, 27 October 2026

Authorization: Christopher requested investigation of the attached lookup-free KR1
harness and a valuable independent subresult. This is a new bounded investigation;
RR003/RR004 ledgers remain closed. Base: 4ccc4fe (PR16 head, verified remotely).

Objective: audit the supplied compiler, characterize its exact valid domain and
image, prove both inverses, and derive a positive generating function if possible.
Full residue-gap KR1 remains the overarching unresolved objective. This compiler
acts on cluster coordinates, not residue partitions. No claim of resolving the
missing residue/cluster bridge, no novelty claim, and no formal certification.

Budget: at most 90 minutes active work, ten cumulative minutes enumeration,
2 GiB per enumeration process, 1 GiB incremental storage, 5 GiB free-space floor;
standard-library Python only, one separate critic, at most two criticism rounds.
No new paid providers, external messages, user-file deletions or website changes.
Work is on an isolated worktree. Prepare local commit and reviewable artifacts;
no remote push or external publication in this contract.

Stop: retain a written theorem with separate review, or an exact counterexample;
do not attempt a broad global KR1 reconstruction. Enumerate through weight60 only
if small-case falsification and the inverse gate have been completed. Record
commands/results and preserve the supplied compiler's failure separately.

## Reflection and discovery exposure

Applied tweak 1: test literal output validity before studying collisions. Evidence:
the supplied compiler contains a `pass` at the advertised boundary repair and
leaves carry_lift unchanged. Cost: a small exact pilot. Outcome: first invalid
output at N10, (a,b,mu,nu)=(1,1,(0,),(3,)) -> (4,3,3).

Applied tweak 2: require intrinsic target recognition and inverse before a large
sweep. Evidence: prior restricted maps collided when overlaid (RR003) and PR15's
N41 extension failed. Cost: one proof and one separate review; no claim that this
workflow improves scientific success generally. If inverse or image fails,
retain the obstruction instead of extending the sweep.

Discovery-exposed: supplied text, existing RR003 endpoint-cluster-merge.md,
existing PR15/16 status and the N0..12 pilot. Conjectured criterion before broad
verification: for a,b>0, mu_a >= ceil(3*(nu_1/3)/2). Pure sectors unrestricted.
Expected image: gap partitions whose descending atom word is S^a P^b.
