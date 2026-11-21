# 多模态判断后训练：企业图文意图

更新：2026-11-21。场景：企业已有**数千张截图＋人工意图标签**，可以补充判定时点之前的历史上下文；目标机为 M5 Pro 48GB。本页只写怎么做。“为什么这样做”见 [P11](../problems/P11-multimodal.md)；合同、通用数据规则和风险验收沿用[通用流程](decision-pipeline.md)，本页只写多模态特有的部分。

现状：方案可执行，但没有运行过；以下命令和资源估计都未在目标机上验证。

<a id="hypotheses"></a>
## 1. 预注册假设与主终点

| 假设 | 什么结果推翻它 | 推翻后怎么办 |
|---|---|---|
| H1 可见输入能确定目标，且图像提供增量信息 | 独立标注仍有不可消除的歧义；或上下文、OCR、冻结特征已解释全部有效信号 | 改目标或补证据，不声称学会了多模态意图 |
| H2 受限适配能改善业务决策 | 相对最强冻结基线，每案件配对净成本下降的置信下界未超过预注册的最小收益，或关键风险不达标 | 保留基线或停止。F1 提高不单独算成功 |
| H3 指定的读出或训练改动有独立价值 | 同底座、同标签、同视觉处理、同预算下增益消失，或冻结 head 已填平差距 | 报告系统改动有用，但不归因于表示突破 |

**主终点**：每个独立案件的预期总成本，包括错误、人审、延迟和算力，用配对净下降衡量。最小有意义收益 `delta_cost` 和关键风险上限，由负责人在看结果之前确定。macro-F1、风险—覆盖和概率质量都是辅助指标。

<a id="matrix"></a>
## 2. 实验矩阵：先便宜的臂，过门槛再扩展

所有臂使用同一冻结任务和同一划分。特征、示例、head 只用 Train 拟合，Dev 做有限选择，所有臂最后在同一个锁定 Test 上比较。补齐历史后的同一批样本上，必须做四组证据对照：image-only、context-only、OCR＋context、image＋context。历史视图未获准构建之前，只能报告 image-only，不能声称测过多模态增益。

| 臂 | 配置 | 检验什么 |
|---|---|---|
| B0-R / B0-T | 现有规则；有真实文本时用普通文本分类器 | 低成本底线，以及目标是否可分 |
| B0-O | 冻结 OCR＋同一个上下文分类器 | OCR 的信息增量，计入 OCR 错误与预处理成本 |
| F0 | 冻结图文编码器特征＋正则化线性 head | 不改 VLM 的低成本监督融合 |
| B1 | 主候选 Qwen3.5-4B，零样本＋Train-only 少样本短标签 | 未适配对照 |
| F1 | 冻结 B1 骨干，在核实的特征位置训练小 head | head 是否已经够用 |
| B2 | 同一量化 B1 底座，图像条件语言侧 QLoRA，completion-only 短标签 SFT，至少 3 个种子 | adapter 相对 B1/F1 的增量 |
| B3（过门槛后） | B2 同底座，候选子集 CE，再在同一实现中加 Brier 项 | 读出与目标的归因 |
| D0 / I0（过门槛后） | D3 或 Intern-Decision 推理；平台、图像训练、导出门槛都通过后才训练 | 严肃的系统级对照 |

种子 ID 在运行前记录，保留全部尝试，不在 Test 上挑最好的种子。强基线已达业务目标，是有效的停止结果。

<a id="training-support"></a>
## 3. 哪些路径真的训练了视觉

