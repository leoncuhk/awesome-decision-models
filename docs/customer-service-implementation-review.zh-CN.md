# 客服语义分流：Parlant、Modem、Entagl 的源码与保留审查

审阅：2026-11-19。[当前业务问题](domain-path-applicability-research.zh-CN.md) · [应用证据](decision-model-application-evidence.zh-CN.md) · [业务入口](dynamic-skill-loading-business-playbook.zh-CN.md)

## 保留结论与位置

三项都可以保留，但只有Parlant有本轮可核查的核心分流源码，不能按三个同等成熟的开源项目收录。

| 对象 | 保留什么／放在哪里 | 当前判断 |
|---|---|---|
| Parlant | canonical routing条目、本文的固定版本研读链接；上游独立checkout放工作区`refs/repos/parlant` | 优先保留源码参考；不vendor整仓、不据此批准迁移框架 |
| Modem Smart Triggers | routing类产品案例、官方公告与automation契约；不新建源码目录 | 保留“精确过滤→语义条件→触发”的设计；未定位实际Jev触发器服务端源码 |
| Entagl客服回放 | evaluation类报告与状态/回退反例；不新建源码目录 | 保留评估经验；未定位可复算该报告的公开harness、标注与逐条输出 |

本仓保存资料与审查结论，工作区统一管理第三方源码；本次只新增一份Parlant clone。商业API、MCP连接说明和客户端插件不能代替服务端实现。以上结论针对本次公开来源覆盖，不证明未公开代码不存在。

## Parlant：源码确实接入了判断链路

源码pin：`develop@07b2bcb4bebfeda7c53f1e2bbf2c68415f389e83`，提交于2026-11-18，Apache-2.0；这是阅读版本，不是权重或实际API响应版本。原11月17日研读的旧pin保留为历史，当前补充以此pin为准。

```text
Engine：preload / fill / 工具后update
  -> 发现会话候选 + 当前回合评估
  -> RuleRanker：共享state，每规则一个Proposition
  -> OpenRouterDecisionMaker：一批问题，一次HTTP请求
  -> exclusion / entailment / dependency / priority解析
  -> responder与工具执行；工具结果可引发重判
```

