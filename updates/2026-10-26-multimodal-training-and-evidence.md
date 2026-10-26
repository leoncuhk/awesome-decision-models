# 2026-10-26 · 企业图文意图微调：训练支持、证据监督与验收更新

[English guide](../docs/multimodal-decision-finetuning.md) · [中文指南](../docs/multimodal-decision-finetuning.zh-CN.md) · [选型](../docs/selection-guide.md#image-intent-adaptation) · [来源登记](../docs/sources.md) · [10 月 25 日核验](2026-10-25-weekly-review.md)

核验截止：2026-10-26 UTC。基线为 `3dad80a613c67c56a0a711e722d30adcefaec45d`。这是公开来源与代码路径审阅、实验合同维护；没有启动训练、模型推理、业务数据访问或部署修改。下文“可执行”指产物、输入、对照和停止条件明确，**不表示这些第三方训练命令已在本机跑通**。

## 本次新增、未变与修正

| 类别 | 相对现有记录的变化 | 不支持的推论 |
| --- | --- | --- |
| 新收录训练资产 | 补核 Qwen2／2.5／3-VL 官方图像 SFT／LoRA；另核 ms-swift 的 Qwen3.5 图文 LoRA loader／template／示例 | 两套 trainer 不可按名称互换；不形成优于 D3 的效果排名 |
| 深化既有 Intern 路径 | 从配置追到实际 dataset、视觉张量、loss 对齐、冻结视觉注入及保存核验；代码在 9 月 26 日已发布 | 10 月 18 日指南已有带图全语言训练判断；本次不是新 release，也不是从“只能推理”首次改判 |
| 新纳入 D3-Turbo | 10 月 19 日发布、20 日卡修订；共享状态后各题独立分支、Box／Track、API 别名 | 推理功能不证明可训练；作者榜单估计不能当官方榜单新成绩 |
| 补记实验边界 | Clef 社区训练实现有静态图像到 loss 链；mlx-decision 训练解析器拒收媒体 | “有源码”“图片进入设计链路”“真实权重跑过”“本地复现”“企业有效”是五层证据 |
| 新收录论文 | Rep2Act／VAD-R 为 9 月 26 日工作；VLTest 为 10 月 22 日工作 | 新收录不等于当天新发表；不引用其高分冒充客服准确率 |
| 未变 | MIRE／EcomMIR／前三方法、D3 经典版与 Vis 文本边界、10 月 25 日 Decider v1.2／RouteGuard 等结论 | 不重复包装成新发现，不重做既有竞赛、转换或模型验证 |

<a id="trainability"></a>
## 1. 哪些路线有真实图文监督路径

“源码链”仅指已读到图片处理、模型调用和监督损失之间的连接；未执行链路仍可能存在依赖、梯度、内存或导出错误。作者跑过也不等于完整数据可重放。

| 路线与一手入口 | 源码可读／图片到 loss | 作者运行证据 | 本仓库复现／企业效果 | 当前用途 |
| --- | --- | --- | --- | --- |
| [QwenVL 官方 trainer](https://github.com/QwenLM/Qwen3-VL/blob/96588727e44c78b25ba03ea03b8e12f7e64fd0da/qwen-vl-finetune/qwenvl/train/train_qwen.py)、[visual collator](https://github.com/QwenLM/Qwen3-VL/blob/96588727e44c78b25ba03ea03b8e12f7e64fd0da/qwen-vl-finetune/qwenvl/data/data_processor.py) | 是／静态可查；Qwen2／2.5／3-VL 生成式 SFT，PEFT attention LoRA，保存 processor | 官方提供配方；本次未审计一个指定业务训练 run | 未复现／未建立 | B2 短标签 SFT 的可查起点；普通 collator 会截断，须审实际保留证据和监督 token |
| [ms-swift Qwen3.5 指南](https://github.com/modelscope/ms-swift/blob/942be5a6120d46443f1b1940f2902c3757e312a5/docs/source_en/BestPractices/Qwen3_8-Best-Practice.md)、[示例](https://github.com/modelscope/ms-swift/blob/942be5a6120d46443f1b1940f2902c3757e312a5/examples/models/qwen3_5/transformers.sh) | 是／图像 OCR＋messages＋生成式 LoRA；另核 [loader](https://github.com/modelscope/ms-swift/blob/942be5a6120d46443f1b1940f2902c3757e312a5/swift/model/models/qwen.py)与 [template](https://github.com/modelscope/ms-swift/blob/942be5a6120d46443f1b1940f2902c3757e312a5/swift/template/templates/qwen.py) | 作者指南含演示及运行描述；不是本次复现实验 | 未复现／未建立 | Qwen3.5 候选路径；精确依赖、dense／MoE、模板和训练模块需固定 |
| [Intern 配置](https://github.com/InternLM/Intern-Decision/blob/565350244af860e1c276768cd80bdd9b8be93913/configs/training/qwen35.py)、[数据](https://github.com/InternLM/Intern-Decision/blob/565350244af860e1c276768cd80bdd9b8be93913/docs/DATA.md) | 是／实际图文 masked answer-token CE；语言全参，视觉／projector 冻结 | [论文 v1](https://arxiv.org/html/2610.22131v1)报告带图训练；原始数据／图片／制作流程未释放 | 未复现／未建立企业持出效果 | 可研究 full-language 适配；不是现成 LoRA，也不能用文本七套分数证明图文业务收益 |
| D3 经典版／[Turbo wrapper](https://huggingface.co/vllm-sr/d3-turbo/blob/a0f3e9e59ebd1202fe1d4de1c4c0f9a986758cbb/modeling_d3.py) | 推理代码可读／官方封装 `train(True)` 抛错；没有已核图像训练配方 | 已发布模型与作者推理报告；原始图像训练组成／完整配方未核实 | 未复现／未建立 | 冻结推理对照；独立 trainer 在架构上可能实现，但不能视作已支持 |
| [Vis D3 文本 trainer](https://github.com/Blockether/vis-decisions/blob/d73768e3c18d89d11f6b9a774b87d64ccd55f27d/src/blockether/vis_decisions/_d3_trainer.py) | 文本 full／LoRA＋255-code head；去掉视觉，不是图片到 loss | 沿用既有源码核验，无新增运行 | 未复现／未建立 | 文本机制参照，不可直接当多模态 C 臂 |
| [Decider v1.2](https://huggingface.co/perplexity-ai/pplx-decider-v1.2/blob/cce0f3f80033e9d89d80831d5281fd72124aacce/README.md) | 发布了图文推理；未核实公开图像监督训练器／完整数据重放 | 沿用 10 月 25 日作者报告；数据与请求格式同时改变 | 未复现／未建立 | 图文推理对照；不由 System One 兼容接口推出 Trainer／PEFT 支持 |
| Clef 官方／[社区 trainer](https://github.com/MersivMedia/clef-finetune/blob/c83f7bc1acc23c81ad0de838510c59c48bf60c79/src/clef_finetune/train.py) | 社区静态连接 image encoding／collation 到 LoRA＋FP32 head 的 CE＋Brier；非官方完整 RLCD | [KNOWN_ISSUES](https://github.com/MersivMedia/clef-finetune/blob/c83f7bc1acc23c81ad0de838510c59c48bf60c79/docs/KNOWN_ISSUES.md)明确没有真实 Clef GPU run，也无图片训练测试，仅随机小模型 CPU 检查 | 未复现／未建立 | 实验实现；先通过真实图像／权重／重载梯度关，不能称成熟配方 |
| [mlx-decision parser](https://github.com/armbues/mlx-decision/blob/d3e239a8c8c2afb362725f94c5076b90221168a5/src/mlx_decision/data/format.py)、[training scope](https://github.com/armbues/mlx-decision/blob/d3e239a8c8c2afb362725f94c5076b90221168a5/docs/TRAINING.md) | 训练拒绝 images／videos 与 state 内图片；部分模型仅训 head／readout | 文档排除 D3／pplx／Clef 骨干 LoRA／full tuning | 未复现／未建立 | 不可用它的看图推理支持证明 Mac 图像微调；不外推至所有 MLX 框架 |

对当前研究的取舍：先选一条明确的图像监督生成式 VLM 路径做最小学习检查，再比较同骨干读出；Intern 全语言训练单独计预算；D3／Turbo、Decider、Clef 保留严肃推理对照。**这是按可检查性安排实验次序，不是声称 Qwen 的业务质量更好。**

### Intern：本次到底补核了什么

[原始 release commit](https://github.com/InternLM/Intern-Decision/commit/63292c8b5e0f5d410a7159e0f1c14475b828839a)时间为 2026-09-26 08:03:14 UTC；本次 pin 到 10 月 22 日文档提交 `565350244af860e1c276768cd80bdd9b8be93913`，关键训练文件 blob 未变。`MEDIA_ROOT` 非空启用视觉 tokenizer，模型／tokenizer／processor 均由同一 `MODEL_PATH` 读取。虽然配置写 `class_name='VLMJsonlDataset'`，实际 [build](https://github.com/InternLM/Intern-Decision/blob/565350244af860e1c276768cd80bdd9b8be93913/src/inputs/dataset.py)构造 `UniversalDataset(JsonlDataset)` 并调用 `tokenize_fn(row, media_root)`，不能仅凭类名字判支持。

[masked.py](https://github.com/InternLM/Intern-Decision/blob/565350244af860e1c276768cd80bdd9b8be93913/src/inputs/masked.py)生成 `pixel_values`／`image_grid_thw` 和多模态位置，将 hard target 只写 labels，再由 collator 移位到 `<decision>` 前一位置；[DecisionQwen](https://github.com/InternLM/Intern-Decision/blob/565350244af860e1c276768cd80bdd9b8be93913/src/model/qwen.py)计算冻结视觉特征并注入语言 embeddings，缺 grid 或错误的 text-only forward 会拒绝。训练是完整词表的 masked answer-token CE，区别于候选子集 CE／Brier。冻结视觉塔仍然使用图像监督训练语言模块。

[保存核验器](https://github.com/InternLM/Intern-Decision/blob/565350244af860e1c276768cd80bdd9b8be93913/scripts/verify_checkpoint.py)检查视觉张量不变、语言层确有更新及各 rank 初始加载审计；它不等于导出／服务 logits 全等或业务验收。论文已披露训练规模与组成，并声称核对三种模型的输入 hash／日志／cache；这些是作者披露，不能写成“训练组成完全未知”，也不能推成原始数据和审计日志已全部公开。这里不重录既有训练规模数字或七套成绩。

<a id="d3-turbo"></a>
### D3-Turbo：多题共用一次状态不等于题目互相注意

[固定 runtime](https://huggingface.co/vllm-sr/d3-turbo/blob/a0f3e9e59ebd1202fe1d4de1c4c0f9a986758cbb/d3_runtime.py)的 `prefix_bidir`／`StateOnce` 先编码公共状态；full-attention 缓存 K/V，DeltaNet 保留因果 recurrent／convolution state，各题分支只读公共状态与自身题块。它与经典 D3 逐题重读不同，也与 Decider v1.2 全请求题目互相注意不同。应分别测试新增／重排问题、无关题干、候选顺序、批处理和后端等价，不能只因都返回多题概率就合并机制。

Turbo 的[卡片](https://huggingface.co/vllm-sr/d3-turbo/blob/a0f3e9e59ebd1202fe1d4de1c4c0f9a986758cbb/README.md)说明：Box 在目标不存在时也总会返回一个框，需另问 presence；框坐标／框 confidence 不能作为意图证据充分性的证书。API 的 `vllm-sr/d3` 已是 Turbo 别名，历史 D3 比较须固定本地 release 或实际 served identity。卡中 Index 是作者估计而非官方成绩，未新增排行榜数值。其 [Oct19 外评元数据](https://huggingface.co/vllm-sr/d3-turbo/blob/a0f3e9e59ebd1202fe1d4de1c4c0f9a986758cbb/.eval_results/vllm-sr__d3-turbo.yaml)记载当时原生 vLLM nightly 不支持 `prefix_bidir`、改用 AutoModel；不能据此断言今天仍失败，也不能把 SR Engine 路径与原生 upstream vLLM 混用。`decision_config` 的验证长度、可选长上下文和底座配置上限另行记录；都不是领域长图质量结果。

<a id="annotation-contract"></a>
## 2. 让模型学会判断，而非背诵可变业务事实

以下为拟议标注合同，均用通用客服情境；不是读取或发布真实记录。以同一张支付状态页为例，“查支付是否到账”与“我要取消本次付款”有不同目标；仅识别页面类别学不到用户意图。即使页面可读，也可能缺用户目标；即使目标明确，也可能缺最新状态。

| 监督对象 | 独立标注内容 | 必留的反例／评价 |
| --- | --- | --- |
| 业务意图 | 当时可见目标、允许多意图／部分意图、已知类／未知类／OOS | 同图异诉求、同诉求异页面；不把当前操作员动作当金标 |
| 可见证据 | 支持判断的文字／区域、来源版本与时间；不可见的值保持未知 | 证据位置只是监督线索，不把教师生成理由当事实或隐藏思维真值 |
| 充分性及原因 | 可读性不足、目标未明确、事实缺失／过期、模态冲突、候选遗漏 | “可答”与“猜对”分开；不能用统一低置信度代替缺口诊断 |
| 下一步 | 在明确成本和可用动作内选择回答、检索、追问或转交；可接受追问目标 | 不承诺任意问题有收益；需真实反馈才能评价澄清效果／退出；路由标签不授予退款等权限 |
| 实际结果 | 意图与充分性联合正确、后续回答服从门控、澄清是否解决缺口 | 过度拒答、错误接受、门控拒答但仍编造答案、正确接受但答案错误分别计数 |

把价格、政策日期、资格、订单状态、类别说明放到带版本／生效时间的检索或工具结果；微调学习“用所给事实判断、发现缺口、遵守拒判”，而不是把这些值固化为训练记忆。对未来政策版本、全新事实值、旧截图配新工具状态设置持出测试；预先定义证据优先级及冲突时动作。缺外部事实用取证，缺用户目标用澄清，未知类别按开放集处理；这些不能用“再思考更久”互相替代。

同意图保持、只换事实值的样本可帮助测语义迁移；会改变答案的值替换必须重标，禁止盲目保留原标签。所有合成、翻译、crop、模板改写只从 Train 派生并继承原 group。对自然／合成不足分别报告，保持代表性数据与富集压力集的分母。先双人独立审核一部分，按类别／缺口分歧裁定；不要用学生与教师一致率自证效果。

<a id="acceptance-plan"></a>
## 3. 可执行的最小对照与停止合同

沿用[既有最小矩阵](../docs/multimodal-decision-finetuning.md#experiment-matrix)及[科研协议](../docs/multimodal-decision-research-protocol.md)，只补本次会改变选择的检查。执行者应先填写以下产物；此更新没有替执行者运行模型或获取数据。

| 步骤 | 必需产物／对照 | 继续或停止 |
| --- | --- | --- |
| 0. 复用已有证据 | 按输入／split／checkpoint／代码／预处理 hash 建 ledger，写清已完成检查的版本与结果 | 版本和问题均未变时引用现有结果；只对新实现、变更或未解问题补测，不重跑已完成验证凑“更新” |
| 1. 数据准入 | 可用文件及许可 manifest、意图／充分性／动作标签、分歧裁定、独立组数、缺图／坏图／排除计数 | 未合法取得完整数据、没有可信标签或意图不能由输入确定，停对应训练臂；不以增加样本掩盖不识别性 |
| 2. 固定划分 | Train／Dev／Cal-fit／Cal-policy／Test 的 group IDs、时间窗口及内容 hash；审计泄漏连通分量 | 同用户／会话、近重复图、同一模板实例及所有派生版本不跨划分；抽象 UI family 另作未知模板持出，防止把全库连成一组后随意拆开 |
| 3. 强基线 | 规则／TF-IDF 文本、OCR＋文本监督分类、冻结零／少样本 VLM、同 VLM＋时效检索；D3 classic／Turbo、Intern、Decider／Clef 按支持与预算纳入 | 同样证据、候选定义、目标标签接触与总预算；监督／零样本分轨，不把更多标签或检索收益归给 head |
| 4. 图像与梯度关 | 实际 resize 后可读性、pixels／grid／位置／mask、真实梯度模块；极小 Train 子集拟合、图像必需样本去图／换图、adapter 保存重载／合并 | 图像没有影响时区分任务不需要图与链路损坏；tiny-fit 不能证明泛化。未通过不扩大训练，不把 text-only 结果称多模态 |
| 5. 受控微调 | 同精确 checkpoint 的短标签生成 SFT、候选 logits CE（可选 CE＋Brier）及独立 head；固定视觉处理／数据／参数预算，Dev 做有限搜索和 nested 学习曲线 | 已有 LM 答码读出不需要新 head；多 token 标签需固定评分／归一化。head 的架构、损失、模块、保存与推理路径需自己实现验证；不凭 API 宣称现成支持 |
| 6. 校准与策略冻结 | 最终选定 checkpoint 在 Cal-fit 拟合概率，在独立 Cal-policy 选风险／成本门槛，冻结温度、阈值、检索、澄清、fallback 全策略 | Dev 选模型／模板／rank／loss；两个 Cal 不再参与选模型；样本不足可用有适用依据的交叉拟合，否则只报探索性，不借用独立校准保证 |
| 7. 一次 Test 验收 | 同项配对且按用户／会话组估区间；意图 macro-F1、关键混淆、充分性误收／误拒、联合正确、risk–coverage／AURC、概率质量、成本与 p50／p95 | 只有相对最强冻结基线的覆盖增益达到预设实质标准，且关键风险／成本受控才继续；不满足则保留负结果或停。Test 失败不能直接变下一轮训练材料 |

时间持出不自动防止同用户／模板泄漏，按两个条件共同审计。中文业务迁移至少区分：自然中文持出（时间／新页面）、同义表达／否定／省略／多意图、图内中文小字与 OCR，以及跨语言同源样本。翻译对、同一图片或问题改写必须同组；中文合成压力测试不冒充真实中文分布。

固定未知类与候选覆盖任务：完整意图类持出、真实 OOS、自然检索 miss、人工移除正确候选分别命名。候选不存在是“选择空间不足”，图片不清是“证据不足”，不要一律标为同一 unknown。图文一致、图冲突、文冲突、双冲突、缺图／缺文都需独立裁定预期行为。采用 VLTest 启发的原始／仅改图／仅改文／联合四格时，共用同一原始或重建基准；改变事实的编辑重标。已通过的单模态控制可复用，新组合仍要核对答案保持性；富集失效发现率不是流量上的风险估计。

完整成本包括 OCR／检索、图像预处理／编码、多题状态复用、生成／重读、排队／网络、超时／非法输出／重试、澄清等待／退出、人工复核与纠错；记录硬件、精度、batch／concurrency、输入分布、cache、样本数及冷／热 p50／p95。人工有错误与延迟，不能默认为免费全对。另报误接受与误拒答成本矩阵；用真实同一预算比较路由总体，不能仅报被门控选中的容易子集。样本少导致风险区间过宽时，报告不能认证，而不是降低口径。

## 4. 两篇新收录论文怎样改变实验

| 一手论文及实际日期 | 可借用的具体区别 | 可获取性与限制 |
| --- | --- | --- |
| [Rep2Act／VAD-R v1](https://arxiv.org/html/2609.32653v1)，2026-09-26 | 显式可答判断与直接生成时自发拒答不同；证据缺口标注、text-only／image-only 捷径诊断、answer／abstain 动作与后续响应一致性 | 作者的 A-Acc 衡量回答／拒答动作是否匹配，不能当答案正确率；平衡划分、模型裁判及有限人工审计不证明企业效果。本文 CC BY 4.0；本次未核实可下载实现／数据及其复用许可，作为监督设计候选 |
| [VLTest v1](https://arxiv.org/html/2610.30794v1)，2026-10-22；[固定代码说明](https://github.com/beanduan22/VLTest/blob/b5861f2f990a63a1b8d0af37881471cf9034e66f/README.md) | 图文联合失效应有对应单模态控制与预期答案保持检查，输出变化本身不算失败 | 代码 MIT，外部图像／checkpoint 权利另核。README 要求 manifest、独立 pilot 阈值和人工审计，部分模型 adapters／budget 参数待补；论文自动 oracle 不能当已完整落地。seed-correct 选择不能直接估真实总体风险。未验证 TOSEM 页眉对应的正式发表状态 |

上述只是新增方法入口，无新数值写入 `data/evaluations.json`。MIRE 的图文意图数据／许可及竞赛三类方法继续引用[既有案例](../docs/mire-case-study.md#transfer-boundaries)和[10 月 22 日数据准入核验](../docs/multimodal-decision-research-protocol.md)，本次没有重获完整数据、伪造数据许可或重新确认其匿名下载资格。

## 5. 版本、许可证与待补项

| 资产 | 本次固定身份／许可 | 仍须核验 |
| --- | --- | --- |
| QwenVL 训练代码 | `96588727e44c78b25ba03ea03b8e12f7e64fd0da`，最新所阅 commit 为 2026-01-30，代码 Apache-2.0 | 不是 10 月新代码；所选权重／processor／环境和数据版本需独立固定。所阅 [Qwen3-VL-4B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct)卡声明 Apache-2.0，不代表所有 Qwen 型号同条款 |
| ms-swift | `942be5a6120d46443f1b1940f2902c3757e312a5`，2026-10-26，代码 Apache-2.0 | 当天 head 是 RLHF 性能改动，不是本次发现图像训练的发布日期；所阅 [Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B)卡声明 Apache-2.0。示例 OCR 数据许可独立检查，未下载／再分发 |
| Intern | `565350244af860e1c276768cd80bdd9b8be93913`；原始训练 release 9 月 26 日，保留既有 Apache-2.0 卡片记录 | 原始图像／训练／校准／制作流程未随接口文档公开；论文有组成披露但无企业持出证明 |
| D3-Turbo | `a0f3e9e59ebd1202fe1d4de1c4c0f9a986758cbb`，HF latest modified 2026-10-20；卡／LICENSE／manifest 声明 Apache-2.0 | manifest hash 是作者提供，未下载或逐字节核验权重；API 别名／请求 identity、独立校准与图像训练路径未建立 |
| Clef 社区 | `c83f7bc1acc23c81ad0de838510c59c48bf60c79`，10 月 2 日 v0.1.0，代码 Apache-2.0；Clef 权重沿用既有卡片条款 | 保持 FP32 head、按 encoder option IDs 对齐、LoRA 重载后模块审计；尚缺真实图像 GPU／多 GPU／merge 质量验证。监督 ordinal loss 不是 RLCD |
| mlx-decision | `d3e239a8c8c2afb362725f94c5076b90221168a5`，固定 parser 与训练文档 | 本次只收录负面训练边界，不改写其他 Core ML／MLX 部署记录或主张全部 Mac 路线不可训练 |

检索使用作者论文正文／版本历史、官方模型卡、HF 元数据和固定代码文件；搜索抓取日没有当作发表日。GitHub 首选连接器；普通终端 DNS 和部分网页 raw／API 读取失败后，只读下载公开源码／卡片到临时目录。未读全部外部 artifact、无全网穷尽保证，未运行 live watcher 或外部模型测试；失败访问不证明项目停止维护。保持现有 JSON → 双语生成方式、目录、历史 E01–E36、watcher 与 CI 配置。

English: This targeted review adds inspectable Qwen image-supervised training paths, deepens the existing Intern audit, distinguishes D3-Turbo state reuse from cross-question attention, and preserves Clef/MLX training limitations. New paper entries inform supervision and robustness controls. No model was trained, no business data were accessed, and no new benchmark score or business benefit is claimed. Publication and actual repository-check results are reported with the PR.
