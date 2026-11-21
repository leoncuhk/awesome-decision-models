# Awesome Decision Models [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**AI 系统中有界决策的模型、方法与证据，按企业大模型应用真正面对的问题组织。**

[English](README.md) · [问题地图](#problem-map) · [落地手册](#playbooks) · [领域图谱](docs/landscape.md) · [模型卡](docs/models.md) · [证据台账](docs/evidence.md) · [方法论](docs/methodology.md)

决策模型由 TypeSafe 的 Jev 于 2026 年 9 月带火：对给定选项**一次前向输出类型化概率**，不生成文本。新东西是这个输出合同：它让有界判断可以计价、校准、设门槛。本仓只回答一个问题：**对一个具体决策，哪种方法能以可接受的风险和完整成本得到可接受的结果？**

核查批次 2026-11-21：92 项资源，35 个核心模型族，45 条证据记录。仅做来源审阅，**尚无本仓独立复现**。收录不代表推荐。

## 仓库怎么组织

| 层 | 回答什么 | 位置 |
| --- | --- | --- |
| 问题 | 知道什么、不知道什么、有多确定 | [problems/](problems/)：一个问题一个文件，含判断、证据、反证、开放实验 |
| 落地 | 企业里怎么做 | [playbooks/](playbooks/)：通用流程加场景手册 |
| 查阅 | 查事实 | [领域图谱](docs/landscape.md)，以及生成的[模型卡](docs/models.md)、[证据](docs/evidence.md)、[来源](docs/sources.md) |
| 规则 | 证据怎么判 | [方法论](docs/methodology.md)、[贡献规则](CONTRIBUTING.md) |

<a id="problem-map"></a>
## 问题地图

成熟度：**共识**＝多来源、含第三方对照；**有据**＝有对照但条件窄；**开放**＝缺关键证据。

| | 问题 | 当前判断 | 成熟度 |
| --- | --- | --- | --- |
| **判断本身** | [P01 输出合同与读出](problems/P01-output-contract.md) | 价值在合同而非新智能；读出头选择影响小 | 有据 |
| | [P02 适配的学习信号](problems/P02-learning-signal.md) | 直接 CE/BCE 监督是默认；RL、蒸馏、软标签须证明增量 | 有据 |
| | [P03 读一次还是先推理](problems/P03-read-or-reason.md) | 差距来自推理而非规模；把推理外包给参考答案往往更省 | 开放 |
| **概率到决策** | [P04 confidence 语义与服务保真](problems/P04-confidence-fidelity.md) | confidence 只是接口字段；按任务、返回对象、服务链路重新校准 | 共识 |
| | [P05 策略级风险认证与漂移](problems/P05-policy-risk.md) | 认证接受策略而非单题置信度；漂移后保证失效 | 理论共识／实证开放 |
| | [P06 缺选项与候选覆盖](problems/P06-candidate-coverage.md) | softmax 发现不了“全错”；NONE 在困难负例下崩溃 | 有据 |
| **系统集成** | [P07 读对了仍然做错](problems/P07-state-and-action.md) | 多数错误在状态与动作合同，不在读出 | 有据 |
| | [P08 技能与路径的动态加载](problems/P08-skill-loading.md) | 问题在选错而非上下文长度；优化带回退的加载召回 | 有据 |
| | [P09 System-1 作评审与评测层](problems/P09-judge-layer.md) | 低成本一级评审＋升级；最先成熟的落地点 | 有据 |
| | [P10 部分反馈与异质修复动作](problems/P10-repair-actions.md) | 追问、补证、扩候选、转人是不同干预；研究前沿 | 开放 |
| **多模态** | [P11 多模态判断的后训练](problems/P11-multimodal.md) | 视觉常常没有真正参与训练；先验证视觉路径再比质量 | 有据 |
| **选型** | [P12 评测碎片化与选型经济学](problems/P12-benchmarks-and-selection.md) | 名次不是选型信号；按许可、可训练性、硬件、服务保真准入 | 共识 |

<a id="playbooks"></a>
## 落地手册

| 手册 | 适用场景 |
| --- | --- |
| [通用流程](playbooks/decision-pipeline.md) | 任何企业决策：合同 → 方法与底座 → 数据 → 训练 → 验收 |
| [多模态后训练](playbooks/multimodal-posttraining.md) | 截图加意图标签；本地 Mac 训练；G0–G4 关卡 |
| [Skill 路由选择器](playbooks/skill-routing.md) | 几十个技能的服务 Agent；选择器训练、分阶段实验 H1–H6 |

## 核心模型

下表只列机制和建议实验；版本边界、许可与限制见[模型卡](docs/models.md)。不做混合排行：零样本、微调与 Best-of-N 回答的是不同问题。

| 模型 | 机制 | 建议实验 |
| --- | --- | --- |
| [Jev / TypeSafe](https://typesafe.ai) · [模型卡](docs/models.md#jev) | 托管的结构化判断服务：对选项、命题与有序评分标准输出分布。 | 可作为托管类型化判断对照或冻结的语义特征提取器；与监督基线比较时统一任务与标签规则。 确定性业务规则由代码执行，语义判断单独验证。 |
| [Laya classic encoders (package 0.5 defaults to Vega)](https://github.com/NandhaKishorM/laya) · [模型卡](docs/models.md#laya) | 经典421M／322M编码器检查点及动态选项头；包0.5默认已转为独立Vega冻结reader引擎，使用经典模型须显式选择。 | 显式选择经典encoder作低资源监督对照；Vega拟合头学习另立假设、基线及保留集验收。 |
| [Kev](https://github.com/jaredpalmer/kev) · [模型卡](docs/models.md#kev) | Qwen 骨干与动态 pointer head 的类型化判断系列；Kev 1.0 将现有检查点固定为发布基线。 | 可检查、可微调的领域监督判断实验底座。 |
| [Contrastive Language Models (CLM)](https://github.com/Contrastive-LM/CLM) · [模型卡](docs/models.md#clm) | 冻结语言模型编码器，分别表示状态与动作，再用可训练投影头匹配。 | 适合候选可复用的工具目录、排序及领域 Best-of-N 选择。 |
| [Bespoke Nimble](https://github.com/bespokelabsai/nimble) · [模型卡](docs/models.md#nimble) | 开放Qwen3.5-9B监督判断adapter，与后续Nimble托管v4／v4.1服务分别识别。 | 适合证据敏感的判断，也可借鉴最小差异训练样本。 |
| [GLiNER2.5-Decide](https://huggingface.co/fastino/GLiNER2.5-Decide-1B) · [模型卡](docs/models.md#gliner-decide) | 通过运行时标签与多个判断头实现模式条件化的本地分类。 | 适合轻量业务分类；跨字段约束需核对具体运行库支持。 |
| [GLiClass (v4 family; v4.1 Edge metadata only)](https://github.com/Knowledgator/GLiClass) · [模型卡](docs/models.md#gliclass) | 标签条件分类系列：v4有decoder-KV／label评分及多模态Qwen变体；v4.1 Edge目前属于文档不完整的产物。 | 作为动态意图／标签分类对照，先选单标签或多标签语义，再量具体任务的校准。 |
| [jevos (current v5; historical v2)](https://github.com/feder-cr/jev) · [模型卡](docs/models.md#jevos) | 本地CPU类型化判断，采用Jev形状的API：v5文档在是非之外加入choice和早期score支持，发布OpenVINO INT8及GGUF产物。 | 作为短规则／分流判断的CPU推理对照；考虑适配前，先验证各题型与精确发布产物。 |
| [Clef / Clef-Flash / Clef-Omni](https://huggingface.co/Cloudflare/clef) · [模型卡](docs/models.md#clef) | Cloudflare类型化判断系列：稠密Clef／Flash及10月9日Clef-Omni用联合schema评分；Clairic是独立提取系列。 | 按任务所需文本／图像／音频／视频证据，在相同风险与完整系统成本下比较有界判断。 |
| [Strands Decider (v1 pointer / v2 code readout)](https://github.com/strands-labs/strands-decider) · [模型卡](docs/models.md#strands-decider) | Qwen／Gemma判断系列：v1为adapter与pointer发布物，11月17日Gemma4 E2B v2为合并权重与答码读出；训练及服务合同不同。 | 在相同有界文本判断上比较v1与v2；选配方前核对领域训练从何种权重开始及导出后的推理路径。 |
| [Perplexity Decider (current v1.3; archival v1 / v1.1 / v1.2)](https://huggingface.co/perplexity-ai/pplx-decider-v1.3) · [模型卡](docs/models.md#pplx-decider) | v1.3类型化判断及可选span定位系列；27B Qwen3.8与蒸馏Flash 4B Qwen3.5，早期版本分别保留。 | 经具体任务验证后，作为文本／图像判读的自部署对照。 |
| [Microsoft-Decision-1.1](https://ai.azure.com/catalog/models/Microsoft-Decision-1.1) · [模型卡](docs/models.md#ms-decision) | Gemma4托管类型化判断，GA且支持图像。 | 比较分类、路由和按标准评分。 |
| [OpenAI Decisions API / GPT-6 Luna](https://developers.openai.com/api/docs/guides/decisions) · [模型卡](docs/models.md#openai-decisions) | 面向文本／图像的GA类型化判断API。 | 托管分类、路由与有序评分。 |
| [Google Gemini Decision 1 / Decisions API](https://aistudio.google.com/docs/models/gemini-decision-1) · [模型卡](docs/models.md#gemini-decision-1) | 11月11日发布的托管模型，支持文本、图像、音频、视频和PDF判断，在共享输入上隔离各问题。 | 在相同证据、风险约束和完整成本下比较多模态分流、媒体规则检查与路由。 |
| [Nace Drex v1.5 / v2.0 / Max v1](https://github.com/nace-ai/drex-decision-models) · [模型卡](docs/models.md#drex) | Drex 系列：文本 pointer-head v1.5／v2.0，加上独立 255-code 读出的多模态 dense 27B Max v1。 | 比较本地文本／JSON 与 Max CUDA 图像判断；跨版本比较须匹配精度、读出、证据和上下文。 |
| [vLLM-SR D3 / Turbo / Ultra / D3.1-nano](https://huggingface.co/collections/vllm-sr/decision-30) · [模型卡](docs/models.md#decision3) | 多模态类型化判断系列，经典逐题、Turbo／Ultra共享state及11月12日D3.1-nano发布物须分别识别。 | 固定文本／图像／视频判断合同对比；将小型D3.1-nano作为独立能力候选、Ultra作为大模型参照，适配可行性另验。 |
| [Intern-Decision](https://github.com/internlm/Intern-Decision) · [模型卡](docs/models.md#intern-decision) | Qwen3.5 多模态 0.8B／2B／4B 系列，在一个因果 masked assistant skeleton 中评分多个类型化字段。 | 与每题独立模型比较多字段成本和字段／顺序敏感性，测试基于图像证据的判断。 |
| [Verdict / OpenJev](https://github.com/Heman10x-NGU/Verdict-open-jev) · [模型卡](docs/models.md#verdict) | 151M ModernBERT／GLiClass 候选分类器，含显式证据不足选项及 per-K 校准。 | 轻量意图分类与缺少正确选项测试；核对实际服务概率和评测 renderer／校准器。 |
| [StartLux-Decision v1.1 (Instant / AutoThink)](https://github.com/StartLuxLabs/StartLux-Decision) · [模型卡](docs/models.md#startlux-decision) | 使用 LM 选项字母读出：Instant 的 full-attention 提示双向，因果 AutoThink 按需推理并混合两次分布。 | 在证据充分的判断上以相同风险与总成本比较一次读出和选择性计算；商业使用权重需另获授权。 |
| [Baseten mammoth-1 / elephant-1 / joey-1](https://huggingface.co/baselabs/mammoth-1) · [模型卡](docs/models.md#baseten-decision) | 基于Qwen的27B／9B／2B类型化判断系列，共享证据前缀、分别读问题；Joey是10月新增的小型号。 | 在2B／9B／27B之间做同合同独立问题对照，将公共suite与复制指数评测分开。 |
| [Jeffan (31B-1710 / 4B-2010 / 9B and 27B-1211)](https://huggingface.co/tattrongvu/Jeffan-31b-1710) · [模型卡](docs/models.md#jeffan) | 文本判断发布物采用不同计算策略：较早Gemma31B选择性重读，较新Qwen9B／27B为双向答码读出并可循环中层。 | 固定loop／重读策略及完整请求成本比较有界文本判断，再单独验证领域／语言迁移。 |
| [SII-Decision (4B / 27B)](https://github.com/amazingljy1206/SII-Decision) · [模型卡](docs/models.md#sii-decision) | 将推理后概率自蒸馏为零生成类型化判断；公开4B与27B产物。 | 作为能力与蒸馏参照；发布检查点评测与企业领域适配分别验证。 |
| [GLiDE / Fastino](https://fastino.ai/blog/glide-decision-model-family) · [模型卡](docs/models.md#glide) | 五尺寸开放权重判断系列，并有面向客户数据的原生训练API。 | 新增小模型／读出对照；企业数据可获准上云时比较托管领域适配。 |
| [Liquid d1 / d1.2](https://docs.liquid.ai/lfm/models/decision-models) · [模型卡](docs/models.md#liquid-d1) | 开放d1-2B／Omni-2B与独立托管d1.2／ultra产品。 | 研究小型非Qwen实现及多标签合同，托管与本地产物分别比较。 |
| [Mapika Decider](https://github.com/Mapika/decider) · [模型卡](docs/models.md#mapika-decider) | 有监督训练及数据构造器的开放判断系列；此前已有研读来源，但缺核心索引条目。 | 比较可审查的监督实现与逐题型校准；反馈匹配时才研究环境学习。 |
| [RSI-Jev v7.0-VL](https://github.com/Shanghua-Gao/RSI-Jev) · [模型卡](docs/models.md#rsi-jev) | 公开完整训练代码的Qwen判断实现，另有截断3B衍生物。 | 优先审实现并做小规模自有标签对照，保留简单读出／LoRA基线。 |
| [Jeff 1.1 / j-geuter](https://github.com/j-geuter/Jeff) · [模型卡](docs/models.md#jgeuter-jeff) | 与Jeffan不同的公开判断训练实现；发布权重／数据有非商用限制。 | 参考数据／训练机制；商用应从许可合适底座与获授权自有数据起训。 |
| [JAD-S1 v0.5](https://huggingface.co/DreamBlooms/JAD-S1-7B-A1B-v0.5) · [模型卡](docs/models.md#jad) | 基于扩散／MoE、单mask读出的闭集判断adapter。 | 任务有需要时作为不同骨干／读出的研究对照。 |
| [H2O Lightning 4B](https://huggingface.co/h2oai/h2o-lightning-4b) · [模型卡](docs/models.md#h2o-lightning) | 开放Qwen4B类型化判断引擎；属于补录，非11月20日新权重。 | 固定协议／提示配置后作为小型类型化推理对照。 |
| [MNN-Pocket-0.3B-Dec](https://huggingface.co/taobao-mnn/MNN-Pocket-0.3B-Dec) · [模型卡](docs/models.md#mnn-pocket-dec) | 小型中英Choice／命题／有序评分pointer-head发布包。 | 极小中文读出／成本对照，同时保留已训多语encoder。 |
| [IBM Granite Switch / decision adapter](https://huggingface.co/blog/ibm-granite/granite-switch-4-1) · [模型卡](docs/models.md#granite-switch) | Granite4.1上可复用的decision adapter，与聊天、guard及ASR并列。 | 较大底座确有必要时，研究判断／聊天共用及cache-aware adapter。 |
| [Ant Digital LingDT-Decision-1.0](https://maas.antdigital.com/models/modelservice-1792325631780001741) · [模型卡](docs/models.md#ant-lingdt) | 托管类型化判断服务，原生支持问题依赖DAG。 | 国内托管合同／依赖参考，另验访问与数据治理。 |
| [Respan Span-02](https://www.respan.ai/blog/introducing-span-2) · [模型卡](docs/models.md#span-02) | 使用专用量化Rust／CUDA引擎、可选推理的开放判断服务产物。 | 研究自托管推理与预算推理，作为独立服务策略对照。 |
| [Decisio tuned v3 / Tachara AI](https://github.com/aminry/decisio) · [模型卡](docs/models.md#decisio) | 11月20日发布的Gemma12B适配权重，含calibrated／commit策略及多精度部署包。 | 新增服务／读出对照；同合同分验calibrated、commit及计算器。 |
| [Valen-Decision1.5](https://github.com/Valen-Team/Valen) · [模型卡](docs/models.md#valen-decision) | 多模态类型化判断系列，有从已发布native检查点领域训练的入口，与ONNX／GGUF／ANE转换分开。 | 在兼容硬件上优先纳入可审查的native续训LoRA对照，保留原版及直接CE控制。 |

## 值得保留的基线

新的训练名称不会让熟悉的基线过时。

- **[SetFit](https://github.com/huggingface/setfit)** — 少样本句向量适配，再训练分类头。
- **[Qwen3-Reranker](https://huggingface.co/Qwen/Qwen3-Reranker-0.6B)** — 面向查询与文档的任务专用重排。
- **[Outlines](https://github.com/dottxt-ai/outlines)** — 为普通语言模型提供受约束结构化输出。
- **[TabICLv2](https://arxiv.org/abs/2602.11139)** — 用于表格分类与回归的基础模型。
- **[FluidUse / decision-model Core ML deployment](https://github.com/FluidInference/FluidUse)** — Apple 部署资源，含原生 Swift manager 与 Python 辅助 Core ML bridge，支持 Decision 3.0 等。
- **[Semantic features + supervised predictor](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery)** — LLM 提议问题，Jev 将文本转成语义特征，再由监督 CatBoost 预测任务标签。
- **[ezjev text candidate-logit LoRA](https://github.com/everettjf/ezjev/tree/8b3d88957c0795bea160c8fbc9c6d2a54b051136)** — 可检查的逐题候选 CE＋Brier、回放及温度拟合，训练路径使用 Qwen3.5 文本输入。
- **[decision-pacman decision distillation](https://github.com/grapeot/decision-pacman/tree/593ed1f59f4f97ad0bda7287ff304e9667360089)** — 用文本状态的教师／模拟器标签训练小型候选分布 LoRA 学生。
- **[Qwen VLM image-supervised SFT / LoRA](https://github.com/QwenLM/Qwen3-VL/blob/96588727e44c78b25ba03ea03b8e12f7e64fd0da/qwen-vl-finetune/README.md)** — 可查图像监督路径：QwenVL 官方、ms-swift Qwen3.5，以及供 Mac 实验的固定 MLX-VLM 图像条件语言 adapter。
- **[DFIP / Decision-Focused Inference Path](https://arxiv.org/html/2610.36804v1)** — 配对原生基线系统研究，分别审计驻留加速、对外答案字段与外部到达流量。
- **[DICE / Direct Item Choice Estimation](https://arxiv.org/html/2610.34124v1)** — 监督式商品选择，以候选隔离共享前缀注意力和单独校准的置信度进行推荐。
- **[Clairic / Clairic-Flash (typed extraction)](https://blog.cloudflare.com/open-clairic/)** — 相邻的类型化提取／估计系列：11月18日改版用并行slot自回归提取及专用数值头，与Clef闭集判断分开。
- **[Unsloth decision-model training (FastDecisionModel / DecisionTrainer)](https://unsloth.ai/docs/basics/train-your-own-decision-model-with-unsloth)** — 通用训练框架：把可微调 LLM（含 Qwen3.5 VLM）训练成 Clef 式联合头决策模型，自带校准、合并导出、本地兼容 Jev 的 Decision API，以及 Apple Silicon（MLX）LoRA 路径。

## 路由与从结果中学习

- **[RouteLLM](https://github.com/lm-sys/RouteLLM)** — 利用学习到的信号在强模型与便宜模型间路由。
- **[LLMRouter](https://github.com/ulab-uiuc/LLMRouter)** — 构建和比较路由策略的研究基础设施。
- **[Vowpal Wabbit](https://github.com/VowpalWabbit/vowpal_wabbit)** — 在线学习与上下文老虎机工具。
- **[Parlant rule matching / Jev integration](https://github.com/emcie-co/parlant)** — 已核CX引擎源码：共享状态批量判断逐规则命题，再解析声明的规则关系。
- **[Modem Smart Triggers](https://modem.ai/blog/smart-triggers)** — 实施者产品案例：精确过滤与语义条件控制事件是否启动完整Agent。
- **[Enterprise multi-turn intent learning (Amazon study)](https://aclanthology.org/2026.customnlp4u-1.8/)** — 以证据解释和自检改善教师标签，再为真实电商对话训练独立的领域／意图／问题RoBERTa分类器。

## 可靠性

- **[MAPIE](https://github.com/scikit-learn-contrib/MAPIE)** — 预测集合、不确定性与保形风险工具。
- **[Calibration and Risk-Budgeted Decisions with System One Models](https://arxiv.org/html/2610.19811v1)** — 预印本将概率校准与固定序列 LTT 对二元风险预算策略的认证分开。
- **[RouteGuard / Cost-Aware Abstention](https://arxiv.org/html/2610.31657v1)** — 按校准集选成本敏感工单路由，分开概率校准和错误区分能力。
- **[Rep2Act / VAD-R](https://arxiv.org/html/2609.32653v1)** — 证据缺口标注及可答性到动作的对齐；本次新收录 9 月 26 日预印本。

## 评测

- **[HF-hosted Decision Index (archival releases and live board)](https://huggingface.co/spaces/multimodalart/jev-decision-index)** — 具有明确聚合规则的较广覆盖决策评测指数。
- **[Nimble public evaluations](https://github.com/bespokelabsai/nimble/blob/62076b4f2d365b5879dafcf7f6dd072a1fe76df7/docs/PUBLIC_BENCHMARKS.md)** — 人工参考标签子集、配对比较及校准报告。
- **[Decision-model benchmark](https://github.com/nibzard/decision-model-benchmark)** — 用于判断模型比较的第三方代码与协议。
- **[Financial-document decision tests](https://insights.ml4trading.io/p/testing-jev-on-financial-documents)** — 原评测者比较 Jev 与监督文本／TF-IDF 模型，分别测试财报变化、8-K 标签和 SEC 后续问询。
- **[MIRE / WWW2025 multimodal intent competition](https://github.com/liujunwen23/MIRE/tree/d101287af90d114c5bf0cbfbd56fe9c52358e3bb)** — 并列的 23 类场景／23 类对话意图任务、官方 full-SFT 基线，以及有来源的金银铜方法和复赛成绩。
- **[DecisionPivot v1.1](https://huggingface.co/datasets/startlux-models/DecisionPivot/tree/b6a65d303f3f8689d293869aff3db41f944984c6)** — 13 个生成对比家族、程序标签及公开生成／求解／评分资产，另有复用公共任务参考轨。
- **[Artificial Analysis Decision Index](https://artificialanalysis.ai/methodology/decision-index)** — 托管与开放决策模型指数；11月8日 v2 以 50×(1+准确率−Brier) 计分，把校准计入主分，私有数据占比升至 45%。
- **[Commit or Abstain? Missing Legal Authority](https://arxiv.org/html/2610.29961v1)** — 独立于模型提供商的评估，在构造 CaseHOLD 上揭示错误接受与不必要拒答的权衡。
- **[VLTest joint image-text testing](https://arxiv.org/html/2610.30794v1)** — 10 月 22 日方法以原始／仅改图／仅改文／联合四格对照，核查扰动是否保持预期答案。
- **[Beyond Ranking: calibrated relevance scoring](https://arxiv.org/html/2611.11480v1)** — 同候选相关性排序与留出集概率校准。
- **[System1 perturbation and question-interference audit](https://arxiv.org/html/2611.12521v1)** — 审计分布派生置信度、多题干扰及扰动解释。
- **[Decision models for RAG conflict typing](https://arxiv.org/html/2610.36915v1)** — 直接冲突分类、问题拆分与置信门控级联。
- **[Entity matching using decision models](https://arxiv.org/html/2610.34626v1)** — 零样本记录对匹配，比较提示、鲁棒性与级联。
- **[Jev time-series decision benchmark](https://arxiv.org/html/2610.33410v1)** — 评估序列输入、事件类别及方向预测。
- **[Confidence Is Not a Promise / Typed Deciders Audit](https://arxiv.org/html/2610.36311v1)** — 参考审计区分置信排序、选择性准确率承诺及其在分布变化下的失效。
- **[Entagl customer-routing replay](https://www.entagl.com/blog/typesafe-jev-benchmark-ai-decision-models)** — 实施者报告的标注决策与真实客服历史路由回放。
- **[JEVal v2](https://arxiv.org/html/2610.03935v2)** — 面向中英文多领域的局部类型化判断、推理边界与工作流组合评测。
- **[To Jev or Not to Jev (System-1 models as LLM judges)](https://arxiv.org/abs/2611.00505)** — 预先声明协议，在 11 个评审基准上比较 14 个 System-1 决策模型与 4 个生成式评审，覆盖参考答案引导、校准与注入指令鲁棒性。
- **[Reading Right, Acting Wrong (agent-loop decision diagnosis)](https://arxiv.org/abs/2610.18579)** — 对同一 agent 状态同时提问下一步动作与独立事实探针，区分“读错状态”与“读对仍选错”。

## 基础文献

阅读顺序：概率质量 → 弃权 → 转交执行者 → 风险控制。

- **[Strictly Proper Scoring Rules (2007)](https://doi.org/10.1198/016214506000001437)** — 为什么对数损失等适当评分规则以真实分布为目标。
- **[On Calibration of Modern Neural Networks (2017)](https://proceedings.mlr.press/v70/guo17a.html)** — 经验校准及事后温度缩放。
- **[Selective Classification (2017)](https://arxiv.org/abs/1705.08500v2)** — 带拒判的分类与风险／覆盖率权衡。
- **[Learning to Defer to an Expert (2020)](https://proceedings.mlr.press/v119/mozannar20b.html)** — 联合学习预测与向专家交接。
- **[Conformal Risk Control (2022; reviewed v4)](https://arxiv.org/abs/2208.02814v4)** — 在明确条件下校准风险控制程序。
- **[Non-Monotonic Conformal Risk Control (2026)](https://arxiv.org/abs/2602.20151v1)** — 将风险控制讨论扩展到非单调损失。
- **[Proper Scoring Rules: 2026 review](https://doi.org/10.1146/annurev-statistics-042424-050626)** — 近期关于估计与预测评估的适当评分综述。
- **[Causal Learning to Defer (AAAI 2026)](https://ojs.aaai.org/index.php/AAAI/article/view/39493)** — 研究存在隐藏混杂时的交接学习。
- **[Jev in the Wild (2026)](https://arxiv.org/abs/2609.30216)** — 基于 2,170 个公开 GitHub Jev 项目的数据驱动综述与分析，涵盖早期增长、应用领域及决策用途分布。
- **[Post-Rationale Distribution Optimization (PRDO v2)](https://arxiv.org/html/2609.38850v2)** — 为选择性预测优化每条采样推理之后的答案分布，以恰当评分规则为目标。

## 相关列表

- **[Awesome System One](https://github.com/andyrewlee/awesome-system-one)** — 最接近主题的生态列表，适合发现项目。
- **[Awesome Jev 中文](https://github.com/yzfly/awesome-jev-zh)** — Jev 生态的中文资料。
- **[Awesome LLM Routing and Cascading](https://github.com/ymoslem/awesome-llm-routing-cascading)** — 专门的路由与级联文献目录。
- **[Awesome Conformal Prediction](https://github.com/valeman/awesome-conformal-prediction)** — 专门的不确定性与保形预测资料。
- **[Awesome Martech AI](https://github.com/leoncuhk/awesome-martech-ai)** — 涵盖营销数据、智能、决策、激活和测量的资源及实践指南。

## 贡献

规范数据在 [`data/`](data/)；README、模型卡、证据和来源页由 `python3 scripts/render.py` 生成。新资料只有在改变某个问题的判断、证据或开放实验时才值得加入，见 [CONTRIBUTING](CONTRIBUTING.md)。变更记录见 [CHANGELOG](CHANGELOG.md)。

原创代码与整理文字采用 [MIT](LICENSE)；所链接的项目、权重、数据与论文保留各自许可。
