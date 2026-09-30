# Model cards / 模型卡

[Home](../README.md) · [中文首页](../README.zh-CN.md) · [Evidence](evidence.md)

Source review: 2026-09-30. These are source-backed descriptions and curatorial use cases, not production certifications.

`Unknown` is intentional. An inspected source revision does not identify the deployed weight revision. Language support, licenses and resource requirements must be checked for the exact artifact. Recorded weight identifiers are source-reported unless a local binary verification is explicitly documented; recording an identifier is not a claim that the weights were downloaded or hashed here.

<a id="jev"></a>
## Jev / TypeSafe

[Project / model](https://typesafe.ai)

Hosted typed judgments: probabilities over supplied choices, propositions and ordinal rubrics.
托管的结构化判断服务：对选项、命题与有序评分标准输出分布。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Not publicly established by the reviewed material. | 核对的公开资料未明确参数规模。 |
| Mechanism | Proprietary decision model; public API is more inspectable than its internals. | 专有判断模型；接口可查，内部实现公开程度有限。 |
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
| Boundary | Do not mix base and specialized scores. The typed checkpoint currently discloses training/calibration overlap and inherited-temperature conflicts. | 不可混用基础版与专项版成绩；专项卡明确披露训练与校准数据重叠及温度配置冲突。 |

**License note:** Reviewed family/specialist cards declare Apache-2.0; verify each selected artifact.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Laya model family](https://huggingface.co/convaiinnovations/laya); [Laya Typed-Decisions model card](https://huggingface.co/convaiinnovations/laya-typed-decisions)

<a id="kev"></a>
## Kev

[Project / model](https://github.com/jaredpalmer/kev)

Qwen-based adapters and a dynamic pointer head for typed decisions, with training and serving tools.
Qwen 骨干、适配器及动态 pointer head，配套类型化判断训练和部署工具。

| Dimension | English | 中文 |
| --- | --- | --- |
| Scale | Released family spans 0.8B, 4B, 9B and 27B; inspect the exact backbone/card. | 公开系列覆盖 0.8B、4B、9B、27B；须核对具体骨干与模型卡。 |
| Mechanism | Dynamic option readout on a language-model backbone; several model sizes. | 在语言模型骨干上动态读出选项分数；提供多个规模。 |
| Training | Supervised cross-entropy, LoRA and post-hoc temperature calibration. | 监督交叉熵、LoRA 与事后温度校准。 |
| Deployment | Open implementation and published checkpoints; the underlying backbone is still required. | 公开实现及检查点；部署仍需基础模型。 |
| Suggested use | An inspectable starting point for domain-supervised decision models. | 可检查、可微调的领域监督判断实验底座。 |
| Boundary | New-source development, held-out tests and trained-source scores are distinct. Adapter size is not deployment memory. | 新来源开发集、最终测试集与已训练来源成绩不同；适配器大小不是部署内存。 |

**License note:** Repository describes Apache-2.0; confirm adapter and backbone terms separately.
**Recorded weight identifier:** Unknown / not pinned

**Sources:** [Kev repository](https://github.com/jaredpalmer/kev/blob/2855ba2a55a80579176a459f78b95d03548cabb5/README.md); [Kev-4B model card](https://huggingface.co/jaredpalmer/kev-4b)

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
| Mechanism | A local GGUF yes/no model returning P(yes), without generating a text answer. The reviewed sources do not establish the submitted MiniCPM5 base, 17-layer count or exact readout implementation. | 本地 GGUF 是非模型，返回 P(yes) 而不生成文本答案。本次核读资料未确证投稿所述 MiniCPM5 基座、17 层结构或确切读出实现。 |
| Training | Training recipe, dataset and base-checkpoint provenance were not established by the reviewed sources; no independent training reproduction. | 核读来源未确证训练配方、数据集和基座检查点来源；没有独立训练复现。 |
| Deployment | The v2 release lists q4_k_m (619,289,280 bytes) and q8_0 GGUF assets. Documentation describes offline CPU use via llama.cpp. Listed hashes are publisher/API metadata, not local binary verification. | v2 发布页列出 q4_k_m（619,289,280 字节）和 q8_0 GGUF 权重，文档说明可通过 llama.cpp 在 CPU 上离线运行。记录的哈希来自发布方/API 元数据，未经本地下载核验。 |
| Suggested use | Experiment with CPU-local reading and triage questions; put the full policy in `instructions` and validate behavior on your own labeled cases. | 用于探索 CPU 本地文本判读与分流；将完整规则写入 `instructions`，并用自己的标注样例验证行为。 |
| Boundary | Yes/no only: `choice` and `score` return 422, and the jevos documentation says `criteria` is accepted but ignored. Wire-format compatibility is not semantic equivalence. Arithmetic/date errors and benchmark sensitivity are author-reported; old README results do not identify v2 performance. | 仅支持是非判断：`choice`、`score` 返回 422，jevos 文档说明 `criteria` 虽被接受却不参与判断。接口格式兼容不等于语义等价。算术、日期错误及评测敏感性由作者自报；旧版 README 的成绩不能代表 v2。 |

**License note:** Repository LICENSE is MIT; reviewed release metadata does not separately establish base-weight license provenance.
**Recorded weight identifier:** 3cbf010ce06cba932af73346ee683ee98d375dc284c029967eb418472a4993f3

**Sources:** [jevos pinned README and runtime documentation](https://github.com/feder-cr/jev/tree/9e7d9e8a24e9605bec249045a39df91ff2b58b0d); [jevos-v2 release and asset metadata](https://github.com/feder-cr/jev/releases/tag/jevos-v2); [jevos repository README](https://github.com/feder-cr/jev/blob/eb74cf78e5377e85fcaa76f6ebc9f82e8b517250/README.md)

