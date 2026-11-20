# Model cards / 模型卡

[Home](../README.md) · [中文首页](../README.zh-CN.md) · [Evidence](evidence.md)

Source review: 2026-11-20. These are source-backed descriptions and curatorial use cases, not production certifications.

`Unknown` is intentional. An inspected source revision does not identify the deployed weight revision. Language support, licenses and resource requirements must be checked for the exact artifact. Recorded weight identifiers are source-reported unless a local binary verification is explicitly documented; recording an identifier is not a claim that the weights were downloaded or hashed here.

<a id="jev"></a>
## Jev / TypeSafe

[Project / model](https://typesafe.ai)

Hosted typed judgments: probabilities over supplied choices, propositions and ordinal rubrics.
托管的结构化判断服务：对选项、命题与有序评分标准输出分布。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Not publicly established by the reviewed material. | 核对的公开资料未明确参数规模。 |
| Mechanism | Proprietary model. Choice/Score confidence summarizes the returned distribution; it is not a separate probability-of-correctness estimate. Noul returns P(yes) with no separate confidence field. Question IDs are not model input; each instruction must be complete. Same-request answers are documented as independent; dependent evidence requires a later request. Question-context independence is not statistical independence of errors. | 专有模型。Choice／Score 的 confidence 是返回分布的统计量，并非独立预测的正确概率；Noul 返回 P(yes)，没有单独 confidence 字段。 文档称问题 ID 不送入模型，instructions 须写完整；同请求答案互不作为上下文，依赖新证据的判断需后续请求。 问题上下文互不读取不等于误差在统计上独立。 |
| Training | Vendor-described RLCD; no customer self-service fine-tuning/LoRA. Request state/instruction customization is not weight adaptation; independent controlled training ablations remain unestablished. | 官方称采用 RLCD；不支持客户自助权重微调／LoRA，state／instructions 定制不是权重适配；独立受控训练消融仍未确立。 |
| Deployment | Hosted API; version1.14 dates Oct14, with latest/preview currently aliasing1.14.0. Pin/log the returned version for tuned policies. No public weights verified. Default64k request/32k per question; opt-in262k is explicitly slower/less accurate. Images/Box require experimental opt-in and are below vendor production standards; Box requires1.14. No audio/video. This availability snapshot was reviewed November1; November13 changelog still lists1.14 as the latest release. No media request run here. | 托管 API；1.14 发布于10月14日，latest／preview 当前指向1.14.0，已调策略应固定并记录返回版本。未核公开权重。默认每请求64k／每题32k；实验262k明确更慢／更不准确。图像／Box需实验开关且低于厂商生产标准，Box需1.14；无音频／视频。 上述可用性快照核查于11月1日；11月13日changelog仍列1.14为最新发布。本次未执行媒体请求。 |
| Suggested use | Managed typed-judgment comparator or frozen semantic-feature generator; compare supervised baselines under the same task and label policy. Keep deterministic business rules in code; separately validate semantic judgments. | 可作为托管类型化判断对照或冻结的语义特征提取器；与监督基线比较时统一任务与标签规则。 确定性业务规则由代码执行，语义判断单独验证。 |
| Boundary | RLCD is vendor-described; the full training recipe is not public. Valid schemas and confidence fields do not establish semantic reliability. Experimental image support is not production readiness; CJK needs its own evaluation. Author deployment stories/smoke checks do not establish a large independently auditable randomized KPI A/B. | RLCD 的完整训练配方未公开；格式合法与置信度字段不等于语义可靠。 实验图片支持不等于生产成熟，CJK 须另测；作者生产案例／smoke 不构成可独立核验的大规模随机 KPI A/B。 |

**License note:** Commercial service terms; no open-weight license implied.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev); [TypeSafe primitives](https://docs.typesafe.ai/primitives); [TypeSafe confidence semantics](https://docs.typesafe.ai/confidence); [Stefan Jansen: Testing Jev on Financial Documents](https://insights.ml4trading.io/p/testing-jev-on-financial-documents); [TypeSafe autoresearch semantic features with CatBoost](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery); [Jev current model identities and customization boundary](https://docs.typesafe.ai/models); [Jev experimental image and Box contract](https://docs.typesafe.ai/images); [Jev probability versus confidence statistics](https://docs.typesafe.ai/confidence); [Pocos author account: evidence, stale-state and phone-agent gates](https://medium.com/@geo.lomidze/jev-in-production-how-we-turned-our-ai-phone-assistant-into-a-fast-predictable-jev-gated-system-4a1b1a85de6c); [Taritas semantic turn detection implementation account](https://taritas.com/blog/semantic-turn-detection-jev); [Agora community Jev VAD integration example](https://github.com/AgoraIO-Community/convoai-jev-vad/blob/c950900359fecd892e0a51cc7e828f83d425e290/README.md); [Judgments and code-owned decisions](https://typesafe.ai/blog/dont-call-it-a-decision-model); [Jev model changelog checked November13](https://docs.typesafe.ai/changelog); [Jev versioned IDs, aliases and experimental long context](https://docs.typesafe.ai/models); [Jev experimental image/Box input contract and production caveats](https://docs.typesafe.ai/images)

<a id="laya"></a>
## Laya classic encoders (package 0.5 defaults to Vega)

[Project / model](https://github.com/NandhaKishorM/laya)

Classic 421M / 322M encoder checkpoints with dynamic option heads; package 0.5 now defaults to a separate Vega frozen-reader engine unless a classic checkpoint is selected.
经典421M／322M编码器检查点及动态选项头；包0.5默认已转为独立Vega冻结reader引擎，使用经典模型须显式选择。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Classic English/specialist about 421M, multilingual about 322M. Default Vega reader starts at 0.8B and supports other selected readers; those are not new classic-encoder sizes. | 经典英语／专项约421M，多语种约322M。默认Vega reader从0.8B起并可另选reader；它们不是经典encoder的新尺寸。 |
| Mechanism | Classic checkpoints use a bidirectional encoder and option-conditioned head. Since 0.5, unnamed Agent/load selects Vega: frozen reader features feed a separate decision engine/fitted heads and calibration. Explicit classic names or vegaml=False retain the encoder path. | 经典检查点为双向encoder加选项条件头；0.5起未指定模型的Agent／load选Vega，以冻结reader特征供独立判断引擎／拟合头及校准。显式经典模型名或vegaml=False保留encoder路径。 |
| Training | Classic cards describe proper-score/policy-gradient training and specialist soft CE; this is not confirmed Jev training reproduction. Vega fit/Learner fits small heads and updates/calibration over frozen-reader features; it does not fine-tune the classic 322M / 421M backbone. Do not merge their label-efficiency or Banking77 results. | 经典卡描述proper-score／策略梯度训练及专项soft CE，不是确认的Jev训练复现。Vega的fit／Learner在冻结reader特征上拟合小头并更新／校准，不微调经典322M／421M骨干；两者标签效率或Banking77结果不得合并。 |
| Deployment | Package 0.5.0 and vegaml 0.17.2 were uploaded November 19. Current classic English/multilingual HF comparisons changed README only, not binary identities. Classic MPS/CPU training examples and Vega local fitting are different workflows; neither is a verified M5 enterprise training outcome here. Record package, reader, head and calibration identities separately. | 包0.5.0及vegaml0.17.2于11月19日上传；所比经典英语／多语种HF仅README改变，binary身份未变。经典MPS／CPU训练例与Vega本地拟合是不同流程，本仓均无M5企业训练效果验证；包、reader、head及校准身份分别记录。 |
| Suggested use | Use explicitly selected classic encoders as low-resource supervised controls; consider Vega fitted-head learning as a separate hypothesis with its own baseline and held-out acceptance. | 显式选择经典encoder作低资源监督对照；Vega拟合头学习另立假设、基线及保留集验收。 |
| Boundary | Classic base/specialist, language and calibration-overlap limitations remain. action.act_probability from the older path is not a safe execution gate. Vega package defaults and conformal/route fields do not certify future shifted traffic; small calibration examples and fitted-head gains are not classic-backbone or production evidence. | 经典基础／专项、语言及校准重叠限制仍保留；旧路径action.act_probability不能作安全执行门槛。Vega默认及conformal／route字段不认证未来漂移流量，小校准例及拟合头收益不是经典骨干或生产证据。 |

**License note:** Reviewed classic cards and package sources declare Apache-2.0; exact Vega reader, fitted artifact, dependency and data terms remain separate. No new classic weights inferred from package/card dates.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Laya model family](https://huggingface.co/convaiinnovations/laya); [Laya Typed-Decisions model card](https://huggingface.co/convaiinnovations/laya-typed-decisions); [Laya documented operational limitations](https://github.com/NandhaKishorM/laya/blob/a4a8921afebfd852bba0000475cfb6ab737a124c/README.md#honest-limits); [Laya current Learner: Banking77 table belongs to a 4B reader/head path](https://github.com/NandhaKishorM/laya/blob/76c9184871feac23609362315cb40f9c32caafc6/README.md); [Vega learning: frozen reader features and fitted TTT head](https://github.com/NandhaKishorM/vegaml/blob/8b0ca58e8d92ac3fc9c5cc682c93aebc7b885a20/docs/learn.md); [Laya 0.5: default Vega engine and classic-checkpoint selection](https://github.com/NandhaKishorM/laya/blob/416dd9ed20da2d43fc40e23712e9adceefabf634/README.md); [Laya 0.5.0: fixed package-release metadata](https://pypi.org/pypi/laya/0.5.0/json); [vegaml 0.17.2: fixed dependency-release metadata](https://pypi.org/pypi/vegaml/0.17.2/json); [Synth-NLP/laya-intencao-ptbr-sintetico — real-label and synthetic augmentation experiment](https://huggingface.co/Synth-NLP/laya-intencao-ptbr-sintetico/blob/eae976f3b0663d67fe09b92fb5b04d9887f4efc8/README.md)

<a id="kev"></a>
## Kev

[Project / model](https://github.com/jaredpalmer/kev)

Qwen-based typed decision family with a dynamic pointer head; Kev 1.0 freezes existing checkpoints as a release baseline.
Qwen 骨干与动态 pointer head 的类型化判断系列；Kev 1.0 将现有检查点固定为发布基线。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Released family spans 0.8B, 4B, 9B and 27B; inspect the exact backbone/card. | 公开系列覆盖 0.8B、4B、9B、27B；须核对具体骨干与模型卡。 |
| Mechanism | Dynamic option readout on a language-model backbone; several model sizes. | 在语言模型骨干上动态读出选项分数；提供多个规模。 |
| Training | 0.8B/4B/9B use LoRA plus a head. 27B v2 fully fine-tunes Qwen3.8-27B, then averages weights 0.85/0.15 with v1. Temperature fitting is distribution-specific; 0.8B/4B use held-out items from trained families. Oct22 adaptation scripts distinguish full question/rubric identity, keep state variants in one split, and reject exact fractional JSON ordinal labels before float rounding. Data-contract fixes, not a weight release. | 0.8B／4B／9B 使用 LoRA 与判断头；27B v2 全参数微调 Qwen3.8-27B，再按 0.85／0.15 与 v1 平均权重。温度拟合依赖分布；0.8B／4B 使用训练任务族的保留样本。 10 月 22 日适配脚本按完整问题／rubric 判冲突、同状态变体不跨划分，并在浮点舍入前拒绝真实小数序数标签；这是数据契约修复，不是权重发布。 |
| Deployment | Small releases require the base plus adapter/head; 27B v2 ships about 51 GB of full bf16 weights plus head. Served limit: 65,536 tokens. Author-validated CUAD context: 8,192 for 0.8B/4B/9B, 65,536 for 27B, under the stated 3-pp non-inferiority rule. Current server supports explicit CPU/accelerator selection and isolated fail-closed probes; those probes do not validate every kernel. | 小型号需基座、适配器与判断头；27B v2 发布约 51 GB 的完整 bf16 权重与判断头。服务上限 65,536 token；按作者 CUAD 的 3 个百分点非劣效规则，0.8B／4B／9B 仅验证至 8,192，27B 至 65,536。 当前服务支持明确 CPU／加速器选择及隔离 fail-closed 探测；探测不验证所有内核。 |
| Suggested use | An inspectable starting point for domain-supervised decision models. | 可检查、可微调的领域监督判断实验底座。 |
| Boundary | Keep trained-family tests separate from transfer. 27B v2 is worse and overconfident on long contracts (CUAD ECE 0.053 versus v1 0.007). Serving capacity and fitted temperature do not guarantee accuracy or calibration on new workloads. | 须区分训练任务族测试与迁移测试。27B v2 在长合同上退步且过度自信（CUAD ECE 0.053，v1 为 0.007）；可接收长度和拟合温度不保证新任务的准确率或校准。 |

**License note:** Kev 1.0 cards declare Apache-2.0 for the released weights/head and listed bases; verify the exact artifact. A family entry has no single weight revision.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Kev repository](https://github.com/jaredpalmer/kev/blob/2855ba2a55a80579176a459f78b95d03548cabb5/README.md); [Kev-4B model card](https://huggingface.co/jaredpalmer/kev-4b); [Kev 1.0 release baseline](https://github.com/jaredpalmer/kev/blob/5e42a7a03f28134853dd3ff77461457e921e5ec1/docs/releases/kev-1.0.md); [Kev-27B v2 model card](https://github.com/jaredpalmer/kev/blob/5e42a7a03f28134853dd3ff77461457e921e5ec1/docs/model-cards/kev-27b.md); [Kev current serving and source-watch review](https://github.com/jaredpalmer/kev/blob/85ccf56a0afb952323c621055b02876e8498d60c/README.md); [Kev: complete-question identity for data splits and conflict detection](https://github.com/jaredpalmer/kev/commit/ac8e24524695cfb2d5147bf8063c3db3ef9276e6); [Kev: preserve exact JSON score fractions before label validation](https://github.com/jaredpalmer/kev/commit/e7ae8fd5fda9d40865d3a9de90f074feb0735985); [Synth-NLP/kev-0.8b-intencao-ptbr-sintetico — real-label and synthetic augmentation experiment](https://huggingface.co/Synth-NLP/kev-0.8b-intencao-ptbr-sintetico/blob/fbe9f5a9e420fe46f5db2825581a5e68c7704c3f/README.md); [Synth-NLP/kev-4b-intencao-ptbr-sintetico — real-label and synthetic augmentation experiment](https://huggingface.co/Synth-NLP/kev-4b-intencao-ptbr-sintetico/blob/0aa1eaea1d8f0c684b5ff1058112a9fa49f45d94/README.md)

<a id="clm"></a>
## Contrastive Language Models (CLM)

[Project / model](https://github.com/Contrastive-LM/CLM)

Separate state and action representations with learned projection heads on a frozen language-model encoder.
冻结语言模型编码器，分别表示状态与动作，再用可训练投影头匹配。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | 8B base encoder plus learned heads in the reviewed release. | 本版核对的发布使用 8B 骨干及可训练投影头。 |
| Mechanism | Dual encoding permits candidate caching; released base uses frozen Qwen3-8B. | 双侧编码允许缓存候选；发布的基础版使用冻结 Qwen3-8B。 |
| Training | Contrastive InfoNCE with negatives; specialized heads require their own evidence. | 含负例的 InfoNCE 对比学习；专项投影头需单独评测。 |
| Deployment | Local code and weights; backbone still runs at inference. | 公开代码与权重；推理仍需运行骨干。 |
| Suggested use | Reusable candidate catalogs, tool selection and domain-trained Best-of-N selection. | 适合候选可复用的工具目录、排序及领域 Best-of-N 选择。 |
| Boundary | Relative ranking cannot detect every all-wrong candidate set. Best-of-N scores include supplied candidates, not autonomous task-solving ability. | 相对排序不能保证识别“全部候选都错”；Best-of-N 成绩不代表模型独立解题能力。 |

**License note:** Base card: Apache-2.0. Reviewed DeepSWE head card: MIT. Do not assign one license to the whole family.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [CLM repository](https://github.com/Contrastive-LM/CLM/blob/bb42c6c5bf914fd449bed2f6ca65be80602cb1f7/README.md); [CLM v0.1-8B model card](https://huggingface.co/Contrastive-LM/CLM-v0.1-8B); [DeepSWE fixed-split projection head](https://huggingface.co/Contrastive-LM/deepswe-clm-heads-8k); [CLM citation-only source-watch review](https://github.com/Contrastive-LM/CLM/blob/d5f9ef0fd9bde185df0ceaad4f4ecc6cfe8c34f6/README.md)

<a id="nimble"></a>
## Bespoke Nimble

[Project / model](https://github.com/bespokelabsai/nimble)

Open Qwen3.5-9B supervised decision adapter, distinct from the later Nimble hosted v4/v4.1 service.
开放Qwen3.5-9B监督判断adapter，与后续Nimble托管v4／v4.1服务分别识别。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | 9B backbone plus adapter; adapter bytes alone are not required memory. | 9B 骨干加适配器；适配器文件大小不等于所需内存。 |
| Mechanism | The open 9B model applies LoRA and reads allowed answer-token logits; candidate logits are divided by temperature before softmax, once. | 开放9B用LoRA并读允许答案token的logits；候选logits除以温度后做softmax，温度只应用一次。 |
| Training | Supervised candidate-token CE; minimal-edit evidence pairs are data construction, not an embedding contrastive loss. The reviewed curriculum has 2,676 synthetic training and 324 synthetic evaluation rows; these are not independently adjudicated human benchmark labels. | 候选token交叉熵监督；最小事实改动对是数据构造，不是表示层对比损失。已阅课程含2676合成训练／324合成评测行；不等同独立人工基准参考标签。 |
| Deployment | The open 9B model requires the Qwen3.5-9B base plus a PEFT adapter; the pinned card specifies 8k context, 255 options and T=1.0, distinct from original-2676/v2. Public MLX inference does not establish Mac training. Later hosted version claims do not identify an open v4 weight release. | 开放9B需Qwen3.5-9B底座加PEFTadapter；当前卡为8k上下文、255选项、T1.0，与original-2676／v2区分。MLX推理不证明Mac训练；后续托管版本声明不等于开放v4权重。 |
| Suggested use | A transparent baseline for evidence-sensitive judgments and minimal-edit training examples. | 适合证据敏感的判断，也可借鉴最小差异训练样本。 |
| Boundary | Keep the open 9B model, historical evaluated checkpoints and hosted versions separate. Public benchmarks are author-run and raw runs are incomplete. Minimal-edit examples are a reusable data idea, not production outcome evidence. | 须区分开放9B、历史被测检查点及托管版本。公开基准由作者运行，完整原始逐次输出不全。最小事实改动法可借鉴，但不是生产效果证明。 |

**License note:** Pinned open9B model card declares Apache-2.0; base/dependencies retain their terms. No root LICENSE found in the inspected current GitHub tree; do not infer a blanket source-code license from model metadata.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Bespoke Nimble model card](https://huggingface.co/bespokelabs/Bespoke-Nimble-9B); [Nimble public human-reference benchmark protocol and results](https://github.com/bespokelabsai/nimble/blob/62076b4f2d365b5879dafcf7f6dd072a1fe76df7/docs/PUBLIC_BENCHMARKS.md); [Nimble current repository: hosted versions and local training/inference](https://github.com/bespokelabsai/nimble/tree/b30ec429fcd78c15fa12a5d3b68c5fbc3bf0430f); [Bespoke-Nimble-9B: exact open adapter card](https://huggingface.co/bespokelabs/Bespoke-Nimble-9B/tree/bd792f44ec8e265be861bfcdf4e05967ffe0e858)

<a id="gliner-decide"></a>
## GLiNER2.5-Decide

[Project / model](https://huggingface.co/fastino/GLiNER2.5-Decide-1B)

Schema-conditioned local classification with runtime labels and multiple decision heads.
通过运行时标签与多个判断头实现模式条件化的本地分类。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | 1B card directly reviewed; 340M and 287M sibling results/links are cross-reported there. | 直接核对 1B 卡；340M 与 287M 同系列资料由该卡交叉报告。 |
| Mechanism | Encoder-style classification; single-label and multilabel outputs. | 编码器式分类；支持单标签与多标签输出。 |
| Training | Treat checkpoint-specific training details as documented, not inferred from sibling models. Oct20 runtime fixes distributed gradient synchronization; audit prior multi-GPU adaptation runs. Published checkpoint exposure to this defect is unknown; no inferred retraining or gain. | 训练细节按具体检查点文档记录，不从同系列模型推断。 10 月 20 日运行库修复多卡梯度同步，既有分布式适配运行应核查；公开检查点是否受影响未知，不推断已重训或性能提升。 |
| Deployment | Published checkpoints; current runtime supports Transformers 5 and schema-extraction loading. Match runtime, checkpoint config and classify_text examples; unchanged LFS weight identity across the watched revisions. | 公开检查点；当前运行库支持 Transformers 5 与 schema-extraction 加载。须匹配运行库、检查点配置及 classify_text 示例；所监测两版本的 LFS 权重标识相同。 |
| Suggested use | Compact operational classification; inspect the runtime for supported cross-field constraints. | 适合轻量业务分类；跨字段约束需核对具体运行库支持。 |
| Boundary | This review inspected the 1B card, which cross-reports 340M results. Dataset audit is incomplete; JevK5 in that table is not TypeSafe Jev. | 本版核对的是 1B 模型卡，其中交叉报告 340M 成绩；数据集审计未完成，表中 JevK5 不是 TypeSafe Jev。 |

**License note:** Reviewed 1B card declares Apache-2.0; other checkpoints need separate checks.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [GLiNER2.5-Decide-1B model card](https://huggingface.co/fastino/GLiNER2.5-Decide-1B); [GLiNER2 runtime](https://github.com/fastino-ai/GLiNER2); [GLiNER2 runtime compatibility review](https://github.com/fastino-ai/GLiNER2/blob/b86d35c02f2c1a4d9840ea50197bd1b6d13b031e/README.md); [GLiNER2.5-Decide-1B current compatibility metadata](https://huggingface.co/fastino/GLiNER2.5-Decide-1B/blob/67af949e17bebd20f05fe020a971079889e7a462/README.md); [GLiNER2: distributed training gradient synchronization fix](https://github.com/fastino-ai/GLiNER2/commit/fe3145e065958f9d6f738cdc891acff0cd673efc)

<a id="gliclass"></a>
## GLiClass (v4 family; v4.1 Edge metadata only)

[Project / model](https://github.com/Knowledgator/GLiClass)

Label-conditioned classification family: v4 adds decoder-KV/label scoring and multimodal Qwen variants; v4.1 Edge is an incompletely documented artifact.
标签条件分类系列：v4有decoder-KV／label评分及多模态Qwen变体；v4.1 Edge目前属于文档不完整的产物。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Checkpoint-specific: v4 Edge 0.4B uses DeBERTa; v4 Qwen-based 2B / 9B / 27B variants have separate identities. No single family size or calibration claim. | 依检查点而定：v4 Edge0.4B用DeBERTa，v4 Qwen系2B／9B／27B分别固定身份，不为整族指定单一规模或校准结论。 |
| Mechanism | In reviewed v4 decoder-KV variants, the backbone encodes input evidence, transient label tokens read its cache, and a label scorer/refinement cell produces scores without text generation. Single-label softmax and multilabel scores are different contracts; inspect the chosen architecture. | 所阅v4 decoder-KV变体先编码输入证据，再由临时label token读缓存，label评分／迭代模块输出分数，不生成文本。单标签softmax与多标签分数的合同不同，须核具体架构。 |
| Training | The repository provides supervised training entry points; reviewed v4 cards describe decision-mixture training and, for calibrated releases, a fitted per-pair calibrator. The exact released-v4 full pipeline and all data were not independently replayed. Do not infer a usable v4.1 recipe from the older family trainer. | 仓库提供监督训练入口；所阅v4卡描述判断数据混合训练，带校准器的发布物另拟合逐对calibrator。未独立重放精确v4完整流程和所有数据，也不能从旧family trainer推定v4.1已有可用配方。 |
| Deployment | Public v4 cards and weights exist. v4 Edge includes a calibrator; the reviewed 2B card explicitly ships without one and warns of saturated raw scores. November 9 v4.1 Edge has model/config/tokenizer files but no inspected README/LICENSE/cardData. No verified M5 training result or v4.1 deployment contract. | v4模型卡及权重公开；v4 Edge带calibrator，所阅2B卡明确未带并提醒raw分数趋0／1。11月9日v4.1 Edge有model／config／tokenizer，但所查无README／LICENSE／cardData；没有已验证M5训练结果或v4.1部署合同。 |
| Suggested use | Dynamic intent/label classification comparator, choosing single-label or multilabel semantics and measuring task-specific calibration. | 作为动态意图／标签分类对照，先选单标签或多标签语义，再量具体任务的校准。 |
| Boundary | Architecture, label cardinality and calibrator differ by release. Do not inherit v4 license/quality/training claims into undocumented v4.1; a high label score is not a certified correctness probability or enterprise routing guarantee. | 不同发布物的架构、标签数及calibrator不同；不得将v4许可／质量／训练声明继承给缺文档v4.1，高label分数不是认证正确概率或企业路由保证。 |

**License note:** Reviewed v4 cards/repository declare Apache-2.0; v4.1 Edge lacks inspected license metadata/files and remains unresolved. Verify each model/base/data artifact separately.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [GLiClass](https://github.com/Knowledgator/GLiClass); [GLiClass current repository: versions and training entry](https://github.com/Knowledgator/GLiClass/blob/af82d425c0259a6f46f240bb0633fcdab821eaea/README.md); [GLiClass v4 Edge: DeBERTa decision scorer and calibrator](https://huggingface.co/knowledgator/gliclass-v4-edge/blob/885af1af8a07edf4ed34df83ca0d995ed8201283/README.md); [GLiClass v4 2B: multimodal decoder-KV scorer](https://huggingface.co/knowledgator/gliclass-v4-2b/blob/40fe023b45e8d97d1ae4f7f9342279ac1c76317d/README.md); [GLiClass v4 27B: Qwen-based multimodal scorer](https://huggingface.co/knowledgator/gliclass-v4-27b/blob/acd9c277c2175de565cc9546e1cc3a45b1a63d5c/README.md); [GLiClass v4.1 Edge: unreviewed artifact metadata](https://huggingface.co/knowledgator/gliclass-v4.1-edge/tree/6a05e85cbaa7ab536d6dcd19bcfb3ab3b63d6a4d)

<a id="jevos"></a>
## jevos (current v5; historical v2)

[Project / model](https://github.com/feder-cr/jev)

Local CPU typed decisions in a Jev-shaped API: v5 adds documented choice and early score support alongside yes/no, with OpenVINO INT8 and GGUF assets.
本地CPU类型化判断，采用Jev形状的API：v5文档在是非之外加入choice和早期score支持，发布OpenVINO INT8及GGUF产物。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Earlier documentation described 1B; an independently checked current-v5 tensor parameter count and exact base identity were not established. | 早期资料称1B；本轮未独立核算当前v5张量参数量，也未建立精确base身份。 |
| Mechanism | Current v5 documentation returns per-answer probabilities and expected score levels without free-form output; several questions share an input request. The earlier audited fixed binary-token readout belongs to an older version, not a verified complete v5 implementation audit. | 当前v5文档返回候选概率和期望评分，不输出自由文本；同输入可带多个问题。此前核读的固定二元token读出属于旧版，不能冒称已完整审计v5内部实现。 |
| Training | A complete training recipe, dataset and base-checkpoint lineage remain unestablished. The seven task sets described in the v5 README helped select the released checkpoint, so they are development evidence rather than an untouched independent test. | 完整训练配方、数据及base谱系仍未建立；v5 README所列七组任务参与发布检查点选择，属于开发证据，不是未触及的独立测试。 |
| Deployment | GitHub v5 release published October 16 with Linux, Windows and macOS-arm64 binaries, OpenVINO INT8 and q4/q8 GGUF plus SHA256SUMS. HF main has a different earlier timestamp; equality to the GitHub v5 package is not authenticated. Asset metadata and Mac binary existence are not a local weight hash or M5 training result. | GitHub v5于10月16日发布Linux／Windows／macOS-arm64程序、OpenVINO INT8及q4／q8 GGUF和SHA256SUMS。HF main时间较早，尚未认证其与GitHub v5包相同；asset元数据及Mac程序存在不等于本地权重hash或M5训练结果。 |
| Suggested use | A CPU inference comparator for short policy/triage decisions; validate each supported type and the exact released artifact before considering adaptation. | 作为短规则／分流判断的CPU推理对照；考虑适配前，先验证各题型与精确发布产物。 |
| Boundary | Do not apply old v2 noul-only/422/ignored-criteria descriptions to v5. Wire-format compatibility does not establish semantic equivalence; score support is labeled early. Current parameter lineage, calibrated risk and a usable enterprise fine-tuning path remain unknown. | 不可把旧v2仅noul／422／忽略criteria的描述套给v5。接口形状兼容不等于语义等价，score仍标为早期支持；当前参数谱系、校准风险及可用企业续训链仍未知。 |

**License note:** Repository LICENSE is MIT and the inspected HF metadata declares MIT; exact GitHub v5 weight/base provenance and any inherited terms are not fully authenticated here.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [jevos pinned README and runtime documentation](https://github.com/feder-cr/jev/tree/9e7d9e8a24e9605bec249045a39df91ff2b58b0d); [jevos-v2 release and asset metadata](https://github.com/feder-cr/jev/releases/tag/jevos-v2); [jevos repository README](https://github.com/feder-cr/jev/blob/eb74cf78e5377e85fcaa76f6ebc9f82e8b517250/README.md); [jevos v5: dated release and downloadable asset identities](https://github.com/feder-cr/jev/releases/tag/jevos-v5); [jevos current README: v5 typed CPU decisions](https://github.com/feder-cr/jev/blob/2383312e05b4379aee3432140f44b06eaa53dddd/README.md)

<a id="clef"></a>
## Clef / Clef-Flash / Clef-Omni

[Project / model](https://huggingface.co/Cloudflare/clef)

Cloudflare typed-decision family: dense Clef/Flash and October 9 Clef-Omni use joint schema scoring; Clairic is a separate extraction family.
Cloudflare类型化判断系列：稠密Clef／Flash及10月9日Clef-Omni用联合schema评分；Clairic是独立提取系列。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Clef 27B Qwen3.8, Flash 9B Qwen3.5, and Omni Qwen3-Omni-30B-A3B-Instruct thinker. Omni card reports about 64 GB BF16 on H200; active MoE size does not imply 48 GB training fit. | Clef27B基于Qwen3.8，Flash9B基于Qwen3.5，Omni基于Qwen3-Omni-30B-A3B-Instruct thinker。Omni卡示例BF16约64GB／H200，MoE激活规模不意味着48GB能训练。 |
| Mechanism | A joint transformer schema head routes state evidence and scores allowed options without free-form text generation. Omni retains visual/audio encoders, while unused speech-output modules are not loaded. Clairic extraction generation must not be attributed to these decision releases. | 联合Transformer schema头路由state证据并给允许选项评分，不生成自由文本；Omni保留视觉／音频编码器，不加载未用的语音输出模块。不可将Clairic提取生成机制归入这些判断发布物。 |
| Training | The original dense Clef report describes rank 256 LoRA plus routing head, smoothed CE, Brier and secondary RLCD on internal synthetic data; full data/recipe not independently audited. Do not silently assign that exact recipe to Omni. The MersivMedia community adaptation remains experimental, without a verified real-weight multimodal run/export or RLCD reproduction. No complete Omni enterprise fine-tuning package was established in this refresh. | 原稠密Clef报告描述rank256 LoRA加routing head、平滑CE、Brier与辅助RLCD，数据为内部合成；完整数据／配方未经独立审计，不可默认为Omni也用完全相同配方。MersivMedia社区适配仍为实验实现，未验证真实权重多模态训练／导出或RLCD复现。本轮未建立完整Omni企业微调包。 |
| Deployment | Public custom HF runtimes and Workers AI. Omni binary package dates to October 9; later metadata are evaluations. October 9 Clef serving speedups and Flash hosted context 64k→24k did not change dense weights. Local defaults, hosted limits and media/truncation differ. Existing MLX-VLM inference support is not generic SFT-head training support; no M5 training verified. | 公开定制HF运行库及Workers AI；Omni binary包始于10月9日，后续metadata为评测。10月9日Clef服务提速及Flash托管context64k→24k未改变稠密权重。本地默认、托管上限、媒体与截断合同不同；已有MLX-VLM推理支持不等于通用SFT-head训练，未验证M5训练。 |
| Suggested use | Compare bounded judgments using required text/image/audio/video evidence, at matched workload risk and full-system cost. | 按任务所需文本／图像／音频／视频证据，在相同风险与完整系统成本下比较有界判断。 |
| Boundary | Vendor task-specific benchmarks and API compatibility do not certify business risk. Keep Omni, dense releases and adjacent Clairic extraction distinct. Public weights do not prove complete original-data replay, a customer-training service contract, or local Mac training feasibility. | 厂商分任务基准及API兼容不认证业务风险。Omni、稠密发布物及邻接Clairic提取须分别识别；公开权重不证明完整原始数据重放、客户训练服务合同或Mac本地训练可行。 |

**License note:** Reviewed dense and Omni cards declare Apache-2.0; exact bases, datasets, runtime notices and any training-service terms require separate checks.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Cloudflare Clef launch and evaluation report](https://blog.cloudflare.com/clef-decision-models/); [Clef 27B model card](https://huggingface.co/Cloudflare/clef/blob/2f3de3dd85f379784083b0814d997ab627200f0c/README.md); [Clef-Flash 9B model card](https://huggingface.co/Cloudflare/clef-flash/blob/17f0b0ad64efb65d273590632833508766b2aae6/README.md); [Clef Workers AI interface and context limit](https://developers.cloudflare.com/workers-ai/models/clef/); [Community Clef adapter and FP32 head training loop](https://github.com/MersivMedia/clef-finetune/blob/c83f7bc1acc23c81ad0de838510c59c48bf60c79/src/clef_finetune/train.py); [Community Clef fine-tuning explicit unverified cases](https://github.com/MersivMedia/clef-finetune/blob/c83f7bc1acc23c81ad0de838510c59c48bf60c79/docs/KNOWN_ISSUES.md); [MLX-VLM Clef image inference and custom call contract](https://github.com/Blaizzy/mlx-vlm/blob/2ceff4c14b991370a459d14eb49d1bedf4fb9e84/mlx_vlm/models/clef/clef.py); [Clef: safeagents evaluation YAML only, unchanged weight identities](https://huggingface.co/Cloudflare/clef/commit/cfddda043dd190ef3b01cff449d5ee8cff1e8ec6); [Clef-Omni: fixed model, media and memory contract](https://huggingface.co/Cloudflare/clef-omni/blob/189097bdeaaaea246bd876310d4ae30f9a50415a/README.md); [Cloudflare October9: Clef-Omni release and Clef serving changes](https://blog.cloudflare.com/clef-faster-cheaper-multimodal/)

<a id="strands-decider"></a>
## Strands Decider (v1 pointer / v2 code readout)

[Project / model](https://github.com/strands-labs/strands-decider)

Qwen / Gemma decision family: v1 adapter-and-pointer releases and November 17 Gemma 4 E2B v2 merged code-readout release have different training and serving contracts.
Qwen／Gemma判断系列：v1为adapter与pointer发布物，11月17日Gemma4 E2B v2为合并权重与答码读出；训练及服务合同不同。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | v1 spans Qwen3.5 2B and Gemma 4 E2B/E4B/12B/26B-A4B. Released v2 E2B is 2.3B effective and 5.1B with embeddings, about 10.3 GB BF16; active size is not resident memory. | v1覆盖Qwen3.5 2B及Gemma4 E2B／E4B／12B／26B-A4B。已发布v2 E2B为2.3B有效参数、含embedding共5.1B，BF16约10.3GB；激活规模不等于驻留内存。 |
| Mechanism | v1 replaces the LM head with a dynamic pointer head. v2 E2B trains a 255-code LM-row readout with strands-chat and prefix_bidir: state is shared, question branches are isolated, and all Gemma layers use the stated full-prompt mask, including normally sliding-window layers. No free-text generation. | v1以动态pointer头替代LM头；v2 E2B用255答码LM-row读出、strands-chat及prefix_bidir：共享state，各题分支隔离；按其专用mask处理全部Gemma层，包括通常的滑窗层。不生成自由文本。 |
| Training | v1 Qwen / Gemma recipes and three-seed adapter/head soups remain historical and have missing inputs. Current source also publishes v2 from-base supervised recipes: E2B rank 64 / alpha 128 LoRA plus token readout, prefix_bidir and a typed-row converter. Original v2 training/dev data are absent; the converter drops images and missing instructions. Export merges adapters into base BF16 shards and saves readout.safetensors plus decision_config.json. The trainer supports token-readout training but rejects its frozen-KL anchor option. | v1的Qwen／Gemma配方与三种子adapter／head平均保留为历史，部分输入缺失。当前源码也公开v2从原始底座开始的监督配方：E2B为rank64／alpha128 LoRA加token readout、prefix_bidir及typed-row转换；原v2训练／开发数据未公开，转换器丢弃图片及缺instructions行。导出将adapter合入base BF16 shards，另存readout.safetensors和decision_config.json；trainer支持token-readout训练，但拒绝其frozen-KL选项。 |
| Deployment | v1 trained adapter/head checkpoints can use init_from and then recalibrate. Released v2 is a merged decision checkpoint without the training config/adapter layout expected by that init_from loader; direct domain continuation from its HF ID is not established. Public v2 recipes can train on supplied text rows from the original base, or continue a retained unmerged training checkpoint. v2 MPS/CPU support on the card is inference; training selects CUDA else CPU and documents Linux/WSL NVIDIA. No M5 training run or generic MLX calibration support verified. | v1已训adapter／head检查点可用init_from并重新校准；发布v2为合并decision检查点，不含该init_from loader要求的训练config／adapter布局，尚未建立直接从其HF ID领域续训的路径。公开v2配方可从原始底座用自备文本训练，或继续保留的未合并训练检查点。卡片的MPS／CPU支持指推理；训练器选择CUDA否则CPU，文档以Linux／WSL NVIDIA为环境，未验证M5训练或通用MLX校准。 |
| Suggested use | Compare v1 and v2 on the same bounded text decisions; audit the actual domain-training starting point and exported inference path before selecting a recipe. | 在相同有界文本判断上比较v1与v2；选配方前核对领域训练从何种权重开始及导出后的推理路径。 |
| Boundary | Do not transfer v1 pointer/soup/KL or missing-image results to v2. v2 was trained on text; inherited image input is not image-adaptation evidence. Author public benchmarks and calibrated temperature do not certify enterprise risk. Legacy E07/E08/E11 and their missing-data/development-selection limitations remain dated records. | 不可将v1的pointer／soup／KL或缺图结果直接套给v2。v2仅用文本训练，继承图片输入不等于图像适配证据。作者公共基准及拟合温度不认证企业风险；E07／E08／E11及其缺数据、开发选择限制保留为带日期记录。 |

**License note:** Reviewed v1 adapter/head and v2 model/code declare Apache-2.0; v1 loads a separate base, v2 ships merged base plus readout. Check exact base/data terms; no M5 or original-data replay claim.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Strands Decider repository](https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/README.md); [Strands Decider architecture](https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/docs/architecture.md); [Strands Decider v19 experiment configuration](https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/configs/experiments/v19.yaml); [Strands Decider evaluation and limitations](https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/evaluation/README.md); [Strands Decider experiment record](https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/research/README.md); [Strands Decider original and AWS retrain results](https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/evaluation/results.md); [Strands Decider published v19 adapter card](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v19/blob/bb282d786bc251fd4e3068de3ada9ddbb38127cd/README.md); [Strands Decider published adapter provenance](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v19/blob/bb282d786bc251fd4e3068de3ada9ddbb38127cd/provenance.json); [Strands Decider v21 release and same-host seed results](https://github.com/strands-labs/strands-decider/blob/3e94e9d84c620ed5a95f1a3310c3decb971e261c/evaluation/results.md); [Strands Decider released v21b recipe](https://github.com/strands-labs/strands-decider/blob/3e94e9d84c620ed5a95f1a3310c3decb971e261c/configs/experiments/v21b.yaml); [Strands October 9 v1 releases](https://github.com/strands-labs/strands-decider/blob/0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534/CHANGELOG.md); [Strands Qwen3.5 / Gemma 4 v1 results](https://github.com/strands-labs/strands-decider/blob/0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534/evaluation/results.md); [Strands Gemma 4 serving limits and attention fix](https://github.com/strands-labs/strands-decider/blob/0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534/docs/inference.md); [Strands Qwen v1 missing-image reliability](https://github.com/strands-labs/strands-decider/blob/0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534/docs/vision.md); [Strands dataset/source inventory](https://github.com/strands-labs/strands-decider/blob/0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534/data/sources.md); [Strands: request-local pointer offsets and tokenizer/cache concurrency fixes](https://github.com/strands-labs/strands-decider/commit/6039cf8b64c6074e75804000c07ac3d4cce795f7); [Strands: eval/calibrate use serving model preparation](https://github.com/strands-labs/strands-decider/commit/930e6d5de16309be32579f5631a7369a3322140c); [Strands: five published v1 seed-0 training configurations and missing-input disclosure](https://github.com/strands-labs/strands-decider/commit/94f1cc1d491ebc456140103ea60c5f7daa21eca8); [Strands: continuing released adapter and head training](https://github.com/strands-labs/strands-decider/commit/e69edb2650d87ecdd28e6ff0563c5a40d716f1f1); [Strands: retire slot heads and require explicit frozen pointer KL reference](https://github.com/strands-labs/strands-decider/commit/13c05149265dc404c09d2469636f71b1320e1713); [Strands: keep Gemma4 MLX loading and execution on one owned worker](https://github.com/strands-labs/strands-decider/commit/13faf5214f7cbea07d005278f1aeaf3973611eba); [Strands Decider v2 E2B: merged decision checkpoint](https://huggingface.co/StrandsAgents/strands-decider-E2B-gemma4-v2-2611/blob/a74ee815c2af08d16afd0b9dfa079ce260cfafdb/README.md); [Strands v2: recipe, data conversion and release-checkpoint boundaries](https://github.com/strands-labs/strands-decider/blob/d4915c9b11f61bb01ed293f4dc4c770a0a51792b/training/README.md); [Strands v2 E2B: fixed from-base LoRA configuration](https://github.com/strands-labs/strands-decider/blob/d4915c9b11f61bb01ed293f4dc4c770a0a51792b/configs/v2/strands-decider-E2B-gemma4-v2-2611.yaml); [Strands trainer: token-readout, init_from and device contracts](https://github.com/strands-labs/strands-decider/blob/d4915c9b11f61bb01ed293f4dc4c770a0a51792b/training/train.py); [Strands v2: supervised row converter](https://github.com/strands-labs/strands-decider/blob/d4915c9b11f61bb01ed293f4dc4c770a0a51792b/training/data/strands_v2.py); [Strands v2: merge and decision-checkpoint export](https://github.com/strands-labs/strands-decider/blob/d4915c9b11f61bb01ed293f4dc4c770a0a51792b/training/export_v2.py); [Strands training checkpoints: required config and adapter layout](https://github.com/strands-labs/strands-decider/blob/d4915c9b11f61bb01ed293f4dc4c770a0a51792b/src/strands_decider/modeling.py)

<a id="pplx-decider"></a>
## Perplexity Decider (current v1.3; archival v1 / v1.1 / v1.2)

[Project / model](https://huggingface.co/perplexity-ai/pplx-decider-v1.3)

v1.3 typed-decision and optional span-location family; 27B Qwen3.8 and distilled Flash 4B Qwen3.5, with distinct earlier versions.
v1.3类型化判断及可选span定位系列；27B Qwen3.8与蒸馏Flash 4B Qwen3.5，早期版本分别保留。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | 27B Qwen3.8 and Flash 4B Qwen3.5; distinct head sizes and calibrators. | 27B Qwen3.8 与 Flash 4B Qwen3.5；头维度、校准器分别匹配。 |
| Mechanism | Default separate encodes each state/images/question independently; isolated uses shared state with a different attention contract. A 255-code readout replaces full-vocabulary generation. Locate uses a separate optional span adapter; mixed Locate/decisions require two passes. | 默认separate逐题独立编码state／images／question；isolated共享状态且attention合同不同。255答码readout不生成完整词表文本。Locate另用可选span adapter；与判断混合需两次pass。 |
| Training | v1.3 saved configs disclose CE for 27B and teacher-distribution distillation for Flash, frozen readouts. Temperatures 1.2263882168038833 / 1.3302962111834522 are v1.3-specific. Complete original training data/replay not verified. Preserve v1.2 training and comparisons in its dated records. | v1.3保存配置披露27B用CE、Flash蒸馏教师分布、readout冻结；温度分别1.2263882168038833／1.3302962111834522，专属v1.3。未验证完整原始训练数据／重放；v1.2训练与对比保留在带日期记录。 |
| Deployment | November 19 HF metadata public/ungated despite residual private-repository wording; tensors not downloaded. Saved image cap 1.6 MP. Locate is text-only with nonempty state and at most 128 questions; either fast=True or locate=False disables Locate. Configured length is not a quality guarantee; overlength rejects or splits question groups retaining state. | Nov19 HF元数据公开且无门控，卡片仍有private措辞；未下载tensor。保存图像上限1.6MP。Locate仅非空文本state、最多128题；fast或locate=False关闭。配置长度不保证质量；超长拒绝或保留state拆问题组。 |
| Suggested use | A self-hosted comparator for text/image judgments after task-specific validation. | 经具体任务验证后，作为文本／图像判读的自部署对照。 |
| Boundary | Version, mode, grouping, images and backend alter the inference contract. v1.2 historical results cannot be relabeled v1.3. Neither near-identical fast-path choices nor a fitted temperature establish new-domain quality, production risk or Mac training. | 版本、mode、分组、图像与后端改变推理合同。不可把v1.2历史结果重命名为v1.3。fast近似答案与拟合温度均不证明新域质量、生产风险控制或Mac训练。 |

**License note:** Official model card declares Apache-2.0; public weights do not imply public training data.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Perplexity pplx-decider-v1-27b model card](https://huggingface.co/perplexity-ai/pplx-decider-v1-27b); [Perplexity local inference wrapper](https://huggingface.co/perplexity-ai/pplx-decider-v1-27b/blob/main/inference.py); [Perplexity released decision configuration](https://huggingface.co/perplexity-ai/pplx-decider-v1-27b/blob/main/decision_config.json); [Perplexity Decider v1.1: native head, attention and deployment card](https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b/blob/14c9d90137962d300f3de95633f7b6535e80c5ce/README.md); [Perplexity Decider v1.1: fixed native code and calibration configuration](https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b/blob/14c9d90137962d300f3de95633f7b6535e80c5ce/source/src/autojev/model.py); [Perplexity Decider v1.2: joint requests and retrained data mixture](https://huggingface.co/perplexity-ai/pplx-decider-v1.2/blob/cce0f3f80033e9d89d80831d5281fd72124aacce/README.md); [Perplexity Decider Flash v1.2: distilled 4B and grouping regressions](https://huggingface.co/perplexity-ai/pplx-decider-flash-v1.2/blob/9ff7cf9838e59df461c276b7699d56b244d2af58/README.md); [Perplexity Decider v1.3 27B: card and saved configuration](https://huggingface.co/perplexity-ai/pplx-decider-v1.3/tree/9c2ebb27470d3dec2ad7ab727727e40d142c7213); [Perplexity Decider Flash v1.3: card and saved configuration](https://huggingface.co/perplexity-ai/pplx-decider-flash-v1.3/tree/d06fb3f2d97e0a52325a0d463c450cf0338f44fe)

<a id="ms-decision"></a>
## Microsoft-Decision-1.1

[Project / model](https://ai.azure.com/catalog/models/Microsoft-Decision-1.1)

GA hosted typed decisions on Gemma4, including images.
Gemma4托管类型化判断，GA且支持图像。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Gemma4 26B-A4B; previous1.0 used a Qwen9B backbone. | Gemma4 26B-A4B；旧1.0使用Qwen9B底座。 |
| Mechanism | Foundry state and named noul/choice/score questions; text/image contract must match the deployed version. | Foundry接收state及命名noul／choice／score；文本／图像合同须匹配部署版本。 |
| Training | Vendor post-training; exact recipe, raw data and customer self-service decision-specific tuning not established. | 厂商后训练；精确配方、原始数据及客户自助判断模型微调未确立。 |
| Deployment | GA1.1 announced Nov17; no public weights verified. Product1.1, deployment name and Foundry model-version1 are different identifiers. | 11月17日宣布1.1 GA，未核公开权重；产品1.1、部署名及Foundry model-version1为不同标识。 |
| Suggested use | Compare classification, routing and rubric judgments. | 比较分类、路由和按标准评分。 |
| Boundary | Vendor comparisons lack audited item-level artifacts; familiar-task calibration need not transfer. Wording and safety errors remain. | 厂商比较缺少已审计的逐项产物；熟悉任务的校准不保证迁移，措辞与安全判断仍可能出错。 |

**License note:** Proprietary hosted service; open Gemma backbone does not make the Microsoft checkpoint open-weight.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Microsoft-Decision-1 launch, 2026-10-09](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/); [Microsoft Foundry decision API and limitations](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision); [Microsoft Decision1.1 GA](https://commandline.microsoft.com/microsoft-decision-model-ga/); [Microsoft Decision current Foundry contract](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision)

<a id="openai-decisions"></a>
## OpenAI Decisions API / GPT-6 Luna

[Project / model](https://developers.openai.com/api/docs/guides/decisions)

GA typed-judgment API for text and images.
面向文本／图像的GA类型化判断API。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Not established by the guide. | 指南未确立参数规模。 |
| Mechanism | POST /v1/decisions has a top-level input (string or ordered items), including messages, user input_json content parts and tool/image context; predicate/choice/score questions return an answers array. GA supports up to400 questions. | POST /v1/decisions顶层input为字符串或有序items，可含messages、user的input_json内容part及工具／图像上下文；predicate／choice／score问题返回answers数组，GA最多400题。 |
| Training | No public weights or Decisions-specific customer tuning entry verified; generic model fine-tuning support is not this product contract. | 未核公开权重或Decisions专属客户调优入口；通用模型微调支持不自动成为本产品合同。 |
| Deployment | GA announced Oct22; current guide supports only gpt-6-luna, with caching and Private Link. Account/region availability not tested here. | 10月22日宣布GA；当前指南仅支持gpt-6-luna，含缓存及Private Link，本次未实测账号／地域可用性。 |
| Suggested use | Managed classification, routing and ordinal scoring. | 托管分类、路由与有序评分。 |
| Boundary | Refusal is a separate answer variant, not calibrated abstention. Confidence needs target-task validation; training and serving identity are undisclosed here. | 拒答为单独返回类型，不等于校准后的拒判；confidence 需在目标任务验证，训练与服务身份尚未披露。 |

**License note:** Proprietary hosted API; no public-weight license established.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [OpenAI Decisions public beta guide](https://developers.openai.com/api/docs/guides/decisions); [OpenAI Decisions GA announcement](https://openai.com/index/decisions-api/); [OpenAI Decisions current contract](https://developers.openai.com/api/docs/guides/decisions)

<a id="gemini-decision-1"></a>
## Google Gemini Decision 1 / Decisions API

[Project / model](https://aistudio.google.com/docs/models/gemini-decision-1)

November11 hosted model for text, image, audio, video and PDF judgments with shared-input isolated questions.
11月11日发布的托管模型，支持文本、图像、音频、视频和PDF判断，在共享输入上隔离各问题。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Parameter count and public weight identity not established by reviewed official material. | 所核官方资料未确立参数量或公开权重身份。 |
| Mechanism | Single-prefill noul/choice/score judgments; confidence equals top-outcome probability (max(p,1-p) for noul), unlike an entropy statistic. Score is the expected zero-based rubric index. Documented question isolation is not statistical independence of errors. | 单次prefill输出noul／choice／score；confidence等于最高选项概率（noul为max(p,1-p)），不是熵统计量。score为从0起的rubric索引期望。文档问题隔离不等于错误统计独立。 |
| Training | Proprietary; no independently audited training mixture, calibration split or contamination analysis obtained. | 专有模型；未取得独立审计的训练混合、校准划分或污染分析。 |
| Deployment | Gemini Developer API v1beta, model gemini-decision-1; up to1000 questions and262144 tokens total. Paid input $0.10/M tokens as reviewed November13; shared input once/request plus question tokens, zero output tokens; no cross-request caching. | Gemini Developer API v1beta，模型gemini-decision-1；最多1000题，总上下文262144 tokens。11月13日核价为输入$0.10/百万tokens；每请求共享输入计一次，题目token另计、输出0 tokens，无跨请求缓存。 |
| Suggested use | Compare multimodal triage, media policy checks and routing at fixed evidence, risk and complete cost. | 在相同证据、风险约束和完整成本下比较多模态分流、媒体规则检查与路由。 |
| Boundary | Calibration, speed and internal deployments are vendor-reported. Confidence is top-outcome probability, not independent reliability evidence. Safety blocks return HTTP400; no cache or Batch API. | 校准、速度及内部部署由厂商报告；confidence为最高选项概率，不是独立可靠性证据。安全拦截返回HTTP400；无缓存或Batch API。 |

**License note:** Proprietary hosted Gemini Developer API; no public model-weight license established.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Gemini Decisions API launch](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/); [Gemini API November11 release notes](https://aistudio.google.com/docs/changelog); [Gemini Decision1 model specification](https://aistudio.google.com/docs/models/gemini-decision-1); [Gemini Decisions API guide](https://aistudio.google.com/docs/decisions-api); [Gemini Decision1 pricing](https://aistudio.google.com/docs/pricing#gemini-decision)

<a id="drex"></a>
## Nace Drex v1.5 / v2.0 / Max v1

[Project / model](https://github.com/nace-ai/drex-decision-models)

Drex family: text pointer-head v1.5/v2.0 and dense 27B multimodal Max v1 with a fixed 255-code readout.
Drex 系列：文本 pointer-head v1.5／v2.0，加上独立 255-code 读出的多模态 dense 27B Max v1。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | v1.5 approximately 9B; v2.0 author describes 35B total/~3B active, 256 experts/8 active. Active size is not resident weight memory; tensors not independently counted. Max v1 is nominal dense27B; a runtime docstring identifies Qwen3.8-27B, while release prose omits the base name. No independent tensor count. | v1.5 约 9B；v2.0 作者称总量 35B／激活约 3B，256 专家中激活 8 个。激活规模不等于驻留权重内存，未独立统计张量。 Max v1 名义 dense27B；运行库 docstring 称 Qwen3.8-27B，发布正文未列基座名，未独立统计张量。 |
| Mechanism | Pointer head scores supplied noul/choice/score options without generation, per question. v2.0 runtime extracts Qwen3_5Moe language_model and drops vision; hybrid questions are independent causal rows. Fork runtimes can share state prefixes. Max differs: last-state biasless255-code head, noncausal full-attention and causal linear layers, a complete independent row per question; no shared state cache. | pointer head 每题对给定 noul／choice／score 候选评分而不生成。v2.0 运行时提取 Qwen3_5Moe language_model 并舍弃视觉，混合骨干的各题为独立因果 row；分支运行库可共享状态前缀。 Max 不同：最后状态经无偏置255-code头，full-attention双向而线性层因果；每题完整独立行，无共享状态缓存。 |
| Training | v1.5 uses benchmark training splits plus procedural data. The November 9 v2 paper describes staged supervision, adjusted feedback, v2.0 specialization and Max vision tuning. Pointer RLAF directly differentiates corrected-target proper losses; Max uses finite-action verified/judge reward with reference KL. These versions have different recipes. Full raw training/calibration data, complete RLAF trainer and identity of every evaluated tensor remain unverified; do not transfer one release recipe or temperature to another. | v1.5使用基准训练划分加程序数据。11月9日论文v2补充阶段监督、修正反馈、v2.0专项及Max视觉训练；pointer RLAF直接求修正目标的proper loss梯度，Max为有限动作verified／judge奖励加参考KL，各版配方不同。原始训练／校准数据、完整RLAF训练器与全部被测张量身份仍未核实，不能移植某一版配方或温度。 |
| Deployment | Python CUDA and Nace llama.cpp/Ollama forks; default state-plus-one-question limit 16384, configurable maximum 131072. v2.0 HF snapshot/card/config plus 16 shard and head LFS identities reviewed; no tensors downloaded or parity tested. Base vision packaging does not establish image input support. Oct23 Q4_K_M Apple path adds Kapitsa v0.2.15 shared-state branches/cache; defaults separately cap state, branch, packed request and sequence at 16384. Hardware-fit/short-ticket medians do not establish quantized decision quality, calibration or 131072-context accuracy. Max CUDA supports images; Mac GGUF/MLX/Kapitsa is text-only. Max default16384/configured262144 is not validated long-context quality. Kapitsa max probability drift0.0329 exceeds its0.02 parity gate despite no flips; long-row/32k reference checks remain unrun. A21-field short Q4 check on48GB is not broad hardware/calibration validation. | Python CUDA 及 Nace llama.cpp／Ollama 分支；状态加一题默认上限 16384、可配置最大 131072。已核 v2.0 HF snapshot／卡／配置、16 分片及 head 的 LFS 标识，未下载张量或测试等价；基座视觉包装不证明支持图像输入。 10 月 23 日 Q4_K_M 苹果路径新增 Kapitsa v0.2.15 共享状态分支／缓存；状态、分支、整包及序列各默认限 16384。硬件可装载／短工单中位延迟不证明量化决策质量、校准或 131072 长度准确率。 Max CUDA 支持图像；Mac GGUF／MLX／Kapitsa 仅文本。Max 默认16384／配置262144不证明长上下文质量。Kapitsa 最大概率漂移0.0329超过0.02等价门槛，虽无答案翻转仍未通过；长行／32k参考核验未跑。48GB上的21字段短Q4检查不等于普遍硬件／校准验收。 |
| Suggested use | Compare local text/JSON decisions and Max CUDA image judgments; match precision, readout, evidence and context before comparing releases. | 比较本地文本／JSON 与 Max CUDA 图像判断；跨版本比较须匹配精度、读出、证据和上下文。 |
| Boundary | v1.5 uses benchmark training splits; its results are not unseen-domain zero-shot. Public Index 0.3.1 leaders fall inside its tie band. Small runner checks do not establish broad parity. v2.0 JevBench author counts trail Jev 1.13.0 by two items (E32); this is not a significance result or a universal win. Current snapshot is not proven identical to evaluated weights. Max public-only Index results are not private text Full0.4; retain the failed native probability-parity gate, not just stable categorical picks. Max RLAF stage gains (E45) lack equal-extra-compute continued-SFT and training-seed controls; they do not erase the earlier serving-parity limits. | v1.5 使用基准训练划分，其结果不能视为未知领域零样本；公开 Index 0.3.1 前列处于平局带内，小规模运行器核对不证明普遍等价。 v2.0 作者 JevBench 计数比 Jev 1.13.0 少两题（E32），不作显著性或普遍胜出结论；当前 snapshot 与实测权重未建立同一性。 Max 仅公共 Index 结果不能当作私有文本 Full0.4；须保留原生路径概率等价未通过，不能只看选项未翻转。 Max RLAF阶段正结果（E45）缺等新增算力的继续SFT与训练种子控制，也不能抹去旧服务路径的概率等价限制。 |

**License note:** Code Apache-2.0; weights use modified Nace.AI Open RAIL-M with commercial thresholds, competitor exclusions and use restrictions. Public access does not imply unrestricted open source.
**Recorded weight identifier:** v2.0 HF nace-ai/drex-v2.0@3e6d164cb5c8cf264eec167905cc2448d89ea97d (published LFS identities; tensor bytes not locally verified; v1.5 remains unpinned); Max HF repository a67fa2808b5d91a4db62629beb14eba6d3f3e53c (metadata only; evaluated tensor equality unverified)

**Sources:** [Drex v1.5 release and public evaluation](https://github.com/nace-ai/drex-decision-models/blob/5c3d2220713c732a6820c4cdda51c7c38db991f5/models/drex-v1.5/README.md); [Drex local context limits](https://github.com/nace-ai/drex-decision-models/blob/5c3d2220713c732a6820c4cdda51c7c38db991f5/docs/context-length.md); [Drex v1.5 modified Open RAIL-M license](https://github.com/nace-ai/drex-decision-models/blob/5c3d2220713c732a6820c4cdda51c7c38db991f5/models/drex-v1.5/LICENSE); [Nace Drex training-overlap disclosure](https://www.nace.ai/drex); [Drex v2.0 fixed release card and public evaluation scope](https://github.com/nace-ai/drex-decision-models/blob/be8ba7c8157241b9393862e9fcec104d0dc5caff/models/drex-v2.0/README.md); [Drex v2.0 pinned HF model card/config and published LFS identities](https://huggingface.co/nace-ai/drex-v2.0/tree/3e6d164cb5c8cf264eec167905cc2448d89ea97d); [Drex fixed runtime: language-only MoE loading and independent question rows](https://github.com/nace-ai/drex-decision-models/blob/be8ba7c8157241b9393862e9fcec104d0dc5caff/kev/model.py); [Drex v2.0 Nace.AI Open RAIL-M weight license](https://huggingface.co/nace-ai/drex-v2.0/blob/3e6d164cb5c8cf264eec167905cc2448d89ea97d/LICENSE); [Drex v2.0: Q4_K_M Apple deployment and corrected engine limits](https://github.com/nace-ai/drex-decision-models/blob/f2afd75f714997fe8a950888252b833f2c5198f9/models/drex-v2.0/apple-silicon.md); [Kapitsa v0.2.15: shared recurrent state, branch readout and limits](https://github.com/nace-ai/kapitsa/blob/5c489cc69b397d2088aa165f9017129b4a724b7a/docs/systemone.md); [Drex Max v1: dense 27B release, independent code-readout rows and evaluation scope](https://github.com/nace-ai/drex-decision-models/blob/e206b278e3988ad1b58e6f1556b559a65947a4e6/models/drex-max-v1/README.md); [Drex Max HF snapshot: repository identity, not verified tensor hash](https://huggingface.co/nace-ai/drex-max-v1/tree/a67fa2808b5d91a4db62629beb14eba6d3f3e53c); [Kapitsa Drex Max: failed probability-parity gate and unrun long-row checks](https://github.com/nace-ai/kapitsa/blob/dd1a80963dd36023a9889e26214030c2a98214c2/docs/drex-max.md); [Drex Max affine Q4: separate 21-field short-context Mac check](https://huggingface.co/nace-ai/drex-max-v1-affine-q4/blob/e7d0c597706239a015608c06dfe0951197e95096/README.md); [Drex v2 paper: RLAF objectives and stage ablations](https://arxiv.org/html/2611.07854v2)

<a id="decision3"></a>
## vLLM-SR D3 / Turbo / Ultra / D3.1-nano

[Project / model](https://huggingface.co/collections/vllm-sr/decision-30)

Multimodal typed-decision family with distinct classic per-question, Turbo/Ultra shared-state and November 12 D3.1-nano releases.
多模态类型化判断系列，经典逐题、Turbo／Ultra共享state及11月12日D3.1-nano发布物须分别识别。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Classic card counts range from 0.59B edge to 26.09B d3 including vision. Ultra is 26.09B including 0.46B vision; D3.1-nano is 2.21B including 0.33B vision, based on Qwen3.5-2B. Nominal size and serving memory differ. | 经典卡片参数量含视觉，从edge 0.59B到d3 26.09B。Ultra为26.09B（视觉0.46B）；D3.1-nano基于Qwen3.5-2B，共2.21B（视觉0.33B）。名义规模不同于服务内存。 |
| Mechanism | Classic D3 and D3.1-nano use an independent forward pass per question despite one HTTP call; candidate-code readouts normalize allowed options. Turbo/Ultra reuse state for question branches. Full-attention layers and causal DeltaNet behavior require the release runtime. Confidence fields/backend semantics are not interchangeable correctness probabilities; Ultra adds Box/Track, which require their own presence and localization checks. | 经典D3及D3.1-nano即使一次HTTP调用也逐题独立前向，以答码读出归一化允许选项；Turbo／Ultra为问题分支复用state。Full-attention与因果DeltaNet行为须匹配发布运行库。不同后端confidence不能当作同一正确概率；Ultra另有Box／Track，须分别验目标存在及定位。 |
| Training | Original full training mixture/recipe and overlap/calibration audits remain unestablished. Prior classic/Turbo wrapper audits found inference-only restrictions; those are not proof about every external trainer. The separate Vis Decisions path provides text-only full/LoRA adaptation and strips vision, not original or multimodal D3 training reproduction. This refresh establishes new release identities, not an audited Ultra/D3.1-nano enterprise fine-tuning workflow. | 原始完整训练混合、配方及重叠／校准审计仍未确立。既有经典／Turbo封装审查发现仅推理限制，但这不能否定所有外部训练器。独立Vis Decisions提供去视觉的文本full／LoRA适配，不是原始或多模态D3训练复现。本轮确认新发布身份，未建立已审计的Ultra／D3.1-nano企业续训链。 |
| Deployment | Ultra was released October 26; November 17 cache/card edits are runtime/metadata. D3.1-nano weights were uploaded November 12; later manifest/card edits are not retraining. Existing six native models and Turbo binary identities match the compared pins; a separate CoreML repo added edge conversion/MLX binaries on October 14. Custom Transformers/Router/native-vLLM support differs by release and build; historical integration limits are not current universal guarantees. No weights downloaded or M5 training verified. | Ultra于10月26日发布，11月17日cache／card改动属运行库及元数据；D3.1-nano权重11月12日上传，后续manifest／card不是重训。既有六个native模型及Turbo与对比pin的binary身份相同；另一个CoreML仓10月14日新增edge转换／MLX binary。定制Transformers／Router／原生vLLM能力依发布物和build不同，历史集成限制不是当前通用保证；未下载权重或验证M5训练。 |
| Suggested use | Matched text/image/video decision comparisons, with small D3.1-nano as a separate capability candidate and Ultra as a larger reference; verify adaptation separately. | 固定文本／图像／视频判断合同对比；将小型D3.1-nano作为独立能力候选、Ultra作为大模型参照，适配可行性另验。 |
| Boundary | Keep official private Full, public-suite and author SR-Text/SR-Box results separate. D3.1-nano reported public score uses two choice orders averaged; ordinary runtime reads one order, and its image/video quality is unevaluated. CoreML/quantized ports and security/cache fixes are not new native training. API aliases do not freeze model identity; historical E12–E16/E21–E23 protocols remain unchanged. | 官方private Full、public suite及作者SR-Text／SR-Box结果分别记录。D3.1-nano报告的公共分数平均两种choice顺序，普通运行库只读一种；该版本图像／视频质量未评测。CoreML／量化端口及安全／cache修复不等于新的native训练；API别名不固定模型身份，E12–E16／E21–E23历史协议不变。 |

**License note:** Reviewed classic/Turbo and new Ultra/D3.1-nano cards declare Apache-2.0; check exact base/runtime notices. Binary metadata comparison is not local tensor-byte verification or full training-data availability.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Decision 3.0 d3 v3.1.0 model card](https://huggingface.co/vllm-sr/d3/blob/093cffbaa7be6f5dfe14252ae7e80c396c06dbd9/README.md); [d3 package manifest](https://huggingface.co/vllm-sr/d3/blob/093cffbaa7be6f5dfe14252ae7e80c396c06dbd9/MODEL_MANIFEST.json); [Decision 3.0 d3-flash v3.1.0 model card](https://huggingface.co/vllm-sr/d3-flash/blob/f6075bff3c0f7d5704e353d0fb2ebf94888d1691/README.md); [d3-flash package manifest](https://huggingface.co/vllm-sr/d3-flash/blob/f6075bff3c0f7d5704e353d0fb2ebf94888d1691/MODEL_MANIFEST.json); [Decision 3.0 d3-mini v3.1.0 model card](https://huggingface.co/vllm-sr/d3-mini/blob/0e78bbdbe3cf480ed1461c185c9e0c4fa9258011/README.md); [d3-mini package manifest](https://huggingface.co/vllm-sr/d3-mini/blob/0e78bbdbe3cf480ed1461c185c9e0c4fa9258011/MODEL_MANIFEST.json); [Decision 3.0 d3-nano v3.1.0 model card](https://huggingface.co/vllm-sr/d3-nano/blob/9d9b937f5f117f78c030ea7ba677c0b3d328ec58/README.md); [d3-nano package manifest](https://huggingface.co/vllm-sr/d3-nano/blob/9d9b937f5f117f78c030ea7ba677c0b3d328ec58/MODEL_MANIFEST.json); [Decision 3.0 d3-lite v3.1.0 model card](https://huggingface.co/vllm-sr/d3-lite/blob/3c49f5c0bd48a4b28e29b8ec1f38f56e199f3d61/README.md); [d3-lite package manifest](https://huggingface.co/vllm-sr/d3-lite/blob/3c49f5c0bd48a4b28e29b8ec1f38f56e199f3d61/MODEL_MANIFEST.json); [Decision 3.0 d3-edge v3.1.0 model card](https://huggingface.co/vllm-sr/d3-edge/blob/20c745653400d191ecacd99c4eafc0c5900dc15e/README.md); [d3-edge package manifest](https://huggingface.co/vllm-sr/d3-edge/blob/20c745653400d191ecacd99c4eafc0c5900dc15e/MODEL_MANIFEST.json); [d3 backbone/runtime architecture configuration](https://huggingface.co/vllm-sr/d3/blob/093cffbaa7be6f5dfe14252ae7e80c396c06dbd9/config.json); [Decision 3.0 Transformers loader](https://huggingface.co/vllm-sr/d3/blob/093cffbaa7be6f5dfe14252ae7e80c396c06dbd9/modeling_d3.py); [Decision 3.0 code readout and multimodal runtime](https://huggingface.co/vllm-sr/d3/blob/093cffbaa7be6f5dfe14252ae7e80c396c06dbd9/d3_runtime.py); [Decision 3.0 on Apple Silicon](https://vllm-sr.ai/blog/decision-3-0-on-apple-silicon/); [Decision 3.0 Core ML conversion packages](https://huggingface.co/FluidInference/d3-coreml/blob/62b6a996e15342bdd3d608030d8f445f11a52367/README.md); [FluidUse native Swift/Core ML runtime](https://github.com/FluidInference/FluidUse/blob/d278e17df85e39e8c21bb64a467da81c39576fcd/README.md); [d3 October 15 card and identity review](https://huggingface.co/vllm-sr/d3/blob/225be8b1e2270becab69c5fe05b26f99cbbdd66b/README.md); [d3-flash October 15 card and identity review](https://huggingface.co/vllm-sr/d3-flash/blob/8b35c853b90e777595ec36bacae820fe08ea077a/README.md); [d3-mini October 15 card and identity review](https://huggingface.co/vllm-sr/d3-mini/blob/97dd054df4b3e0b3beb6af23ab8c82b7c0052e0e/README.md); [d3-nano October 15 card and identity review](https://huggingface.co/vllm-sr/d3-nano/blob/aeb70d4dd53ed25b855c3b0a66394b8fe265db7f/README.md); [d3-lite October 15 card and identity review](https://huggingface.co/vllm-sr/d3-lite/blob/9c10703193afc7c7d28c88201c0364bfbbf58320/README.md); [d3-edge October 15 card and identity review](https://huggingface.co/vllm-sr/d3-edge/blob/cab71e6ad3461b8086d51ddb572c656babd63b0b/README.md); [d3 package-verification scope update](https://huggingface.co/vllm-sr/d3/blob/225be8b1e2270becab69c5fe05b26f99cbbdd66b/d3_runtime.py); [Native vLLM Decision 3.0 integration and author tests](https://github.com/vllm-project/vllm/pull/61565); [vLLM structured decisions at the D3 merge](https://github.com/vllm-project/vllm/blob/89cab550862e4b7f08d70c19682121362d7dd0c5/docs/models/structured_decisions_models.md); [vLLM D3 classification model implementation](https://github.com/vllm-project/vllm/blob/89cab550862e4b7f08d70c19682121362d7dd0c5/vllm/model_executor/models/d3.py); [Decision Index 0.3.2 text aggregate snapshot](https://multimodalart-jev-decision-index.static.hf.space/data/v03.json); [Decision Index 0.3.2 vision aggregate snapshot](https://multimodalart-jev-decision-index.static.hf.space/data/vision.json); [Decision Index 0.3.2 scoring-change description](https://multimodalart-jev-decision-index.static.hf.space/index.html); [Decision 3.0: inference-only wrapper training boundary](https://huggingface.co/vllm-sr/d3/blob/225be8b1e2270becab69c5fe05b26f99cbbdd66b/modeling_d3.py); [Vis: third-party D3 Edge/Lite text training scope](https://github.com/Blockether/vis/blob/7589e04daa7af13ccd0c5b3c03a5e402c7f4abfb/resources/vis-docs/decision-models.md#choose-and-train-d3); [Vis Decisions: text D3 full/LoRA gradients and candidate loss](https://github.com/Blockether/vis-decisions/blob/d73768e3c18d89d11f6b9a774b87d64ccd55f27d/src/blockether/vis_decisions/_d3_trainer.py); [Vis Decisions: text-only D3 reconstruction and merged FP32/ONNX export](https://github.com/Blockether/vis-decisions/blob/d73768e3c18d89d11f6b9a774b87d64ccd55f27d/src/blockether/vis_decisions/_d3.py); [D3-Turbo card: state reuse, localization and API alias](https://huggingface.co/vllm-sr/d3-turbo/blob/a0f3e9e59ebd1202fe1d4de1c4c0f9a986758cbb/README.md); [D3-Turbo prefix_bidir StateOnce implementation](https://huggingface.co/vllm-sr/d3-turbo/blob/a0f3e9e59ebd1202fe1d4de1c4c0f9a986758cbb/d3_runtime.py); [D3-Turbo wrapper still refuses training and generic saving](https://huggingface.co/vllm-sr/d3-turbo/blob/a0f3e9e59ebd1202fe1d4de1c4c0f9a986758cbb/modeling_d3.py); [D3-Turbo fixed decision configuration](https://huggingface.co/vllm-sr/d3-turbo/blob/a0f3e9e59ebd1202fe1d4de1c4c0f9a986758cbb/decision_config.json); [D3-Turbo external evaluator runtime note](https://huggingface.co/vllm-sr/d3-turbo/blob/a0f3e9e59ebd1202fe1d4de1c4c0f9a986758cbb/.eval_results/vllm-sr__d3-turbo.yaml); [vLLM: enforce request-template trust before structured-decision admission](https://github.com/vllm-project/vllm/commit/51be9ea6a3a356b42e3b72a0fc6e8cb8c8975944); [D3-Ultra: October26 release, current fixed card](https://huggingface.co/vllm-sr/d3-ultra/blob/3ac9ff15579ca9193a0d44f4fa9056f2ea62731d/README.md); [D3.1-nano: November12 2B release and public-suite protocol](https://huggingface.co/vllm-sr/d3.1-nano/blob/71d06677f56e243042fe5d5f983804648a5689e8/README.md); [D3 CoreML: October14 edge conversion artifacts](https://huggingface.co/FluidInference/d3-coreml/tree/78a1f66580199e5eca3c5ff60a265b0f691b38fd)

<a id="intern-decision"></a>
## Intern-Decision

[Project / model](https://github.com/internlm/Intern-Decision)

Qwen3.5 multimodal 0.8B/2B/4B family; multiple typed fields scored from one causal masked assistant skeleton.
Qwen3.5 多模态 0.8B／2B／4B 系列，在一个因果 masked assistant skeleton 中评分多个类型化字段。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | 0.8B, 2B and 4B nominal Qwen3.5 sizes; independently inspected cards, no local tensor count. | 0.8B、2B、4B 为 Qwen3.5 名义规模；分别核对模型卡，未本地统计张量。 |
| Mechanism | Reads candidate-token logits immediately before each `<decision>` placeholder in one causal pass; up to 16 fields / 62 options, no free-text generation. Fields share the schema sequence, so order/context invariance needs testing. Confidence=max(P), unlike Jev distribution summaries. | 一次因果前向，从每个 `<decision>` 前一位置读取候选 token logits；最多 16 字段／62 选项，不生成自由文本。字段共享 schema 序列，须验证顺序／上下文不变性；confidence=max(P)，不同于 Jev 的分布统计量。 |
| Training | Decision-tuned language backbone; frozen vision tower/projector. Cards report NLL temperature fitting on 1728 calibration and 1693 separate validation cases: 0.8B T=2.747760550703, 2B T=2.100509348278, 4B T=1.99241824. Private original records and full data construction remain unavailable. Inspected XTuner configuration trains full language parameters with masked full-vocabulary answer-token CE, not LoRA; gold symbols remain labels, while the input retains placeholders. Paper v1 reports 17880 training samples / 23500 decisions, including 5500 image-bearing samples, for full language-backbone tuning with vision/projector frozen. This is not LoRA effectiveness evidence or verification that the full raw training data are public. Oct26 deeper audit confirms Sep26 code, not a new release: MEDIA_ROOT selects visual tokenization; actual UniversalDataset passes pixels/grid through the collator to frozen visual-feature injection. Missing image grids reject. Final HF saving/tensor-audit tools exist, but were not run. | 微调语言骨干，冻结视觉 tower／projector。卡片称用 1728 校准及 1693 独立验证样本按 NLL 拟合温度：0.8B 为 2.747760550703、2B 为 2.100509348278、4B 为 1.99241824；原始私有记录及完整数据构建未公开。已审阅 XTuner 配置以 masked 完整词表 answer-token CE 训练语言全参数，并非 LoRA；金标答码只在 labels，输入保持占位符。 论文 v1 称有 17880 条训练样本／23500 个决策，其中 5500 条带图；训练语言骨干、冻结视觉塔／projector。它不是 LoRA 效果证据，也不代表已核实完整原始训练数据公开。 10 月 26 日深化核验的是 9 月 26 日源码而非新发布：MEDIA_ROOT 选择视觉分词，实际 UniversalDataset 经 collator 把 pixels／grid 送入冻结视觉特征注入；缺 grid 拒绝。存在最终 HF 保存／张量审计工具，本次未执行。 |
| Deployment | Public HF weights, own inference.py and repository HF/XTuner paths. HF card default 8192 tokens rejects overlength, up to 8 images. Core ML 0.8B port in FluidUse is text-only and uses smaller fixed buckets; it does not inherit HF image/context support. | 公开 HF 权重、专属 inference.py 及仓库 HF／XTuner 路径。HF 卡默认 8192 token、超长拒绝，最多 8 图；FluidUse 的 Core ML 0.8B 仅文本、较小固定 bucket，不能继承 HF 的图像／上下文支持。 |
| Suggested use | Compare multi-field cost and field/order sensitivity against per-question models; test image-grounded judgments. | 与每题独立模型比较多字段成本和字段／顺序敏感性，测试基于图像证据的判断。 |
| Boundary | Private training/calibration records are absent. A 96-case distribution pilot is diagnostic; size/backend-specific temperature and max(P) confidence are not portable business risk guarantees. Paper seven-suite accuracy concerns text tasks; visual trajectories are qualitative. Public Jevbench informed development; matched-data ablations and a matched D3 multimodal comparison are absent from the reviewed evidence. | 原始训练／校准记录私有；96-case 分布试验只作诊断。型号／后端专属温度与 max(P) confidence 不能直接保证业务风险。 论文七套准确率针对文本任务，视觉轨迹为定性演示；公开 Jevbench 参与开发，已阅证据缺同数据消融及同条件 D3 多模态对照。 |

**License note:** Three inspected cards declare Apache-2.0 and retained Qwen notices. Check evaluation dataset licenses separately; original training/private calibration records are not released. Root repository Apache-2.0 LICENSE was already present at the September 29 commit; the November 20 check is a correction of contrary claims, not a new license grant.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Intern-Decision architecture and release scope](https://github.com/internlm/Intern-Decision/blob/3572c8a68b5df5dafe02d0e093989ba8ec0183bc/README.md); [Intern-Decision evaluation protocol](https://github.com/internlm/Intern-Decision/blob/3572c8a68b5df5dafe02d0e093989ba8ec0183bc/docs/EVALUATION.md); [Intern-Decision known-distribution calibration pilot](https://github.com/internlm/Intern-Decision/blob/3572c8a68b5df5dafe02d0e093989ba8ec0183bc/docs/CALIBRATION_BENCHMARK.md); [Intern-Decision-0.8B model card](https://huggingface.co/internlm/Intern-Decision-0.8B/blob/85a0cc5a99d67ea8d56dfe98115689212867171d/README.md); [Intern-Decision-2B model card](https://huggingface.co/internlm/Intern-Decision-2B/blob/8797836c65fc91a2435b1fb6850b5f0aabd75cc3/README.md); [Intern-Decision-4B model card](https://huggingface.co/internlm/Intern-Decision-4B/blob/0e5e6aa7d6d750e2b1504ba11a8136cb58aeb3cd/README.md); [Intern-Decision 4B masked-next-token inference](https://huggingface.co/internlm/Intern-Decision-4B/blob/0e5e6aa7d6d750e2b1504ba11a8136cb58aeb3cd/inference.py); [FluidUse native Swift/Core ML runtime](https://github.com/FluidInference/FluidUse/blob/d278e17df85e39e8c21bb64a467da81c39576fcd/README.md); [Intern-Decision: multimodal full-language training configuration](https://github.com/InternLM/Intern-Decision/blob/3572c8a68b5df5dafe02d0e093989ba8ec0183bc/configs/training/qwen35.py); [Intern-Decision: masked labels and causal placeholder input compilation](https://github.com/InternLM/Intern-Decision/blob/3572c8a68b5df5dafe02d0e093989ba8ec0183bc/src/inputs/schema.py); [Intern-Decision paper v1: image-bearing training versus text-suite evidence](https://arxiv.org/html/2610.22131v1); [Intern-Decision original public training-code release](https://github.com/InternLM/Intern-Decision/commit/63292c8b5e0f5d410a7159e0f1c14475b828839a); [Intern-Decision hard-label and local-image training contract](https://github.com/InternLM/Intern-Decision/blob/565350244af860e1c276768cd80bdd9b8be93913/docs/DATA.md); [Intern-Decision actual UniversalDataset construction](https://github.com/InternLM/Intern-Decision/blob/565350244af860e1c276768cd80bdd9b8be93913/src/inputs/dataset.py); [Intern-Decision visual tokenization, labels and collator](https://github.com/InternLM/Intern-Decision/blob/565350244af860e1c276768cd80bdd9b8be93913/src/inputs/masked.py); [Intern-Decision frozen visual-feature injection](https://github.com/InternLM/Intern-Decision/blob/565350244af860e1c276768cd80bdd9b8be93913/src/model/qwen.py); [Intern-Decision checkpoint verification boundaries](https://github.com/InternLM/Intern-Decision/blob/565350244af860e1c276768cd80bdd9b8be93913/scripts/verify_checkpoint.py); [Intern-Decision root Apache license, already present September 29](https://github.com/InternLM/Intern-Decision/blob/3572c8a68b5df5dafe02d0e093989ba8ec0183bc/LICENSE)

<a id="verdict"></a>
## Verdict / OpenJev

[Project / model](https://github.com/Heman10x-NGU/Verdict-open-jev)

151M ModernBERT/GLiClass candidate classifier with an explicit insufficient-evidence option and per-K calibration.
151M ModernBERT／GLiClass 候选分类器，含显式证据不足选项及 per-K 校准。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | 151378177 parameters reported; up to 25 logits = 24 substantive candidates plus abstention. | 报告 151378177 参数；最多 25 logits，即 24 个实质候选加拒答项。 |
| Mechanism | Encoder scores candidates including __insufficient_evidence__, without text generation. Engine renders hypothesis-style descriptions and applies candidate-count temperatures; choosing abstention is a trained candidate decision, not a risk bound. | 编码器评分包括 __insufficient_evidence__ 的候选，不生成文本。Engine 使用 hypothesis-style 描述及候选数对应温度；拒答是学习到的候选判断，并非风险上界。 |
| Training | Author describes CE+Brier post-training with temperature scaling. Shipped per-K/global calibration differs from the single T fitted by the held-out evaluator; original full training provenance and all open-domain fitting splits not independently audited. | 作者称使用 CE+Brier 后训练与温度校准；发布的 per-K／全局校准不同于保留集评测拟合的单温度。完整原始训练来源及所有开放域拟合划分未独立审计。 |
| Deployment | Public HF weights/ONNX and Python/WebGPU/WASM paths; 512-token serving budget. Separate Core ML FP16 L128/L512 conversion with full rendered-request limits; LUT8 package failed conversion acceptance and is not validated. | 公开 HF 权重／ONNX 及 Python／WebGPU／WASM 路径，服务预算 512 token。独立 Core ML FP16 L128／L512 转换须遵守完整请求长度；LUT8 未通过转换验收，不属于已验证包。 |
| Suggested use | Compact intent classification and missing-option tests; compare native serving probabilities with the exact evaluation renderer/calibrator. | 轻量意图分类与缺少正确选项测试；核对实际服务概率和评测 renderer／校准器。 |
| Boundary | Author tests show abstention collapsing under hard negatives and synonym wording. Converter reports shipped serving calibration differs substantially from the held-out evaluation; no domain-independent abstention guarantee. | 作者测试显示 hard negative 和同义改写下拒答崩塌；转换者报告实际服务校准与保留集评测明显不同，不能保证跨域拒答可靠性。 |

**License note:** Pinned model card and repository declare Apache-2.0; base and dataset terms remain separate. An OpenJev name denotes this independent project, not an official TypeSafe release.
**Recorded weight identifier:** HF repository 8af2496eb63c7fa66d7d234e1f62629380030eb4 (source pin; tensor bytes not locally verified)

**Sources:** [Verdict / OpenJev mechanism and negative findings](https://github.com/Heman10x-NGU/Verdict-open-jev/blob/30f15564821626ca5c1ad5b2638c4eb7078787dd/README.md); [Verdict 151M release model card](https://huggingface.co/heman10x/rlcd-modernbert-151m/blob/8af2496eb63c7fa66d7d234e1f62629380030eb4/README.md); [Verdict typed serving renderer and calibration path](https://github.com/Heman10x-NGU/Verdict-open-jev/blob/30f15564821626ca5c1ad5b2638c4eb7078787dd/core/engine_encoder.py); [Verdict shipped per-K calibration artifact](https://huggingface.co/heman10x/rlcd-modernbert-151m/blob/8af2496eb63c7fa66d7d234e1f62629380030eb4/calibrator.json); [Verdict raw abstention-generalization report](https://github.com/Heman10x-NGU/Verdict-open-jev/blob/30f15564821626ca5c1ad5b2638c4eb7078787dd/reports/v2/exp_e5_abstention_generalization.json); [Verdict Core ML conversion and rejected quantization](https://huggingface.co/FluidInference/verdict-coreml/blob/835208c443699f1f95c4bed1b177dc916300cffe/README.md); [FluidUse official-harness and application-path reports](https://github.com/FluidInference/FluidUse/blob/d278e17df85e39e8c21bb64a467da81c39576fcd/Documentation/OfficialBenchmarks.md)

<a id="startlux-decision"></a>
## StartLux-Decision v1.1 (Instant / AutoThink)

[Project / model](https://github.com/StartLuxLabs/StartLux-Decision)

Option-letter LM readout: Instant uses prompt-bidirectional full-attention; causal AutoThink conditionally reasons and fuses two distributions.
使用 LM 选项字母读出：Instant 的 full-attention 提示双向，因果 AutoThink 按需推理并混合两次分布。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Five Instant nominal sizes: 0.8B/2B/4B/9B/27B; AutoThink: 4B/9B/27B. Cards separately pinned; no independent tensor count. | Instant 五个名义规模：0.8B／2B／4B／9B／27B；AutoThink 为 4B／9B／27B。各卡固定版本，未独立统计张量。 |
| Mechanism | No new classifier head: selected existing LM A–Z rows, up to 26 candidates/readout; longer lists use group/final tournaments. Each question is a separate row. Instant changes full-attention only; linear-attention layers stay causal. AutoThink keeps causal attention, gates on max(P), and normally fuses 25% initial + 75% post-thought. API confidence is a different statistic. | 不新增分类头：选已有 LM 的 A–Z 行，每次最多 26 候选，长列表分组／决赛归约；每题独立 row。Instant 仅改 full-attention，linear-attention 保持因果；AutoThink 全因果，以 max(P) 开门，通常初判 25%＋后判 75%；API confidence 是不同统计量。 |
| Training | Paper: full-language SFT; merged adapters/data/attention specialization and Instant seed-weight averaging; causal reasoning supervision then RLCD². Vision frozen. RLCD² uses a frozen starting scorer, proper-score difference and soft length penalty with group-relative policy gradients. Public inference plus archived v1 text LoRA does not establish the complete v1.1 training/data package. V2 specifies about 2.7M stage-1 examples for 0.8–9B but 0.8M for 27B; its policy-aware calibration is not a universal per-type temperature guarantee. | 论文：语言全参数 SFT；adapter／数据／注意力适配后合并，Instant 多种子权重平均；因果推理监督后接 RLCD²，视觉冻结。RLCD² 由冻结起始评分器计算 proper-score 差值及软长度惩罚，以 group-relative policy gradients 优化推理；公开推理加归档 v1 文本 LoRA 不等于完整 v1.1 训练／数据包。 v2的Stage1约270万只适用于0.8–9B，27B约80万；其策略感知校准也不是单一按题型温度的普遍保证。 |
| Deployment | Inspected vLLM/llama.cpp/MLX/Transformers paths, not executed. Accuracy release vLLM 0.19.1 is text-only; launcher 0.31 enables up to 8 images, video=0. Default Instant context cap 131072; causal configuration 262144, not verified full-context quality. AutoThink default gate 0.6/budget 4096, loop handling and 4000-character tail; full latency includes reasoning and reread. Oct17 fixes normalize list-form criteria/options before tournament routing (including a 26-choice none slot); optional vLLM extra now pins 0.31.0. Eight card revisions are unchanged; no new measured gain. Prism now also serves v1.1 Instant 4B/9B/27B (Q8_0/W4A8), with a complete prompt per question and no shared evidence/prefix cache; thoughts are rejected for Instant. AutoThink uses a separate causal shared-state path; allow_none defaults on. Oct27 fixes MXFP4 double-added residuals that made answers batch-dependent. Internal batch invariance, BF16 parity and probability calibration are separate checks; quantization calibration proves none of the latter. | 已阅 vLLM／llama.cpp／MLX／Transformers 路径，未运行。成绩发布用 vLLM 0.19.1 仅文本；launcher 0.31 最多八图、video=0。默认 Instant 上限 131072，因果配置 262144，不等于全长度质量验证。AutoThink 默认门槛 0.6／预算 4096，含循环处理及末 4000 字符后读；总延迟须含推理与再读出。 10 月 17 日修复将列表式 criteria／options 先规范化再做分组归约，含 26 选项另加 none 的情况；可选 vLLM 依赖现固定 0.31.0。八卡 revision 未变，无新增实测增益。 Prism 现也支持 v1.1 Instant 4B／9B／27B（Q8_0／W4A8）：每题完整 prompt，不共享证据／前缀缓存，拒绝生成 thoughts。AutoThink 另走因果共享状态路径，allow_none 默认开启。10 月27日修复 MXFP4 重复残差导致答案随批次变化的问题；内部批次不变性、BF16 等价、概率校准须分别核验，量化校准不证明后两者。 |
| Suggested use | Compare one-pass versus selective computation on evidence-complete decisions, at matched risk and complete cost; commercial use requires separate weight authorization. | 在证据充分的判断上以相同风险与总成本比较一次读出和选择性计算；商业使用权重需另获授权。 |
| Boundary | Public DI is development-selected, not the full/private board. DecisionPivot is author-built/evaluated. Gate 0.9 paper results do not describe current 0.6 defaults; confidence/none signals need policy-specific validation. November 20 targeted review: the October 16 DI lead is historical; DI 0.4.1 changes tasks/weights and no longer places this release first. Neither an aggregate rank nor commercial authorization establishes domain post-training superiority. | 公共 DI 参与开发选择，并非完整／私有榜；DecisionPivot 为作者自建自测。论文 0.9 门槛成绩不代表当前 0.6 默认；confidence／none 须按实际策略验证。 11月20日定向复核：10月16日DI榜首为历史结果，DI0.4.1改变任务／权重后已非第一；汇总排名或取得商业授权都不证明领域后训练最优。 |

**License note:** Inference code Apache-2.0; all eight inspected v1.1 cards declare CC BY-NC 4.0 weights. Commercial use requires a separate license. Training/reference dataset and backbone terms remain separate; no unrestricted open-source model claim. Prism own code has no selected license at reviewed revision; do not extend the Apache license of vendored files to it.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [StartLux-Decision: AutoThink and RLCD² technical report v1](https://arxiv.org/html/2610.17309v1); [StartLux v1.1: family and inference-package release](https://github.com/StartLuxLabs/StartLux-Decision/blob/cb1d11f1ac9e9b43b95ef3a6468fa29b607c40fd/README.md); [StartLux API: gates, confidence and none_probability](https://github.com/StartLuxLabs/StartLux-Decision/blob/cb1d11f1ac9e9b43b95ef3a6468fa29b607c40fd/docs/api.md); [StartLux inference: separate question rows and adaptive readout](https://github.com/StartLuxLabs/StartLux-Decision/blob/cb1d11f1ac9e9b43b95ef3a6468fa29b607c40fd/startlux_decide/pipeline.py); [StartLux serving: backend, context and media boundaries](https://github.com/StartLuxLabs/StartLux-Decision/blob/cb1d11f1ac9e9b43b95ef3a6468fa29b607c40fd/docs/engines.md); [StartLux archived v1: text LoRA example is not v1.1 RLCD² training](https://github.com/StartLuxLabs/StartLux-Decision/blob/cb1d11f1ac9e9b43b95ef3a6468fa29b607c40fd/v1/finetune/finetune_lora.py); [startlux-models/StartLux-Decision-v1.1-27B-AutoThink model card](https://huggingface.co/startlux-models/StartLux-Decision-v1.1-27B-AutoThink/blob/dd62d5cd84a483d75bdd548880bbf08bdd3f67a4/README.md); [startlux-models/StartLux-Decision-v1.1-0.8B-Instant model card](https://huggingface.co/startlux-models/StartLux-Decision-v1.1-0.8B-Instant/blob/6496ae641cc71b149ce9dad69bd97f2a44e7bf11/README.md); [startlux-models/StartLux-Decision-v1.1-2B-Instant model card](https://huggingface.co/startlux-models/StartLux-Decision-v1.1-2B-Instant/blob/f1e6cd147dda82c9ffa3e8e725d5c1f175566fb1/README.md); [startlux-models/StartLux-Decision-v1.1-4B-Instant model card](https://huggingface.co/startlux-models/StartLux-Decision-v1.1-4B-Instant/blob/416088f77cfce09633906a3675c7cd2e5dabcf10/README.md); [startlux-models/StartLux-Decision-v1.1-9B-Instant model card](https://huggingface.co/startlux-models/StartLux-Decision-v1.1-9B-Instant/blob/18a17f734966b213b2f00fa9c915e8b9af2a9b20/README.md); [startlux-models/StartLux-Decision-v1.1-27B-Instant model card](https://huggingface.co/startlux-models/StartLux-Decision-v1.1-27B-Instant/blob/32e7d35d74db615c4a059181efbf21c5421f3561/README.md); [startlux-models/StartLux-Decision-v1.1-4B-AutoThink model card](https://huggingface.co/startlux-models/StartLux-Decision-v1.1-4B-AutoThink/blob/23dd4c513ef387705bb13fd8caadc2d5c863082f/README.md); [startlux-models/StartLux-Decision-v1.1-9B-AutoThink model card](https://huggingface.co/startlux-models/StartLux-Decision-v1.1-9B-AutoThink/blob/efc649d8493b5b7353cf2ed6da0cdcbc215958ef/README.md); [StartLux: normalize list-form criteria/options before tournament routing](https://github.com/StartLuxLabs/StartLux-Decision/commit/83fe6c7d61a687a6e17f118b4f7d8f429f5d3a01); [StartLux: optional vLLM extra pinned to 0.31.0](https://github.com/StartLuxLabs/StartLux-Decision/commit/4b2026c96c0c5d4f5257745b3a03caf428fc730f); [StartLux-Prism: GGUF CUDA runtime, parity scope and licensing](https://github.com/StartLuxLabs/StartLux-Prism/tree/f32ed8eee9d89ea56dde03a978cf4128d2bbf497); [Prism: bidirectional Instant GGUF path and independent question rows](https://github.com/StartLuxLabs/StartLux-Prism/commit/cb700d0237ea37dad1772548f1f150dd4fc76b0b); [Prism: MXFP4 deferred-residual batch-invariance correction](https://github.com/StartLuxLabs/StartLux-Prism/commit/35d118d80dbe850d656efb409b2f475c84968e34); [Prism current serving: quantization and model-specific execution boundaries](https://github.com/StartLuxLabs/StartLux-Prism/blob/ef28f6f8d1b19f1336eafe418f26b96d053e8f76/docs/serving.md); [StartLux v2: training stages, selective computation and policy-aware calibration](https://arxiv.org/html/2610.17309v2); [StartLux current inference and archived v1 training boundary](https://github.com/StartLuxLabs/StartLux-Decision/tree/a99977d9332decc9fb27a2488b4a83b533b6cd5f); [Decision Index 0.4.1: November 19 frozen public aggregate](https://huggingface.co/spaces/multimodalart/jev-decision-index/blob/4ee57a1610e0547634ba0ec11990d10122672191/data/v03.json); [DI 0.4.1 scoring, equating and display ties](https://huggingface.co/spaces/multimodalart/jev-decision-index/blob/4ee57a1610e0547634ba0ec11990d10122672191/methodology.html)

<a id="baseten-decision"></a>
## Baseten mammoth-1 / elephant-1 / joey-1

[Project / model](https://huggingface.co/baselabs/mammoth-1)

Qwen-based 27B / 9B / 2B typed-decision family using shared-prefix evidence and separate question readouts; Joey is the smaller October sibling.
基于Qwen的27B／9B／2B类型化判断系列，共享证据前缀、分别读问题；Joey是10月新增的小型号。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | mammoth-1 nominal 27B from Qwen3.5-27B, elephant-1 9B from Qwen3.5-9B, Joey-1 2B from Qwen3.5-2B; no local tensor count. | mammoth-1名义27B基于Qwen3.5-27B，elephant-1 9B基于Qwen3.5-9B，Joey-1 2B基于Qwen3.5-2B；未本地统计张量。 |
| Mechanism | Existing LM answer-code logits with shared-state prefix and separated question suffixes. Full-attention layers use block-bidirectional masks; Gated DeltaNet remains causal. Bounded choice/noul/score outputs require the released prompt/runtime contract. | 使用LM答码logits，共享state前缀、问题后缀分开；full-attention用分块双向mask，Gated DeltaNet保持因果。有界choice／noul／score须匹配发布prompt／runtime合同。 |
| Training | Report/cards describe full language-model fine-tuning with frozen vision and CE plus Brier on a 6.21M-row Mix8; Joey card states one epoch and 16 H100s. Original report and earlier cards conflict on image supervision, so do not certify complete image-training provenance. Recipe disclosure and Brier training are not an audited enterprise fine-tuning package or deployment calibration. | 报告／卡描述冻结视觉、全语言微调，以CE加Brier训练621万行Mix8；Joey卡称一epoch、16张H100。原报告与早期卡在图像监督上有冲突，不认证完整图像训练谱系。披露配方及Brier训练不等于已审计企业续训包或部署校准。 |
| Deployment | Public HF serving bundles. Joey binary uploaded October 27; October 29 card links launch. Its trained length is 16,384 and longer requests reject rather than truncate. Public benchmark recipe selection and gated/missing training data still limit reproduction. No verified M5 training workflow. | 公开HF服务包；Joey binary于10月27日上传，10月29日卡链接launch。训练长度16384，超长拒绝而非截断；公共基准参与配方选择及gated／缺失训练数据仍限制复现，未验证M5训练链。 |
| Suggested use | Matched independent-question comparisons across 2B / 9B / 27B, keeping public-suite and replicated-index evaluations separate. | 在2B／9B／27B之间做同合同独立问题对照，将公共suite与复制指数评测分开。 |
| Boundary | Author public scores and a replica of Artificial Analysis are not official private Full results. Card image-input support does not establish image supervision or production risk. No universal-winner or 48 GB training-fit claim. | 作者公共成绩及Artificial Analysis复制评测不等于官方private Full；卡片支持图像输入不证明图像监督或生产风险控制，不声称通用胜出或48GB训练可行。 |

**License note:** Reviewed mammoth/elephant/Joey cards declare MIT; check each base, dataset and runtime term. No blanket public-data or commercial-service assurance.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Base Labs: mammoth-1 / elephant-1 technical report](https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models); [Mammoth-1 current card: image-input claim and conflicting training description](https://huggingface.co/baselabs/mammoth-1); [Baseten Joey-1: 2B sibling and training disclosure](https://huggingface.co/baselabs/joey-1/blob/9efbe485efbed9598dfca5294cbbe8da00e21908/README.md)

<a id="jeffan"></a>
## Jeffan (31B-1710 / 4B-2010 / 9B and 27B-1211)

[Project / model](https://huggingface.co/tattrongvu/Jeffan-31b-1710)

Text decision releases with distinct compute policies: older Gemma 31B selective rereading and newer Qwen 9B / 27B bidirectional code-readout models with optional layer loops.
文本判断发布物采用不同计算策略：较早Gemma31B选择性重读，较新Qwen9B／27B为双向答码读出并可循环中层。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Older Gemma 4-31B and 4B sibling; new Qwen3.5-9B card counts 8.95B and Qwen3.8-27B counts 26.90B, text-only. Layer-loop passes change compute without adding parameters. | 较早有Gemma4-31B及4B型号；新Qwen3.5-9B卡统计8.95B、Qwen3.8-27B统计26.90B，均仅文本。Layer-loop次数改变计算，不新增参数。 |
| Mechanism | Older 31B rereads the whole input below top probability 0.9 and replaces the first distribution. New 9B / 27B use noncausal full-attention with causal DeltaNet and code logits; repeated middle-layer blocks use damped updates. New 27B default loop_passes=1, new 9B default=2; one-pass vLLM and multi-pass reference are different workloads. | 旧31B在最高概率低于0.9时重读整段输入并替换初判；新9B／27B用非因果full-attention、因果DeltaNet及答码logits，以阻尼更新重复部分中层。新27B默认loop_passes=1，新9B默认=2；单pass vLLM与多pass参考是不同负载。 |
| Training | The new fixed cards identify bases and release weights but do not establish a full original training dataset/recipe or a domain fine-tuning workflow. Rereading and layer loops are inference policies, not training disclosures; no verified production probability calibration. | 新固定卡给出base及发布权重，但未建立完整原始训练数据／配方或领域续训链。重读和layer-loop是推理策略，不是训练披露；概率未验证生产校准。 |
| Deployment | New 9B / 27B binaries uploaded November 9; later November 12/13 edits concern card/vLLM serving. Published wrappers support different loop/backend settings; keep exact prompts and total latency. Quantized/GGUF siblings are inference artifacts, not M5 training evidence. Historical 31B context boundaries and unsupported image use remain version-specific. | 新9B／27B binary于11月9日上传；11月12／13日改动主要是卡及vLLM服务。发布封装支持的loop／后端配置不同，须固定prompt并计完整延迟。量化／GGUF sibling是推理产物，不是M5训练证据；旧31B上下文边界及未用图像应限于其版本。 |
| Suggested use | Compare bounded text decisions at fixed loop/reread policies and full request cost, then validate domain/language transfer separately. | 固定loop／重读策略及完整请求成本比较有界文本判断，再单独验证领域／语言迁移。 |
| Boundary | New public-suite scores are author runs, not official private Full. New cards report weaker non-English/unfamiliar-task behavior. Do not transfer old 31B results, thresholds or calibration to new 9B/27B, or treat a passing serving path as a post-training result. | 新公共suite成绩由作者运行，不是官方private Full；新卡披露非英语／陌生任务较弱。不可把旧31B成绩、阈值或校准移给新9B／27B，也不可把服务可运行当后训练效果。 |

**License note:** Reviewed current cards declare Apache-2.0 for weights/inference; earlier 31B / 4B license-only edits remain dated history. Verify exact upstream base terms and any new artifact separately.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Jeffan-31b-1710: model card and published conditional-reread engine](https://huggingface.co/tattrongvu/Jeffan-31b-1710/blob/cebfa86c2bed2b5c83b12e44de4374b20c87fd79/inference/README.md); [Jeffan: license-only change to Apache-2.0](https://huggingface.co/tattrongvu/Jeffan-31b-1710/commit/cebfa86c2bed2b5c83b12e44de4374b20c87fd79); [Jeffan 27B-1211: new weight identity and layer-loop contract](https://huggingface.co/tattrongvu/Jeffan-27B-1211/blob/f0ce7043ca32ebfe6613615e573a5010bda7228a/README.md); [Jeffan 9B-1211: two-pass default and serving contract](https://huggingface.co/tattrongvu/Jeffan-9B-1211/blob/862d1a7a8b64a8d708ddb0b0cd775a740f01841a/README.md); [Jeffan 4B-2010: earlier sibling and license change](https://huggingface.co/tattrongvu/Jeffan-4B-2010/blob/937a008f86f4a20a903d628f22ffad3e3f431d2c/README.md)

<a id="sii-decision"></a>
## SII-Decision (4B / 27B)

[Project / model](https://github.com/amazingljy1206/SII-Decision)

Reasoning-to-readout self-distillation into non-generative typed decisions; open 4B and 27B releases.
将推理后概率自蒸馏为零生成类型化判断；公开4B与27B产物。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | 4B: Qwen3.5-4B; 27B LoRA/Full: Qwen3.8-27B. | 4B基于Qwen3.5-4B；27B LoRA／Full基于Qwen3.8-27B。 |
| Mechanism | Candidate probabilities at a fixed first-answer-token readout without a generated rationale at deployment. | 部署不生成推理，在固定首个答案token位置读出候选概率。 |
| Training | Average two same-size reasoning-teacher distributions, distill by weighted soft cross-entropy, ordinal expected-score penalty and KL to p0. Released loader requires gold_target, train_target and p0; gold also controls hard-Noul weighting. LoRA and language-linear full tuning are distinct; Full still freezes embeddings/output head/norm/vision. | 平均同规模教师两次推理分布，以加权软交叉熵、序数期望差惩罚及对p0的KL蒸馏。公开loader要求gold_target、train_target与p0；gold还控制hard-Noul权重。LoRA与语言linear层Full训练分开；Full仍冻结embedding／输出头／norm／vision。 |
| Deployment | Public standalone BF16 HF releases and code. LoRA training saves adapters; published LoRA releases merge them into BF16 weights. Full training saves separate standalone checkpoints. Current multi-GPU launchers and inference demonstrations do not establish M5 training. The family has multiple HF revisions. | 公开独立BF16 HF产物与源码。LoRA训练保存adapter，发布LoRA是合并后的BF16权重；Full训练保存独立完整检查点。当前多GPU启动器及推理演示不能证明M5训练可行；系列有多个HF revision。 |
| Suggested use | Capability and distillation comparator; evaluate exact released checkpoints separately from enterprise adaptation. | 作为能力与蒸馏参照；发布检查点评测与企业领域适配分别验证。 |
| Boundary | JEVal is reported by SII authors. Required teacher/reference/gold fields and original-base training configurations are not a generic released-checkpoint hard-label warm-start recipe. No matched Chinese enterprise or Mac training result here. | JEVal包含作者对自有SII的报告。教师／参考／gold字段及从原始底座开始的配置，不等于从发布检查点直接硬标签续训。这里无共同中文企业数据或Mac训练实测。 |

**License note:** Repository/model cards declare Apache-2.0; retain upstream model and dataset obligations. No local tensor download or authentication of paper-evaluated weights.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [JEVal and SII-Decision: General Decision Models, paper v2](https://arxiv.org/html/2610.03935v2); [SII-Decision: released training and readout implementation](https://github.com/amazingljy1206/SII-Decision/tree/1723d83cbda69f48641c273280b5a2d06d6b3510); [SII-Decision-4B-LoRA: merged BF16 release](https://huggingface.co/jylin001206/SII-Decision-4B-LoRA/tree/5c77219871d297bd375c033eb63ad2cd010af657); [SII-Decision-27B-LoRA: merged BF16 release](https://huggingface.co/jylin001206/SII-Decision-27B-LoRA/tree/a7e7f9686bb9dad88b378978a984e3a52c13e649); [SII-Decision-27B-Full: language-linear full-tuning release](https://huggingface.co/jylin001206/SII-Decision-27B-Full/tree/8f5a51dcde7b0fd6a2eea3ab423bad5e3b11dfda)

<a id="glide"></a>
## GLiDE / Fastino

[Project / model](https://fastino.ai/blog/glide-decision-model-family)

Five-size open-weight decision family plus a native customer training API.
五尺寸开放权重判断系列，并有面向客户数据的原生训练API。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | 0.4B / 0.8B / 2B / 9B / 27B; inspect each backbone/readout separately. | 0.4B／0.8B／2B／9B／27B；各尺寸骨干与读出分别核验。 |
| Mechanism | Typed closed-option readout. The fixed public 2B runtime reports top1-minus-top2 confidence; score is the argmax level, with expectation in expected_level. Larger variants add recurrent depth. | 类型化闭集读出。固定公开2B运行库的confidence为top1与top2概率差；score为最高概率档，期望另在expected_level；大尺寸另有循环深度。 |
| Training | Native text rows accept gold and/or soft_target; glide_decision combines CE/KL (.3/.7 by default). A specific training/deploy API exists; complete public local trainer not located. Small-model prices and a 2B demo exist, but exact self-service IDs/account access/export remain untested. | 原生文本行接受gold及／或soft_target，glide_decision默认组合CE／KL(.3／.7)。已有具体训练／部署API，未定位完整公开本地trainer；有小模型报价及2B示例，但精确自助ID、账号开放性及导出未实调。 |
| Deployment | Family announced Nov5; fine-tuning example Nov18. Five public HF sizes; reviewed cloud training is text-only, 16,384 tokens/row, 512 rows/batch and no lora_config. No M5 backward or local training validation. | 11月5日发布家族、18日有微调示例；五个HF尺寸公开。所核云训练仅文本，每行16,384 tokens、每批512行，不接lora_config；未验证M5反向或本地训练。 |
| Suggested use | Add a small-model/readout comparator and, if data may leave the enterprise, a managed domain-adaptation route. | 新增小模型／读出对照；企业数据可获准上云时比较托管领域适配。 |
| Boundary | Do not inherit thresholds from another System One service. Public weights, a synthetic simulator improvement and training API documentation do not establish Chinese customer-service superiority or five-size self-service support. | 不能继承其他System One服务阈值；公开权重、合成模拟器增益及训练API文档不确立中文客服优势，也不证明五尺寸均已自助可训。 |

**License note:** Fastino Community License, not Apache; production commercial use by entities above the stated US$10M revenue threshold requires a separate agreement. Backbone terms also apply.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [fastino/GLiDE-2B — fixed release card](https://huggingface.co/fastino/GLiDE-2B/blob/00f122c120cdeed82284106cb77d9bab5a50ad16/README.md); [GLiDE decision model family](https://fastino.ai/blog/glide-decision-model-family); [GLiDE Training API](https://docs.fastino.ai/training); [Native decision forward/backward contract](https://docs.fastino.ai/api-reference/training-jobs/interactive/forward-backward); [GLiDE small-model fine-tuning example](https://fastino.ai/blog/glide-multimodal-decisions-fine-tuning); [GLiDE-2B Community License](https://huggingface.co/fastino/GLiDE-2B/blob/00f122c120cdeed82284106cb77d9bab5a50ad16/LICENSE); [GLiDE model/training pricing](https://docs.fastino.ai/pricing); [GLiDE-2B fixed public readout implementation](https://huggingface.co/fastino/GLiDE-2B/blob/00f122c120cdeed82284106cb77d9bab5a50ad16/glide/model.py)

<a id="liquid-d1"></a>
## Liquid d1 / d1.2

[Project / model](https://docs.liquid.ai/lfm/models/decision-models)

Open d1-2B/Omni-2B and separate hosted d1.2/ultra decision products.
开放d1-2B／Omni-2B与独立托管d1.2／ultra产品。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Open d1-2B about1.92B, with text/image/video inputs; Omni-2B is a separate artifact. Hosted ultra scale is not inferred from open2B. | 开放d1-2B约1.92B，支持文本／图像／视频输入；Omni-2B为另一产物。不从开放2B推测托管ultra规模。 |
| Mechanism | Typed decisions and extraction shapes vary by runtime. Multi-choice reports per-option P(yes), not a normalized single-choice simplex. | 类型化判断与提取形状依运行库而异；多选返回各项P(yes)，不是和为1的单选分布。 |
| Training | Generic LFM fine-tuning tooling is public, but a complete d1-specific typed-head training/save/reload/calibration path was not established. | 通用LFM微调工具公开，尚未建立d1专属typed-head训练、保存重载及校准闭环。 |
| Deployment | Hosted d1.2 announced Nov16; open2B replaces old3B. Official MPS/MLX inference and Chinese among16 languages; no user-machine training run. | 托管d1.2于11月16日发布；开放2B替代旧3B。官方有MPS／MLX推理、16语言含中文；无用户目标机训练实测。 |
| Suggested use | Study a small non-Qwen implementation and multi-label contract; evaluate hosted and local artifacts separately. | 研究小型非Qwen实现及多标签合同，托管与本地产物分别比较。 |
| Boundary | Do not transfer ultra benchmarks to open2B or confuse M5 inference with48GB training. Typed-answer support and reported calibration vary by release/runtime. | 不能将ultra成绩搬给开放2B，也不能将M5推理当48GB训练；类型与校准声明依版本／运行库而异。 |

**License note:** LFM Open License v1.0; commercial revenue threshold and separate-agreement conditions apply, not unconditional Apache.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [LiquidAI/d1-2B — fixed release card](https://huggingface.co/LiquidAI/d1-2B/blob/a6bce774e6dde338dcc3036ceb5d91f78bf4c19e/README.md); [LiquidAI/d1-Omni-2B — fixed release card](https://huggingface.co/LiquidAI/d1-Omni-2B/blob/51918b53052eacfd24062f99f13556c3c56fcf63/README.md); [Introducing d1.2](https://www.liquid.ai/blog/d1-2); [Liquid decision-model contracts](https://docs.liquid.ai/lfm/models/decision-models); [LFM license guide](https://docs.liquid.ai/lfm/help/model-license); [Liquid Finetune scope](https://docs.liquid.ai/lfm/fine-tuning/liquid-finetune)

<a id="mapika-decider"></a>
## Mapika Decider

[Project / model](https://github.com/Mapika/decider)

Open typed-decision family with supervised training/data builders; previously sourced but missing a core catalog entry.
有监督训练及数据构造器的开放判断系列；此前已有研读来源，但缺核心索引条目。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Reviewed2B v12,4B v3 and31B v2 releases date through Oct20. | 本轮核2B v12、4B v3及31B v2，发布至10月20日。 |
| Mechanism | Candidate-conditioned Qwen readouts and per-type temperatures; text/image contracts depend on size and release. | 候选条件化Qwen读出及按题型温度；文本／图片合同依尺寸与版本。 |
| Training | Public supervised recipe, data builders and own-label conversion. Environment PPO is a separate reported experiment; its complete research trainer was not located. | 监督配方、数据构造及自有标签转换公开；环境PPO为另一报告实验，未定位完整研究trainer。 |
| Deployment | Open weights/code; existing October releases, not newly trained today. MPS/MLX domain training not validated. | 权重／代码公开；属于10月发布补录，非今天新训练；未验证MPS／MLX领域训练。 |
| Suggested use | Compare an inspectable supervised implementation and its per-type calibration; study environment learning only with matching feedback. | 比较可审查的监督实现与逐题型校准；反馈匹配时才研究环境学习。 |
| Boundary | Default Noul T=.05 targets score optimization, not a validated probability. Fitted-temperature alternatives and all mixed-source licenses need separate review. | 默认Noul T=.05用于分数优化，不代表概率已校准；拟合温度替代项与混合来源许可分别核验。 |

**License note:** Apache-2.0 project/model declarations; upstream and mixed training-source conditions remain separate.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Mapika/decider-2b — fixed release card](https://huggingface.co/Mapika/decider-2b/blob/7614a6c7ea5a047aa7d7bcfb1a0015469381c3e3/README.md); [Mapika/decider-4b — fixed release card](https://huggingface.co/Mapika/decider-4b/blob/585473dec4fa93f0325c2bf02dda7273b61f44c1/README.md); [Mapika supervised training and deployment](https://github.com/Mapika/decider/tree/91b6fa9b94ab6c4dc2c63d3b14d413243b4fffcc)

<a id="rsi-jev"></a>
## RSI-Jev v7.0-VL

[Project / model](https://github.com/Shanghua-Gao/RSI-Jev)

Open Qwen decision implementation with public full training code and a truncated3B derivative.
公开完整训练代码的Qwen判断实现，另有截断3B衍生物。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | 4B instruction backbone;3B is the first20 language layers without retraining. | 4B指令底座；3B由前20语言层截断，未另训。 |
| Mechanism | Option-echo token pooling, bidirectional prefix and detached early-exit heads. | 候选复述的token pooling、双向前缀及分离梯度的早退头。 |
| Training | Full language fine-tuning with soft CE, retention/permutation KL and ranking; train/v7.0 and recipe public. Original2.76M rows/traces/dev not released; reported run used4 H200s. | 语言全参训练，含soft CE、保留／排列KL及排序；train/v7.0及配方公开。原276万行／轨迹／dev未发布；作者运行用4张H200。 |
| Deployment | 4B weights Nov5, truncated3B Nov7, MLX4bit conversion Nov10; fixed CUDA/NCCL trainer, MLX inference is separate. No M5 training receipt. | 4B权重11月5日、截断3B于7日、MLX4bit转换于10日；trainer固定CUDA／NCCL，MLX为推理；无M5训练回执。 |
| Suggested use | Prioritize code inspection and a small own-label comparison, including simple readout/LoRA controls. | 优先审实现并做小规模自有标签对照，保留简单读出／LoRA基线。 |
| Boundary | Public code is not full original-data reproduction; 3B/quantized variants are not independent training gains. Author benchmarks do not establish target-domain superiority. | 源码公开不等于原数据完整复现；截断／量化不是独立训练增益，作者成绩不确立目标域优势。 |

**License note:** Apache-2.0 declarations; inspect exact backbone, data and runtime dependencies before deployment.
**Recorded weight identifier:** 58baf6fc961f42108756b27ff92fddf4aea3b1d8

**Sources:** [shgao/rsi-jev-v7.0-vl-4b — fixed release card](https://huggingface.co/shgao/rsi-jev-v7.0-vl-4b/blob/58baf6fc961f42108756b27ff92fddf4aea3b1d8/README.md); [RSI-Jev v7 training and recipe](https://github.com/Shanghua-Gao/RSI-Jev/tree/e58526f061afd4c383d33a22b309b888f8a3e3c7)

<a id="jgeuter-jeff"></a>
## Jeff 1.1 / j-geuter

[Project / model](https://github.com/j-geuter/Jeff)

Open decision training implementation, distinct from Jeffan; published weights/data have noncommercial restrictions.
与Jeffan不同的公开判断训练实现；发布权重／数据有非商用限制。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Qwen4B/27B and Gemma12B/31B variants; complete4B weights existed by the reviewed Oct23 snapshot and are unchanged through Nov14. | Qwen4B／27B及Gemma12B／31B；所核10月23日快照已有完整4B权重，至11月14日tensor未变。 |
| Mechanism | Residual LM-row head with rank32 LoRA and three-seed adapter/head soup. | 残差LM-row读出，rank32 LoRA及三seed adapter／head平均。 |
| Training | Trainer/export, four configs and --data own JSONL were published Nov14; soft CE. DecisionBank mixes annotator votes and a Qwen teacher, including on annotator rows. | 11月14日公开trainer／export、四配置及--data自有JSONL；用soft CE。DecisionBank结合标注票数与Qwen教师，含有人类票数的行也混教师。 |
| Deployment | Code and raw dataset inspectable; current trainer selects CUDA/CPU, not native MPS. Existing4B tensors did not change with new trainer publication. | 源码及原始数据可审；当前trainer选择CUDA／CPU，无原生MPS路径；新公开trainer没有改变既有4B tensor。 |
| Suggested use | Study data/training mechanics; for commercial use train an appropriately licensed base on authorized own data. | 参考数据／训练机制；商用应从许可合适底座与获授权自有数据起训。 |
| Boundary | Published weights and full mixed dataset cannot be assumed commercially reusable. No Chinese-enterprise adaptation or M5 training evidence; do not conflate this owner with Jeffan. | 不能默认发布权重及全量混合数据可商用；无中文企业适配或M5训练证据，不能与Jeffan混同。 |

**License note:** Published weights CC-BY-NC-4.0; full mixed DecisionBank explicitly noncommercial. Code, base and individual data licenses are separate.
**Recorded weight identifier:** e2c4fb2f00189672c77e9d9a1619a8fd4884ab2d

**Sources:** [jgeuter/Jeff-1.1-Qwen-4B — fixed release card](https://huggingface.co/jgeuter/Jeff-1.1-Qwen-4B/blob/e2c4fb2f00189672c77e9d9a1619a8fd4884ab2d/README.md); [Jeff public training/export and own JSONL](https://github.com/j-geuter/Jeff/tree/938ac5a03c6ac43512e61266d9febf691edc17f8); [DecisionBank source/label provenance](https://huggingface.co/datasets/jgeuter/DecisionBank/tree/fbeee67758966fe78bfb008b28fc771924c0bc71)

<a id="jad"></a>
## JAD-S1 v0.5

[Project / model](https://huggingface.co/DreamBlooms/JAD-S1-7B-A1B-v0.5)

Diffusion/MoE-based closed-option decision adapter with single-mask readout.
基于扩散／MoE、单mask读出的闭集判断adapter。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | LLaDA-MoE7B total /1B active; resident memory is not1B. | LLaDA-MoE总7B／激活1B，驻留内存不等于1B。 |
| Mechanism | Read candidate-letter logits at one masked position rather than autoregressive answer generation. | 在单个mask位置读取候选字母logit，不自回归生成答案。 |
| Training | Rank8 adapter and inference/calibration package public; no complete trainer or raw training corpus in inspected release tree. | rank8 adapter及推理／校准包公开；所审发布树无完整trainer或原始训练语料。 |
| Deployment | v0.5 adapter uploaded Nov12 UTC, card version Nov13. Author ROCm128GB environment; not a validated M5 training path. | v0.5 adapter于UTC11月12日上传、卡标13日；作者用ROCm／128GB环境，非已验证M5训练路径。 |
| Suggested use | A different-backbone/readout research control if the local task justifies it. | 任务有需要时作为不同骨干／读出的研究对照。 |
| Boundary | Author Chinese translations/benchmarks are not enterprise data; active parameter count and open adapter do not establish low-memory training. | 作者中文翻译／基准非企业数据；激活参数与开放adapter不确立低内存训练。 |

**License note:** Apache-2.0 declarations for base/adapter code; exact dependencies and data rights remain separate.
**Recorded weight identifier:** 178febae0936d8c0f71312421d65e5b6baca466c

**Sources:** [DreamBlooms/JAD-S1-7B-A1B-v0.5 — fixed release card](https://huggingface.co/DreamBlooms/JAD-S1-7B-A1B-v0.5/blob/178febae0936d8c0f71312421d65e5b6baca466c/README.md)

<a id="h2o-lightning"></a>
## H2O Lightning 4B

[Project / model](https://huggingface.co/h2oai/h2o-lightning-4b)

Open Qwen4B typed-decision engine; this is a catch-up inclusion, not a November20 weight release.
开放Qwen4B类型化判断引擎；属于补录，非11月20日新权重。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Qwen3.5-4B; reviewed package v1.2.2. | Qwen3.5-4B；所核包v1.2.2。 |
| Mechanism | Custom typed readout/attention; option-order averaging, two-way reading and calculator settings change the measured path. | 定制类型读出／注意力；候选顺序平均、双向重读及计算器配置改变实际测量路径。 |
| Training | Training descriptions do not establish a complete own-data training/save/reload loop in this release. | 训练描述尚未建立本发布物的完整自有数据训练／保存重载链。 |
| Deployment | Created Oct2, current snapshot Nov1; image-capable inference package, no M5 backward verification. | 10月2日创建、当前快照11月1日；有图片推理包，无M5反向验证。 |
| Suggested use | Small typed-inference comparator after protocol and prompt settings are fixed. | 固定协议／提示配置后作为小型类型化推理对照。 |
| Boundary | Do not use stale October leaderboard placement as current quality or mistake HF auto-generated chat examples for the typed API. | 不能用10月旧榜位代表当前质量，也不能把HF自动聊天示例当类型化API。 |

**License note:** Apache-2.0 card declaration; check exact upstream/runtime licenses.
**Recorded weight identifier:** 659fc412de8486dbc2477b0d1cb4121e97e72471

**Sources:** [h2oai/h2o-lightning-4b — fixed release card](https://huggingface.co/h2oai/h2o-lightning-4b/blob/659fc412de8486dbc2477b0d1cb4121e97e72471/README.md)

<a id="mnn-pocket-dec"></a>
## MNN-Pocket-0.3B-Dec

[Project / model](https://huggingface.co/taobao-mnn/MNN-Pocket-0.3B-Dec)

Small Chinese/English choice, proposition and ordinal pointer-head package.
小型中英Choice／命题／有序评分pointer-head发布包。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | About300M base plus rank16 adapter and pointer head; bundled base is about723MB. | 约300M底座加rank16 adapter及pointer head；包内底座约723MB。 |
| Mechanism | Escaped reserved markers, shared state and isolated question branches; up to255 options with32k request rejection boundary. | 转义保留marker、共享state并隔离问题分支；最多255选项，32k请求边界超长拒绝。 |
| Training | Unmerged adapter/head present; inspected bundle exposes inference/calibration, not a complete domain-training loop. | 有未合并adapter／head；所审包提供推理／校准，非完整领域训练loop。 |
| Deployment | Created Oct15; metadata current Nov10. Original quantized/mobile MNN formats are separate artifacts; M5 training untested. | 10月15日创建、元数据至11月10日；原移动量化MNN格式为不同产物，M5训练未测。 |
| Suggested use | Very small Chinese readout/cost control, paired with a trained multilingual encoder. | 极小中文读出／成本对照，同时保留已训多语encoder。 |
| Boundary | Reported temperature fit on600 calibration cases is not held-out task accuracy or an enterprise risk guarantee. | 600个校准样本的温度拟合不等于独立任务准确率或企业风险保证。 |

**License note:** Apache-2.0 LICENSE.txt declaration; upstream terms remain applicable.
**Recorded weight identifier:** 7d5b512f3fe579418c45a77b178da39273b2a114

**Sources:** [taobao-mnn/MNN-Pocket-0.3B-Dec — fixed release card](https://huggingface.co/taobao-mnn/MNN-Pocket-0.3B-Dec/blob/7d5b512f3fe579418c45a77b178da39273b2a114/README.md)

<a id="granite-switch"></a>
## IBM Granite Switch / decision adapter

[Project / model](https://huggingface.co/blog/ibm-granite/granite-switch-4-1)

A reusable decision adapter alongside chat, guard and ASR capabilities on Granite4.1.
Granite4.1上可复用的decision adapter，与聊天、guard及ASR并列。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Frozen8B/30B base plus rank64 adapters; tiny adapter does not remove the resident base. | 冻结8B／30B底座加rank64 adapter；小adapter不消除底座驻留。 |
| Mechanism | LoRA/aLoRA decision marker activates single-label-token logits; no sampling/generate for decisions. Each question uses a pass; aLoRA reuses pre-marker base cache. | LoRA／aLoRA判断marker激活单标签token读出；判断不采样／generate，每题一次pass，aLoRA复用marker前底座cache。 |
| Training | Adapter artifacts and inference contract public; generic PEFT adaptation is not a verified complete decision-domain training pipeline. aLoRA is not merged into the base. | adapter产物及推理合同公开；通用PEFT可适配不等于完整判断领域trainer已验证；aLoRA不合入base。 |
| Deployment | Official introduction Oct15; current core/adapter revision Oct28, v1.1. English card; no M5 training validation. | 官方10月15日介绍；当前core／adapter于28日、v1.1；卡为英语，无M5训练验证。 |
| Suggested use | Study decision/chat sharing and cache-aware adapters when a larger resident base is justified. | 较大底座确有必要时，研究判断／聊天共用及cache-aware adapter。 |
| Boundary | Adapter size and cache sharing are efficiency mechanisms, not calibrated correctness or Chinese adaptation evidence. | adapter大小与cache共享是效率机制，不是概率校准或中文适配证据。 |

**License note:** Apache-2.0 declarations; base, adapter and dependencies must be pinned separately.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [IBM Granite Switch introduction](https://huggingface.co/blog/ibm-granite/granite-switch-4-1); [Granite decision adapter v1.1](https://huggingface.co/ibm-granite/granitelib-core-r1.0/blob/b881a4371db7284beac66a658b0cadcd32b12977/decision/README.md)

<a id="ant-lingdt"></a>
## Ant Digital LingDT-Decision-1.0

[Project / model](https://maas.antdigital.com/models/modelservice-1792325631780001741)

Hosted typed decision service with native question-dependency DAG.
托管类型化判断服务，原生支持问题依赖DAG。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Current public contract identifies a4B test endpoint; no public weight identity established. | 当前公开合同列4B测试端点，未建立公开权重身份。 |
| Mechanism | Choice, multi-choice, proposition, score and extraction. The native depth3 DAG service calls layers sequentially and injects upstream_answers into later state; this is orchestration, not established single-forward model dependency reasoning. | 单／多选、命题、评分与提取。原生深度3 DAG服务逐层调用，并将upstream_answers注入后续state；这是编排合同，不证明模型单前向完成依赖推理。 |
| Training | No public weights or this decision product-specific customer fine-tuning entry verified. | 未核公开权重或本判断产品专属客户微调入口。 |
| Deployment | Observed free test-period contract:4B endpoint,16k request,32 questions,255 options, default60RPM. A production reference to LingDT1.1 does not identify a new Decision1.1 checkpoint. | 本次观察免费测试期合同：4B端点、16k请求、32题、255选项、默认60RPM；建议生产用LingDT1.1不等于确立新Decision1.1检查点。 |
| Suggested use | Domestic hosted contract/dependency reference; evaluate access and data governance separately. | 国内托管合同／依赖参考，另验访问与数据治理。 |
| Boundary | Public service metadata establishes an advertised contract, not actual account availability, self-training or production effect. | 公开服务元数据只确立声明的合同，不证明账号可用、自主后训练或生产效果。 |

**License note:** Proprietary service terms; no open-weight or customer training license established.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Ant Digital public LingDT decision service contract](https://maas.antdigital.com/api/v1/model-service/public/get/modelservice-1792325631780001741)

<a id="span-02"></a>
## Respan Span-02

[Project / model](https://www.respan.ai/blog/introducing-span-2)

Open decision serving artifact with a specialized quantized Rust/CUDA engine and optional reasoning.
使用专用量化Rust／CUDA引擎、可选推理的开放判断服务产物。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Gemma4 26B-A4B; about4B active is not4B resident or trainable-package memory. | Gemma4 26B-A4B；约4B激活不等于4B驻留或训练包内存。 |
| Mechanism | Choice is non-generative readout; number questions generate numeric tokens. auto/on/off and budget_ms change the returned decision path. | Choice为非生成读出，number题生成数字token；auto／on／off及budget_ms改变实际判断路径。 |
| Training | No full trainer, raw training data or trainable BF16 release established; current engine is an inference artifact. | 未建立完整trainer、原始训练数据或可训练BF16发布物；现有engine为推理产物。 |
| Deployment | Blog Oct15, gateway changelog Oct19. Specific NVIDIA engine, about28GB GPU memory; not ordinary Transformers/vLLM or a verified M5 route. | 博客10月15日、gateway于19日更新；专用NVIDIA引擎、约28GB GPU内存，非普通Transformers／vLLM或已验证M5路线。 |
| Suggested use | Study self-hosted inference and budgeted reasoning as separate serving controls. | 研究自托管推理与预算推理，作为独立服务策略对照。 |
| Boundary | Span-01 behavior detection is a different contract. Quantized open serving weights do not establish enterprise post-training or portable confidence thresholds. | Span-01行为检测为另一合同；开放量化服务权重不确立企业后训练或可移植置信阈值。 |

**License note:** Apache-2.0/Gemma4 declarations; inspect engine and upstream terms separately.
**Recorded weight identifier:** 63cbdd774391f1b7d9bc3829179efe996d0191ce

**Sources:** [respanai/span-02 — fixed release card](https://huggingface.co/respanai/span-02/blob/63cbdd774391f1b7d9bc3829179efe996d0191ce/README.md); [Introducing Span-02](https://www.respan.ai/blog/introducing-span-2)

<a id="decisio"></a>
## Decisio tuned v3 / Tachara AI

[Project / model](https://github.com/aminry/decisio)

November20 Gemma12B tuned release with calibrated and commit serving policies and multiple precision ports.
11月20日发布的Gemma12B适配权重，含calibrated／commit策略及多精度部署包。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | 12B; about22GB merged BF16 weights, not total training memory. | 12B；合并BF16约22GB，仅权重、非完整训练内存。 |
| Mechanism | One forward per question reads typed-option probabilities; per-type temperature and an external calculator affect the service. | 每题一次前向读取类型化选项概率；逐题型温度及外部计算器影响服务。 |
| Training | Card reports rank32/alpha64 LoRA on463,859 questions for one epoch. Inspected server tree does not establish a complete public own-data trainer; card calibration claims need independent task validation. | 卡称rank32／alpha64 LoRA、463,859题一epoch；所审服务树未建立完整公开自有数据trainer，卡的校准声明须独立任务验证。 |
| Deployment | Eight November20 repos include policy/FP8/MLX variants. Complete declared LFS tensor sets match between the two BF16 flavors; no tensor bytes downloaded. MLX inference is not MLX training. | 11月20日八个仓包含策略／FP8／MLX变体；两BF16策略包完整声明LFS tensor集合相同，未下载tensor字节；MLX推理不等于训练。 |
| Suggested use | A fresh serving/readout comparator; evaluate calibrated policy, commit policy and calculator under the same contract. | 新增服务／读出对照；同合同分验calibrated、commit及计算器。 |
| Boundary | Author held-out tests come from its training distribution, not an independent enterprise benchmark. Policy variants are not eight separately trained models; calibration is not guaranteed under shift. | 作者留出测试来自其训练分布，非独立企业基准；策略变体不是八个独立训练模型，漂移下不保证校准。 |

**License note:** Apache-2.0 card/LICENSE declaration; base, runtime and derived artifacts separately pinned.
**Recorded weight identifier:** 1e9159cc082c689fd95381e0ed6306402dc932d2

**Sources:** [tachara-ai/Decisio-12b-tuned-v3-calibrated — fixed release card](https://huggingface.co/tachara-ai/Decisio-12b-tuned-v3-calibrated/blob/1e9159cc082c689fd95381e0ed6306402dc932d2/README.md); [Decisio serving repository](https://github.com/aminry/decisio/tree/ad9c265abd677fd7113435bd5e4b766c9a4848ce)

<a id="valen-decision"></a>
## Valen-Decision1.5

[Project / model](https://github.com/Valen-Team/Valen)

Multimodal typed-decision family with native published-checkpoint domain training, separate from its ONNX/GGUF/ANE conversions.
多模态类型化判断系列，有从已发布native检查点领域训练的入口，与ONNX／GGUF／ANE转换分开。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Fixed4B audit; family card lists0.8B/2B/4B/9B/27B. BF16 backbone and FP32 decision/grounding heads. | 固定核4B；家族卡列0.8B／2B／4B／9B／27B；BF16骨干、FP32判断／grounding头。 |
| Mechanism | Block-bidirectional attention, trained Mixer and bbox grounding; typed predicate/choice/score/bbox readout, with shared-state question branches. | block-bidirectional注意力、已训练Mixer及bbox grounding；predicate／choice／score／bbox类型化读出，shared-state问题分支。 |
| Training | Complete native checkpoint can retain Mixer/grounding for own-JSONL full or LoRA SFT. Public runner, schema/configs, resume/export tests and cookbook; the SFT loss defaults to distribution CE, with optional RPS/Brier used by the domain example. Sampled discrete-action RLCD is a separate experimental objective, not PRDO or a verified TypeSafe recipe. Original training data not public. | 完整native检查点可保留Mixer／grounding，用自有JSONL做full／LoRA SFT；公开runner、schema／配置、恢复／导出测试及cookbook。SFT loss缺省为分布CE，领域示例另配可选RPS／Brier；采样离散动作RLCD是另一个实验目标，不是PRDO或已验证TypeSafe配方。原始训练数据未公开。 |
| Deployment | Complete4B tensors uploaded Nov9; Nov12 card edit, Nov15 source snapshot. Official0.8B/H200 one-update plus resume smoke is not a4B/M5 run. Trainer defaults CUDA; configured-device float64 statistics need MPS compatibility work. ANE/ONNX/GGUF are inference formats. | 完整4B tensor于11月9日上传，12日改卡，源码快照15日。官方0.8B／H200单步加恢复smoke不是4B／M5运行。默认CUDA；配置device上的float64统计需处理MPS兼容；ANE／ONNX／GGUF为推理格式。 |
| Suggested use | Prioritize an inspectable native-checkpoint LoRA comparator for proprietary data on compatible hardware; keep original and direct CE controls. | 在兼容硬件上优先纳入可审查的native续训LoRA对照，保留原版及直接CE控制。 |
| Boundary | Short engineering receipts and author public index results do not establish enterprise adaptation gains, Chinese long-state performance or calibrated acceptance risk. A Metal/ANE port does not solve training device, gradient or export contracts. | 短工程回执及作者公共指数不确立企业适配增益、中文长状态表现或校准放行风险；Metal／ANE端口不解决训练设备、梯度及导出合同。 |

**License note:** Apache-2.0 native model/code declarations; original training data not public, upstream and media/data rights remain separate.
**Recorded weight identifier:** 9b0cacc976d7fb72f252ee1adb1564f5f15e462c

**Sources:** [Valen Decision1.5 4B fixed native release](https://huggingface.co/Valen-Team/Valen-Decision-1.5-4B/blob/9b0cacc976d7fb72f252ee1adb1564f5f15e462c/README.md); [Valen native own-data SFT/RLCD training](https://github.com/Valen-Team/Valen/blob/f6df4fdbc45bf44a4ffbebaeda53f5fe6e49b339/valen/training/README.md); [Valen training device/statistics boundary](https://github.com/Valen-Team/Valen/blob/f6df4fdbc45bf44a4ffbebaeda53f5fe6e49b339/valen/training/distributed.py); [Valen complete domain adaptation workflow](https://valen-team.github.io/cookbook/domain-finetuning/)

