# 2026-11-17：领域对话的路径适用性与优先关系

[业务实验入口](https://github.com/leoncuhk/awesome-decision-models/blob/bfe34486a0537cca5eda963315ae612a6184ca8d/docs/dynamic-skill-loading-business-playbook.zh-CN.md) · [领域路径判断研究](https://github.com/leoncuhk/awesome-decision-models/blob/bfe34486a0537cca5eda963315ae612a6184ca8d/docs/domain-path-applicability-research.zh-CN.md)

本次将当前诉求、已确认状态与候选路径条件的探索整理进动态技能加载研究分支。保留原实验：先固定候选与执行器比较判断器，必要时再比较加载策略。

## 新增的有效区分

- Parlant固定源码快照已把Jev用于批量规则相关性过滤；它在不确定时偏向保留，不能直接当作业务执行资格门槛。
- ShARC/EMT/MUDERN为逐条件满足/反证/未知及澄清提供任务参考；条件反证与来源彼此冲突分开。
- 将诉求相关性、路径适用性、信息缺口、优先/依赖/互斥分开；四状态输出及验收方案是未实施的编者建议。
- 补入近期readout、状态更新、校准与澄清研究；不重复已有性能记录，不新增模型排名或生产收益结论。

## 证据和发布边界

来源为官方文档、原论文与部分作者源码。Parlant固定`develop`提交`687044f61ab5d8e70d3bbeddcd918ca190d35da9`；该代码提交不固定Jev实际服务版本。临床分诊与RegretBench只核摘要和元数据，不导入性能数字；其余核查范围见研究正文。

本次为文档变更，没有改canonical目录、性能账本、生成模板或实验代码。已通过`python3 scripts/validate.py --links-only`与`git diff --check`，并人工审阅内容；不新增只复述文档的测试。检查不证明外部URL可达、来源事实正确或模型效果。没有模型调用、训练、独立复现、客户数据或线上试验。

## English summary

Add a source-grounded research note on state-dependent domain-path applicability, missing facts and precedence, linked from the existing business playbook. Distinguish Parlant's Jev relevance filter from execution eligibility, and condition refutation from conflicting evidence. Preserve the fixed-loader comparison before testing loading policies. This is documentation and an unimplemented contract, not model or business validation.
