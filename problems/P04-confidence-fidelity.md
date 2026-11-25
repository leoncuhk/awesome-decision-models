# P04 confidence 的语义与服务保真

成熟度：**共识** · 层：从概率到决策 · 落地：[通用流程 §6](../playbooks/decision-pipeline.md#enterprise-gates)

## 问题

返回的 `confidence` 代表什么？它在目标任务和实际服务链路上还准吗？

## 当前判断

`confidence` 只是接口字段，通常是返回分布的统计量（最大概率、概率差、1 − 归一化熵），不是独立估计的正确率。必须在目标任务、实际返回的分布、实际服务链路上重新拟合。阈值不跨任务、跨版本、跨服务链路迁移。置信度：高。

## 证据

- 出厂校准取决于“模型×任务”组合；每个任务单独拟合一个温度，几乎能降低所有模型的误差，但不增加区分度（[2610.00346](https://arxiv.org/html/2610.00346v2)）。
- 评测时的校准不等于服务时的校准：Verdict 的服务端概率与留出评测差别很大（[E19](../docs/evidence.md#e19)）。驻留加速会让置信度跨过阈值（[E38](../docs/evidence.md#e38)）。
- ECE 从 54% 降到 2%，正确性 AUROC 仍是 50%：ECE 下降不会带来错误排序能力（[E35](../docs/evidence.md#e35)）。
- 点估计阈值在 190 次评估中失效 147 次（[E37](../docs/evidence.md#e37)）。
- 定义各不相同：D3 的 confidence 是 1 − 归一化熵；GLiDE-2B 公开版是概率差；Gemini 是最高选项概率。
- 行业信号：[AA Index v2](https://artificialanalysis.ai/articles/decision-index-v2) 以 50×(1+准确率−Brier) 计分，校准进入主分。

- Perplexity v1.3的isolated可经state间接串扰，默认separate才是逐题独立合同；Locate与decision混合需分开forward。公开API关闭梯度、推理mask生命周期与保存后的Locate兼容都需单独核验，见[企业适配准入](../playbooks/decision-pipeline.md#pplx-v13-enterprise)。

## 企业含义

- 每个上线判断都要有独立的 Cal-fit 集；温度拟合的对象是实际返回给系统的那个分布。
- 换版本、量化、后端、批处理方式，都要重新校准。温度只拟合一次，不能在导出时重复应用。
- 同时报告 NLL、Brier、ECE（写明分箱方式）和风险—覆盖，不只报 ECE。

## 关键阅读

[Guo et al. 2017](https://proceedings.mlr.press/v70/guo17a.html) · [2610.00346](https://arxiv.org/html/2610.00346v2) · [Confidence Is Not a Promise](https://arxiv.org/html/2610.36311v1)
