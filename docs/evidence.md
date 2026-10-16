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

<a id="e12"></a>
## E12 · Decision 3.0: internal Index and device timing are bounded author reports

**Evidence:** `author_reported` · **Reviewed:** 2026-10-13 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | d3 text Decision Index 0.3.1 and vision board 0.3.1; separate text/image/10-second-video timing workloads |
| Test unit | Card does not provide all internal/private item counts or raw paired outputs; timing workload counts not fully specified |
| Split | Public, same-skill/new-domain text and public/private vision components; complete private splits inaccessible |
| Reference | Index composite aggregates, not raw classification accuracy; four visual datasets marked approximate rebuild (CharXiv, InfographicVQA, Mind2Web, KIE) |
| Training | Released d3 v3.1.0; public training-overlap/decontamination/calibration artifacts not established |
| Measurement | Internal author evaluation; competitors imported from text board 2026-10-10 and vision board 2026-10-09. Timings are medians per input type, not end-to-end P95 |
| Hardware | One AMD Instinct MI325X, one request at a time; reviewed runtime BF16 backbone / FP32 readout. Full preprocessing/network/queue/retry cost not established |

| Reported measurement | Value |
| --- | --- |
| d3 internal text Index 0.3.1 | 64.7 |
| d3 internal vision Index 0.3.1 | 71.6 |
| d3 text request median (ms) | 55 |
| d3 one-image request median (ms) | 273 |
| d3 10-second-video request median (ms) | 553 |

**Interpretation:** This establishes a reported release benchmark and hardware-specific timing scope, not current first place or a calibrated production risk.

- Live page title is 0.3.2; complete dynamic ranks and exact current models were not audited. No current leader is asserted.
- Imported competitor scores are not a same-hardware, same-day rerun.
- Approximate visual rebuilds and private components prevent treating every row as the identical official protocol.
- Training overlap remains unknown; absence of an audit is not evidence that contamination occurred.

**Artifacts and limits:**
- protocol: Pinned v3.1.0 card at 093cffbaa7be6f5dfe14252ae7e80c396c06dbd9
- raw outputs: Complete internal/private raw run archive not audited
- weight identity: Author-supplied package manifest; binary bytes unverified

