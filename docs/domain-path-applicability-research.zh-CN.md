# 领域对话：路径适用性、信息缺口与优先关系

审阅日期：2026-11-17。[业务实验入口](dynamic-skill-loading-business-playbook.zh-CN.md) · [应用证据](decision-model-application-evidence.zh-CN.md) · [方法](methodology.md)

## 问题与结论

给定客户当前诉求、相关对话、已确认业务状态和候选路径的适用条件，判断哪些路径可以继续、哪些缺信息、哪些存在矛盾，以及多条路径相关时先处理什么。

类Jev模型最值得验证的职责是**基于证据的语义条件判定**：客户是否表达某种诉求、某个自然语言条件是否得到支持。状态读取、精确计算、条件组合、优先关系和动作执行保留明确的业务合同。路径相关、满足执行条件和实际完成是三个不同结果。

这是本分支“当前业务状态下应保持、切换还是澄清”的具体研究入口。先在固定候选与执行器下比较判断器；确认必要能力遗漏确实是瓶颈后，才进入动态技能加载实验。本文提供来源核查与设计建议，未实现runtime、调用模型或验证业务收益。

## 先读的三个直接参考

### 1. TypeSafe客服workflow：共享状态、条件判断与有序规则

[Customer Service workflow](https://evals.typesafe.ai/customer_service)输入双方对话、客户记录、账户状态和待确认方案；先并行读出诉求、情绪与风险，再按需要补充consent、fraud、money、retention判断，意图接近时另做tie-break，最后按章节顺序组合动作。输出可以包含多个动作，也可以没有动作。

[2026-11-03官方设计文章](https://typesafe.ai/blog/dont-call-it-a-decision-model)进一步区分语言判断与代码事实：退款请求、未授权活动等由模型判断，金额比较、账户字段和路径顺序由代码处理。值得借鉴的是判定与组合的边界，并非照抄其示例业务政策或阈值。

**证据边界**：[官方评估方法](https://evals.typesafe.ai/)假设harness正确，以强模型输出共识作为参考；这是产品方流程示例与评测，不是人工业务真值、独立复现或线上收益证明。

### 2. Parlant：已经接入Jev的批量规则判断

本次核查`develop`提交`687044f61ab5d8e70d3bbeddcd918ca190d35da9`（2026-11-16）。[TurnEvaluator契约](https://github.com/emcie-co/parlant/blob/687044f61ab5d8e70d3bbeddcd918ca190d35da9/src/parlant/core/engines/compass/matching/rule_evaluation.py)区分会话候选发现与当前回合判定；[RuleRanker](https://github.com/emcie-co/parlant/blob/687044f61ab5d8e70d3bbeddcd918ca190d35da9/src/parlant/core/engines/compass/matching/rule_ranker.py#L228)把共享对话上下文作为state、每条规则作为一个Proposition，批量请求后按概率筛选。[OpenRouter适配器](https://github.com/emcie-co/parlant/blob/687044f61ab5d8e70d3bbeddcd918ca190d35da9/src/parlant/adapters/nlp/openrouter_service.py#L1070)注册decision capability，默认`~typesafe/jev-latest`。

**必须保留的限制**：这是first-pass filter，提示拿不准时偏向yes，相关性阈值为0.5；目标是减少漏掉重要规则，不能把该阈值当作业务执行资格门槛。源码称概率calibrated不等于本仓已验证领域校准。commit固定代码文本，不固定实际响应的模型版本或权重。

[政策文档](https://www.parlant.io/docs/customizing-behavior/policies/)提供pairwise priority、entailment、dependency和工具后reevaluation。当前policy从`content`判断适用，只有observation有独立condition，不能套用旧版接口。[Adaptive effort](https://www.parlant.io/docs/customizing-behavior/adaptive-effort/)说明decision model如何让较低effort批量检查更多规则。

优先和依赖关系仍需业务作者定义；历史规则曾matched不等于前序动作成功。多条规则有关系，也不证明系统能自动发现任意事实矛盾或推导正确的业务优先级。

### 3. ShARC / EMT / MUDERN：条件未知时应补问什么

[ShARC（EMNLP 2018）](https://aclanthology.org/D18-1233/)的问题形式是规则文本、用户场景、初始问题和对话历史，输出Yes / No / Irrelevant或追问。[Explicit Memory Tracker（ACL 2020）](https://aclanthology.org/2020.acl-main.88/)显式跟踪逐条件的Entailed / Contradicted / Unknown，再决定回答还是补问；[作者代码](https://github.com/Yifan-Gao/explicit_memory_tracker)可供检查。

[MUDERN / OR-ShARC（2021）](https://arxiv.org/abs/2102.08633)加入从规则库召回多篇候选、条件分割和多篇蕴含判断；[作者项目](https://github.com/Yifan-Gao/open_retrieval_conversational_machine_reading)提供数据与实现。适合借鉴候选召回、条件判定和澄清的拆分，不应把旧英文资格问答结果外推到中文客服或动作优先调度。

尤其应区分：**条件被反证**是该条件不成立；**证据冲突**是两个来源或两段陈述彼此矛盾。后者不能直接用EMT的Contradicted标签代替。

## 补充参考：只在相应缺口存在时使用

| 缺口 | 参考与可借鉴部分 | 限制 |
|---|---|---|
| 路径入口、槽位与中断恢复 | [Rasa CALM flows](https://rasa.com/docs/reference/primitives/flows)的description、flow guards、collect、分支；[patterns](https://rasa.com/docs/reference/primitives/patterns)处理澄清、改口、中断等 | 是完整框架，不是自动给所有路径输出已校准分数的小模型 |
| 多条条件同时命中 | [Camunda DMN hit policy](https://docs.camunda.io/docs/components/modeler/dmn/decision-table-hit-policy/)的Unique、Any、First、Rule Order、Collect | Unique多命中会失败，不是自动选第一条；不负责自然语言证据理解 |
| 资格、相关性与优先仲裁混在一起 | [Pega Next-Best-Action](https://academy.pega.com/topic/next-best-action-designer/v2/in/90801/90816)区分eligibility、applicability、suitability与arbitration | 借鉴领域分层，不因此引入整套商业平台；未验证其对本任务的效果 |
| 本地typed-decision基线 | [AnyJev](https://github.com/nokia-applied-research/AnyJev)与[levels契约](https://github.com/nokia-applied-research/AnyJev/blob/main/docs/levels.md) | 当前0.3.0的L0不按标签校准置信度，可花多次prefill；L1/L2留在0.2.0，不能照旧介绍当前API |
| 便宜的诉求/多标签基线 | [GLiClass](https://github.com/Knowledgator/GLiClass) | 分类能力不等于完整规则执行、缺口定位或冲突解析 |

完整任务验收继续参考[已有研究补充中的τ-bench](dynamic-skill-loading-research-supplement.zh-CN.md)。[Entagl回放](https://www.entagl.com/blog/typesafe-jev-benchmark-ai-decision-models)中缺少当前会话owner导致误路由的反例，已记录在[应用证据](decision-model-application-evidence.zh-CN.md)；不再用同一来源重复制造新性能记录。

## 近期研究改变了哪些判断

| 来源日期／原始资料 | 核查到的报告 | 对本任务的有限启示 |
|---|---|---|
| 2026-11-16，[*Small Heads, Strong Decisions* v3](https://arxiv.org/html/2611.15592v3) | 同底座、数据和训练协议比较五种readout；该实验中复杂head未带来明显准确率收益，底座规模影响更大 | 先做好任务、证据和简单强基线；不是所有领域都已证明head无关 |
| 2026-11-08，[*Beyond Ranking* v1](https://arxiv.org/html/2611.11480v1) | 检索相关性原生概率过度自信，独立数据拟合校准后改善；本仓已有[11月13日审阅](../updates/2026-11-13-jev-utility.md) | 路径相关性的概率仍需目标域校准；检索实验数字不能搬成业务资格正确率 |
| 2026-10-18，[*What Can’t Jev Decide?* v1](https://arxiv.org/html/2610.24929v1) | 读取记录与组合多次状态更新表现不同；过期摘要可导致模型高置信地沿用错误状态 | 显式维护状态并测过期输入；所测Jev1.13及开放模型快照不是所有未来型号的能力上限 |
| 2026-10-17，[*Native Probability Outputs for Clinical Triage*](https://arxiv.org/abs/2610.24692) | 概率误差较低与识别必要澄清并不同步；独立问信息充分性增加召回，也增加无必要澄清 | 单独验收“该不该问”；这里只借鉴任务设计，不作医疗应用外推 |
| 2026-07-24，[*One More Turn, Less Regret* v2](https://arxiv.org/abs/2607.21143) | 将是否问、问什么、何时停止视为多轮澄清策略，计入交互成本与无效澄清 | 不能只测最后答对率；原实验是开放问答与推荐，非业务执行路径 |

这些是作者报告的研究结果。核查范围包括摘要、元数据、相关正文方法/结果段和上述源码；未全面审计论文数据、训练权重与逐样本产物。临床分诊与RegretBench本轮只核摘要及元数据，不导入性能数字。没有新增`reproduced_here`记录，也没有据此改变模型榜单或宣布生产收益。

## 最小判定合同（编者建议，尚未实施）

输入应包含：当前目标、相关对话片段、已确认字段及来源/时间、未知字段、当前活动路径、已完成动作；候选路径应声明适用/排除条件、必要事实、前置动作、互斥与优先关系。系统记录、客户陈述和模型推断分开，`unknown`不能默认为false。

```text
当前证据 + 候选路径条件
  -> 逐条件判断：supported / refuted / unknown / conflicting_evidence
  -> 按路径合同组合：适用 / 不适用 / 待补信息 / 待核实
  -> 对适用集合处理优先、依赖与互斥
  -> 继续 / 查询状态 / 补问 / 交人工
```

四状态是本文提出的领域合同，并非Jev原生保证。可以用每条件一个Choice表达；可精确计算的条件由代码直接判断。若需证据引用或missing fact ids，优先由现有证据ID与条件→事实键映射提供，不假定不生成文本的模型能直接写任意解释与问题。

需要分别保留：

- **条件状态**与**模型不确定性**：信息不足是被判断的业务状态，不是概率接近0.5的同义词；模型也可能高置信地判为unknown。
- **相关性**与**执行适用性**：退款话题相关，不表示身份、订单、退款状态和授权条件已满足。不要用条件平均分抵消硬性排除。
- **多条适用**与**冲突**：两条流程可顺序或并行处理；只有互斥动作、矛盾指令或不一致事实才需要相应消解。
- **优先级**与**概率**：按已冻结的业务依赖/优先约束仲裁，在允许范围内遵循客户明确顺序；概率高不表示客户收益大，也不表示应先执行。

Jev官方[Introduction](https://docs.typesafe.ai/introduction)说明同次请求的各问题针对同一state独立评估；依赖另一答案的判断须先在代码组合或下一次请求，不能假设同批答案互相可见。[Companion Noul](https://docs.typesafe.ai/patterns/companion-noul)提供“哪个最像”与“是否有任何一个适用”分开询问的模式；[confidence文档](https://docs.typesafe.ai/confidence)说明置信字段是分布统计量，不提供额外独立证据。

补问只针对可能改变当前可选路径的必要事实；系统能查的先查。某路径已有确定排除条件时，不为它补齐无关字段。来源冲突先按来源权威性和新鲜度核实，不要求模型自行猜一个业务真值。

## 如何接入原实验

1. 选一个现有有界业务问题，冻结路径、状态口径与可接受结果。先测固定候选，不同时改变状态提取、判断器和加载策略。
2. 比较现用LLM结构化输出、规则/合适的轻量分类或NLI基线、至多两个Jev类候选；各组看到相同证据，使用同一确定性条件组合。保留整体判断基线，不预设语义问题拆得越细越准。
3. 独立标注条件状态、路径集合、必要补问与可接受优先关系。覆盖否定/假设、改口、多诉求、无适用路径、缺信息、事实冲突、状态过期、工具返回后资格变化；按案件、规则族和时间划分。
4. 分别测逐条件/路径错误、关键错误放行、缺口/冲突召回、优先关系违规、冗余补问、含回退的总成本与p95。并行模型问答不等于总调用数或端到端延迟固定。
5. 若该判断环节有净价值，再按[原playbook的阶段B](dynamic-skill-loading-business-playbook.zh-CN.md)比较技能暴露与补载；完整任务成功及业务收益另行验收。第一轮交付可以是瓶颈诊断和停止决定，无需先搭建新平台。

## English orientation

This source review narrows the branch's state-dependent keep/switch/clarify question into per-condition evidence judgments, path applicability, missing facts and explicit precedence. Parlant's inspected develop snapshot already batches Jev rule-relevance checks, but its recall-oriented first-pass filter is not execution eligibility. ShARC/EMT/MUDERN inform condition tracking and clarification; DMN and Rasa inform explicit rule/flow semantics. The proposed four-state contract and experiment are unimplemented. No model inference, independent reproduction or business uplift is claimed.