| 候选 | 已核实的起点 | 用图训练前必须过的门槛 |
|---|---|---|
| MLX-VLM（Mac 原生） | 固定 commit `2ceff4c1` 有本地图像、completion-only SFT 和量化底座的语言侧 adapter 路径：VisionDataset → pixels/grid → shifted completion loss → Qwen3.5 视觉融合 → 梯度引擎 | 源码支持不等于本机跑通。要核真实 pixels、mask、梯度、最长输入的内存和保存重载 |
| Intern-Decision | CUDA/XTuner 路径带图训练：冻结视觉塔与 projector，训练全部语言参数；监督只在答码位置 | 不是现成的 Mac LoRA。要保留其占位符和答码监督合同，移植与导出另行验证 |
| D3 经典版 / Turbo | 官方 wrapper 的 `train(True)` 抛出 inference-only 错误；第三方 Vis 只训练文本，去掉了视觉塔 | API 别名或推理能力不能证明可以训练图像 |
| Qwen2/2.5/3-VL、Qwen3.5 | QwenVL 官方和 ms-swift 的图像训练配方可以作参考 | CUDA/Transformers 上的支持不能直接迁移到 MLX |
| Clef / Decider | MLX-VLM Clef 支持图像和视频推理；调用需要 question/option spans 和 qtype | 普通 shifted-SFT CLI 不能证明 joint head 可训 |
| mlx-decision / mlx-lm | mlx-decision 拒收媒体输入；mlx-lm 只支持文本 | 不能由此推断 MLX-VLM 也不能训练图像 |

<a id="mac"></a>
## 4. M5 Pro 48GB 候选

主候选是 **Qwen3.5-4B 原生 VLM 的图像条件语言侧 QLoRA**。Qwen3.5-2B 作为资源回退；如果卡在 Qwen3.5 实现的兼容性上，再考虑 Qwen3-VL-2B 的独立路径。2B 冒烟成功不是试 4B 的前提，4B 也没有被证明更好或一定能训。

