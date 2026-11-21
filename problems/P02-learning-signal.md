# P02 适配的学习信号：CE、蒸馏、软标签还是 RL

成熟度：**有据** · 层：判断本身 · 落地：[通用流程 §2](../playbooks/decision-pipeline.md#method-selection)

## 问题

用企业数据训练决策模型，用哪种信号：CE/BCE、教师 soft/KL、思考到读出的自蒸馏、RLCD、RLAF、GRPO、PRDO，还是部分反馈（CAPS）？

## 当前判断

有可信标签时，**CE/BCE 加合适底座的参数适配是默认起点**。其他信号都可能有用，但目前没有一项在等数据、等算力的对照下默认胜过直接监督。教师用来补标签缺口；RL 只在“策略错误确是瓶颈且有可验证反馈”时立项。置信度：中。

## 证据

支持：
- 同预算下，4B QLoRA 直接适配有领域增量；通用 decision 适配也可能负迁移（[标签预算 v2](https://arxiv.org/html/2610.26325v2)）。
- Inner Jev 中 Gemma 31B 把 soft 换成 hard，未检出能力差异（[2610.17205](https://arxiv.org/html/2610.17205v1)）。
- Laya 三个配对种子分不出 soft-CE 与 RLCD（[E42](../docs/evidence.md#e42)）。
- 窄覆盖适配会让跨题型表现退化：231 题 JevBench 一列从 81.4 降到 74.9（[LLM-as-Jev v3](https://arxiv.org/html/2610.02076v3)）。
- 唯一有线上比较的企业案例（Amazon 多轮意图）用的是“教师解释＋自检＋人工审核”产出的标签，再训练 RoBERTa 学生（[E43](../docs/evidence.md#e43)、[E44](../docs/evidence.md#e44)）。

反证或条件性正例：
- Drex Max 追加 RLAF 阶段后 DI 64.9 → 66.9，但缺少等算力继续 SFT 的对照和种子控制（[E45](../docs/evidence.md#e45)）。
- PRDO 在保留推理的设置下，Brier 和 AURC 相对 GRPO＋TS 有改善；0.6B 数学验证的准确率反而下降（[E40](../docs/evidence.md#e40)）。
- CAPS 在 10 选 1 的模拟日志上优于 positive-only，但日志是唯一 gold 的正误反馈，不是自然企业日志。

实现层面：Unsloth `DecisionTrainer` 原生支持 hard／soft 目标、Brier、ordinal 项，以及对参考头的 KL 锚定（[源码](https://github.com/unslothai/unsloth/blob/8b7cde79ebf5a901b2fd936bbee214fb8c7562c7/unsloth/models/decision.py)）。hard 与 soft、加不加锚定的对照，现在在同一实现里改一个参数就能做，不需要各自搭训练器。它的校准代码注释写明：用 soft 目标训练会使 Clef 式头偏向低置信，所以校准统一按 hard gold 拟合。这是实现者的观察，不是受控实验结论。

## 开放

- **中文长状态**：0.6–4B LoRA 能否胜过现代多语 encoder？目前的新研究主要是英语。
- **标签形式**：hard 与 soft 应按标签性质选择。可复核的真实分歧才保留分布；教师 logit、口述置信度、采样频率不是同一种信号。
- **部分反馈**：见 [P10](P10-repair-actions.md)。

最小实验：同一合同、同一分组留出集，比较冻结 embedding＋小头、多语 encoder 监督、0.6–4B LoRA，并画学习曲线（例如 200 / 1k / 5k 标签）。之后只对剩余的标签缺口加入教师，在同一批保留样本上比较 hard 与 soft。

停止条件：encoder 或托管 API 已在预定非劣界内达标时，不训练决策底座。

## 企业含义

各方法需要什么数据、用什么实现、怎样在同一张表上比较，见[通用流程：方法与数据视图](../playbooks/decision-pipeline.md#method-views)和[统一评测协议](../playbooks/decision-pipeline.md#unified-evaluation)。


首轮只跑三组。不要默认走“教师 soft → 27B → 4B → 每周 CAPS → PRDO”这条链。使用 Jev 的输出训练竞争模型有条款风险。

## 关键阅读

[标签预算 v2](https://arxiv.org/html/2610.26325v2) · [Inner Jev](https://arxiv.org/html/2610.17205v1) · [Drex v2](https://arxiv.org/html/2611.07854v2) · [PRDO v2](https://arxiv.org/html/2609.38850v2) · [CAPS](https://arxiv.org/html/2611.15572v1)
