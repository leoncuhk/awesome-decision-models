# Awesome Decision Models

**面向 AI 系统可靠判断的模型、方法与实证资料。**

[English](README.md) · [模型卡](docs/models.md) · [评测证据](docs/evidence.md) · [选型指南](docs/selection-guide.md) · [收录与评测方法](docs/methodology.md) · [来源登记](docs/sources.md)

收录用于**分类、评分、排序、验证、路由与拒判**的模型和方法。我们关心的不是谁的宣传数字更高，而是：**在具体任务中，哪种方法能以可接受的风险和总成本，交付可验收的结果。**

**本版来源核验日期：2026-09-25。** 精选 30 项资源，其中 7 个核心模型系列、5 条带协议背景的评测记录。本版完成的是公开资料核验，**没有宣称独立运行并复现这些模型**。阅读深度、版本固定情况与未解决的资料缺口均见[来源登记](docs/sources.md)。收录不等于背书，也不等于通过生产可靠性认证。

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
| [Jev / TypeSafe](https://typesafe.ai) | 托管的结构化判断服务：对选项、命题与有序评分标准输出分布。 | 验证判断节点价值时，可作为无需自建部署的对照。 | RLCD 的完整训练配方未公开；格式合法与置信度字段不等于语义可靠。 |
| [Laya](https://github.com/NandhaKishorM/laya) | 小型编码器与动态选项判断头；包含通用、多语言及工作流专项检查点。 | 适合有领域训练数据、需要控制高频调用成本的窄域判断。 | 不可混用基础版与专项版成绩；专项卡明确披露训练与校准数据重叠及温度配置冲突。 |
| [Kev](https://github.com/jaredpalmer/kev) | Qwen 骨干、适配器及动态 pointer head，配套类型化判断训练和部署工具。 | 可检查、可微调的领域监督判断实验底座。 | 新来源开发集、最终测试集与已训练来源成绩不同；适配器大小不是部署内存。 |
| [Contrastive Language Models (CLM)](https://github.com/Contrastive-LM/CLM) | 冻结语言模型编码器，分别表示状态与动作，再用可训练投影头匹配。 | 适合候选可复用的工具目录、排序及领域 Best-of-N 选择。 | 相对排序不能保证识别“全部候选都错”；Best-of-N 成绩不代表模型独立解题能力。 |
| [Bespoke Nimble](https://github.com/bespokelabsai/nimble) | Qwen 监督适配器，直接读取答案标签 logits，而非生成解释。 | 适合证据敏感的判断，也可借鉴最小差异训练样本。 | 对比式样本构造不等于 CLM 的对比表示训练；公开比较由项目方运行，完整逐行输出并未全部提交。 |
| [GLiNER2.5-Decide](https://huggingface.co/fastino/GLiNER2.5-Decide-1B) | 通过运行时标签与多个判断头实现模式条件化的本地分类。 | 适合轻量业务分类；跨字段约束需核对具体运行库支持。 | 本版核对的是 1B 模型卡，其中交叉报告 340M 成绩；数据集审计未完成，表中 JevK5 不是 TypeSafe Jev。 |
| [GLiClass](https://github.com/Knowledgator/GLiClass) | 以用户提供的标签为条件进行文本分类，包含多标签任务。 | 动态意图与标签分类的重要相邻基线。 | 分类能力不等于通用工作流验收能力，也不保证业务风险已校准。 |

### 重要成绩必须连同条件阅读

- [E01 — Laya：专项训练收益与校准数据问题需要分开。](docs/evidence.md#e01)
- [E02 — CLM：在 38 个保留任务上选择候选，不是独立完成编码。](docs/evidence.md#e02)
- [E03 — Nimble / Jev：配对人工标签评测仍须按任务解读。](docs/evidence.md#e03)
- [E04 — GLiNER2.5-Decide：新评测范围、来源可见性与名称辨别。](docs/evidence.md#e04)
- [E05 — Kev：区分开发集、测试集与来源域。](docs/evidence.md#e05)

零样本分类、专项微调与 Best-of-N 选择不是同一个问题。本地 GPU 前向耗时与远程 API 往返耗时，也不是同一种性能测量。

## 应该保留的基线

新术语不能证明旧方法已经过时。这些基线有助于判断收益究竟来自数据、输出约束、模型结构还是训练目标。

- **[SetFit](https://github.com/huggingface/setfit)** — 少样本句向量适配，再训练分类头。 不等于任意类型化问题接口。
- **[Qwen3-Reranker](https://huggingface.co/Qwen/Qwen3-Reranker-0.6B)** — 面向查询与文档的任务专用重排。 相关性分数不是业务正确概率。
- **[Outlines](https://github.com/dottxt-ai/outlines)** — 为普通语言模型提供受约束结构化输出。 模式合法不保证事实正确。
- **[TabICLv2](https://arxiv.org/abs/2602.11139)** — 用于表格分类与回归的基础模型。 按论文收录；未本地复现，不外推自然语言能力。

能够用规则或普通监督分类器解决的任务，也应保留相应对照。只有可靠地增加了价值，复杂性才值得付出。

## 路由与结果反馈学习

- **[RouteLLM](https://github.com/lm-sys/RouteLLM)** — 利用学习到的信号在强模型与便宜模型间路由。 效果依赖候选模型、流量与路由训练分布。
- **[LLMRouter](https://github.com/ulab-uiuc/LLMRouter)** — 构建和比较路由策略的研究基础设施。 2026 年 8 月论文为预印本；基础设施不是已证明的最优策略。
- **[Vowpal Wabbit](https://github.com/VowpalWabbit/vowpal_wabbit)** — 在线学习与上下文老虎机工具。 需要合适的日志、探索与评估假设。

选择执行者时，应记录**任务、可用证据、执行者、结果、耗时和成本**。只知道已选执行者的表现，并不知道所有其他执行者会怎样。相关假设可从下方的交接学习与因果研究继续了解。

## 可靠性与评测

- **[MAPIE](https://github.com/scikit-learn-contrib/MAPIE)** — 预测集合、不确定性与保形风险工具。 保证依赖方法、风险目标及数据假设。

- **[Decision Index 0.2](https://huggingface.co/spaces/multimodalart/jev-decision-index)** — 具有明确聚合规则的较广覆盖决策评测指数。 综合指数不是准确率；API 与 GPU 延迟并非受控硬件实验。
- **[Nimble public evaluations](https://github.com/bespokelabsai/nimble/blob/62076b4f2d365b5879dafcf7f6dd072a1fe76df7/docs/PUBLIC_BENCHMARKS.md)** — 人工参考标签子集、配对比较及校准报告。 由项目方运行；本列表未独立复现。
- **[Decision-model benchmark](https://github.com/nibzard/decision-model-benchmark)** — 用于判断模型比较的第三方代码与协议。 第三方身份本身不保证方法或标签可靠。

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

## 相关资料库

以下项目提供互补的发现入口。本仓库侧重任务分类、机制比较与结论级证据记录，不复制它们的全部链接，也不按 Star 排序。

- **[Awesome System One](https://github.com/andyrewlee/awesome-system-one)** — 最接近主题的生态列表，适合发现项目。 本版收录不代表认可其中每个条目。
- **[Awesome Jev 中文](https://github.com/yzfly/awesome-jev-zh)** — Jev 生态的中文资料。 本版收录不代表认可其中每个条目。
- **[Awesome LLM Routing and Cascading](https://github.com/ymoslem/awesome-llm-routing-cascading)** — 专门的路由与级联文献目录。 本版收录不代表认可其中每个条目。
- **[Awesome Conformal Prediction](https://github.com/valeman/awesome-conformal-prediction)** — 专门的不确定性与保形预测资料。 本版收录不代表认可其中每个条目。

## 维护与贡献

事实资料保存在 [`data/catalog.json`](data/catalog.json)，性能声明保存在 [`data/evaluations.json`](data/evaluations.json)。首页和详细表格由同一份数据生成，避免中英文成绩各自漂移。

```sh
python3 scripts/render.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

仓库包含[资料维护 Skill](.agents/skills/decision-models-curator/SKILL.md)和[每周来源检查工作流](.github/workflows/source-watch.yml)。前者规定怎样研究，后者发现来源变化并维护待审核 Issue。**工作流不会自动运行 AI 研究、改写结论或合并代码，也不需要付费模型 API。** 启用条件、调度限制和手动运行方式见[维护说明](docs/maintenance.md)。

新增项目或成绩前请阅读 [CONTRIBUTING](CONTRIBUTING.md)。欢迎负面结果、假设变化与纠错。[首版核验记录](updates/2026-09-25.md)说明关键限制；[发布说明](PUBLISHING.md)提供面向空仓库的安全初始化步骤。

原创代码与整理文字使用 [MIT](LICENSE)；链接的项目、模型、数据与论文保留各自许可证。固定来源文档的提交版本，**不等于**固定模型权重。
