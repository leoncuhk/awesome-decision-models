# 领域对话：路径适用性、信息缺口与优先关系

> 页面角色：本页维护领域决策问题和标签语义；当前后训练候选与证据门槛见[总览](decision-model-posttraining-enterprise.zh-CN.md)，全量导航见[文档地图](README.md)。

审阅日期：2026-11-17。[业务实验入口](dynamic-skill-loading-business-playbook.zh-CN.md) · [应用证据](decision-model-application-evidence.zh-CN.md) · [方法](methodology.md)

2026-11-19实现复核：[Parlant、Modem、Entagl源码与保留审查](customer-service-implementation-review.zh-CN.md)区分实际可读源码、产品契约和历史回放；新增Parlant源码pin及协议边界观察。下文11月17日固定来源保留原时点。

2026-11-19后训练研究：[企业后训练总览](decision-model-posttraining-enterprise.zh-CN.md)统筹方法、可训练底座、企业数据与生产验收；引用材料的[方法核查](decision-model-posttraining-method-audit.zh-CN.md)和[平台核查](decision-model-posttraining-platform-audit.zh-CN.md)分别保留版本、数字口径及适用条件。当前没有本次企业项目数据，未开始该企业训练或验证生产收益。

## 问题与结论

**当前问题：面对客户当前诉求和已确认事实，哪些业务处理路径适用，信息是否足够，多条路径相关时先处理哪条？**

输入是当前诉求、相关对话、已确认状态，以及候选路径的适用/排除条件和已定义的关系。输出至少分开四项：

| 输出 | 要回答的问题 |
|---|---|
| 路径适用性 | 哪些路径满足条件，哪些应排除？必要条件分别得到什么证据支持？ |
| 信息充分性 | 哪些必要事实未知，应查系统还是补问客户？ |
| 冲突 | 是来源事实相互矛盾、路径动作互斥，还是业务指令冲突？ |
| 优先关系 | 哪些可并行，哪些依赖前序步骤，哪些按业务政策或客户意愿暂缓？ |

类Jev模型最值得验证的职责是**基于证据的语义条件判定**：客户是否表达某种诉求、某个自然语言条件是否得到支持。状态读取、精确计算、条件组合、优先关系和动作执行保留明确的业务合同。路径相关、满足执行条件和实际完成是三个不同结果。

**Decision model是实现候选，动态技能加载是可能的上下文策略；二者都不是预设结论。** 先在固定状态、候选、政策与执行器下验证这些输出，再决定是否替换判断器；只有必要技能遗漏/无关正文干扰确实影响结果时，才进入加载策略实验。本文提供来源核查与设计建议，未实现runtime、调用模型或验证业务收益。

## 资料与问题的对应范围

以下是按当前问题的贴合程度整理的阅读顺序，不是模型性能排名。

| 层次／资料 | 对应哪一部分 | 没有覆盖或尚未证明什么 |
|---|---|---|
| 直接工程参考：Parlant | 每轮规则相关性、显式优先/依赖、工具后重新判断 | 首轮相关性过滤不是执行资格；未证明任意事实冲突或业务优先级可自动推导 |
| 直接方法参考：ShARC / EMT / MUDERN | 逐条件支持/反证/未知、必要追问、多篇规则检索 | 主要是资格问答；没有完整验证多业务路径的优先调度和执行 |
| 部分对应、用于验收：SOPBench | 执行前条件、动作允许性、检查过程、终态 | 主要覆盖执行前资格，动态分支和主观条件有限；它不是专用判断模型 |
| 判定器实现参考：Jev / Koa-decision | 给定问题与候选答案的快速语义判断 | 不定义企业条件、信息缺口或优先政策；路由准确率不证明四项输出均正确 |
| 相邻方法：KADS | 检索程序文档辅助动作预测 | 未确认直接生产采用或持续维护实现，降为历史方法参考 |
| 表示与压力测试：FlowBench / ToolSandbox / DialFork | 流程表示、缺信息/工具、状态依赖、偏离检测 | 测试方法不能当作Jev类模型的生产应用证据 |
| 复核器候选：Granite Guardian | 按特定标准检查回复、上下文支撑或工具调用 | 不是完整路径选择器；中文领域标准及延迟均需另测 |
| 下游验收与改进：τ² / CARE | 完整任务结果、失败归因与版本改进 | 不能隔离证明路径判断器的贡献，或直接证明专用模型有收益 |

