# 企业决策模型后训练研究与引用核查

2026-11-19。当前目标是为未来企业客服判断与路由适配提供可审查、可实施的研究依据；本轮没有目标企业项目或数据，训练将由实际使用者另机执行。

## 入口与归属

- [企业后训练总览](../docs/decision-model-posttraining-enterprise.zh-CN.md)：现有分支分工、四项业务判断、可训练模型家族、数据、对照、校准与生产验收。
- [方法与横向比较核查](../docs/decision-model-posttraining-method-audit.zh-CN.md)：RLCD／PRDO、CE／Brier、蒸馏、部分反馈及原引用的数值口径。
- [平台与生产证据核查](../docs/decision-model-posttraining-platform-audit.zh-CN.md)：TypeSafe、阿里、Clef、Tev与具名应用的权限、训练、成本及证据边界。
- [Mac条件路线](../docs/decision-model-posttraining-mac-recipe.zh-CN.md)：固定Laya代码／权重版本、MPS配方、数据格式和独立校准；不是已测胜出模型。

研究正本统一在本仓docs；工作区原来的后训练选型页仅保留引用入口。PR #5继续多模态证据与修复研究，PR #6维护领域路径判断及本轮后训练研究，不合并两条研究问题。

## 影响选型的更正

OpenJev-RLCD需同时保留旧v1和最新PRDO v2；测试oracle覆盖率不能当部署保证。Inner Jev的冻结对象、Capability与准确率、训练步数和温度策略需恢复原实验范围。CAPS的金标模拟反馈不是企业结果日志。托管服务、可下载权重和完整本地训练实现分别核查；阿里的部署价格不是训练总价，普通单token SFT也不等于Jev运行时。

## 检查与未执行项

已执行`python3 scripts/validate.py --links-only`及`git diff --check`；本地Markdown链接通过。Mac配方JSON／Python及shell内Python语法、TrainConfig参数与相邻研究入口已检查；官方训练CLI的help与参数解析也已通过。平台核查的27个引用完成HTTP可达检查，返回状态不代替正文与服务准入核查。

未下载权重、安装训练依赖、运行推理／后训练、访问目标Mac、读取企业数据或进行生产实验。所有外部指标仍按作者报告或平台声明解释，没有新增`reproduced_here`记录；检查通过不证明模型效果、事实完整性或生产收益。
