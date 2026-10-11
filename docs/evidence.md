# Evidence ledger / 评测证据

[Home](../README.md) · [中文首页](../README.zh-CN.md) · [Methodology](methodology.md)

These are **archival claim records**, not a common leaderboard. None was rerun by this repository. A source review checks what was reported, not whether the underlying experiment is reproducible or unbiased.

本页保存带条件的历史声明，不生成混合排名。所列记录均为来源报告，不是本仓库独立复现。来源阅读、产物审计与实验复现是三种不同工作。

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

<a id="e06"></a>
## E06 · Clef: a vendor comparison has task-specific reversals

**Evidence:** `author_reported` · **Reviewed:** 2026-10-02 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | When2Call multiple-choice accuracy in Cloudflare's Decision Index comparison; the model card names suite version 0.2.1 |
| Test unit | Decision items; exact item count and independence unit not established by the reviewed launch table/card |
| Split | Exact sampled cohort, dataset revision and train/calibration/test overlap not established here |
| Reference | Benchmark answer labels; construction and item-level mappings not independently audited |
| Training | Cloudflare post-trained Clef/Clef-Flash; no claim that all compared models share training data, tuning or model-selection conditions |
| Measurement | Percentage accuracy as printed in the launch table; card rounds these results to one decimal. No cross-benchmark aggregate or latency ranking imported |
| Hardware | No hardware-dependent measurement included; exact serving versions for the compared endpoints are not pinned |

| Reported measurement | Value |
| --- | --- |
| Clef When2Call accuracy | 72.37% |
| Clef-Flash When2Call accuracy | 65.58% |
| Jev When2Call accuracy (reported by Cloudflare) | 80.97% |

**Interpretation:** This author-run comparison contains a task where Jev scores above both Clef variants. It supports preserving task-level trade-offs, not a universal winner or a production recommendation.

- The reporter is Cloudflare, author of Clef; the comparison was not reproduced by this repository.
- Pinned model-card revisions identify reviewed text, not the weights or API deployment used for these measurements.
- Missing cohort, failure accounting and uncertainty estimates limit what can be inferred about a new application.
- The announcement's speed and overall-leadership claims are not imported as a common leaderboard or an end-to-end cost guarantee.

**Artifacts and limits:**
- protocol: Launch table and pinned model cards inspected; linked live benchmark application not audited
- raw outputs: Not inspected
- model hash: None
- serving version: None

