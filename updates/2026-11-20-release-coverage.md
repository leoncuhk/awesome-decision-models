# 11月20日发布覆盖复核：补齐模型池，保留后训练资格边界

核查日：**2026-11-20，Asia/Shanghai，本轮公开来源快照**；不是预先声明的日终封盘或全网穷尽。当前企业方法与实施判断只在[单份主指南](../docs/decision-model-posttraining-enterprise.zh-CN.md)维护；逐模型事实进入[规范索引](../docs/models.md)，不另建一份竞争排名。

**旧清单没有覆盖完这批发布。** 本轮前有75项资源／22个核心系列／350条来源；补录13个核心系列及Clairic相邻提取任务，成为89项／35个核心系列。既有8族的版本、训练与可用性字段也有实质更新，另纠正Microsoft和OpenAI的托管版本。此前已经出现过Mapika的研究来源，不应说成完全未研究；相反，只有收录名或旧版本也不能叫当前完整覆盖。

本轮做了来源、指定源码与完整公开文件元数据核查，**没有下载或核验tensor字节，没有执行模型推理／训练，没有访问企业数据或用户M5 Pro 48GB**。评测台账45条完整保留，未把本轮新卡片的宣传分数追加成混合排行榜。收录和软件检查均不是效果复现。

## 1. 最近的实质更新

日期区分正式公告、权重上传和代码／卡片更新；没有核到正式公告的只写实际观察事件。以下不是效果排名。

