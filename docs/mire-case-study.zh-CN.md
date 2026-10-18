# MIRE／WWW2025：多模态意图竞赛案例

[English](mire-case-study.md) · [实验指南](multimodal-decision-finetuning.zh-CN.md#quick-route) · [证据 E33](evidence.md#e33)

核验日期：2026-10-18。本页汇总公开任务定义、固定代码、组织方结果和方法论文，属于来源审阅，不是模型复现或生产验收。两个任务**并列出题、分别预测**；场景分类不是意图识别的强制前置步骤。最终奖项与线上成绩也对应不同评估。

<a id="tasks"></a>
## 1. 问题与任务契约

比赛研究在图文证据分散、标注与计算资源受限时，怎样识别电商客服图片场景与当前用户意图。评测对象是类别标签，不是回复质量、执行交易的权限或最终处理成效。依据：[官方赛题](https://tianchi.aliyun.com/competition/entrance/532277/information)、[组织方论文](https://doi.org/10.1145/3701716.3719642)第2节及[固定 README](https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/README_zh.md)。

| | A：图片场景分类 | B：多轮对话意图分类 |
| --- | --- | --- |
| 核心问题 | 图片属于哪种电商场景？ | 用户此刻想咨询或反馈什么？ |
| 输入 | 图片＋任务指令／标签定义 | 历史对话、当前表达、有关历史图片＋任务／标签定义 |
| 输出 | 一个场景标签字符串，23 个有效类 | 一个意图标签字符串，23 类 |
| 图片作用 | 主要识别对象 | 帮助理解对话的证据 |
| 边界 | 页面／物体类别不等于用户目标 | 同一页面可对应不同诉求，上下文可能不可缺少 |

这不是要求每条记录同时输出两个标签；公开基线是生成标签的 SFT，不是已核实的 D3／Intern 候选 logits 实现。

<a id="labels"></a>
## 2. 完整有效标签

保留官方中文标签原串，因为字符串身份影响评分。下列分组是**编辑阅读辅助，不是官方上层训练标签**；具体边界以[官方定义](https://tianchi.aliyun.com/competition/entrance/532277/information)为准。README 场景表共25行，其中 `消费者与客服聊天页面`、`个人信息页面` 两项删除线；下面完整保留23个有效类，包含 `评论区截图页面`。

| 场景分组 | 有效标签 |
| --- | --- |
| Product presentation / 商品展示 | `商品分类选项`、`商品头图`、`商品详情页截图` |
| Order and payment / 下单支付 | `下单过程中出现异常（显示购买失败浮窗）`、`订单详情页面`、`支付页面`、`购物车页面` |
| Logistics / 物流 | `物流页面-物流列表页面`、`物流页面-物流跟踪页面`、`物流页面-物流异常页面` |
| After-sales and disputes / 售后争议 | `退款页面`、`退货页面`、`换货页面`、`投诉举报页面`、`平台介入页面` |
| Store, promotion, reviews, account / 店铺活动评价账户 | `店铺页面`、`活动页面`、`优惠券领取页面`、`评论区截图页面`、`账单/账户页面` |
| Other images / 其他图像 | `实物拍摄(含售后)`、`外部APP截图`、`其他类别图片` |

| 意图分组 | 标签 |
| --- | --- |
| Attributes and variants / 属性区别 | `商品材质`、`商品规格`、`包装区别`、`版本款型区别`、`适用季节`、`上市时间` |
| Function and usage / 功能使用 | `是否好用`、`功效功能`、`排水方式`、`能否调光`、`控制方式`、`用法用量`、`养护方法` |
| Quality and feedback / 品质反馈 | `是否会生锈`、`是否易褪色`、`反馈密封性不好`、`反馈用后症状`、`信号情况`、`气泡` |
| Recommendation and supply / 推荐供给 | `单品推荐`、`套装推荐`、`发货数量`、`何时上货` |

`其他类别图片` 不自动等于通用未知意图或澄清保证。`控制方式` 与 `能否调光`、`包装区别` 与 `商品规格`，须按正式定义结合当前上下文区分；此标签集也不覆盖所有客服需求。

<a id="competition-design"></a>
## 3. 数据、赛程与资源边界

| 阶段 | 官方描述的供给／评价 |
| --- | --- |
| 训练 | 合计1000条已标注图文／对话样本；不能推断两任务各1000或具体分配 |
| 初赛 | 10000条不公开标签的测试样本，平台自动评分 |
| 复赛／后一个算法测试轮 | 另增10000条新无标签样本；线上榜最佳提交日期为2025年1月18—19日 |
| 最终综合评审 | 方案、代码／模型／数据／技术材料、复现／合规核验及答辩；2025年1月22—27日专家评估与线上成绩共同决定最终名次 |

[官方规则](https://tianchi.aliyun.com/competition/entrance/532277)要求模型可私有部署并提交推理代码、模型小于10B、每例最多3次模型调用且总输出在100 token以内；比赛还限制私有领域训练数据和商业 LLM API 调用。README／论文的边界措辞并非完全一致（≤与<，论文对 API 情形另作表述），应保留具体来源，不能当成完全相同的已测试条件。基线 `max_new_tokens=128` 是示例推理设置，不证明满足比赛限制。数据访问及比赛外使用权须另核。

组织方论文描述脱敏与专家标签审核；本仓库未独立审计这些过程，也未取得完整数据／图片。分辨率、逐类支持、任务占比、图像—轮次精确对齐、独立分组数量及重叠仍未知。

<a id="data-and-code"></a>
## 4. 数据→全参SFT→生成→提交→评分

| 环节 | 固定代码及含义 |
| --- | --- |
| 数据字段 | [data_info.json](https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/mire_baseline/configs/data_info.json)：`instruction`→prompt、`input`→query、`image`→images、`output`→response；`id` 是样本身份元数据，`image` 是一张或多张图片的路径列表。`input` 为空不等于没有文本，demo 对话／候选已经放入 `instruction`。`output` 仅作监督／真值，不能成为推理证据。 |
| 训练 | [qwen2_vl_full_sft.yaml](https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/mire_baseline/configs/qwen2_vl_full_sft.yaml)：Qwen2-VL-7B-Instruct、`finetuning_type: full`、LLaMA-Factory、3轮、LR 5e-6、验证比例0.1、训练截断1024。`max_samples: 10000` 是读取上限，不是人工标注规模；实际 train.json、任务混合／分组切分及训练权重未审计。 |
| 推理 | [predict.yaml](https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/mire_baseline/configs/predict.yaml)：生成标签字符串；模型与示例数据路径须对应实际运行。推理截断2048与生成上限128，分别区别于训练／比赛限制。 |
| 提交 | [convert2submit.py](https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/mire_baseline/convert2submit.py)：读取 JSONL `predict`、按行序回填并导出 CSV。要保留身份／顺序并检查条数，脚本并非按ID安全联结；官方 CSV 至少含 `id`、`predict`。 |
| 本地指标 | [cal_acc.py](https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/mire_baseline/cal_acc.py)：逐例比较 `output`／`predict` 字符串，调用 sklearn weighted F1／P／R及accuracy。注释写多标签，不代表实际单字符串记录是集合式多意图评测。 |

[官方评分](https://tianchi.aliyun.com/competition/entrance/532277/information)是**全部分类标签的加权 F1**，不是 macro-F1，也不是两个任务分数的等权均值；本页直接保留官方 `score`，不从四舍五入值反推类别数量／权重。加权总分可能掩盖稀有类错误。README 的基线 F1 与accuracy是不同量，本页不据此制造同条件提升幅度。

<a id="public-examples"></a>
## 5. 公开样例与证据缺口

[demo_test.json](https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/data/demo_test.json)包含10条文本／标签记录及图片引用。第2条灯具历史涉及调光、手机连接，当前转向开关控制，标为 `控制方式`；第8条在讨论材质后问“这个是哪个地方”，标为 `商品材质`。这些是**真实公开文字样例的摘意**，不是新增模型预测，也不是成对反事实实验。原图片未读取，不能用编造画面冒充比赛截图。

“物流异常截图→对应场景标签”或简化的气泡JSON可说明格式，但未核原始公开图片时必须标为自制说明。关键文字缺失、裁剪不可读或当时上下文缺失可能使意图不可辨识；固定标签比赛分数没有独立验收新设计的澄清／unknown策略。

<a id="finalists"></a>
## 6. 最终奖项、线上名次与方法

### 官方最终奖项与复赛成绩分列

已读取渲染后的[最终结果](https://tianchi.aliyun.com/competition/entrance/532277/customize583)与[后轮算法榜](https://tianchi.aliyun.com/competition/entrance/532277/rankingList)。排行榜英文界面称该算法轮为“Final Round”，对应**复赛／后轮测试**，不是后续综合奖项评审。[官方赛程](https://tianchi.aliyun.com/competition/entrance/532277)明确最终名次由线上成绩与专家评估共同决定。

| 最终综合名次／奖项 | 官方队名 | 对应方法 | 复赛线上名次 | 官方 score | intent_score | image_scene_score |
| --- | --- | --- | --- | --- | --- | --- |
| 1／金奖 | Dynamic Challengers | IntentionGPT | 3 | 0.9051 | 0.9365 | 0.8339 |
| 2／银奖 | 拥抱LLM／EmbraceLLM | EcomMIR | 2 | 0.9070 | 0.9420 | 0.8278 |
| 3／铜奖 | scale | CuSMer | 1 | 0.9085 | 0.9265 | 0.8676 |

完整协议见 [E33](evidence.md#e33)。这些是组织方汇总结果，不是本仓库重跑；所核最终表未给出专家／综合数值总分。EcomMIR 两任务值的均值为0.8849，**不是**官方0.9070，不能用自造等任务权重替换全标签加权；也不能把2025年线上轮次与最终奖项拼进后来模型总榜。

### 三方法究竟做了什么

| 方法／归属 | 所核技术思路 | 阅读深度／限制 |
| --- | --- | --- |
| [IntentionGPT](https://doi.org/10.1145/3701716.3718370)，Dynamic Challengers | 自数据增强、协同去噪、结构感知领域检索及 model soups；组织方第3节提供队伍层面的技术概述。 | 已读出版方 [SIGWEB 摘要](https://www.sigweb.sigweb.hosting.acm.org/toc/www25b.html)，未取得全文、精确底座／训练／代码产物。摘要自述第一，与最终金奖表一致；不把同名聊天App当冠军代码。 |
| [EcomMIR](https://doi.org/10.1145/3701716.3718371)，拥抱LLM／EmbraceLLM | CN-CLIP 场景训练／Greedy Soup；MiniCPM-V 2.6 意图LoRA；清洗、分层标签及高置信伪标签扩训。 | 已读[作者全文](https://zhoushengisnoob.github.io/papers/WWWComp.pdf)。[E28](evidence.md#e28)保留作者Round2分任务结果，现在另由官方榜对应数值佐证；多干预组合不能归因于LoRA单项。 |
| [CuSMer](https://doi.org/10.1145/3701716.3718373)，scale | 伪标签→微调→合并、图像增强→微调→合并两链路；组织方第3节另将多样性／置信采样和 Breadcrumbs／TIES 合并归给scale。 | 已读出版方摘要／组织方概述及[作者身份页](https://binglin-wu.github.io/)，未核方法全文／代码。摘要的线上后轮第一与作者铜奖并不冲突，因为阶段／排名不同。 |

组织方Table1确认 Dynamic Challengers／EmbraceLLM／scale 的奖项；方法归属由对应作者报告和技术描述连接，CuSMer作者明确写出 scale@DLUT 与铜奖。精确“榜单提交→论文检查点”仍未固定。本轮尚未找到并核实三方法的官方实现仓库，不等于断言没有；MIRE官方基线仓库也不是三队实现的公开集合。

<a id="transfer-boundaries"></a>
## 7. 如何迁移到新的实验

可检验的假设是证据／标签定义、上下文检索、标签保持增强、监督适配及可审计合并。EcomMIR使用Round1无标签输入扩训，不能称仅原始1000人工标注的纯监督；该接触本身既不能证明Round2污染，也不能证明未触碰留出。组织方所述新增伪标签或去噪幅度，本页不当作已审计数据计数或因果效应。

比赛未证明校准、风险证书、稀有类覆盖、新UI／时间泛化、完整服务p95，或D3／Intern／自定义读出优越性。适配新领域前使用现有[分组划分](multimodal-decision-finetuning.zh-CN.md#split-protocol)、[最小矩阵](multimodal-decision-finetuning.zh-CN.md#experiment-matrix)、[训练前检查](multimodal-decision-finetuning.zh-CN.md#preflight)及[结果模板](multimodal-decision-finetuning.zh-CN.md#result-template)。逐因素实验、保留分组验收；预定风险／收益／成本条件不满足时停止扩展或保留较强基线。

<a id="sources-and-gaps"></a>
## 8. 来源与尚未核实项

上文附一手链接；MIRE不可变代码版本为 `d101287af90d114c5bf0cbfbd56fe9c52358e3bb`。[来源登记](sources.md)区分全文／摘要阅读并保存组织方PDF内容哈希。[E28](evidence.md#e28)保持原样，[E33](evidence.md#e33)新增官方阶段比较。已审阅官方规则／结果、组织方全文、基线代码与公开文字demo；完整数据／图像、提交权重／原始预测、三队精确代码、IntentionGPT／CuSMer全文及专家数值总分仍未核实。本轮未运行模型、训练、外部评测脚本或比赛数据下载流程。
