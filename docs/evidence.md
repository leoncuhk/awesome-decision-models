# Evidence ledger / 评测证据

[Home](../README.md) · [中文首页](../README.zh-CN.md) · [Methodology](methodology.md)

These are **archival claim records**, not a common leaderboard. None was rerun by this repository. A source review checks what was reported, not whether the underlying experiment is reproducible or unbiased.

本页保存带条件的历史声明，不生成混合排名。五项记录均为来源报告，不是本仓库独立复现。来源阅读、产物审计与实验复现是三种不同工作。

Reported fractions are displayed as percentages where appropriate. More printed digits do not imply greater statistical precision. Source publication dates remain unknown unless independently established.

<a id="e01"></a>
## E01 · Laya: specialist performance is not base-model performance

**Evidence:** `author_reported` · **Reviewed:** 2026-09-25 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | Four synthetic typed-decision workflows |
| Test unit | 400 cases containing 2,000 decisions |
| Split | Official test split reported by the author; specialist uses workflow training data |
| Reference | Teacher-based synthetic benchmark references, not independent observed business outcomes |
| Training | Specialist fine-tuned; base comparison is not fine-tuned on these workflows |
| Measurement | Hard-label accuracy; calibration caveats separately reported |
| Hardware | Not required for the accuracy statement; no latency claim imported |

| Reported measurement | Value |
| --- | --- |
| Workflow-specialized Laya accuracy | 76.60% |
| Base Laya accuracy | 36.20% |
| Per-question majority baseline | 46.10% |

**Interpretation:** The useful result is a within-project base-versus-specialist contrast, not evidence of universal superiority over Jev.

- The Jev value on the source card is imported from another report with different prompts/sample sizes; excluded from this side-by-side measurement.
- The released checkpoint discloses temperature fitting on a training slice and a conflicting inherited temperature configuration. Do not treat its current confidence as held-out calibrated.
- A teacher-agreement reference is not an objective ceiling on real-world correctness.

**Artifacts and limits:**
- protocol: public model card and linked notebook
- raw outputs: Not independently audited by this list
- model hash: not captured

