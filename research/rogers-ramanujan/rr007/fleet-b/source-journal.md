# RR007 Fleet B retrieval journal

All retrievals below used the read-only web tool. Times are UTC on
2026-10-24; grouped timestamps are the surrounding tool-call times, not
server-side publication timestamps. **Final initial usage: 8 query strings,
12 opens, 3 detailed source records.** Reserved criticism allowance remains
4 query strings, 6 opens, at most 3 further detailed records across RR007.
No local curl/network subprocess or additional retrieval was used.

## Attempts in order

| Time | ID | Exact query or URL/line target | Result and inspection scope |
|---|---|---|---|
| 20:46:12 | O1 | https://arxiv.org/html/2002.00300v2 | Primary full HTML indexed, 1352 lines; initial response exposed introduction, grounding, flat/regular definitions and theorem leads. |
| 20:46:17–20:46:21 | Q1 | `Kanade Russell first identity bijective proof 2025 2026 KR1` | Returned older mod-12 analytic work, current secondary status pages and new-paper leads. Secondary returns were discovery only, not substantive evidence. |
| same | Q2 | `Kanade Russell conjectures bijection first conjecture proof Konan weighted words` | Same grouped response; no primary full KR1 bijection located. |
| same | O2 | https://arxiv.org/html/2002.00300v2 line 330 | Low-yield return around regular definition; not a full proof read. |
| same | O3 | https://arxiv.org/html/2002.00300v2 line 610 | Wrong proof target, crystal section; no mathematical result imported. |
| 20:46:23–20:46:27 | O4 | https://arxiv.org/html/2002.00300v2 line 270 | Definition 2.1 minimal energy; secondary-part definitions; degree-two proof not obtained. |
| same | O5 | https://arxiv.org/html/2002.00300v2 line 335 | Theorem 2.8, exact ground hypotheses, preservation statement, ordinary m-flat specialization. |
| same | O6 | https://arxiv.org/html/2002.00300v2 line 770 | Flat-to-regular formulas and size/p-positivity/bounded-length argument, lines about 743–807. |
| same | Q3 | `site:arxiv.org "Kanade" "Russell" "modulo nine" 2026 bijection` | Located Xia 2609.08816 and Mizuno 2609.09653 primary records. |
| same | Q4 | `site:arxiv.org "Kanade" "Russell" bijective proof identity modulo 9` | Grouped results include analytic primary preprints and older mod-12 work; no bijection conclusion. |
| 20:46:31–20:46:36 | O7 | https://arxiv.org/html/2002.00300v2 line 675 | Regular staircase decomposition, flat insertion-slot data, about lines 653–722. |
| same | O8 | https://arxiv.org/html/2002.00300v2 line 825 | Explicit inverse (4.13),(4.14), insertion and flat-validity argument through (4.17), about lines 809–892. |
| same | O9 | https://arxiv.org/html/2609.08816 | Xia v1 dated 8 Sep2026; primary abstract/intro start/contents only. Claims analytic results; proof not audited. |
| same | O10 | https://arxiv.org/html/2609.09653 | Mizuno v3 dated 5 Oct2026; Theorem 1.1 exact KR1 formula and A-equivalence paragraph, contents; proof not inspected. |
| 20:46:46–20:46:50 | O11 | https://arxiv.org/html/2002.00300v2 line 730 | Flat-to-regular start, lines 730–742, complementing O6. |
| same | O12 | https://arxiv.org/html/2002.00300v2 line 925 | Jumped to section 5 Proposition 5.1; final inverse tail 893–919 remained unexposed. No degree-two claim imported. |
| same | Q5 | `"Kanade" "Russell" "bijection" "2026"` | Mostly unrelated current partition papers and analytic leads; no verified KR1 bijection. |
| same | Q6 | `site:arxiv.org/html/2609.09653 "proof" "bilinear" "Casoratian"` | No useful direct primary proof excerpt in grouped returns. |
| same | Q7 | `"Kanade–Russell" "bijective proof"` | Returned Konan primary journal text excerpt on interpreting KR identities through flat partitions; retained only as a lead, not a solved specialization. |
| 20:47:06–20:47:07 | Q8 | `site:arxiv.org/html/2002.00300v2 "bijection" "4.18" "4.19"` | Empty search results; attempted remaining proof-tail retrieval failed. Counts against query ceiling. |

## Local utility receipts and limits

All local reads were run under `.runs/rr007/meter.py` with category b and
bound 0. Labels: `rr007_b_sources_boot` failed before execution because
reserve=0 is forbidden by the meter; `rr007_b_sources_boot2` read assigned
instructions; `rr007_b_sources_read_prior` read README and RR006 prior
source records; `rr007_b_sources_defs` was an rg utility that failed on two
nonexistent guessed paths while returning matching RR007 notes;
`rr007_b_sources_verify` checked the saved algorithm handoff. No
mathematical subprocess or enumeration ran. The meter receipts, not this
prose, hold measured elapsed seconds and RSS. File editing used apply_patch.

The precise fixed-sector obstruction and the five-color U/B derivation in
sources.md are author-only mathematical arguments for the next author and
critic. They do not consume a new candidate variant or justify finite
extension. Full C encoding, literal weight compatibility, image closure
and all KR1 endpoint composition remain open obligations.
