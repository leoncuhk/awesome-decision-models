# 决策模型领域后训练：平台与生产证据核查

核查日期：**2026-11-19**。范围：企业客服的分类、路由、升级、评分与拒判；只查公开一手资料，未登录控制台、申请授权、训练、推理或接触企业数据。文档可读不等于本账户已获服务权限；Git/Hugging Face 文本 revision 不等于已下载核验权重。

**结论：领域后训练已有可查路线，但不能把它们统称为“微调 Jev”。** TypeSafe 当前不提供客户权重适配；阿里有受限开放的托管 LoRA；Together 有普通语言模型 SFT 配方；Clef 有开放权重和人工协作代训服务。公开证据仍不足以证明“某企业用自己的客服数据训练 Jev 类模型，经过独立线上对照改善了客户结果”已普遍成立。

2026-11-20定向纠错：本页此前将Chinese-Jev行业权重统称planned，漏核了**10月18日已发布的CJ-Medical**；这不是当天新增。固定产物、许可证、Intern许可和StartLux／PPLX版本等后续事实见[逐项讨论核查](decision-model-discussion-fact-check-2026-11-20.zh-CN.md)。下方该行已修正；其余来源仍按各自核查日理解。

证据标记：**D**＝官方产品/接口文档；**A**＝模型作者离线实验/配方；**P**＝供应商或使用方报告实际生产使用，仍非独立审计；**I**＝本次据来源推断。所有性能数字均非 `reproduced_here`。

## 产品能力与训练契约

