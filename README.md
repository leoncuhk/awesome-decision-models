# Awesome Decision Models

**Models, methods and evidence for reliable decisions in AI systems.**

[简体中文](README.zh-CN.md) · [Model cards](docs/models.md) · [Evidence ledger](docs/evidence.md) · [Selection guide](docs/selection-guide.md) · [Methodology](docs/methodology.md) · [Sources](docs/sources.md)

A curated guide to systems that **classify, score, rank, verify, route or abstain** rather than primarily generate prose. The central question is not which model has the most impressive headline, but **which method delivers acceptable outcomes at acceptable risk and total cost for a particular task**.

**Source review: 2026-09-25.** 31 selected resources, including 8 core model families and 5 contextualized evidence records. This edition reviews public sources; **it does not claim independent model reproduction**. Review depth and unresolved gaps are recorded in the [source register](docs/sources.md). Inclusion is not an endorsement or a production-readiness certification.

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
| [Jev / TypeSafe](https://typesafe.ai) | Hosted typed judgments: probabilities over supplied choices, propositions and ordinal rubrics. | A managed comparator when testing whether a judgment node is useful. | RLCD is vendor-described; the full training recipe is not public. Valid schemas and confidence fields do not establish semantic reliability. |
| [Laya](https://github.com/NandhaKishorM/laya) | Compact encoder family with dynamic option heads; general, multilingual and workflow-specialized checkpoints. | Narrow, high-volume judgments with domain training and measured hardware costs. | Do not mix base and specialized scores. The typed checkpoint currently discloses training/calibration overlap and inherited-temperature conflicts. |
| [Kev](https://github.com/jaredpalmer/kev) | Qwen-based adapters and a dynamic pointer head for typed decisions, with training and serving tools. | An inspectable starting point for domain-supervised decision models. | New-source development, held-out tests and trained-source scores are distinct. Adapter size is not deployment memory. |
| [Contrastive Language Models (CLM)](https://github.com/Contrastive-LM/CLM) | Separate state and action representations with learned projection heads on a frozen language-model encoder. | Reusable candidate catalogs, tool selection and domain-trained Best-of-N selection. | Relative ranking cannot detect every all-wrong candidate set. Best-of-N scores include supplied candidates, not autonomous task-solving ability. |
| [Bespoke Nimble](https://github.com/bespokelabsai/nimble) | Qwen-based supervised adapter that reads answer-label logits instead of generating an explanation. | A transparent baseline for evidence-sensitive judgments and minimal-edit training examples. | Contrastive data construction is not CLM-style contrastive embedding training. Public benchmark reporting is author-run and raw run outputs are not all committed. |
| [GLiNER2.5-Decide](https://huggingface.co/fastino/GLiNER2.5-Decide-1B) | Schema-conditioned local classification with runtime labels and multiple decision heads. | Compact operational classification; inspect the runtime for supported cross-field constraints. | This review inspected the 1B card, which cross-reports 340M results. Dataset audit is incomplete; JevK5 in that table is not TypeSafe Jev. |
| [GLiClass](https://github.com/Knowledgator/GLiClass) | Label-conditioned text classification with user-supplied labels, including multilabel tasks. | An adjacent baseline for dynamic intent and label classification. | Classification capability does not establish general workflow verification or calibrated operational risk. |
| [jevos](https://github.com/feder-cr/jev) | Local, CPU-only alternative to Jev for yes/no decisions: a 1B model (MiniCPM5 cut to 17 layers with a single-logit output head) served as GGUF via llama.cpp, over the same wire format as Jev's API. | A drop-in endpoint for TypeSafe's Jev SDK when only yes/no (`noul`) questions are needed and running fully offline on a laptop CPU is preferred over the hosted service. | Only yes/no questions are supported; `choice` and `score` requests return 422. On 2,000 yes/no questions from policies unseen in training it scored 0.815 accuracy versus the vendor's reported 0.927 for Jev (Laya 0.489 on the same set) — the author's own comparison, not an independent reproduction. |

### Read these results in context

- [E01 — Laya: specialist performance is not base-model performance](docs/evidence.md#e01)
- [E02 — CLM: a domain-trained selector recovers more successful supplied candidates](docs/evidence.md#e02)
- [E03 — Nimble vs Jev: paired human-reference comparisons remain task-dependent](docs/evidence.md#e03)
- [E04 — GLiNER2.5-Decide: keep a newly reported suite in its proper scope](docs/evidence.md#e04)
- [E05 — Kev: preserve development/test and source-domain distinctions](docs/evidence.md#e05)

**No combined accuracy leaderboard:** zero-shot classification, workflow fine-tuning and Best-of-N selection answer different questions. Local GPU forward time and remote API round-trip time are also different measurements.

## Baselines worth keeping

A new training label is not evidence that a familiar baseline is obsolete. These alternatives help isolate gains from the data, output contract, architecture and training objective.

- **[SetFit](https://github.com/huggingface/setfit)** — Few-shot sentence-transformer adaptation followed by a classification head. Not an arbitrary typed-question API.
- **[Qwen3-Reranker](https://huggingface.co/Qwen/Qwen3-Reranker-0.6B)** — Task-trained query/document reranking. A relevance score is not a probability of business correctness.
- **[Outlines](https://github.com/dottxt-ai/outlines)** — Constrained structured output for ordinary language models. Schema validity does not guarantee factual validity.
- **[TabICLv2](https://arxiv.org/abs/2602.11139)** — A tabular foundation model for classification and regression. Paper-level inclusion; no local reproduction or natural-language claim.

Also retain a deterministic rule or ordinary supervised classifier where the task permits. A model should earn its complexity against the simplest credible alternative.

## Routing and learning from outcomes

- **[RouteLLM](https://github.com/lm-sys/RouteLLM)** — Routes between stronger and cheaper language models using learned signals. Performance depends on the model pair, traffic and router training distribution.
- **[LLMRouter](https://github.com/ulab-uiuc/LLMRouter)** — Research infrastructure for building and comparing routing strategies. The August 2026 paper is a preprint; do not equate infrastructure with a proven best policy.
- **[Vowpal Wabbit](https://github.com/VowpalWabbit/vowpal_wabbit)** — Online-learning and contextual-bandit tooling. Requires appropriate logging, exploration and evaluation assumptions.

For executor selection, collect **task, available evidence, executor, outcome, latency and cost**. Observed success for one selected executor does not reveal how every alternative would have performed. See the learning-to-defer and causal references below.

## Reliability and evaluation

- **[MAPIE](https://github.com/scikit-learn-contrib/MAPIE)** — Prediction-set, uncertainty and conformal-risk tooling. Guarantees depend on the procedure, target risk and data assumptions.

- **[Decision Index 0.2](https://huggingface.co/spaces/multimodalart/jev-decision-index)** — A broader decision benchmark index with explicit aggregation rules. Composite scores are not raw accuracy; API/GPU timings are not a controlled hardware experiment.
- **[Nimble public evaluations](https://github.com/bespokelabsai/nimble/blob/62076b4f2d365b5879dafcf7f6dd072a1fe76df7/docs/PUBLIC_BENCHMARKS.md)** — Human-reference subsets, paired comparisons and calibration reporting. Project-author-run, not independently reproduced by this list.
- **[Decision-model benchmark](https://github.com/nibzard/decision-model-benchmark)** — Third-party code and protocols for decision-model comparisons. Third-party status alone does not certify methodology or labels.

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

## Related lists

These maintainers provide complementary discovery paths. This repository adds a task-first comparison and claim-level evidence records; it does not copy their collections or sort by stars.

- **[Awesome System One](https://github.com/andyrewlee/awesome-system-one)** — Closest ecosystem list; useful for discovery. Inclusion here does not endorse every linked item.
- **[Awesome Jev 中文](https://github.com/yzfly/awesome-jev-zh)** — Chinese-language Jev ecosystem resources. Inclusion here does not endorse every linked item.
- **[Awesome LLM Routing and Cascading](https://github.com/ymoslem/awesome-llm-routing-cascading)** — Specialist routing and cascading bibliography. Inclusion here does not endorse every linked item.
- **[Awesome Conformal Prediction](https://github.com/valeman/awesome-conformal-prediction)** — Specialist uncertainty and conformal prediction resources. Inclusion here does not endorse every linked item.

## Maintenance and contribution

The factual catalog lives in [`data/catalog.json`](data/catalog.json); numerical claims live in [`data/evaluations.json`](data/evaluations.json). Generated Markdown must stay synchronized with those records.

```sh
python3 scripts/render.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

A [repository-scoped curator skill](.agents/skills/decision-models-curator/SKILL.md) defines the research/review procedure. A [weekly source watcher](.github/workflows/source-watch.yml) checks selected sources for changes and maintains an issue for review. **It does not run an AI researcher, update scientific claims, merge changes or require a paid model API.** See [maintenance](docs/maintenance.md) for setup, security, scheduling limits and manual use.

Read [CONTRIBUTING](CONTRIBUTING.md) before adding a project or result. Negative findings, changed assumptions and corrections are welcome. [Initial review notes](updates/2026-09-25.md) document this edition's important qualifications. [Publishing instructions](PUBLISHING.md) explain how to initialize an empty repository safely.

Original code and curation text: [MIT](LICENSE). Linked projects, model weights, datasets and papers retain their own licenses. A source-text revision does **not** pin a model's weights.