| 角色 | 原始 HF revision | MLX 4-bit revision |
|---|---|---|
| 主候选 Qwen3.5-4B | [851bf6e8](https://huggingface.co/Qwen/Qwen3.5-4B/tree/851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a) | [0e7ffd5c](https://huggingface.co/mlx-community/Qwen3.5-4B-4bit/tree/0e7ffd5c629ef7719d4cbc04069232580bfa9d9c) |
| 回退 Qwen3.5-2B | [15852e8c](https://huggingface.co/Qwen/Qwen3.5-2B/tree/15852e8c16360a2fea060d615a32b45270f8a8fc) | [674aaa72](https://huggingface.co/mlx-community/Qwen3.5-2B-4bit/tree/674aaa7240b91e8012fcad5d791b7dfe5ba90207) |
| 独立路径 Qwen3-VL-2B | [89644892](https://huggingface.co/Qwen/Qwen3-VL-2B-Instruct/tree/89644892e4d85e24eaac8bacfd4f463576704203) | [9c4f5209](https://huggingface.co/mlx-community/Qwen3-VL-2B-Instruct-4bit/tree/9c4f5209e57b31f4b9dfba735de3fb983739c9cc) |

实施要点：
- **许可**：官方 Qwen3.5-4B 声明 Apache-2.0。社区 4B 转换的固定目录里没有 README 和 LICENSE，G0 要追溯许可；无法确认就停用该产物，改为从官方权重受控转换。
- **训练模块**：Qwen3.5 训练时令 `use_kernel=False`，走 chunked/reference ops。语言层的 linear 模块包含 DeltaNet 的 `in_proj_qkv/z/b/a` 与 `out_proj`，不能照搬 Qwen3-VL 的 q/k/v/o 清单；保存并审计真实的可训练模块、参数数和梯度覆盖。
- **模板**：固定 thinking 开关、完整的 processor/chat template 和评分前缀。Qwen3.5 默认生成前缀带 thinking 标记，金标短标签、空 thinking 段与推理前缀必须一致，逐 token 核对。
- **资源**：4-bit、每例单图、microbatch 1 加梯度累积。先用代表性最长的输入实测反向和保存重载，再扩大规模。48GB 内存或量化文件的大小都不是容量保证。

<a id="data"></a>
## 5. 数据与标签

- **可读性审计**：用实际推理时缩放、裁剪、压缩后的图来审计，不看原图。标注者能否读出关键文字、区分 UI 状态？模糊、小字、缺区、脱敏造成的信息丢失，要与语义混淆分开记录。删除关键证据或颠倒 UI 关系的增强，不算保持标签的增强。
- **标签类型**：建模前定义 `task_mode`。单意图要约定主标签冲突规则；多意图用集合目标，不用互斥 softmax。`unknown`、`out_of_scope`、`insufficient`／`needs_clarification` 分开（见 [P06](../problems/P06-candidate-coverage.md)）。模型低置信拒判是策略输出，不等于这些金标。
- **独立审核**：两位标注者独立审核代表性样本，以及另行富集的歧义和稀有类样本；记录逐类一致性和裁决。同一图文仍有多个合理意图时，先补上下文或改合同，再训练。
- **变化事实**：价格、资格、订单状态、政策版本作为带时间戳的输入证据提供，不靠权重记忆。训练的目标是学会识别缺失、过时、冲突，而不是记住事实本身。
- **短标签分数**：中文类别名可能是多 token 且长度不同。优先用映射到版本化标签的固定短 ID，并在完整模板里核对 tokenization。不能只取第一个 token 的概率，也不能把模型自报的 confidence 当成类别分数。

记录示意（虚构字段，真实数据只放在获授权的本地系统）：

```json
{"record_id":"synthetic-001","image_ref":"LOCAL_ONLY","visible_text":"…","evidence_cutoff":"…",
 "conversation_group":"G_A","near_duplicate_group":"DUP_A","leakage_component":"C_A","ui_family":"UI_A",
 "label_schema_version":"labels-v1","task_mode":"single_intent","intents":["INTENT_A"],
 "evidence_status":"sufficient","annotation_status":"independently_reviewed_and_adjudicated",
 "rights_status":"LOCAL_REVIEW_REQUIRED","split":"unassigned"}
```

<a id="split"></a>
## 6. 防泄漏划分

1. **建泄漏连通组**：同会话、同用户、完全或近重复的截图（精确哈希、视觉/OCR 相似度、人工核对）之间连边，取连通分量。增强和改写继承父样本所在的组。巨型连通组是待处理的限制，不能为了比例好看硬拆。
2. **声明目标总体**：常规流量集保持自然比例；要声称对未来或新页面的泛化，另外冻结后续时间段和未见 UI 家族作为留出集，单独报告。
3. **锁定职责**：五个职责的示例比例如下（虚构的 3,000 条预算，不是强制比例）。

| 职责 | 示例 | 唯一用途 |
|---|---|---|
| Train | 1,500 | 拟合特征、head、adapter |
| Dev | 300 | 有限的模型、模板、超参选择 |
| Cal-fit | 300 | 拟合冻结产物的概率映射 |
| Cal-policy | 300 | 在预注册的策略族中选择 |
| Locked Test | 600 | 只确认一次 |

4. **CV 只在开发范围内用**：做分组折；目标是未来流量时用前向时间折。外层 Test 和最终 Cal 保持不动。
5. **变更要版本化**：Dev 的难例移入 Train 后，原开发成绩作废。Test 错误一旦被用来调整，旧 Test 就成为开发历史，需要新的验收集。

训练前列出五个职责的逐类、逐独立组数量表。没有正例的类别，recall 标为不可估。

<a id="preflight"></a>
## 7. 训练前检查（留存通过/失败记录）

- **视觉路径**：用同一 checkpoint 配套的 processor，检查实际的 `pixel_values`、grid/位置元数据、视觉 token 和 attention mask 是否进入模型，图像证据是否因截断丢失。
- **看图敏感性**：在人工确认需要看图的样本上，做去图、错图替换和纯文本消融。输出没有差异，可能是题目不需要看图，也可能是路径坏了，用这批样本区分。
- **监督位置**：解码若干训练 batch，核对图像尺寸、视觉 token 数、thinking 前缀、答案位置和 mask、标签到答码的映射。超长或坏图样本不能静默丢弃，要计数报告。
- **梯度**：只有 LoRA 和读出参数收到梯度；冻结的视觉部分仍在传递图像特征；loss 和梯度有限。
- **选项重排**：交换选项时同步重映射标签，测顺序敏感性。
- **四格对照**：原始、仅改图、仅改文、联合编辑，逐格裁定预期答案。随机换图可能改变正确答案，不能盲目沿用原标签。

<a id="gates"></a>
## 8. 关卡 G0–G4

| 关卡 | 工作与产物 | 通过 / 停止 |
|---|---|---|
| G0 合同 | 权利、任务、标注审计；独立组与成本清单 | 目标有歧义、拿不到数据或权利未明：停该臂 |
| G1 技术冒烟 | 32–64 条非敏感样本跑通管线；16–32 条 Train 样本做过拟合排错；保存 batch、mask、梯度、重载记录 | 视觉输入非零且有预期的看图敏感性；adapter 有变化、冻结权重不变、重载等价 |
| G2 基线与受限适配 | B0/F0、B1/F1、有限的 B2，至少 3 个种子；分组学习曲线与错误分析 | 没有可学的残差或没有实质收益：保留基线，停止 |
| G3 冻结验收 | Dev 固定选择 → Cal-fit/Cal-policy → 锁定 Test 一次 | `Delta_cost` 的置信下界超过 `delta_cost`，且关键风险合格 |
| G4 影子评估 | 仅在另获授权后，在自然流量上计入真实人审、未回复和失败 | 离线通过不授予上线权限 |

G1 示例（未执行；路径是虚构的；不包含下载）：

```json
{"images":["images/synthetic-status.png"],"messages":[{"role":"user","content":"Infer intent from this synthetic image and the pre-decision message: Please check this status. Labels: L0=status inquiry; L1=other."},{"role":"assistant","content":"L0"}]}
```

```sh
python -m mlx_vlm.train \
  --model /local/pinned-model --data /local/derived-data \
  --train-type lora --train-on-completions --seed 0 \
  --batch-size 1 --gradient-accumulation-steps 4 \
  --lora-rank 8 --lora-alpha 16 --learning-rate 1e-5 \
  --grad-checkpoint --max-seq-length 2048 --iters 100 \
  --cache-size 4 --steps-per-eval 25 --val-batches -1 \
  --adapter-file /local/run/weights.safetensors
```

这只是技术冒烟的起点，不是最优超参。`iters` 计的是 microstep：100 次、累积 4 次，对应 25 次 optimizer 更新。应用 2048 的长度上限前，先核实视觉 token、保留的文字和 completion target，不能为了塞进内存把关键小字压没。续训时恢复的是权重，optimizer 是新建的、RNG 状态没有保存，所以不能叫 exact resume。

<a id="serving-regression"></a>
## 9. 每次训练、导出或换后端后的服务回归

| 案例 | 检查内容 |
|---|---|
| 单请求与并发 | 交错发送不同的状态、问题、选项，与各自独立运行的输出比较；另一个请求绝不能改变选项身份 |
| 图文混合与长度 | processor、pixels/grid、截断方向、实际保留的证据；缺图、坏图、接近长度上限的输入要有明确并计数的结果 |
| 训练态 / 合并 / 导出 | 同样的案例和候选映射，记录 logits、概率和标签差异，特别关注接近平局的样本；不能假定合并或导出保留了视觉和读出 |
| 设备 / 精度 / 量化 | 每种组合单独记录，重新验证校准器和策略 |
| 负载 | 并发、batch、图片预算、冷热缓存、p50/p95、内存、超时和非法输出率 |

<a id="acceptance"></a>
## 10. 验收

定义 `Delta_cost = mean(C_baseline − C_candidate)`，在配对案件上计算。只有 `Delta_cost` 的置信下界超过 `delta_cost`，**且**各项关键风险约束都通过，才算业务成功。不确定性用按案件、会话或用户分组的配对 bootstrap 估计；种子之间的波动单独报告。概率质量、OOS 和风险认证沿用[通用流程 §6](decision-pipeline.md#enterprise-gates)与 [P05](../problems/P05-policy-risk.md)。

可借鉴的公开数据：[MIRE](https://github.com/liujunwen23/MIRE/tree/d101287af90d114c5bf0cbfbd56fe9c52358e3bb)，23 类场景加 23 类意图，官方基线是全参 SFT。只能用于静态图文意图，不能代替企业留出集；数据能否商用要另行核实。