| 待核查说法 | 判定 | 应使用的表述与边界 | 一手来源 | 证据 |
|---|---|---|---|---|
| Jev 仍须等候名单，企业可微调专属 Jev | 前半过时，后半不成立 | 当前开放注册；Models 明说同一权重服务所有账户，不用客户数据作 fine-tune/LoRA。业务适配靠 state、规则、示例和代码组合。 | [注册帮助](https://help.typesafe.ai/articles/4519713419-how-do-i-create-or-activate-my-account-after-an-invitation-or-waitlist-approval)、[Customizing Jev](https://docs.typesafe.ai/models#customizing-jev) | D |
| Jev 仅文本、64k、255 选项、$0.042/M | 部分过时 | 1.14 已发布，默认请求64k/单题32k，Choice最多255项；输入还支持图像，图像/Box仍是实验状态。长上下文须显式开启至262k；输入价仍为$0.042/百万tokens、输出免费。 | [模型](https://docs.typesafe.ai/models)、[Choice](https://docs.typesafe.ai/primitives/choice)、[图像状态](https://docs.typesafe.ai/images)、[价格](https://help.typesafe.ai/articles/5187202169-how-much-does-jev-cost) | D |
| 能下载官方 Jev 权重，在 M5 上训练 | 未找到支持 | 本次官方文档/发布入口未发现 Jev 权重或本地训练包。不能从兼容 API 的其他模型反推 Jev 内部结构，更不能把 Kev/Tev 权重称为 Jev 权重。 | [TypeSafe 模型与定制契约](https://docs.typesafe.ai/models) | D＋I，缺公开产物 |
| `/v1/systemone` 已是事实标准，阿里/Ollama可无差别替换 | 表述过强 | 多家沿用该接口形状，可称生态兼容约定；未见正式共同规范/一致性认证。阿里原生API写Bearer，微调指南推理示例用裸key；本轮未实测两者是否都接受，不能概括成一律不用Bearer。Ollama支持取决于版本和模型，模型类型、概率、校准与图像合同仍须逐项验收。 | [阿里调用契约](https://help.aliyun.com/en/model-studio/decision-model-tuning-guide)、[Ollama 官方发布](https://ollama.com/blog/ollama-now-supports-jev-style-decision-models) | D＋I |
| 阿里 decision-model-preview 可领域后训练 | 成立，但有准入与版本限制 | 官方版本`decision-model-preview-2026-09-24`，方法`efficient_sft`＝LoRA；需客户经理开通。控制台限北京，OpenAPI另支持新加坡。预览模型仍迭代，文档建议高稳定性业务等待正式版。 | [官方微调指南](https://help.aliyun.com/en/model-studio/decision-model-tuning-guide) | D，未实测授权 |
| 阿里 soft label 自动解决校准，均匀目标等于可靠拒判 | 只支持训练建议 | 必填hard label、可选覆盖全部选项的概率target；示例用教师标注并调温，对不可判断输入设均匀target且不计accuracy。它不证明独立校准、OOD拒判或业务风险界限。问题ID/type/instructions/criteria变更须按指南重制数据/重训。 | [Soft labels / FAQ](https://help.aliyun.com/en/model-studio/decision-model-tuning-guide) | D；效果为服务方主张 |
| 阿里训练成本21元/小时、10139元/月 | 成本归属错误 | 这是MU5×1**部署**规格的按量/月租价；训练暂免token费用，教师生成数据另收费。不是任意本地/GPU训练的通用报价，也不是全流程总价。 | [Deployment / billing FAQ](https://help.aliyun.com/en/model-studio/decision-model-tuning-guide) | D，限当前页面/规格 |
| Clef：CE＋Brier、rank256 LoRA、RL partial reward/KL | 大部分有作者说明，KL细节未核验 | 公布冻结基座参数、联合训练head及rank256适配器，label-smoothed CE配Brier；RL阶段称对邻近序数给部分分、精确record给奖励，并加reference penalty。未见该文给出明确KL实现/系数，不能补写成已复现的完整RLCD配方。 | [Cloudflare训练说明](https://blog.cloudflare.com/clef-decision-models/#how-we-trained-clef) | A |
| Clef客服76.3/77/Jev76，CLINC97.43、BANKING94.20证明企业客服可用 | 数值有出处，含义须纠正 | 客服前三项为共识参考标签下的**Exact actions百分比**；后两项分别为CLINC150+OOS、BANKING77的**macro-F1百分数**。它们不是线上解决率、拒判覆盖或安全阈值；表格未提供可直接迁移的业务置信阈值。 | [Clef固定模型卡](https://huggingface.co/Cloudflare/clef/blob/171287b2571042abec9e7b99752aee58216b0ed0/README.md)、[发布表](https://blog.cloudflare.com/clef-decision-models/) | A，供应商比较 |
| Clef开放权重＝完整训练开源且M5可直接微调 | 不成立 | Clef/Flash确有Apache-2.0权重、joint head与专用运行代码；原始内部合成数据及完整训练过程并未由这些产物完整公开。卡片验证环境为CUDA/H200，不能据此承诺Apple MPS/MLX的训练或概率一致性。 | [Clef文件](https://huggingface.co/Cloudflare/clef/tree/171287b2571042abec9e7b99752aee58216b0ed0)、[Flash卡片](https://huggingface.co/Cloudflare/clef-flash/blob/22b75507981345858dd152fbd9a6f8c0c4068b0a/README.md) | D/A＋I |
| Cloudflare自助RL微调平台已全面开放 | 未获支持 | 发布说明提供FDE协作服务；自助训练/重新部署仍属后续目标，部分组件为work-in-progress，并征集design partner。未核验账户可用性、合同或统一价格。 | [RL service与fine-tuning服务](https://blog.cloudflare.com/clef-decision-models/#our-new-rl-service) | D，发布承诺/服务说明 |
| Together花$17就能在本地得到完整Jev | 错误合并了三件事 | $17/约25分钟是作者托管训练示例，另要部署专用端点，非含数据标注/评测/推理的总成本。官方仓库为普通Qwen LoRA SFT示例；Tev保留next-token LM head，按字母输出，不是Jev式非自回归运行时。 | [官方教程](https://www.together.ai/blog/how-to-train-your-own-jev)、[固定代码配方](https://github.com/togethercomputer/tev1/tree/1dde7782382c9f49d627153759b8d1deab426ce0) | A/D |
| Tev公开代码/权重所以商业本地训练已无缺口 | 有产物，许可与复现仍待核实 | 代码MIT；权重确实可取，但当前模型卡称微调权重发布许可尚在确定，不能套用基座Apache-2.0。配方为rank8、1epoch、2048序列示例；仓库承认实际上传数据与job精确设置仍待核验。开发评测不是新留出验收。 | [固定Tev模型卡](https://huggingface.co/togethercomputer/Tev1-4B-experimental/blob/0b7becf017daa0e5eb222f8ce7483c8c8259c52f/README.md)、[训练说明](https://github.com/togethercomputer/tev1/blob/1dde7782382c9f49d627153759b8d1deab426ce0/README.md) | D/A，非完整本地复现 |

## 哪些是企业生产证据

| 案例/说法 | 判定与正确范围 | 一手来源 | 证据 |
|---|---|---|---|
| Salesforce HyperClassifier/Koa证明企业会领域训练专门决策模型 | **支持这一方向。** Salesforce说明已把专门微调的HyperClassifier用于Agentforce路由且GA/默认使用；Koa是后续Gemma训练版本。26ms对约1.4s为组件级测量，不是端到端业务增量。它是平台方训练并服务客户，不证明客户可上传自身数据自助训练同一产品。 | [2026-07生产栈说明](https://www.salesforce.com/news/stories/cutting-inference-spend-by-right-sizing-models/)、[2026-11 Koa说明](https://www.salesforce.com/news/stories/koa-decisions-salesforce-decision-models/)、[Koa论文v2](https://arxiv.org/html/2609.36115v2) | P＋A，供应商自述 |
| Koa论文的企业路由结果是否证明客户后训练收益 | 论文v2在通用适配后，以587条脱敏生产路由记录作零样本评估；原记录因合同／隐私不公开。可参考匹配服务协议和生产来源的离线比较；不是在这587条上训练取得的增量，少样本encoder对照也不是充分调优的监督上限。 | [Koa论文v2](https://arxiv.org/html/2609.36115v2) | A，生产来源／离线 |
| Jack & Jill是否证明自有数据微调Jev有效 | 真实岗位／历史选择的离线配对，加供应商报告的生产接入；Jev使用共享权重，不是客户专属微调。可研究昂贵后续之前的廉价筛选及关键漏选；预测节省不是已兑现收益或招聘质量因果证明。数值与限制见[应用证据](decision-model-application-evidence.zh-CN.md)。 | [供应商案例](https://typesafe.ai/blog/jack-jill-jev-case-study)、[官方模型说明](https://docs.typesafe.ai/models) | P／A，供应商自述 |
| Entagl回放与个人Skill适配能否补足企业后训练证明 | Entagl未训练Jev且双方owner等状态不匹配；LayaStudio、pi-laya-skill-router等提供本地适配起点，但公开集、个人加载记录和教师标签不等于企业独立真值。前者核[客服实现审查](customer-service-implementation-review.zh-CN.md)，后者核[Mac实现示例](decision-model-posttraining-mac-recipe.zh-CN.md)。 | [Entagl回放](https://www.entagl.com/blog/typesafe-jev-benchmark-ai-decision-models)、[Skill实现](https://github.com/ericmjl/pi-laya-skill-router) | A，历史回放／实现 |
| Kev客服67.7%→73.6%是企业生产案例 | **不是。** 作者示例：三题、1050条生成记录、H100约15分钟；5%误差预算下经验覆盖34%→48%，不是SLA或真实人工替代率。400条实验的增益仍在噪声内。 | [固定作者配方](https://github.com/jaredpalmer/kev/blob/2074cc44256200bb37540103fa4572901faa10f3/skills/kev-finetune/README.md) | A，合成离线 |
| Kev CFPB 0.804→0.904是企业私有客服生产收益 | **不是。** 历史documents阶段：5219条公开投诉训练，测试936题，另有953题私有留出；同一CFPB来源及两套题型，标签经过AI裁定/人工抽查。当前卡已是后续版本，不能把历史差值当当前新实验，更不是线上客户结果。 | [历史固定卡957b91e](https://huggingface.co/jaredpalmer/kev-4b/blob/957b91e762e883935830246eeb02381f9d2694b6/README.md)、[当前卡](https://huggingface.co/jaredpalmer/kev-4b/blob/6cfce5c2fa4b4bd64026336ab649c5ca78857d52/README.md) | A，真实文本/离线同分布 |
| Audiala证明替换Jev路由必然提速 | **直接反例。** 使用方23分钟后回滚；65场景×3回归中稳定通过38→33，路由中位382→294ms，完整轮次8677→9262ms。保留较窄重排/缓存用途与回退。这是托管模型集成，未作客户权重训练；回归样本也不等于自然用户流量。 | [使用方生产复盘](https://audiala.com/blog/jev-in-production) | P，使用方报告含负结果 |

Salesforce另有[2025-11工程访谈](https://engineering.salesforce.com/solving-real-time-ai-classification-for-agentforce-how-single-token-prediction-delivers-30x-faster-agent-responses/)说明单token微调、KV缓存、fallback/回滚与教师共识验证；其页面显示“Nov20”，HTML元数据日期为2025-11-20，不应误写成2026-11-20未来发布。文中明确当时是内部hero agents人工签核，并非完整A/B框架；因此仍不能把厂商准确率叙述当独立真人业务验收。

## 对当前研究的含义

1. **先确定要改哪一层。** Jev只能作托管判断器/教师候选；阿里是获授权后的云LoRA；Clef是开放权重加定制运行时；Tev是LM单token SFT；Kev是开放pointer-head适配路线。接口相近不代表训练对象相同。
2. **把权重训练、外部校准、阈值选择分开。** 封闭API不能由用户改内部权重，但仍可在有标签的独立样本上校准固定版本输出、选择覆盖/风险阈值；不要照抄Kev说明中“托管模型无法重校准”的绝对化措辞。[校准原理](https://proceedings.mlr.press/v70/guo17a.html)
3. **未来M5 Pro 48GB只作条件性硬件目标。** 这里没有企业项目/数据，也没有执行Mac训练；不能把H100/H200的训练时间或延迟迁到该硬件。先核验小模型专用head、训练算子、完整导出/加载与推理概率一致性，再谈客服效果。
4. **生产证据仍有明确空缺。** 本次材料中，平台方专门训练并投入Agent产品最有力；客户自行训练typed模型且有预注册业务对照的公开材料未定位到。没有找到不等于不存在，也不能拿通用客服LLM SFT案例补成这项证据。

复核边界：阿里英文官方页本次可直接读取；样例ZIP的浏览器文本提取不支持其内容，未执行该包。Salesforce帮助页只返回CSS错误，未把该页当已读证据；采用可读官方新闻、论文及工程说明交叉限定结论。所有价格/准入/别名均为核查日文档状态，实际使用前须复核。

## 可训练产物矩阵

以下比较的是训练对象、产物开放程度和实现门槛，不是效果排名；当前研究角色与采纳条件以[总览](decision-model-posttraining-enterprise.zh-CN.md)为准。

“直接返回概率”可以来自固定分类头、动态候选评分、pointer head或候选token读出；它不是某一种训练损失的同义词。也不是所有主流候选都基于Qwen：Laya的ModernBERT／mmBERT、GLiClass的不同编码器和Strands的Gemma分支都应保留。`Base`、指令版、视觉版与不同版本的同名模型不能互换。

| 候选／当前核查起点 | 适配对象与开放程度 | 48GB Mac上的选择边界 |
|---|---|---|
| 普通监督分类器、冻结embedding＋小分类头 | 标签稳定、状态短时可直接训练；模型小、成本容易量清 | 必须有的任务基线。固定标签头无法天然接收任意新路径，但可用请求＋候选配对做条件判断；不是只能用于简单关键词 |
| [Laya](https://github.com/NandhaKishorM/laya) | English421M／multilingual322M；encoder＋决策头；官方有全参／冻结encoder、CE／RLCD、MPS训练与校准接口；Apache-2.0 | 只确认可审查训练入口；独立中文／跨域负面证据不支持企业质量优先级。先通过同条件质量门槛，才判断是否值得投入适配；Mac页是实现备选 |
| [GLiClass](https://github.com/Knowledgator/GLiClass) | 动态标签／描述条件化分类；不同代际有32.7M小模型、多语种encoder与更大decoder模型，训练代码和权重可用 | 对固定与动态标签均是实质候选；需按精确版本检查多语种能力、读出和训练接口。公开train.py的随机切分不能替代企业分组／时间切分 |
| [Kev](https://github.com/jaredpalmer/kev) | 0.8／4／9B为Qwen3.5-Base＋LoRA与pointer head；27B为Qwen3.8-27B全权重版本；训练、校准和模型卡较完整 | 0.8B或4B可作需更强上下文理解时的候选；MPS训练与MLX服务是两条实现。9B需验证训练余量，27B原精度权重已超出48GB，不是本机首轮方案 |
| [Strands Decider](https://github.com/strands-labs/strands-decider) | 当前Qwen3.5-2B-Base分支及四种Gemma4指令底座分支；LoRA＋pointer head，版本有多seed合并与后校准；原料有未完整公开部分 | 已有MLX推理不等于MLX训练／校准；官方训练recipe以NVIDIA环境为主。Qwen视觉继承与真实图像适配不同，Gemma发布分支为文本，不能全家族合称多模态已训练 |
| [Mapika Decider](https://huggingface.co/Mapika/decider-2b) | Qwen3.5-Base的2B／4B等分支；候选字母logit读出；监督阶段与后续RL／视觉阶段按版本区分，代码与注册数据源可查 | 2B v12与历史v10／v11、4B不是同一个训练产物；GGUF推理不提供后训练路径。先核查可继续训练原artifact的代码，再判断是否值得迁移到Mac |
| [CLM](https://github.com/Contrastive-LM/CLM) | 冻结LLM编码器＋可训练state/action投影头，以对比目标适配候选选择；公开主路线为Qwen3-8B编码器 | 候选可复用时有吸引力；小head不等于无需8B编码器。相对排序不能发现所有候选均不合法，仍需绝对适用性／拒判和候选召回验收 |
| [Clef／Clef-Flash](https://huggingface.co/Cloudflare/clef) | Qwen3.8-27B／Qwen3.5-9B带视觉骨干＋joint schema head；开放权重／推理，原始完整训练数据未开放；有社区训练桥接 | 更适合作为需要图像时的推理／技术候选。不能把通用VLM LoRA命令当定制schema head的完整训练；Mac训练链路的已测与未测部分见平台核查 |
| [Perplexity Decider v1.3／Flash](https://huggingface.co/perplexity-ai/pplx-decider-v1.3) | Qwen3.8-27B／Qwen3.5-4B；共享状态、定制joint读出；开放权重与推理，完整原始后训练材料未据此建立 | Flash4B推理可列候选，但不能因尺寸可放入内存就称公开配方可在Mac续训；默认因果LM读出不等价于该模型的协议 |
| [Intern-Decision](https://github.com/InternLM/Intern-Decision) | Qwen3.5指令检查点；固定回答骨架、决策marker的causal CE；冻结vision／projector并训练语言骨干；源码和权重分开发布，原训练数据不完整公开 | 官方配置不是现成LoRA，当前训练实现要求Linux／CUDA／XTuner。把4B推理放入48GB不能证明可原样全语言参数训练；新增LoRA需验证marker与视觉链路 |
| [SII-Decision](https://github.com/amazingljy1206/SII-Decision) | 4B为Qwen3.5-4B指令版、27B为Qwen3.8-27B；第一token候选读出，同底座思考分布蒸馏；现有代码、训练数据、LoRA与Full发布；训练器从原始底座起步，要求gold_target、train_target和p0，并非只收企业硬标签的续训入口。Full只更新与LoRA相同的指定语言线性层，非每个参数 | 4B值得保留为不同信号路线；提供的4／8GPU训练wrapper与4090推理脚本不能称单Mac已可复现。LoRA发布为合并权重，继续训练前核查起点及保存格式 |
| [Nimble开放9B](https://huggingface.co/bespokelabs/Bespoke-Nimble-9B) | Qwen3.5-9B＋PEFT adapter、候选token CE；最小事实改动是数据方法，非表示层contrastive loss；2676合成训练／324合成评测行不等于独立人工金标 | MLX推理不证明Mac训练；旧开放9B与新托管v4／v4.1分别识别。模型卡Apache-2.0不自动证明当前GitHub全部代码同许可；版本与许可边界见[模型卡](models.md#nimble) |
| [Chinese-Jev](https://github.com/gulucaptain/Chinese-Jev) | 已有encoder训练／数据构造代码；[10月18日发布记录](https://github.com/gulucaptain/Chinese-Jev/commit/02a84752a7915a6c66baf434e6d58ea5909f1e0e)链接CJ-Medical，[固定权重卡](https://huggingface.co/bbldCVer-hf/CJ-Medical/blob/1ae360b3ec9927622dd82f1430f0111f292ee17f/README.md)声明Apache-2.0。General及其他行业产物分别核查；混合CJ数据保留各来源许可 | 本轮只核卡／元数据，未下载权重或认证论文原run身份；医学题表现不等于中文客服效果或目标Mac训练可行。不能再写所有行业权重均未发布，也不能把社区底座适配当原论文复现 |
| [Koa Decisions](https://www.salesforce.com/news/stories/koa-decisions-salesforce-decision-models/) | 供应商生产组件与论文方法参考，原企业数据及部署检查点不公开 | 主要借鉴原子标签映射、匹配服务评估和状态合同；不属于现成的本地开放权重训练方案 |

上述模型的代码／权重许可与训练来源许可分开。Apache-2.0卡片不能自动覆盖混合训练语料；某个家族含研究用／非商业来源时，需按精确artifact解释，不能用另一个同家族版本代替。
