# Awesome Decision Models [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**Models, methods and evidence for reliable decisions in AI systems.**

[简体中文](README.zh-CN.md) · [Model cards](docs/models.md) · [Evidence ledger](docs/evidence.md) · [Selection guide](docs/selection-guide.md) · [Methodology](docs/methodology.md) · [Sources](docs/sources.md)

A curated guide to systems that **classify, score, rank, verify, route or abstain** rather than primarily generate prose. The central question is not which model has the most impressive headline, but **which method delivers acceptable outcomes at acceptable risk and total cost for a particular task**.

**Source review: 2026-10-17.** 50 selected resources, including 18 core model families and 31 contextualized evidence records. This edition reviews public sources; **it does not claim independent model reproduction**. Review depth and unresolved gaps are recorded in the [source register](docs/sources.md). Inclusion is not an endorsement or a production-readiness certification.

## Contents

- [Start with the task](#start-with-the-task)
- [Core models](#core-models)
- [Baselines worth keeping](#baselines-worth-keeping)
- [Routing and learning from outcomes](#routing-and-learning-from-outcomes)
- [Reliability and evaluation](#reliability-and-evaluation)
- [Foundations and recent research](#foundations-and-recent-research)
- [Related lists](#related-lists)
- [Maintenance and contribution](#maintenance-and-contribution)

## Start with the task

Here, **decision model** is an organizing label, not a claim that all these projects form one new, unified discipline. *Typed decisions* describes an output contract; *System One* is terminology used by some projects; *RLCD*, contrastive learning and supervised classification are different training approaches. Routing and selective prediction concern what the system does with a judgment.

| Your bottleneck | A useful starting comparison | Do not confuse it with |
| --- | --- | --- |
| Understand a message or check a bounded requirement | Typed models, label classifiers and a supervised baseline | Optimizing the effect of a downstream action |
| Choose among many reusable candidates | Dual encoders, rerankers and domain-trained selectors | Proving the best available candidate is correct |
| Choose an executor: model, tool or person | Routing and learning to defer, using actual executor outcomes | A generic task-difficulty score |
| Decide whether to automate | Held-out calibration, risk–coverage evaluation and abstention | Trusting a field named `confidence` |
| Learn which action improves an outcome | Contextual bandits or suitable causal methods | Predicting correlations from historical logs |

These are **curatorial starting points, not measured winners**. See the [selection guide](docs/selection-guide.md) for the decision contract and a minimal evaluation plan.

## Core models

The table compares mechanisms and use cases, **not incompatible benchmark scores**. Each row links to primary material; version-specific details and licensing notes are in the [model cards](docs/models.md).

| Model | Mechanism / proposition | Useful experiment | Important limitation |
| --- | --- | --- | --- |
| [Jev / TypeSafe](https://typesafe.ai) | Hosted typed judgments: probabilities over supplied choices, propositions and ordinal rubrics. | Managed typed-judgment comparator or frozen semantic-feature generator; compare supervised baselines under the same task and label policy. | RLCD is vendor-described; the full training recipe is not public. Valid schemas and confidence fields do not establish semantic reliability. |
| [Laya](https://github.com/NandhaKishorM/laya) | Compact encoder family with dynamic option heads; general, multilingual and workflow-specialized checkpoints. | Narrow, high-volume judgments with domain training and measured hardware costs. | Do not mix base/specialist scores; the typed card discloses training/calibration overlap and inherited-temperature conflicts. Boolean labels can dominate noul/choice; semantic labels alone do not make negation safe. action.act_probability is documented as nearly constant at 1 and unsuitable as an execution gate. Validate confidence on your workload instead. |
| [Kev](https://github.com/jaredpalmer/kev) | Qwen-based typed decision family with a dynamic pointer head; Kev 1.0 freezes existing checkpoints as a release baseline. | An inspectable starting point for domain-supervised decision models. | Keep trained-family tests separate from transfer. 27B v2 is worse and overconfident on long contracts (CUAD ECE 0.053 versus v1 0.007). Serving capacity and fitted temperature do not guarantee accuracy or calibration on new workloads. |
| [Contrastive Language Models (CLM)](https://github.com/Contrastive-LM/CLM) | Separate state and action representations with learned projection heads on a frozen language-model encoder. | Reusable candidate catalogs, tool selection and domain-trained Best-of-N selection. | Relative ranking cannot detect every all-wrong candidate set. Best-of-N scores include supplied candidates, not autonomous task-solving ability. |
| [Bespoke Nimble](https://github.com/bespokelabsai/nimble) | Qwen-based supervised adapter that reads answer-label logits instead of generating an explanation. | A transparent baseline for evidence-sensitive judgments and minimal-edit training examples. | Contrastive data construction is not CLM-style contrastive embedding training. Public benchmark reporting is author-run and raw run outputs are not all committed. |
| [GLiNER2.5-Decide](https://huggingface.co/fastino/GLiNER2.5-Decide-1B) | Schema-conditioned local classification with runtime labels and multiple decision heads. | Compact operational classification; inspect the runtime for supported cross-field constraints. | This review inspected the 1B card, which cross-reports 340M results. Dataset audit is incomplete; JevK5 in that table is not TypeSafe Jev. |
| [GLiClass](https://github.com/Knowledgator/GLiClass) | Label-conditioned text classification with user-supplied labels, including multilabel tasks. | An adjacent baseline for dynamic intent and label classification. | Classification capability does not establish general workflow verification or calibrated operational risk. |
| [jevos](https://github.com/feder-cr/jev) | Local yes/no decision model served as GGUF through llama.cpp, with a TypeSafe Jev-compatible request/response shape for `noul` questions. | Experiment with CPU-local reading and triage questions; put the full policy in `instructions` and validate behavior on your own labeled cases. | Yes/no only: `choice` and `score` return 422, and the jevos documentation says `criteria` is accepted but ignored. Wire-format compatibility is not semantic equivalence. Arithmetic/date errors and benchmark sensitivity are author-reported; old README results do not identify v2 performance. |
| [Clef / Clef-Flash](https://huggingface.co/Cloudflare/clef) | Multimodal Qwen backbones with a joint schema head for typed decisions and a Jev/SystemOne-compatible wrapper. | Compare text/image-based classification, triage and ordinal judgments with task-specific error costs. | Vendor benchmarks have task-specific trade-offs. API compatibility and probability outputs do not establish calibrated business risk; local inference needs the custom schema runtime. |
| [Strands Decider](https://github.com/strands-labs/strands-decider) | Qwen3.5 and Gemma 4 pointer-head family; October v1 releases average three trained adapters/heads and then calibrate. | A local baseline for short classification and domain-supervised decisions; test question changes, option order and risk–coverage on your own traffic. | Qwen v1 data builders are not yet on main. Several dev evaluations have their train splits in the mix. E2B index predates a CUDA attention fix; Qwen v1 missing-image overconfidence worsens on POPE. E07/E08 remain historical, not current guarantees. |
| [Perplexity Decider v1 / v1.1 (27B)](https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b) | Qwen3.8-27B family; v1.1 native artifact uses a separate 255-code head and saved noncausal full-attention, with image inputs. | A self-hosted comparator for text/image judgments after task-specific validation. | Archived v1/API card results and native v1.1 are distinct. Training source/manifests are inspectable, but full raw-data replay and backend/calibration equivalence are not independently established. |
| [Microsoft-Decision-1](https://ai.azure.com/catalog/models/Microsoft-Decision-1) | Hosted Qwen3.5-9B post-training for bounded option scoring. | Compare classification, routing and rubric judgments. | Vendor comparisons lack audited item-level artifacts; familiar-task calibration need not transfer. Wording and safety errors remain. |
| [OpenAI Decisions API / GPT-6 Luna](https://developers.openai.com/api/docs/guides/decisions) | Public-beta typed judgment API for text and images. | Managed classification, routing and ordinal scoring. | Refusal is a separate answer variant, not calibrated abstention. Confidence needs target-task validation; training and serving identity are undisclosed here. |
| [Nace Drex v1.5](https://github.com/nace-ai/drex-decision-models) | MiMo-V2.6-Distill-Qwen-9B backbone with a Kev pointer head and public-weight release links. | Local candidate for text/JSON decisions, including long inputs. | Benchmark training splits are used; results are not unseen-domain zero-shot. Public Index 0.3.1 leaders fall inside its tie band. Small runner checks do not establish broad parity. |
| [vLLM-SR Decision 3.0](https://huggingface.co/collections/vllm-sr/decision-30) | Six multimodal code-readout checkpoints; native vLLM main support added October 14, with an independent prompt read per question. | Local text/image/video classification, scoring and routing; compare sizes at fixed input and candidate budgets. | Index versions and public-only scores differ. In the Oct15 snapshot, weight/calibration identities were unchanged and the text numerical leader shared the top tie band. That serving review required post-merge/nightly native vLLM; LoRA and CUDA were unmeasured in the integration report. |
| [Intern-Decision](https://github.com/internlm/Intern-Decision) | Qwen3.5 multimodal 0.8B/2B/4B family; multiple typed fields scored from one causal masked assistant skeleton. | Compare multi-field cost and field/order sensitivity against per-question models; test image-grounded judgments. | Private training/calibration records are absent. A 96-case distribution pilot is diagnostic; size/backend-specific temperature and max(P) confidence are not portable business risk guarantees. Paper seven-suite accuracy concerns text tasks; visual trajectories are qualitative. Public Jevbench informed development; matched-data ablations and a matched D3 multimodal comparison are absent from the reviewed evidence. |
| [Verdict / OpenJev](https://github.com/Heman10x-NGU/Verdict-open-jev) | 151M ModernBERT/GLiClass candidate classifier with an explicit insufficient-evidence option and per-K calibration. | Compact intent classification and missing-option tests; compare native serving probabilities with the exact evaluation renderer/calibrator. | Author tests show abstention collapsing under hard negatives and synonym wording. Converter reports shipped serving calibration differs substantially from the held-out evaluation; no domain-independent abstention guarantee. |
| [StartLux-Decision v1.1 (Instant / AutoThink)](https://github.com/StartLuxLabs/StartLux-Decision) | Option-letter LM readout: Instant uses prompt-bidirectional full-attention; causal AutoThink conditionally reasons and fuses two distributions. | Compare one-pass versus selective computation on evidence-complete decisions, at matched risk and complete cost; commercial use requires separate weight authorization. | Public DI is development-selected, not the full/private board. DecisionPivot is author-built/evaluated. Gate 0.9 paper results do not describe current 0.6 defaults; confidence/none signals need policy-specific validation. |

### Read these results in context

- [E01 — Laya: specialist performance is not base-model performance](docs/evidence.md#e01)
- [E02 — CLM: a domain-trained selector recovers more successful supplied candidates](docs/evidence.md#e02)
- [E03 — Nimble vs Jev: paired human-reference comparisons remain task-dependent](docs/evidence.md#e03)
- [E04 — GLiNER2.5-Decide: keep a newly reported suite in its proper scope](docs/evidence.md#e04)
- [E05 — Kev: preserve development/test and source-domain distinctions](docs/evidence.md#e05)
- [E06 — Clef: a vendor comparison has task-specific reversals](docs/evidence.md#e06)
- [E07 — Strands Decider: instruction sensitivity and experiment-selection limits](docs/evidence.md#e07)
- [E08 — Strands Decider v21: release seed and controlled retrain comparison](docs/evidence.md#e08)
- [E09 — Drex v1.5: public-suite ties and benchmark-training overlap](docs/evidence.md#e09)
- [E10 — Microsoft-Decision-1: perturbation stability is an author claim](docs/evidence.md#e10)
- [E11 — Strands Qwen3.5 v1: new recipe, soup and missing-image limits](docs/evidence.md#e11)
- [E12 — Decision 3.0: internal Index and device timing are bounded author reports](docs/evidence.md#e12)
- [E13 — Decision 3.0: the full public kit is not the internal composite or JevBench](docs/evidence.md#e13)
- [E14 — Decision 3.0 video: sampled-frame QA does not validate audio or streaming reliability](docs/evidence.md#e14)
- [E15 — Decision 3.0 on Apple: conversion and public-harness evidence](docs/evidence.md#e15)
- [E16 — Decision 3.0 PR triage: throughput and real-label agreement are different tests](docs/evidence.md#e16)
- [E17 — WebMCP application test: small differences and preprocessing errors](docs/evidence.md#e17)
- [E18 — Intern-Decision: exact-distribution calibration pilot, not hard-label accuracy](docs/evidence.md#e18)
- [E19 — Verdict deployment: evaluator calibration is not shipped serving calibration](docs/evidence.md#e19)
- [E20 — Verdict abstention: preserve hard-negative and synonym failures](docs/evidence.md#e20)
- [E21 — Decision 3.0 Index 0.3.2: scoring changes with unchanged weight identities](docs/evidence.md#e21)
- [E22 — Decision 3.0 serving: batching gains have load and overload boundaries](docs/evidence.md#e22)
- [E23 — Native vLLM D3: merged source and bounded parity/concurrency evidence](docs/evidence.md#e23)
- [E24 — Financial earnings: conditional comparison labels and unequal text windows](docs/evidence.md#e24)
- [E25 — Financial 8-K categories: supervision and post-hoc selection](docs/evidence.md#e25)
- [E26 — SEC follow-up: 90-day forecasting differs from textual completeness](docs/evidence.md#e26)
- [E27 — Semantic features: wine-score prediction with development-only discovery](docs/evidence.md#e27)
- [E28 — EcomMIR: scene and intent scores belong to a combined competition pipeline](docs/evidence.md#e28)
- [E29 — StartLux: public DI 0.3 is a development-selected subset, not a full-board result](docs/evidence.md#e29)
- [E30 — DecisionPivot: author-built contrast benchmark and release-run pair accuracy](docs/evidence.md#e30)
- [E31 — RLCD²: conditional reasoning-efficiency gains are not universal calibration or service-latency gains](docs/evidence.md#e31)

For domain evaluation and verified training support, see the [image-intent adaptation workflow](docs/selection-guide.md#image-intent-adaptation). Start with the [one-page multimodal post-training route](docs/multimodal-decision-finetuning.md#quick-route), then follow the controlled experiments, candidate gates and [layered academic reading list](docs/multimodal-decision-finetuning.md#reading-list).

The [readout and adaptive-reasoning comparison](docs/decision-readout-and-reasoning.md) separates StartLux Instant/AutoThink, D3, Decider v1.1 and hosted Jev, including training versus serving and public versus independent evidence.

**No combined accuracy leaderboard:** zero-shot classification, workflow fine-tuning and Best-of-N selection answer different questions. Local GPU forward time and remote API round-trip time are also different measurements.

## Baselines worth keeping

A new training label is not evidence that a familiar baseline is obsolete. Deployment resources also help test whether a local implementation preserves the intended decision behavior. These alternatives help isolate gains from the data, output contract, architecture and training objective.

- **[SetFit](https://github.com/huggingface/setfit)** — Few-shot sentence-transformer adaptation followed by a classification head. Not an arbitrary typed-question API.
- **[Qwen3-Reranker](https://huggingface.co/Qwen/Qwen3-Reranker-0.6B)** — Task-trained query/document reranking. A relevance score is not a probability of business correctness.
- **[Outlines](https://github.com/dottxt-ai/outlines)** — Constrained structured output for ordinary language models. Schema validity does not guarantee factual validity.
- **[TabICLv2](https://arxiv.org/abs/2602.11139)** — A tabular foundation model for classification and regression. Paper-level inclusion; no local reproduction or natural-language claim.
- **[FluidUse / decision-model Core ML deployment](https://github.com/FluidInference/FluidUse)** — Apple deployment resource with native Swift managers and Python-assisted Core ML bridges, including Decision 3.0. Conversion parity and smoke tests are not quality guarantees. Match length buckets, precision, tokenizer, calibrator and media path; bridge calls queue serially and timeouts close the session. Automatic downloads/environment setup are documented, not run here.
- **[Semantic features + supervised predictor](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery)** — LLM-proposed questions and Jev judgments turn text into features for a supervised CatBoost predictor. Author-reported wine regression. Feature discovery belongs inside development folds; downstream training does not fine-tune Jev or establish financial/multimodal generalization.
- **[ezjev text candidate-logit LoRA](https://github.com/everettjf/ezjev/tree/8b3d88957c0795bea160c8fbc9c6d2a54b051136)** — Inspectable per-question candidate CE+Brier, replay and temperature fitting on a Qwen3.5 text-training path. Not an image fine-tuning implementation. MIT covers code only; some training data are non-commercial or lack stated terms. No training or calibration result reproduced here.
- **[decision-pacman decision distillation](https://github.com/grapeot/decision-pacman/tree/593ed1f59f4f97ad0bda7287ff304e9667360089)** — Text-state teacher/simulator labels train a small option-distribution LoRA student. Game-specific author reports include lost generality. Not image-training or customer-support transfer evidence; complete data/evaluated artifacts not audited.

Also retain a deterministic rule or ordinary supervised classifier where the task permits. A model should earn its complexity against the simplest credible alternative.

## Routing and learning from outcomes

- **[RouteLLM](https://github.com/lm-sys/RouteLLM)** — Routes between stronger and cheaper language models using learned signals. Performance depends on the model pair, traffic and router training distribution.
- **[LLMRouter](https://github.com/ulab-uiuc/LLMRouter)** — Research infrastructure for building and comparing routing strategies. The August 2026 paper is a preprint; do not equate infrastructure with a proven best policy.
- **[Vowpal Wabbit](https://github.com/VowpalWabbit/vowpal_wabbit)** — Online-learning and contextual-bandit tooling. Requires appropriate logging, exploration and evaluation assumptions.

For executor selection, collect **task, available evidence, executor, outcome, latency and cost**. Observed success for one selected executor does not reveal how every alternative would have performed. See the learning-to-defer and causal references below.

## Reliability and evaluation

- **[MAPIE](https://github.com/scikit-learn-contrib/MAPIE)** — Prediction-set, uncertainty and conformal-risk tooling. Guarantees depend on the procedure, target risk and data assumptions.

- **[Decision Index (archival releases and live board)](https://huggingface.co/spaces/multimodalart/jev-decision-index)** — A broader decision benchmark index with explicit aggregation rules. Oct14-generated 0.3.2 aggregate JSON inspected on Oct15; private items/raw runs remain unaudited. Text uses a 0.9-point tie band. Archive scoring versions separately: 0.3.2 includes scoring/data corrections, not evidence of retraining.
- **[Nimble public evaluations](https://github.com/bespokelabsai/nimble/blob/62076b4f2d365b5879dafcf7f6dd072a1fe76df7/docs/PUBLIC_BENCHMARKS.md)** — Human-reference subsets, paired comparisons and calibration reporting. Project-author-run, not independently reproduced by this list.
- **[Decision-model benchmark](https://github.com/nibzard/decision-model-benchmark)** — Third-party code and protocols for decision-model comparisons. Third-party status alone does not certify methodology or labels.
- **[Financial-document decision tests](https://insights.ml4trading.io/p/testing-jev-on-financial-documents)** — Original-evaluator comparison of Jev and supervised text/TF-IDF models on earnings, 8-K labels and SEC follow-up. Vendor API support; historical selected populations, hindsight screening, post-hoc prompts and split limitations. No universal tree-versus-Jev winner or investment-return claim.
- **[MIRE / EcomMIR multimodal intent evaluation](https://github.com/liujunwen23/MIRE/tree/d101287af90d114c5bf0cbfbd56fe9c52358e3bb)** — Image-scene and multi-turn intent challenge, with full-SFT baseline and a published LoRA-based competition solution. EcomMIR scores are author-reported combined interventions with Round 1 pseudo-labels; not LoRA-only or a 1,000-example-only untouched-test result. Dataset rights and full replay remain unverified.
- **[DecisionPivot v1.1](https://huggingface.co/datasets/startlux-models/DecisionPivot/tree/b6a65d303f3f8689d293869aff3db41f944984c6)** — 13 generated contrast families, programmatic labels and public generator/solver/scoring assets; separate reused-public-task reference track. StartLux-author benchmark and runs, not third-party reproduction. Corrected v1.1 and intermediate tables must not be silently equated to the paper release scores. Hindsight coverage metrics are not deployment risk guarantees.

A useful scorecard includes task quality, consequential errors, calibration, risk–coverage, subgroup/shift behavior and full-system cost. Fix the acceptance threshold on calibration data, not on the final test set. Keep sampling automatically accepted cases so confidently wrong decisions remain visible.

## Foundations and recent research

Reading order: probability quality → abstention → executor handoff → risk control. Dates are publication/version dates, not a claim of exhaustive coverage of the latest literature. Abstract-only reviews are labeled in the source register.

- **[Strictly Proper Scoring Rules (2007)](https://doi.org/10.1198/016214506000001437)** — Why log loss and other proper scores target truthful distributions. An ideal optimization target is not proof of deployment calibration.
- **[On Calibration of Modern Neural Networks (2017)](https://proceedings.mlr.press/v70/guo17a.html)** — Empirical calibration and post-hoc temperature scaling. Calibration cannot repair incorrect rankings or missing evidence.
- **[Selective Classification (2017)](https://arxiv.org/abs/1705.08500v2)** — Classification with abstention and risk/coverage trade-offs. Source experiments are not guarantees for unrelated LLM tasks.
- **[Learning to Defer to an Expert (2020)](https://proceedings.mlr.press/v119/mozannar20b.html)** — Jointly learn prediction and handoff to an expert. Humans and tools are not assumed infallible.
- **[Conformal Risk Control (2022; reviewed v4)](https://arxiv.org/abs/2208.02814v4)** — Calibrate risk-controlling procedures under stated conditions. Read exchangeability, loss and monotonicity assumptions.
- **[Non-Monotonic Conformal Risk Control (2026)](https://arxiv.org/abs/2602.20151v1)** — Extends the risk-control discussion beyond monotone losses. Preprint; stability-dependent bounds, not unconditional safety.
- **[Proper Scoring Rules: 2026 review](https://doi.org/10.1146/annurev-statistics-042424-050626)** — A recent review of estimation and forecast evaluation. Included from the abstract and publication metadata.
- **[Causal Learning to Defer (AAAI 2026)](https://ojs.aaai.org/index.php/AAAI/article/view/39493)** — Studies handoff learning with hidden confounding. Adjacent research, not a turnkey production router.
- **[Jev in the Wild (2026)](https://arxiv.org/abs/2609.30216)** — Data-driven survey and analysis of 2,170 public GitHub Jev projects, including early growth, application domains and decision-use patterns. Public repository counts do not establish deployment adoption or model accuracy; included from the abstract, not an independent reproduction.

## Related lists

These maintainers provide complementary discovery paths. This repository adds a task-first comparison and claim-level evidence records; it does not copy their collections or sort by stars.

- **[Awesome System One](https://github.com/andyrewlee/awesome-system-one)** — Closest ecosystem list; useful for discovery. Inclusion here does not endorse every linked item.
- **[Awesome Jev 中文](https://github.com/yzfly/awesome-jev-zh)** — Chinese-language Jev ecosystem resources. Inclusion here does not endorse every linked item.
- **[Awesome LLM Routing and Cascading](https://github.com/ymoslem/awesome-llm-routing-cascading)** — Specialist routing and cascading bibliography. Inclusion here does not endorse every linked item.
- **[Awesome Conformal Prediction](https://github.com/valeman/awesome-conformal-prediction)** — Specialist uncertainty and conformal prediction resources. Inclusion here does not endorse every linked item.
- **[Awesome Martech AI](https://github.com/leoncuhk/awesome-martech-ai)** — Marketing data, intelligence, decision, activation and measurement resources with applied playbooks. Companion navigation, not independent product validation; its synthetic demo does not establish customer uplift.

## Maintenance and contribution

The factual catalog lives in [`data/catalog.json`](data/catalog.json); numerical claims live in [`data/evaluations.json`](data/evaluations.json). Generated Markdown must stay synchronized with those records.

```sh
python3 scripts/render.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

A [repository-scoped curator skill](.agents/skills/decision-models-curator/SKILL.md) defines the research/review procedure. A [weekly source watcher](.github/workflows/source-watch.yml) checks selected sources for changes and maintains an issue for review. **It does not run an AI researcher, update scientific claims, merge changes or require a paid model API.** See [maintenance](docs/maintenance.md) for setup, security, scheduling limits and manual use.

Read [CONTRIBUTING](CONTRIBUTING.md) before adding a project or result. Negative findings, changed assumptions and corrections are welcome. [Initial review notes](updates/2026-09-25.md) preserve the original qualifications; the [October 6 release review](updates/2026-10-06-release-boundaries.md) and [October 11 review](updates/2026-10-11-typed-releases.md) record additions, corrections and remaining gaps. [October 13 multimodal/deployment review](updates/2026-10-13-multimodal-deployment.md) separates new release, calibration and application evidence. [October 15 update](updates/2026-10-15-serving-and-adaptation.md) reviews native vLLM, score changes, semantic features and domain adaptation. [October 16 research update](updates/2026-10-16-multimodal-finetuning.md) adds training-path and competition-evidence checks. [October 17 StartLux review](updates/2026-10-17-startlux-and-decisionpivot.md) records new model, benchmark and mechanism evidence. [Multimodal post-training guide update](updates/2026-10-17-d3-text-training.md) adds a paper-grounded experiment route and clarifies D3 text training. [Publishing instructions](PUBLISHING.md) explain how to initialize an empty repository safely.

Original code and curation text: [MIT](LICENSE). Linked projects, model weights, datasets and papers retain their own licenses. A source-text revision does **not** pin a model's weights.
