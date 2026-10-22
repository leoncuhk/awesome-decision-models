<!-- conversion-metadata
Source: multimodal-decision-models-research-survey-2026-10-22.pdf
Report date/version: 2026-10-22 / v1; original timezone: Hong Kong
PDF SHA-256: 2135dda2fb286732da049e3ef8de15f6e8238eef624945f5ff577f336719061e
Conversion: 2026-10-22; 11 original pages; 51 PDF link annotations merged into 49 Markdown links.
Verification: all non-whitespace body characters retained against the original Library text extraction, excluding repeated page footers.
Only heading syntax, paragraph wrapping and link syntax were added. Original claims and historical statements remain unchanged.
This is an archival full conversion, not a newly verified experiment or an updated literature review.
The separate experiment protocol contains the new planning and source-access checks.
-->

> 转换说明（2026-10-22）：本文为原 PDF v1 的完整保真转换，保留原文观点、版本与结论边界；仅整理标题、换行与超链接，移除重复页脚。11 页正文、10 节、附录六部分与 15 篇优先论文全部保留。51 个 PDF 链接标注中两处跨行同链接合并，共 49 个 Markdown 链接。原文“未修改仓库”等表述描述报告交付当时；新增规划与本次核验另见[科研实验协议](multimodal-decision-research-protocol.md)。

# 多模态 Decision Models：研究图谱与可证伪选题

2026-10-22  面向论文立项的研究备忘录  v1

## 结论先行

这个方向值得研究，但“给 Jev/Laya 加视觉、加追问、再做置信度校准”已经不构成清晰的独立创新。当前更值得追求的是：当决策失败时，系统能否识别哪一种干预能真正降低错误，并在不完整、带选择偏差的记录中可靠地学习这种干预价值？

建议将第一候选课题收窄为“异质干预下的多模态决策修复：识别条件、有效审计与保守策略”。它不是已经证实的学术空白，更不是顶会录用承诺。只有证明现有强方法在一个重要、真实、明确界定的条件下确实失败，并给出不可由简单组合替代的解决办法，才值得进入全面开发。

你已确认场景会有追问。这使互动研究成为可能，但尚未确认可用记录规模、追问前后图像、未回复样本、检索候选快照、记录策略或数据发布权限。不能把“有追问”直接等同于“已获得每一种追问的反事实效果”。

本报告把三种内容分开：已有文献结论；对证据的批判性解释；尚待实验验证的研究建议。所有建议实验、定理目标、时间规划均尚未实施。最新资料覆盖到 2026-10-21 发布，按香港时间标注本报告日期。

## 与你已有研究的关系

已只读核对 awesome-decision-models 截至10月18日的整理：原方案已经包含图文意图、冻结VLM与LoRA、CE/Brier对照、独立校准、风险下自动接受覆盖率。因此这些属于本次起点，不列为新贡献。本报告没有改动仓库、目录或同步方式。

