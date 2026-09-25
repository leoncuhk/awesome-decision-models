# Selection guide / 选型指南

[Home](../README.md) · [Model cards](models.md) · [Evidence](evidence.md)

## 1. Define the decision before selecting the model

Write one small **decision contract**: available evidence, question, allowed answers, what makes an answer correct, cost of each error, and what happens when evidence is insufficient. Keep semantic judgment separate from permission to act.

Example: “Does this deliverable satisfy these stated acceptance tests?” is different from “Which worker should receive it?” and from “Which intervention will improve its final outcome?” The first needs evidence and acceptance criteria; the second needs executor performance; the third needs an appropriate action/outcome learning design.

For a bounded adjudication, a useful design objective is

\[
 a^*(x)=\arg\min_{a\in A_{\mathrm{allowed}}(x)}
 \{\mathbb{E}[L(a,Y)\mid x]+C_{\mathrm{execution}}(a)+C_{\mathrm{delay}}(a)\}.
\]

This is a **design formulation**, not a claim that the listed models estimate every term. For interventions, use an action-conditional causal or bandit formulation rather than silently treating a predicted label as an action's effect. See the [contextual-bandit tutorial](https://vowpalwabbit.org/docs/vowpal_wabbit/python/latest/tutorials/python_Contextual_bandits_and_Vowpal_Wabbit.html).

## 2. Choose the information structure

| Situation | Reasonable experiment | Key check |
| --- | --- | --- |
| Exact arithmetic, dates or explicit hard rules | Code/rules first; give their results to the semantic model | Test the preprocessing independently. |
| Stable labels with examples | A conventional classifier or SetFit, alongside a typed model | Does flexibility justify added cost? |
| Few choices with subtle conditions | A joint text/question/option readout such as Kev or Nimble, plus a hosted comparator | Negation, exceptions, missing evidence and order changes. |
| Many reusable options | A dual encoder such as CLM; a reranker where relevance is the real target | Cache economics and the all-wrong/missing-candidate case. |
| Very frequent, narrow classification | Laya or GLiNER2.5-Decide as local candidates | Domain adaptation, languages, context limits and actual hardware. |
| Model/tool/person handoff | RouteLLM or LLMRouter experiments; learning-to-defer formulations | Measured executor complementarity, not generic difficulty. |
| Mostly numerical or categorical records | Conventional tabular baselines and, where appropriate, TabICLv2 | Missing values, drift, sample regime and leakage. |

These are hypotheses to test, not published comparative results. No single architecture should be the default for every row. In particular, candidate selection and final acceptance can be different stages.

## 3. Start with the simplest credible learning signal

With complete, trusted labels for a single-step judgment, supervised log loss is a strong baseline. Its expected objective can be decomposed as \(H(p)+D_{KL}(p\|q)\), so the ideal minimizer matches the target distribution. This does not remove finite-sample, optimization, misspecification or distribution-shift problems. [Proper scoring rules](https://doi.org/10.1198/016214506000001437) and [calibration research](https://proceedings.mlr.press/v70/guo17a.html) provide the conceptual background.

RLCD may be useful, but “reinforcement learning” is not a prerequisite for probabilistic output. Compare objectives while holding data, backbone, budget and protocol fixed before crediting a training acronym. If only the chosen action receives feedback, or downstream sequential outcomes matter, supervised classification alone no longer describes the learning problem.

Separate three changes that can each improve a system:

1. Better evidence: retrieve the right policy and compute deterministic quantities.
2. Better boundaries: train on minimal meaningful changes, exceptions and insufficient evidence.
3. Better decision policy: select thresholds and handoff rules using observed costs and risk.

Test these as ablations rather than swapping the entire system at once.

## 4. A small but informative evaluation

Freeze a task definition and a representative held-out set before repeated tuning. Split by customer/source/time where appropriate, not just random paraphrase rows. Keep model training, calibration and final testing separate. An operational benchmark should contain easy, boundary, ambiguous, missing-evidence and deliberately misleading cases; it should also contain the common cases that dominate actual volume.

Start with three candidates: a simple baseline, a managed reference when permitted, and one locally trainable model. Add CLM only for a real candidate-selection bottleneck and add small encoders when latency or deployment constraints matter. Record the same evidence, allowed actions and errors for every run.

Use a scorecard such as:

| Question | Measurement |
| --- | --- |
| Does it judge the task correctly? | Task metric plus important false-positive/false-negative categories |
| Can high-risk cases be identified? | Risk–coverage curve, accepted-set errors and their uncertainty |
| Are the numbers meaningful? | NLL/Brier and calibration, with explicit definitions |
| Does it generalize? | Held-out source/time/language and relevant subgroups |
| Is it economical? | Full-system p50/p95 latency and outcome cost, including review |
| Can a result be traced? | Input provenance, rules, model revision, decision and observed outcome |

Do not select a threshold by repeatedly looking at the final test set. Low observed error on a small sample is not proof of low production risk. Guarantees from [conformal risk control](https://arxiv.org/abs/2208.02814v4) or its [2026 extension](https://arxiv.org/abs/2602.20151v1) must be matched to the actual loss and assumptions.

## 5. Deploy the decision, not just the model

Keep the loop small:

**Evidence → deterministic checks → semantic judgment → policy/risk gate → verified outcome.**

The gate may request evidence, spend more computation, use another executor or abstain. Log automatically accepted cases as well as escalations, and audit a sample of both. Otherwise, the most confidently wrong cases can remain invisible.

Maintain rollback, versioned rules, outcome maturation windows and privacy-aware logging. A new model's shadow evaluation should not silently change the live acceptance threshold. Human review has cost, delay and error; measure it rather than assuming it solves all uncertainty.

## 中文：一页决策建议

**先定义判断契约。** 输入证据是什么、输出有哪些、怎样才算正确、错判代价是多少、证据不够怎么办。判断“是什么”、预测“谁能做”、学习“怎样能改善结果”，需要的标签和方法不同。

**按任务挑候选，不按热度挑模型。** 少量复杂选项可试 Kev／Nimble，并以 Jev 作托管对照；稳定的标签先试普通分类器或 SetFit；候选多而可复用时试 CLM；窄域高频分类再比较 Laya 与 GLiNER2.5-Decide；执行者分工则需要真实执行记录。以上是实验顺序，不是声称已经测出赢家。

**先测证据和数据，再争论训练缩写。** 日期与算术由代码完成；训练集覆盖边界、否定、例外、缺失证据和无关改写。固定基础模型、数据和预算后，才知道 RLCD、对比学习或更大的模型究竟带来了多少增益。

**验收完整系统。** 主要目标是在可接受风险下自动完成的比例及总交付成本。训练、校准和最终测试分开；按来源、客户或时间留出；同时记录延迟、人工复核、失败重试与错误修正。抽检自动放行案例，避免只学到“已转人工”的那部分世界。

**不急于构建一个无所不能的领域大脑。** 一个稳定、可验证的判断节点，比一套无法确认效用的宏大架构更有积累价值。先跑通证据、判断、升级和验收，再根据测量结果扩展。
