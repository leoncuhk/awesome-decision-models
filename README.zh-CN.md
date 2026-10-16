# Awesome Decision Models [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**面向 AI 系统可靠判断的模型、方法与实证资料。**

[English](README.md) · [模型卡](docs/models.md) · [评测证据](docs/evidence.md) · [选型指南](docs/selection-guide.md) · [收录与评测方法](docs/methodology.md) · [来源登记](docs/sources.md)

收录用于**分类、评分、排序、验证、路由与拒判**的模型和方法。我们关心的不是谁的宣传数字更高，而是：**在具体任务中，哪种方法能以可接受的风险和总成本，交付可验收的结果。**

**本版来源核验日期：2026-10-16。** 精选 48 项资源，其中 17 个核心模型系列、28 条带协议背景的评测记录。本版完成的是公开资料核验，**没有宣称独立运行并复现这些模型**。阅读深度、版本固定情况与未解决的资料缺口均见[来源登记](docs/sources.md)。收录不等于背书，也不等于通过生产可靠性认证。

## 目录

- [先看任务，而不是模型名称](#先看任务而不是模型名称)
- [核心模型](#核心模型)
- [应该保留的基线](#应该保留的基线)
- [路由与结果反馈学习](#路由与结果反馈学习)
- [可靠性与评测](#可靠性与评测)
- [基础原理与近期研究](#基础原理与近期研究)
- [相关资料库](#相关资料库)
- [维护与贡献](#维护与贡献)

## 先看任务，而不是模型名称

本仓库用 **Decision Models（决策／判断模型）** 组织资料，不声称它们已经构成一门统一的新学科。*Typed decisions* 描述输出契约；*System One* 是部分项目采用的类别名称；RLCD、对比学习、监督分类是不同训练路线。路由与选择性预测则进一步研究如何使用一个判断。

| 真正要解决的问题 | 值得优先比较的方案 | 不要混淆成 |
| --- | --- | --- |
| 理解消息、核对有限条件 | 类型化判断模型、标签分类器、监督学习基线 | 某个行动能否改善结果 |
| 从大量可复用候选中选择 | 双编码器、重排器、领域选择器 | 最好的候选一定正确 |
| 交给哪个模型、工具或人 | 基于实际执行结果的路由与交接学习 | 给任务打一个泛化的难度分 |
| 哪些案例可以自动处理 | 独立校准、风险—覆盖率评估、拒判 | 相信名为 `confidence` 的字段 |
| 哪个行动会带来更好结果 | 上下文老虎机或合适的因果方法 | 从历史日志中预测相关性 |

这是**实验起点，不是已测出的通用赢家**。决策契约和最小测试方案见[选型指南](docs/selection-guide.md)。

## 核心模型

首页比较机制、用途与限制，**不把不同协议的准确率拼成总榜**。每个项目均链接原始资料；训练方式、部署和许可证注意事项见[模型卡](docs/models.md)。

| 模型 | 机制／定位 | 适合的实验 | 重要限制 |
| --- | --- | --- | --- |
| [Jev / TypeSafe](https://typesafe.ai) | 托管的结构化判断服务：对选项、命题与有序评分标准输出分布。 | 可作为托管类型化判断对照或冻结的语义特征提取器；与监督基线比较时统一任务与标签规则。 | RLCD 的完整训练配方未公开；格式合法与置信度字段不等于语义可靠。 |
| [Laya](https://github.com/NandhaKishorM/laya) | 小型编码器与动态选项判断头；包含通用、多语言及工作流专项检查点。 | 适合有领域训练数据、需要控制高频调用成本的窄域判断。 | 不可混用基础版／专项版成绩；专项卡披露训练／校准重叠和继承温度冲突。布尔标签可能主导 noul／choice；语义标签也不能保证否定句安全。官方称 action.act_probability 几乎恒为 1，不适合作为执行门槛；confidence 也需在实际任务上验证。 |
| [Kev](https://github.com/jaredpalmer/kev) | Qwen 骨干与动态 pointer head 的类型化判断系列；Kev 1.0 将现有检查点固定为发布基线。 | 可检查、可微调的领域监督判断实验底座。 | 须区分训练任务族测试与迁移测试。27B v2 在长合同上退步且过度自信（CUAD ECE 0.053，v1 为 0.007）；可接收长度和拟合温度不保证新任务的准确率或校准。 |
| [Contrastive Language Models (CLM)](https://github.com/Contrastive-LM/CLM) | 冻结语言模型编码器，分别表示状态与动作，再用可训练投影头匹配。 | 适合候选可复用的工具目录、排序及领域 Best-of-N 选择。 | 相对排序不能保证识别“全部候选都错”；Best-of-N 成绩不代表模型独立解题能力。 |
| [Bespoke Nimble](https://github.com/bespokelabsai/nimble) | Qwen 监督适配器，直接读取答案标签 logits，而非生成解释。 | 适合证据敏感的判断，也可借鉴最小差异训练样本。 | 对比式样本构造不等于 CLM 的对比表示训练；公开比较由项目方运行，完整逐行输出并未全部提交。 |
| [GLiNER2.5-Decide](https://huggingface.co/fastino/GLiNER2.5-Decide-1B) | 通过运行时标签与多个判断头实现模式条件化的本地分类。 | 适合轻量业务分类；跨字段约束需核对具体运行库支持。 | 本版核对的是 1B 模型卡，其中交叉报告 340M 成绩；数据集审计未完成，表中 JevK5 不是 TypeSafe Jev。 |
| [GLiClass](https://github.com/Knowledgator/GLiClass) | 以用户提供的标签为条件进行文本分类，包含多标签任务。 | 动态意图与标签分类的重要相邻基线。 | 分类能力不等于通用工作流验收能力，也不保证业务风险已校准。 |
| [jevos](https://github.com/feder-cr/jev) | 通过 llama.cpp 以 GGUF 格式提供本地是非判断，`noul` 请求与响应采用 TypeSafe Jev 的接口格式。 | 用于探索 CPU 本地文本判读与分流；将完整规则写入 `instructions`，并用自己的标注样例验证行为。 | 仅支持是非判断：`choice`、`score` 返回 422，jevos 文档说明 `criteria` 虽被接受却不参与判断。接口格式兼容不等于语义等价。算术、日期错误及评测敏感性由作者自报；旧版 README 的成绩不能代表 v2。 |
| [Clef / Clef-Flash](https://huggingface.co/Cloudflare/clef) | 多模态 Qwen 骨干加联合 schema 判断头，输出类型化决策，提供 Jev/SystemOne 兼容封装。 | 比较文本／图像分类、分流与有序评分，并按具体任务衡量错误成本。 | 厂商评测存在任务间取舍；接口兼容和概率输出不等于业务风险已校准，本地推理需要定制 schema 运行代码。 |
| [Strands Decider](https://github.com/strands-labs/strands-decider) | Qwen3.5 与 Gemma 4 pointer-head 系列；10 月 v1 发布平均三个训练适配器／判断头后再校准。 | 可作为短文本分类和领域监督判断的本地基线；用实际流量测试问题变化、选项顺序和风险—覆盖率。 | Qwen v1 数据构建器尚未进入 main；若干 dev 评测对应训练划分已用于训练。E2B index 先于 CUDA 注意力修复；Qwen v1 缺图时 POPE 过度自信恶化。E07／E08 保留为历史，不能当作当前保证。 |
| [Perplexity pplx-decider-v1-27b](https://huggingface.co/perplexity-ai/pplx-decider-v1-27b) | Qwen3.8-27B 微调模型，公开权重与类型化判断运行代码，支持图像输入。 | 经具体任务验证后，作为文本／图像判读的自部署对照。 | 模型卡成绩来自 Perplexity API；与本地权重是否等价未验证。完整训练数据、校准验证及原始评测产物尚未确证。 |
| [Microsoft-Decision-1](https://ai.azure.com/catalog/models/Microsoft-Decision-1) | 托管的 Qwen3.5-9B 后训练模型，对有限选项评分。 | 比较分类、路由和按标准评分。 | 厂商比较缺少已审计的逐项产物；熟悉任务的校准不保证迁移，措辞与安全判断仍可能出错。 |
| [OpenAI Decisions API / GPT-6 Luna](https://developers.openai.com/api/docs/guides/decisions) | 面向文本与图像的类型化判断 API，处于公开测试。 | 托管分类、路由与有序评分。 | 拒答为单独返回类型，不等于校准后的拒判；confidence 需在目标任务验证，训练与服务身份尚未披露。 |
| [Nace Drex v1.5](https://github.com/nace-ai/drex-decision-models) | MiMo-V2.6-Distill-Qwen-9B 骨干加 Kev pointer head，提供公开权重发布链接。 | 本地文本／JSON 判断候选，可测试长输入。 | 使用基准训练划分，不能视为未知领域零样本；公开 Index 0.3.1 前列处于平局带内，小规模运行器核对不证明普遍等价。 |
| [vLLM-SR Decision 3.0](https://huggingface.co/collections/vllm-sr/decision-30) | 六个多模态 code-readout 检查点；10 月 14 日新增原生 vLLM main 支持，每题仍独立读取 prompt。 | 本地文本／图像／视频分类、评分与路由；固定输入和候选预算比较各型号。 | Index 各版本与公共分数不可混用；权重／校准标识未变，文本数值领先者处于共享第一平局带。原生 vLLM 需合并后／nightly 版本，集成报告未测 LoRA 和 CUDA。 |
| [Intern-Decision](https://github.com/internlm/Intern-Decision) | Qwen3.5 多模态 0.8B／2B／4B 系列，在一个因果 masked assistant skeleton 中评分多个类型化字段。 | 与每题独立模型比较多字段成本和字段／顺序敏感性，测试基于图像证据的判断。 | 原始训练／校准记录私有；96-case 分布试验只作诊断。型号／后端专属温度与 max(P) confidence 不能直接保证业务风险。 |
| [Verdict / OpenJev](https://github.com/Heman10x-NGU/Verdict-open-jev) | 151M ModernBERT／GLiClass 候选分类器，含显式证据不足选项及 per-K 校准。 | 轻量意图分类与缺少正确选项测试；核对实际服务概率和评测 renderer／校准器。 | 作者测试显示 hard negative 和同义改写下拒答崩塌；转换者报告实际服务校准与保留集评测明显不同，不能保证跨域拒答可靠性。 |

### 重要成绩必须连同条件阅读

- [E01 — Laya：专项训练收益与校准数据问题需要分开。](docs/evidence.md#e01)
- [E02 — CLM：在 38 个保留任务上选择候选，不是独立完成编码。](docs/evidence.md#e02)
- [E03 — Nimble / Jev：配对人工标签评测仍须按任务解读。](docs/evidence.md#e03)
- [E04 — GLiNER2.5-Decide：新评测范围、来源可见性与名称辨别。](docs/evidence.md#e04)
- [E05 — Kev：区分开发集、测试集与来源域。](docs/evidence.md#e05)
- [E06 — Clef：厂商比较中的任务取舍，不是通用胜出。](docs/evidence.md#e06)
- [E07 — Strands Decider：问题指令敏感性与实验选择限制。](docs/evidence.md#e07)
- [E08 — Strands v21：发布种子与同机多种子比较。](docs/evidence.md#e08)
- [E09 — Drex v1.5：公开套件平局与基准训练重叠。](docs/evidence.md#e09)
- [E10 — Microsoft-Decision-1：作者报告的扰动稳定性。](docs/evidence.md#e10)
- [E11 — Strands Qwen v1：新配方、种子平均及缺图限制。](docs/evidence.md#e11)
- [E12 — Decision 3.0：内部 Index 与单设备延迟边界。](docs/evidence.md#e12)
- [E13 — Decision 3.0：完整公共套件与其他协议分开。](docs/evidence.md#e13)
- [E14 — Decision 3.0 视频：采样帧问答不验证音频或实时可靠性。](docs/evidence.md#e14)
- [E15 — Decision 3.0 Core ML：转换与公共评测证据。](docs/evidence.md#e15)
- [E16 — Decision 3.0 PR 分流：吞吐与真实标签一致率分开。](docs/evidence.md#e16)
- [E17 — WebMCP 应用：小样本差异与前置规则错误。](docs/evidence.md#e17)
- [E18 — Intern-Decision：精确分布校准试验。](docs/evidence.md#e18)
- [E19 — Verdict 部署：评测校准不等于实际服务校准。](docs/evidence.md#e19)
- [E20 — Verdict 拒答：保留 hard negative 与同义改写失败。](docs/evidence.md#e20)
- [E21 — Decision 3.0：0.3.2 评分变化与不变的权重标识。](docs/evidence.md#e21)
- [E22 — Decision 3.0：批处理吞吐、延迟与过载边界。](docs/evidence.md#e22)
- [E23 — 原生 vLLM D3：已合入源码与有限工程测试。](docs/evidence.md#e23)
- [E24 — 财报变化：条件标签和不等长文本窗口。](docs/evidence.md#e24)
- [E25 — 8-K 分类：监督标签与事后选择。](docs/evidence.md#e25)
- [E26 — SEC 后续问询：90 日预测不同于文本完整性。](docs/evidence.md#e26)
- [E27 — 语义特征：开发集内发现与葡萄酒评分预测。](docs/evidence.md#e27)
- [E28 — EcomMIR：多模态场景与意图的组合竞赛方案。](docs/evidence.md#e28)

领域评测、训练支持核查与未知／澄清策略见[图片意图适配流程](docs/selection-guide.md#image-intent-adaptation)。详细[多模态微调研究方案](docs/multimodal-decision-finetuning.zh-CN.md)比较同骨干短标签 SFT 与候选读出，核查真实图像训练路径，并定义风险／成本验收。

零样本分类、专项微调与 Best-of-N 选择不是同一个问题。本地 GPU 前向耗时与远程 API 往返耗时，也不是同一种性能测量。

## 应该保留的基线

新术语不能证明旧方法已经过时。这些基线有助于判断收益究竟来自数据、输出约束、模型结构还是训练目标。

部署资源也用于核对本地实现是否保留原有判断行为；转换等价须与任务质量分开。

- **[SetFit](https://github.com/huggingface/setfit)** — 少样本句向量适配，再训练分类头。 不等于任意类型化问题接口。
- **[Qwen3-Reranker](https://huggingface.co/Qwen/Qwen3-Reranker-0.6B)** — 面向查询与文档的任务专用重排。 相关性分数不是业务正确概率。
- **[Outlines](https://github.com/dottxt-ai/outlines)** — 为普通语言模型提供受约束结构化输出。 模式合法不保证事实正确。
- **[TabICLv2](https://arxiv.org/abs/2602.11139)** — 用于表格分类与回归的基础模型。 按论文收录；未本地复现，不外推自然语言能力。
- **[FluidUse / decision-model Core ML deployment](https://github.com/FluidInference/FluidUse)** — Apple 部署资源，含原生 Swift manager 与 Python 辅助 Core ML bridge，支持 Decision 3.0 等。 转换等价和 smoke test 不保证质量；须匹配长度 bucket、精度、tokenizer、校准器与媒体路径。bridge 调用串行排队，超时会关闭 session；文档中的自动下载／环境安装本轮未运行。
- **[Semantic features + supervised predictor](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery)** — LLM 提议问题，Jev 将文本转成语义特征，再由监督 CatBoost 预测任务标签。 葡萄酒回归属于作者报告；特征发现须限制在开发划分，训练下游模型不等于微调 Jev，也不证明金融／多模态泛化。
- **[ezjev text candidate-logit LoRA](https://github.com/everettjf/ezjev/tree/8b3d88957c0795bea160c8fbc9c6d2a54b051136)** — 可检查的逐题候选 CE＋Brier、回放及温度拟合，训练路径使用 Qwen3.5 文本输入。 不是图像微调实现；MIT 仅覆盖代码，部分训练数据为非商业许可或未说明条款；未在此复现训练或校准。
- **[decision-pacman decision distillation](https://github.com/grapeot/decision-pacman/tree/593ed1f59f4f97ad0bda7287ff304e9667360089)** — 用文本状态的教师／模拟器标签训练小型候选分布 LoRA 学生。 游戏专项作者报告同时存在通用能力下降；不证明图像训练或客服泛化，完整数据／评测产物未审计。

能够用规则或普通监督分类器解决的任务，也应保留相应对照。只有可靠地增加了价值，复杂性才值得付出。

## 路由与结果反馈学习

- **[RouteLLM](https://github.com/lm-sys/RouteLLM)** — 利用学习到的信号在强模型与便宜模型间路由。 效果依赖候选模型、流量与路由训练分布。
- **[LLMRouter](https://github.com/ulab-uiuc/LLMRouter)** — 构建和比较路由策略的研究基础设施。 2026 年 8 月论文为预印本；基础设施不是已证明的最优策略。
- **[Vowpal Wabbit](https://github.com/VowpalWabbit/vowpal_wabbit)** — 在线学习与上下文老虎机工具。 需要合适的日志、探索与评估假设。

选择执行者时，应记录**任务、可用证据、执行者、结果、耗时和成本**。只知道已选执行者的表现，并不知道所有其他执行者会怎样。相关假设可从下方的交接学习与因果研究继续了解。

## 可靠性与评测

- **[MAPIE](https://github.com/scikit-learn-contrib/MAPIE)** — 预测集合、不确定性与保形风险工具。 保证依赖方法、风险目标及数据假设。

- **[Decision Index (archival releases and live board)](https://huggingface.co/spaces/multimodalart/jev-decision-index)** — 具有明确聚合规则的较广覆盖决策评测指数。 10 月 15 日核对了 10 月 14 日生成的 0.3.2 汇总 JSON，私有题目／原始运行仍未审计。文本榜有 0.9 分平局带；0.3.2 含评分／数据修正，不能据此推断重训。
- **[Nimble public evaluations](https://github.com/bespokelabsai/nimble/blob/62076b4f2d365b5879dafcf7f6dd072a1fe76df7/docs/PUBLIC_BENCHMARKS.md)** — 人工参考标签子集、配对比较及校准报告。 由项目方运行；本列表未独立复现。
- **[Decision-model benchmark](https://github.com/nibzard/decision-model-benchmark)** — 用于判断模型比较的第三方代码与协议。 第三方身份本身不保证方法或标签可靠。
- **[Financial-document decision tests](https://insights.ml4trading.io/p/testing-jev-on-financial-documents)** — 原评测者比较 Jev 与监督文本／TF-IDF 模型，分别测试财报变化、8-K 标签和 SEC 后续问询。 厂商提供 API；历史筛选样本含回顾检查、事后提示和划分限制，不能宣布树模型／Jev 通用胜负或投资收益。
- **[MIRE / EcomMIR multimodal intent evaluation](https://github.com/liujunwen23/MIRE/tree/d101287af90d114c5bf0cbfbd56fe9c52358e3bb)** — 图像场景与多轮意图挑战，提供全参数 SFT 基线及已发表的 LoRA 竞赛方案。 EcomMIR 为含 Round 1 伪标签等组合干预的作者报告，不是 LoRA 单项或仅 1,000 样本的未触及测试结果；数据使用权与完整复现仍未核实。

评测应同时看任务质量、关键错误、校准、风险—覆盖率、子群与分布变化，以及完整系统成本。阈值在校准集确定，不能在最终测试集上反复调参。自动放行的案例也必须保留抽检，才能发现“自信地判错”。

## 基础原理与近期研究

建议按“概率质量 → 拒判 → 执行者交接 → 风险控制”阅读。年份是论文或版本时间，不代表穷尽了全部最新文献；只审阅摘要的条目在来源登记中明确标注。

- **[Strictly Proper Scoring Rules (2007)](https://doi.org/10.1198/016214506000001437)** — 为什么对数损失等适当评分规则以真实分布为目标。 理想优化目标不等于部署已校准。
- **[On Calibration of Modern Neural Networks (2017)](https://proceedings.mlr.press/v70/guo17a.html)** — 经验校准及事后温度缩放。 校准不能修复错误排序或证据缺失。
- **[Selective Classification (2017)](https://arxiv.org/abs/1705.08500v2)** — 带拒判的分类与风险／覆盖率权衡。 原始实验不是无关 LLM 任务的保证。
- **[Learning to Defer to an Expert (2020)](https://proceedings.mlr.press/v119/mozannar20b.html)** — 联合学习预测与向专家交接。 不能假设人工与工具不会犯错。
- **[Conformal Risk Control (2022; reviewed v4)](https://arxiv.org/abs/2208.02814v4)** — 在明确条件下校准风险控制程序。 检查交换性、损失与单调性等假设。
- **[Non-Monotonic Conformal Risk Control (2026)](https://arxiv.org/abs/2602.20151v1)** — 将风险控制讨论扩展到非单调损失。 预印本；依赖稳定性的界，不是无条件安全。
- **[Proper Scoring Rules: 2026 review](https://doi.org/10.1146/annurev-statistics-042424-050626)** — 近期关于估计与预测评估的适当评分综述。 基于摘要与出版元数据收录。
- **[Causal Learning to Defer (AAAI 2026)](https://ojs.aaai.org/index.php/AAAI/article/view/39493)** — 研究存在隐藏混杂时的交接学习。 相邻研究，不是即用型生产路由器。
- **[Jev in the Wild (2026)](https://arxiv.org/abs/2609.30216)** — 基于 2,170 个公开 GitHub Jev 项目的数据驱动综述与分析，涵盖早期增长、应用领域及决策用途分布。 公开仓库数量不能证明实际部署规模或模型准确率；此处仅核读摘要，未独立复现。

## 相关资料库

以下项目提供互补的发现入口。本仓库侧重任务分类、机制比较与结论级证据记录，不复制它们的全部链接，也不按 Star 排序。

- **[Awesome System One](https://github.com/andyrewlee/awesome-system-one)** — 最接近主题的生态列表，适合发现项目。 本版收录不代表认可其中每个条目。
- **[Awesome Jev 中文](https://github.com/yzfly/awesome-jev-zh)** — Jev 生态的中文资料。 本版收录不代表认可其中每个条目。
- **[Awesome LLM Routing and Cascading](https://github.com/ymoslem/awesome-llm-routing-cascading)** — 专门的路由与级联文献目录。 本版收录不代表认可其中每个条目。
- **[Awesome Conformal Prediction](https://github.com/valeman/awesome-conformal-prediction)** — 专门的不确定性与保形预测资料。 本版收录不代表认可其中每个条目。
- **[Awesome Martech AI](https://github.com/leoncuhk/awesome-martech-ai)** — 涵盖营销数据、智能、决策、激活和测量的资源及实践指南。 相关导航不构成独立产品验证；合成演示不证明客户业务增量。

## 维护与贡献

事实资料保存在 [`data/catalog.json`](data/catalog.json)，性能声明保存在 [`data/evaluations.json`](data/evaluations.json)。首页和详细表格由同一份数据生成，避免中英文成绩各自漂移。

```sh
python3 scripts/render.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

仓库包含[资料维护 Skill](.agents/skills/decision-models-curator/SKILL.md)和[每周来源检查工作流](.github/workflows/source-watch.yml)。前者规定怎样研究，后者发现来源变化并维护待审核 Issue。**工作流不会自动运行 AI 研究、改写结论或合并代码，也不需要付费模型 API。** 启用条件、调度限制和手动运行方式见[维护说明](docs/maintenance.md)。

新增项目或成绩前请阅读 [CONTRIBUTING](CONTRIBUTING.md)。欢迎负面结果、假设变化与纠错。[首版核验记录](updates/2026-09-25.md)保留原始限制；[10 月 6 日发布核验记录](updates/2026-10-06-release-boundaries.md)与[10 月 11 日核验记录](updates/2026-10-11-typed-releases.md)说明新增、修正及证据缺口；[10 月 13 日多模态／部署核验](updates/2026-10-13-multimodal-deployment.md)区分新发布、校准和应用证据；[10 月 15 日更新](updates/2026-10-15-serving-and-adaptation.md)核查原生 vLLM、评分变化、语义特征与领域适配；[10 月 16 日研究更新](updates/2026-10-16-multimodal-finetuning.md)补充训练路径与竞赛证据核查；[发布说明](PUBLISHING.md)提供面向空仓库的安全初始化步骤。

原创代码与整理文字使用 [MIT](LICENSE)；链接的项目、模型、数据与论文保留各自许可证。固定来源文档的提交版本，**不等于**固定模型权重。
