# 多模态 Decision Models：面向新发现的科研实验协议

[首页](../README.zh-CN.md) · [原报告完整转换](multimodal-decision-research-survey-2026-10-22.md) · [已有适配方案](multimodal-decision-finetuning.zh-CN.md#quick-route) · [MIRE 案例](mire-case-study.zh-CN.md#tasks) · [读出与推理机制](decision-readout-and-reasoning.md)

版本：v1，2026-10-22。状态：研究规划与来源核验，尚未运行模型、训练、数据采集或因果实验。目标是产生可反驳、可复现、超出简单模块组合的领域发现；不预先承诺首创、正收益或顶会录用。原 PDF 的历史观点保留在独立转换文档，本协议补充可执行的实验合同，不静默改写报告。

## 1. 先确定论文要回答的问题

第一候选是：**当可选修复分别涉及补看图像、扩展候选、询问用户和更换决策者时，在选择性日志与有限审计预算下，哪些策略价值可识别，哪些只能得到保守区间；如何把审计花在会改变策略选择的未知量上？**

这不是“图文分类 + 置信度 + 追问”的产品系统设计。已有方案已包含 LoRA、CE/Brier、校准、风险下覆盖率，它们是必要基线。新贡献必须落在一个明确失效机制、比现有方法更有效的估计/审计方法，或会改变方法排序的评测证据上。只提高 MIRE weighted F1，不足以回答这个科学问题。

首阶段限制为一次修复后做一次判断，使用有限、预先定义的修复菜单和策略族。先不同时研究开放问题生成、无限动作、多轮 RL 和生产部署。单步结果成立后，才考虑序贯扩展；单步 OPE 公式不能直接搬到多轮历史。

| 可证伪假设 | 首个反证实验 | 失败后的决定 |
| --- | --- | --- |
| H-A：相近初始置信度下仍存在可预测的修复价值异质性 | 同成本 oracle 与 matched-confidence pilot | 无实质 headroom 或简单 router 已解释收益，停止新路由表示研究 |
| H-I：动作结构使可识别性/审计效率产生实质差异 | 已知真值的日志删失、假设破坏与估计器退化对照 | 若完全等价于 AFAPE/标准 bandit，撤回方法创新主张 |
| H-R：新估计/审计方法在自然缺陷下改善策略选择 | 同审计预算比较估计误差、区间覆盖、策略 regret | 仅人工遮挡有效或未胜强基线，降级结论或转向 |
| H-G：现象不依赖单一弱模型或标签体系 | 第二数据源、不同 backbone、持出页面/候选组合 | 若不迁移，只保留局部条件性发现 |

## 2. 数据与官方协议：本次核验和未解条件

2026-10-22 再读 [MIRE 原始 README](https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/README.md)，[当前 main API](https://api.github.com/repos/liujunwen23/MIRE/commits/main) 仍解析为 `d101287af90d114c5bf0cbfbd56fe9c52358e3bb`。固定源码不等于已固定训练数据、权重或线上评测器。

| 核验项 | 可确认的事实 | 研究决策与剩余缺口 |
| --- | --- | --- |
| 两任务 | 图像场景与多轮意图是两个并列任务，各 23 个有效类别；场景表另有两个划掉的退役类别 | 保留 `task_id` 和精确标签。不是每条记录都必须输出两标签，也不强制场景作为意图前级；完整标签复用[已有表](mire-case-study.md#labels) |
| 规模 | 训练总共 1000 个有标签对话样本；初赛 10000 无标签样本，复赛另增 10000 | 不是每任务 1000；任务配比、独立会话数、类别频数与重叠尚未审计 |
| baseline | [Qwen2-VL-7B-Instruct full SFT 配置](https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/mire_baseline/configs/qwen2_vl_full_sft.yaml)：3 epoch、LR 5e-6、`val_size=0.1`、cutoff 1024 | 不是官方 LoRA baseline；`max_samples=10000` 是读取上限。配置未明示 best-checkpoint 选择规则，不能臆造官方独立 Cal/Test 或分组策略 |
| 本地 scorer | [cal_acc.py](https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/mire_baseline/cal_acc.py) 对 `output`/`predict` 字符串计算 support-weighted F1、P/R 与 accuracy | 精确标签匹配，不是 macro-F1；代码未给出比赛两任务总榜聚合或 checkpoint 选择规则。注释中的“多标签”不改变实际单字符串任务 |
| 官方总榜 | [既有核验](mire-case-study.md#data-and-code)记录官方页面按所有分类标签 weighted F1 评分 | 保留其官方来源与历史证据边界；不得取两个 task F1 的等权平均冒充官方 score。本次匿名访问只见登录壳，不推翻以前渲染核验 |
| 资源规约 | README 规定模型参数小于 10B、每样本至多 3 次调用、总输出至多 100 token | “竞赛规约轨”单列，并遵循[原规约差异说明](mire-case-study.md#competition-design)；研究扩展轨可另设预算，但不能与原榜混排 |
| 可获取性 | [固定目录树](https://api.github.com/repos/liujunwen23/MIRE/git/trees/d101287af90d114c5bf0cbfbd56fe9c52358e3bb?recursive=1)中 `data/` 仅见 `demo_test.json`，未见完整图像集或根目录 LICENSE | 原始数据当前下载资格、隐藏标签是否释放、赛后提交是否开放及使用/衍生标注/再发布条款均未验证。代码可见不等于数据获许可 |

[天池数据/任务入口](https://tianchi.aliyun.com/competition/entrance/532277/information)本次匿名访问只返回登录壳；[issue #21](https://github.com/liujunwen23/MIRE/issues/21)在 2025-07-14 报告官网无法下载，本次 API 显示 open、零评论。这是访问风险线索，不证明今天关闭。下一步由已有资格的研究者检查授权界面、条款和文件清单；本次不代为登录、不提交申请或联系作者。数据未取得前，MIRE 完整实验处于待数据条件，10 条文本示例只能检查格式，不能产生可靠性能结论。

[EcomMIR，DOI 10.1145/3701716.3718371](https://doi.org/10.1145/3701716.3718371)收录于 [WWW Companion '25 的 MDSIRC Challenge Track](https://www.sigweb.sigweb.hosting.acm.org/toc/www25b.html)，不是 WWW 主研究轨；它是方案论文，不是另一套独立数据。IntentionGPT/EcomMIR/CuSMer 的组合技术与[原比赛结果](mire-case-study.md#finalists)作为强工程参照，其收益不能归因于单独 LoRA 或读出。Round1 无标签输入参与伪标签学习属于额外 transductive exposure；必须与仅训练集的归纳实验分轨，不能把第三方 Plus 扩充版、伪标签或模型同意标签当官方 gold。

### 公开核心与匿名外部验证

| 来源 | 本次可读的一手证据与用途 | 边界/启动条件 |
| --- | --- | --- |
| MIRE | 上述官方 README、baseline 与示例；适合静态图文分类、候选读取、证据必要性与校准 | 完整数据及权利待核；没有反事实追问菜单，也不自动提供终局结果 |
| SIMMC 2.0 | [归档 README](https://github.com/facebookresearch/simmc2/blob/main/dstc10/README.md)有消歧/共指/对话状态任务；[仓库](https://github.com/facebookresearch/simmc2)当前首页已是 2.1 | 明确固定 2.0 或 2.1，不混用标注；仓库声明 [CC-BY-NC-SA-4.0](https://github.com/facebookresearch/simmc2/blob/main/LICENSE)。核对实际资源和 split；对话后续不是任意新问题的反事实 |
| ABCD | [原始 README](https://github.com/asappresearch/abcd)提供动作化对话、train/dev/test、AST/CDS 与 v1.1 数据说明 | 文本动作任务，不能冒充视觉补全；[根 LICENSE](https://github.com/asappresearch/abcd/blob/master/LICENSE)为 MIT，使用前核对数据和附属资源适用条款 |
| MIntRec2.0 | [论文与作者资源入口](https://arxiv.org/abs/2403.10943)包含自身意图体系及 OOS | 用自身标签进行外部验证；不能机械映射到 MIRE 23 类。实际媒体获取、授权与 split 仍需审计；它不提供新询问的反事实 |
| 匿名私有样本 | 仅用户确认场景“会有追问” | 尚未读取或确认日志、行为概率、结果、规模和发布权。只在授权后本地脱敏审计；不公开企业身份、客户图像、内部字段或可逆标识 |

公共核心应能由公开且获准的资源独立重跑，私有数据只作为外部验证单列，不能让主要贡献依赖不可检查的内部数据。公开数据暂不可得时，可先完成识别反例和公开规则环境；模拟结果只能证明对应受控环境，不能填补真实互动证据。

## 3. 证据阶梯与研究边界

每一层都先出可审查结果再进入下一层。L0-L4 可为静态研究提供证据；不能跨级宣称 L5 的因果效用。

| 层级 | 准入条件 | 基线与主要指标 | Kill criteria | 不能宣称 |
| --- | --- | --- | --- | --- |
| L0 数据与权利 | 许可/来源/manifest/hash、文件可读、split 和 task 标签清单 | 计数、缺图率、重复/组重叠、gold 来源核验 | 无可用 gold/合法获取路径，停该数据线 | 已复现、已获再发布权 |
| L1 可识别性 | 当时图文可见边界和独立标注 | text-only、image-only、OCR+text；一致性、证据充分率、模态必要切片 | 大量标签无法由输入确定，重定任务；无法确认视觉必要性，停“视觉修复”主张 | text shortcut 首创、图像一定有益 |
| L2 机制归因 | 同 checkpoint、相同训练/标签/视觉预算，学习路径可查 | 第 7 节 B0-B6；task-wise F1/准确率、概率和成本 | 强同骨干简单基线解释全部增益，撤回 head/loss 贡献 | 跨系统差异来自读出 |
| L3 风险与覆盖 | 独立 Cal-fit/Cal-policy、冻结完整策略、足够支持 | 温度/类条件校准、selective prediction；风险-覆盖与成本 | 区间太宽或未满足预设风险，保持探索性 | 无条件部署安全、每群体保证 |
| L4 派生 open-world/shift | 自然检索缺失/OOS/页面迁移独立命名、版本化 | coverage v2 风格、强 retriever+selector、prior correction 适用对照 | 仅人工删标签获益，降低外推范围 | 官方 MIRE 新标签、真实追问因果效果 |
| L5 真实修复价值 | 可重放动作或合适的随机/可识别日志，独立目标与成本 | 第 8 节路由/OPE；价值误差、区间覆盖、regret、非响应 | 无支持且无有效界，报告不可识别；不硬估计 | 未观察问题的真实收益、长期业务效果 |
| L6 外部确认 | 冻结协议、第二来源/模型或独立执行者 | 成对差异区间、自然数据复现、负结果 | 效果仅在单一来源/弱模型，收窄论文 | 普遍优越、保证录用 |

[Text Takes Over（EMNLP 2025）](https://aclanthology.org/2025.emnlp-main.1226/)已经研究多模态意图的文本偏置；L1 是必要诊断，不把“发现文本主导”本身作为新颖性。删去依赖文本的样本会改变分布；代表性总体与富集视觉必要切片分别报告。

## 4. 逐条 novelty matrix：先排除已占据的概念

下表是**候选差异和反证义务**，不是已证明的空白。2026 预印本保留其版本与作者报告属性。已读摘要/相关正文不等于完成全式、代码和证明审计；立项 Gate 1 必须补齐 theorem/假设/估计目标/数据/可运行实现对应表。

| 最近邻/一手来源 | 已做到什么 | 本研究必须证明的额外差异 | 会否定创新的证据 / 必需对照 |
| --- | --- | --- | --- |
| [LAVOIR](https://arxiv.org/html/2609.30706)，2026-09 预印本 | slot VOI、一次读出决定何时问什么；规则 posterior 和真实对话分析 | 选择性观测下对异质动作价值的识别/审计，而非再加 VOI head；任务损失与概率增益分开 | 加同样训练信号即可达到收益；对照原 VOI 目标和直接 loss-gain regression |
| [SIEVE](https://arxiv.org/abs/2607.17262)，2026-07 预印本 | 逐样本 direct/repair 分支、loss gap 和 gate | 从“是否修复”到可支持的策略比较，必须有估计/审计增益 | 仅扩成多分支 gate 就足够；对照同表示多动作 outcome regression |
| [ActiveEvidence v2](https://arxiv.org/html/2610.20532v2)，2026-10-16 | 付费视觉获取、交互项、preview value、模型相对证书与独立语义评测 | 不能重提“主动取证/有成本/停止”；需解决不同动作假设与选择性日志的估计瓶颈 | 原获取/审计机制直接覆盖目标或简单适配等效；保留其 acquisition 与 interaction 对照 |
| [RouteCert v2](https://arxiv.org/html/2608.15520v2)，2026-09-07 | 策略诱导终端分组、完整 policy-pattern 的风险验证 | 如研究混合动作后的验证，必须逐式区别其分组与选择条件 | 只是照搬 policy-pattern 校准，不列新理论；其有效适用版本是必需风险基线 |
| [candidate coverage v2](https://arxiv.org/html/2610.03387v2)，2026-10-06 | 人工遗漏、自然 retrieval misses、OOS、等校准预算迁移 | 研究扩大候选的净行动价值和识别，不能声称首次研究自然缺失 | 只新增 OOS 或阈值调参；对照固定强检索、显式 NONE 与同候选 selector |
| [AFAPE，JMLR 2025](https://jmlr.org/papers/v26/23-1635.html) | NDE/NUC 的识别、半离线评估、DM/IPW/DRL | 给出可重放部分与会影响人/目标部分的精确条件，以及相同审计预算的非平凡改进 | 估计器完全退化成既有 AFAPE/OPE；对照适用 estimator、退化等价与区间宽度 |
| [LLM-as-Jev](https://arxiv.org/abs/2610.02076)、[Inner Jev](https://arxiv.org/abs/2610.17205)、[Intern-Decision](https://arxiv.org/abs/2610.22131) | 原 head 候选读出、适配/温度、多字段机制已存在 | 新发现需超出 readout 接口或更换 head | 同骨干 no-training / short-label SFT 完全解释收益 |
| [Text Takes Over](https://aclanthology.org/2025.emnlp-main.1226/) | 多模态意图的文本偏置与去偏评测 | 需显示偏置如何改变修复策略比较，或新的可证伪机制 | 仅报告 text-only 很强，不列新贡献 |
| [Bayes-sufficient](https://arxiv.org/abs/2606.04045)、[COLT 2026](https://proceedings.mlr.press/v336/ye26a.html)、[DSSR](https://arxiv.org/abs/2609.32805) | 决策充分表示/压缩已有理论与应用 | 备选 B 需限定视觉属性与政策族并给出更有效的选择/学习结论 | 仅重命名 information bottleneck、加 invariant loss 或调整同标签成本矩阵 |

继续沿这些工作的一手参考文献排查 classical VOI、active feature acquisition、learning to defer、contextual bandit/OPE、选择性标签、主动审计、clarifying questions 与 partial identification。不能以搜索未发现作为首创证明。新近邻覆盖了核心贡献时，优先缩小/改题，保留失败记录。

## 5. 估计对象、动作合同与识别条件

令 `H` 是决策时可见历史，含当时图文、候选集/检索版本和允许使用的元信息；`a=0` 表示不修复，`a∈{v,c,q,d}` 分别表示补看、扩候选、追问、更换决策者。问题、crop/resolution、检索预算、强模型版本均是动作合同的一部分，不能把不同处理混成同一个 `a`。

对于目标稳定、独立裁定初始意图 `Y0` 的分类任务，冻结下游模型 `m`，定义：

\[
Q_m(h,a)=\mathbb E[\ell(f_m(h),Y_0)-\ell(f_m(h,E^a),Y_0)-c(a)\mid H=h],\quad Q_m(h,0)=0.
\]

`c(a)` 由资源、等待、用户负担按预先固定权重计算，也同时保留未加权成本向量。研究目标主要是有限策略 `π` 的总体净值 `V_m(π)=E[Q_m(H,π(H))]`，或同成本策略差；不是从几百条事件宣称精确识别每个用户的个体处理效应。选择最优策略的比较对象必须在相同可行预算下。

如果问题改变了用户目标，固定 `Y0` 的公式只衡量对**初始目标**的恢复，不等于后续体验。需另记目标转移；对终局结果定义共同尺度的 `U(O^a)-c(a)` 并比较策略干预值。不能把“用户被引导到另一个更容易处理的目标”计成初始意图纠错，也不能跨动作更换结果定义。

| 动作 | 允许观测和可重放部分 | 不可默认的条件 / 必留负结果 |
| --- | --- | --- |
| v 补看图 | 已保存原图的确定性 crop/分辨率；冻结预处理与模型可重放 | 原图当时已存在、无世界变化才可能满足 NDE；新拍照是新获取，不等同旧图裁剪。成本含视觉编码和所有失败 |
| c 扩候选 | 固定索引、query、时间快照上的重检索 | 改变选项空间和归一化；不等于只降输入噪声。记录自然 miss、coverage@k 与冗余项。旧日志没候选快照不能事后假装原结果 |
| q 追问 | 真实已问问题的回答/未回复/退出 | 一个用户不能同时提供所有互斥问题的无干扰结果；NDE/固定目标可能失败。未回复是结果，不只在回答者中算收益 |
| d 更强模型/人工 | 固定强模型在已存图文可重放；人工独立裁定目标与执行角色分开 | 强模型/人工有相关错误、等待和费用；“更强”不等于 oracle。不能用同一人的处理结果与裁判同意自证正确 |

只在一致性、可比较结果、适用的无干扰/目标稳定、观测充分性和正支持条件下讨论识别。行为策略 `b(a|h)` 若已记录可直接审计；未记录但在可信 NUC 下估计时要 cross-fit 并报告误差，不能编造 propensity，更不能因估计了概率就消除未观测混杂。对不可忽略非响应，不把回复者均值外推到全体。NDE 与 NUC 的精确定义和 AFAPE 可用条件按原文逐式审计。

### 理论与方法的可审查目标

1. **退化检查**：固定 latent 状态、纯被动取证、NUC/NDE 成立时，明确映射至 AFAPE；不能把已知等式列为新定理。
2. **失败构造**：构造具有相同观测日志、不同反事实追问效果/策略排序的两个世界，指出缺失的假设和可补充的最少观测。单个不可识别反例通常只够动机。
3. **混合证据估计**：候选研究是让可重放动作的已知结果成为控制变量/辅助信息，把真实随机审计用于互动残差；以直接 outcome regression、IPW/DR 和 AFAPE 半离线估计为基线。必须推导偏差、方差、支持条件与数据依赖，不能把重放行视为独立用户，不能事先保证新 estimator 一定更优。
4. **保守选择与审计分配**：未支持区域先用有界损失的最坏上下界；其宽度随未支持目标质量增长是普通基线，单靠这条界不是新贡献。只在真正缩紧区间、减少相同策略识别误差所需审计样本，或得到非平凡 regret/sample-complexity 改进时提出方法贡献。审计优先级与最终评估独立，审计选择概率留痕。

拟议理论目前没有证明。若所有结果都可直接由既有方法推出，应把论文转为有实质外部意义的诊断/评测研究，或停止该主线。

## 6. Pilot：先测是否值得造模型

先在 Train/Dev 所属发现池规划 300-500 个**独立事件**的 pilot；数量不是统计充分性或全动作反事实可得的承诺。按图像证据不足、自然候选遗漏、两者并存、证据完整但判断错误/不可修复分层，同时保留代表性随机样本以恢复总体权重。对不确定案例至少双人独立标注与裁定；不可识别标签单列。

每事件记录当时可见输入和“行动后才可见”的分区。能完整审计的是已存图像、冻结检索和固定模型等可重放动作；对于真实用户问题，只有有依据的响应模型/随机化人口层平均值，**不能宣称取得同一用户的全问题 oracle**。实际后续回复只对应实际已问问题；LLM 模拟回答仅作探索或压力测试。

| Pilot 检查 | 设计和输出 | 停止判断 |
| --- | --- | --- |
| Oracle headroom | 在可重放子菜单上计算逐事件动作 oracle 与 Dev 选定最佳固定策略的同成本差；有噪声的动作值重复估计并报告选择乐观偏差 | 预先设定最低有意义净值 `δ_value`/覆盖增益 `δ_cov`；上置信界仍低于最低效应则停止。互动菜单只能报可识别的界或随机策略值 |
| Matched confidence | 用初始 max-prob、entropy、margin、候选数、检索分数及可见质量元信息做分层/匹配；比较简单 router 与 richer features 在 held-out pilot 组的价值 | 无条件剩余异质性或增量预测无实质效用则停止新表示。gold 基础错误率只能用于离线分层诊断，不能泄漏到在线路由 |
| 动作收益分解 | 固定 `m`；分别报错→对、对→错、无效、超时、退出、额外成本，代表性和富集样本分开 | 仅更自信、教师更同意，未改善独立目标，不算成功 |
| 选择性日志压力 | 在可重放完整子矩阵上按已知旧策略删失；改变支持/确定性偏好/成本，保留真值用于评价。另设明确标记的隐藏混杂和非响应机制 | 估计有偏却区间过窄，或新法无改进，撤回保证；受控删失不是天然真实日志 |
| 迁移与自然性 | 在已冻结的自然 miss/模糊图上检查；人工扰动单列，换下游模型和候选本体组合 | 仅合成错配、删标签或模拟用户有效，不外推真实修复 |

初始阈值不预设为通用 1%/5% 或任意 F1 增量：按任务损失和审计成本，先填写第 12 节合同，再看 pilot 结果。pilot 用于发现与样本量规划，不作为论文最终确认 Test。

## 7. 静态机制实验：MIRE 的最小强基线

复用[已有实验矩阵](multimodal-decision-finetuning.md#experiment-matrix)、[视觉路径检查](multimodal-decision-finetuning.md#preflight)和[证据消融](multimodal-decision-finetuning.md#evidence-ablations)。以下补足科研归因，不再复制一套训练教程。选一个已获许可、实际支持训练/导出的 2B-4B VLM 为主机制骨干；具体 checkpoint 在运行前核验。官方 7B full SFT 单列，不能因 2B 更便宜就称复现官方 baseline。

| Arm | 设置 | 回答的问题 |
| --- | --- | --- |
| B0-T/O | 相同训练标签的 text-only 与固定 OCR+text 低成本分类器 | 文本可分性与 OCR 信息增益；OCR 是视觉衍生证据，非纯无图控制 |
| B1-G | 同一冻结 VLM 的 label generation；限制短合法标签输出 | 原模型无需专项训练能做到什么，含格式错误成本 |
| B1-L | 同一冻结 VLM 的字母/代码 logits、候选 likelihood/suffix scoring | no-training readout 是否已足够，不只对比昂贵长文本生成 |
| B2 | 同 checkpoint、同视觉管线/Train/步数上限的 short-label SFT/LoRA | 训练本身的效应；与该精确未适配 base 成对 |
| B3-CE | 同 B2 初始化、样本和训练资源的 candidate-subset CE | 候选归一化与 readout/objective 联合改变的效果；不是纯 loss 因果效应 |
| B3-Brier | 与 B3-CE 完全相同，仅加入预定权重的 Brier 项 | 额外目标的成对效应；权重 Dev 选择，温度 Cal-fit |
| B4 | 同一冻结表示上的 linear/MLP classifier；需要时再给相同适配预算 | 简单监督 head 是否解释全部收益；声明表示抽取位置和可见候选 |
| B5 | 同骨干/图像预算的 cross-encoder/listwise reranker；必要时 late interaction | 比较 joint candidate interaction 与缓存代价，分清候选读取和 proposal 质量 |
| B6 | 官方 Qwen2-VL-7B full SFT，以及 EcomMIR 等已公开技术的可审查重实现 | 历史系统参照；多个改变的组合效果单列，不拿来归因某一个 head |

D3/Intern 等独立预训练模型可作系统级推理对照，但不证明 readout 的因果收益。没有经过验证的图像训练/导出路径时，保留推理 comparator，不假装已实现该模型多模态适配。不同大小/预训练来源的结果只给质量-资源前沿，不冒称严格同骨干对照。

对所有 Arm 冻结数据、标签/标注预算、视觉分辨率/token、候选可见性、训练样本暴露、步数/算力上限、Dev 搜索次数、推理 token/调用数和 Cal 标签数。逐项披露无法匹配的成本，而不是只写“相同参数量”。无训练轨、同监督轨、额外伪标签/跨域数据轨分开。报告实际 FLOPs 或设备秒、内存、p50/p95、端到端耗时与每正确完成成本；收费 API 不在本次执行范围。

多 token 中文标签必须说明如何计算完整序列 likelihood、长度处理和候选归一化；首 token 概率不是完整标签概率。语义标签与中性代码做同义映射对照，随机化候选顺序并同步 remap gold；冻结代码 tokenization、末位置与 padding。完整词表 CE、候选子集 CE、独立 classifier head 不混称一种目标。23 类须有完整 23 候选实现，受 16 选项上限的外部实现不能直接宣称覆盖原任务。

图像移除、遮挡、错配仅在人工确认其语义和目标是否保持的子集进行；目标变化则重新标注，不用原 gold 把合法变化当模型失效。同图不同上下文、视觉必要/不必要、细字/关系、近重复与新布局分切片。图像通路未进入模型、截断删关键证据或选项映射错误时先修工程，不能把这种失败包装成新机制。

## 8. 动作策略与估计器的强基线

| 类别 | 必需比较 | 公平性/结果边界 |
| --- | --- | --- |
| 策略下限与上界 | 永不修复、最佳固定动作、同成本随机、强模型 always-on、可重放菜单 oracle | 最佳固定策略在 Dev 选；Test oracle 只作上界，不能回流训练；人工不是完美 oracle |
| 简单路由 | max-prob/entropy/margin、加候选数/检索分数/可见质量的 logistic/tree router | 该基线必须认真调优；特征、标签和 Cal 预算匹配 |
| 直接预测 | 每动作 outcome regression、共享表示多头、直接净损失改变量回归 | 同 backbone 和全部监督；损失目标与 LAVOIR 式概率增益分别比较 |
| 最近邻模块 | LAVOIR VOI、SIEVE gate、ActiveEvidence acquisition/interaction，独立强模块加简单 router | 明确官方代码、忠实重实现与本任务适配差异；未运行不称复现 |
| OPE/缺失估计 | 直接法、IPW/自归一化、标准 DR、适用 AFAPE DM/IPW/DRL、保守界 | 匹配假设/观察模式/预算；报 propensity 支持、权重极值、有效样本量和截断敏感性 |
| 校准/风险 | 温度、类条件映射、selective prediction；适用时 RouteCert policy-pattern/LTT | 同校准预算、冻结完整执行策略，不能只给新方法更多认证标签 |

对“新方法”只逐项加入动作结构、重放信息、审计分配或保守选择之一；分别撤掉并对照标准估计器。若只是把现成取证器、校准器和 router 接起来，视为工程基线。实验要能回答为何收益来自所主张的结构，而不是新增监督、强模型调用或更多视觉 token。

真实追问先定义有限、安全的问题菜单；当前仅规划，**没有新增采集或随机化授权**。后续若获准，在可接受范围内做前瞻随机审计，记录分配概率；不能重问同一用户不同问题并把顺序影响忽略。随机化单位考虑用户/事件及干扰。只做 immediate intent correction 时不必等待长期业务结果，但仍需真实回答、独立稳定标签和成本；最终解决率/满意度/投诉变化需要对应结果与适合的因果设计。

## 9. 划分、派生任务与泄漏防护

完整复用[分组划分协议](multimodal-decision-finetuning.md#split-protocol)和[小样本支持要求](multimodal-decision-finetuning.md#sample-size)。Train 拟合权重/检索/增强，Dev 选择 schema/prompt/checkpoint/路由与预算，Cal-fit 拟合概率映射，独立 Cal-policy 验证风险，Test 只评估冻结策略。cross-fitting 必须对应最终部署模型，不能把多模型 OOF 校准器未经验证套给重训模型。

同用户/会话、同事件、近重复图、所有裁剪/改写/反事实派生放在同泄漏组件。模板族整体持出是额外泛化测试；不要把所有相似页面强行连成无法划分的巨组，也不能放过真实近重复。时间外推仅在可靠时间戳存在时成立；缺时间时明确不能证明时间迁移，用页面/会话持出代替，不能拿文件顺序冒充时间。

1000 条再分 Train/Dev/Cal/Test 后，稀有类和动作-终端组可能没有统计支持。先按独立组件、任务与类计数，再决定划分比例；不机械用 80/10/10，也不把 `val_size=0.1` 当足够的风险认证。可在开发池做 group-aware CV；最终 Cal/Test 保持独立。若只有隐藏竞赛 test 无 gold，则本地重划已获标签数据的 Test 只能称内部 held-out 研究，不能称官方复现。没有足够独立 gold 时停留探索性结论。

派生任务至少分版本：`MIRE-static`（原标签）、`MIRE-derived-candidate`（固定 retriever 的自然 top-k misses）、`MIRE-derived-missing-evidence`（经裁定的图文缺证据）和外部 OOS/迁移轨。候选库来自允许数据，固定索引时间与 query 构造；不得用 Test gold 搜索后补正确候选。人工删除 gold 仅作机制控制，不作为自然 miss 主证据。`unknown/OOS/insufficient` 不等于 MIRE 已知类“其他类别图片”；新 taxonomy 的 gold、采样与评分另行发布协议。

## 10. 主要终点、风险与统计

预注册主要终点为：在预定关键错误风险与总成本约束下，相对最强简单策略的有效正确完成率增益；同时报告给定成本的净效用/策略 regret。数据不足以支持风险约束时，报告探索性的风险-覆盖曲线和区间，不把不可验证保证写进标题。

分类保留官方 all-label weighted F1 以作原协议参照；task-wise weighted/macro-F1、每类 recall/支持数、稀有类、证据必要切片是额外研究指标。独立任务不强行混榜。非法输出、缺图、超时、拒答、追问未回复均留在原始总体；分别报告失败定义，不能删除困难样本提高分数。

动作评价同时报纠错率、致错率、无效修复、用户摩擦/退出、coverage@k、正确候选缺失检测与已覆盖误拒、策略价值估计偏差/RMSE、置信区间覆盖/宽度与最终策略 regret。regret 的 oracle 范围必须明确；真实互动无个体反事实时只报告可识别策略差或界。ECE/Brier/AUROC、trace 证书和教师一致度是诊断，不能替代独立任务结果。增加信息对固定弱模型有负收益，不等于信息在理想决策意义上有害。

[Conformal Risk Control](https://arxiv.org/abs/2208.02814)的期望单调损失保证，不能无条件改写为每次部署高概率的 accepted-set conditional risk；若需要高概率控制，可按 [Learn then Test](https://arxiv.org/abs/2110.01052)匹配风险函数、样本与多重检验条件。策略/路由改变终端分组时，遵守 RouteCert 所要求的完整 policy-pattern 及独立/同时选择条件；未认证分组拒答和继续获取是两种不同完整策略。校准不是对语义真值、分布迁移或执行权限的通用保证。

在单一预先固定切片、独立接受样本、零错误的理想情形，单侧 95% 二项上界 `1-0.05^(1/n)`，低于 5% 约需 59 个**接受**样本，低于 1% 约需 299 个；多个标签/终端组、阈值选择和相关事件需要不同处理。“测试共 300 条”不等于每组都有足够风险证据。

模型差异按同事件/用户层级的配对 bootstrap 或与随机化设计匹配的推断，记录效应区间，不把同图十种改写当十个独立样本。预先指定主比较和多重比较处理；随机种子用于估计训练波动，不增加独立用户数。pilot 后用配对差值方差、目标最小效应和分组/非响应率做样本量设计；未做 power 计算前不承诺最终 n。罕见错误支持不足则扩大合法审计或收窄主张，不事后放宽门槛。

## 11. 备选 B：窄政策族下的视觉证据保留

仅在 A 的识别/互动数据瓶颈无法解决，且存在可审计视觉属性时启动。若政策只改变相同标签 `Y` 的损失矩阵，完整后验 `p(Y|H)` 加显式成本规则是充分强基线；不能把成本矩阵变化包装成新的表示充分性。

可研究设置须有标签外属性 `Z`（例如可人工核验的状态标记）和有限政策族 `Π`，部分规则训练、持出规则组合测试。构造对所有政策无关与至少一政策会改变最优动作的成对视觉干预；验证语义并保留自然样本。同 token/分辨率/监督预算比较：完整后验+规则、显式属性 bottleneck、冻结表示 linear/MLP、通用 token pruning、对比不变性、同骨干 short-label SFT 和完整图像上界。

主指标是政策族内/持出组合的 worst-policy regret、政策切换错误、关键证据保留、原意图性能和完整成本。需给出连接视觉干预与政策 regret 的非平凡学习/选择结论，或新的可解释失效边界。简单显式属性提取器已解决、只在合成页生效，或理论等价于既有充分表示时停止。B 不是与 A 同时堆进首篇的第二套大系统。

## 12. 启动合同、交付与停止记录

下面是**待研究者在看最终结果前填写的合同**，不是已经存在的运行记录。

```yaml
protocol_version: multimodal-repair-v1
status: planned_not_executed
data:
  source_revision_and_file_hashes: REQUIRED
  rights_research_derivatives_redistribution: UNVERIFIED
  task_label_gold_provenance: REQUIRED
  group_split_manifest_hash: REQUIRED
  reliable_timestamps_available: UNKNOWN
target:
  estimand: REQUIRED_stable_intent_or_downstream_outcome
  primary_population_and_endpoint: REQUIRED
  loss_and_cost_vector_scalarization: REQUIRED
  risk_cap_alpha_and_failure_probability_delta: REQUIRED
  minimum_useful_value_and_coverage_gains: REQUIRED
actions:
  feasible_menu_versions_and_costs: REQUIRED
  replayable_actions_and_assumptions: REQUIRED
  response_dropout_goal_stability_fields: UNKNOWN
  logged_propensity_or_identification_basis: UNKNOWN
resources:
  backbone_weights_processor_runtime_revisions: REQUIRED
  train_labels_visual_tokens_compute_calibration_budgets: REQUIRED
  dev_search_grid_and_seeds: REQUIRED
evaluation:
  finite_policies_and_primary_baselines: REQUIRED
  cal_fit_policy_test_roles_and_count_table: REQUIRED
  invalid_output_timeout_abstention_accounting: REQUIRED
  grouped_uncertainty_and_multiplicity_method: REQUIRED
  kill_criteria_and_stopping_decision: REQUIRED
```

后续实验清单复用[已有结果模板](multimodal-decision-finetuning.md#result-template)，增补动作观测矩阵、支持/非响应、估计器假设、区间和 audit allocation。公开证据包应包含协议版本、允许发布的 manifest/重构脚本、独立标注规范、模型与代码版本、所有 baseline 配置/预算、失败记录、原始预测与评分脚本（按数据权利决定内容）、统计脚本及复现命令。无再发布权则提供合法获取与重建说明，不打包原始数据。私有外部验证仅发布获准匿名聚合；身份和客户数据不进入此公开仓库。

| Gate / 建议工作顺序 | 需要形成的成果 | 继续条件 |
| --- | --- | --- |
| G0 来源与可用性 | 数据权利/样本 manifest，MIRE 下载与 gold 可用性，近邻逐式审计表 | 有可实施且可检查的公共核心；否则暂停该数据线 |
| G1 问题存在性 | L1 诊断、oracle/matched-confidence、简单路由 pilot | 有足够且不能被简单元信息解释的 headroom |
| G2 最小方法 | 识别边界/反例、适用估计器、单一新增机制和理论目标 | 超过既有方法的差异明确；否则撤回方法创新 |
| G3 确认性评价 | 自然缺失、同资源基线、独立校准与冻结 Test、效应区间 | 满足预定最小收益/风险/成本，或形成重要可复现负发现 |
| G4 外部确认 | 第二数据/模型、消融、独立重跑、公开证据包 | 主张范围与证据一致后才写论文结论 |

原报告的六周节奏只作资源规划，理论/获取/统计瓶颈可能更久。触发以下任一条件应停止扩模型：oracle headroom 不足；简单 router/独立强模块达到同等收益；只在模拟用户或人工扰动有效；新理论完全等价于标准估计；支持/许可不足以检验主结论；独立语义标签不支持效用。保存失败原因、日期与可重开的证据，不用新名字、更多模块或反复 Test 调参掩盖失败。

本次只完成文档与来源检查。没有下载完整数据/模型、训练、付费 API、读取私有数据、随机化用户、联系作者或创建论文实验结果。Git 同步仅发布文档，不代表已执行实验。
