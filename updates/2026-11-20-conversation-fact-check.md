# 讨论事实核查：训练方法、榜单与意图路由

日期：2026-11-20。沿用`research/dynamic-skill-loading-2026-11`／Draft PR #6；未改PR #5或合并主线。

[逐项核查正文](https://github.com/leoncuhk/awesome-decision-models/blob/bfe34486a0537cca5eda963315ae612a6184ca8d/docs/decision-model-discussion-fact-check-2026-11-20.zh-CN.md)覆盖用户提交的11月19–20日整段讨论。按模型／平台、方法／旧数字、PRDO、StartLux、路由和业务推论分开记录；重复主张合并，实施边界明确标出，非逐字引文不冒充原话。

主要发现：

- StartLux在DI0.3.2历史榜首成立；最新可核DI0.4.1改变题目、权重与刻度后，27B Instant为raw29／并列第6组。public、Full和joint请求分数不能混排；取得商业许可也不等于完整训练器或企业后训练效果已具备。
- PRDO主要证据是MMLU-Pro的Brier／AURC，数学验证有accuracy退化；不是StartLux的同算法封装，也不是普通事后校准。论文每run用两张Ada中的一张，另有125GB主机内存。
- CAPS Banking77所引结果为10-way，不是77-way；单gold类别对错的模拟日志不能直接等同退款满意／再进线的多动作业务反馈。
- CLINC层级.673为域与细分同时正确；公开输出复算确认Jev域422、gold域细分567、联合404／600。“description-only＋6.8pp”属于this-that，原回复遗漏归属；成本为58%意味着节省42%，原回复成本比例本身正确。
- Laya新Banking77聚合表属于冻结4B reader＋拟合head，不是经典322M／421M encoder后训练；原始split／阈值隔离尚未完整认证。LLM-as-Jev当前v3、JevBench与General列的区别已补。
- 本仓此前Chinese-Jev行业权重全planned的说法漏核CJ-Medical（10月18日已发布），现修正。Intern的Apache许可证早在9月29日存在；Chinese-Jev医疗“高4.0%”为相对增幅，不能改成4个百分点。
- 阿里原生API明确16题及Bearer，而微调指南推理示例用裸key；两份官方说明一并保留，未用客户凭据实测，不再把单个示例提升为所有推理鉴权通则。

当前判断仍按部署合同与学习信号维护在[企业总览](../docs/decision-model-posttraining-enterprise.zh-CN.md)。有可信标签可先作监督基线；CAPS与PRDO分别需要反馈语义和保留推理合同，不串成已证最优升级链，不以新榜单再换一个默认第一名。

规范数据新增10条针对性来源，更新StartLux／Laya的版本边界及Intern许可来源；原有42条评测记录原字节不变，没有新增本仓模型复现声明。来源登记更新批次不表示342份来源同日全部重读。

执行检查：生成5份页面；完整validator、生成同步与diff检查通过。依据数据／文档变更边界未重复跑单元测试；未下载权重、跑模型、训练、读取企业数据或验证生产效果。公开预测与榜单重算、科学性审查、原话忠实度审查和软件结构检查分别成立。