**Sources:** [Cloudflare Clef launch and evaluation report](https://blog.cloudflare.com/clef-decision-models/); [Clef 27B model card](https://huggingface.co/Cloudflare/clef/blob/2f3de3dd85f379784083b0814d997ab627200f0c/README.md); [Clef-Flash 9B model card](https://huggingface.co/Cloudflare/clef-flash/blob/17f0b0ad64efb65d273590632833508766b2aae6/README.md)

<a id="e07"></a>
## E07 · Strands Decider: instruction sensitivity and experiment-selection limits

**Evidence:** `author_reported` · **Reviewed:** 2026-10-02 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | Question-sensitivity probe on original research v19: keep state and option text/order fixed, replace the real instruction with first-option, last-option, NOT-fit or unrelated-task questions |
| Test unit | Same-answer comparisons paired by original example. Actual recorded denominator unknown; code defaults to at most 200 examples per task, which must not be treated as a verified run count |
| Split | Held-out choice tasks emotion and massive_intent; options restricted to 3–9 and shuffled once per example with original gold neither first nor last |
| Reference | Agreement with the same model's original-question answer, not correctness against the changed instruction or a human safety judgment |
| Training | Original research v19 adapter/pointer-head run; source-code pin does not establish its weight identity or make it identical to the later published adapter/AWS retrain |
| Measurement | Fraction of changed-instruction predictions identical to the original-question prediction, separately by perturbation; repeated variants of one example are not independent samples |
| Hardware | Probe code targets CUDA; exact hardware and command of the archived CSV run not established. No latency comparison imported |

| Reported measurement | Value |
| --- | --- |
| v19 same answer when asked for the first option | 95.00% |
| v19 same answer when asked for the last option | 93.50% |
| v19 same answer with NOT-fit instruction | 94.75% |
| v19 same answer with unrelated-task instruction | 92.25% |

**Interpretation:** The reported probe exposes weak sensitivity to changed instructions in this held-out choice setting. It is not an overall error rate, universal instruction-following result or measurement of the published adapter.

- The source describes roughly 94% answer retention; the four recorded conditions are preserved separately rather than given a fabricated sample denominator.
- The CSV is public, but its referenced raw JSON and item-level predictions were not committed in the inspected checkout; no reproduction was run here.
- Author documentation limits confidence-band evidence to short classification and reports drift on long documents and answer-adequacy inputs; thresholds need application-specific calibration.
- The experiment record explicitly lists v13, v14, v16, v17 and v18 as promoted despite missed preregistered bars. v19 itself met all four predictions; the later v20 did not replace it.
- The v19-seed1 preregistration says the run stopped at step 1,420 with no results. Separate AWS retraining evidence exists, but does not turn this unfinished seed-only comparison into a completed experiment.
- This is an archival v19 record. The 2026-10-05 hobson-v21 release and same-host multi-seed comparison are recorded separately in E08.

**Artifacts and limits:**
- protocol: Pinned probe code and collection script read; no execution
- aggregate results: https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/research/data/probe_heldout_choice.csv
- raw outputs: reports/qsens_hobson-2b-v19.json referenced by CSV but absent from inspected checkout
- seed replicate: https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/research/preregistrations/PREREGISTRATION-v19-seed1.md
- model hash: None

**Sources:** [Strands Decider held-out choice probe results](https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/research/data/probe_heldout_choice.csv); [Strands Decider question-sensitivity protocol](https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/evaluation/question_sensitivity.py); [Strands Decider evaluation and limitations](https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/evaluation/README.md); [Strands Decider experiment record](https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/research/README.md); [Strands Decider original and AWS retrain results](https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/evaluation/results.md); [Strands Decider published v19 adapter card](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v19/blob/bb282d786bc251fd4e3068de3ada9ddbb38127cd/README.md)

<a id="e08"></a>
## E08 · Strands Decider v21: release seed and controlled retrain comparison

**Evidence:** `author_reported` · **Reviewed:** 2026-10-06 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | JevBench public set at window 4096; release v21 is research v21b, seed 5 |
| Test unit | 231 public tasks; six independently trained seeds per recipe in the same-host comparison |
| Split | Public evaluation set, not a new sequestered test; seed selection also uses four named internal/transfer measures |
| Reference | Public JevBench labels through its harness; labels and item-level results not independently audited here |
| Training | Rank-16 LoRA plus pointer head; one epoch, 3738 steps; v21b adds paraphrases and agreement-filtered 4B distillation to v19 |
| Measurement | Released seed tasks correct and Brier; compare recipe means only within one host. Release seed selected by minimum standardized distance from the six-seed mean across five measures |
| Hardware | Release training: p5.48xlarge, 8 H100 GPUs, FAST settings. Text release check: L40S via main. Same-host ablation is separate from this release host |

| Reported measurement | Value |
| --- | --- |
| Released v21 seed JevBench tasks correct | 176/231 (76.19%) |
| Released v21 Brier | 0.323 |
| Same-host v19 recipe mean tasks correct (six seeds) | 172.8 |
| Same-host v21b mean tasks correct (six seeds) | 172.3 |
| Same-host v19 mean Brier | 0.341 |
| Same-host v21b mean Brier | 0.331 |

**Interpretation:** The same-host comparison supports a lower reported mean Brier, not a demonstrated accuracy gain. The released seed score cannot be subtracted from a historical v19 single run to estimate a recipe improvement.

- Author-reported, not reproduced here; raw predictions and uncertainty analyses were not independently replayed.
- The other release host has a v21b mean of 175.0 tasks; host means must not be mixed as if only the recipe changed.
- The release selection rule uses public benchmark and other evaluation measures; this is not independent final-test model selection.
- Historical v19 confidence bands and question-change probes do not establish the current release behavior.

**Artifacts and limits:**
- protocol: Pinned results and v21b config inspected
- raw outputs: Not independently audited
- weight hash: None
- release identity: StrandsAgents/strands-decider-2B-hobson-v21; source-text commit is not a verified weight hash

**Sources:** [Strands Decider v21 release and same-host seed results](https://github.com/strands-labs/strands-decider/blob/3e94e9d84c620ed5a95f1a3310c3decb971e261c/evaluation/results.md); [Strands Decider released v21b recipe](https://github.com/strands-labs/strands-decider/blob/3e94e9d84c620ed5a95f1a3310c3decb971e261c/configs/experiments/v21b.yaml)

<a id="e09"></a>
## E09 · Drex v1.5: public-suite ties and benchmark-training overlap

**Evidence:** `author_reported` · **Reviewed:** 2026-10-11 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | JevBench public closed-option questions; separate from Decision Index 0.3.1 |
| Test unit | 231 public items; no audited item-level pairing |
| Split | Public evaluation; Nace discloses training on official training splits of Index tasks, not unseen-domain zero-shot |
| Reference | Public benchmark labels, not real-world operational outcomes |
| Training | Drex v1.5 task-trained; exact checkpoint and API deployment hashes not established |
| Measurement | Reported hard-answer accuracy; no latency or aggregate Index metric combined here |
| Hardware | Own APIs as reported on product page; hardware and end-to-end cost unverified |

| Reported measurement | Value |
| --- | --- |
| Drex v1.5 public tasks correct | 199/231 (86.15%) |
| Jev 1.13.0 public tasks correct (Nace report) | 201/231 (87.01%) |

**Interpretation:** Two items do not establish a general winner. The newer public Index table declares Drex/Jev/Nimble within its tie band.

- Pinned repository reports Index 0.3.1: 37 public benchmarks, no private tests, 0.9-point tie band. Website 0.2.1: 38 tests, 0.25 band. Do not merge editions.
- Nace reports its own Drex run; other Index rows are copied from the board, not a common independently rerun comparison.
- Public benchmark train/test separation does not establish absence of pretraining overlap or sequestered final-test model selection.
- Local/API equivalence, calibration splits and raw predictions were not audited.

**Artifacts and limits:**
- protocol: Pinned release page and live training FAQ
- raw outputs: Not audited
- weight hash: None
- serving version: None

**Sources:** [Drex v1.5 release and public evaluation](https://github.com/nace-ai/drex-decision-models/blob/5c3d2220713c732a6820c4cdda51c7c38db991f5/models/drex-v1.5/README.md); [Nace Drex training-overlap disclosure](https://www.nace.ai/drex)

<a id="e10"></a>
## E10 · Microsoft-Decision-1: perturbation stability is an author claim

**Evidence:** `author_reported` · **Reviewed:** 2026-10-11 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | Eight request perturbations including option order and paraphrases |
| Test unit | Perturbations; sample denominator and clustering unknown |
| Split | Author says broader 36-benchmark comparison is blind from training; exact perturbation cohort and overlap unverified |
| Reference | Decision agreement under perturbation, not correctness or calibrated risk |
| Training | Microsoft post-trained Qwen3.5-9B; calibration split/recipe undisclosed in inspected sources |
| Measurement | Average decision flip rate reported in launch text; aggregation/weighting not specified |
| Hardware | No latency comparison imported; serving versions and hardware not pinned |

| Reported measurement | Value |
| --- | --- |
| Author-reported average perturbation flip rate | 1.30% |

**Interpretation:** Low reported flip rate does not establish correctness, instruction sensitivity or production-safe acceptance thresholds.

- No raw perturbations/predictions or uncertainty analysis inspected; this is not independent reproduction.
- The 36-benchmark headline and this perturbation probe do not necessarily share the same denominator.
- Official deployment docs still warn about wording/order sensitivity, familiar-task calibration and harmful/benign classification errors.

**Artifacts and limits:**
- protocol: Live launch article; no immutable revision supplied
- raw outputs: Not inspected
- weight hash: None
- serving version: None

**Sources:** [Microsoft-Decision-1 launch, 2026-10-09](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/); [Microsoft Foundry decision API and limitations](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision)

<a id="e11"></a>
## E11 · Strands Qwen3.5 v1: new recipe, soup and missing-image limits

**Evidence:** `author_reported` · **Reviewed:** 2026-10-11 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | JevBench public set and separate missing-image POPE probe |
| Test unit | 231 public JevBench tasks; three training seeds; POPE denominator not established here |
| Split | 4096-token public evaluation; MuSiQue/ContractNLI/BoardgameQA dev splits have train splits in training; HotpotQA held out of training. Some short held-out tasks also serve calibration |
| Reference | Benchmark labels; missing-image experiment removes required evidence rather than creating an answerable task |
| Training | 246678-row balanced Qwen v1 mix, Gemma-4-31B teacher with gold agreement, v19 KL anchor, three-seed soup then calibration; builders absent from main |
| Measurement | Released soup through main versus separate seed/harness scores; do not infer recipe gain from two release runs |
| Hardware | Soup on NVIDIA L4 via main; seeds on 8 A100; paired image comparison on one L4 |

| Reported measurement | Value |
| --- | --- |
| Released Qwen v1 JevBench tasks correct | 180/231 (77.92%) |
| Released Qwen v1 Brier | 0.28 |
| Released Qwen v1 ECE | 0.072 |
| POPE missing-image Qwen v1 ECE | 0.334 |
| POPE missing-image v21 ECE | 0.292 |

**Interpretation:** This is new training and a calibrated soup, not a rename of v21. Reported text results do not imply improved reliability when essential image evidence is missing.

- Training harness scores 181/231; release code scores 180, with one near tie. Neither is silently substituted for the other.
- Public benchmark model selection and absent data builders limit independent reproducibility; weight bytes and raw runs not audited here.
- Author reports missing-image POPE ECE difference +0.042 (paired-bootstrap 95% CI +0.039 to +0.044); confidence does not detect absent images.
- Gemma v1 uses another data mix/teacher and is text-only. E2B pre-fix Decision Index is not a post-fix capability claim.
- E07/E08 preserve v19/v21 evidence; no controlled same-host recipe improvement inferred for v1.

**Artifacts and limits:**
- protocol: https://github.com/strands-labs/strands-decider/blob/0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534/evaluation/results.md
- vision protocol: https://github.com/strands-labs/strands-decider/blob/0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534/docs/vision.md
- raw outputs: Linked author runs not independently audited
- weight hash: None

**Sources:** [Strands Qwen3.5 / Gemma 4 v1 results](https://github.com/strands-labs/strands-decider/blob/0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534/evaluation/results.md); [Strands Qwen v1 missing-image reliability](https://github.com/strands-labs/strands-decider/blob/0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534/docs/vision.md); [Strands dataset/source inventory](https://github.com/strands-labs/strands-decider/blob/0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534/data/sources.md)