| 源码入口 | 值得保留的机制 |
|---|---|
| [Engine](https://github.com/emcie-co/parlant/blob/07b2bcb4bebfeda7c53f1e2bbf2c68415f389e83/src/parlant/core/engines/compass/engine.py#L300)、[Matcher](https://github.com/emcie-co/parlant/blob/07b2bcb4bebfeda7c53f1e2bbf2c68415f389e83/src/parlant/core/engines/compass/matcher.py#L205) | 会话候选、当前匹配和工具后更新分开；Jev不是直接交易执行器 |
| [RuleRanker](https://github.com/emcie-co/parlant/blob/07b2bcb4bebfeda7c53f1e2bbf2c68415f389e83/src/parlant/core/engines/compass/matching/rule_ranker.py#L189) | 共用对话、变量和工具事件；逐规则Proposition携带描述、术语及关系上下文 |
| [Jev适配器](https://github.com/emcie-co/parlant/blob/07b2bcb4bebfeda7c53f1e2bbf2c68415f389e83/src/parlant/adapters/nlp/openrouter_service.py#L1169) | 默认`~typesafe/jev-latest`，typed questions映射到noul/choice/score；记录实际返回模型名、usage和reported cost |
| [关系解析](https://github.com/emcie-co/parlant/blob/07b2bcb4bebfeda7c53f1e2bbf2c68415f389e83/src/parlant/core/engines/compass/relational_resolver.py#L452) | 新增exclusion与依赖/蕴含共同迭代，再处理优先；不收敛时保留无法确定应排除的规则并报告unresolved |
| [Python evaluator](https://github.com/emcie-co/parlant/blob/07b2bcb4bebfeda7c53f1e2bbf2c68415f389e83/src/parlant/core/engines/compass/matching/rule_function_evaluator.py#L40) | 允许精确业务条件用代码判定，与模型语义判断共存 |

**调用节省的边界**：一次HTTP覆盖当前batch，不表示完整客服回合只调用一次；匹配、工具和重新判断仍可产生多次工作。普通MIN规则多走recall；MIN/LOW/MEDIUM进入ranker时可用decision，HIGH/MAX使用需要解释的generator。因此不能宣传“所有规则和所有回合都由Jev一次完成”。

**与当前业务问题的差距**：首轮使用`>=0.5`并要求不确定时偏yes，服务于高召回相关性过滤；[原生RuleEvaluation](https://github.com/emcie-co/parlant/blob/07b2bcb4bebfeda7c53f1e2bbf2c68415f389e83/src/parlant/core/engines/rule_evaluation.py#L24)主要是bool与score，不是条件满足/反证/未知/事实冲突四状态。依赖ledger表示规则曾匹配，不是业务动作成功回执；显式排斥也不等于自动发现来源矛盾。

## 接入前需要补强的代码边界

这是针对研读pin的接入风险，不宣称真实Jev接口已返回非法值，也未修改上游。

1. **故障回退须另有合同**：未配置decision maker时会走generator；已进入decision路径后请求失败，并无同处自动切换generator的保证，外层engine会记录失败。不能把“可配置替代模型”解释成“异常时透明降级”。
2. **局部响应校验不足**：[_decode_answer](https://github.com/emcie-co/parlant/blob/07b2bcb4bebfeda7c53f1e2bbf2c68415f389e83/src/parlant/adapters/nlp/openrouter_service.py#L1344)拒绝缺题与未知类型，但未完整检查数值有限性、0–1范围、概率和、候选成员或题答primitive一致；ranker随后只补查PropositionAnswer类型。生产复用需严格校验，不能把返回float直接当可靠决策依据。
3. **关系解析仍有生成模型遵循边界**：priority loser的内容可仍在上下文中，responder添加撤销提示；这不替代实际业务API的权限和状态检查。源码prompt中的“human makes final call”也不是人工审核已发生的证据。

## Modem：保留有限输入下的触发模式

[2026-10-23公告](https://modem.ai/blog/smart-triggers)明确称使用Jev，在工单等事件触发完整Agent前判断自然语言条件。值得借鉴的是来源/作者/状态精确过滤后再判断语义，控制昂贵流程启动。

但[11月19日automation文档](https://modem.ai/docs/features/automations#trigger-conditions)进一步限定：条件只依赖事件详情时才由fast evaluation model前置筛选；依赖历史、跨期计数或事件外资料时，每个匹配事件仍启动Agent，再由Agent检查。该文未固定fast model的名称和版本，不能据旧公告推断当前所有判断都由某一Jev构建完成，也不能声称任意历史相关条件都能避免Agent运行。

本轮检查官方公告、docs、MCP工具说明及站点出链，并以域名作GitHub仓库/代码定向检索，未定位实际服务端判定和阈值实现。接口schema可以帮助理解输入限制，但不能证明模型调用、校准、重试或漏报处理正确。保留为产品/架构案例，不建立伪源码项目。

## Entagl：保留回放和失败归因经验

[原始报告](https://www.entagl.com/blog/typesafe-jev-benchmark-ai-decision-models)描述构造测试与真实客服历史路由回放。消息处置、专员选择及回退的结果不同；缺少当前会话owner、已收集信息和规则冲突会影响判断。其最有用的经验是固定完整状态、人工裁定分歧，并把消息处置与专员路由分开。

本轮读取报告和[公开业务API文档](https://www.entagl.com/api/docs)，检查站点出链及GitHub定向结果，未定位该评测的公开执行代码、完整测试标签或逐条输出。公开业务API不是Jev评测harness。报告来源仍是实施者自报离线回放，不能当成生产随机收益、中文领域结果或可复算benchmark。

## 实际检查与未执行项

- 已核对Parlant固定HEAD、许可证、调用链、适配器、关系解析与已有测试源码，上游工作区保持干净。
- 已执行12项**隔离协议观察**：仅AST抽取同pin的dataclass及encode/decode函数，不导入上游包。三种编码、合法noul、缺题/未知类型按上述边界返回或报错；局部解码接受了`1.4`、`NaN`、题答类型不符、候选外choice和概率和`1.6`，缺失noul字段产生`KeyError`。输入和结果见[协议观察收据](examples/service-routing-review/parlant-protocol-observations.json)。这是接口边界观察，不是模型效果复现或完整引擎测试。
- 仅阅读了[ranker测试](https://github.com/emcie-co/parlant/blob/07b2bcb4bebfeda7c53f1e2bbf2c68415f389e83/tests/core/stable/engines/compass/matching/test_rule_ranker.py#L896)、[adapter测试](https://github.com/emcie-co/parlant/blob/07b2bcb4bebfeda7c53f1e2bbf2c68415f389e83/tests/adapters/nlp/test_openrouter_service.py#L1235)和关系解析测试；没有运行pytest/live tests、安装依赖、调用模型、连接MCP账户或客户系统。
- 没有宣称三者覆盖完整“路径选择＋补问＋转人工＋降低总成本”的生产成功链路。Parlant优先用于研究接口与关系机制；Modem只借鉴事件内可判条件的触发；Entagl用于状态、基线和回退的评估教训。

## English orientation

Retain Parlant as a pinned source-code reference, Modem as a bounded event-gating product case, and Entagl as an implementer-reported replay study. Only Parlant's core decision path was available for code review. Its first-pass relevance verdict is not execution eligibility; declared relationships do not resolve arbitrary factual conflicts. The isolated adapter observations are not model/API or engine reproduction. Upstream source stays in the workspace's single-clone area; this repository stores review notes, provenance and links.