**Sources:** [Laya Typed-Decisions model card](https://huggingface.co/convaiinnovations/laya-typed-decisions)

<a id="e02"></a>
## E02 · CLM: a domain-trained selector recovers more successful supplied candidates

**Evidence:** `author_reported` · **Reviewed:** 2026-09-25 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | DeepSWE trajectory selection |
| Test unit | 38 held-out tasks |
| Split | 75/38 task-disjoint training/evaluation split, seed 42; 66 training tasks have successful trajectories, split 59/7 for train/validation |
| Reference | Trajectory pass outcomes as described by the release; environment execution not rerun here |
| Training | A specialized projection head initialized from CLM v0.1-8B, not the generic checkpoint alone |
| Measurement | Best-of-4; trajectory score averages final 12 available step scores |
| Hardware | Accuracy claim only; candidate generation and full end-to-end cost not measured here |

| Reported measurement | Value |
| --- | --- |
| Selected successful tasks | 31/38 (81.58%) |
| Reported pass@1 baseline | 28/38 (73.68%) |
| Oracle success within supplied candidates | 34/38 (89.47%) |

**Interpretation:** This is selection improvement on a small, task-specific held-out set. It is not the coding success rate of a standalone 8B agent or a full official SWE benchmark score.

- The candidate generator, sampling budget and candidate quality are part of the system.
- 38 tasks provide limited precision; paired per-task outcomes are needed for a defensible significance analysis.
- Do not transfer results from this trained head to CLM zero-shot use.

**Artifacts and limits:**
- protocol: public model card, reproduce command and task-split description
- raw outputs: Linked dataset/reproduction path; binaries and execution not independently checked
- checkpoint sha256: 554989fe88635606cb978dc45a1ce083be1990c4a51e551ea3b6055ead1a029a
- heldout list sha256: d4e2e7639f9eace09fba50318a266111c080d591bfbe39d213c3ea611e7b65c1

**Sources:** [DeepSWE fixed-split projection head](https://huggingface.co/Contrastive-LM/deepswe-clm-heads-8k); [CLM repository](https://github.com/Contrastive-LM/CLM/blob/bb42c6c5bf914fd449bed2f6ca65be80602cb1f7/README.md)

<a id="e03"></a>
## E03 · Nimble vs Jev: paired human-reference comparisons remain task-dependent

**Evidence:** `author_reported` · **Reviewed:** 2026-09-25 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | 13 public-data subsets, including intent and sentence understanding |
| Test unit | 3,880 records overall; MASSIVE en-US example below has 350 records |
| Split | Public subset manifests and family identifiers described in the pinned report |
| Reference | Dataset human labels; some distributions are vote fractions rather than objective probabilities |
| Training | Released nimble-9b vs Jev 1.13.0; provenance of all pretraining data is not fully known |
| Measurement | Same record IDs and reference labels; no candidate shuffling; Nimble raw temperature 1.0 |
| Hardware | No speed conclusion imported |

| Reported measurement | Value |
| --- | --- |
| Nimble: MASSIVE en-US accuracy (n=350) | 86.90% |
| Jev 1.13.0: MASSIVE en-US accuracy (n=350) | 87.40% |

**Interpretation:** This is a useful paired protocol, but a small difference in one subset does not establish a general winner.

- The Nimble project ran the comparison; it is not an independent audit.
- Manifests and procedures are public, while raw run/comparison outputs are gitignored and must be regenerated.
- A subsequently fitted temperature was not applied to these reported runs; do not mix it with the displayed calibration numbers.
- Records can share source families. Uncertainty analysis should account for clustering and multiple comparisons.

**Artifacts and limits:**
- protocol: Pinned source commit 62076b4f2d365b5879dafcf7f6dd072a1fe76df7
- raw outputs: Not all committed; report says regenerate from scripts
- model hash: Exact evaluated binary not independently hashed here

**Sources:** [Nimble public human-reference benchmark protocol and results](https://github.com/bespokelabsai/nimble/blob/62076b4f2d365b5879dafcf7f6dd072a1fe76df7/docs/PUBLIC_BENCHMARKS.md)

<a id="e04"></a>
## E04 · GLiNER2.5-Decide: keep a newly reported suite in its proper scope

**Evidence:** `author_reported` · **Reviewed:** 2026-09-25 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | fastino/fast-decisions classification |
| Test unit | 17 domains × 300 held-out examples = 5,100 records, as reported |
| Split | Author-described held-out split; independent dataset inspection incomplete |
| Reference | Label provenance and benchmark construction not fully audited here |
| Training | Checkpoint-specific models; training/test overlap not independently established |
| Measurement | Average exact-match accuracy on an English suite |
| Hardware | No speed conclusion imported |

| Reported measurement | Value |
| --- | --- |
| GLiNER2.5-Decide 340M, cross-reported in the 1B card | 60.20% |
| GLiNER2.5-Decide-1B | 59.60% |

**Interpretation:** The card supports including this family in local classification experiments, not declaring it universally better than Jev or Laya.

- The accessible source is the 1B card, not an independently audited 340M release.
- The table contains JevK5, not TypeSafe Jev.
- The English suite cannot establish multilingual production quality.
- A larger model does not automatically win this particular reported suite.

**Artifacts and limits:**
- protocol: Model card; referenced dataset card was not fully accessible during review
- raw outputs: Not independently inspected
- model hash: not captured

**Sources:** [GLiNER2.5-Decide-1B model card](https://huggingface.co/fastino/GLiNER2.5-Decide-1B)

<a id="e05"></a>
## E05 · Kev: preserve development/test and source-domain distinctions

**Evidence:** `author_reported` · **Reviewed:** 2026-09-25 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | Typed decisions on the project’s new-source suite |
| Test unit | Dataset/sample definitions must be read with the pinned repository report |
| Split | New-source development and held-out test are separate; trained-source results are a different slice |
| Reference | Project benchmark references; not treated here as real-world outcome labels |
| Training | Kev-4B release represented in the pinned README; model revisions can move independently of repository commits |
| Measurement | New Sources accuracy reported as development / test |
| Hardware | No hardware ranking imported |

| Reported measurement | Value |
| --- | --- |
| Kev-4B new-source development accuracy | 81.70% |
| Kev-4B new-source test accuracy | 83.80% |

**Interpretation:** The split distinction is more informative than copying a single score. This record is an archival source snapshot, not a claim about the latest downloaded weights.

- Model selection on development results is not a blind final evaluation.
- A pinned README commit fixes the source text, not the weights served by a live model ID.
- Do not compare these numbers with a different task mix or a Jev result from another split.

**Artifacts and limits:**
- protocol: Pinned source commit 2855ba2a55a80579176a459f78b95d03548cabb5
- raw outputs: Not independently replayed or fully audited
- model hash: not captured

**Sources:** [Kev repository](https://github.com/jaredpalmer/kev/blob/2855ba2a55a80579176a459f78b95d03548cabb5/README.md); [Kev-4B model card](https://huggingface.co/jaredpalmer/kev-4b)

