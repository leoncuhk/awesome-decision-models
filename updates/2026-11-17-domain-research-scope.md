# 2026-11-17：收敛领域路径问题与研究对应范围

[业务研究入口](../docs/dynamic-skill-loading-business-playbook.zh-CN.md) · [领域研究与来源](../docs/domain-path-applicability-research.zh-CN.md) · [当日首次整理](2026-11-17-domain-path-applicability.md)

## 当前问题

面对客户当前诉求、相关对话、已确认状态和候选路径条件，分别判断路径适用性、信息充分性、冲突与优先关系。Jev/Koa类判断器和动态技能加载均是待检验的实现选择；不能由模型类别反推业务问题，或用意图分类/最终任务成功替代全部中间判断。

## 实质修订

- 将Parlant、EMT/MUDERN列为最贴近的部分参考，明确规则相关性与执行资格、多条件问答与多路径调度的边界。
- SOPBench用于执行前条件、步骤与终态验收；Koa用于判定器实现，τ²/CARE用于下游结果和改进，辅助基准/复核器保持各自用途。
- KADS降为历史方法参考：未找到可确认的持续维护实现、直接后继生产采用或收益对照。DialFork相关工作引用及同公司Infinitus图模型不作为直接采用证据；负面检索不证明内部使用不存在。
- 纳入Koa、SOPBench、FlowBench、ToolSandbox、DialFork、Granite Guardian和CARE的有边界来源说明，集中在领域研究文档，避免把相邻研究堆成现成方案。
- 同步业务入口、研究补充、价值复核及双语加载方案的当前范围；原有合成样本、方案和历史证据保留。

## 核查与证据边界

沿用本次会话已查阅的原论文、作者代码与官方文档；新段落标明方法/源码核查和仅摘要来源的适用边界，不新增数值性能记录或`reproduced_here`。没有调用模型、训练、操作客户系统或验证业务提升。KADS的采用结论仅限公开检索覆盖，不用引用数量代替价值判断。

本次为文档变更，已通过`python3 scripts/validate.py --links-only`与`git diff --check`，并人工检查范围及中英文对应；这些检查不验证外部事实、模型效果或生产收益。生成模板、canonical目录、实验代码及账户/发布设置未变。

## English summary

Refocus the research on four state-dependent domain-path outputs: applicability, information sufficiency, conflicts and precedence. Keep decision-model substitution and dynamic loading as conditional interventions. Separate direct partial mechanisms from implementation choices, verification benchmarks and whole-agent outcomes. Downgrade KADS to historical methodology because explicit downstream adoption and production benefit were not confirmed. Preserve earlier research artifacts and mark the current scope at every active entry point.
