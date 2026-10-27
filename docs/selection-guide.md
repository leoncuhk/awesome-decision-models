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

## 6. October 2026 deployment checks / 10 月部署验收

The newer releases add distinct experiments; they do not replace task-specific acceptance. See [Decision 3.0](models.md#decision3), [Intern-Decision](models.md#intern-decision), [Verdict](models.md#verdict) and the [deployment evidence](evidence.md#e15).

| Decision constraint | Concrete experiment | Acceptance boundary |
| --- | --- | --- |
| Many questions about one state | Compare Decision 3.0's separate question rows with Intern-Decision's shared causal schema skeleton and a hosted reference | Measure total tokens, memory, p50/p95 and field/order effects. One HTTP call, one prompt row and one backbone pass are different units. |
| Private text/image/video processing on Apple devices | Test the exact FluidUse/Core ML package against its upstream renderer on the same labeled inputs | Match precision, length bucket, image/video path, near-tie decisions, cold start and concurrent queue. Conversion parity does not certify task accuracy. |
| Missing correct option or incomplete evidence | Test explicit abstention alongside external evidence checks and risk–coverage thresholds | Include hard-negative options, synonyms, missing images and mixed in/out-of-scope traffic. Verdict's negative findings in [E20](evidence.md#e20) rule out trusting a named abstention option alone. |
| Probability-based automation | Evaluate the deployed renderer and calibrator on separate calibration and final test splits | A published temperature may be size/backend/candidate-count specific. [E19](evidence.md#e19) shows an evaluator and serving path yielding different calibration. |
| Tool or team routing with preprocessing rules | Freeze the whole pipeline, then score rules and model calls separately | Count bypassed-model failures, retries and human clarification. [E17](evidence.md#e17) illustrates how a helpful rule can become the dominant error source. |

中文：新增型号扩大可测试的方案空间。验收必须固定模型／转换包、schema、规则、校准器和完整测量边界；“多题一次调用”不意味着每种模型都只编码一次。公共 Index、231-task JevBench、业务标签一致率、转换等价和吞吐演示分别回答不同问题，不能相互代替。先以影子评测验证关键错误、校准、拒答和总成本，再决定是否上线。

<a id="image-intent-adaptation"></a>

## 7. Image intent and domain adaptation / 图片意图与领域适配

Current implementation plan: [Mac small-data route](multimodal-decision-finetuning.md#mac-implementation), with conditional capacity, matched baselines, cost/risk acceptance and research gates. / 当前实施方案：[Mac 小样本路线](multimodal-decision-finetuning.zh-CN.md#mac-implementation)，统一条件容量、同条件基线、成本／风险验收及科研门槛。

[2026-10-26 training-support audit](../updates/2026-10-26-multimodal-training-and-evidence.md#trainability) distinguishes image-supervised Qwen/Intern paths, experimental Clef, verified inference paths for D3-Turbo/Decider and mlx-decision media rejection. The same update specifies learned judgment versus changing facts and frozen acceptance. / [10 月 26 日训练支持核验](../updates/2026-10-26-multimodal-training-and-evidence.md#trainability)分开图像监督 Qwen／Intern、实验 Clef、仅确证推理的 D3-Turbo／Decider 与拒收媒体训练的 mlx-decision，并给出学习判断、变化事实与冻结验收的合同。

This is a proposed evaluation workflow, not a validated deployment or a customer case. Image content and conversational intent are different labels. The same payment screenshot may accompany a receipt submission, a status question or a complaint. Define intent from the image **and only the text/context available at decision time**. Keep visible facts, inferred intent and allowable action as separate outputs. Support multiple intents, unknown and targeted clarification when evidence cannot identify the request.

以下是通用评测建议，并非已验证部署或任何客户案例。图像内容不等于会话意图；同一张付款截图可能用于提交凭证、询问进度或投诉。输入应包含图像和判断时已经存在的文本上下文。把可见事实、推断意图和可执行动作分开，允许多意图、未知和有针对性的澄清。

| Stage / 阶段 | Concrete experiment / 实验 | Acceptance boundary / 验收边界 |
| --- | --- | --- |
| Define labels / 定义标签 | Specify user goal, evidence span, ambiguity policy and error cost; independently adjudicate disagreements. / 定义诉求、证据范围、歧义规则及错判代价，独立裁定标注分歧。 | Later resolution can help construct labels, but future messages/agent replies cannot enter an earlier model input. / 后续结果可辅助制标签，但未来消息／客服回复不能泄漏到早先判断的输入。 |
| Freeze the domain test / 固定领域测试 | Compare text-only, OCR+text classifier/rules, an instruction VLM and a multimodal decision model on identical labels/evidence. / 统一标签与证据，比较纯文本、OCR+文本分类／规则、指令 VLM 和多模态判断模型。 | Include same image with different contexts, image-only ambiguity, missing/wrong images, small text, crops and new layouts. OCR may lose visual relationships. / 包含同图异上下文、仅图歧义、缺图／错图、小字、裁剪和新布局；OCR 可能丢失视觉关系。 |
| Diagnose before training / 先归因再训练 | Improve context, OCR, label definitions or deterministic extraction first; measure macro-F1, costly confusions, unknown/clarification coverage and total latency. / 先改善上下文、OCR、标签或确定性提取；测宏F1、关键混淆、未知／澄清覆盖和总延迟。 | Closed-set accuracy may conceal confident forced choices; measure risk–coverage and clarification burden separately. / 闭集准确率可能掩盖强制猜测，风险—覆盖和澄清负担须单测。 |
| Adapt with verified support / 核验支持后适配 | With adjudicated target examples, compare a supervised text classifier, VLM SFT/parameter-efficient adaptation and a distilled smaller student. / 有裁定样本后，比较监督文本分类、VLM SFT／参数高效适配和小模型蒸馏。 | Check exact backbone/readout, image processor, loss/masking, trainable modules, dependency versions, memory, export and serving adapter. A generic text ModernBERT/LoRA recipe does not certify D3 multimodal training. / 核对骨干／读出、图像处理、损失掩码、训练模块、依赖版本、内存、导出和服务适配；文本 ModernBERT／LoRA 配方不等于 D3 多模态支持。 |
| Freeze calibration / 冻结校准 | Split by conversation, source and time; group near-duplicate images and template variants. Fit calibration separately, then freeze before final test. / 按会话、来源和时间划分，图像近重复与模板变体分组；独立校准后冻结最终测试。 | Preserve minority-intent/shift tests. Audit teacher labels and soft probabilities; distillation does not make teacher errors correct. / 保留少数意图和漂移检查；抽检教师标签及软概率，蒸馏不会使教师错误变正确。 |
| Gate actions / 权限隔离 | Predict intent or clarify; authenticated policy controls consequential actions such as refunds and account changes. / 模型识别意图或澄清；退款、账户变更等动作交由身份与策略规则。 | Confidence is not authorization; a screenshot does not establish permission. / 置信度不是授权，截图不能证明动作权限。 |

The [native D3 integration report](https://github.com/vllm-project/vllm/pull/61565) explicitly leaves LoRA unmeasured. [TRL's generic VLM/PEFT documentation](https://huggingface.co/docs/trl/en/sft_trainer) is a starting reference for supported generative models, not evidence that D3's custom noncausal readout has a working multimodal training/export recipe. Keep that support unknown until the exact path is verified. No private images were collected or uploaded for this guide.

[原生 D3 集成报告](https://github.com/vllm-project/vllm/pull/61565)明确未测 LoRA；[TRL 通用 VLM／PEFT 文档](https://huggingface.co/docs/trl/en/sft_trainer)仅可作为受支持生成模型的参考，不能证明 D3 的定制双向注意力读出已有可用的多模态训练／导出配方。具体路径核验前保留未知。本指南未收集或上传私人图片。

The official D3 wrapper restriction does not exclude a separate trainer. [Vis Decisions](https://github.com/Blockether/vis-decisions/blob/d73768e3c18d89d11f6b9a774b87d64ccd55f27d/src/blockether/vis_decisions/_d3_trainer.py) implements text-only full/LoRA adaptation with a trainable readout and merged export; it removes the vision tower and therefore does not verify image fine-tuning. Qwen3.5/VLM SFT or LoRA is an experimental baseline, not a demonstrated quality winner over D3; the reviewed sources do not establish a matched task/data/scale/budget multimodal comparison. B2/B3 must hold the exact base checkpoint fixed to isolate readout effects.

官方 D3 封装的限制不排除独立训练器。[Vis Decisions](https://github.com/Blockether/vis-decisions/blob/d73768e3c18d89d11f6b9a774b87d64ccd55f27d/src/blockether/vis_decisions/_d3_trainer.py)实现文本 full／LoRA 适配、可训练读出及合并导出，但去掉视觉塔，不能据此确证图片微调。Qwen3.5／VLM 的 SFT 或 LoRA 是实验基线，并非已证明效果胜过 D3；已阅来源未确立同任务／数据／规模／预算的多模态对照。B2／B3 需固定精确底座，才能归因读出收益。

The [one-page route](multimodal-decision-finetuning.md#quick-route) and [layered reading list](multimodal-decision-finetuning.md#reading-list) turn this into experiment gates, separating peer-reviewed methods, preprints and engineering. / [一页路线](multimodal-decision-finetuning.zh-CN.md#quick-route)及[分层阅读](multimodal-decision-finetuning.zh-CN.md#reading-list)给出实验关卡，分开同行评议、预印本与工程证据。

The [MIRE case](mire-case-study.md#finalists) separates final prizes from online F1 and traces three method families. / [MIRE案例](mire-case-study.zh-CN.md#finalists)分开最终奖项与线上F1，并追溯三类参赛方法。

Execution details: [grouped splits](multimodal-decision-finetuning.md#split-protocol), [minimal matrix](multimodal-decision-finetuning.md#experiment-matrix), [result template](multimodal-decision-finetuning.md#result-template). / 执行细节：[防泄漏划分](multimodal-decision-finetuning.zh-CN.md#split-protocol)、[最小矩阵](multimodal-decision-finetuning.zh-CN.md#experiment-matrix)、[结果模板](multimodal-decision-finetuning.zh-CN.md#result-template)。

For a complete proposed experiment, see the [multimodal fine-tuning research plan](multimodal-decision-finetuning.md): matched B0–B3 arms, actual image-path checks, candidate versus full-vocabulary loss, grouped splits, distillation, export and risk/cost stopping rules. [E28](evidence.md#e28) keeps the MIRE/EcomMIR competition results separate from decision-model leaderboards.

完整实验设计见[多模态微调研究方案](multimodal-decision-finetuning.zh-CN.md)：同条件 B0–B3 对照、真实图像路径检查、候选／完整词表损失、分组划分、蒸馏、导出及风险／成本停止条件；[E28](evidence.md#e28)单独保存 MIRE／EcomMIR 竞赛结果，不混入判断模型总榜。

<a id="semantic-feature-prediction"></a>
## 8. Semantic judgment, features and prediction / 语义判断、特征与预测

The [financial-document comparison](evidence.md#e24) separates reading a reported fact, reproducing a public taxonomy and forecasting later institutional action. They require different labels and validation. Another useful arm is the [semantic-feature pipeline](evidence.md#e27): freeze evidence-grounded judgments, then train a supervised predictor alongside TF-IDF/embeddings/structural features. Run question/schema discovery inside development folds; freeze it before final testing and include extraction cost. A wine-score result does not demonstrate financial returns or transfer to image intent.

[财务文档对照](evidence.md#e24)将读取已报告事实、复现公共分类标签、预测后续机构行为分开，不能以一种任务代替另一种。也可把[语义判断作为特征](evidence.md#e27)，与 TF-IDF／嵌入／结构特征并排训练监督预测器；问题和 schema 搜索只能发生在开发划分，最终测试前冻结并计入提取成本。葡萄酒评分结果不能证明金融收益或图片意图泛化。

<a id="adaptive-reasoning"></a>
## 9. Read or think / 一次判断还是按需推理

The [mechanism comparison](decision-readout-and-reasoning.md) separates option-letter readouts, dedicated code heads and hosted unknowns. Compare StartLux Instant with AutoThink only after freezing evidence, gate, mixture, candidate reduction and backend; a gate is a compute policy, not a risk certificate. For a generic support image with missing conversational context, clarify or retrieve rather than expecting a longer thought to invent the evidence. Exact dates/arithmetic retain deterministic-tool baselines. Fit calibration on the actual returned selection/routing policy and include thought generation, rereads, queueing and failures in cost. StartLux weights require separate commercial authorization.

[机制比较](decision-readout-and-reasoning.md)分开选项字母读出、独立答码头和托管未知实现。比较 StartLux Instant／AutoThink 前冻结证据、门槛、混合、候选归约与后端；门槛是计算策略，不是风险认证。通用客服图像缺会话上下文时应澄清或取证，不能期待长推理补造证据；日期／算术保留确定性工具基线。按实际选择／路由输出校准，并把推理生成、再读、排队与失败计入总成本；StartLux 权重商用需另获授权。

## 中文：一页决策建议

**先定义判断契约。** 输入证据是什么、输出有哪些、怎样才算正确、错判代价是多少、证据不够怎么办。判断“是什么”、预测“谁能做”、学习“怎样能改善结果”，需要的标签和方法不同。

**按任务挑候选，不按热度挑模型。** 少量复杂选项可试 Kev／Nimble，并以 Jev 作托管对照；稳定的标签先试普通分类器或 SetFit；候选多而可复用时试 CLM；窄域高频分类再比较 Laya 与 GLiNER2.5-Decide；执行者分工则需要真实执行记录。以上是实验顺序，不是声称已经测出赢家。

**先测证据和数据，再争论训练缩写。** 日期与算术由代码完成；训练集覆盖边界、否定、例外、缺失证据和无关改写。固定基础模型、数据和预算后，才知道 RLCD、对比学习或更大的模型究竟带来了多少增益。

**验收完整系统。** 主要目标是在可接受风险下自动完成的比例及总交付成本。训练、校准和最终测试分开；按来源、客户或时间留出；同时记录延迟、人工复核、失败重试与错误修正。抽检自动放行案例，避免只学到“已转人工”的那部分世界。

**不急于构建一个无所不能的领域大脑。** 一个稳定、可验证的判断节点，比一套无法确认效用的宏大架构更有积累价值。先跑通证据、判断、升级和验收，再根据测量结果扩展。


<a id="decision-index-protocols"></a>
## Decision Index protocols / 同名指数的协议边界

| Publisher / 发布者 | Reviewed scope / 所核范围 | Interpretation / 解读 |
| --- | --- | --- |
| [HF-hosted community Decision Index](https://huggingface.co/spaces/multimodalart/jev-decision-index), archived 0.2/0.3.2 and reviewed 0.4 methodology | Text and visual tracks; public/private coverage and versioned chance-correction/aggregation; public-only 37-task reports are subsets. / 文本、视觉分轨，公开／私有覆盖及版本化机会校正／聚合；仅公共 37 任务是子集。 | Keep track, scoring version, date and tie band with every score. / 每个成绩保留分轨、评分版本、日期与平局带。 |
| [Artificial Analysis Decision Index](https://artificialanalysis.ai/methodology/decision-index), methodology 1.0 | Four equal 25% parts: private 500-item knowledge set, 513 text HLE MCQs, When2Call, filtered 835-row WildGuardTest. / 四等权部分：私有 500 题知识集、513 道文本 HLE 选择题、When2Call、筛选后 835 行 WildGuardTest。 | Different publisher/tasks/aggregation; no score/rank imported here. / 发布者、任务及聚合均不同，本轮不引入排名／成绩。 |

AA knowledge scoring splits its weight between accuracy and non-hallucination; the latter is `100 * (1 - wrong/(wrong + IDK))`, so its denominator excludes correct answers. WildGuard averages three F1 scores. Neither composite substitutes for policy-conditioned calibration, image-specific acceptance or full-service p95. A single API call containing multiple questions does not establish a single shared model forward pass. Private items and raw runs remain unaudited.

AA 知识部分将权重平分给准确率与非幻觉率；后者为 `100 * (1 - wrong/(wrong + IDK))`，分母不含答对项。WildGuard 平均三个 F1。两个总分都不能代替实际策略校准、图像专项验收或完整服务 p95；一次多题 API 调用不证明模型一次共享前向。私有题与原始运行仍未审计。

## Risk-budgeted policy / 风险预算策略

The Oct14 [risk-budgeted System One preprint](https://arxiv.org/html/2610.19811v1) studies binary policies: score `s(X)` predicts a positive event, Action 0 on `s(X) < tau` has `FOR = P(Y=1 | s(X)<tau)`, and Action 1 is the conservative fallback. Its fixed-sequence LTT result requires a frozen scorer/ordered threshold family derived from Fit independently of iid Cal from the same deployment population. With error level delta, the probability over calibration samples of certifying a population-risk-violating policy is bounded by delta. This is not each answer's probability of correctness, a promise that every finite test estimate stays below budget, or an automatic multiclass/image/shift guarantee. No certificate means fallback for the policy, distinct from per-input abstention. Six English-text datasets/single seed are author evidence; no local replication or numeric gain is claimed.

10 月 14 日的[风险预算 System One 预印本](https://arxiv.org/html/2610.19811v1)研究二元策略：`s(X)` 预测正事件，`s(X) < tau` 区域执行 Action 0，风险为 `FOR = P(Y=1 | s(X)<tau)`，其余执行保守回退 Action 1。固定序列 LTT 要求评分器与有序阈值族由 Fit 冻结，并与来自部署同一总体的 iid Cal 独立；以 delta 为错误水平时，对校准集抽样而言，认证出总体风险超预算策略的概率不超过 delta。这不是逐题正确率、每次有限测试估计必不超预算，也不自动覆盖多类／图像／漂移。无证书意味着策略回退，区别于单输入拒答。六个英文文本集／单种子属于作者证据，本轮未复现或引入数值增益。


The [October25 methodology review](../updates/2026-10-25-weekly-review.md) separates **text0.4 Full** (private same-skill/new-domain60/40, public-scale mapping; revised hidden domain set) from **vision Full** (public/private same-skill50/50). Public0.3 remains a visible diagnostic, with zero text-Full weight. Score changes across editions are not model improvements; old fixed-source records remain even when live archival files disappear.

10 月25日核查：文本0.4 Full 为纯私有同技能／新领域60／40（映射到公共尺度，隐藏新领域集合也已修订）；视觉 Full 仍为公共／私有同技能50／50。公共0.3 仍展示，但不计文本 Full。跨版分数变化不等于模型提升，上游移除在线旧文件后仍保留本库固定来源。

For acceptance policies, [E34](evidence.md#e34) shows opposite false-commitment/false-abstention errors on constructed legal inputs; [E35](evidence.md#e35) shows that lower ECE can leave error ranking unchanged. Specify missing-evidence cases, the cost of unnecessary review and calibration selection before testing. Neither result transfers automatically to screenshot intent or new traffic.

验收策略应同时看 [E34](evidence.md#e34) 的错误承诺／误拒答及 [E35](evidence.md#e35) 的“ECE降低而错误排序不变”。测试前写清缺证据样本、不必要复核成本与校准选择，不能直接迁移为截图意图或新流量的保证。