| 对象 | 核到的新事件 | 自有企业数据后训练的实际资格与限制 |
|---|---|---|
| **GLiDE** | [11/5五尺寸开放发布](https://fastino.ai/blog/glide-decision-model-family)；[11/18训练示例](https://fastino.ai/blog/glide-multimodal-decisions-fine-tuning) | 0.4／0.8／2／9／27B权重；有具体[typed-row训练API](https://docs.fastino.ai/training)、CE／KL目标与checkpoint部署。已有2B示例及小尺寸报价，但精确账号／base ID／导出未实调；未定位完整本地trainer。Community License有收入门槛，非Apache |
| **Strands Gemma4 v2** | [E2B权重](https://huggingface.co/StrandsAgents/strands-decider-E2B-gemma4-v2-2611/tree/a74ee815c2af08d16afd0b9dfa079ce260cfafdb)于UTC11/17上传，即上海11/18 | 新token readout／prefix-bidirectional及[公开v2配方](https://github.com/strands-labs/strands-decider/blob/d4915c9b11f61bb01ed293f4dc4c770a0a51792b/training/README.md)。可从原始底座与自备行训练；HF合并发布物不满足旧`init_from`训练checkpoint布局。CUDA训练，不是已验证Mac LoRA；约5.1B总参数／2.3B有效参数须分清 |
| **Liquid d1** | [11/16托管d1.2／ultra](https://www.liquid.ai/blog/d1-2)；开放2B／Omni-2B另属[本地模型](https://docs.liquid.ai/lfm/models/decision-models) | 官方有MPS／MLX推理及中文声明；尚未建立d1 typed-head完整续训链。通用LFM微调工具不自动适配本合同。LFM许可有商用收入门槛；托管ultra成绩不能搬到开放2B |
| **Clairic／Flash** | [11/18正式公布改版](https://blog.cloudflare.com/open-clairic/)，当前权重已于11/13上传 | 27B／9B类型化提取／估计；常规提取采用并行slot自回归，另有数值头。输入计费不等于零生成。Apache权重，但未建立完整企业trainer；作为相邻提取任务，不能挤入闭集路由质量榜 |
| **WPS Decision v1.1** | [显式v1.1 tag](https://huggingface.co/Kingsoft-Office/wps-decision-1/tree/fe7acc7de60124085cc20e9102249f4b98851a76)于11/17更新；默认main仍为v1.0 | 新Qwen9B合并权重／256槽读出，与旧D3-flash衍生v1.0不同。Apache；当前适配器未实现训练／通用保存／量化加载。Linux CUDA验证不能外推M5；不把默认main误认v1.1 |
| **Microsoft Decision1.1** | [11/17 GA](https://commandline.microsoft.com/microsoft-decision-model-ga/) | 现为Gemma4 26B-A4B及图片支持，不能沿用1.0的Qwen9B／preview说明；未核公开权重或本产品自助FT。部署名、model-version `1`与产品1.1不同 |
| **j-geuter/Jeff1.1** | [11/14新公开训练／export入口](https://github.com/j-geuter/Jeff/tree/938ac5a03c6ac43512e61266d9febf691edc17f8)；完整4B权重最迟10/23已存在 | 自有JSONL、LoRA／head与原始DecisionBank可审；发布权重及全量混合数据非商用。商业研究可参考代码，从许可合适底座与自有数据起训。当前CUDA／CPU，未验MPS |
| **Valen-Decision1.5** | [完整4B权重11/9上传](https://huggingface.co/Valen-Team/Valen-Decision-1.5-4B/tree/9b0cacc976d7fb72f252ee1adb1564f5f15e462c)，11/12卡片更新；[训练源码快照11/15](https://github.com/Valen-Team/Valen/tree/f6df4fdbc45bf44a4ffbebaeda53f5fe6e49b339) | 是值得补录的独立上游：自有JSONL、native检查点保留Mixer／grounding、full／LoRA SFT、恢复／导出有实际入口。loss缺省CE、领域示例另配辅助项；实验RLCD与PRDO分开。官方0.8B／H200短smoke仅工程回执，MPS训练统计float64路径需处理；今天ANE包不是新的训练或Mac训练证明 |
| **RSI-Jev v7.0-VL** | [4B于11/5](https://huggingface.co/shgao/rsi-jev-v7.0-vl-4b/tree/58baf6fc961f42108756b27ff92fddf4aea3b1d8)、截断3B于11/7、MLX量化于11/10 | [完整训练源码](https://github.com/Shanghua-Gao/RSI-Jev/tree/e58526f061afd4c383d33a22b309b888f8a3e3c7)值得优先审。原始276万行／dev未公开，原配方全语言参数＋CUDA／多H200。3B无重新训练、MLX为推理，不能记作两个独立训练增益 |
| **D3.1-nano／D3 Ultra** | [nano权重11/12](https://huggingface.co/vllm-sr/d3.1-nano/tree/71d06677f56e243042fe5d5f983804648a5689e8)；[Ultra](https://huggingface.co/vllm-sr/d3-ultra/tree/3ac9ff15579ca9193a0d44f4fa9056f2ea62731d)10/26，11/17为运行库／卡片更新 | nano公开成绩平均两种choice顺序，普通运行路径不等价；未评图像／视频质量。新产物身份不等于完整续训链；CoreML／MLX转换另记 |
| **Laya0.5.0／Vega** | [包0.5.0](https://pypi.org/pypi/laya/0.5.0/json)于UTC11/19上传，即上海11/20 | 默认Vega冻结reader拟合小头，不等同经典322M／421M encoder微调；经典HF tensor在所比版本未变。新小头／校准结果不能继承旧Banking77成绩 |

另外更新Clef-omni、Baseten Joey、Jeffan9B／27B、jevos v5和GLiClass v4。GLiClass v4.1 Edge虽有11/9权重／配置，但所查无卡片及许可证，不能继承v4的授权或效果。旧22族不是都重读了全部代码；本轮有些仅刷新metadata与已知版本边界，source登记保留各自实际深度和日期。

## 2. 今天确有新上传，但不等于几十个新独立模型

Hugging Face的`decision-model`标签检索取两页400条元数据；该样本中391条创建于UTC11/12及以后。按**上海11/20**而非UTC日筛到47个仓；其中27个创建于UTC11/19晚间。该标签不是领域完整目录，仓库数量也不是独立训练或模型家族数量。

本轮读取这47仓的公开元数据及可得卡片，对重要者选读实现与历史tensor元数据；没有声称对47份实现逐行审计或运行。发现层与技术层分开：空仓、量化、合并、改名、训练中间版本和相邻任务均保留各自身份。

| 今天的候选／发布组 | 核验后怎样处理 |
|---|---|
| **[Decisio tuned v3](https://huggingface.co/tachara-ai/Decisio-12b-tuned-v3-calibrated/tree/1e9159cc082c689fd95381e0ed6306402dc932d2)** | Gemma12B、作者463,859题LoRA及逐题型温度。八仓含BF16策略／FP8／MLX包；calibrated与commit两份BF16的完整声明tensor集合相同。作者分布内留出不是独立企业基准；未建立完整公开自有数据trainer。作为新增核心推理参照，不作今日效果冠军 |
| **[Guy-Amit safety-decision](https://huggingface.co/Guy-Amit/gemma4-e2b-safety-decision)** | 合并版及LoRA版是同一安全／判断适配线；原训练base revision未明确记录。公开卡不支持它是通用中文路由赢家，也未建立本机训练闭环 |
| **[Ling-3.0-tiny-JEV-v1.1](https://huggingface.co/AsystemAReno/Ling-3.0-tiny-JEV-v1.1)** | Ling3.0 tiny的LoRA／候选token读出，约7.9B总／1.3B激活；不是驻留1.3B。公开推理适配与原完整trainer不同，所查无许可；不作商用默认 |
| **[miniRSI-jev-4b](https://huggingface.co/k2021211255/miniRSI-jev-4b)** | 所有者不同于RSI-Jev作者，不能只按名称合并。Qwen4B全参／图像公共作者评测；非商用权重，未公开trainer，作者CUDA80GB不外推Mac |
| **[Adjudex0.8B v7](https://huggingface.co/newsbang/adjudex-0.8b-v7)** | Qwen0.8B／255候选头及公开作者测试；公开成绩不等于目标域后训练增益，完整自有数据trainer未建立，暂作观察 |
| **Zils多所有者变体** | 多数为已有D3／Qwen系的adapter、soup、delta蒸馏或中间检查点；只有明确技术增量才另审，不为每个名称建独立家族。数据来源／权重授权及独立任务验证仍要核 |
| **[Synth-NLP葡语意图三份发布](https://huggingface.co/Synth-NLP/laya-intencao-ptbr-sintetico)** | Laya、Kev0.8B／4B是真实标签与合成增强的同一实验；三个新入口的模型tensor均与11/15旧分支相同，不是当天三次新训练。其公开数据／逐题输出值得参考，但反复使用validation、单划分／有限seed与语言审校限制不支持中文生产效果 |
| **[NightWatch0.8B](https://huggingface.co/nullptr04/NightWatch-0.8B)** | D3-lite视觉watcher领域适配，具有生成桌面／网页及frame outcome标签；任务与Skill路由不同，不把视觉状态成绩当客服路线增益 |
| **格式转换／新命名** | Kev ONNX、GLiDE WebGPU Q8、Elephant MLX、lg-decision GGUF、Valen ANE等，属于推理产物；转换小样本检查不是新训练、广泛概率等价或Mac训练证明 |
| **相邻及空仓** | `s6-ear3-nano`为语音end-of-turn任务，作者Mac训练声明及失败gate另记；`jedld/system-one-choice`为Magic游戏动作策略（有`.pt`权重，权利受限），不是企业通用判定器；GUI grounding／多专家拼接按任务核；仅`.gitattributes`的`QWEN_to_JEV_LoRA`不算已发布模型 |

“有MLX／Metal／ANE包”“作者在M5训练过另一个小任务”和“用户48GB机器能训练当前typed模型”是三个命题。

## 3. 补齐旧遗漏及其他观察项

| 条目 | 本轮结论 |
|---|---|
| **Mapika Decider** | 此前有RL说明来源但缺核心入口；[监督配方／数据转换](https://github.com/Mapika/decider/tree/91b6fa9b94ab6c4dc2c63d3b14d413243b4fffcc)值得纳入。2B／4B／31B当前权重是10月已有；环境PPO与静态监督分开，默认Noul低温不认证概率 |
| **[MNN-Pocket-0.3B-Dec](https://huggingface.co/taobao-mnn/MNN-Pocket-0.3B-Dec/tree/7d5b512f3fe579418c45a77b178da39273b2a114)** | 极小中英pointer-head参照，10/15已有；包有adapter／head不等于有训练loop。600例温度拟合不是独立任务准确率 |
| **[H2O Lightning4B](https://huggingface.co/h2oai/h2o-lightning-4b/tree/659fc412de8486dbc2477b0d1cb4121e97e72471)** | 10/2已有、当前11/1快照；类型化推理包及顺序平均／重读／计算器影响测量。未建立领域trainer，不继承旧榜首宣传 |
| **[IBM Granite Switch](https://huggingface.co/blog/ibm-granite/granite-switch-4-1)** | 10/15发布、当前decision adapter v1.1于10/28；冻结8B／30B＋LoRA／aLoRA，cache复用值得研究。aLoRA不合入base，通用PEFT不等于完整领域trainer；小adapter不消除大底座驻留 |
| **[JAD-S1 v0.5](https://huggingface.co/DreamBlooms/JAD-S1-7B-A1B-v0.5/tree/178febae0936d8c0f71312421d65e5b6baca466c)** | LLaDA-MoE单mask读出可作不同骨干对照；11/12上传／卡标11/13。公开adapter／推理／校准，未见完整trainer；7B总／1B激活不是1B内存 |
| **[Ant LingDT Decision](https://maas.antdigital.com/models/modelservice-1792325631780001741)** | 官方公开服务JSON确认1.0／4B免费测试端点及逐层调用／注入上游答案的DAG合同；不从通用LingDT1.1的生产建议补猜Decision1.1。未核公开权重／专属客户FT |
| **[Respan Span-02](https://huggingface.co/respanai/span-02/tree/63cbdd774391f1b7d9bc3829179efe996d0191ce)** | 10/15博客、10/19网关更新，开放专用CUDA量化engine；未建立可训练BF16／trainer。number会生成token，不能把全产品概括零生成。Span-01行为检测是另一合同 |
| **[Ainvest31B v2](https://huggingface.co/Ainvest-World/Ainvest-Decision-31b-v2.0/tree/8e1ed5b2a6a268282010635206f2362cf88e5d12)** | 11/11权重；可做大模型离线对照，BF16约62.55GB，原始trainer／数据未公开；不是M5原配方 |
| **[NewTokenEra27B](https://huggingface.co/NewTokenEra/newTokenEra-decision-ct-Qwen3.8-27B/tree/3bb9995c413076019bb5ec9e37a70a7da2e32bd9)** | 11/18确有tensor变化，11/19主要为服务／说明；未建立统一授权及trainer。不能因训练来源含非商用材料就直接裁定全部权重许可，也不能默认可商用 |
| **[JDI](https://huggingface.co/JoyIndustrial/JDI-Decision-V1/tree/505835366f2ae6cd69349b7c6783b4e8588aab0d)** | 当前第一方卡明确权重CC-BY-NC4，外部registry的Apache标签不可靠；Qwen／D3改动、OCR／视觉及CUDA组合engine分别核。未建立完整trainer，权利历史不作法律裁决 |
| **swiftpick／SecJev** | 前者为Strands移植Nemotron与公开训练fork，不重复计上游；后者为Kev系安全任务，验证集阈值到留出流量明显退化，适宜作授权／漂移负例，非通用路由新底座 |
| **[Zuse](https://bineric.com/zuse)** | 有论文／托管服务，但官方未开放权重、trainer及数据；不能写成可自行后训练的新增开放模型 |

## 4. 托管产品也需刷新版本与生命周期

[OpenAI Decisions](https://openai.com/index/decisions-api/)已于10/22 GA，当前指南有400题、缓存、工具历史及Private Link；旧beta／200题信息过时。其专属客户FT未核，不能从普通模型微调能力推断。Google Gemini Decision1的11/11服务已在旧索引中，本轮未确认更晚模型；当前API服务不是开放Gemma权重。

另外核到[SubQ Snap1.2（11/11）](https://subq.ai/subq-snap-1-2)、[Celeris1.1（11/5）](https://celeris.ai/celeris-1-1-decision)、[meraGPT Decider1.1](https://meragpt.com/models/decider-1)、[Hanzo Kai1.2](https://docs.hanzo.ai/docs/models/kai/)及[Solar Decide](https://console.upstage.ai/docs/models/solar-decide)的官方合同；本轮未建立这些具体产品的公开权重／自助领域FT。Kai不是开放Zen；服务alias会移动，旧ID不能当冻结权重。

[Mercury Decide官方指南](https://docs.inceptionlabs.ai/capabilities/decisions)仍有接口，但[当前结束服务通知](https://docs.inceptionlabs.ai/support/wind-down)写明2026/12/28后停止API／平台。通知发布日期未钉，只记录11/20观察；不因旧主页宣传而推荐长期新接入。

## 5. 对企业后训练的决定

1. **保留算法采纳顺序。** 可信领域标签的直接CE／BCE适配是起点；有明确标签缺口再加入经核验教师／蒸馏；PRDO只用于部署保留推理且确有净收益的子任务。新发布、公开榜分、参数量和下载量均没有替代目标业务对照。
2. **扩展有实际入口的模型池。** Kev／原始小底座／多语encoder继续作可实施基线；新增优先审Valen、Strands v2、RSI、Mapika与Jeff的训练实现。Jeff权重／混合数据的商业边界另处理；“代码可参考”不是“发布物可直接商用”。GLiDE在数据可获准上云时与百炼比较托管训练资格。
3. **小模型和托管对照按失败类型选少数。** Liquid、MNN、JAD、H2O、Decisio等是新增可比较载体，不要求全部训练，更没有实证支持先训27B再压4B。Strands E2B、MoE激活参数、小adapter、MLX推理都不提供48GB训练承诺。
4. **下一步仍是企业独立数据。** 在相同输入、候选、允许集合、标注预算与完整成本下，比较原版和直接适配；再检查概率、整条接受／转交策略、完整任务成功与副作用。当前仍无本次企业模型冠军、训练增益或生产结论。

## 6. 核查范围与可追溯性

- 使用一手卡、指定源码、正式公告及服务合同确认事实；外部registry只作发现入口。发现时间轴123项含Jev本身与衍生／runtime，且部分止于11/11，不能当最新或独立模型总数。
- 既有17个固定HF仓完成全分页文件元数据比对，**16个binary清单身份未变；另1个CoreML仓新增8个edge转换binary**。这里的身份是远端声明的LFS对象／字节数，不是本地下载hash验证，不证明评测时权重一致。
- 新开放候选另核13个完整HF清单，机构与当天重要产物另核完整API siblings。分页的`tree?expand=true`默认50条，本轮跟随Link或与完整siblings对齐，未把第一页当全量。
- 完整公开metadata／卡片抓取与差异回执保存在本地忽略的`reports/2026-11-20-release-coverage/`；公开索引中的固定revision链接可追原内容。Git源码commit、HF仓revision、LFS声明对象、API别名和训练批次仍分开。
- 这不是所有第三方分支、量化仓、原始数据行许可、全部350条旧来源或每行代码的重审。没有新增实验成绩，45条既有评测不变；旧历史原件与独立PR5不变。docs仍17份Markdown，企业正文仍一份。
