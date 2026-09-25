# Curation and evaluation methodology

[Home](../README.md) · [中文首页](../README.zh-CN.md) · [Evidence ledger](evidence.md)

## Scope: a useful boundary, not a new discipline

This list covers bounded judgments used inside AI systems: classification, ordinal scoring, candidate ranking, verification, routing and abstention. A resource belongs here when it changes how a system **forms, evaluates or uses such a judgment**.

The core is typed or label-conditioned language judgment. Routing, selective prediction, contextual bandits and tabular methods are explicitly adjacent. We do not collect every agent framework, every reasoning model, every business-intelligence product or all of reinforcement learning. We include familiar baselines where they test whether a specialized model is necessary.

“System One,” “typed decision model” and “non-generative readout” are not synonyms. An output contract, a cognitive analogy, an architecture and a training objective describe different layers. No new field-wide standard is implied.

## Inclusion criteria

A resource needs an identifiable maintainer or research author, an inspectable primary source, a concrete task fit, and a concise limitation. Code, a model card, documentation or a paper may suffice for inclusion, but **availability is not evidence of effectiveness**. Abstract-only literature entries are allowed when explicitly marked and when no detailed experimental claim is imported.

Stars, social engagement and claimed multipliers do not determine order. Paid placement is not accepted. Duplicate wrappers without a meaningful technical distinction should be linked under the original project rather than added as new model families.

A model is not called “open source” simply because its weights can be downloaded. Record code, weights, training data and training recipe separately. Check the exact model and backbone licenses before deployment. Unknown information remains unknown.

## Three activities that must not be conflated

| Activity | What has actually been established |
| --- | --- |
| Source review | The source says this, and the statement is represented with its conditions. |
| Artifact audit | Specified data, code, hashes and outputs can be inspected and related to the claim. |
| Reproduction | An identified evaluator ran an identified protocol and obtained recorded results. |

The initial edition performs source review. It does not claim complete artifact audits or any model reproduction. A repository commit pins text or code; a live Hugging Face name does not pin weights. A hash printed in a model card is **author-supplied** until the corresponding bytes have been checked.

## Evidence types

`author_reported` means a model author or project contributor ran/reported the experiment. `third_party_reported` means the identified reporter is separate from the compared model authors to the extent verified. `reproduced_here` requires this repository to publish the evaluator, environment, commands, exact artifacts and resulting outputs. `unverified_claim` can be a research lead, but must not be presented as an established performance result.

These are provenance labels, not automatic quality scores. An excellent author experiment can be more informative than a weak third-party experiment. Funding, overlap, prompt selection and artifact access matter. Attach the label to **each claim**, not the entire project.

## A minimum performance record

Record the exact model/checkpoint and serving version; source revision; task and candidate set; dataset version and source; train/development/calibration/test splits; sample and independence unit; label provenance; zero-shot or training setup; metric definition; hardware, precision, batching and concurrency; cost boundary; errors/timeouts; original results; reproduction status; date reviewed; and unresolved limitations.

Not every source supplies everything. Missing fields do not require excluding a potentially useful resource, but they reduce the conclusion that can be supported. This is why the first edition preserves `null` weight revisions rather than guessing a checkpoint from a current model page.

### Direct comparison is conditional

For a direct claim, match the task, test items, label mapping, evidence visible to the models, candidate budget, evaluation mode and failure accounting. Do not merge:

- Zero-shot results with task-tuned results, or development sets with final test sets.
- Teacher agreement with independently observed outcomes or human adjudication.
- Candidate selection with candidate generation, or a small local subset with a full official benchmark.
- CPU measurements, warm GPU forward time and API round-trip latency.

If the same examples have multiple paraphrases, steps, candidates or labels, retain a grouping identifier and use the right unit for uncertainty estimates. Paired comparisons, family-aware resampling and correction for multiple comparisons may be needed. A small apparent gain is not automatically a statistically or operationally meaningful gain.

## What to measure

**Task quality.** Use appropriate task metrics: accuracy or macro-F1 for classification, MAE with an explicit ordinal scale, ranking quality at a specified candidate budget, or observable execution success. Report critical error types, not just the average.

**Probability quality.** State the NLL/Brier convention, class aggregation, clipping and ECE binning. A scoring rule's theoretical optimum does not establish empirical calibration. Post-hoc calibration needs data separated from model training and final testing. See [proper scoring rules](https://doi.org/10.1198/016214506000001437) and [Guo et al.](https://proceedings.mlr.press/v70/guo17a.html).

**Selective behavior.** For an acceptance set \(S_t\), report coverage \(P(X\in S_t)\) and error conditional on acceptance, not only overall error. Specify whether the threshold was fixed before testing. Distinguish an observed risk on a finite sample from a statistically supported bound and from a production service-level objective. Relevant starting points are [selective classification](https://arxiv.org/abs/1705.08500v2), [conformal risk control](https://arxiv.org/abs/2208.02814v4) and its [non-monotonic-loss extension](https://arxiv.org/abs/2602.20151v1); their assumptions are not interchangeable.

**Complete cost.** Include evidence retrieval, preprocessing, candidate generation, model inference, retries, tool execution, manual review and correction. Report cold/warm behavior, input and candidate lengths, precision/quantization, concurrency, cache policy, p50/p95, timeouts and invalid outputs. A tiny trainable adapter can still require a large backbone at inference.

**Shift and robustness.** Test source/time/customer separation, language, missing evidence, contradictory inputs, all-wrong candidate sets, option order, long contexts, negation, exception rules and prompt injection inside untrusted material. A model-selected “none” option is not automatically a calibrated abstention mechanism.

## Interpret scores before acting

A normalized probability over candidates answers a relative question. It need not measure the absolute chance that any candidate is acceptable. A confidence margin is not necessarily an independently estimated probability of correctness. Lower ECE does not imply higher useful coverage. Logically consistent outputs can still be false.

A scoring model should not decide its own permissions. Validate schemas and hard constraints in code. Let policies determine the allowable actions and error costs. For routing, use actual executor performance, including human fallibility; [learning to defer](https://proceedings.mlr.press/v119/mozannar20b.html) is not merely a synonym for classifying task difficulty.

## Chinese summary / 中文要点

本仓库把“来源声称”“产物可查”“独立复现”分开。首页按任务与机制组织，成绩必须带版本、样本、划分、参考标签和测量范围。未披露的信息不补猜。

检查点名称、运行库版本、Git 提交和模型权重是不同对象。代码更新不代表能力更新；公开权重不代表训练过程可复现。概率分布、置信差值、校准与业务风险也不是同一概念。

技术选择应回答：在预先确定的风险约束下，多少真实工作可以自动完成，完整成本是多少。无法直接比较的成绩保留为独立证据，不拼总榜。校准、拒判和权限控制是系统职责，不应全寄托在模型自报分数上。
