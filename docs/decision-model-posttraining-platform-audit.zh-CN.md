# 决策模型领域后训练：平台与生产证据核查

核查日期：**2026-11-19**。范围：企业客服的分类、路由、升级、评分与拒判；只查公开一手资料，未登录控制台、申请授权、训练、推理或接触企业数据。文档可读不等于本账户已获服务权限；Git/Hugging Face 文本 revision 不等于已下载核验权重。

**结论：领域后训练已有可查路线，但不能把它们统称为“微调 Jev”。** TypeSafe 当前不提供客户权重适配；阿里有受限开放的托管 LoRA；Together 有普通语言模型 SFT 配方；Clef 有开放权重和人工协作代训服务。公开证据仍不足以证明“某企业用自己的客服数据训练 Jev 类模型，经过独立线上对照改善了客户结果”已普遍成立。

证据标记：**D**＝官方产品/接口文档；**A**＝模型作者离线实验/配方；**P**＝供应商或使用方报告实际生产使用，仍非独立审计；**I**＝本次据来源推断。所有性能数字均非 `reproduced_here`。

## 产品能力与训练契约

| 待核查说法 | 判定 | 应使用的表述与边界 | 一手来源 | 证据 |
|---|---|---|---|---|
| Jev 仍须等候名单，企业可微调专属 Jev | 前半过时，后半不成立 | 当前开放注册；Models 明说同一权重服务所有账户，不用客户数据作 fine-tune/LoRA。业务适配靠 state、规则、示例和代码组合。 | [注册帮助](https://help.typesafe.ai/articles/4519713419-how-do-i-create-or-activate-my-account-after-an-invitation-or-waitlist-approval)、[Customizing Jev](https://docs.typesafe.ai/models#customizing-jev) | D |
| Jev 仅文本、64k、255 选项、$0.042/M | 部分过时 | 1.14 已发布，默认请求64k/单题32k，Choice最多255项；输入还支持图像，图像/Box仍是实验状态。长上下文须显式开启至262k；输入价仍为$0.042/百万tokens、输出免费。 | [模型](https://docs.typesafe.ai/models)、[Choice](https://docs.typesafe.ai/primitives/choice)、[图像状态](https://docs.typesafe.ai/images)、[价格](https://help.typesafe.ai/articles/5187202169-how-much-does-jev-cost) | D |
| 能下载官方 Jev 权重，在 M5 上训练 | 未找到支持 | 本次官方文档/发布入口未发现 Jev 权重或本地训练包。不能从兼容 API 的其他模型反推 Jev 内部结构，更不能把 Kev/Tev 权重称为 Jev 权重。 | [TypeSafe 模型与定制契约](https://docs.typesafe.ai/models) | D＋I，缺公开产物 |
| `/v1/systemone` 已是事实标准，阿里/Ollama可无差别替换 | 表述过强 | 多家沿用该接口形状，可称生态兼容约定；未见正式共同规范/一致性认证。阿里推理鉴权不用Bearer前缀；Ollama支持取决于版本和模型，模型类型、概率、校准与图像合同仍须逐项验收。 | [阿里调用契约](https://help.aliyun.com/en/model-studio/decision-model-tuning-guide)、[Ollama 官方发布](https://ollama.com/blog/ollama-now-supports-jev-style-decision-models) | D＋I |
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
