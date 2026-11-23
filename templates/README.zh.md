# Awesome Decision Models [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**AI 系统中有界决策的模型、方法与证据，按企业大模型应用真正面对的问题组织。**

[English](README.md) · [问题地图](#problem-map) · [落地手册](#playbooks) · [领域图谱](docs/landscape.md) · [模型卡](docs/models.md) · [证据台账](docs/evidence.md) · [方法论](docs/methodology.md)

决策模型由 TypeSafe 的 Jev 于 2026 年 9 月带火：对给定选项返回**类型化分布**。直接读出是常见实现，推理后读出、逐题前向及服务编排依产品而异。新东西是这个输出合同：它让有界判断可以计价、校准、设门槛。本仓只回答一个问题：**对一个具体决策，哪种方法能以可接受的风险和完整成本得到可接受的结果？**

核查批次 {{DATE}}：{{ENTRY_COUNT}} 项资源，{{CORE_COUNT}} 个核心模型族，{{EVIDENCE_COUNT}} 条证据记录。仅做来源审阅，**尚无本仓独立复现**。收录不代表推荐。

## 仓库怎么组织

| 层 | 回答什么 | 位置 |
| --- | --- | --- |
| 问题 | 知道什么、不知道什么、有多确定 | [problems/](problems/)：一个问题一个文件，含判断、证据、反证、开放实验 |
| 落地 | 企业里怎么做 | [playbooks/](playbooks/)：通用流程加场景手册 |
| 查阅 | 查事实 | [领域图谱](docs/landscape.md)，以及生成的[模型卡](docs/models.md)、[证据](docs/evidence.md)、[来源](docs/sources.md) |
| 规则 | 证据怎么判 | [方法论](docs/methodology.md)、[贡献规则](CONTRIBUTING.md) |

<a id="problem-map"></a>
## 问题地图

成熟度：**共识**＝多来源、含第三方对照；**有据**＝有对照但条件窄；**开放**＝缺关键证据。

| | 问题 | 当前判断 | 成熟度 |
| --- | --- | --- | --- |
| **判断本身** | [P01 输出合同与读出](problems/P01-output-contract.md) | 先定义输出合同；简单读出有据，不能普遍等同 | 有据 |
| | [P02 适配的学习信号](problems/P02-learning-signal.md) | 直接 CE/BCE 监督是默认；RL、蒸馏、软标签须证明增量 | 有据 |
| | [P03 读一次还是先推理](problems/P03-read-or-reason.md) | 推理与参考引导有条件收益，须比较完整成本 | 开放 |
| **概率到决策** | [P04 confidence 语义与服务保真](problems/P04-confidence-fidelity.md) | confidence 只是接口字段；按任务、返回对象、服务链路重新校准 | 共识 |
| | [P05 策略级风险认证与漂移](problems/P05-policy-risk.md) | 认证接受策略而非单题置信度；漂移后保证失效 | 理论共识／实证开放 |
| | [P06 缺选项与候选覆盖](problems/P06-candidate-coverage.md) | softmax 发现不了“全错”；NONE 在困难负例下崩溃 | 有据 |
| **系统集成** | [P07 读对了仍然做错](problems/P07-state-and-action.md) | 分别探测事实与动作，区分证据、合同和模型失败 | 有据 |
| | [P08 技能与路径的动态加载](problems/P08-skill-loading.md) | 问题在选错而非上下文长度；优化带回退的加载召回 | 有据 |
| | [P09 System-1 作评审与评测层](problems/P09-judge-layer.md) | 低成本一级评审＋升级是候选，生产成熟度待验 | 有据 |
| | [P10 部分反馈与异质修复动作](problems/P10-repair-actions.md) | 追问、补证、扩候选、转人是不同干预；研究前沿 | 开放 |
| **多模态** | [P11 多模态判断的后训练](problems/P11-multimodal.md) | 视觉常常没有真正参与训练；先验证视觉路径再比质量 | 有据 |
| **选型** | [P12 评测碎片化与选型经济学](problems/P12-benchmarks-and-selection.md) | 名次不是选型信号；按许可、可训练性、硬件、服务保真准入 | 共识 |

<a id="playbooks"></a>
## 落地手册

| 手册 | 适用场景 |
| --- | --- |
| [通用流程](playbooks/decision-pipeline.md) | 任何企业决策：合同 → 方法与底座 → 数据 → 训练 → 验收 |
| [多模态后训练](playbooks/multimodal-posttraining.md) | 截图加意图标签；本地 Mac 训练；G0–G4 关卡 |
| [Skill 路由选择器](playbooks/skill-routing.md) | 几十个技能的服务 Agent；选择器训练、分阶段实验 H1–H6 |

## 核心模型

下表只列机制和建议实验；版本边界、许可与限制见[模型卡](docs/models.md)。不做混合排行：零样本、微调与 Best-of-N 回答的是不同问题。

{{CORE_TABLE}}

## 值得保留的基线

新的训练名称不会让熟悉的基线过时。

{{BASELINES}}

## 路由与从结果中学习

{{ROUTING}}

## 可靠性

{{RELIABILITY}}

## 评测

{{EVALUATION}}

## 基础文献

阅读顺序：概率质量 → 弃权 → 转交执行者 → 风险控制。

{{FOUNDATIONS}}

## 相关列表

{{RELATED_LISTS}}

## 贡献

规范数据在 [`data/`](data/)；README、模型卡、证据和来源页由 `python3 scripts/render.py` 生成。新资料只有在改变某个问题的判断、证据或开放实验时才值得加入，见 [CONTRIBUTING](CONTRIBUTING.md)。变更记录见 [CHANGELOG](CHANGELOG.md)。

原创代码与整理文字采用 [MIT](LICENSE)；所链接的项目、权重、数据与论文保留各自许可。
