# 文档地图：当前判断、证据与实验边界

首轮来源审视截至2026-11-19，整理于11月20日完成；11月20日追加了[后续讨论逐项核查](decision-model-discussion-fact-check-2026-11-20.zh-CN.md)及定向纠错。当前分支为`research/dynamic-skill-loading-2026-11`、[Draft PR #6](https://github.com/leoncuhk/awesome-decision-models/pull/6)。首轮原有29份`docs/**/*.md`加本导航为30份，本轮新增核查后共31份。审视包括全文、相互引用、现行结论与重要主张的一手来源核对；不表示重新检索每个来源、复现模型或验证企业收益。

**当前判断统一在[企业决策模型后训练总览](decision-model-posttraining-enterprise.zh-CN.md)。** 按部署合同与可用学习信号确定候选，不维护一个混合总榜。没有本次目标企业项目或数据；尚未在用户的M5 Pro 48GB执行训练。

## 阅读顺序与责任

| 要解决的问题 | 正本／补充 | 页面状态 |
|---|---|---|
| 为什么训练、目前该研究哪些路线 | [企业后训练总览](decision-model-posttraining-enterprise.zh-CN.md) | 当前综合判断；候选角色、改变判断的条件和实施门槛 |
| 企业到底要判断什么 | [领域路径与标签语义](domain-path-applicability-research.zh-CN.md)、[业务实验合同](dynamic-skill-loading-business-playbook.zh-CN.md) | 当前问题定义与条件性验收步骤，尚无企业执行结果 |
| 论文的数字和方法是否支持推论 | [方法审计](decision-model-posttraining-method-audit.zh-CN.md)、[平台／可训练产物审计](decision-model-posttraining-platform-audit.zh-CN.md) | 有版本的来源、元数据与公开输出复算；保留反例和未知项 |
| 长篇讨论中的每个结论是否成立 | [11月19–20日逐项核查](decision-model-discussion-fact-check-2026-11-20.zh-CN.md) | 按主张分开判定；补StartLux最新榜单、路由协议、CAPS反馈及本仓旧错误，不另建采用排名 |
| 目标机上怎样起步 | [Mac训练准入及实现示例](decision-model-posttraining-mac-recipe.zh-CN.md) | 先核前列候选可行性；Laya附录只示范链路，未执行模型训练 |
| 其他客服系统给了什么证据 | [应用证据](decision-model-application-evidence.zh-CN.md)、[Parlant／Modem／Entagl实现核查](customer-service-implementation-review.zh-CN.md) | 有日期的主题审查；产品合同、代码、历史回放和生产结果分开 |
| 全仓如何比较、记录和解释结果 | [选型通则](selection-guide.md)、[证据方法](methodology.md) | 通用规则；具体企业候选以总览为准 |

## 分开记录的技术维度

| 维度 | 记录内容 |
|---|---|
| 决策合同与基座 | 可见证据、答案语义、语言／上下文；原始底座、精确权重与许可 |
| 读出与运行方式 | 分类头／候选token、单次读出／生成推理、字段及候选的归一化范围 |
| 权重适配 | 只训头、LoRA、全参；实际训练与部署内存、精度及算子 |
| 目标和数据 | CE／Brier／蒸馏／逐推理proper score；人工标签、教师目标、最小事实改动与日志反馈分别记录 |
| 校准和策略 | Cal-fit拟合概率；独立Cal-policy选完整规则；冻结Test确认。授权、业务状态和执行校验独立负责 |

同一候选在某一维度可取，不代表其他维度已通过。代码可用、来源核查、公开输出复算、新模型推理／训练、生产增量是不同证据。

## 条件性子问题与专题材料

| 文档 | 使用边界 |
|---|---|
| [动态技能加载计划（中文）](dynamic-skill-loading-experiment-plan.zh-CN.md)／[English](dynamic-skill-loading-experiment-plan.md) | 假设企业的条件性草案，尚非已注册实验。先诊断加载瓶颈；规模、样本量、阈值和收益界由业务与pilot确定 |
| [加载价值审查](dynamic-skill-loading-value-review.zh-CN.md)、[补充研究](dynamic-skill-loading-research-supplement.zh-CN.md) | 解释早期设想的限制、评估资料与数据来源，不再各自定义全分支当前方向 |
| [REFLEX与有界Agent控制](agent-control-reflex-trajectory.zh-CN.md)、[读出与自适应推理](decision-readout-and-reasoning.md) | 有日期的机制案例，非最新完整候选表或企业效果排名 |
| [技能加载合成示例说明](examples/skill-loading/README.md) | 字段与合同示例，非真实客户数据或模型成绩 |
| [MIRE案例（中文）](mire-case-study.zh-CN.md)／[English](mire-case-study.md) | 比赛任务、标签、复合奖项与代码证据；不直接迁移为当前企业效果 |
| [多模态适配基础稿（中文）](multimodal-decision-finetuning.zh-CN.md)／[English](multimodal-decision-finetuning.md) | 本分支保留10月18日基础稿；独立[PR #5](https://github.com/leoncuhk/awesome-decision-models/pull/5)的[固定784b6d6版本](https://github.com/leoncuhk/awesome-decision-models/blob/784b6d6f3e830c106dfbfc20b945524e271d8092/docs/multimodal-decision-finetuning.zh-CN.md)研究图像、历史证据、信息充分性和有成本修复。不同版本不混用，本次未合并该分支 |
| [多模态科研协议](multimodal-decision-research-protocol.md) | 选择性日志、修复动作与可识别性的拟议研究；没有执行结果或新颖性保证 |

## 生成索引、维护与历史

| 文档 | 维护方式 |
|---|---|
| [模型卡](models.md)、[证据台账](evidence.md)、[来源登记](sources.md) | 由`data/`与renderer生成；按条目看日期／深度，索引更新日期不等于全部来源重新审读。旧评测与新版本分列，未知权重不由代码SHA代填 |
| [维护说明](maintenance.md) | 来源检测与人工语义审查分开；实际仓库设置及运行状态另行核验 |
| [11月13日分支复核](branch-review-2026-11-13.md) | 历史审查，原字节保留；当前目录事实与判断见本导航和总览 |
| [10月22日报告完整转换](multimodal-decision-research-survey-2026-10-22.md) | 原始报告的历史转换，原字节保留；旧观点不能覆盖当前结论 |
| [图像归属与来源](assets/agent-control/README.md) | 资产出处记录，原字节保留；图片不是实验结果 |

本轮范围、纠错、执行检查与未执行边界见[审视记录](../updates/2026-11-19-docs-quality-review.md)。新证据先核版本、实际协议和反证，再更新其对应判断；论文与同作者代码不计作两次独立验证。