[已有多模态方案](https://github.com/leoncuhk/awesome-decision-models/blob/main/docs/multimodal-decision-finetuning.md)                     [机制与推理对照](https://github.com/leoncuhk/awesome-decision-models/blob/main/docs/decision-readout-and-reasoning.md)

## 1. 先确定真正要贡献什么

不要把论文中心句写成“我们提出一个更好的多模态 decision model”。这个表述没有说明哪个问题被解决，也很容易被更大的 backbone 或更强 SFT 击败。更好的中心问题是：同样的不确定预测，为什么需要完全不同的纠正行动；系统何时能从历史信息识别这些行动的价值，何时必须收集新证据？

具体例子：用户发来付款页面并说“处理一下”。系统既可能看不清状态，也可能不知道用户要查进度还是申请退款，还可能因候选检索遗漏了正确处理流程。放大图像、问用户目标、扩大候选库分别修复不同问题。它们可能具有相似的当前最大概率，却有不同的执行后效用。反过来，证据已经齐全但模型推理能力不足时，重复追问可能只是增加成本。

因此研究对象应是“行动后错误损失的真实变化”，而不是“模型执行行动后更自信”。但这一思想也不是首次出现：LAVOIR 已预测询问价值，SIEVE 已研究修复是否有益，ActiveEvidence 已研究付费视觉获取与交互价值。新意必须落在这些工作没有解决的明确条件和方法上。[LAVOIR](https://arxiv.org/abs/2609.30706) [SIEVE](https://arxiv.org/abs/2607.17262) [ActiveEvidence v2](https://arxiv.org/abs/2610.20532v2)

真正有价值的贡献可有三种形态：发现并解释一个此前被忽略的重要失效机制；给出在严格条件下更强的方法或理论；建立能够改变研究结论的可复现评测与数据。无需同时占全三种，但不能只有新的模块名称和一个总分提升。

## 2. 哪些看起来新，其实已经有人研究

“直接从图文输出候选概率”：Intern-Decision、LLM-as-Jev 与原生 VLM 读出已覆盖；更换输出头不能独立证明决策能力提高。

“低置信度时追问”：LAVOIR 已在单次前向中预测各 slot 的信息价值。它的真实对话证据仍有限，但“增加 VOI 头”不是足够的新点。

“正确答案不在候选里就拒答”：候选覆盖论文最新 v2 已有自然检索遗漏、真实域外查询和跨任务拒答策略迁移，不只是人工删标签。[候选覆盖 v2](https://arxiv.org/abs/2610.03387v2)

“主动补看图像，考虑成本和停止”：ActiveEvidence 已包含候选/分辨率选择、交互项、付费预览和模型相对停止证书；不能把相同概念重命名。

“自适应获取模态后做风险控制”：RouteCert 已处理策略决定校准分组的问题。[RouteCert v2](https://arxiv.org/abs/2608.15520v2)

“用选择性日志学习取证策略”：AFAPE 已有识别条件、半离线评估和多种估计器。简单加 IPW/DR 并不新。[AFAPE，JMLR 2025](https://jmlr.org/papers/v26/23-1635.html)

“保持决策充分的压缩表示”：已有 Bayes-sufficient representations、COLT 决策充分表示和 [DSSR agent memory](https://arxiv.org/abs/2609.32805) 方向。不能把 information bottleneck 换名就称新理论。[COLT 2026](https://proceedings.mlr.press/v336/ye26a.html) [Bayes-sufficient representations](https://arxiv.org/abs/2606.04045)

“校准过就能安全执行”：校准、正确性、候选覆盖、联合约束和长期效用是不同性质。一个全部给出低置信度的无用模型，也可能获得漂亮的某些校准指标。需要报告风险与有效完成率的共同边界。

## 3. 首选研究问题 A：不同修复动作，是否真的能被同一套学习假设处理？

工作标题：Identifiable Multimodal Repair Policies under Heterogeneous Interventions。标题只帮助确定研究对象，不代表已确认首创。

核心假设 H1：观测补全、候选空间扩展、用户交互和更换决策者不是同一类干预；如果把它们都当作“补一个缺失特征”，离线价值估计会出现可预测的偏差。利用这些动作的不同结构，有机会在同样的审计预算下更准确地比较策略，或者在支持不足时给出有用的保守界。

必须区分四类动作：

1. 观测型：读取已有原始图像的高清区域，或恢复当时已经存在的原始信息。若不会改变任务世界，可合理考虑 no-direct-effect 假设，部分结果可以重放。

2. 候选型：重新检索处理选项，修复正确候选未进入集合的问题。这改变可选动作集合，不能只当作输入噪声降低。

3. 交互型：向用户追问。回答可能暴露原有目标，也可能因问题引导而改变目标；用户还可能拒答、超时或退出。不能默认为固定 latent intent 的无损读取。

4. 决策者型：交给更强模型或人工。需要计入对方的相关错误、等待和成本，不能用“人工必然正确”作为默认 oracle。

定义要估计的对象：在决策时可见历史 h 下，执行动作 a 后的期望任务损失降低，减去获取、等待和计算成本。任务损失来自独立标签或真实结果；“教师同意”与“模型自信提高”只能作为代理，不能偷偷替代目标。

可投稿的方法贡献至少应满足以下一项：新的、比现有工作更适用的识别或部分识别结果；利用可重放证据降低审计样本量的有效估计方法；针对未确定策略比较的审计分配算法，并给出非平凡的 regret 或样本复杂度结果。

为什么可能有价值：它针对的不是某个模型的误差，而是整个领域把“获取信息”“改变选择空间”“影响人”混成一种动作的评估漏洞。潜在贡献可以迁移到客服、文档决策和交互式视觉系统。是否真的存在足够的新方法空间，仍须继续与 AFAPE/OPE、active feature acquisition、交互式澄清逐式比较。

为什么现在还不能说创新成立：如果最终估计器只是标准 contextual bandit 或 AFAPE 的改名，或者仅把多个现有模块接在一起，就应撤回方法创新主张。一个简单的“两种世界不可识别”反例可以帮助说明问题，但通常不够单独支撑强论文。

## 4. A 的决定性实验：先找现象，再造模型

第一步不是训练新模型，而是建立小型、完整审计的 pilot。建议以 300-500 个独立事件作为发现性起点，样本规模是工作规划，不是统计充分性的保证。按证据不足、自然候选遗漏、两者同时存在、可用行动仍无法修复分层；尽可能保留真实自然缺陷，而非只有人工遮挡。

对每个初始状态，只展示决策当时可见的信息。把原始高清图、实际后续回答、自然重检索结果等作为行动之后才能看到的内容。LLM 可以协助组织材料，但不能凭空生成“用户真实会回答什么”来充当主要交互真值。

关键实验一：oracle headroom。先问在同成本下，逐案例选最好修复动作，比最佳固定策略到底好多少？若差距很小，即使路由学得完美也没有足够研究价值。

关键实验二：matched-confidence。控制当前模型置信度、基础错误率与检索元信息后，最优修复动作是否仍系统不同？若仅靠 confidence + candidate count 的简单路由已解释全部收益，就没有必要新造深层表示。

关键实验三：真实动作价值。冻结下游判断模型，分别执行可行修复；同时报告纠错、把原来正确变错、无效询问、非响应、总成本。增加信息可能伤害固定的弱模型，但理想决策者可以忽略新信息；因此“负修复收益”是模型相对现象，不能称信息本身有害。

关键实验四：选择性日志。保留完整审计真值，再用多种现实旧策略删去部分可见结果，让算法只见日志。分别改变支持覆盖、获取策略、用户非响应和未观测混杂；检验价值估计偏差、区间覆盖与最终策略 regret。真实未观测混杂下不存在无条件的神奇保证。

关键实验五：迁移。持出应用/页面模板、用户、会话、时间和候选本体组合；同时更换下游模型，确认收益不是对某个弱模型的过拟合。

最低基线：永远不修复、最佳固定修复、同成本随机修复、置信度路由、直接逐动作 outcome regression、LAVOIR 风格 VOI、SIEVE 风格 gate、ActiveEvidence 风格获取、AFAPE 的适用估计器、独立强模块加简单 router、动作 oracle。若代码不可用，应明说“忠实重实现”与差异，不冒称官方复现。

## 5. 真实追问数据能证明什么，不能证明什么

已有追问的价值很大：它能提供真实语言、用户回应质量、缺失信息如何被消除，以及追问造成的实际摩擦。但一条日志只记录旧策略选择的一个问题，通常没有记录同一时刻其他问题的结果。观察到问过后解决，并不单独证明这次提问导致解决，更不证明它优于其他行动。

若目标只是“立即的意图分类纠错”，有稳定目标标签和成对补充观察，就可以研究；不必等待几个月业务结果。若要声称提高最终解决率、减少投诉或改变用户体验，则需要对应下游结果与适合的因果设计。

最低数据清单：初始图文与时间边界；当时候选集合及检索版本；追问内容和选择依据；实际用户回答/未回复/退出；补图与重新获取的内容；最终标签和独立标注依据；动作延迟和资源成本。行为策略概率若未记录，不能事后编造。可在批准后的低风险范围安排小规模随机审计，以获取关键策略比较的支持。

事实分层：用户已确认“会有追问”；目前没有检查私有数据，也没有确认上述字段可得。可先用公开可复现任务做方法核心，再用匿名私有数据做外部验证。任何企业名称、客户原始图像和内部字段都不能因论文需要自动变为可公开材料。

公开起点：[SIMMC 2.0](https://github.com/facebookresearch/simmc2) 可提供视觉指代/消歧场景；[ABCD](https://github.com/asappresearch/abcd) 可补充动作化对话；MIRE 可支持静态图文意图。它们都不是现成的全动作反事实数据集，需清楚说明派生构造与人工核验，不能混成一个天然统一benchmark。

## 6. 备选 B：保留未来决策真正需要的视觉证据

工作标题：Policy-Conditioned Evidence Preservation for Multimodal Decisions。

核心问题：在固定视觉 token 或表示预算下，能否保留当前标签不需要、但一类明确后续政策会需要的视觉信息，同时丢掉对这类政策都无关的变化？例如同属“退款咨询”，一个很小的状态标记会改变是否允许自动处理。对当前意图无关，不等于对所有后续行动无关。

先排除一个伪问题：如果未来政策只改变同一组意图标签上的损失矩阵，那么准确的完整标签后验加显式成本规则已经足够。此时现有 CE/Brier 概率模型就是强基线，不能声称发现全新的“决策充分性”。

真正可研究的设置需要政策依赖标签之外的属性，并明确限定政策族。用人工或任务规则验证的成对干预，区分“对整类政策都无关的修改”和“至少对某种政策改变最优动作的修改”。训练部分规则，测试未见规则组合与真实页面。

必要新增：连接可审计的证据干预与政策族最坏 regret 的有效学习/选择方法，或可清晰解释的新失效边界。不是只给 representation 加一个 invariant loss。需要对比属性 bottleneck、全后验加成本规则、通用token pruning、对比不变性训练和同骨干短标签 SFT。

主要指标：同等视觉 token 下的政策切换错误、成本加权 regret、关键证据保留、原任务准确率、真实自然案例迁移。若一个简单显式属性提取器已经解决问题，应淘汰更复杂方法。

定位：这是有条件的备选，不是第二条同时铺开的主线。已有 Bayes-sufficient、COLT 充分表示和 DSSR memory 研究，抽象定义已不新。只有窄政策族、真实视觉属性和强对照能让它站住。

## 7. 另两个问题值得跟踪，但不建议首篇同时做

联合可执行决策：单字段校准不保证多个字段的联合动作合理；应比较联合模型、CRF/因子图、独立头加投影与约束解码。但概率一致性和结构化预测已有长历史，不能仅以“加一个约束图”立项。只有联合依赖改变最优风险行动、且投影无法恢复的信息确实重要时，才值得进入方法研究。

异步证据状态：截图可能过期，日志可能只记录“计划执行”，工具返回可能延迟；永远信图像或日志都可能错。研究 refresh/verify/retry/continue 的策略有价值，但 [Claim Laundering](https://arxiv.org/abs/2610.25947)、[Omni-Decision](https://arxiv.org/abs/2607.11433)、ActiveEvidence 已经很近，需要可回放环境和未见故障机制测试。它比当前图文意图数据更远，建议作为后续。

优先级判断：A 的理论空间最深但数据要求高；B 可以在更受控环境验证，但创新被既有充分表示理论挤压；联合决策与异步状态均先列观察，不为了凑论文而拼成一个大系统。

## 8. 什么证据才配得上“有价值、独到”

论文的 claim 必须可被推翻。建议预先写四个失败条件：同成本 oracle 没有足够提升空间；简单路由和独立模块组合已达到同等收益；收益只存在人工扰动或模拟用户；新理论完全退化成已知假设下的标准估计器。触发后转向，而不是继续堆模块直到总分变好。

公平比较必须锁住 backbone、训练样本、标签预算、图像分辨率、视觉 token、候选覆盖、观察次数、推理 token 和校准预算。一个 API 请求不等于一个前向；一次前向也不等于零推理成本。报告 p50/p95 延迟、完整任务成本和每成功决策成本，不只报单次调用速度。

划分 Train / Dev / Calibration / Test。把近重复截图、同用户会话、同模板和同一事件的所有反事实放进同一组，防止泄漏。先冻结目标、超参数选择规则和主要终点，再查看最终测试。主评价需独立真值，不让同一个模型生成、验证并裁判整个测试集。

主指标建议：固定关键错误风险下的有效完成率，以及给定总成本下的任务 regret。补充纠错率、致错率、拒错率、用户摩擦和分组风险；ECE、Brier、AUROC 是机制诊断，不能独自代表业务价值。对结果做配对置信区间和用户/事件层级 bootstrap，不把同图多条改写当独立样本。

风险保证必须注明假设。单一预先固定切片、独立接受样本、零错误时，单侧95%二项上界为1-0.05^(1/n)。要低于5%约需59个接受样本，低于1%约需299个；多个切片、策略选择和相关样本会改变要求。不能用“总测试300条”替代“每个承诺风险切片都有足够有效样本”。

观察不齐全时允许报告“不可识别/区间太宽”，这可能是有价值的结果。不要用一个漂亮的形式证书替代语义正确性：ActiveEvidence 自己也将模型相对证书与独立语义质量分开。

## 9. 建议立项节奏与 OKR

O：找到并验证一个现有强方法尚未解释或解决、且对真实多模态决策重要的机制问题，形成可复现的论文贡献，而不是先承诺做一个新模型。

KR1：为最终单一问题建立最近邻 claim matrix；每项预期贡献都写明已有工作已经做到什么、剩下的差异是什么、什么证据会否证差异。验收不是“读了多少篇”。

KR2：在发现性 pilot 中确认有实质 oracle headroom，且在控制置信度和简单元信息后仍有可预测的动作价值异质性。最低有意义效应应在看最终结果前按任务成本确定，不事后追逐显著性。

KR3：在固定预算、独立 held-out 事件和自然缺陷条件下，超过最强简单基线；改善来自提出的机制而非更大模型、更多标签或不同候选。若失败，明确撤销原假设。

KR4：形成一个可供外部检查的核心证据包：协议、公开或合规派生数据、完整基线、效应区间、负结果和可重运行脚本；私有验证单列，发布前获得授权。

建议节奏（依数据与算力调整）：第1周冻结近邻与数据可用性；第2周完成 oracle/matched-confidence kill tests；第3-4周仅在通过后做最小方法和定理；第5-6周做自然数据、迁移、消融与统计审查。时间是计划，不代表六周可保证达到顶会水平；理论或采样瓶颈可能要求更久。

算力先冻结一个2B-4B图文模型和强参考模型，训练小头或做读出对照；看到机制信号再做LoRA，不先上大规模在线RL。当前没有启动训练、运行付费API、读取私有客户数据或修改仓库。

## 10. 阅读顺序与研究判断

先读 LLM-as-Jev、Releasing the Inner Jev、Intern-Decision，理解哪些能力已经是廉价基线；再读DecisionPivot、候选覆盖v2、prevalence shift，理解总分掩盖的控制问题；然后精读 LAVOIR、ActiveEvidence、RouteCert、AFAPE，判断 A 是否真有方法缺口；若考虑 B，再读 Bayes-sufficient 与COLT 理论。

我的当前判断：把“错误检测”推进到“可识别的干预价值”，比单纯给多模态判断增加一个头更值得投入；但仅有这个方向名称还不够。下一步最有价值的工作是用真实追问场景建立能杀死坏想法的试验，而不是提前写一篇宣称创新的摘要。

以下文献图谱提供可逐篇阅读的原始链接、版本和边界。它是聚焦式 survey，不是穷尽性系统综述；未执行模型独立复现，预印本结果均为作者报告。搜索没有发现某项方法，不等于证明全领域无人做过。

## 附录 A：模型机制、最新论文与基线图谱

检索时间：2026-10-21 23:54 UTC（中国时区已为 10 月 22 日）。范围为可检索的 arXiv、正式会议/期刊页面、作者仓库及模型卡，不声称穷尽。以下 2026 年 9-10 月论文在此次访问的 arXiv 页面未显示已获正式会议/期刊录用，统一按预印本处理；产品模型与厂商报告单列，不能把预印本/排行榜写成顶会结论。本文的研究解释与局限判断是基于论文的分析，不是独立复现实验。

### 一、先把五种不同问题分开

1. Typed decision models / System One models（本轮新热点）：输入状态/证据、自然语言问题、候选项，输出候选概率或有界分数。形式是 p(y | x, q, C)，并不是默认优化长期回报。相对于普通分类器，主要新增的是任务在请求时指定、标签空间可变、共享基础模型、概率接口和低延迟。相对于 LLM，差别可以只是 readout/训练/服务方式，而非全新模型类别。单次 prefill 后读合法 token logits 就能实现重要子类。研究重点应是这些概率对应什么事件、在何种变化下有效，以及软件消费它们后实际怎样。

2. Decision-focused learning（DFL）：学习预测器或决策代理，但训练目标是下游优化损失/regret，而非单纯预测精度。通常有显式约束、成本与优化器。这是目标函数层面的定义，既不等于 Jev，也不要求用Transformer。与多模态 TDM 最有价值的交叉，是让视觉/音频表征优先保留会改变最优行动的信息，而非所有易预测细节。新的理论锚点包括 [Online Decision-Focused Learning，ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/4e14a2a225d5d186b7eb1ecc7605bc2d-Abstract-Conference.html) 和 [DF ，UAI 2025](https://proceedings.mlr.press/v286/kong25a.html)。前者给在线 DFL 静态/动态 regret 保证，但实证主要是 knapsack；后者直接学习期望优化目标，不能把distribution-free 一词误读成任意分布迁移都保证安全。

3. Decision Transformer / 轨迹条件生成：以目标 return-to-go、状态和行动历史条件化下一行动，核心是离线序贯决策的轨迹建模，不是通用候选概率 API。[Decision Transformer，NeurIPS 2021](https://proceedings.neurips.cc/paper_files/paper/2021/hash/7f489f642a0ddb10272b5c31057f0663-Abstract.html)。若任务有奖励、历史依赖和闭环轨迹，它是合理基线；若只有图像分类，加入 DT 名称无意义。

4. 生成式规划/动作模型：扩散、flow 等生成动作块或轨迹，通过目标、奖励、约束引导采样。[Diffuser，ICML 2022](https://proceedings.mlr.press/v162/janner22a.html) 将整条状态-动作轨迹的去噪与规划结合；[SafeDiffuser，ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/file/f95606d8e870020085990d9650b4f2a1-Paper-Conference.pdf) 加入控制屏障函数约束。它们解决候选生成/连续控制，TDM 更多解决候选选择/验证。两者可以组合，而不是简单替代关系。

5. 世界模型与 LLM/VLM policy：世界模型预测行动后果，policy 选择行动，critic 衡量回报，三者不能混同。[DreamerV3，Nature 2025-04-02](https://www.nature.com/articles/s41586-025-08744-2) 是清晰的 world model-actor-critic 分解。文字/视频预测真实，不自动意味着决策最优；有合法候选概率，也不自动意味着具备动力学或因果模型。

核心区分：格式有效性 不等于 分类正确率 不等于 排序能力 不等于 概率校准 不等于 逻辑一致性 不等于分布外可靠性 不等于 闭环效用。应分别测试，不宜用一个“Capability”分数代替。

### 二、Jev、Laya、CLM 的核实结果

- Jev：TypeSafe 官方于 2026-09-15 发布。官方声称新架构、parallel sampler 和 RLCD，输入 state + typed questions，返回 choice/score/noul。架构与完整训练过程未公开，不能把第三方复现方法当成 Jev 的真实实现。“不生成字符串”排除了特定格式失败，不排除判断错误或错误高置信。[官方发布](https://typesafe.ai/blog/introducing-system-one-models-and-jev)

- Laya：已核到原作者仓库，确为非自回归文本决策模型，不是臆测名称。英语 checkpoint 使用ModernBERT-large 421M；多语言版本使用 mmBERT-base 322M。作者提供 proper-scoring-rule reward/GRPO-style 训练及温度校准代码。训练使用 proper scoring rule 并不证明有限数据、有限容量、分布迁移下的校准。[原作者仓库](https://github.com/NandhaKishorM/laya)

- CLM-v0.1-8B：已核到作者模型卡与仓库。冻结 Qwen3-8B，分别训练 state/action 投影头，以双向InfoNCE 关联状态和行动；候选可缓存。其概率是给定候选集内的相对分数，不是行动结果的客观成功概率。作者引用条目标明为技术博客，而不是已核验会议论文。DeepSWE/Terminal-Bench 的高分来自任务微调 heads，不能写成基础 checkpoint 的 zero-shot 成绩。[模型卡](https://huggingface.co/Contrastive-LM/CLM-v0.1-8B)；[代码](https://github.com/Contrastive-LM/CLM)

- 产业最新快照：Liquid AI 10/7 发布 d1-3B（图文）与实验性 d1-omni-600M（文字+图像或文字+音频）；Baseten 10/21 发布 mammoth-1/elephant-1，后训练 Qwen3.5-27B/9B。两者说明接口快速产品化，但厂商排名和速度不能替代匹配硬件/数据的独立研究。[Liquid 官方](https://huggingface.co/blog/LiquidAI/open-d1)；[Baseten 官方](https://www.baseten.co/blog/the-best-decision-models-in-the-world-mammoth-1-and-elephant-1/)

### 三、15 篇优先阅读论文

#### 1. LLM-as-Jev: LLMs Are Already Jev-Style Decision Models - When and How to Fine-Tune Them

首发 2026-10-01；当前 v3 2026-10-13；预印本。 [论文](https://arxiv.org/abs/2610.02076) 保留原架构的候选打分、任意选项数处理、KL anchors 微调；还讨论带预算的 Thinking Jev。强骨干可零训练得到有竞争力的决策表现，微调收益依模型规模/任务而变。意义：任何新 decision head 都应先打败同骨干的无训练读出。边界：主要测试有限模型与任务，不能推出所有基础模型都无需决策训练；有 reasoning 就不能再把全部速度归因于“单次前向”。

#### 2. Releasing the Inner Jev: A Simple Recipe for Open Decision Models

2026-10-12；预印本。 [论文](https://arxiv.org/abs/2610.17205) 从末位置 A-P logits 直接取候选概率，以原 LM head 切片初始化决策头，LoRA 加温度校准；提出 OpenDecisions 2,352 问题。消融发现主要收益来自表征的 LoRA 适配，而非新head。边界：该实现最多 16 选项；OpenDecisions 是验证集，部分标签来自模型，不能当完全独立的人类真值测试。论文直接削弱“加一个决策头即方法创新”的论证。

#### 3. General Decision Models: Benchmarking and Insights Beyond Jev

首发 2026-10-02；v2 2026-10-12；预印本。 [论文](https://arxiv.org/abs/2610.03935) JEVal 包含 11,257 实例、36 数据集、10 领域、25 模型配置。局部证据充分时表现强；专门知识、精确概率和长轨迹更弱。τ-bench 中局部更快但成功率可下降。Reasoning-to-Readout 自蒸馏模型在当前摘要名为 SII-Decision-4B/27B，不要沿用早期搜索缓存中的InnerJev。边界：静态汇总、闭环实验和社会模拟证明的是各自设置，不是普遍能力界。

#### 4. MetaEncoder: Exploring the Limit of Bi-Encoders for Multimodal System One Decision Making with Natural Language Interface

2026-10-08；预印本。 [论文](https://arxiv.org/abs/2610.11316) 将 Muse-Glimmer 30B 对比微调为图像/视频双编码器，跨小候选集和百万检索库。关键消融：把完整候选列表加到 request，MMLU 提升 18.11 个百分点，MMMU 提升 7.54 点。这揭示缓存友好编码与候选交互之间张力。边界：其强小集合配置并非“请求与候选完全无交互”；复杂推理仍明显依赖中间 reasoning，不能用更多帧替代推理。

#### 5. Intern-Decision: Efficient Multimodal Decision Making with Autoregressive Masked Language Modeling

2026-10-15；预印本。 [论文](https://arxiv.org/abs/2610.22131) 在完整 JSON 骨架中设置多个 decision placeholders，用原生 LM head 一次causal forward 并行读取字段。0.8B/2B/4B；4B 在作者七套评估平均 90.02%，Jev 88.74%。边界很重要：校准试验只有 96 个已知分布样本；handoff 只有 111 题；游戏/浏览器是定性演示。44.16ms 是固定289-token 三字段本地请求，不等于完整视觉 agent 帧率，也不等于对 API 的匹配硬件加速比。

#### 6. AudioJev: Direct Audio Decisions with Order-Calibrated Probabilities

2026-10-01；预印本。 [论文](https://arxiv.org/abs/2610.01293) 直接 waveform + question + candidates，使用随机错排成对训练与对齐后的symmetric KL，降低选项顺序导致的分布变化。三随机种子完整 MMAU/MMAR 平均准确率68.88%/55.33%。关键术语：这里的 order calibration 是顺序不变性，不是预测 0.8 的事件长期 80% 发生的频率校准。适合作为多模态 invariance 基线，不能声称已解决风险可靠性。

#### 7. LEV: Thinking Fast and Deep with Looped Decision Models

2026-10-14；预印本。 [论文](https://arxiv.org/abs/2610.20951) 对 loop-pretrained backbone 多次循环层，逐深度读出，联合训练；通过stopper 按难度分配深度。作者 2.6B 模型深度 1至4 在 JevBench 从 63.2% 到 76.2%。边界：这是潜在空间可变计算，不是免费的一次前向推理；收益依赖 loop backbone、训练预算与延迟匹配。新工作不能只把“不确定时多算几步”作为新意。

#### 8. Beyond Calibration: Do a Typed-Decision Model's Probabilities Obey the Probability Axioms?

2026-09-27；预印本。 [论文](https://arxiv.org/abs/2609.33209) 用逻辑相关的正反命题、互斥标签和多选题检查逐样本 coherence，不依赖新标签。Jev 在 480 否定对上的概率和偏差平均 0.064，优于某些 LLM 读出但仍不一致。边界：只有 160 来源样本与有限模型；逻辑一致不意味着语义正确，语义正确率也不保证跨接口一致。这是联合决策/多字段动作研究必须引用的分界。

#### 9. Does a Hosted Decision Model Respect Irrelevant Alternatives? A Pre-Registered Test of Option-Set Dependence in Jev

2026-10-12；预印本。 [论文](https://arxiv.org/abs/2610.16655) 299,463 调用检查候选集合改变是否影响原有选项 odds；低概率额外选项也能产生系统变化。独立 yes/no 打分移除该集合依赖，却损失 8.7 个点准确率。启发：概率到底属于候选、候选集还是事件，必须明确。边界：不要把 IIA 当所有真实决策的普适理性公理；有上下文依赖/相关替代项时，变化可合理。应明确测试的是语义等价变换还是任务本身改变。

#### 10. Benchmarking candidate coverage and rejection policy transfer in typed decision models

首发 2026-10-02；v2 2026-10-06；预印本。 [论文](https://arxiv.org/abs/2610.03387) 区分人工移除正确项、真实 retrieval misses、公开out-of-scope queries；比较等校准预算下拒绝策略迁移。某 Jev 源域阈值迁至 Emotion 会错拒绝 69.3% 已覆盖输入。意义：最大 softmax 小并不等价于正确动作不在候选集。边界：v2 已超出“只做 label omission”；新论文不能把补上自然 OOS 当作未被研究的贡献。主要是诊断而非通用解法。

#### 11. Typed Decision Models under Prevalence Shift: Decision Training, Calibration, and Implicit Priors

2026-10-19；预印本。 [论文](https://arxiv.org/abs/2610.26325) 三个 TDM、匹配骨干和两个训练分类器，五数据集，35 预定配对检验。决策微调并非普遍增益；在该实验里 TDM 也不是独有的 label-shift 脆弱类别。EM prior correction 有条件改善，带标签重校准更强。边界：通过重采样构造纯 label shift，故 p(x|y) 不变；不涵盖模态损坏、观测策略改变或概念漂移。不能将其总结成“TDM 在漂移下一定崩溃”。

#### 12. Teacher Supervision, Fixed Representations and Calibration: Exact Risk Calculations for Candidate-Scoring Decision Models

2026-10-19；预印本。 [论文](https://arxiv.org/abs/2610.26797) 在高斯/Probit 代理中分解教师偏差、冻结表征与温度校准的风险；更多教师伪标签不能去掉教师偏差，概率缩放也无法修复方向错误。还有真实投诉结果实验与候选事件细化一致性分析。意义：必须用 realized outcomes 而非 teacher agreement 验证决策。边界：解析结果依赖明确代理假设，不是对 Jev 未公开训练算法的证明；其对 Jev 架构的二手描述不能覆盖官方“不公开”的事实。

#### 13. Multimodal Reranking Is a System One Decision

2026-10-20；position paper / 预印本。 [论文](https://arxiv.org/abs/2610.28435) 将 top-16 检索结果放入同一多选上下文，用标签概率排序；在其 MMEB-V2 图像实验优于逐候选 yes/no 读出 5.4-7.3 hit@1。文本 decision tuning 对页面检索也可有迁移。边界：27B 新代 VLM 与 2B/8B 专用 reranker 对比存在规模和代际混杂，作者明确承认。对照必须包含同骨干、同图像预算的 listwise reranker；不能把“多模态重排也是决策”本身当新课题。

#### 14. DecisionPivot: A Diagnostic Benchmark for Decision Models in LLM Systems

2026-10-20；预印本。 [论文](https://arxiv.org/abs/2610.28522) 48 任务、40,033 项；其中 7,800 核心项来自 13 个生成家族，用独立 solver 验证；比较 40 decision models 与 14 general models。相近总分可掩盖 70.1% vs 44.2% 的 contrast-group accuracy 差异；正确概率排序也不保证两个边界样本都分类正确。边界：仍是受控诊断，不直接证明真实流量风险或闭环成功。建议继承其 pivotal counterfactual 分组，而不只新增静态图像测试。

#### 15. ActiveEvidence: Decision-Focused Evidence Graphs with Verifiable Acquisition Gaps

首发 2026-10-14；v2 2026-10-16；预印本。 [论文](https://arxiv.org/abs/2610.20532) 在免费元数据/付费观测边界下，用证据交互图、gap-directed refinement 与冻结 trace 证书选择视觉证据；包含有成本的 previews、paired continuation rollouts 和轨迹认证。边界：证书是 给定固定学习评分下的 model-relative 最优性，不是语义真值保证；640 案例、128 测试。它已覆盖主动多模态证据采集，因此“学会何时看更多”不足以宣称首创，需要与该方法实质区分。

### 四、补充阅读与反证（按研究问题选，不必全做主表）

- [Typed Decision Models: An Early Evidence Audit and Evaluation Checklist](https://arxiv.org/abs/2609.32160)，2026-09-26。审计 9/19-9/24 的 28篇论文，提出 14 项评估检查。适合作为证据等级/公平对照起点，但时间窗口仅最初九天，不能当 10 月完整综述。

- [Qwen-Audio-Jev](https://arxiv.org/abs/2610.21614)，2026-10-15。统一音频 choice/noul/score，18 配置；作者明确将 streaming decisions 留作未来扩展。约 20× 速度是相对指定原骨干与其评估流程，不是对一切音频模型的通用结论。

- [Can Jev be Your Q or Policy in Reinforcement Learning?](https://arxiv.org/abs/2610.11692)，2026-10-08。把冻结决策模型用于 reference policy、exploration judge、replay rater，9 MiniGrid + 3 Atari；指出不能直接当 cardinal value function。这与“概率等同 Q-value”的误读直接相关。

- [System Switch](https://arxiv.org/abs/2610.09683)，2026-10-07。离线 confidence deferral 有增益，但 33 闭环 Doom 游戏无变体到达出口。校准、错误检测 AUROC、真正闭环成功是不同维度。

- [CLM-as-a-Judge](https://arxiv.org/abs/2610.07177)，2026-10-05。公开 judge 任务上 CLM 基础模型可近随机；重校准能降低 ECE，但无力创造判别能力。不能从这一个 checkpoint/任务推出所有 contrastive models 无效，也不能忽略官方 verifier强结果依赖微调。

- [JevAdvBench](https://arxiv.org/abs/2609.31142)，2026-09-25。类型合法不等于免疫 prompt injection；受操纵的输出仍可完全满足 schema。

- [TypedBench](https://arxiv.org/abs/2610.11392)，首发 10/8、v2 10/9。七类 policy-labelled generators、九评估套件；考虑有限样本校准噪声基线、措辞敏感、ordinal/noul 一致性，适合作为 probability evaluation 的对照。

### 五、必须覆盖的 baseline families

1. 同骨干 no-training readout：答案字母 logits、candidate likelihood / suffix scoring；不能只和昂贵长文本生成比较。

2. 同骨干 post-training：SFT/LoRA + 原 head；新 decision head；对比学习双编码器。分离骨干、数据量、目标函数、输出头的效应。

3. 成熟小模型：任务训练分类器（例如 DeBERTa/ModernBERT）、线性 probe、检索/相似度；需要标签的模型和 zero-shot 要分不同资源轨道。

4. 多模态专用模型：cross-encoder/listwise reranker、late-interaction、VLM 直接读出。视觉 token、帧数、图像分辨率必须匹配。

5. 自适应计算：entropy/max-prob gate、随机等预算路由、oracle gate、强模型 always-on、LEV 类动态深度；把观测成本与 reasoning 成本分开。

6. 序贯决策基线（仅在任务需要时）：行为克隆/Decision Transformer、标准 RL、world-model planner、生成动作+固定 selector。不能以单步分类精度代替回报/任务成功。

7. 可靠性校正：温度缩放、向量/类条件校准、合适的 prior correction、selective prediction/conformal 风险控制。校准集、模型选择集、最终测试必须独立。

8. 候选生成和检索：固定强 proposal generator、同候选集统一 selector、oracle candidate inclusion、真实候选缺失。否则 selector 增益可能只是 proposal 更好。

### 六、仍值得追问的问题，但不得直接当未被研究的新颖性声明

- 从“对候选标签的相对信念”到“行动结果概率/效用”的语义桥梁是否成立？概率向量合法、teacher对齐和 realized outcome 对齐是三件事。

- 哪些多模态信息是决策充分的？低延迟双编码器省掉的交互，在哪些关系、时序与反事实任务中不可省？MetaEncoder 的 options-in-prompt 消融是重要线索，不是普适定理。

- 在证据变化、候选变化和行动反馈同时改变数据分布时，单步校准如何迁移到策略诱导分布？纯label-shift 校正不回答这一问题。

- 主动观测、拒答、更多 reasoning 和执行行动的收益如何统一计量？ActiveEvidence、LEV、System Switch、candidate coverage、RouteCert 等已经接近，需要逐项定位其条件边界，而不是笼统宣称无人研究。

- 多字段/多步决策的联合约束如何保持？逐字段概率和为一并不提供联合 coherence，也不保证可执行约束。

总体结论：新鲜且重要的方向，不等于新鲜名字就有方法贡献。最有研究价值的是识别具体的失效机制与成立条件，给出能被反例推翻的假设，在同资源强基线下改善真实闭环效用，并明确概率和保证的适用范围。仅加视觉 encoder、换 head、做小型分类集或展示局部速度，已经很难支撑顶级论文。
