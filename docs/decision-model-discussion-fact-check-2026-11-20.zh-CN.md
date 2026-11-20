# 11月19–20日决策模型讨论：逐项事实与推论核查

核查日期：2026-11-20。对象为用户提供的整段讨论，覆盖Jev定义、后训练、模型排序、PRDO／StartLux、客服下一步动作、意图路由和最后的三篇推荐。重复主张合并核查，问候、提问和没有事实断言的文字不单列。

**结论：多组数字确有原文，但讨论不能整体作为可执行方案。** 主要问题是版本／指标混用、把有条件实验外推为通则，以及从分类标签训练跳到业务动作价值时遗漏识别条件。当前企业选型仍以[总览](decision-model-posttraining-enterprise.zh-CN.md)为准；本文是可追溯的讨论核查，不维护另一份模型排行榜。

判定：**成立**＝来源在所述协议内支持；**需限定**＝部分正确但缺重要条件；**错误**＝与来源或数学条件冲突；**未证实**＝本轮未取得足够一手证据。成立也不表示本仓重跑模型。没有下载权重、执行训练／模型推理、取得企业数据或验证生产效果。

## 来源版本与覆盖

| 材料 | 核查对象与边界 |
|---|---|
| TypeSafe、云平台与模型仓 | 当日官方文档／固定代码、卡片和元数据；接口可读不等于服务或目标机实测 |
| [Inner Jev](https://arxiv.org/html/2610.17205v1) | Jeff模型论文v1；OpenDecisions Capability与外部macro accuracy分开 |
| [OpenJev旧v1](https://arxiv.org/html/2609.38850v1)／[PRDO v2](https://arxiv.org/html/2609.38850v2) | 是同一论文不同版本；v1两阶段成绩不能用作v2主结果 |
| [JEVal／SII v2](https://arxiv.org/html/2610.03935v2) | 11,257总题；主分类表10,938题，另319个score；作者也提出SII |
| [CAPS v1](https://arxiv.org/html/2611.15572v1) | 选中类别对错的金标模拟日志；不是企业业务策略的生产实验 |
| [StartLux v2](https://arxiv.org/html/2610.17309v2) | 论文、发布包与DI榜单快照分别核查，不混用版本或评分 |
| [CLINC路由v2](https://arxiv.org/html/2610.00346v2) | 英语固定意图及OOS、训练暴露不同的分类器／LLM／决策模型 |
| [LLM-as-Jev v2](https://arxiv.org/html/2610.02076v2)／[当前v3](https://arxiv.org/html/2610.02076v3) | 分别标版本；配方可读与原训练代码可执行分开 |
| [Agent决策点v1](https://arxiv.org/html/2610.02267v1) | 不同决策点、候选难度和标签审核的作者实验，不是领域通用定理 |

## A. Jev、平台、可训练模型及最初排序

下表按原主张核查；标“实施边界”的行补充必要条件，不冒充对方逐字原话。代码、权重、完整训练材料和实际效果分别判断。

| ID | 原主张／实施边界 | 判定 | 校正与一手来源 |
|---|---|---|---|
| A01 | Jev还要排队／waitlist | **错误／过时** | 官方帮助明确可直接注册、不需waitlist approval。未据此声称任何账户必然付款／调用成功。[账户帮助](https://help.typesafe.ai/articles/4519713419-how-do-i-create-or-activate-my-account-after-an-invitation-or-waitlist-approval) |
| A02 | Jev纯文本 | **错误／过时** | 1.13／1.14均接受PNG/JPEG；Box需1.14。图像／Box默认关闭，须显式Danger-Zone header，官方仍不称production-ready。原生音频／视频尚不支持。[Models](https://docs.typesafe.ai/models)、[Images](https://docs.typesafe.ai/images#turning-on-images) |
| A03 | $0.042／百万tokens | **正确，限计费口径** | 当前模型表为每百万**输入**tokens $0.042，输出免费；不是含重试、检索、执行和人工复核的总成本。[Models价格表](https://docs.typesafe.ai/models#current-models) |
| A04 | 64k上下文、最多255项 | **需条件** | 默认每请求64k、每题32k；长上下文显式开启后两者均262k。255是每个Choice的选项上限，不是问题数量。[Context](https://docs.typesafe.ai/models#context-length)、[Choice](https://docs.typesafe.ai/primitives/choice#good-practice-ask-more-than-one-question-per-request) |
| A05 | 有社区反馈API在国内访问不了 | 需限定 | 个人访问失败不能外推为整个地区禁用；本轮没有当地网络／账户实测，也未以官方文档确认全域不可用。 [官方模型／访问说明](https://docs.typesafe.ai/models) |
| A06 | 接口成为事实标准，以后换模型基本不用改代码 | 需限定 | 已有多家接口形状兼容，可称生态约定；尚不能据此保证所有模型／版本无差别替换，媒体、schema、鉴权、错误和概率语义仍须验收。 [Ollama官方发布](https://ollama.com/blog/ollama-now-supports-jev-style-decision-models) [百炼指南](https://help.aliyun.com/en/model-studio/decision-model-tuning-guide) |
| A07 | Ollama可直接用同API | **正确，需模型／版本条件** | 官方发布说明从0.35提供`/v1/systemone`并演示TypeSafe SDK；首批nimble、tev1及tev1:0.8b。不能据此把任意普通Ollama模型当成原生决策模型，亦未核验每个版本的完整兼容性。[Ollama API与模型清单](https://ollama.com/blog/ollama-now-supports-jev-style-decision-models) |
| A08 | 百炼兼容Jev接口，并支持LoRA式SFT | 成立，需准入／版本条件 | 这是百炼自己的模型；efficient_sft需开通，版本／地域／鉴权受文档约束。它不能用来更新TypeSafe Jev内部权重。 [Data／Post-deployment invocation](https://help.aliyun.com/en/model-studio/decision-model-tuning-guide) |
| A09 | Jev不提供客户专属FT／LoRA | 成立 | 官方明确共享权重且不做客户FT／LoRA；外部输出校准和阈值选择仍可进行。 [Customizing Jev](https://docs.typesafe.ai/models#customizing-jev) |
| A10 | TypeSafe承诺不把客户数据用于训练，还是仅不做客户专属FT | **两项有独立来源，须保留合同条件** | Models Data handling另外明确Jev不以客户requests／responses训练，不能仅由共享权重推出来。MCA §4.1承诺未经客户事先同意，不将Customer Data放入修改AI／ML权重的训练集；这不等于任何同意安排下永不训练，Telemetry用途另列。[Data handling](https://docs.typesafe.ai/models#data-handling)、[MCA §4.1–4.3](https://typesafe.ai/legal/mca) |
| A11 | 开放决策模型普遍＝冻结Qwen＋LoRA＋新head＋CE/Brier | **错误概括** | Laya为encoder；Mapika保留候选LM-logit读出；Intern训练语言骨干；Kev27B全权重；SII的LoRA／Full有同一指定层覆盖。损失也包括CE、蒸馏、对比目标等，Brier不是通用必要项。[Laya trainer](https://github.com/NandhaKishorM/laya/blob/d1282e791d71e92f24f816ff3836e4fd1c2ded4a/laya/train.py)、[Kev Models](https://github.com/jaredpalmer/kev/blob/051142bf849c2c6ad3f23e17a7b5aea2686d9a91/README.md#models)、[SII Training](https://github.com/amazingljy1206/SII-Decision/blob/1723d83cbda69f48641c273280b5a2d06d6b3510/README.md#training) |
| A12 | Kev的0.8／4／9B用LoRA，27B全参 | 成立，需补底座版本 | 当前前三者基于Qwen3.5-Base，27B基于Qwen3.8；全家不能统称同一Qwen3.5检查点。 [当前Models／Previous generation](https://github.com/jaredpalmer/kev/blob/051142bf849c2c6ad3f23e17a7b5aea2686d9a91/README.md) |
| A13 | Kev4B微调约1美元、三平台都能跑 | 需限定 | 1美元为作者小任务H100示例，非总成本或Mac耗时；训练、推理及各框架／算子支持分开，目标M5尚无训练实测。 [kev-finetune What you need](https://github.com/jaredpalmer/kev/blob/051142bf849c2c6ad3f23e17a7b5aea2686d9a91/skills/kev-finetune/README.md) |
| A14 | “自己的客服数据”67.7→73.6 | 数字有出处，数据性质需纠正 | 该例是1050条生成记录和三道支持工单问题；为作者离线适配，不是本次目标企业真实客服数据或生产收益。 [Why fine-tune](https://github.com/jaredpalmer/kev/blob/051142bf849c2c6ad3f23e17a7b5aea2686d9a91/skills/kev-finetune/README.md#why-fine-tune-at-all) |
| A15 | CFPB准确率.804→.904 | 成立，限历史协议 | 来自公开投诉、两种模板及作者AI裁定／人工抽查；不是当前新版本跨企业泛化或线上增量。 [固定历史卡](https://huggingface.co/jaredpalmer/kev-4b/blob/957b91e762e883935830246eeb02381f9d2694b6/README.md#read-this-before-relying-on-the-documents-numbers) |
| A16 | Kev覆盖52–69%，Jev70% | **正确，限该作者新来源suite与5%错误预算** | 是Kev4／9／27B的经验自动接受覆盖；0.8B另为14%。既不是总体准确率，也不是领域保证或真实工作自动化比例。使用方必须独立选阈值并验证。[Confidence](https://github.com/jaredpalmer/kev/blob/051142bf849c2c6ad3f23e17a7b5aea2686d9a91/README.md#what-to-expect) |
| A17 | Kev公开训练代码／评测数据，工具链最完善 | 前半有产物，最高级未证实 | 有可查训练、校准、适配和评测入口；“最完善”缺统一比较标准，不能由代码齐全证明中文企业质量。 [Training／Limits](https://github.com/jaredpalmer/kev/blob/051142bf849c2c6ad3f23e17a7b5aea2686d9a91/README.md) |
| A18 | 应从已训decision checkpoint继续FT | **合理候选，不是定律** | Kev确有`--init_from`路径，可保留已学读出／格式；领域改进仍需对比原检查点。若旧模型的语义／候选偏差严重，原始base＋相同读出也可作Dev对照；不能把训练起点建议等同已证优。[Kev train API](https://github.com/jaredpalmer/kev/blob/051142bf849c2c6ad3f23e17a7b5aea2686d9a91/kev/train.py) |
| A19 | Strands最新r16，准确率72% | **r16符合Qwen路线，72%过时** | 72.3%=历史v19的167/231；当前Qwen v1为180/231=77.9%，另有Gemma4分支。小公开集且多版本开发反馈，不能由这些分数证明新企业效果。[README架构／Performance](https://github.com/strands-labs/strands-decider/blob/7e8380ca64604a5be3dc954e726173fa1acb6c73/README.md#performance) |
| A20 | Strands在3090为106ms | **当前来源未证实该精确值** | 当前README原始表是v19：RTX3090／WSL2 median115ms、P95 299ms；不同长度／Mac另表。若106来自另一个run，须附版本／输入／计时范围，不能写通用值。[延迟表](https://github.com/strands-labs/strands-decider/blob/7e8380ca64604a5be3dc954e726173fa1acb6c73/README.md#performance) |
| A21 | Strands可用于自有数据后训练 | 有入口，完整复现／Mac训练仍需版本条件 | 公开构建／训练／校准链路与v19/v1配置可查；原料、teacher／replay与算力条件仍须逐版核验。 [Training](https://github.com/strands-labs/strands-decider/blob/7e8380ca64604a5be3dc954e726173fa1acb6c73/training/README.md) [Reproduction contract](https://github.com/strands-labs/strands-decider/blob/7e8380ca64604a5be3dc954e726173fa1acb6c73/data/README.md#reproduction-contract) |
| A22 | Mapika用了约95数据集，数据都开源 | **前半有来源，后半过强** | 原仓有约95公开来源的构建器、mixture及teacher材料；监督复建与所有后续RL／视觉阶段不等价，RL阶段所需独立环境／研究loop并未全部包含。混合源保留各自许可，不由代码Apache统一覆盖。[Train your own](https://github.com/Mapika/decider/blob/91b6fa9b94ab6c4dc2c63d3b14d413243b4fffcc/README.md#train-your-own)、[2B当前卡License](https://huggingface.co/Mapika/decider-2b/blob/7614a6c7ea5a047aa7d7bcfb1a0015469381c3e3/README.md#license) |
| A23 | Mapika每种问题类型单独一个温度 | 机制存在，须指明版本／取值 | 当前默认Noul的T=.05用于特定计分，作者明确损害概率校准；另有fitted per-type温度。存在温度参数不等于可直接作为业务置信度。 [2B Changes from v11](https://huggingface.co/Mapika/decider-2b/blob/7614a6c7ea5a047aa7d7bcfb1a0015469381c3e3/README.md) [4B卡](https://huggingface.co/Mapika/decider-4b/blob/585473dec4fa93f0325c2bf02dda7273b61f44c1/README.md) |
| A24 | Clef209／Flash38.8／Jev524ms | 成立，近似数值有条件 | 官方median精确为209.3／38.8／524.1ms；是供应商协议下的报告，不能迁移为目标Mac或业务端到端延迟。 [官方延迟表](https://blog.cloudflare.com/clef-decision-models/#how-do-our-models-compare) |
| A25 | Clef开放权重，是可再后训练候选 | 部分成立，实施合同尚须核查 | 权重、joint head与推理源码可读；原始数据和专用head适配不是同一产物，不能由开放权重承诺目标机训练已跑通。 [官方训练说明](https://blog.cloudflare.com/clef-decision-models/#how-we-trained-clef) [Flash固定卡](https://huggingface.co/Cloudflare/clef-flash/blob/22b75507981345858dd152fbd9a6f8c0c4068b0a/README.md) |
| A26 | Clef为冻结Qwen＋r256 LoRA＋label-smoothed CE／Brier＋RL参考约束 | **作者当日说明支持；具体KL实现未核实** | 官方How we trained Clef仍明确这组监督训练设置；辅助RLCD给邻近ordinal部分分、精确record奖励及reference penalty。不能把最后一项补写成已公开KL公式／系数或完整可复现训练包。[官方训练段](https://blog.cloudflare.com/clef-decision-models/#how-we-trained-clef) |
| A27 | Cloudflare有工程团队协助的RL训练服务 | 成立，限当日服务说明 | FDE协作为当前说明，自助平台仍是后续目标；本轮未登录或核客户准入，不把服务说明当生产效果。 [Our new RL service](https://blog.cloudflare.com/clef-decision-models/#our-new-rl-service) |
| A28 | v1.2是最新pplx-decider | **错误／过时** | 当前官方已发布v1.3与Flash v1.3；27B为Qwen3.8，Flash为Qwen3.5-4B蒸馏。旧分数和prompt不能自动继承。[v1.3发布说明](https://www.perplexity.ai/en-GB/hub/blog/perplexity-decider)、[v1.3卡](https://huggingface.co/perplexity-ai/pplx-decider-v1.3/blob/9c2ebb27470d3dec2ad7ab727727e40d142c7213/README.md) |
| A29 | PPLX在Qwen底座上全参微调 | 需补全阶段／版本 | 当前v1.3作者说明包括generalist全FT、domain／vision LoRA和多seed合并；Flash经教师分布蒸馏，Locate为另一个adapter／span头。 [How we train](https://www.perplexity.ai/en-GB/hub/blog/perplexity-decider) |
| A30 | 卡中private文案与公开标记矛盾，下载前须确认 | 成立，当前元数据可澄清 | 当前两个v1.3仓private=false／gated=false，匿名首shard HEAD200；卡中private需token文字为残留。未下载权重字节，也不保证未来访问状态。 [27B元数据](https://huggingface.co/api/models/perplexity-ai/pplx-decider-v1.3) [Flash元数据](https://huggingface.co/api/models/perplexity-ai/pplx-decider-flash-v1.3) |
| A31 | PPLX未公开训练代码，微调需自行实现 | 当前完整配方未确认 | 本轮找到推理包和过程说明，未定位完整对应训练器／数据包。可求梯度的推理head不等于现成业务适配链路；是否从零写应另评现有实现。 [Checkpoint format](https://huggingface.co/perplexity-ai/pplx-decider-v1.3/blob/9c2ebb27470d3dec2ad7ab727727e40d142c7213/README.md#checkpoint-format-and-serving) |
| A32 | DI68.09／58.88说明“可商用最高首选” | **分数属历史特定协议；排序结论无依据** | 数字来自v1.2 **Decision Index0.3 public、joint requests**。27B单题67.75，Flash单题60.05反高；不是private/full榜单、准确率或当前v1.3分数。Apache是使用许可，不是企业质量证明。[27B v1.2 Evaluation](https://huggingface.co/perplexity-ai/pplx-decider-v1.2/blob/cce0f3f80033e9d89d80831d5281fd72124aacce/README.md#evaluation)、[Flash v1.2](https://huggingface.co/perplexity-ai/pplx-decider-flash-v1.2/blob/9ff7cf9838e59df461c276b7699d56b244d2af58/README.md#evaluation) |
| A33 | 27B需52GiB | **历史卡确这样写，不能当当前精确占用** | v1.2卡确写约52GiB；v1.3写约49GiB。当前index声明total_size=52,170,660,320 bytes＝52.17GB＝48.59GiB，另加working memory。这里核的是index元数据，不是实测RAM/VRAM；不能混GB和GiB。[v1.2 Usage](https://huggingface.co/perplexity-ai/pplx-decider-v1.2/blob/cce0f3f80033e9d89d80831d5281fd72124aacce/README.md#usage)、[v1.3 index](https://huggingface.co/perplexity-ai/pplx-decider-v1.3/blob/9c2ebb27470d3dec2ad7ab727727e40d142c7213/model.safetensors.index.json) |
| A34 | Intern七组90.02对88.74，可称4B级别最强 | 数值有出处，最强结论未建立 | 是不加权七套文本均值；同一JEVal表SII-4B又高于Intern4B，因此没有跨任务的4B最强。开发暴露／checkpoint和backend另有边界。 [官方Accuracy协议](https://github.com/InternLM/Intern-Decision/blob/a7b01e276cd5e18bae640be925e685ba6f5159ad/README.md#benchmark-accuracy) |
| A35 | Intern44ms对Jev110ms | **需完整计时条件** | 官方为RTX4090、BF16、native HF、289输入tokens／3字段，Intern4B mean44.16ms；Jev mean109.70ms为托管调用。不是同硬件的纯模型对照，亦非M5表现。[官方Latency](https://github.com/InternLM/Intern-Decision/blob/a7b01e276cd5e18bae640be925e685ba6f5159ad/README.md#rtx-4090-inference-latency) |
| A36 | Intern仓库没有LICENSE | **当日错误，且不是今日刚增加** | 当前root为Apache-2.0；许可证引入提交3572c8a，时间**2026-09-29 08:43:48 UTC**。模型卡也声明Apache并保留Qwen许可证。此前“没有许可”属于过时／漏核。[固定LICENSE](https://github.com/InternLM/Intern-Decision/blob/3572c8a68b5df5dafe02d0e093989ba8ec0183bc/LICENSE)、[模型卡](https://huggingface.co/internlm/Intern-Decision-4B/blob/38c9dafbbef52dd04bae943c0c6ac918419adfd5/README.md#license) |
| A37 | Intern有CE＋校准及XTuner流程 | 成立，不能换成通用Mac LoRA承诺 | 官方配置训练语言骨干、冻结vision／projector，Linux／CUDA／XTuner；自有预备数据可接入，完整原数据未公开。 [Training on your own data](https://github.com/InternLM/Intern-Decision/blob/a7b01e276cd5e18bae640be925e685ba6f5159ad/README.md#training-on-your-own-data) |
| A38 | Chinese-Jev用10M样本 | **论文作者报告成立，需分阶段** | 10M是General阶段；Medical／Legal／Finance为后续各自适配，不等于每个领域都有10M真实企业记录。[论文v1 §3／A.1](https://arxiv.org/html/2609.36965v1) |
| A39 | 医疗领域比Jev高4.0% | 若指相对增幅则成立 | 87.65对84.29是+3.36个百分点、相对约+4.0%；原文的百分比不能改写成+4个百分点，法律／金融也并非全面优于Jev。 [论文v1 §4.2 Table2](https://arxiv.org/html/2609.36965v1#S4.SS2) |
| A40 | Chinese-Jev平均15ms | 需限定计时边界 | 为作者本地encoder协议，Jev比较含网络；不是手机或完整生产流程统一延迟，iPhone浏览器另约1秒。 [论文v1 §4.2–4.3](https://arxiv.org/html/2609.36965v1#S4.SS3) |
| A41 | CJ-Medical产物不明；本仓此前称行业权重仍planned | 现可确认；本仓旧说法错误 | CJ-Medical在10月18日已由官方README链接发布，卡声明Apache-2.0；这不是11月20日新增。仅核卡／元数据，未下载或认证论文原权重。 [引入提交](https://github.com/gulucaptain/Chinese-Jev/commit/02a84752a7915a6c66baf434e6d58ea5909f1e0e) [固定CJ-Medical卡](https://huggingface.co/bbldCVer-hf/CJ-Medical/blob/1ae360b3ec9927622dd82f1430f0111f292ee17f/README.md) |
| A42 | 商业使用只核权重许可证即可（实施边界） | 不充分 | 具体权重、代码与混合数据来源需分别核查；Apache元数据不能代替全部来源及使用条件。 [CJ-Dataset Use and licenses](https://huggingface.co/datasets/bbldCVer-hf/CJ-Dataset#use-and-licenses) |
| A43 | AutoTrust使用Jev分布，有服务条款风险 | 有依据的风险提醒 | 作者卡说明含Jev分布；TypeSafe现条款有限制，但特定主体的采集时合同和单独授权未知。本轮不裁定已构成违约。 [AutoTrust固定卡](https://huggingface.co/autotrust/AutoTrust-Decider-Pro-27B/blob/14b425269ed24452e0a5ad5a8f3e51d139647a88/README.md) [MCA](https://typesafe.ai/legal/mca) |
| A44 | Decision3.0只在X上，没有正式资料 | **错误** | 项目官方已有模型卡、架构／运行文档、Apple Silicon文章与服务说明。“是否有完整同行评审训练论文”可另列未确认，不能写成无正式可读资料。[官方D3文档](https://vllm-sr.ai/docs/model-runtime/supported-models/decision-3/overview/)、[官方Mac文章](https://vllm-sr.ai/blog/decision-3-0-on-apple-silicon/)、[官方HF](https://huggingface.co/vllm-sr/d3) |
| A45 | ≤2B只适合边缘，不值得生产验证 | **错误绝对化** | 大小决定资源边界，不单独决定适用性；稳定短任务、训练数据与错误成本都可能使小模型合适。Strands本身以实验可承受和有用决策为2B动机；复杂／长状态仍可能需要更大模型。须任务配对比较，不能由尺寸作生产结论。[Strands Why2B](https://github.com/strands-labs/strands-decider/blob/7e8380ca64604a5be3dc954e726173fa1acb6c73/README.md#why-2b) |
| A46 | 先选榜单赢家，再LoRA／蒸馏即可 | **不可直接推出** | 零样本强弱、可训练契约和适配后学习曲线是不同问题。应限定候选、同数据／预算做Dev比较，保留原模型，冻结后一次最终Test；LoRA和蒸馏不是通用修复按钮。[Perplexity作者选择建议](https://www.perplexity.ai/en-GB/hub/blog/perplexity-decider)、[Kev域适配合同](https://github.com/jaredpalmer/kev/blob/051142bf849c2c6ad3f23e17a7b5aea2686d9a91/skills/kev-finetune/README.md) |
| A47 | SII自蒸馏适合少标签企业数据 | 可研究，非即用承诺 | 与M23–M24一致：不用人工gold作蒸馏target，不等于可省教师／p0／参考验证；完整代码入口与目标企业有效性分别确认。[官方训练说明](https://github.com/amazingljy1206/SII-Decision/blob/1723d83cbda69f48641c273280b5a2d06d6b3510/README.md#training) |
| A49 | 政治学七项复现中Jev校准较GPT好、非稳定胜Qwen、无batch成本优势 | 成立，限当时比较 | 论文摘要确这样报告；token概率、单次请求、batch价格及政治学任务范围不能省略，不能推广成全部负面结论。[原论文](https://arxiv.org/html/2610.06625v1) |
| A50 | 钓鱼Jev62.6%对两行规则91.8% | 需匹配分母并保留正反结果 | 62.6是2000封的直接verdict；91.8来自独立半集B1000封，规则全2000为91.6。同面板Jev信号＋回归在B为95.0；不应只摘两值当所有用法同条件胜负。[原作者README](https://github.com/anisselbd/jev-phishing-bench) |
| A51 | Jev类型化概率输出，不生成回复；Transformer但不是LLM | 输出合同成立，内部架构须谨慎 | 官方可确认不生成字符串、并行query；具体架构未公开，不能由API合同或其他开源实现反推所有内部结构。 [官方发布](https://typesafe.ai/blog/introducing-system-one-models-and-jev) |
| A52 | 所有encoder最快；Laya.362接近随机、适配.766 | 需限定 | 两值来自四个合成workflow的400case／2000判断；多数类基线为.461，不能当所有任务的无训练上限。硬件、长度与batch未匹配，不能宣布encoder永远最快。[历史E01](evidence.md#e01) |
| A53 | Laya非拉丁文字会彻底失效，Khmer0／confidence.952 | 个别切片可报告，整体推论过强 | 必须固定English检查点、语言／任务及样本数；不能从单一Khmer切片推出全部非拉丁文字或多语种版本均失效。[所引模型卡](https://huggingface.co/Emerald7664/laya) |
| A54 | Nimble用2676条最小事实差异样本训练 | 成立，需限定数据身份 | 是合成训练集／数据构造，不是独立人工金标或表示层contrastive loss；数量不证明对所有任务都充分。软标签／均匀目标的其他主张分别见M32–M33。[固定卡](https://huggingface.co/bespokelabs/Bespoke-Nimble-9B/blob/bd792f44ec8e265be861bfcdf4e05967ffe0e858/README.md) |
| A55 | 百炼部署实例21元／小时、10139元／月 | 成立，限给定部署规格 | 原回复这里确写部署价格；需保留MU规格和准入条件，不能将该价当训练／数据／调参／推理总成本。 [官方指南](https://help.aliyun.com/en/model-studio/decision-model-tuning-guide) |
| A56 | 先百炼、再LoRA、最后RL是企业默认最优路线 | 未证实 | 可以分别作为有条件试验；托管准入、数据治理、标签和硬件决定选择，没有这条串联链已获目标企业验证。当前候选角色见[总览](decision-model-posttraining-enterprise.zh-CN.md) |
| A57 | 问题ID／类型／说明／选项一变，就必须重训 | 错误通则 | 特定托管服务的训练schema受约束；不等于所有动态候选模型一改便重训。重验与重训分开，1–2周之类时间为规划建议而非实验事实。  |

| A58 | train-jev把Jev分布蒸馏到Qwen3.5-4B | 有相应代码／作者声明 | 当前仓还支持27B及24-slot head，基于公开distill corpus及混合金标；不等于复现官方RLCD或已获所有来源授权。条款风险见A43。[作者训练说明](https://github.com/shibing624/train-jev#训练自己的业务模型) |
| A59 | 现成Qwen不训练直接读概率；概率没校准只能当排序 | 前半成立，后半过强 | 未校准不能直接担保业务风险，但不能先验断言完全没有概率用途。所引项目是逐候选补全log-likelihood＋长度归一化，不应冒称单个答案token一次读出。[原项目机制](https://github.com/I-You-Dream/jev-from-scratch#技术方案) |
| A60 | 百炼单次最多16题，北京与新加坡可用 | 有官方来源，端点／准入另验 | 原生API明确最多16题；微调指南区分北京控制台与新加坡OpenAPI。原生API写Bearer、微调指南示例用裸key，本轮未发带密钥请求裁定两者是否都接受。[API限制](https://help.aliyun.com/en/model-studio/decision-model-api)、[微调指南](https://help.aliyun.com/en/model-studio/decision-model-tuning-guide) |
| A61 | Jev没有公开本地权重／训练路径 | 本轮未找到相反产物 | 官方可查路径为托管API及不做客户权重适配；没有公开权重证据不等于证明任何私有企业部署安排绝不存在。[Models](https://docs.typesafe.ai/models) |
| A62 | 中文仍有缺口，多数开放模型主要英文 | 需数据组成与任务限定 | 目标中文客服验证仍缺；但已存在中文评测与CJ中文数据／权重，不能由单个issue或模型语言声称推导整个生态的训练比例。具体看精确版本和独立中文切片。 |
| A63 | “Kev不如PPLX／SII、Intern是4B最强”的后训练排序 | 未建立 | 混用了榜单、尺寸和训练暴露；零样本名次不决定标签效率、适配后风险与完整成本。PPLX缺现成完整训练器也会影响实施排序，不能只按初始分数选赢家。 |

## M. RLCD、监督目标、基座和旧版数值

依据：[Inner Jev正文与附录B／E–H](https://arxiv.org/html/2610.17205v1)、[PRDO v1](https://arxiv.org/html/2609.38850v1)、[CAPS §3–5](https://arxiv.org/html/2611.15572v1)、[JEVal §4／6和附录F](https://arxiv.org/html/2610.03935v2)。更完整原表见[方法审计](decision-model-posttraining-method-audit.zh-CN.md)。

| ID | 被核查主张 | 判定 | 校正与适用条件 |
|---|---|---|---|
| M01 | Jev被理解为JEPA／世界模型 | 错误 | 用户给定的是TypeSafe Jev；JEPA不是该产品或其训练法。最初澄清范围合理，直接将JEV认成JEPA不合理 |
| M02 | 官方算法不公开，所以RLCD本身用不上 | 需限定 | 不能还原TypeSafe内部配方；独立的OpenJev／PRDO代码仍可研究，不能称复现了官方Jev训练 |
| M03 | 用2610.04985支持官方未公开配方；2609.28940支持proper-score“社区共识” | 来源层级／共识表述需限定 | 两篇分别是安全／隐私与渗透测试harness研究，非TypeSafe一手训练规范。可作背景，不据此认证官方精确算法、数学等价或统一社区共识；应回到官方披露与具体方法论文。[前者](https://arxiv.org/abs/2610.04985)、[后者](https://arxiv.org/abs/2609.28940) |
| M04 | 直接读出时RLCD梯度等于监督Brier | 需限定 | 完整外生标签、指定评分、直接对分布求导且无参数依赖采样路径时可写成监督损失；有随机推理／动作采样时还要区分pathwise与score-function项 |
| M05 | CLINC／ChaosNLI局部负结果证明客服CE够了、RL不会更好 | 错误 | 只支持对应底座、预算、loss及任务的比较；没有覆盖中文企业动作、业务效用或全部RL方法 |
| M06 | Inner Jev的损失比较“输出头冻结” | 错误 | 附录F的该早期实验冻结的是主干，训练上方读出；不能与主文LoRA训练混表 |
| M07 | CE／Brier／Focal／MMCE／效用表中的数字 | 成立 | 78.5／79.6／76.3／78.8／79.4及所贴ECE出自表16；accuracy为七组macro，ECE为六个hard-label集均值；种子数不同，部分只一seed |
| M08 | 最后Top3段称“换损失函数没用”，理由是ECE最多只低约.01 | 错误外推 | .01是该面板的均值观察；早前局部数值可保留，但不能证明accuracy、排序、稀有风险或其他数据／参数化均无收益 |
| M09 | v1 GSM的70.4／91.8／92.2、MMLU的42.3／42.4／47.7及Brier | 需限定 | 确为v1表；SFT直接答、其他臂生成推理，且两阶段800更新对400，不能当完全等算力比较或最新主结果 |
| M10 | v1的81.1%对19.4%可作为上线5%风险覆盖 | 错误 | 是使用测试标签选前缀的oracle coverage；不是冻结阈值的部署覆盖或有限样本风险保证 |
| M11 | 去KL约100步推理崩；偏知识任务第二阶段几乎无增益 | 旧版局部观察需限定 | 前者对应v1特定从头端到端实验，后者是该版本／预算的阶段比较；不是v2所有任务的结果，也不能推出普遍必需KL或阶段二无效 |
| M12 | RLCR的HotpotQA62.1%／ECE.03对63.0%／.37 | 需限定 | 本次在[RLCR arXiv v2表1／附录E.3](https://arxiv.org/html/2507.16806v2)复核相同数值；模型生成分析和显式置信度，非零生成读出。OpenReview阻挡后使用原作者arXiv版本，未借二手转述补证 |
| M13 | CAPS使Banking77比positive-only SFT高2.6pp、ECE低.053 | 成立 | 0.6B、N=5000；每题gold＋8个干扰项＋other，共10选项，非完整77-way。.931／.025对.905／.078，三seed对一个基线seed；完整标签SFT为.946／.022 |
| M14 | 完整标签下，测试的四种bandit方法都没赢CE＋温度 | 需补指标和总体 | 原文限定四个未见schema的平均ECE；不能理解成所有指标、任务或budget都未胜出 |
| M15 | 不能把所选动作概率当REINFORCE奖励，.636降到.111 | 奖励身份需校正 | 崩塌用的是对自身采样概率计算、再detach的特定Brier奖励，不是简单用原始概率；同文奖励r和r−p也避免崩塌，不能据此禁止所有策略梯度 |
| M16 | 土耳其语REINFORCE准确率掉10.2点，校准指标变差 | 指标名称错误，局部退化可保留 | 10.2pp指macro-F1，不是accuracy；是特定线性概率奖励的REINFORCE。该组校准指标也确变差，但不能外推全部RL。[表4](https://arxiv.org/html/2610.06744v1#S7.T4) |
| M17 | Qwen3.5规模曲线48.9／57.6／76.8／82.2／86.5 | 需限定 | 图5的七组零样本macro曲线支持这些约数；没有比较企业适配后的最优尺寸，也不能推出≤2B只适合边缘。MoE按active参数画，模型族也影响结果 |
| M18 | base70.3低14.1，故推荐对话版 | 模型／指标需纠正，推荐有条件 | 是Gemma 4 31B在该配方下的OpenDecisions Capability，不是Qwen准确率；原结果支持该设置内优先instruct，但不能替代目标底座／prompt／预算的比较 |
| M19 | 对话版的过自信可由一个温度修好 | 错误 | 温度只拟合特定校准分布上的映射，不能修复错误证据、全部排序或分布迁移；“能修好”需独立验证 |
| M20 | Jev88.0/.066、Qwen3.6-27B88.3/.052→89.4/.064、4B85.0/.080 | 需限定 | 原文外部七组任务结果，不是OpenDecisions Capability；不同现成模型的对照不能识别底座／loss的单独贡献 |
| M21 | JEVal的9457英＋1800中，以及所贴六模型accuracy／ECE | 需限定 | 总题数正确；accuracy只算10938个choice/noul且invalid计错，ECE仅有效输出；不能把数字当纯中文客服成绩 |
| M22 | SII-27B ECE.0149为该表最低 | 成立 | 仅该JEVal表及被测配置内；不能由此推出中文证据最好、企业风险最低或商用底座第一 |
| M23 | SII两次思考分布均值→无思考student、非RL、39279题 | 成立 | 是同尺寸reasoning-to-readout蒸馏；39279是27B设置，非所有尺寸，亦非“只需任意少量数据” |
| M24 | SII不用人工正确答案，少标签业务可套用其方法 | 原理有依据，实施条件需补齐 | 蒸馏target不是人工gold；公开loader仍要求gold_target／train_target／p0，并用于hard-Noul权重／验证。gold字段也不自动意味着必须人工产生；需明确语义、教师与起点，不能省略整个数据合同 |
| M25 | SII只比模型，没有方法消融 | 错误 | 论文比较Full／LoRA、数据规模及教师／蒸馏行为；不等于做过与PRDO／RLCD²的匹配方法比较 |
| M26 | τ-bench更快但成功率下降，所以别把多轮整体全交它 | 特定实验与谨慎建议可成立 | 77.6→66.1来自特定动作选择器替换；中位episode更快、p95更慢，不是每轮普遍提速。它支持系统级验收，不能解释为禁止任何决策模型参与多轮规划 |
| M27 | 统一LoRA、学习率2e−5、训练400步即可 | 错误 | 400步是该固定WSD日程的终点，原配方不早停；4B还改LR／教师混合／格式。领域实验可另定Dev选择规则，但不能把它称原法或套通用400步 |
| M28 | 只训输出头几乎没有提升 | 成立于所引Gemma消融 | 该设置可支持LoRA的重要性；将其直接搬到另一encoder／领域／标签需要再验。head-only可保留为便宜对照，不应预先认定必无效 |
| M29 | 温度不得低于1 | 错误 | T应为正。论文T≥1是迁移失准后的保守实现措施，不是理论约束；欠自信可能需T<1 |
| M30 | 温度不改排第一答案，只调自信程度 | 单题argmax解释成立 | 同一题单一正温度保持argmax；另需留意ordinal期望分、跨题排序、多阶段融合和实际阈值策略，不将这些额外提醒说成原argmax解释错误 |
| M31 | 小于1个百分点基本是噪声 | 错误 | 看独立案件、配对区间、种子、功效及预定有用差异；没有通用1pp统计界线 |
| M32 | 教师软标签直接教会真实校准 | 错误 | 首先学到的是教师分布；logits、重复采样频率、口述confidence、真实结果率不同，须用独立业务标签验证 |
| M33 | 加均匀target的无法判断样本降低过度自信 | 可作训练假设／正则，需领域验证 | 来源有此建议，但均匀目标不自动是真实概率；unknown、OOS、多合法项、缺候选、事实冲突等应分别定义与验收，不能由该建议推导拒判风险保证 |

| M34 | “领域2026年9月才出现，没有统一公开评测” | 先界定领域和“统一” | Jev发布日为9月15日；若指分类／概率校准学术史则并非新创，若指当轮Jev产品生态应按具体发布记载。已有JEVal／DI等公开评测，但它们不等于统一企业效度标准。[Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)、[Guo等2017](https://proceedings.mlr.press/v70/guo17a.html) |

| M35 | 推理类后训练必须加KL、需要27B级别 | 错误通则 | KL有任务／阶段条件，PRDO主实验本就用0.6–3.8B；是否保留推理及所需尺寸应按领域效果与资源比较，而非规定27B起步。 |

## P. PRDO与StartLux的比较中，PRDO部分

依据：[PRDO v2 §4–6及附录A–G](https://arxiv.org/html/2609.38850v2)。本节仅核该论文；两套方法没有同数据、同底座、同预算的直接胜负比较。

| ID | 被核查主张 | 判定 | 校正与适用条件 |
|---|---|---|---|
| P01 | PRDO是训练方法，不能与完整模型直接排榜 | 成立 | 比较对象不同；论文没有提供击败Jev／StartLux／SII／Kev的领域后训练实验 |
| P02 | 只做MMLU-Pro和GSM8K-Verify，全部只三seed | 错误 | 主设置四个0.6–3.8B底座；还有ARC／SVAMP迁移及ChaosNLI，探索验证追加到五seed；不能说验证完全只有两个数据集 |
| P03 | 每条推理后Answer标记读候选token分布，argmax为答案 | 成立 | 是固定答案槽位读出；有限生成预算／强制marker及候选token化都属于协议 |
| P04 | 第一阶段不奖励推理文字，只训练概率 | 需限定 | 无推理score-function奖励，但读出和推理共享全部权重，pathwise与token KL仍更新这些权重；不是冻结推理模块或只训head |
| P05 | 第二阶段可选、c=.3 | 成立 | 是在阶段一上另加400步score-function项，预算从400变800；不能把其效果与单阶段混合报告 |
| P06 | 四底座MMLU Brier−.068至−.080、AURC−.106至−.161 | 成立 | 对GRPO＋TS的八项主要比较均过Holm且三seed同向；不是相对所有其他家，亦非完整算力成本匹配 |
| P07 | MMLU四底座都显著变好，accuracy提高2.6–4.1pp | 主要指标成立，accuracy另论 | 显著性主要指Brier／AURC；accuracy均值方向正确，但为次要指标，1.7B层级区间跨0，不能将前半显著性自动扩到每一accuracy比较 |
| P08 | 0.6B数学验证accuracy−2.7pp、1.7B无显著差异 | 成立 | 支持排序与解题能力可分离；追加seed和迁移还出现负accuracy，必须保留 |
| P09 | 错答中≥.99置信的60.6–68.5%对.3–1.2% | 成立 | 是MMLU-Pro原始未缩放概率下的错答占比；后一数字属于Brier目标训练模型，不是“Brier分数只有.3–1.2%” |
| P10 | 所以所有GRPO都不能用，温度完全修不回来 | 错误 | 该研究温度改善概率尺度而未恢复错误排序；不能泛化全部GRPO／奖励／底座，更不等于温度对概率质量无效 |
| P11 | RLCR和CREDO都只用文字报置信度 | 错误 | RLCR用显式报数；CREDO为自分析后专用high／low槽位的logit差读出，另有未调优／排除崩塌run的边界 |
| P12 | 恰当评分唯一稳定价值是coverage@5% | 错误 | 最强主证据是Brier与AURC；5%处所引覆盖是测试oracle；正式固定阈值认证另报10%／20%，不能移作5%上线保证 |
| P13 | PRDO第一阶段可作为普通事后校准 | 错误 | 它更新模型权重；温度校准是不同步骤。只因ECE高就加PRDO不是论文已经验证的选择规则 |
| P14 | 可以把StartLux按需推理和PRDO叠加，并会补上短板 | 未证实 | 是可提出的实验假设；两者的冻结评分器、共享权重、gate与融合／校准合同不同，没有组合后的训练或效果证明 |
| P15 | PRDO只适合算术／复杂退款规则 | 错误 | 有效准入是部署保留推理并按其后分布接受／转交；主要支持来自知识选择题，数学反而暴露退化 |
| P16 | 400步0.7–2.3小时、用两张48GB Ada，所以成本低 | 错误 | 每run用“两张中的一张”；Qwen为.7–2.3h，3／3.8B为3–4.5h，thinking约10h，另加评估和125GB主机内存。不能外推M5统一48GB |
| P17 | 只要proper score就保证概率诚实 | 错误 | 严格恰当性是指定分布／报告空间下的期望最优性质；有限数据、模型失配、优化、选择和漂移均可能使部署失准 |

## L. StartLux论文、榜单、许可与配方

本节来源键：P＝[StartLux v2正文与附录](https://arxiv.org/html/2610.17309v2)，G＝[当前代码a99977d](https://github.com/StartLuxLabs/StartLux-Decision/tree/a99977d9332decc9fb27a2488b4a83b533b6cd5f)，D32＝[10月16日DI0.3.2固定汇总](https://huggingface.co/spaces/multimodalart/jev-decision-index/blob/8568068ff617fcbafcf26c30770f6b0c415be59c/data/v03.json)，D41＝[11月19日DI0.4.1固定汇总](https://huggingface.co/spaces/multimodalart/jev-decision-index/blob/4ee57a1610e0547634ba0ec11990d10122672191/data/v03.json)。M32／M41为对应提交下的`methodology.html`；C27／C4为[PPLX27B v1.2](https://huggingface.co/perplexity-ai/pplx-decider-v1.2/blob/cce0f3f80033e9d89d80831d5281fd72124aacce/README.md)／[Flash v1.2](https://huggingface.co/perplexity-ai/pplx-decider-flash-v1.2/blob/9ff7cf9838e59df461c276b7699d56b244d2af58/README.md)卡片。榜单仅重算公开汇总的排序，没有重跑private题。

| ID | 被核查主张 | 判定 | 校正与定位 |
|---|---|---|---|
| L01 | “DI0.3.2，10月16日，174模型，27B以69.12第一” | **正确，严格限历史快照** | D32共有174 rows，engine=`startlux-decision-v1.1-27b-instant`，`v=69.12, rank_v=1, rank_tie=1, tied=false`。这是**Instant**，不是论文AutoThink73.37 |
| L02 | “三个部分都是第一” | **正确，限D32 raw点估计** | 同row public72.88、same64.82、new61.41分别等于174row各栏最大值。未据此建立每个private部分的成对统计显著性 |
| L03 | “私有占80%，所以比论文数字更可信” | **条件成立，后半不能绝对化** | M32 Full为public20%、same-private50%、new-private30%，有降低公开测试记忆／选择影响的设计价值。但private题／完整原始运行未公开，本仓不能审计其标签、污染、覆盖及可重现性；同技能private也不等于目标企业新域。应写“比仅看作者public开发分更有参考价值的一条证据”，不能升级为已验证企业泛化 |
| L04 | “现在仍是第一／有授权就首选” | **错误／未证实** | D41 327rows，StartLux27B Instant Full67.92，原始序位29、网页并列组`=6`，不再第一。榜单协议也从0.3.2改为0.4.1，不能把排名变化归为模型退步。许可不证明领域质量、适配能力、成本或硬件可行性 |
| L05 | 用65.5／61.5及68.09／58.88支撑跨家排序 | **错误：Full/public、版本、请求模式混用** | D32 PPLX27B v1.2 **Full65.55**，Jev1.14 **Full61.53**；C27/C4的68.09／58.88是作者public-suite的**joint**请求结果。Flash在D32 Full54.81。下表分开 |
| L06 | “八个模型为CC BY-NC4，代码Apache2” | **正确，核实际文件** | 5个Instant（0.8/2/4/9/27B）+3个AutoThink（4/9/27B）。8个固定HF repo均有相同CC BY-NC4 LICENSE和NOTICE；GitHub root LICENSE为Apache2，pyproject亦如此。权重条款不能被代码条款覆盖。P附录A.4、G README License及各HF LICENSE/NOTICE一致 |
| L07 | “不能商用” | **条件成立** | 公开权重许可提供非商业用途；NOTICE/模型卡明确商业使用另向StartLux取得许可。不是商业授权永远不存在，亦不是发邮件咨询就已经获得权利。本审查未联系对方、未核任何商业合同 |
| L08 | “基座模型没有公开名字” | **前半需精确化** | 8卡`base_model`未填，config无`_name_or_path`，未见精确upstream model ID/revision；但config明确`model_type=qwen3_5`、架构`Qwen3_5ForConditionalGeneration`，NOTICE保留Alibaba Cloud版权。可说“缺精确可追踪基座身份”，不可说毫无线索，也不能由架构反填某个Qwen权重SHA |
| L09 | “Instant双向attention” | **条件成立** | P§2.2／§2.3.2／B.1：只移除**full-attention层**prompt因果mask，linear-attention仍因果；4B/9B为32层中的8层。整个state+单题+候选prompt双向；不是所有层双向、不是多题共享一次编码，也不是仅推理时临时改mask |
| L10 | “AutoThink threshold=.9、alpha=.75” | **论文正确，当前默认不同** | P Eq2／§2.2的论文评测gate .9、p_final=.25p0+.75p1。G `docs/api.md` Controls/Model folder和README现默认gate **.6**，mix .75，budget4096。用户可覆写，不能用默认请求声称复现论文值。触发看`max(p0)`，并非API返回的归一化`confidence`字段 |
| L11 | “270万SFT数据” | **条件成立** | P§2.3.1／A.2表A.1：0.8–9B约270万；**27B约80万**，分布配比也不同。全语言参数含输出projection，vision冻结；不是全视觉参数训练 |
| L12 | “170万adapter数据” | **正确，为Stage2作者披露** | P§2.3.2：Lux-Rounds约170万，adapter训练后merge；Instant改attention，AutoThink仍因果。Instant0.8B平均3个seed，2–27B平均4个seed，再拟合温度。资料说明不是公开完整混合数据可精确复训的证明 |
| L13 | “推理SFT再RLCD²” | **正确，需补起始点与规模** | P§2.3.3：LuxThink每模型约4000–21000监督推理样本，adapter合并；再RL。AppendixB说明Stage1和RL全语言参数更新，Stage2／reasoning supervision用adapter；全程vision冻结 |
| L14 | “RLCD²用概率改善减长度罚” | **正确，需保留关键差别** | P§3.1 Eq5：r=S(p1,t)−S(p0,t)−1e−4 max(0,L−B)，两次概率由**冻结的reasoning-SFT起始模型**评分。release用decision-weighted proper score（uniform和Beta(8,2)等权混合；ordinal用累计概率），B=3072为soft罚预算，不是生成硬上限4096 |
| L15 | “只训练不确定问题” | **正确** | P§3.2：初判max<.9；≤8token trace作empty、reward0；同prompt采样G条，A=clip(r−组均值,−5,5)，不除组内标准差，PPO式clip surrogate+reference KL。对全非空组S(p0,t)常数在中心化时抵消，不能把差值形式解释成额外可辨识的每trace因果价值保证 |
| L16 | “73.37对57.96，4B67.88” | **正确，限表4public protocol** | 73.37为27B AutoThink，67.88为4B Instant，Jev57.96为旧public参考；是机会校正的weighted skill points，不是普通准确率%，不是当前Full榜同条件赛跑 |
| L17 | “DecisionPivot86.9对GLM82.2” | **正确，限作者bench与pair accuracy** | P§4.3／图9：7800items、13任务族、每族600；通常contrast pairs，两条都对才算pair正确，再按族平均。27B AutoThink gate.9=86.9；GLM5.3 reasoning=82.2；Instant75.4。作者称未用于数据／checkpoint／config选择，但benchmark与模型同作者，不是第三方复现 |
| L18 | “9B trace−65%、结束45.9→93.9” | **正确，限专门诊断** | P§3.3表2：2986保留训练分布样本，去掉35重叠，每题强制推理、一条trace、硬上限4096；2494→868均长，45.9→93.9终止。不是线上每请求端到端延迟减少65%，也不是整个模型族统一数字 |
| L19 | “4B ECE2.4对Jev13.8” | **正确，限DecisionPivot** | P§4.4图11：7800core、15confidence bins，以max option probability为confidence；4B AutoThink gate.9 ECE2.4pp，Jev13.8pp。不是所有任务／当前企业分布，也不能同下行4.0作同一个指标相减 |
| L20 | “AutoThink最终输出过自信4.0pp” | **错误归属** | P§5.5：4B **post-reasoning readout**在2986保留样本上的signed mean confidence−accuracy=+4.0pp；不是最终gated＋fused分布的全局量。默认最终输出ECE4B/9B/27B为3.7/2.2/1.6pp，post-reasoning ECE8.1/3.7/2.8是又一口径；ECE绝对分箱差不等于signed过自信 |
| L21 | “同类任务+8.6、异类+.3” | **正确，限受控追加数据实验** | P§5.1：4B增加rating/safety/preference/logic家族Stage2数据，18对应任务+8.6，非这些家族任务+.3；其余数据组也未见清晰外族迁移。支持任务家族专化风险，不是“永远不能迁移”的定理 |
| L22 | “没有覆盖客服” | **绝对说法错误，实际目标仍未证实** | A.3／D.1包含BANKING77、CLINC150意图类和工具任务；DecisionPivot有policy/tool-call结构题；G归档finetune还给synthetic ticket示例。但没有目标企业中文客服历史会话的同预算后训练对比、真实业务收益或生产风险证明 |
| L23 | “top25 keep3 tournament” | **需校正用词** | P§2.2／D.4和G api/modelcfg/pipeline：**每组至多25**候选，每组留3；单readout通常至多26。当前若晋级>26再截取26，未晋级项共享0.001 residual，最终可能AutoThink。不是先取全局top25；no-answer extra会占最终名额，26候选也可能需tournament。D.4报告151选项下4B86.7对26选项95.7，非免费可扩展能力 |
| L24 | “本质是PRDO工程化” | **错误／未证实的简化** | StartLux P§3明确引用早期OpenJev-RLCD，但自己的RLCD²以冻结judge给trace奖励，再policy-gradient更新推理policy。当前PRDO v2主阶段是对每条实际推理后的readout作exact-gradient proper score，并以token-KL锚定共享模型，主阶段不奖励推理；可选第二阶段才加score-function项。更不用把其双向Instant、三阶段数据、权重平均和校准折成一个方法。StartLux v2为10月20日、PRDO v2为11月1日，不能用后者新命名倒推完全同源工程封装 |
| L25 | “RLCD²主要缩短，准确率变化都在误差范围” | **错误绝对化** | P表2在2986训练分布heldout的default accuracy变化置信区间含0；但DecisionPivot 9B pair53.3→59.9（+6.6，区间+5.0至+8.3），4B512预算60.4→52.9；长计算子组也可降准。应写“主要稳定收益是终止／效率，质量变化依规模、数据、预算，可正可负” |
| L26 | “proper score天然让输出校准，按题型temperature就够” | **错误** | P§5.4–5.5、AppendixC专门展示selection／routing破坏边际校准；per-type T不能保证top-N选择、reasoning-route、cascade之后风险。proper objective的理论激励不等于有限样本＋分布迁移的生产保证 |
| L27 | “有许可就应排第一” | **未证实** | 许可、部署合同、原始数据/训练器、中文企业质量、风险覆盖与真实延迟仍须分别验收；历史27B榜首不能迁移到4B的企业标签效率。取得授权后可纳入匹配组，不能由授权状态替代实验 |

数字合同另列：论文public的27B AutoThink **73.37**／4B Instant **67.88**与旧Jev **57.96**，不是D32 Full的27B Instant **69.12**／PPLX1.2 **65.55**／Jev1.14 **61.53**，也不是PPLX卡片joint-public的 **68.09／58.88**。D32先按stock-base刻度映射再20／50／30加权；D41则纯private 60／40，题目与刻度也变了，不能相减当模型进退步。

v2另外表明**选择策略会改变校准对象**：按route／routing-confidence分层做isotonic，best-of-N另用候选数等特征拟合，再按route选择风险阈值。它没有证明固定.9 gate最优，迁移仍有残留失准。这直接反对“按题型温度即可长期通用”。

完整v1.1三阶段／RLCD²训练器及混合原数据未在当前公开树定位；归档`v1/finetune`是旧版文本LoRA，不能换一个权重名就称v1.1复现。论文M5 Pro **64GB推理**也不是用户M5 Pro **48GB训练**证据。


## R. 意图路由案例、分层及微调风险

本节定位：CLINC＝[2610.00346v2](https://arxiv.org/html/2610.00346v2)，LLM-as-Jev＝[v2](https://arxiv.org/html/2610.02076v2)／[当前v3](https://arxiv.org/html/2610.02076v3)，Fast Models＝[2610.02267v1](https://arxiv.org/html/2610.02267v1)及[固定分析代码e74dfb6](https://github.com/David-DL-Space/sys1-eval/tree/e74dfb6d99ed041f5f5240af386ba5272de84cdd)。Laya表来自[固定README76c9184](https://github.com/NandhaKishorM/laya/blob/76c9184871feac23609362315cb40f9c32caafc6/README.md)和[vegaml 8b0ca58](https://github.com/NandhaKishorM/vegaml/tree/8b0ca58e8d92ac3fc9c5cc682c93aebc7b885a20)。

| ID | 原主张／实施边界 | 判定与校正 | 原文／产物定位 |
|---|---|---|---|
| R01 | 600条ID＋200条OOS，150意图、10域 | **成立。** 150意图各4条形成600条ID；另有200条OOS。层级结构10域×15意图。主表准确率只算ID600，不是800题含OOS的总正确率。 | v2 §4、表5；冻结`d2_k150`及`d2_hier_*`输入 |
| R02 | flat DeBERTa .953、BGE .948、BERT .940、Gemma .942、Jev .913、decider .860、Kev .850 | **数值成立，训练身份不能省。** DeBERTa/BERT使用任务标签；BGE是冻结embedding上训练logistic regression，不是BGE零样本；decider/this-that有相关训练暴露。Gemma-4-31B的.942为verbal读出，likelihood是.940；Kev为该实验的9B检查点。 | v2表5、§4及§5.1 |
| R03 | Jev hierarchy .673、domain .703；Kev hierarchy .602 | **成立。** Jev为404/600联合正确、422/600域正确，gold域细分为567/600；Kev-9B联合361/600、域390/600。不是只看细分一步。 | 表8；作者`a03_e3_cardinality.py`与公开逐题输出，见下方复算 |
| R04 | 第二步在正确域中选、两步误差相乘 | **需精确区分。** 离线第二题确用gold域菜单，但hier分数是域对且细分对的交集。Jev细分整体567/600，域正确子集404/422≈95.7%；.673是404/600联合值。应使用正确率的条件链式法则，不是两步错误率相乘或假定独立。 | 命题2及附录证明；`e3_cardinality.json`保留域/细分/联合三项 |
| R05 | Jev OOS误接受31%降至19.5%；Qwen3.6为3.5% | **有条件成立。** 前后均是面向ID风险目标选择的held-out gate；新增显式OOS选项后Jev为19.5%，不是只加NONE即可达此数。Qwen3.6-27B的3.5%特指likelihood读出＋显式OOS＋gate。拒判率、ID覆盖与错误应同时报告。 | §5.1 OOS段落，§6表11及附录OOS结果 |
| R06 | Kev ECE .051→.377 | **成立但方向有特定含义。** 在150选项CLINC上，该Kev-9B的T=1 raw ECE为.051，使用检查点内置温度后为.377；这是校准迁移失败，不是训练前后准确率变化或所有Kev版本的普遍性质。 | 表7、§5.1 |
| R07 | 只写意图描述比标签名＋描述提高6.8pp | **数字有出处，但原回复遗漏模型归属。** 该增量属于this-that-model-1.0，不能概括为Kev或所有模型都提高；需按模型／语言／候选表重验。 | §5.1 rendering例外、`render_paired.json` |
| R08 | Jev延迟148ms | **成立但仅此测量边界。** 表11为CLINC请求的API客户端中位延迟；表9另一typed-decisions负载是138ms。不能当服务器前向、通用p95或M5性能。 | 表9、11 |
| R09 | decider2b级联Jev，成本为Jev的58% | **成立，限作者计费模型。** 成本比例.58意味着约42%节省；原回复写成本58%本身正确。不同级联、满GPU利用假设及OOF阈值需保留，不能保证线上都兑现。 | 表10、§5.3 |
| R10 | 150选项是应采用某模型／结构的阈值 | **不成立。** 150是CLINC标签数。选项数、描述长度、干扰项和位置共同变化；可行性还取决于head预算、上下文和具体tokenizer。 | §3.3、表8、Laya token-budget审计 |
| R11 | 所有choice必须显式NONE、所有场景都不应hierarchy | **外推过度。** 有OOS时必须验证拒判机制，但可用显式答案、外部gate、查询补证或其他完整策略。实验中的hierarchy增加了易错域预测；已有可靠外部域信息、菜单超预算等条件下仍可能有价值。 | §6及§7；此处为依据实验条件的设计推论 |
| R12 | Banking77 4B 69.0→75.4、0.6B22.2→59.0 | **有出处，不能省掉训练方法。** 4B为Qwen3.5、LoRA λ=1；0.6B为Qwen3、LoRA λ=.01。对应Full配置是75.2、60.5。评估全3,080条测试、77选项；不是77类中抽top-k后才算。 | v2/v3表1，v3表11、附录B |
| R13 | “通用能力81.4→74.9” | **指标错。** 这是231题公开JevBench在Intent-1ep后的结构化决策准确率。General平均为67.3→67.3；不能称通用语言能力整体从81.4降到74.9。 | v3表7、10及附录G |
| R14 | 混合格式、补充长文本可修复意图训练的退化 | **方向有实验支持，不能说唯一因果已分离。** Intent混合95,461例还含commonsense数据，二元/verification和NONE极少；Reason-9k恢复部分行为，长输入混合改善长题。但Reason+Long只375步，Reason-30k为938步，训练预算差异也可能贡献。 | §4.3、附录D/G、表7 |
| R15 | 唯一系统研究“只用意图数据微调会出什么问题” | **唯一性未证实。** 该工作提供相应诊断，但没有穷尽相关工作以排除其他意图适配、遗忘、校准与拒判研究。 | §2、附录J |
| R16 | 监控合法token概率质量，下降就停止 | **局部health check成立。** 参考配置规定root legal log-mass相对下降超过.5 nats则停止；消融仅报警。它检查输出格式/分布漂移，不检验路由正确率、领域回归或生产风险，不能代替开发集、校准及冻结Test。 | 附录A表2；附录H/I |
| R17 | 配方可以直接照搬为原作者可运行训练流程（实施边界） | **未确认完整产物。** 论文配方可读，但本轮未定位作者训练repo／权重。LLM2Jev是另一baseline；第三方MLX报告未训练，不能替代原方法复现。 | [LLM2Jev README](https://github.com/Yinsongxu/LLM2Jev/tree/93d4fcdcc81e0732026a65195eca3b45333af451)、[第三方MLX边界](https://github.com/changtimwu/llm-as-jev-exp) |
| R18 | 大于60意图时Jev81%、Laya35% | **仅该混合F轨成立。** F含200项：100条BANKING77（77标签）＋10种MASSIVE locale各10项（60标签）。不能提升为统一“60是失效阈值”，也不是全部CLINC路由。 | §4表1、§5、附录A |
| R19 | 工具选择99.5%→84.5% | **成立。** 每组400题、K取2/5/10/20/50各80题；随机干扰改为词法近邻后Jev下降。候选歧义、输入预算与选项数须分别考察。 | §5/7；`paper/numbers.json.capacity.overall` |
| R20 | LLM审计发现19.8%有其他合法工具 | **成立但不是人工重标注。** 79/400被DeepSeek判为多有效工具；唯一gold子集281/400，剩余情况也并非都属于多正确答案。该裁判可能与Jev共享偏好，不能用它自证所有下降均是标签错。 | §7/8；`capacity.audit_hard`与`unique_ok` |
| R21 | Laya反转选项翻30.3%，Jev1.8% | **成立。** 总分母1,000，来自A400＋B400＋F200；不是任意任务的翻转率。列表倒序与“交换yes/no标签语义”不是同一个干预。 | §5、`paper/analysis.py` order-flip块 |
| R22 | 两者model routing接近chance，所以不能用decision model做任何model routing | **不成立。** 只测零样本二选一、400平衡请求；gold由RouterBench的7B和GPT-4结果构造，未测训练后的router、替代模型组合或成本最优策略。 | §4标签构造、§8 Routing labels |
| R23 | 4,928训练、924留出、87.5%准确率、ECE .028，92.5%覆盖下91.5%precision，Jev79.4% | **官方页面确有这些数字；原始逐项产物尚未核实。** 比较还给出Jev带示例85.7%。不能只保留不带示例基线后宣称同监督条件胜出。 | 固定Laya README “Learning from a stream”及vegaml同表 |
| R24 | 把该Banking成绩理解为前述Laya小encoder后训练 | **对象不匹配。** 当前表明确4B reader，新Learner／vegaml拟合冻结特征上的小头；经典322M／421M要显式选择另一模型路径。 | Laya README第43–56行；[Learner机制](https://github.com/NandhaKishorM/vegaml/blob/8b0ca58e8d92ac3fc9c5cc682c93aebc7b885a20/docs/learn.md) |
| R25 | “学习”意味着更新reader／LLM权重 | **不成立。** `learner.fit_head`调用`TTTHead`；该类为PCA＋多类logistic head，拟合冻结features。属于head适配/在线监督，不是经典encoder或4B reader的LoRA／全参训练。 | [learner.py](https://github.com/NandhaKishorM/vegaml/blob/8b0ca58e8d92ac3fc9c5cc682c93aebc7b885a20/vegaml/learn/learner.py)、[ttt.py](https://github.com/NandhaKishorM/vegaml/blob/8b0ca58e8d92ac3fc9c5cc682c93aebc7b885a20/vegaml/ttt.py) |
| R26 | 这组成绩支持少量数据即可用于目标企业路由 | **不成立。** 未在本轮定位该Banking表的split种子、数据ID/哈希、候选构造、4B reader精确版本、逐题预测和阈值选择/测试隔离。`docs/learn.md`还说fitted-head confidence没有自身校准。低ECE点估计不构成风险保证，91.5%precision也不是5%错误预算。 | README聚合声明与learn文档Limits；未找到不等于产物不存在 |

**层级评分已实际复算。** 直接读取作者[固定5767320产物](https://github.com/pozapas/system-one-models-survey/tree/5767320ffb6747cb114242ee3add0e13bdc2e645)的两份inputs和四份answers，按item_id配对、取argmax并求交：Jev域422／600、gold域细分567／600、联合404／600；Kev分别390、545、361。协调者与独立审查结果一致。这里只重算公开预测，没有调用模型或重新裁定gold。

**来源本身也有一处额外不一致。** Fast Models摘要的K50“Laya31%对Jev98%”拼了不同群体：完整80题为31.25%对80%；LLM判唯一正确的57题为35.09%对98.25%。这不是用户原回复中的单独断言，但应用该论文前必须知道，不能因为是论文数字就放弃分母核对。

分层可与flat、检索top-k、固定领域状态或保留多候选的tournament比较。CLINC实验支持其所测hard-domain gate有错误瓶颈，不支持“全世界≤150标签一律flat”。保留多候选能降低硬锁域的某些风险，但上游若已淘汰gold，后级仍无法恢复；没有“前一步错误不会锁死”的保证。


## B. “Choose what to do next”的方案推论

以下是本次审查的系统／统计推断，依据上述论文的适用条件与[企业业务合同](domain-path-applicability-research.zh-CN.md)，不是新增实验结果。

| ID | 被核查主张 | 判定 | 应怎样设计与验证 |
|---|---|---|---|
| B01 | 动作少而固定，就等于意图分类且不需推理 | 错误 | 有限输出不意味着证据完整或决策简单；下一步可能要补证、算政策、验证状态并考虑后续影响。可先监督学习，但不能由动作数证明一步读出足够 |
| B02 | 这类客服最优路线已确定为SFT→CAPS→PRDO | 错误 | 没有该完整链的匹配企业实验。分别是可信标签、部分反馈、保留推理三个条件分支，不能强制串成默认升级路线 |
| B03 | 准确概率就直接保证自动化比例／错误率 | 错误 | 总体校准不保证被策略挑出的子集风险；相对选项概率也不自动等于动作可执行／成功概率。校准、选择、迁移和执行合同都需确认 |
| B04 | 只有proper score能训练准确概率 | 错误 | 恰当性提供一致性目标，不保证有限模型结果；也不能据此排除其他估计／校准方法 |
| B05 | 满意、再进线、退款申诉就是CAPS需要的标签 | 错误 | CAPS主实验为单一金标类别对错；业务结果可能多动作均成功、有延迟／缺失和人工干预。先定义事件、窗口、支持和反馈模型；必要时另做策略价值识别 |
| B06 | 通常softmax的每项概率能直接预测各动作成功率 | 错误 | 例如退款和转人工都可能有高成功率，两者之和可大于1，无法由单个softmax同时表示；应明确唯一正确类、允许集合或逐动作结果模型 |
| B07 | 从优秀坐席轨迹抄每轮动作就是gold | 需限定 | 可作示范来源；历史选择不等于最优、唯一或当时获准。恢复决策前状态，审政策版本、替代合法动作与未来信息泄漏 |
| B08 | 让另一大模型思考给软标签，就是SII自蒸馏 | 错误 | SII原法同尺寸自蒸馏、读logit分布；外部教师到4B是跨模型蒸馏，口述概率又是另一信号。均可研究但不能混名自证 |
| B09 | 同请求Q1领域、Q2该领域动作能自动顺序条件化 | 错误 | 预定义并行问题并不自动把Q1答案注入Q2；若Q2选项需随Q1改变，要显式序贯、结构化联合合同或其他实现，不能只靠一次请求叙述 |
| B10 | 改成全意图＋固定动作两问，两问就独立 | 错误 | 选项不依赖彼此不等于语义／统计／计算独立；意图、状态和下一动作常有关联。联合问法可试，但需校验完整动作组合 |
| B11 | 两个置信度都过同一阈值即可保证联合风险 | 错误 | 即使两个.95是有效条件边际且误差独立，联合正确率也只有.9025；实际还不能预设独立。用案件级Cal-policy选择／验证整套规则，不能直接相乘自报概率 |
| B12 | 意图×动作总能由代码唯一映射到skill | 需限定 | 只在固定、完整、版本化映射内成立；多意图、权限、参数、状态、前置依赖及多条合法路径不能被二维表省略 |
| B13 | 高置信就可自动执行退款等动作 | 错误 | 先通过授权、事实新鲜度、参数和业务约束；阈值只管定义好的语义风险，不能代替权限或实际执行回执 |
| B14 | 70%以上走快路、阈值.9、5%错误预算是默认配置 | 未证实 | 分别是未经企业测量的比例、某论文设置和示例风险预算；由真实流量与错误代价确定，不能移植为生产SLA |
| B15 | schema任一变化都得重训 | 错误 | 类型／ID等可能受特定托管服务严格约束；动态候选／自然语言模型可支持变化。任何变化均应重验，但重验不自动等于重训 |
| B16 | 整段成功率下降就一定是错误累积，调阈值或拆动作即可 | 错误 | 也可能来自状态、工具、候选、策略、标注或分布变化；需归因和回滚，不能由一个指标确定原因／补救措施 |
| B17 | 抽1000–2000题作固定评测，选赢家后LoRA／蒸馏 | 需补数据分工 | 数量依功效与风险；原方案未完整区分Train／Dev／Cal-fit／Cal-policy／冻结Test，不能在同一测试集反复选参。客户／案件／会话／时间先分组再增强；测试不能兼作选择集 |

| B18 | 企业数据带来的收益必然大于方法选择 | 未证实 | StartLux同类／异类追加数据消融支持任务家族匹配的重要性；没有在该企业中识别“数据、底座、读出、loss、策略”各因素的最大贡献，不应宣称其中之一必然主导。 |

## T. 最后三篇推荐应怎样理解

| 推荐内容 | 核查结论 |
|---|---|
| Inner Jev作为读出／适配蓝本 | 可读；“instruct一律优、400步、T≥1、换loss没用、只训头必无效”均不能直接搬，见M06–M08、M18–M30 |
| CLINC路由论文作为架构与评测参照 | 直接相关；应借其对照和失败测试，不能搬“≤150一律flat／NONE必设／层级普遍劣”的规则，见R节 |
| LLM-as-Jev作为窄域适配风险参考 | 有价值；“唯一工作”“合法token质量一降就停”及“原训练脚本可直接运行”须另核，见R节 |
| CAPS留待有线上日志，PRDO补StartLux | 应改为按学习信号、输出语义和部署读出各自准入；上线本身不满足CAPS假设，组合也未得到企业实证 |

这三篇是不同问题的阅读材料，不能据此认定“当前最优训练方案”。实战先冻结一个真实失败、可见状态与标签合同，比较当前系统、简单监督／检索、原版与适配版及强参考；以关键错误、任务完成、风险—覆盖、配对区间和完整成本验收。可靠标签上的CE可作强基线；是否加蒸馏、Brier、PRDO或部分反馈方法，由匹配实验决定。

## 本轮执行与尚未解决的证据

本页共**185条带ID核查记录**，含合并后的重复主张及明确标出的实施边界；不是185项模型实验。原回复覆盖如下，后续重复说法不再另建一套结论：

| 原讨论部分 | 对应核查 |
|---|---|
| 最初澄清与JEPA误认 | 范围澄清无须事实判决；身份见M01 |
| Jev与后训练六节综述 | A、M、B节；区分平台合同、模型、数据、应用和步骤 |
| RLCD深调研、损失／底座表 | M节，旧v1与v2分开；额外推理边界见P节 |
| PRDO与StartLux谁最优／原理／效果 | P、L节；模型、方法、榜单及许可分开 |
| 企业后训练候选排序与排除项 | A、L节；未获得可直接采用的统一排序 |
| PRDO是否值得用、与其他方法组合 | P、B节；联合训练只作待验假设 |
| 客服每轮choose-next动作设计 | B节；固定小动作集不证明无需推理／全信息 |
| 四个意图路由案例 | R节；原表、选项数、标签／训练身份及已发布输出分别核 |
| 两层问题矛盾与修正 | R及B09–B12；接口并行、统计独立和联合风险分开 |
| 最后三篇推荐 | T节及其所指M／R；阅读价值不等于可原样搬超参 |

实际执行：读取固定论文正文／附录和针对性官方代码／卡片／许可证；独立复算两个DI汇总的排序、600项CLINC层级结果交集。协调者复核同样得到DI旧rank1、当前raw29／并列6组，以及Jev404／600、Kev361／600联合正确。这里只是公开产物算术；不标为模型复现。

本轮文档验证、5份生成页同步和diff检查通过。没有改可执行脚本或测试；按仓库规则不重复运行上一轮41项单元测试，更不把结构检查当事实认证。审查中识别的论文／协议与原话忠实度问题均已修正并定点复验；未留已识别的阻塞问题不等于不存在未知错误。

仍未知：目标中文企业的标签／完整状态／动作效用与后训练结果、目标Mac真实反向／内存、部分作者benchmark的精确权重和raw runs、Laya新Banking表的完整切分与阈值隔离。cuplivo issue本轮读取超时，未把个人访问线索认证为地区普遍限制。商业授权未联系／取得，不对具体合同作违约裁定。

本轮还纠正本仓已有两处陈述：CJ-Medical已于10月18日发布，不能说行业权重全部planned；阿里原生API与微调指南有Bearer／裸key的不同示例，不能由其一宣布所有推理鉴权都不用Bearer。详见[更新记录](../updates/2026-11-20-conversation-fact-check.md)。
