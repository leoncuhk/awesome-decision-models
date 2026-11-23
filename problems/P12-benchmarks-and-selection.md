# P12 评测碎片化与选型经济学

成熟度：**共识** · 层：评测与选型 · 落地：[通用流程 §2](../playbooks/decision-pipeline.md#model-candidates)

## 问题

公开指数各测各的，很多是作者自评；不同协议的头部名次尚不能证明能力已收敛。企业该怎样评测、怎样选型？

## 当前判断

1. **榜单名次是候选发现信号，不是企业选型结论。** 自建冻结评测集，按客户、会话、时间分组留出。
2. **选型的准入门槛依次是**：许可 → 自有数据训练入口 → 目标硬件可训（forward/backward/保存重载）→ 服务概率与评测一致。全部通过后才比较质量。

置信度：中高。

## 证据

评测碎片化：
- HF 社区 Decision Index 从 0.3.2 到 0.4，评分和数据都改了；0.4 的文本 Full 全部改为私有题，有 0.9 分的平局带。
- [AA Index v2](https://artificialanalysis.ai/articles/decision-index-v2)：私有数据占比 45%，Brier 进入主分；前三名 Drex Max v1.1 / GLiDE v1.2 / Mammoth 27B 分别为 73 / 73 / 72。
- Public 不等于 Full 的又一例：LemonDecider 公告称 DI 0.4.1 Public 61.67 分、Jev 1.14 为 60.7 分，但 0.4 的文本 Full 只由私有题决定，这不能说明“跑赢 Jev”。
- 作者自建自评：StartLux 的 DecisionPivot；SII 用 JEVal 评测自家模型。StartLux 在 10 月 DI 上的第一名，到 DI 0.4.1 已不再是第一（[E29](../docs/evidence.md#e29)）。

选型经济学：
- 同一指数内成本从 $14 到 $859 / 1M tasks，跨度约 60 倍。
- 许可差异：StartLux 权重 CC BY-NC；Jeff 发布权重非商用；GLiDE 有收入门槛；Liquid 有商业收入门槛。
- 训练入口：Jev 不提供客户微调；GLiDE 和百炼提供托管训练；Kev、Valen、Strands v2、RSI、Jeff 有公开训练代码，多数走 CUDA。Unsloth（2026-11）把“受支持LLM加决策头”做成通用框架，覆盖 CUDA 和 Apple Silicon，并提供本地兼容 Jev 接口的 Decision API。这增加了可审查实现，但不等于任意专用checkpoint可续训或M5已可运行；许可（决策模块AGPL-3.0-only）、底座、设备与数据仍分别准入。
- 版本：托管服务的别名不冻结模型身份；Git commit、HF revision、权重哈希、API 版本是不同的标识。

2026-11-23覆盖审查：此前只比较熟悉的4B项目，遗漏Adjudex等更强原版候选。现在从完整榜单按总参数筛选，保留每一项的分数、精确发布revision、许可与训练审查深度，见[69行覆盖表](../playbooks/assets/4b-candidate-audit.csv)及[候选准入](../playbooks/decision-pipeline.md#small-model-coverage)。访问失败不等于闭源；有推理代码不等于完整trainer；存在trainer也不等于目标机已经训练成功。

## 企业含义

- 首轮候选限于少数，见[通用流程的候选表](../playbooks/decision-pipeline.md#model-candidates)。
- 记录每次运行的精确标识，包括模型、revision、运行时、校准器。
- 零样本、任务微调、Best-of-N 回答的是不同问题；本地 forward 时间和 API 往返时间是不同测量，不混成一张榜。

## 关键阅读

[领域图谱 §3](../docs/landscape.md#3-评测体系协议不同分数不混) · [模型卡](../docs/models.md) · [方法论](../docs/methodology.md)