这批资料只提供部分机制与证据，尚未共同验证一套完整覆盖上述四项的成熟方案；这不是研究空白或新颖性声明。优先研读Parlant与EMT/MUDERN，再用SOPBench设计检查，最后按实际瓶颈选择判定器和加载策略。

新增资料须说明：是否显式连接候选路径条件与当前证据；是否区分反证、未知和来源冲突；是否处理多路径关系。只测意图标签、下一工具或最终任务成功的资料，按其实际职责作为辅助参考，不提升为完整问题的直接答案。

## 直接相关资料：各自覆盖部分问题

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

### 4. SOPBench：把资格判断与执行遵守分开验收

[*SOPBench: Evaluating Language Agents at Following Standard Operating Procedures and Constraints*（EMNLP 2026）](https://aclanthology.org/2026.emnlp-main.936/)、[作者代码](https://github.com/Leezekun/SOPBench)提供客服沙箱及代码oracle，分别检查最终数据库、每步动作是否允许，以及执行前必要验证是否完成。方法、分层harness实验与局限部分已核查；没有在本仓运行。

作者实验中，即使提供正确条件结论，执行仍可能失败，因此逐条件判断和后续执行必须分别验收。其主要覆盖执行前资格检查，不能直接推广为动态多路径仲裁、主观事实判断或生产收益。这里指无连字符的SOPBench；Amazon的SOP-Bench是另一项目，不合并其任务与成绩。

## 判定器与历史方法的使用位置

**Koa-decision是实现层参考。** [论文v2](https://arxiv.org/html/2609.36115v2)用监督微调、原子标签token和随机标签映射，把给定候选的判断变成单步解码；仍需读取全部输入。已核方法、文本路由结果和延迟协议，未独立复现。其数据与训练/解码边界不足以证明本任务的四项输出都已解决：生产路由数据不公开，多语言有退化，多标签目标与集合选择细节披露有限，概率也未因此自动成为领域风险保证。论文serving延迟与Salesforce产品组件时延保持不同口径。

**KADS下调为历史方法参考。** [2023原论文](https://aclanthology.org/2023.findings-acl.182/)用程序文档检索与T5预测动作，在ABCD/SGD上做离线评估。按题名、DOI、arXiv编号、作者与GitHub定向检索，本轮未确认持续维护的官方实现、明确复用的后继项目或生产收益对照；未检出不证明内部使用不存在。

两条后续关系应准确表述：[DialFork §2](https://arxiv.org/html/2610.21561v5)只将KADS列为相关研究，没有声明复现/部署；同公司[Infinitus图模型（NAACL Industry 2024）](https://aclanthology.org/2024.naacl-industry.29/)使用图与Transformer做下一动作预测，未确认直接继承KADS。其原公司博客已重定向，技术判断以论文为据。方法相似、同一公司和被引用都不能证明KADS生产采用；当前不据它选择默认架构。

## 补充参考：只在相应缺口存在时使用

| 缺口 | 参考与可借鉴部分 | 限制 |
|---|---|---|
| 路径入口、槽位与中断恢复 | [Rasa CALM flows](https://rasa.com/docs/reference/primitives/flows)的description、flow guards、collect、分支；[patterns](https://rasa.com/docs/reference/primitives/patterns)处理澄清、改口、中断等 | 是完整框架，不是自动给所有路径输出已校准分数的小模型 |
| 多条条件同时命中 | [Camunda DMN hit policy](https://docs.camunda.io/docs/components/modeler/dmn/decision-table-hit-policy/)的Unique、Any、First、Rule Order、Collect | Unique多命中会失败，不是自动选第一条；不负责自然语言证据理解 |
| 资格、相关性与优先仲裁混在一起 | [Pega Next-Best-Action](https://academy.pega.com/topic/next-best-action-designer/v2/in/90801/90816)区分eligibility、applicability、suitability与arbitration | 借鉴领域分层，不因此引入整套商业平台；未验证其对本任务的效果 |
| 本地typed-decision基线 | [AnyJev](https://github.com/nokia-applied-research/AnyJev)与[levels契约](https://github.com/nokia-applied-research/AnyJev/blob/main/docs/levels.md) | 当前0.3.0的L0不按标签校准置信度，可花多次prefill；L1/L2留在0.2.0，不能照旧介绍当前API |
| 便宜的诉求/多标签基线 | [GLiClass](https://github.com/Knowledgator/GLiClass) | 分类能力不等于完整规则执行、缺口定位或冲突解析 |
| 流程知识怎样表示 | [FlowBench（Findings EMNLP 2024）](https://aclanthology.org/2024.findings-emnlp.638/)比较文字、伪代码和流程图，同时测单轮与模拟会话 | 不同指标不由同一格式全面胜出；部分评估依赖模型裁判，非生产流量 |
| 状态依赖与信息不足 | [ToolSandbox（Findings NAACL 2025）](https://aclanthology.org/2025.findings-naacl.65/)的缺信息/工具任务、状态与偏序milestone验收 | 主要是个人助理模拟，应迁移测试思想，不能称企业客服已成功应用 |
| 已偏离流程的识别 | [DialFork（2026，v5）](https://arxiv.org/html/2610.21561v5)构造流程偏离并定位首个异常回合 | 模拟对话与受控偏离，不代表自然客户分布或现成模型已能可靠守住流程 |
| 回复/工具调用的特定标准检查 | [Granite Guardian作者项目](https://github.com/ibm-granite/granite-guardian)与[4.1模型卡](https://huggingface.co/ibm-granite/granite-guardian-4.1-8b)支持自定义criteria | 作者只报告英文训练/测试；不是Koa式单token输出，也未证明中文高频客服的净价值 |

完整任务验收继续参考[已有研究补充中的τ-bench](dynamic-skill-loading-research-supplement.zh-CN.md)。[Entagl回放](https://www.entagl.com/blog/typesafe-jev-benchmark-ai-decision-models)中缺少当前会话owner导致误路由的反例，已记录在[应用证据](decision-model-application-evidence.zh-CN.md)；不再用同一来源重复制造新性能记录。

[CARE（2026）](https://arxiv.org/html/2611.02839v1)提供完整生成式客服Agent的失败归因、冻结模拟验收及生产同期比较，适合作为下游改进参考。它没有单独验证Jev类模型的贡献；跨版本harness变化、稀疏满意度和服务成本口径均限制归因。不把未检出满意度差异写成统计等价，也不将模拟坏例率解释为线上总体错误率。

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

1. 选一个现有有界业务问题，分别冻结路径适用、必要补问、冲突处理与可接受优先关系的标注合同。先测固定状态与候选，不同时改变状态提取、判断器和加载策略；先区分事实/政策/工具缺陷和语义判断错误。
2. 比较现用LLM结构化输出、规则/合适的轻量分类或NLI基线、至多两个Jev类候选；各组看到相同证据，使用同一确定性条件组合。保留整体判断基线，不预设语义问题拆得越细越准。
3. 独立标注条件状态、路径集合、必要补问与可接受优先关系。覆盖否定/假设、改口、多诉求、无适用路径、缺信息、事实冲突、状态过期、工具返回后资格变化；按案件、规则族和时间划分。
4. 分别测逐条件/路径错误、关键错误放行、缺口/冲突召回、优先关系违规、冗余补问、含回退的总成本与p95。并行模型问答不等于总调用数或端到端延迟固定。
5. 若该判断环节有净价值，再按[原playbook的阶段B](dynamic-skill-loading-business-playbook.zh-CN.md)比较技能暴露与补载；完整任务成功及业务收益另行验收。第一轮交付可以是瓶颈诊断和停止决定，无需先搭建新平台。

## English orientation

The current question has four separate outputs: path applicability, information sufficiency, conflicts and precedence, given the current request, confirmed facts and candidate conditions. Parlant and EMT/MUDERN are the closest partial references; SOPBench informs verification, while Jev/Koa are possible judgment implementations. KADS is downgraded to a historical method reference because direct downstream implementation and production adoption were not confirmed. Workflow benchmarks, output judges and whole-agent studies retain distinct roles. Dynamic loading remains conditional on an observed context/skill bottleneck. No cited work validates the entire proposed combination; no model inference, independent reproduction or business uplift is claimed here.
