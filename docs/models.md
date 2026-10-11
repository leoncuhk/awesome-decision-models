# Model cards / 模型卡

[Home](../README.md) · [中文首页](../README.zh-CN.md) · [Evidence](evidence.md)

Source review: 2026-10-11. These are source-backed descriptions and curatorial use cases, not production certifications.

`Unknown` is intentional. An inspected source revision does not identify the deployed weight revision. Language support, licenses and resource requirements must be checked for the exact artifact. Recorded weight identifiers are source-reported unless a local binary verification is explicitly documented; recording an identifier is not a claim that the weights were downloaded or hashed here.

<a id="jev"></a>
## Jev / TypeSafe

[Project / model](https://typesafe.ai)

Hosted typed judgments: probabilities over supplied choices, propositions and ordinal rubrics.
托管的结构化判断服务：对选项、命题与有序评分标准输出分布。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Not publicly established by the reviewed material. | 核对的公开资料未明确参数规模。 |
| Mechanism | Proprietary model. Choice/Score confidence summarizes the returned distribution; it is not a separate probability-of-correctness estimate. Noul returns P(yes) with no separate confidence field. | 专有模型。Choice／Score 的 confidence 是返回分布的统计量，并非独立预测的正确概率；Noul 返回 P(yes)，没有单独 confidence 字段。 |
| Training | Vendor-described RLCD; controlled independent ablations not established here. | 官方称采用 RLCD；本版未取得受控独立消融证据。 |
| Deployment | Hosted API; no public weights verified. | 托管 API；本版未核实公开权重。 |
| Suggested use | A managed comparator when testing whether a judgment node is useful. | 验证判断节点价值时，可作为无需自建部署的对照。 |
| Boundary | RLCD is vendor-described; the full training recipe is not public. Valid schemas and confidence fields do not establish semantic reliability. | RLCD 的完整训练配方未公开；格式合法与置信度字段不等于语义可靠。 |

**License note:** Commercial service terms; no open-weight license implied.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev); [TypeSafe primitives](https://docs.typesafe.ai/primitives); [TypeSafe confidence semantics](https://docs.typesafe.ai/confidence)

<a id="laya"></a>
## Laya

[Project / model](https://github.com/NandhaKishorM/laya)

Compact encoder family with dynamic option heads; general, multilingual and workflow-specialized checkpoints.
小型编码器与动态选项判断头；包含通用、多语言及工作流专项检查点。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | English and workflow specialist: about 421M; multilingual: about 322M. | 英语及专项版约 421M；多语言版约 322M。 |
| Mechanism | Bidirectional encoder plus option-conditioned decision head. | 双向编码器加选项条件化判断头。 |
| Training | Proper-score rewards and policy gradients; the typed specialist also uses soft cross-entropy. Not a confirmed reproduction of Jev training. | 适当评分奖励与策略梯度；专项训练还使用软交叉熵。不是已确认的 Jev 训练复现。 |
| Deployment | Local weights/runtime; checkpoint and language must be selected explicitly. | 本地权重与运行库；应明确检查点及语言。 |
| Suggested use | Narrow, high-volume judgments with domain training and measured hardware costs. | 适合有领域训练数据、需要控制高频调用成本的窄域判断。 |
| Boundary | Do not mix base/specialist scores; the typed card discloses training/calibration overlap and inherited-temperature conflicts. Boolean labels can dominate noul/choice; semantic labels alone do not make negation safe. action.act_probability is documented as nearly constant at 1 and unsuitable as an execution gate. Validate confidence on your workload instead. | 不可混用基础版／专项版成绩；专项卡披露训练／校准重叠和继承温度冲突。布尔标签可能主导 noul／choice；语义标签也不能保证否定句安全。官方称 action.act_probability 几乎恒为 1，不适合作为执行门槛；confidence 也需在实际任务上验证。 |

**License note:** Reviewed family/specialist cards declare Apache-2.0; verify each selected artifact.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Laya model family](https://huggingface.co/convaiinnovations/laya); [Laya Typed-Decisions model card](https://huggingface.co/convaiinnovations/laya-typed-decisions); [Laya documented operational limitations](https://github.com/NandhaKishorM/laya/blob/a4a8921afebfd852bba0000475cfb6ab737a124c/README.md#honest-limits)

<a id="kev"></a>
## Kev

[Project / model](https://github.com/jaredpalmer/kev)

Qwen-based typed decision family with a dynamic pointer head; Kev 1.0 freezes existing checkpoints as a release baseline.
Qwen 骨干与动态 pointer head 的类型化判断系列；Kev 1.0 将现有检查点固定为发布基线。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Released family spans 0.8B, 4B, 9B and 27B; inspect the exact backbone/card. | 公开系列覆盖 0.8B、4B、9B、27B；须核对具体骨干与模型卡。 |
| Mechanism | Dynamic option readout on a language-model backbone; several model sizes. | 在语言模型骨干上动态读出选项分数；提供多个规模。 |
| Training | 0.8B/4B/9B use LoRA plus a head. 27B v2 fully fine-tunes Qwen3.8-27B, then averages weights 0.85/0.15 with v1. Temperature fitting is distribution-specific; 0.8B/4B use held-out items from trained families. | 0.8B／4B／9B 使用 LoRA 与判断头；27B v2 全参数微调 Qwen3.8-27B，再按 0.85／0.15 与 v1 平均权重。温度拟合依赖分布；0.8B／4B 使用训练任务族的保留样本。 |
| Deployment | Small releases require the base plus adapter/head; 27B v2 ships about 51 GB of full bf16 weights plus head. Served limit: 65,536 tokens. Author-validated CUAD context: 8,192 for 0.8B/4B/9B, 65,536 for 27B, under the stated 3-pp non-inferiority rule. | 小型号需基座、适配器与判断头；27B v2 发布约 51 GB 的完整 bf16 权重与判断头。服务上限 65,536 token；按作者 CUAD 的 3 个百分点非劣效规则，0.8B／4B／9B 仅验证至 8,192，27B 至 65,536。 |
| Suggested use | An inspectable starting point for domain-supervised decision models. | 可检查、可微调的领域监督判断实验底座。 |
| Boundary | Keep trained-family tests separate from transfer. 27B v2 is worse and overconfident on long contracts (CUAD ECE 0.053 versus v1 0.007). Serving capacity and fitted temperature do not guarantee accuracy or calibration on new workloads. | 须区分训练任务族测试与迁移测试。27B v2 在长合同上退步且过度自信（CUAD ECE 0.053，v1 为 0.007）；可接收长度和拟合温度不保证新任务的准确率或校准。 |

**License note:** Kev 1.0 cards declare Apache-2.0 for the released weights/head and listed bases; verify the exact artifact. A family entry has no single weight revision.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Kev repository](https://github.com/jaredpalmer/kev/blob/2855ba2a55a80579176a459f78b95d03548cabb5/README.md); [Kev-4B model card](https://huggingface.co/jaredpalmer/kev-4b); [Kev 1.0 release baseline](https://github.com/jaredpalmer/kev/blob/5e42a7a03f28134853dd3ff77461457e921e5ec1/docs/releases/kev-1.0.md); [Kev-27B v2 model card](https://github.com/jaredpalmer/kev/blob/5e42a7a03f28134853dd3ff77461457e921e5ec1/docs/model-cards/kev-27b.md)

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

**Sources:** [CLM repository](https://github.com/Contrastive-LM/CLM/blob/bb42c6c5bf914fd449bed2f6ca65be80602cb1f7/README.md); [CLM v0.1-8B model card](https://huggingface.co/Contrastive-LM/CLM-v0.1-8B); [DeepSWE fixed-split projection head](https://huggingface.co/Contrastive-LM/deepswe-clm-heads-8k)

<a id="nimble"></a>
## Bespoke Nimble

[Project / model](https://github.com/bespokelabsai/nimble)

Qwen-based supervised adapter that reads answer-label logits instead of generating an explanation.
Qwen 监督适配器，直接读取答案标签 logits，而非生成解释。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | 9B backbone plus adapter; adapter bytes alone are not required memory. | 9B 骨干加适配器；适配器文件大小不等于所需内存。 |
| Mechanism | Qwen3.5-9B plus LoRA, scoring allowed answer tokens. | Qwen3.5-9B 加 LoRA，对允许的答案 token 评分。 |
| Training | Supervised learning; minimal changes to decisive evidence help define the boundary. | 监督学习；用决定性证据的最小变化构造判断边界。 |
| Deployment | Adapter and code are public; load the base model as well. | 公开适配器与代码；仍需加载基础模型。 |
| Suggested use | A transparent baseline for evidence-sensitive judgments and minimal-edit training examples. | 适合证据敏感的判断，也可借鉴最小差异训练样本。 |
| Boundary | Contrastive data construction is not CLM-style contrastive embedding training. Public benchmark reporting is author-run and raw run outputs are not all committed. | 对比式样本构造不等于 CLM 的对比表示训练；公开比较由项目方运行，完整逐行输出并未全部提交。 |

**License note:** Reviewed model card declares Apache-2.0; inherited dependencies retain their terms.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Bespoke Nimble model card](https://huggingface.co/bespokelabs/Bespoke-Nimble-9B); [Nimble public human-reference benchmark protocol and results](https://github.com/bespokelabsai/nimble/blob/62076b4f2d365b5879dafcf7f6dd072a1fe76df7/docs/PUBLIC_BENCHMARKS.md)

<a id="gliner-decide"></a>
## GLiNER2.5-Decide

[Project / model](https://huggingface.co/fastino/GLiNER2.5-Decide-1B)

Schema-conditioned local classification with runtime labels and multiple decision heads.
通过运行时标签与多个判断头实现模式条件化的本地分类。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | 1B card directly reviewed; 340M and 287M sibling results/links are cross-reported there. | 直接核对 1B 卡；340M 与 287M 同系列资料由该卡交叉报告。 |
| Mechanism | Encoder-style classification; single-label and multilabel outputs. | 编码器式分类；支持单标签与多标签输出。 |
| Training | Treat checkpoint-specific training details as documented, not inferred from sibling models. | 训练细节按具体检查点文档记录，不从同系列模型推断。 |
| Deployment | Published local checkpoints and GLiNER2 runtime; use version-matched examples. | 公开本地检查点及 GLiNER2 运行库；示例须匹配版本。 |
| Suggested use | Compact operational classification; inspect the runtime for supported cross-field constraints. | 适合轻量业务分类；跨字段约束需核对具体运行库支持。 |
| Boundary | This review inspected the 1B card, which cross-reports 340M results. Dataset audit is incomplete; JevK5 in that table is not TypeSafe Jev. | 本版核对的是 1B 模型卡，其中交叉报告 340M 成绩；数据集审计未完成，表中 JevK5 不是 TypeSafe Jev。 |

**License note:** Reviewed 1B card declares Apache-2.0; other checkpoints need separate checks.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [GLiNER2.5-Decide-1B model card](https://huggingface.co/fastino/GLiNER2.5-Decide-1B); [GLiNER2 runtime](https://github.com/fastino-ai/GLiNER2)

<a id="gliclass"></a>
## GLiClass

[Project / model](https://github.com/Knowledgator/GLiClass)

Label-conditioned text classification with user-supplied labels, including multilabel tasks.
以用户提供的标签为条件进行文本分类，包含多标签任务。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Checkpoint-dependent; no single family-wide parameter claim made here. | 依具体检查点而定；本版不为整个系列指定单一参数量。 |
| Mechanism | Joint text/label representation and label scoring. | 联合表示文本与标签，再对标签评分。 |
| Training | Consult the selected checkpoint; do not attribute every GLiClass variant one recipe. | 以具体检查点为准，不给所有版本统一指定训练配方。 |
| Deployment | Open repository with links to model checkpoints. | 公开仓库，并链接模型检查点。 |
| Suggested use | An adjacent baseline for dynamic intent and label classification. | 动态意图与标签分类的重要相邻基线。 |
| Boundary | Classification capability does not establish general workflow verification or calibrated operational risk. | 分类能力不等于通用工作流验收能力，也不保证业务风险已校准。 |

**License note:** Consult repository and chosen checkpoint license; not fully audited in this edition.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [GLiClass](https://github.com/Knowledgator/GLiClass)

<a id="jevos"></a>
## jevos

[Project / model](https://github.com/feder-cr/jev)

Local yes/no decision model served as GGUF through llama.cpp, with a TypeSafe Jev-compatible request/response shape for `noul` questions.
通过 llama.cpp 以 GGUF 格式提供本地是非判断，`noul` 请求与响应采用 TypeSafe Jev 的接口格式。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Project documentation describes 1B parameters; this review did not inspect the weight tensors or independently count parameters. | 项目文档称为 1B 参数；本次没有检查权重张量或独立核算参数量。 |
| Mechanism | The inspected binary runtime reads logits at fixed 0/1 answer-token slots and applies softmax to return P(yes), without text generation. The submitted MiniCPM5 base and 17-layer count remain unestablished; this code path was not executed here. | 核读源码的二元模式读取固定 0/1 答案 token 槽的 logits，再通过 softmax 返回 P(yes)，不生成文本。投稿所述 MiniCPM5 基座和 17 层结构仍未确证；本次没有执行这条代码路径。 |
| Training | Training recipe, dataset and base-checkpoint provenance were not established by the reviewed sources; no independent training reproduction. | 核读来源未确证训练配方、数据集和基座检查点来源；没有独立训练复现。 |
| Deployment | The v2 release lists q4_k_m (619,289,280 bytes) and q8_0 GGUF assets. Documentation describes offline CPU use via llama.cpp. Listed hashes are publisher/API metadata, not local binary verification. | v2 发布页列出 q4_k_m（619,289,280 字节）和 q8_0 GGUF 权重，文档说明可通过 llama.cpp 在 CPU 上离线运行。记录的哈希来自发布方/API 元数据，未经本地下载核验。 |
| Suggested use | Experiment with CPU-local reading and triage questions; put the full policy in `instructions` and validate behavior on your own labeled cases. | 用于探索 CPU 本地文本判读与分流；将完整规则写入 `instructions`，并用自己的标注样例验证行为。 |
| Boundary | Yes/no only: `choice` and `score` return 422, and the jevos documentation says `criteria` is accepted but ignored. Wire-format compatibility is not semantic equivalence. Arithmetic/date errors and benchmark sensitivity are author-reported; old README results do not identify v2 performance. | 仅支持是非判断：`choice`、`score` 返回 422，jevos 文档说明 `criteria` 虽被接受却不参与判断。接口格式兼容不等于语义等价。算术、日期错误及评测敏感性由作者自报；旧版 README 的成绩不能代表 v2。 |

**License note:** Repository LICENSE is MIT; reviewed release metadata does not separately establish base-weight license provenance.
**Recorded weight identifier:** 3cbf010ce06cba932af73346ee683ee98d375dc284c029967eb418472a4993f3

**Sources:** [jevos pinned README and runtime documentation](https://github.com/feder-cr/jev/tree/9e7d9e8a24e9605bec249045a39df91ff2b58b0d); [jevos-v2 release and asset metadata](https://github.com/feder-cr/jev/releases/tag/jevos-v2); [jevos repository README](https://github.com/feder-cr/jev/blob/eb74cf78e5377e85fcaa76f6ebc9f82e8b517250/README.md)

<a id="clef"></a>
## Clef / Clef-Flash

[Project / model](https://huggingface.co/Cloudflare/clef)

Multimodal Qwen backbones with a joint schema head for typed decisions and a Jev/SystemOne-compatible wrapper.
多模态 Qwen 骨干加联合 schema 判断头，输出类型化决策，提供 Jev/SystemOne 兼容封装。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Cards describe Clef as 27B (Qwen3.8-27B) and Clef-Flash as 9B (Qwen3.5-9B), each retaining a vision encoder; parameter counts are source-reported. | 模型卡称 Clef 为 27B（Qwen3.8-27B），Clef-Flash 为 9B（Qwen3.5-9B），均保留视觉编码器；参数量为来源自报。 |
| Mechanism | Joint transformer head routes state evidence to questions and jointly scores their allowed options in one forward pass; no free-form answer generation. | 联合 Transformer 判断头把状态证据路由到问题，在一次前向计算中对各题允许的选项评分，不生成自由文本答案。 |
| Training | Cloudflare reports rank-256 LoRA plus the routing head, label-smoothed cross-entropy, Brier loss and a secondary RLCD objective on internal synthetic data; the full data/recipe was not audited. | Cloudflare 称使用 rank-256 LoRA 与路由头、标签平滑交叉熵、Brier 损失及辅助 RLCD 目标，训练数据为内部合成数据；完整数据和配方未审计。 |
| Deployment | Public weights and custom load_release_model/systemone helpers; also Workers AI. The hosted Clef page lists 65,536 tokens, while local encode_record defaults to 16,384. Check the specific endpoint schema for supported media and truncation. | 公开权重及定制 load_release_model／systemone 函数，另有 Workers AI。Clef 托管页面列 65,536 token，本地 encode_record 默认 16,384；媒体支持与截断行为须核对具体接口。 |
| Suggested use | Compare text/image-based classification, triage and ordinal judgments with task-specific error costs. | 比较文本／图像分类、分流与有序评分，并按具体任务衡量错误成本。 |
| Boundary | Vendor benchmarks have task-specific trade-offs. API compatibility and probability outputs do not establish calibrated business risk; local inference needs the custom schema runtime. | 厂商评测存在任务间取舍；接口兼容和概率输出不等于业务风险已校准，本地推理需要定制 schema 运行代码。 |

**License note:** Both reviewed release cards declare Apache-2.0; this does not establish that all training data or the full training recipe are public.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Cloudflare Clef launch and evaluation report](https://blog.cloudflare.com/clef-decision-models/); [Clef 27B model card](https://huggingface.co/Cloudflare/clef/blob/2f3de3dd85f379784083b0814d997ab627200f0c/README.md); [Clef-Flash 9B model card](https://huggingface.co/Cloudflare/clef-flash/blob/17f0b0ad64efb65d273590632833508766b2aae6/README.md); [Clef Workers AI interface and context limit](https://developers.cloudflare.com/workers-ai/models/clef/)

<a id="strands-decider"></a>
## Strands Decider

[Project / model](https://github.com/strands-labs/strands-decider)

Qwen3.5 and Gemma 4 pointer-head family; October v1 releases average three trained adapters/heads and then calibrate.
Qwen3.5 与 Gemma 4 pointer-head 系列；10 月 v1 发布平均三个训练适配器／判断头后再校准。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Qwen3.5 2B and Gemma 4 E2B/E4B/12B/26B-A4B; active MoE size does not equal resident weight memory. | Qwen3.5 2B 与 Gemma 4 E2B／E4B／12B／26B-A4B；MoE 激活参数量不等于驻留权重内存。 |
| Mechanism | Replaces the language-model head with a dynamic pointer readout comparing the answer-position state to option-token states; one forward pass for noul, choice or score. Confidence is derived from the distribution, not a separate correctness predictor. | 以动态 pointer 读出替代语言模型输出头，比较答案位置与选项 token 的隐状态，一次前向计算支持 noul、choice、score。置信度由分布推导，并非独立正确率预测器。 |
| Training | Qwen v1: 246678 balanced rows, Gemma-4-31B teacher and v19 KL anchor. Gemma v1: 135602 rows, Qwen3.5-4B teacher and v19 anchor. Three-seed soups store rank-48 LoRA plus three readouts; recipes differ by family. | Qwen v1：246678 条平衡样本、Gemma-4-31B 教师与 v19 KL 锚点。Gemma v1：135602 条样本、Qwen3.5-4B 教师与 v19 锚点。三种子平均保存 rank-48 LoRA 与三个读出头；不同系列配方不同。 |
| Deployment | Current Qwen: strands-decider-2B-qwen3.5-v1-2610; four Gemma v1 sizes are text-only and need runtime main at the reviewed revision. Separate base weights; 4096-token trained/served window. v19/v21 remain published. | 当前 Qwen 为 strands-decider-2B-qwen3.5-v1-2610；四种 Gemma v1 仅文本，所核版本需运行库 main。另需基座权重，训练／服务窗口 4096 token；v19／v21 继续发布。 |
| Suggested use | A local baseline for short classification and domain-supervised decisions; test question changes, option order and risk–coverage on your own traffic. | 可作为短文本分类和领域监督判断的本地基线；用实际流量测试问题变化、选项顺序和风险—覆盖率。 |
| Boundary | Qwen v1 data builders are not yet on main. Several dev evaluations have their train splits in the mix. E2B index predates a CUDA attention fix; Qwen v1 missing-image overconfidence worsens on POPE. E07/E08 remain historical, not current guarantees. | Qwen v1 数据构建器尚未进入 main；若干 dev 评测对应训练划分已用于训练。E2B index 先于 CUDA 注意力修复；Qwen v1 缺图时 POPE 过度自信恶化。E07／E08 保留为历史，不能当作当前保证。 |

**License note:** Repository and published adapter/head declare Apache-2.0. The release contains adapter/head files only; base weights load separately. Check base-model and dataset terms separately.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Strands Decider repository](https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/README.md); [Strands Decider architecture](https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/docs/architecture.md); [Strands Decider v19 experiment configuration](https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/configs/experiments/v19.yaml); [Strands Decider evaluation and limitations](https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/evaluation/README.md); [Strands Decider experiment record](https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/research/README.md); [Strands Decider original and AWS retrain results](https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/evaluation/results.md); [Strands Decider published v19 adapter card](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v19/blob/bb282d786bc251fd4e3068de3ada9ddbb38127cd/README.md); [Strands Decider published adapter provenance](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v19/blob/bb282d786bc251fd4e3068de3ada9ddbb38127cd/provenance.json); [Strands Decider v21 release and same-host seed results](https://github.com/strands-labs/strands-decider/blob/3e94e9d84c620ed5a95f1a3310c3decb971e261c/evaluation/results.md); [Strands Decider released v21b recipe](https://github.com/strands-labs/strands-decider/blob/3e94e9d84c620ed5a95f1a3310c3decb971e261c/configs/experiments/v21b.yaml); [Strands October 9 v1 releases](https://github.com/strands-labs/strands-decider/blob/0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534/CHANGELOG.md); [Strands Qwen3.5 / Gemma 4 v1 results](https://github.com/strands-labs/strands-decider/blob/0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534/evaluation/results.md); [Strands Gemma 4 serving limits and attention fix](https://github.com/strands-labs/strands-decider/blob/0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534/docs/inference.md); [Strands Qwen v1 missing-image reliability](https://github.com/strands-labs/strands-decider/blob/0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534/docs/vision.md); [Strands dataset/source inventory](https://github.com/strands-labs/strands-decider/blob/0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534/data/sources.md)

<a id="pplx-decider"></a>
## Perplexity pplx-decider-v1-27b

[Project / model](https://huggingface.co/perplexity-ai/pplx-decider-v1-27b)

Qwen3.8-27B fine-tune with published weights and a custom typed-decision runtime, including image inputs.
Qwen3.8-27B 微调模型，公开权重与类型化判断运行代码，支持图像输入。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | 27B-class Qwen3.8 backbone; no independent tensor count. | 27B 级 Qwen3.8 骨干；未独立统计张量参数。 |
| Mechanism | Custom autojev DecisionModel returns option probabilities through choice, noul or score helpers; inference uses a saved temperature. | 定制 autojev DecisionModel 通过 choice、noul、score 函数返回选项概率；推理使用保存的温度。 |
| Training | Fine-tuned from Qwen3.8-27B; configuration records provenance hashes and temperature 2.207568. Hashes do not make the full training/calibration protocol reproducible. | 基于 Qwen3.8-27B 微调；配置记录来源哈希及温度 2.207568。仅有哈希不能使完整训练／校准过程可复现。 |
| Deployment | Public full weights and readout; card requests Python 3.12+ and CUDA with about 49 GiB for weights plus working memory. Custom inference example was read, not executed. | 公开完整权重与读出头；模型卡要求 Python 3.12+、CUDA，以及约 49 GiB 权重内存和额外工作空间。本次仅阅读推理示例。 |
| Suggested use | A self-hosted comparator for text/image judgments after task-specific validation. | 经具体任务验证后，作为文本／图像判读的自部署对照。 |
| Boundary | The card reports Perplexity API results; equivalence to local weights is unverified. Full training data, calibration validation and raw benchmark artifacts were not established. | 模型卡成绩来自 Perplexity API；与本地权重是否等价未验证。完整训练数据、校准验证及原始评测产物尚未确证。 |

**License note:** Official model card declares Apache-2.0; public weights do not imply public training data.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Perplexity pplx-decider-v1-27b model card](https://huggingface.co/perplexity-ai/pplx-decider-v1-27b); [Perplexity local inference wrapper](https://huggingface.co/perplexity-ai/pplx-decider-v1-27b/blob/main/inference.py); [Perplexity released decision configuration](https://huggingface.co/perplexity-ai/pplx-decider-v1-27b/blob/main/decision_config.json)

<a id="ms-decision"></a>
## Microsoft-Decision-1

[Project / model](https://ai.azure.com/catalog/models/Microsoft-Decision-1)

Hosted Qwen3.5-9B post-training for bounded option scoring.
托管的 Qwen3.5-9B 后训练模型，对有限选项评分。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | 9B-class backbone, author described. | 作者描述为 9B 级骨干。 |
| Mechanism | Single-pass scoring; Foundry uses state and named noul/choice/score questions. | 单次前向评分；Foundry 接收 state 及命名的 noul／choice／score 问题。 |
| Training | Microsoft post-training; complete recipe, calibration splits and exact weights not verified. | Microsoft 后训练；完整配方、校准划分和精确权重未核实。 |
| Deployment | Foundry model version 1 and OpenRouter; no public weights verified. | Foundry 模型版本 1 及 OpenRouter；未核实公开权重。 |
| Suggested use | Compare classification, routing and rubric judgments. | 比较分类、路由和按标准评分。 |
| Boundary | Vendor comparisons lack audited item-level artifacts; familiar-task calibration need not transfer. Wording and safety errors remain. | 厂商比较缺少已审计的逐项产物；熟悉任务的校准不保证迁移，措辞与安全判断仍可能出错。 |

**License note:** Hosted service terms; Qwen backbone availability does not make the Microsoft checkpoint open-weight.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Microsoft-Decision-1 launch, 2026-10-09](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/); [Microsoft Foundry decision API and limitations](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision)

<a id="openai-decisions"></a>
## OpenAI Decisions API / GPT-6 Luna

[Project / model](https://developers.openai.com/api/docs/guides/decisions)

Public-beta typed judgment API for text and images.
面向文本与图像的类型化判断 API，处于公开测试。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Not established by the guide. | 指南未确立参数规模。 |
| Mechanism | POST /v1/decisions: input plus named predicate/choice/score questions; answers is an array. | POST /v1/decisions：input 加命名的 predicate／choice／score 问题；answers 为数组。 |
| Training | No audited recipe or held-out calibration protocol. | 未取得已审计配方或独立留出校准流程。 |
| Deployment | Only gpt-6-luna supported in the reviewed beta; paid hosted service. | 所核测试版仅支持 gpt-6-luna；付费托管服务。 |
| Suggested use | Managed classification, routing and ordinal scoring. | 托管分类、路由与有序评分。 |
| Boundary | Refusal is a separate answer variant, not calibrated abstention. Confidence needs target-task validation; training and serving identity are undisclosed here. | 拒答为单独返回类型，不等于校准后的拒判；confidence 需在目标任务验证，训练与服务身份尚未披露。 |

**License note:** Proprietary hosted API; no public-weight license established.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [OpenAI Decisions public beta guide](https://developers.openai.com/api/docs/guides/decisions)

<a id="drex"></a>
## Nace Drex v1.5

[Project / model](https://github.com/nace-ai/drex-decision-models)

MiMo-V2.6-Distill-Qwen-9B backbone with a Kev pointer head and public-weight release links.
MiMo-V2.6-Distill-Qwen-9B 骨干加 Kev pointer head，提供公开权重发布链接。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Approximately 9B, author described; memory depends on context and precision. | 作者描述约 9B；内存随上下文和精度变化。 |
| Mechanism | One pass per question; pointer head scores supplied noul/choice/score options. Forked llama.cpp shares the encoded state. | 每题一次前向；pointer head 对 noul／choice／score 选项评分，定制 llama.cpp 共享状态编码。 |
| Training | Official benchmark training splits plus procedural data; full training/calibration artifacts unverified. | 官方基准训练划分加程序生成数据；完整训练／校准产物未核实。 |
| Deployment | Python CUDA and Nace llama.cpp/Ollama forks; default 16384, configurable maximum 131072 tokens for state plus one question. HF card/weight hash not obtained. | Python CUDA 及 Nace 的 llama.cpp／Ollama 分支；状态加一题默认 16384、可配置最大 131072 token，未取得 HF 模型卡／权重哈希。 |
| Suggested use | Local candidate for text/JSON decisions, including long inputs. | 本地文本／JSON 判断候选，可测试长输入。 |
| Boundary | Benchmark training splits are used; results are not unseen-domain zero-shot. Public Index 0.3.1 leaders fall inside its tie band. Small runner checks do not establish broad parity. | 使用基准训练划分，不能视为未知领域零样本；公开 Index 0.3.1 前列处于平局带内，小规模运行器核对不证明普遍等价。 |

**License note:** Code Apache-2.0; weights use modified Nace.AI Open RAIL-M with commercial thresholds, competitor exclusions and use restrictions. Public access does not imply unrestricted open source.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Drex v1.5 release and public evaluation](https://github.com/nace-ai/drex-decision-models/blob/5c3d2220713c732a6820c4cdda51c7c38db991f5/models/drex-v1.5/README.md); [Drex local context limits](https://github.com/nace-ai/drex-decision-models/blob/5c3d2220713c732a6820c4cdda51c7c38db991f5/docs/context-length.md); [Drex v1.5 modified Open RAIL-M license](https://github.com/nace-ai/drex-decision-models/blob/5c3d2220713c732a6820c4cdda51c7c38db991f5/models/drex-v1.5/LICENSE); [Nace Drex training-overlap disclosure](https://www.nace.ai/drex)

