# Decision readouts and adaptive reasoning / 决策读出与自适应推理

[Home](../README.md) · [中文首页](../README.zh-CN.md) · [Model cards](models.md) · [Evidence](evidence.md) · [Selection guide](selection-guide.md)

Reviewed 2026-10-17. This compares mechanisms and evidence boundaries, not an overall ranking. StartLux facts below come from [arXiv v1](https://arxiv.org/html/2610.17309v1), the [fixed inference repository](https://github.com/StartLuxLabs/StartLux-Decision/tree/cb1d11f1ac9e9b43b95ef3a6468fa29b607c40fd) and model cards. Existing D3/Jev evidence remains archival. No model was run here.

本页比较机制与证据边界，不生成总榜。StartLux 来源为论文 v1、固定推理代码与型号卡片；D3／Jev 的历史证据保留原协议。本次未运行模型。

> October 26 scope note: earlier unqualified D3 rows describe the classic release. [D3-Turbo audit](../updates/2026-10-26-multimodal-training-and-evidence.md#d3-turbo) adds cached state with independent question branches, distinct from Decider v1.2 joint-question attention. It does not establish image fine-tuning. / 10 月 26 日补注：下方历史 D3 表述指经典版；Turbo 复用状态、各题分支独立，不同于 Decider v1.2 联合题目注意，也不证明图像微调。

## 1. Separate the layers / 分开比较不同层

| Layer / 层次 | Question / 应问的问题 |
| --- | --- |
| Contract / 输出契约 | Are these exclusive choices, propositions, ordinal levels or multiple labels? / 是互斥单选、命题、有序等级还是多标签？ |
| Readout / 读出 | Vocabulary rows, a separate code head or a classifier? Which candidates enter normalization? / 使用词表行、独立答码头还是分类器？哪些候选参与归一化？ |
| Attention / 注意力 | Which layers are causal, and can a shared prefix be reused? / 哪些层有因果掩码，能否复用共享前缀？ |
| Learning / 训练 | Which parameters, data and objective changed? Is executable training code actually released? / 改了哪些参数、数据和目标？是否发布了对应训练实现？ |
| Computation policy / 计算策略 | When does it reason, call a tool, retrieve evidence or defer? / 何时推理、用工具、取新证据或转交？ |
| Acceptance / 验收 | Does the complete deployed policy meet risk, coverage, latency and licensing requirements? / 完整策略是否满足风险、覆盖、延迟与使用权要求？ |

An API-compatible probability vector does not make models architecturally equivalent. A one-pass readout does not require reinforcement learning, and an RL name does not prove empirical calibration. Learned judgment and deterministic computation can share an output schema while requiring different evidence.

API 兼容的概率向量不代表架构相同；一次读出不以 RL 为前提，训练名称也不证明经验校准。语义判断与确定性计算可以共用输出契约，但需要不同证据。

## 2. A bounded comparison / 有边界的比较

| System / 系统 | Readout and computation / 读出与计算 | Interpretation / 解释边界 |
| --- | --- | --- |
| StartLux v1.1 Instant | Existing LM projection reads option letters A–Z; full-attention layers become bidirectional, linear-attention layers retain causal behavior. Each question is a separate prompt row. / 保留 LM 投影读 A–Z；仅 full-attention 层改双向，linear-attention 仍因果；每题独立 prompt row。 | One pass per ordinary question, not one shared encoding of all questions. Bidirectional prompts prevent question-independent prefix reuse. / 普通题逐题一次读出，不是所有题共享一次编码；双向提示不能直接复用与问题无关的前缀。 |
| StartLux v1.1 AutoThink | Causal initial readout; gate on maximum option probability; uncertain cases generate a thought, read again and mix initial/post probabilities. / 因果初判，按最大选项概率开门；不确定题生成推理、再读出并混合。 | Conditional extra computation; a trace is not guaranteed correct or useful. Current runtime defaults differ from the published evaluation gate. / 有条件地增加计算，不保证推理正确或有用；当前默认门槛不同于论文评测。 |
| Decision 3.0 | Reviewed package uses a standard backbone plus a dedicated 255-code readout, prompt-bidirectional inference and separate question rows. / 已审阅包使用骨干加独立 255 答码读出、双向提示与逐题 row。 | Code rows are not 255 fixed business labels. The official wrapper rejects training; third-party Vis implements text-only full/LoRA adaptation, with no vision tower. Multimodal training remains unverified. / 答码不是 255 个固定业务类别；官方 wrapper 拒绝训练，第三方 Vis 有去视觉塔的文本 full／LoRA 适配，多模态训练仍未验证。 |
| Perplexity Decider v1.1 | [Native artifact](https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b/blob/14c9d90137962d300f3de95633f7b6535e80c5ce/README.md): Qwen3.8-27B identity, `Qwen3_5Model` runtime, separate 255×5120 head and saved noncausal full-attention. / 原生包声明 Qwen3.8-27B，运行类 Qwen3_5Model，独立 255×5120 头与保存的 full-attention 非因果模式。 | This is a distinct v1.1 artifact; old v1/API results do not automatically transfer. Vocabulary-head exports must preserve code mapping, attention and temperature exactly once. / v1.1 是不同产物，旧版／API 成绩不自动继承；词表导出需保留映射、注意力并仅应用一次温度。 |
| Jev / TypeSafe | Hosted typed judgments; probability/confidence semantics are documented. / 托管类型化判断，公开分布与 confidence 语义。 | Full architecture, weights and RLCD training recipe are not established by the inspected public material. Do not identify its implementation with RLCD². / 已阅资料不足以确立完整架构、权重与 RLCD 配方，不能把它等同于 RLCD²。 |

The [model cards](models.md) and [source register](sources.md) hold pinned identities and licensing. StartLux inference code is Apache-2.0, but its v1.1 weights are CC BY-NC 4.0: commercial use needs separate authorization. D3 and the reviewed Decider cards declare Apache-2.0; base/data terms and artifact-specific restrictions still matter. Publicly readable weights are not a universal commercial license.

各产物版本及许可证见模型卡与来源登记。StartLux 推理代码为 Apache-2.0，v1.1 权重为 CC BY-NC 4.0，商业使用需另获授权；已阅 D3／Decider 卡片声明 Apache-2.0。底座、数据与具体产物仍须分别核查，不能以“可下载”代替使用权。

## 3. What StartLux trains versus what its server does / 训练与服务分开

The paper describes three stages: full-language-parameter supervised decision training; adapter-based task/attention adaptation followed by merging, Instant seed-weight averaging and refitted temperatures; then reasoning supervision and RLCD² for causal AutoThink. Vision remains frozen. The first two stages optimize soft cross-entropy over candidate probabilities, without adding a new classifier head.

论文描述三阶段：语言全参数监督决策训练；adapter 任务／注意力适配后合并，Instant 多种子权重平均并重拟合温度；最后为因果 AutoThink 加入推理监督及 RLCD²。视觉塔冻结；前两阶段以候选概率的 soft CE 训练，没有新增分类头。

RLCD² scores traces using a frozen copy of the reasoning-supervised starting model:

\[
r(x,\tau)=S(p_1(x,\tau),t)-S(p_0(x),t)
-\lambda\max(0,|\tau|-B).
\]

The released reward uses a decision-weighted proper score and a soft penalty beyond a token budget; group-relative policy gradients optimize the reasoning policy. For groups of nonempty traces, the initial score is constant and cancels when rewards are centered, as the paper notes. This is not reinforcement learning executed for each user request, nor a guarantee that deployed confidence is calibrated. [E31](evidence.md#e31) isolates the reported reasoning-efficiency result and its conditions.

RLCD² 用冻结的推理监督起始模型评分，按推理后与推理前的 proper score 差值减软长度惩罚，再以 group-relative policy gradients 优化推理策略。论文也指出：一组非空 trace 的初判分数是常数，奖励中心化时会抵消。它不是每次请求都在线训练，也不保证部署置信度已校准。[E31](evidence.md#e31)单列其推理效率报告及条件。

At the reviewed commit, the public package is an inference/server implementation. The archived `v1/finetune` text LoRA example is inspectable, but does not constitute the complete v1.1 three-stage/RLCD² training package or a verified image fine-tuning recipe. Dataset composition and paper pseudocode should not be relabeled as executable end-to-end reproducibility.

固定版本公开包主要是推理／服务实现；归档 `v1/finetune` 有可读的文本 LoRA 示例，不等于 v1.1 三阶段／RLCD² 完整训练包，也未确立图像微调链路。论文配方、数据组成和伪代码不能直接改称可执行的端到端复现。

For an ordinary AutoThink question, the published policy keeps \(p_0\) when \(\max p_0\geq0.9\); otherwise it generates up to 4,096 tokens and returns \(0.25p_0+0.75p_1\). The current service default gate is **0.6**, with request overrides. The gate uses maximum candidate probability, not the API's transformed `confidence`. Current code also handles looping traces, a configurable post-thought tail (default 4,000 characters), and tournament reduction beyond 26 options. Those are serving policies with their own failure modes and costs.

论文普通 AutoThink 题以 0.9 作门槛：高置信保留初判，否则最多生成 4,096 token，再取初判 25%＋后判 75%；当前服务默认门槛是 **0.6**，请求可覆盖。开门使用最大候选概率，不是 API 经变换的 `confidence`。循环检测、后读默认只保留推理末 4,000 字符、超过 26 候选的锦标赛归约，都属于需单独验证成本与失效条件的服务策略。

## 4. Read the results without manufacturing a leaderboard / 成绩不能拼榜

- **DI public versus full DI.** [E29](evidence.md#e29) records author-run public DI 0.3. The paper says this public component contributes 20% of the full score, leaves the private 80% unevaluated, and was used for Stage 2 recipe/attention/seed selection. Most evaluated task families appear in training. These are development-selected results, not an independent blind test or official full-board submission. Task-family exposure does not by itself prove exact test-item leakage. D3's archived full Index 0.3.2 [E21](evidence.md#e21) cannot be directly ranked against it.
- **DecisionPivot.** [E30](evidence.md#e30) keeps the paper's final model comparison separate. The authors say it was excluded from data/checkpoint/configuration selection; they also authored the benchmark and ran the comparison. Public generators, independent solver code and scoring assets enable inspection, not independent reproduction by themselves. Core pair accuracy, ordinary item accuracy, reused-task reference scores and seven-layer chance-corrected scores are distinct metrics.
- **Version identity matters.** DecisionPivot v1.1 corrected 10 of 13 core generators; the rename from DecideBench did not itself change items. The pinned dataset tables include intermediate checkpoints and differ from the paper's release summary. Its change log says old hosted Jev core runs were not carried into corrected v1.1. Do not silently attach those tables to the paper's final checkpoints, substitute a later engine rerun, or merge scores without checking exact item hashes and runs.
- **Readout speed versus complete AutoThink.** One forward/readout at one in-flight request omits conditional thought generation and the second readout. Accuracy release runs use vLLM 0.19.1; later single-readout measurements use 0.31 under their stated hardware/input conditions. Report full request P95, thought rate/tokens, failures and queueing separately.

中文：DI 公共子集只占完整分数的一部分，且参与过配方／注意力／种子选择，不能称独立盲测或全球榜首；任务家族重叠不等于已证实具体测试题泄漏。DecisionPivot 虽据作者称未参与选择，仍是作者自建自测；程序生成、独立 solver 和公开 scorer 是复现资产，不是第三方复现结论。核心 pair accuracy、普通准确率、复用任务及七层 chance-corrected 分数分别报告。固定版本表格含研究中间态，修正版本和旧 Jev 运行覆盖也不同，不能拼接。单次 readout 延迟不能代替完整 AutoThink 的 P95 和成本。

The inspected launcher enables up to eight images on vLLM 0.31 and disables video; 0.19.1 is text-only. Its default limits distinguish Instant's 131,072-token whole-prefill cap from causal folders' 262,144 configuration. These are runtime boundaries and author engineering checks, not evidence of quality throughout the full context. A model config containing a video token does not prove an implemented video decision service.

已阅 launcher 在 vLLM 0.31 启用最多八图并关闭视频；0.19.1 为仅文本。默认 Instant 完整 prefill 上限 131,072 token，因果包配置可到 262,144；这些是服务边界及作者工程检查，不证明全长度质量。配置有 video token 也不能证明已实现视频决策服务。

## 5. A practical experiment / 实际应怎样比较

For a generic support screenshot, first ask whether the image and contemporaneous text identify the request. Missing intent evidence calls for clarification or retrieval; extra thinking cannot create the missing conversation. Exact arithmetic, date rules and constraints are credible deterministic-tool baselines. Use model reasoning where interpreting and combining supplied evidence is the demonstrated bottleneck.

通用客服截图首先要判断图像与当时文本是否足以确定诉求；缺上下文应澄清或取证，更多思考不能补造缺失会话。精确算术、日期与硬约束应保留确定性工具对照；已提供证据的理解／组合确为瓶颈时，再检验模型推理的价值。

Compare a simple OCR/text baseline, one-pass decision model, short-label generative model and AutoThink at matched evidence, labels and budgets. Freeze the gate, mixture, candidate order/reduction, template, backend, image processor and model revision. Measure coverage at a preset accepted-error target, consequential misses, clarification burden and complete cost. The [multimodal research plan](multimodal-decision-finetuning.md) details splits and visual-path checks.

以相同证据、标签及预算比较 OCR／文本基线、一次判断、短标签生成及 AutoThink。冻结门槛、混合、候选顺序／归约、模板、后端、图像处理和模型版本，再测预定风险下覆盖率、关键漏检、澄清负担及总成本。[多模态研究方案](multimodal-decision-finetuning.zh-CN.md)给出划分与视觉路径检查。

Calibrate and certify thresholds on outputs returned by the actual selection/routing policy, then freeze before final testing. The paper's policy-aware calibration is useful evidence for this design principle, with distribution-shift limitations; it does not certify a new deployment. `none_probability` is documented as an alarm score, not a calibrated probability of missing evidence. Candidate-normalized probabilities, rejection and authority to act remain separate.

在实际选择／路由策略返回的输出上校准和验证阈值，最终测试前冻结。论文的 policy-aware calibration 支持这种实验设计，但保留跨分布限制，不能认证新部署。`none_probability` 是告警分数，不是已校准的缺证据概率；候选内归一化、拒判和动作权限仍需分开。


## October25 follow-up / 10月25日补核

[Decider v1.2](https://huggingface.co/perplexity-ai/pplx-decider-v1.2) changes the unit of attention: every question inside a joint request can see the others. This differs from v1.1's independent question rows and from packing independent requests for throughput. [E36](evidence.md#e36) retains the author grouping comparison: related facets can benefit, independent candidates can suffer, and Flash's public aggregate favors one question per request. Freeze grouping with the calibrator; the published temperatures were fitted in joint format. Training around32k and a262144 runtime ceiling do not validate all long-context decisions. Splitting overlong groups also changes joint semantics.

[Decider v1.2](https://huggingface.co/perplexity-ai/pplx-decider-v1.2)让同请求的问题相互可见，区别于 v1.1 独立问题行及保持请求独立的 packing。[E36](evidence.md#e36)保留作者分组对照：相关属性可能受益，独立候选可能受损，Flash 公共总分偏向逐题请求。分组策略须与校准器一起冻结；发布温度在联合格式拟合。约32k训练与262144运行上限不验证任意长上下文，超长拆组也会改变语义。

[Prism](https://github.com/StartLuxLabs/StartLux-Prism/tree/f32ed8eee9d89ea56dde03a978cf4128d2bbf497) adds CUDA GGUF execution for causal AutoThink, not Instant. Its integer-path batch/cache invariance is distinct from equivalence to BF16 or production calibration. Its own code has no chosen license at this revision; vendored Apache files do not resolve that. [Jeffan](models.md#jeffan) instead uses conditional whole-input rereading below0.9, replacing its first distribution; this is a separate adaptive-computation policy, not StartLux's thought-generation/mixing algorithm.

[Prism](https://github.com/StartLuxLabs/StartLux-Prism/tree/f32ed8eee9d89ea56dde03a978cf4128d2bbf497)为因果 AutoThink 增加 CUDA GGUF 路径，不支持 Instant；整数路径批次／缓存不变性不等于 BF16 等价或生产校准。该版本自有代码尚未选许可证，vendored Apache 文件不解决这一点。[Jeffan](models.md#jeffan)则在低于0.9时重复读取整段输入并替换初判，不是 StartLux 的生成推理／分布混合算法。

The public20% statement above describes historical DI0.3. Current text0.4 Full removes public weight and changes the hidden domain set; vision keeps a different formula. Preserve edition/track with all older evidence rather than updating old scores in place.

上文公共占20%描述历史 DI0.3；当前文本0.4 Full 已取消公共权重并修改隐藏领域集合，视觉公式仍不同。保留旧证据的分轨和版本，不原地改写旧成绩。