**Sources:** [Decision 3.0 d3 v3.1.0 model card](https://huggingface.co/vllm-sr/d3/blob/093cffbaa7be6f5dfe14252ae7e80c396c06dbd9/README.md); [Decision 3.0 code readout and multimodal runtime](https://huggingface.co/vllm-sr/d3/blob/093cffbaa7be6f5dfe14252ae7e80c396c06dbd9/d3_runtime.py); [Decision Index live 0.3.2 title](https://multimodalart-jev-decision-index.static.hf.space/index.html)

<a id="e13"></a>
## E13 · Decision 3.0: the full public kit is not the internal composite or JevBench

**Evidence:** `author_reported` · **Reviewed:** 2026-10-13 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | Official Decision Index 0.3 public-suite kit, scored on each released Decision 3.0 checkpoint |
| Test unit | 140178 public requests per checkpoint; author reports all answered, zero unsupported. Requests are not 140178 independent task families |
| Split | Public suite only; no private/same-skill/new-domain composite imported |
| Reference | Public kit references and chance-corrected aggregation; not raw hard-label accuracy |
| Training | Six v3.1.0 checkpoints; train/test overlap and source-domain exclusion not established publicly |
| Measurement | Card headline public-only index values at the pinned revisions; separate from rounded public columns in internal 0.3.1 tables |
| Hardware | No common hardware or complete serving cost established for comparisons; no speed ranking imported |

| Reported measurement | Value |
| --- | --- |
| d3 public-suite index | 65.45 |
| d3-flash public-suite index | 57.79 |
| d3-mini public-suite index | 54.9 |
| d3-nano public-suite index | 42.22 |
| d3-lite public-suite index | 36.93 |
| d3-edge public-suite index | 28.82 |

**Interpretation:** The six public-kit reports are useful release records under one stated suite; they do not transfer to private composite scores or the 231-task exact-label JevBench.

- The report is from the model team, not an independent reproduction.
- Exact raw outputs, task clustering, uncertainty and failure accounting were not fully audited here.
- Public accessibility does not establish training disjointness.

**Artifacts and limits:**
- protocol: Six pinned cards; official-kit claim reviewed
- raw outputs: No model run or complete output audit here
- evaluated version: Cards say released weights; six repository pins and manifest identities recorded separately

**Sources:** [Decision 3.0 d3 v3.1.0 model card](https://huggingface.co/vllm-sr/d3/blob/093cffbaa7be6f5dfe14252ae7e80c396c06dbd9/README.md); [Decision 3.0 d3-flash v3.1.0 model card](https://huggingface.co/vllm-sr/d3-flash/blob/f6075bff3c0f7d5704e353d0fb2ebf94888d1691/README.md); [Decision 3.0 d3-mini v3.1.0 model card](https://huggingface.co/vllm-sr/d3-mini/blob/0e78bbdbe3cf480ed1461c185c9e0c4fa9258011/README.md); [Decision 3.0 d3-nano v3.1.0 model card](https://huggingface.co/vllm-sr/d3-nano/blob/9d9b937f5f117f78c030ea7ba677c0b3d328ec58/README.md); [Decision 3.0 d3-lite v3.1.0 model card](https://huggingface.co/vllm-sr/d3-lite/blob/3c49f5c0bd48a4b28e29b8ec1f38f56e199f3d61/README.md); [Decision 3.0 d3-edge v3.1.0 model card](https://huggingface.co/vllm-sr/d3-edge/blob/20c745653400d191ecacd99c4eafc0c5900dc15e/README.md)

<a id="e14"></a>
## E14 · Decision 3.0 video: sampled-frame QA does not validate audio or streaming reliability

**Evidence:** `author_reported` · **Reviewed:** 2026-10-13 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | Perception Test validation multiple-choice video QA |
| Test unit | All 19140 questions, reported by the card |
| Split | Validation split; no independent blind final-test run here |
| Reference | Three choices per question, top-1 accuracy; chance 1/3 |
| Training | d3 v3.1.0; overlap with training data unknown |
| Measurement | Default 2 fps, minimum 4 / maximum 32 frames spread across the video, up to about 0.2 MP per frame; shared frames visible to each question |
| Hardware | Accuracy statement; video median in E12 is a separate MI325X workload |

| Reported measurement | Value |
| --- | --- |
| d3 Perception Test validation top-1 accuracy | 77.40% |

**Interpretation:** This is an author-reported sampled-visual QA result; it does not validate audio understanding, live alerts or missed short events.

- Sparse sampling can omit brief events; long videos still use at most 32 sampled frames.
- Multiple questions about shared videos require grouped uncertainty, not an independent-question assumption.
- No audio evaluation, continuous-stream P95 or real-world monitoring failure rate was established.

**Artifacts and limits:**
- protocol: Pinned card and video sampling code read
- raw outputs: Not independently inspected
- weights: No download or run here

**Sources:** [Decision 3.0 d3 v3.1.0 model card](https://huggingface.co/vllm-sr/d3/blob/093cffbaa7be6f5dfe14252ae7e80c396c06dbd9/README.md); [Decision 3.0 code readout and multimodal runtime](https://huggingface.co/vllm-sr/d3/blob/093cffbaa7be6f5dfe14252ae7e80c396c06dbd9/d3_runtime.py)

<a id="e15"></a>
## E15 · Decision 3.0 on Apple: conversion and public-harness evidence

**Evidence:** `author_reported` · **Reviewed:** 2026-10-13 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | Core ML lite/nano/mini versus upstream PyTorch; separate JevBench and typed-decisions tasks |
| Test unit | JevBench 231 public tasks; typed-decisions TEST 2000 questions |
| Split | Public JevBench suite and typed-decisions TEST; not official sealed Decision Index ranking |
| Reference | Exact-label JevBench accuracy; typed-decisions gold labels with multiple annotators and disagreement |
| Training | Converted upstream releases; full evaluated upstream/package hashes for the article table not independently tied to binary bytes here |
| Measurement | Unchanged System One adapter/scorer reported; one request at a time, local HTTP round trip included. Median latency, not P95. Displayed percentages are rounded reports |
| Hardware | MacBook Pro M5 Pro 24 GB GPU; PyTorch bf16 reference DeltaNet path versus Core ML text fp16 compute/int8 weights, FP32 vision/readout. These optimizations and the Mac reference backend are part of the comparison |

| Reported measurement | Value |
| --- | --- |
| d3-lite JevBench PyTorch accuracy | 73.20% |
| d3-lite JevBench Core ML accuracy | 74.00% |
| d3-lite typed-decisions PyTorch accuracy | 51.60% |
| d3-lite typed-decisions Core ML accuracy | 51.60% |
| d3-lite JevBench median PyTorch request (ms) | 204 |
| d3-lite JevBench median Core ML request (ms) | 53 |
| d3-nano JevBench PyTorch accuracy | 75.30% |
| d3-nano JevBench Core ML accuracy | 75.80% |
| d3-nano typed-decisions PyTorch accuracy | 62.70% |
| d3-nano typed-decisions Core ML accuracy | 62.70% |
| d3-nano JevBench median PyTorch request (ms) | 173 |
| d3-nano JevBench median Core ML request (ms) | 69 |
| d3-mini JevBench PyTorch accuracy | 81.80% |
| d3-mini JevBench Core ML accuracy | 81.80% |
| d3-mini typed-decisions PyTorch accuracy | 73.60% |
| d3-mini typed-decisions Core ML accuracy | 73.90% |
| d3-mini JevBench median PyTorch request (ms) | 438 |
| d3-mini JevBench median Core ML request (ms) | 169 |

**Interpretation:** A concrete Apple deployment candidate with converter-reported quality and latency; the same-device speedup does not predict CUDA speed or production correctness.

- Alex Weng / Fluid Inference authored the conversion and received early model access; label retained as author_reported, not independent.
- Small parity suites can contain near-tie flips; exact universal equivalence is not established.
- 37 JevBench tasks exceed 1536 tokens, maximum 3970; the article reports a 4096-token graph. Inspect each artifact and reject overlength inputs.
- Article/Hub/Swift snapshots differ in names, sizes and supported paths; later flash/Mario prose is not evidence that the pinned lite/nano/mini Hub package contains flash.
- No cold-start P95, concurrent-load benchmark, full energy/cost accounting or model reproduction here.

**Artifacts and limits:**
- protocol: October 11 live article plus fixed Core ML/Swift source revisions
- raw outputs: Converter-run results reviewed, not rerun
- source revision: d278e17df85e39e8c21bb64a467da81c39576fcd
- converted package revision: 62b6a996e15342bdd3d608030d8f445f11a52367

**Sources:** [Decision 3.0 on Apple Silicon](https://vllm-sr.ai/blog/decision-3-0-on-apple-silicon/); [Decision 3.0 Core ML conversion packages](https://huggingface.co/FluidInference/d3-coreml/blob/62b6a996e15342bdd3d608030d8f445f11a52367/README.md); [FluidUse native Swift/Core ML runtime](https://github.com/FluidInference/FluidUse/blob/d278e17df85e39e8c21bb64a467da81c39576fcd/README.md)

<a id="e16"></a>
## E16 · Decision 3.0 PR triage: throughput and real-label agreement are different tests

**Evidence:** `author_reported` · **Reviewed:** 2026-10-13 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | PR workgroup (seven choices) and change-type triage |
| Test unit | 1000 sample PRs for d3-lite throughput; separate real labeled PR sets for d3-mini: 168 workgroups / 182 types |
| Split | Business-label sample provenance and source/time separation not fully specified |
| Reference | Real vLLM-SR maintainer labels for agreement; 1000-sample throughput has no imported correctness denominator |
| Training | Public model family; use of PR-domain training data not established |
| Measurement | Title, start of description and changed files; two decisions per sample PR. Real-label agreement is separate from timed demo |
| Hardware | M5 Pro local Core ML deployment, as reported by converter article; complete queue/review/correction cost absent |

| Reported measurement | Value |
| --- | --- |
| d3-lite sample PR throughput time (seconds / PR, two questions) | 0.12 |
| d3-mini workgroup label agreement | 134/168 (79.76%) |
| d3-mini change-type label agreement | 153/182 (84.07%) |

**Interpretation:** The deployment demo motivates a shadow triage test; it cannot turn throughput into an accuracy or workflow-success claim.

- The timing and label-agreement tests use different model sizes and populations.
- Maintainer label agreement is a useful reference but not independently observed downstream business success.
- No paired uncertainty or critical misrouting/error-cost analysis supplied.

**Artifacts and limits:**
- protocol: Article PR triage section
- raw outputs: PR IDs, predictions and independently adjudicated outcomes not fully audited
- tested binary: Exact conversion/evaluated weight hashes not established for these demos

**Sources:** [Decision 3.0 on Apple Silicon](https://vllm-sr.ai/blog/decision-3-0-on-apple-silicon/)

<a id="e17"></a>
## E17 · WebMCP application test: small differences and preprocessing errors

**Evidence:** `third_party_reported` · **Reviewed:** 2026-10-13 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | Five Schema Usage page actions with month/type/bucket details; off-topic inputs should cause no action |
| Test unit | 75 frozen test questions, roughly half English / half Spanish; 75 development and 20 original cases separately described |
| Split | Evaluator-authored labels; Nano adjusted variant chosen after looking at test, so that row is selection-biased |
| Reference | Full action and all required details correct; shared extraction/pre-routing rules. Three shared failures bypassed the compared models |
| Training | Cloud systems treated as untuned for this test; checkpoint/serving revisions not frozen for all compared models |
| Measurement | Baseline rule-on test counts below. Removing the term rule is a separate post-test intervention. Three common option permutations and paired McNemar comparisons reported |
| Hardware | Local d3 Python on M5 Pro; Microsoft via decisions-api.dev (report says OpenRouter upstream); Jev via jev-ai.pro and decisions-api.dev. No direct official TypeSafe timing or cost comparison established |

| Reported measurement | Value |
| --- | --- |
| Microsoft-Decision-1 rule-on full-call correctness | 71/75 (94.67%) |
| d3-flash rule-on full-call correctness | 70/75 (93.33%) |
| d3-mini rule-on full-call correctness (technical discussion) | 70/75 (93.33%) |
| Jev rule-on full-call correctness | 69/75 (92.00%) |

**Interpretation:** A useful application-level failure analysis, not a clear statistical winner among Microsoft, d3 flash/mini and Jev.

- No pooled ranking with Index, JevBench or typed-decisions is justified.
- Three errors came from a term-matching pre-rule: the model never saw those questions. Test the rule layer independently.
- Post-test Nano selection and rule-removal results cannot be called untouched hold-out improvements.
- jev-ai.pro is an independent platform; its upstream connection is self-reported. Microsoft was tested only through an intermediary. Reported latency/pricing belongs to those paths.
- Missing immutable evaluated versions and a complete output audit limit reproduction and generalization.

**Artifacts and limits:**
- protocol: Original report and technical appendix
- raw outputs: Report describes stored probabilities; complete frozen output/code archive not audited here
- version: Model names reported; exact evaluated weight/API revisions unknown

**Sources:** [Natzir Turrado: Schema Usage / WebMCP application test](https://natzir.com/posicionamiento-buscadores/modelos-decision-en-webmcp/); [Jev AI independent platform disclosure](https://jev-ai.pro/about)

<a id="e18"></a>
## E18 · Intern-Decision: exact-distribution calibration pilot, not hard-label accuracy

**Evidence:** `author_reported` · **Reviewed:** 2026-10-13 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | Known-distribution-pilot-v1: predict probabilities of random outcomes under stated mechanisms |
| Test unit | 96 cases, six categories, 24 families and 48 paired settings; all settings report 96 valid predictions |
| Split | Evaluation-only pilot; author says no fit/selection on its references. 4B temperature fitted separately; private calibration/validation records not released |
| Reference | Exact rational outcome distributions, separate from inference inputs; not sampled hard labels |
| Training | Final Intern-Decision-4B; XTuner backend fixed T=1.992418; Jev 1.13.0 comparator. Evaluated binary/hash not independently authenticated against current HF weights |
| Measurement | Expected multiclass Brier (including irreducible randomness); expected ECE with 10 equal-width bins, returned confidence or max(P) fallback. Pooled ECE recomputed, not mean category ECE |
| Hardware | Probability metrics only; RTX4090 latency table and HF/Core ML timings are different protocols |

| Reported measurement | Value |
| --- | --- |
| 4B uncalibrated expected Brier | 0.628 |
| 4B calibrated expected Brier | 0.55 |
| 4B uncalibrated expected ECE | 21.30% |
| 4B calibrated expected ECE | 8.90% |
| Jev 1.13.0 expected Brier on this pilot | 0.595 |
| Jev 1.13.0 expected ECE on this pilot | 13.00% |

**Interpretation:** The within-model calibration contrast is useful on these exact-reference problems; it establishes neither an overall model winner nor production risk control.

- Author-run small diagnostic; paired variants are not 96 independent observations.
- NLL-fitting records are private and full training-overlap audit unavailable.
- Backend-specific calibration must be matched to the actual inference path; HF and XTuner numerics need separate validation.
- Exact-distribution ECE/Brier must not be merged with hard-label suite scores or interpreted as future realized-outcome accuracy.

**Artifacts and limits:**
- protocol: Pinned repository, pilot documentation and public reference/scorer paths read
- raw outputs: Complete replay not performed here
- temperature: Author-provided preset; private fitting/validation records unavailable

**Sources:** [Intern-Decision architecture and release scope](https://github.com/internlm/Intern-Decision/blob/3572c8a68b5df5dafe02d0e093989ba8ec0183bc/README.md); [Intern-Decision known-distribution calibration pilot](https://github.com/internlm/Intern-Decision/blob/3572c8a68b5df5dafe02d0e093989ba8ec0183bc/docs/CALIBRATION_BENCHMARK.md); [Intern-Decision evaluation protocol](https://github.com/internlm/Intern-Decision/blob/3572c8a68b5df5dafe02d0e093989ba8ec0183bc/docs/EVALUATION.md); [Intern-Decision-4B model card](https://huggingface.co/internlm/Intern-Decision-4B/blob/0e5e6aa7d6d750e2b1504ba11a8136cb58aeb3cd/README.md)

<a id="e19"></a>
## E19 · Verdict deployment: evaluator calibration is not shipped serving calibration

**Evidence:** `third_party_reported` · **Reviewed:** 2026-10-13 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | Verdict Core ML on author-held-out Banking77 / CLINC-OOS protocol, then actual answer serving path |
| Test unit | 1000 test requests; 500 calibration separate; full report also includes 1000 challenge-slice records |
| Split | Author public cal/test files at pinned Verdict commit; converter refit single T on calibration only |
| Reference | Same held-out labels; evaluator raw rendering differs from hypothesis-style answer renderer and abstention placement |
| Training | Pinned trained 151M checkpoint; conversion reporter states identity with author checkpoint, not locally verified here |
| Measurement | Compare author-protocol raw logits with separately fitted single T against shipped answer() per-K calibration; same answer logits with T=1 is an ablation |
| Hardware | FluidUse Swift Core ML FP16 on Apple M5 Pro; no pooled latency claim with author WASM proxy |

| Reported measurement | Value |
| --- | --- |
| Core ML author-protocol top-1 accuracy | 95.00% |
| Core ML author-protocol ECE | 3.38% |
| Shipped answer() top-1 accuracy | 93.10% |
| Shipped answer() ECE | 21.20% |
| Same answer logits with T=1 ECE | 1.90% |
| Shipped answer() NLL | 0.395 |
| Shipped answer() Brier | 0.167 |
| Raw-logit reference decision agreement | 998/1000 (99.80%) |

**Interpretation:** Converter-reported findings show why deployment acceptance must test the actual renderer and calibrator, even when ported logits are close.

- Independent of the upstream model authors but reported by the port maintainer; not a detached audit, and not reproduced_here.
- The open-domain shipped calibrator is under-confident on this in-domain test; this does not establish that globally disabling calibration is preferable.
- Raw-evaluator 95% is not the answer-path accuracy; rendering and calibrator differences must remain explicit.
- Converter LUT8 failed its agreement gate; FP16 parity does not certify quantized abstention behavior.

**Artifacts and limits:**
- protocol: Fixed FluidUse OfficialBenchmarks.md; author code and calibrator text independently read
- raw outputs: Reporter describes saved artifacts and row agreement; complete archive not rerun/audited here
- upstream revision: 30f15564821626ca5c1ad5b2638c4eb7078787dd
- model repository revision: 8af2496eb63c7fa66d7d234e1f62629380030eb4
- conversion revision: 835208c443699f1f95c4bed1b177dc916300cffe

**Sources:** [FluidUse official-harness and application-path reports](https://github.com/FluidInference/FluidUse/blob/d278e17df85e39e8c21bb64a467da81c39576fcd/Documentation/OfficialBenchmarks.md); [Verdict typed serving renderer and calibration path](https://github.com/Heman10x-NGU/Verdict-open-jev/blob/30f15564821626ca5c1ad5b2638c4eb7078787dd/core/engine_encoder.py); [Verdict shipped per-K calibration artifact](https://huggingface.co/heman10x/rlcd-modernbert-151m/blob/8af2496eb63c7fa66d7d234e1f62629380030eb4/calibrator.json); [Verdict Core ML conversion and rejected quantization](https://huggingface.co/FluidInference/verdict-coreml/blob/835208c443699f1f95c4bed1b177dc916300cffe/README.md)

<a id="e20"></a>
## E20 · Verdict abstention: preserve hard-negative and synonym failures

**Evidence:** `author_reported` · **Reviewed:** 2026-10-13 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | Missing-correct-option abstention, standard versus hard-negative K=9 / synonym / combined conditions |
| Test unit | 200 cases per condition; paired perturbations, not 800 independent cases |
| Split | Author diagnostic report; exact independence from training/calibration not fully audited |
| Reference | Correct action is abstain because the valid intent is absent from the candidate menu |
| Training | Verdict v2 reported model; evaluated tensor hash not independently tied to current HF binary here |
| Measurement | Abstention recall; raw JSON reports true abstentions and false negatives, zero false positives in these all-abstain slices |
| Hardware | Quality failure analysis only; no hardware-performance conclusion |

| Reported measurement | Value |
| --- | --- |
| Standard missing-option abstention recall | 151/200 (75.50%) |
| Hard-negative K=9 abstention recall | 36/200 (18.00%) |
| Synonym phrasing abstention recall | 47/200 (23.50%) |
| Combined hard negatives and synonym abstention recall | 20/200 (10.00%) |

**Interpretation:** An explicit abstention candidate can fail under plausible schema perturbations; production acceptance needs more than a high distant-OOS score.

- Recall on an all-abstain slice does not measure precision on realistic mixed traffic.
- Variants share base examples; report family-aware paired uncertainty.
- Preserve this negative result separately from author marketing about guaranteed calibration/abstention.

**Artifacts and limits:**
- protocol: Pinned raw exp_e5 report read
- raw outputs: Aggregate counts public; per-example inference not replayed here
- upstream revision: 30f15564821626ca5c1ad5b2638c4eb7078787dd

**Sources:** [Verdict / OpenJev mechanism and negative findings](https://github.com/Heman10x-NGU/Verdict-open-jev/blob/30f15564821626ca5c1ad5b2638c4eb7078787dd/README.md); [Verdict raw abstention-generalization report](https://github.com/Heman10x-NGU/Verdict-open-jev/blob/30f15564821626ca5c1ad5b2638c4eb7078787dd/reports/v2/exp_e5_abstention_generalization.json)

<a id="e21"></a>
## E21 · Decision 3.0 Index 0.3.2: scoring changes with unchanged weight identities

**Evidence:** `author_reported` · **Reviewed:** 2026-10-15 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | Text and vision Full composites, separate board protocols; release claims corroborated against published aggregate JSON |
| Test unit | Oct 14-generated text: 166 entries; vision: 34 entrants. Entry counts are not evaluation sample sizes |
| Split | Public/same-skill/new-domain text panels; public/private vision panels. Hidden examples/raw runs not audited |
| Reference | Text weights 0.2/0.5/0.3 with private-scale equating; vision public/private 0.5/0.5. Composites, not raw accuracy |
| Training | Six v3.1.0 weight/readout Git/LFS and manifest identities unchanged since Oct 13 pins; temperature remains 1.0. No tensor bytes verified |
| Measurement | Retrieved/rechecked Oct 15. Text tie band 0.9: d3 66.26 and linne-oak 65.61 share rank group 1; card entry counts reflect an older snapshot |
| Hardware | Aggregate source review; serving timings are E22/E23 |

| Reported measurement | Value |
| --- | --- |
| d3 displayed text Full index 0.3.2 | 66.26 |
| d3 displayed vision Full index 0.3.2 | 71.26 |
| d3-flash displayed text Full index 0.3.2 | 55.79 |
| d3-flash displayed vision Full index 0.3.2 | 66.89 |
| d3-mini displayed text Full index 0.3.2 | 52.61 |
| d3-mini displayed vision Full index 0.3.2 | 63.16 |
| d3-nano displayed text Full index 0.3.2 | 38.86 |
| d3-nano displayed vision Full index 0.3.2 | 54.67 |
| d3-lite displayed text Full index 0.3.2 | 32.33 |
| d3-lite displayed vision Full index 0.3.2 | 42.11 |
| d3-edge displayed text Full index 0.3.2 | 20.24 |
| d3-edge displayed vision Full index 0.3.2 | 31.71 |

**Interpretation:** A new evaluation snapshot does not establish newly trained weights or an uncontested text winner.

- Changelog describes omitted same-skill sets and public-suite corrections. Subtracting 0.3.1 from 0.3.2 is not a controlled model-improvement experiment.
- Published release/board aggregates are not an independent rerun by this repository; hidden-item and calibration audits remain incomplete.
- Training overlap/decontamination remains unknown; approximate visual rebuilds and private/public boundaries remain relevant.
- The tie band is a board convention, not a production confidence interval or risk guarantee.

**Artifacts and limits:**
- text generated utc: 2026-10-14T09:16:12Z
- text sha256: e51e388fd9f7be8d82662bc349c1971147ffc64be2072568aca96820941b4133
- vision generated utc: 2026-10-14T09:16:14Z
- vision sha256: 66c74cfaa91f899cafc0fe2b639feca7febd611d9c7f5da42435fafc2e0a36f6
- raw outputs: Aggregate JSON/metadata only; no benchmark run here

**Sources:** [d3 October 15 card and identity review](https://huggingface.co/vllm-sr/d3/blob/225be8b1e2270becab69c5fe05b26f99cbbdd66b/README.md); [d3-flash October 15 card and identity review](https://huggingface.co/vllm-sr/d3-flash/blob/8b35c853b90e777595ec36bacae820fe08ea077a/README.md); [d3-mini October 15 card and identity review](https://huggingface.co/vllm-sr/d3-mini/blob/97dd054df4b3e0b3beb6af23ab8c82b7c0052e0e/README.md); [d3-nano October 15 card and identity review](https://huggingface.co/vllm-sr/d3-nano/blob/aeb70d4dd53ed25b855c3b0a66394b8fe265db7f/README.md); [d3-lite October 15 card and identity review](https://huggingface.co/vllm-sr/d3-lite/blob/9c10703193afc7c7d28c88201c0364bfbbf58320/README.md); [d3-edge October 15 card and identity review](https://huggingface.co/vllm-sr/d3-edge/blob/cab71e6ad3461b8086d51ddb572c656babd63b0b/README.md); [Decision Index 0.3.2 text aggregate snapshot](https://multimodalart-jev-decision-index.static.hf.space/data/v03.json); [Decision Index 0.3.2 vision aggregate snapshot](https://multimodalart-jev-decision-index.static.hf.space/data/vision.json); [Decision Index 0.3.2 scoring-change description](https://multimodalart-jev-decision-index.static.hf.space/index.html)

<a id="e22"></a>
## E22 · Decision 3.0 serving: batching gains have load and overload boundaries

**Evidence:** `author_reported` · **Reviewed:** 2026-10-15 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | AutoModel in-process, package HTTP server and vLLM-SR Engine; Engine batching versus former one-request-per-forward mode |
| Test unit | Oct 13: about 330-token ticket, text with 1/16 questions, new 1.6-MP images, new 10-second 1080p video and 32k text; 3 warmups then up to 20 calls; load levels 15–60 seconds |
| Split | Runtime benchmark, not unseen-domain quality. Separate public-suite drift sample: 4000 requests / 29339 questions |
| Reference | Same model/GPU; Engine source optimizations newer than published images. AutoModel back-to-back versus closed-loop Engine clients up to 64 |
| Training | No weight/calibrator change established. Batching changes numerical execution: 14 of 29339 decisions differ, described as near-ties |
| Measurement | 27 one-question-text requests/s at p99 <1 s; 29 at saturation is another operating point. Eight-question images fail that p99 target at every tested load. Engine admits 32 in-flight, rejects excess with HTTP 503 |
| Hardware | One MI325X per replica, each side alone; ROCm 7.2/PyTorch 2.12, AutoModel Transformers 5.17.0. Startup: local weights, empty kernel caches; CLI image pull excluded |

| Reported measurement | Value |
| --- | --- |
| AutoModel warm text-question median (ms) | 54.4 |
| AutoModel warm image-question median (ms) | 290 |
| AutoModel warm ten-second-video median (ms) | 500 |
| Engine batching text-question median (ms) | 57.2 |
| AutoModel one-question text rate (requests/s) | 18.4 |
| Engine batching text rate with p99 under 1 s (requests/s) | 27 |
| Engine text saturation rate (requests/s) | 29 |
| Batched decisions changed | 14/29339 (0.05%) |
| Engine batching startup, local weights (s) | 20.4 |
| AutoModel startup, local weights (s) | 38.4 |

**Interpretation:** Batching improves reported serving throughput while adding latency to a single short request; no hardware-independent speedup follows.

- SR Engine differs from native vLLM in E23; do not merge their startup or throughput tables.
- Byte parity concerned former unbatched mode with matched kernel settings; default batching has near-tie changes.
- Measured Engine commit/image is not fully pinned. Startup excludes downloads/pulls; overload, retries and full costs are incomplete.
- Tiny reported gold-accuracy drift under batching is not a demonstrated training improvement.

**Artifacts and limits:**
- protocol: Pinned Oct 15 card, Serving performance section
- run date: 2026-10-13
- raw outputs: Author report only; no load run/failure-log audit here

**Sources:** [d3 October 15 card and identity review](https://huggingface.co/vllm-sr/d3/blob/225be8b1e2270becab69c5fe05b26f99cbbdd66b/README.md)

<a id="e23"></a>
## E23 · Native vLLM D3: merged source and bounded parity/concurrency evidence

**Evidence:** `author_reported` · **Reviewed:** 2026-10-15 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | Native D3Strategy classify/pooling on /v1/systemone; one prompt/classify read per question with shared media features |
| Test unit | PR: 416 questions per d3/mini/edge. Mixed throughput: 40% one-question text, 20% four-question text, 10% JSON, 10% 40-option choice, 15% new image, 5% new video |
| Split | Parity fixtures and serving loads, not unseen-domain effectiveness. Flash/nano/lite, CUDA, tensor parallelism and LoRA explicitly unmeasured in PR |
| Reference | PR d3@fc2d74bd, mini@6d8971f4, edge@fe71f8e1 versus checkpoint runtimes. Separate Oct 15 MI300X nightly check in card changes one d3 decision |
| Training | Unchanged checkpoints, FP32 readout. Merged 89cab550862e4b7f08d70c19682121362d7dd0c5 at 2026-10-14T17:10:56Z; latest official v0.31.0 predates support |
| Measurement | PR load: 8 s warmup, 30 s per closed-loop level. Rate below compares native vLLM with HTTP checkpoint server, not in-process AutoModel or SR Engine. Confidence/usage/error semantics differ; optional permutation_average absent |
| Hardware | PR one MI325X per side, ROCm nightly 5555a2d8 + PR tree, PyTorch 2.13/ROCm 7.2; reference Transformers 5.17.0/FLA 0.5.2. Card separately tests MI300X Oct 15 nightly 0.32.0rc1.dev190+g3f1bcfd82 |

| Reported measurement | Value |
| --- | --- |
| PR d3 decisions changed | 0/416 (0.00%) |
| PR d3-mini decisions changed | 1/416 (0.24%) |
| PR d3-edge decisions changed | 2/416 (0.48%) |
| Card Oct 15 MI300X d3 decisions matched | 415/416 (99.76%) |
| PR d3 checkpoint HTTP server, 8 clients (requests/s) | 6.1 |
| PR d3 native vLLM, 8 clients (requests/s) | 8.6 |
| PR d3 checkpoint HTTP server, 64 clients (requests/s) | 4.6 |
| PR d3 native vLLM, 64 clients (requests/s) | 8.5 |
| PR native d3 cold startup, local weights (s) | 214.5 |
| PR AutoModel cold startup, local weights (s) | 39.9 |

**Interpretation:** Native support is merged source with author-run measurements, not a stable-release or universal-parity guarantee.

- Noncausal attention disables prefix caching/chunked prefill; one HTTP request is not one shared text encoding.
- Up to 64 questions/255 choice options; top-level instructions and invalid/too-long questions return HTTP 400, unlike package per-question errors.
- Device/build checks differ at near-ties. The CUDA install command is not NVIDIA validation.
- Default 0.92 GPU utilization reserves HBM; reported reservation is not weight size. New-video decoding queues under load.

**Artifacts and limits:**
- merge commit: 89cab550862e4b7f08d70c19682121362d7dd0c5
- pr body sha256: 0ae4020db2a05e5caa67309f962810bed64cb36b9f67c49b740080acf75f12a5
- raw outputs: Author tables/tests read; no model execution
- release check: Latest official release rechecked Oct 15: v0.31.0

**Sources:** [Native vLLM Decision 3.0 integration and author tests](https://github.com/vllm-project/vllm/pull/61565); [vLLM structured decisions at the D3 merge](https://github.com/vllm-project/vllm/blob/89cab550862e4b7f08d70c19682121362d7dd0c5/docs/models/structured_decisions_models.md); [vLLM D3 classification model implementation](https://github.com/vllm-project/vllm/blob/89cab550862e4b7f08d70c19682121362d7dd0c5/vllm/model_executor/models/d3.py); [d3 October 15 card and identity review](https://huggingface.co/vllm-sr/d3/blob/225be8b1e2270becab69c5fe05b26f99cbbdd66b/README.md)

<a id="e24"></a>
## E24 · Financial earnings: conditional comparison labels and unequal text windows

**Evidence:** `third_party_reported` · **Reviewed:** 2026-10-15 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | 2023 release revenue/EPS year-on-year direction and net loss, separate binary tasks |
| Test unit | Selected revenue 802/EPS 833; unfiltered revenue 887/EPS 948; net loss 1044. Five submitted releases failed token limit |
| Split | Supervised classifiers company-grouped five-fold; historical, not forward-time/after-training-cutoff. TF-IDF vocabulary/IDF fit on full corpus before label splits |
| Reference | Later matched XBRL reports provide labels; retrospective magnitude-string screen selects comparisons. No complete corrected answer key |
| Training | Reported Jev 1.13.0 without task examples; TF-IDF LightGBM and fine-tuned ModernBERT/SEC-BERT use labeled releases with fixed settings |
| Measurement | Accuracy conditional on each population. Jev sees full text, encoders about first 4000 tokens. No extraction-and-arithmetic baseline |
| Hardware | Encoders trained on one RTX 3090; hosted Jev source review, no speed comparison |

| Reported measurement | Value |
| --- | --- |
| Jev selected revenue accuracy | 98.50% |
| LightGBM selected revenue accuracy | 72.60% |
| Jev selected EPS accuracy | 99.00% |
| LightGBM selected EPS accuracy | 63.60% |
| Jev unfiltered revenue accuracy | 95.40% |
| Jev unfiltered EPS accuracy | 94.90% |
| Jev net-loss accuracy | 97.30% |

**Interpretation:** Jev leads the tested document classifiers on these specified comparisons; conditional screening and label defects prevent a universal accuracy claim.

- TypeSafe supplied API access; external evaluator report, not reproduced here.
- XBRL is later scoring evidence, not model input. Hindsight availability screening is not a deployable eligibility rule.
- Disagreement-only label audit does not establish 100% correctness; binary options force answers for absent comparisons.
- Unequal windows, untuned training, full-corpus preprocessing and historical exposure limit architecture-level conclusions.

**Artifacts and limits:**
- protocol: Original article and appendix
- raw outputs: Complete frozen code/predictions not audited
- model revision: Report attribution; original compact files lack version fields

**Sources:** [Stefan Jansen: Testing Jev on Financial Documents](https://insights.ml4trading.io/p/testing-jev-on-financial-documents)

<a id="e25"></a>
## E25 · Financial 8-K categories: supervision and post-hoc selection

**Evidence:** `third_party_reported` · **Reviewed:** 2026-10-15 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | Reproduce filer-selected 8-K category among 11 classes, with item headings removed |
| Test unit | 3006 usable Jan–Sep 2023 filings; five failed documents /15 question rows excluded |
| Split | Company-grouped classifier folds, TF-IDF full-corpus preprocessing; no forward-time test |
| Reference | Company filing category, including overlapping 7.01/8.01 conventions; not objective event semantics alone |
| Training | Jev without task examples; logistic/LightGBM and encoders supervised on public categories |
| Measurement | Same Jev-answered feed; Jev averages three wordings. Nine-class analysis and 99%-precision cutoffs chosen after outcomes |
| Hardware | No controlled hardware/speed comparison |

| Reported measurement | Value |
| --- | --- |
| Jev full 11-class accuracy | 79.30% |
| TF-IDF logistic accuracy | 89.40% |
| TF-IDF LightGBM accuracy | 91.30% |
| Jev post-hoc coverage at 99% observed precision | 47.90% |
| ModernBERT post-hoc coverage at 99% observed precision | 55.50% |

**Interpretation:** Supervision helps reproduce these public reporting labels; post-hoc subsets/thresholds do not establish prospective reliability.

- Vendor API access disclosed; no independent replay here.
- Nine-class analysis conditions on true category, unavailable as a live filter. Reporting conventions may differ from semantic intent.
- Cutoffs used evaluated outcomes, not frozen calibration data; observed 99% precision is not a production guarantee.
- Supervised versus zero-shot setup does not prove trees always outperform a decision architecture.

**Artifacts and limits:**
- protocol: Article task/split appendix
- raw outputs: Some TF-IDF per-document predictions not retained according to source
- model revision: Reported Jev 1.13.0; immutable serving version unavailable

**Sources:** [Stefan Jansen: Testing Jev on Financial Documents](https://insights.ml4trading.io/p/testing-jev-on-financial-documents)

<a id="e26"></a>
## E26 · SEC follow-up: 90-day forecasting differs from textual completeness

**Evidence:** `third_party_reported` · **Reviewed:** 2026-10-15 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | Predict substantive SEC follow-up within 90 days after a response |
| Test unit | 2261 unique 2022–2023 letters, 925 positives; closing letters/silence negative, incomplete observation windows excluded |
| Split | Text classifiers train on 8875 letters outside recorded test CIKs; 86 co-registrant IDs still overlap. Grouping is not chronological isolation |
| Reference | Observed subsequent correspondence. Questions omit 90-day horizon; fully-resolves wording targets a different judgment |
| Training | Reported Jev 1.13.0 zero-shot; supervised ModernBERT/SEC-BERT. Vendor-suggested fund-form hint added after seeing same-letter results |
| Measurement | Direct accuracy/AUC/Brier below; augmented prompt is a separate post-hoc arm, not untouched validation |
| Hardware | No latency or investment-performance comparison |

| Reported measurement | Value |
| --- | --- |
| Jev direct-question accuracy | 67.00% |
| Jev direct-question AUC | 71.30% |
| Jev direct-question Brier | 0.2204 |
| ModernBERT accuracy | 80.60% |
| ModernBERT AUC | 89.00% |
| ModernBERT Brier | 0.1346 |
| Jev post-hoc hint AUC | 83.10% |
| Jev post-hoc hint Brier | 0.1878 |

**Interpretation:** Trained classifiers forecast this labeled process better; a same-sample domain hint needs new-letter validation, and semantic completeness is another target.

- API support and prompt suggestion disclosed; source review is not our reproduction.
- Company sequencing/regex labels may mislink reviews. Residual issuer overlap, TF-IDF preprocessing and historical exposure remain limitations.
- Form-plus-length comparator uses another split, so is not imported as equally company-isolated.
- Lower Brier alone does not prove calibration; no financial-return guarantee follows.

**Artifacts and limits:**
- protocol: Original methods appendix and question wording
- raw outputs: Full raw prediction audit absent
- version: Report attributes Sep 21–Oct 7 runs to Jev 1.13.0 using sampled recheck

**Sources:** [Stefan Jansen: Testing Jev on Financial Documents](https://insights.ml4trading.io/p/testing-jev-on-financial-documents)

<a id="e27"></a>
## E27 · Semantic features: wine-score prediction with development-only discovery

**Evidence:** `author_reported` · **Reviewed:** 2026-10-15 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | Predict critic score from wine tasting-note text, not finance or visual intent |
| Test unit | 2000 sampled notes, exact duplicate text removed; 1200 development / 800 held-out, seed 0 |
| Split | Proposal/selection uses development only, 5-fold CV repeated 3 times; five arms and round diagnostics evaluated on held-out afterward |
| Reference | Critic score 80–100; cached sample 80–98. Public dataset revision 90eb39f35fc64e556fc17f06d4137a4a69ec3297 |
| Training | Aug 3 cached run: fixed Jev 1.12 features, claude-sonnet-5 proposer, CatBoost 400 trees / depth 4 / rate 0.05. No Jev parameter training |
| Measurement | Five rounds, 38 questions (29 score + 9 noul) become 67 columns; RMSE in critic points. Paired bootstrap conditional on this split; discovery-seed uncertainty unmeasured |
| Hardware | Author cached/API workflow, not full-cost benchmark; no API calls here |

| Reported measurement | Value |
| --- | --- |
| Mean baseline RMSE | 3.088 |
| Same CatBoost word-count RMSE | 2.466 |
| Direct Jev score with dev-fitted offset RMSE | 2.145 |
| First-round 18-question RMSE | 1.869 |
| Fifth-round 38-question RMSE | 1.772 |
| Round 5 minus round 1 RMSE | -0.097 |

**Interpretation:** Semantic judgments can be features for supervised prediction; this tests a pipeline, not Jev fine-tuning or general domain transfer.

- Most gain comes from the first proposal; later-round paired 95% CI [-0.147,-0.050] concerns 800 rows, not repeated discovery runs.
- Feature/schema search must stay inside development folds; future text and target leakage need separate checks.
- Random row split and exact dedup do not establish temporal/group/near-duplicate generalization or no pretraining overlap.
- Feature importance is predictive, not causal. Source cache/alternate proposer descriptions are not our replay.

**Artifacts and limits:**
- protocol: Official code/output read
- raw outputs: Source describes cache; notebook/cache not replayed
- run date: 2026-08-03
- markdown sha256: 24e0854e5a5846c269142d2a57abfb8aa90d63c37231b03036ed08f1e9989b72

**Sources:** [TypeSafe autoresearch semantic features with CatBoost](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery)

<a id="e28"></a>
## E28 · EcomMIR: scene and intent scores belong to a combined competition pipeline

**Evidence:** `author_reported` · **Reviewed:** 2026-10-16 · **Reproduced here:** no

| Protocol | Recorded context |
| --- | --- |
| Task | WWW 2025 MIRE image-scene classification and multi-turn dialogue intent recognition; distinct outputs |
| Test unit | Round 2 competition examples; exact scored counts, item IDs and independent conversation groups not established from the reviewed paper |
| Split | Paper separates Local, Round 1 and Round 2. Round 1 unlabeled samples supply high-confidence pseudo-labels for training; a 9:1 local scene train/validation split is described. Do not call this 1,000-label-only training or untouched evaluation-round data. |
| Reference | Competition scene/intent labels; individual labels and adjudication not audited here |
| Training | CN-CLIP scene training/model soup; MiniCPM-V 2.6 intent LoRA plus data cleaning, hierarchical labels, high-confidence selection and image augmentation. Official MIRE Qwen2-VL full-SFT baseline is a separate implementation. |
| Measurement | Paper Table 3 intent Round 2 Ours F1; Table 2 scene Round 2 Model Soup F1. Aggregation convention and uncertainty not established here; do not combine task scores or compare to Decision Index/JevBench. |
| Hardware | Paper intent LoRA training uses two 80GB A800 GPUs with ms-swift/DeepSpeed; no serving P95, total cost or independently measured throughput imported |

| Reported measurement | Value |
| --- | --- |
| MiniCPM-V 2.6 combined intent system: Round 2 F1 | 94.20% |
| CN-CLIP scene Model Soup: Round 2 F1 | 82.78% |

**Interpretation:** A primary worked example supports studying multimodal adaptation and data interventions. These results do not isolate LoRA, prove a legal-option readout advantage or establish customer-support production outcomes.

- Both results are author-reported and were not rerun by this repository. Exact trained weight revisions and full raw outputs are not pinned.
- Round 1 pseudo-label selection and multiple interventions limit attribution; this is not training on only the original 1,000 labeled examples. Round 2 item identity/overlap is not independently audited; neither contamination nor a clean blind final test is established here.
- Paper tables report F1 without enough reviewed detail to equate it with a newly designed macro-F1 protocol or compute a significance claim.
- Some cleaning removes short utterances/handoff requests and image augmentation changes content; label preservation must be checked for any new task.
- Dataset access, base-model terms, code licenses and commercial usage rights are separate; no automatic commercial-use conclusion.

**Artifacts and limits:**
- protocol: Four-page primary paper read, Tables 1–3 visually checked; official challenge README/config inspected
- raw outputs: Not independently audited; no complete replay performed
- model hash: Exact evaluated checkpoints not captured
- source identity: DOI 10.1145/3701716.3718371; PDF content hash in source register

**Sources:** [EcomMIR: multimodal intent recognition competition solution](https://zhoushengisnoob.github.io/papers/WWWComp.pdf); [MIRE: official multimodal scene and dialogue-intent challenge](https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/README.md); [MIRE: Qwen2-VL-7B full-SFT baseline configuration](https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/mire_baseline/configs/qwen2_vl_full_sft.yaml)

