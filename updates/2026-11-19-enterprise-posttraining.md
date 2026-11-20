# 企业决策模型后训练研究与引用核查

2026-11-19。当前目标是为未来企业客服判断与路由适配提供可审查、可实施的研究依据；本轮没有目标企业项目或数据，训练将由实际使用者另机执行。

## 入口与归属

- [企业后训练总览](../docs/decision-model-posttraining-enterprise.zh-CN.md)：现有分支分工、四项业务判断、可训练模型家族、数据、对照、校准与生产验收。
- [方法与横向比较核查](https://github.com/leoncuhk/awesome-decision-models/blob/bfe34486a0537cca5eda963315ae612a6184ca8d/docs/decision-model-posttraining-method-audit.zh-CN.md)：RLCD／PRDO、CE／Brier、蒸馏、部分反馈及原引用的数值口径。
- [平台与生产证据核查](https://github.com/leoncuhk/awesome-decision-models/blob/bfe34486a0537cca5eda963315ae612a6184ca8d/docs/decision-model-posttraining-platform-audit.zh-CN.md)：TypeSafe、阿里、Clef、Tev与具名应用的权限、训练、成本及证据边界。
- [Mac条件路线](https://github.com/leoncuhk/awesome-decision-models/blob/bfe34486a0537cca5eda963315ae612a6184ca8d/docs/decision-model-posttraining-mac-recipe.zh-CN.md)：固定Laya代码／权重版本、MPS配方、数据格式和独立校准；不是已测胜出模型。

研究正本统一在本仓docs；工作区原来的后训练选型页仅保留引用入口。PR #5继续多模态证据与修复研究，PR #6维护领域路径判断及本轮后训练研究，不合并两条研究问题。

## 影响选型的更正

OpenJev-RLCD需同时保留旧v1和最新PRDO v2；测试oracle覆盖率不能当部署保证。Inner Jev的冻结对象、Capability与准确率、训练步数和温度策略需恢复原实验范围。CAPS的金标模拟反馈不是企业结果日志。托管服务、可下载权重和完整本地训练实现分别核查；阿里的部署价格不是训练总价，普通单token SFT也不等于Jev运行时。

## 检查与未执行项

已执行`python3 scripts/validate.py --links-only`及`git diff --check`；本地Markdown链接通过。Mac配方JSON／Python及shell内Python语法、TrainConfig参数与相邻研究入口已检查；官方训练CLI的help与参数解析也已通过。平台核查的27个引用完成HTTP可达检查，返回状态不代替正文与服务准入核查。

未下载权重、安装训练依赖、运行推理／后训练、访问目标Mac、读取企业数据或进行生产实验。所有外部指标仍按作者报告或平台声明解释，没有新增`reproduced_here`记录；检查通过不证明模型效果、事实完整性或生产收益。

## 后续：选型证据交叉核查

用户指出此前Laya优先建议与低准确率证据不一致后，补查不同实验来源，并实际复算公开产物：

- JEVal论文明确将Laya预算提高至8192，不能用默认512解释低分。其实际HF权重revision和逐题输出仍未定位到，26.30%不能声称已独立重算；固定公开输入Parquet的11257行和10938个分类判断已读取、校验SHA-256并由两个执行者分别复算。
- 中文基准固定提交`aaf56ff1`的10份公开预测JSONL按相同467个判断键／378个原始case对齐后，复算Jev416题正确、multilingual Laya370题、English Laya324题；34题客服路由分别30、21、18。脚本经独立执行再次得到相同计数、配对与文件指纹，没有运行新模型或重新裁定标签。
- Laya公开Gate D三seed结果由原分析器及独立算式复核：soft-CE相对RLCD为−1.45、+1.35、+0.15个百分点，没有稳定方向。早期单seed优势不能决定默认方法；另有开放PR提出纠正训练文档。
- 独立适配研究既有正结果，也有标签先验、标点捷径、漂移及未达非劣标准的反例，不能只取高分作为企业底座优先依据。

据此撤回Laya的质量优先级，Mac页保留为训练实现样例；监督CE仍是基线，不是已经选出的最优方法。新的比较表、检查点未知项、负对照与适用范围并入总览和方法核查。尚无相同中文企业数据、相同可见证据与训练预算下的底座／方法胜者；质量门槛先于资源优化。

## 后续：PRDO v2全文与路线复核

重新读取v2正文1–7、附录A–G、图注和补充表1–6，并交叉核对作者训练器、估计器、指标、实验计划入口及offload实现，完整判断并入方法核查§8。PRDO的稳定正证据在知识选择题；数学验证存在准确率退化，因此将其限定为“只有中间计算才考虑”过窄。主研究合同改为两类：零生成的快速判断适配／蒸馏，以及保留推理后按分布接受／转交的PRDO；最小事实改动的数据方法跨路线使用。

该论文不比较SII、Kev、Intern与Nimble，不能用它确认底座排序；对student推理混合目标的批评，也不直接推翻SII固定教师均值蒸馏。主PRDO没有推理score-function奖励，但共享权重仍更新；第二阶段与KL效果依任务，保留预算匹配及负结果。原48GB独显加125GB主机内存不能当M5 48GB统一内存的训练证明。指定tag和部分归档仍未取得，没有宣称重训／独立复现论文或验证企业收益。
