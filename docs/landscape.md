# 领域图谱：机制、生态与评测

更新：2026-11-21。本页回答“这个领域由哪些部分组成”。“该信什么”见 [problems/](../problems/)，“怎么落地”见 [playbooks/](../playbooks/)。逐模型事实见[模型卡](models.md)。

## 1. 六个层次，分开比较

同一个概率向量 API，背后可能是完全不同的系统。比较两个模型之前，先逐层对齐：

| 层次 | 要问的问题 |
|---|---|
| 输出合同 | 互斥单选、独立命题、有序等级，还是多标签？候选是否运行时给出？有没有 NONE？ |
| 读出 | 词表行（选项字母）、独立答码头（如 255 码）、pointer head、分类头，还是双塔相似度？哪些候选参与归一化？ |
| 注意力 | 提示部分是否双向？共享前缀能否复用？多题是共享状态并行，还是联合注意？ |
| 训练 | 改了哪些参数、用了什么数据和目标（CE、soft KL、RLCD、RLAF、PRDO）？训练代码是否真的公开？ |
| 计算策略 | 何时推理、重读、调用工具、补证据或转交？ |
| 验收 | 完整策略是否满足风险、覆盖、延迟和许可要求？ |

注意：一次读出不以 RL 为前提；训练名称不证明校准；API 兼容不代表语义等价。

## 2. 生态分布（2026-11）

**托管服务**：合同已趋同，差异在模态、版本冻结和数据边界。
- Jev（TypeSafe，1.14）；OpenAI Decisions API（GPT-6 Luna，10-22 GA）；Microsoft-Decision-1.1；Google Gemini Decision 1（11-11，覆盖文本、图像、音频、视频、PDF）；Cloudflare Clef（Workers AI）；Liquid d1.2；Ant LingDT；百炼 decision-model。
- 关键差异：能否客户微调（Jev 不能，GLiDE 和百炼可以）；版本别名是否冻结；confidence 的定义。

**开放权重家族**：35 族，大致分三类：
- 有可续训入口：Kev、Valen、Strands v2、RSI-Jev、Jeff、Mapika、SII（需特定字段）。
- 主要提供推理和服务：Drex、Mammoth、PPLX Decider、StartLux（权重非商用）、D3、Decisio、Span-02。
- 小模型和 encoder：Laya、GLiClass、GLiNER-Decide、Verdict、MNN-Pocket-0.3B、jevos（CPU）。

**训练与方法**：
- 直接监督（CE/BCE + LoRA）是共同底座。
- 变体：soft target 蒸馏、思考到读出的自蒸馏（SII）、RLCD／RLCD²（StartLux）、RLAF（Drex）、PRDO（逐推理 proper score）、CAPS（chosen-action 部分反馈）。

**相邻工具**：SetFit、Qwen3-Reranker、Outlines（结构化输出）、RouteLLM／LLMRouter（路由）、Vowpal Wabbit（bandit）、MAPIE（conformal）、Parlant（规则匹配引擎）。

## 3. 评测体系：协议不同，分数不混

| 基准 | 测什么 | 读法 |
|---|---|---|
| HF 社区 Decision Index（0.3.2 / 0.4.x） | 多任务汇总；0.4 文本 Full 全部私有 | 版本间评分规则不同，不能当作模型增益；0.9 分平局带 |
| [AA Decision Index](https://artificialanalysis.ai/articles/decision-index-v2) v1.0 / v2 | v2 = 50×(1+准确率−Brier)，45% 私有 | 校准进入主分；前三相差 1 分以内 |
| JEVal v2 | 中英多领域本地判断 | SII 作者评测自家模型；分母口径不同 |
| DecisionPivot | 13 个对比族的程序化标签 | StartLux 作者自建、自评 |
| TypedBench、[2610.00346](https://arxiv.org/html/2610.00346v2) | 校准、措辞敏感性、成本；对比训练分类器 | 第三方；出厂校准取决于模型×任务 |
| [To Jev or Not to Jev](https://arxiv.org/abs/2611.00505) | 用作 LLM 评审，含注入测试 | 第三方、预先声明协议；英文公开基准 |
| [Reading Right, Acting Wrong](https://arxiv.org/abs/2610.18579) | agent loop 中的读错与做错 | 初版；冻结的模拟状态 |

规则：零样本、任务微调、Best-of-N 回答的是不同问题；本地 GPU forward 时间和远程 API 往返时间是不同测量。本仓不制作混合排行榜。

## 4. 演进脉络

| 时间 | 阶段 | 标志 |
|---|---|---|
| 2026-09 | 合同确立 | Jev 发布（09-15），开源复现与小模型涌现（Laya、Kev、CLM、Nimble） |
| 2026-10 | 发布潮 | Clef、D3、Intern、StartLux、PPLX、Drex；OpenAI GA；HF DI 0.4 改为私有 Full；第三方校准审计出现 |
| 2026-11 上 | 托管收敛，评测转向 | Google Gemini Decision（11-11）；AA v2 把 Brier 计入主分（11-08）；judge 横评与 agent loop 诊断 |
| 2026-11 中 | 训练入口开放 | GLiDE 训练 API、Valen native 续训、Strands v2、Jeff 训练器；企业多轮意图线上比较（Amazon） |

下一阶段的看点：作为评审与评测层落地（[P09](../problems/P09-judge-layer.md)）；策略级风险认证（[P05](../problems/P05-policy-risk.md)）；部分反馈学习（[P10](../problems/P10-repair-actions.md)）；读出与推理的按需分配（[P03](../problems/P03-read-or-reason.md)）。
