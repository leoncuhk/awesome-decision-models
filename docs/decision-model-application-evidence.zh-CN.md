# Decision models实际应用证据与技能加载判断（2026-11-13）

[价值复核](dynamic-skill-loading-value-review.zh-CN.md) · [实验方案](dynamic-skill-loading-experiment-plan.zh-CN.md)

## 核查范围

读取用户给出的OpenRouter页面时静态HTML未正确应用筛选，混入普通生成模型；浏览器访问不可用。随后按OpenRouter官方文档调用带筛选的公开API，得到39条、16提供方标识，其中5个latest别名。未调用付费推理或获取用户请求。目录存在不代表端点可用、校准可靠或业务收益。

来源：[筛选API](https://openrouter.ai/api/v1/models?output_modalities=decisions)、[官方选型说明](https://github.com/OpenRouterTeam/skills/blob/main/skills/openrouter-decisions/references/models.md)。以下为当日目录快照，不保证后续不变。

| 提供方 | API条目 |
|---|---|
| perplexity | `perplexity/pplx-decider-flash-v1.3:free`, `perplexity/pplx-decider-v1.3:free`, `perplexity/pplx-decider-flash-v1.2`, `perplexity/pplx-decider-v1.2`, `~perplexity/pplx-decider-flash-latest`, `~perplexity/pplx-decider-latest` |
| google | `google/gemini-decision-1` |
| nace-ai | `nace-ai/drex-max-finance`, `nace-ai/drex-max`, `nace-ai/drex-v2.0`, `nace-ai/drex-v1.5` |
| parallel | `parallel/decisions-fast:free` |
| morph | `morph/reflex` |
| cloudflare | `cloudflare/clairic`, `cloudflare/clef-omni`, `cloudflare/clef-flash`, `cloudflare/clef` |
| baseten | `baseten/joey-1`, `baseten/mammoth-1`, `baseten/elephant-1` |
| liquid | `liquid/d1.1`, `~liquid/d1-ultra-latest`, `~liquid/d1-latest`, `liquid/d1-ultra`, `liquid/d1` |
| respan | `respan/span-02`, `respan/span-01`, `respan/span-01-lite`, `respan/span-01-lite:free` |
| typesafe | `typesafe/jev-1.14`, `~typesafe/jev-latest`, `typesafe/jev-1.13` |
| scaledown | `scaledown/classify-1` |
| microsoft | `microsoft/microsoft-decision-1` |
| upstage | `upstage/solar-decide-flash`, `upstage/solar-decide` |
| openai | `openai/gpt-6-luna-decisions` |
| togethercomputer | `togethercomputer/tev1-4b-experimental` |
| jaredpalmer | `jaredpalmer/kev-4b` |

## 直接讨论这一应用吗？

是。OpenRouter官方decision skill把routing、escalation、approval gates列为用途，要求最小充分state、固定版本和真实输入阈值验证。这是接口与集成指导，不是动态skill加载效果证据。[官方说明](https://github.com/OpenRouterTeam/skills/blob/main/skills/openrouter-decisions/README.md)

## 补充关键实践和反证

| 模型／来源 | 实际工作和价值点 | 证据与边界 |
|---|---|---|
| [Perplexity Decider v1.3](https://www.perplexity.ai/en-GB/hub/blog/perplexity-decider) | 内部离线审查Agent日志，寻找规则漏报/误报，提出修正规则；RL轨迹归因；网页质量过滤 | 作者报告7000会话产生14项规则修复，其中6项两天内批准上线；一周日志回放最繁忙规则告警量降52%。不是线上随机收益证据。RL监控只诊断、不改reward。生产百万请求分析用LLM裁判，反映使用任务及一致率，不是业务正确率；本地/托管成本口径不同，不导入统一省钱倍数 |
| [Cloudflare Clef](https://blog.cloudflare.com/clef-decision-models/) | Threat Intelligence团队试验网站分类，多标签共享一次读取 | 自报包含抓取渲染分类2.2s，对照gpt-oss-120b4.7s；输出类别数量不同，缺批量协议/误判与后续处置收益，不解释为已证实安全提升 |
| [Parallel Decisions](https://parallel.ai/blog/decisions-openrouter) | 查实时网页后判断API支持、供应商属性等，减少搜索与判断串联 | 厂商100题自建benchmark和产品用例；没有本轮可核的具名客户业务结果。与只读给定state的模型证据获取条件不同，不适合直接比较分类准确率 |
| [Morph Reflex](https://www.morphllm.com/products/reflex) | 客服团队/紧急程度多问题判断、重复state缓存 | 产品示例和5次缓存调用，不是客户收益实证；可作技术候选，不能称胜出 |
| [Baseten Mammoth/Elephant](https://www.baseten.co/blog/the-best-decision-models-in-the-world-mammoth-1-and-elephant-1) | 通用分类、工单路由、安全判断 | 发布与benchmark材料，尚无本轮核得的具名部署效果；榜单不能替代流程验证 |
| [REFLEX with Jev](https://arxiv.org/html/2609.26532v1) | 简单控制由Jev处理，复杂情况升级强LLM | 第三方研究，非本仓复现。外部60个tau2任务：Jev方案成功.850、成本.0572美元；便宜LLM级联.917、.0411美元，成功差区间未定。相对全强模型便宜不等于优于便宜级联。这里REFLEX架构不是Morph Reflex产品 |

## 对动态skills方向的修订判断

已有案例支持“把频繁、有限答案的语义判断从生成式调用中抽出”，并不要求先拥有庞大技能库。最值得从企业现状抽取的判断是：是否切换意图、是否需要工具、是否缺证据要澄清、需要哪个流程候选、是否转人工。确定性的资格与权限由代码决定。

拆成两项独立实验：A固定加载方式，只替换现有语义判断器；B固定判断器，只比较静态/按需加载。A成功说明判断器有价值；B成功才说明动态加载有额外收益。评估当前基线、小监督模型/规则、便宜LLM级联以及少数decision候选，避免把所有39条逐个跑成与业务无关的排行榜。

入口意图选择只覆盖技能契约的一部分：还需正确的历史/状态、必要依赖、退出条件、工具约束、参数、回退。优先试已有高频单点；若只在离线日志复核能产生价值，就采用离线复核，不强行插入实时控制路径。若现有简单方案风险与成本均达标，则停止动态加载研究。

## 具名客户／使用方案例复核

## 优先参考清单

| 模型／案例 | 实际判断点和价值机制 | 证据与边界 | 与动态技能加载关系 |
|---|---|---|---|
| **Jev — Jack & Jill** | 招聘流水线初筛：每岗位约6000候选缩至2000，再由强模型细审；替换原Gemini 3.1 Flash Lite判断调用。 | [供应商发布的客户案例](https://typesafe.ai/blog/jack-jill-jev-case-study)：150真实岗位离线配对，历史招聘经理选中者召回93.9%→94.6%，差的90%CI为−0.4至+1.8pp。每千候选token成本$0.755→$0.092（约88%降幅）；每岗位全部候选评分中位20.3→10.3秒。$500K为考虑增长的年预测，不是已兑现节省；不是招聘质量／公平性证明。 | 最有参考价值的是**昂贵下游之前廉价筛选，明确测漏掉的有价值对象**；不能直接证明skills筛选有效。 |
| **HyperClassifier / Koa — Salesforce Agentforce** | 将用户请求路由至话题／子Agent，减少每次调用的通用推理开销。 | [使用方官方介绍](https://www.salesforce.com/news/stories/koa-decisions-salesforce-decision-models/?bc=OTH&ver=1794428066)报告HyperClassifier约26ms对通用LLM约1.4秒；Koa为后续Gemma训练版本，多模态／更广API扩展是不同发布。数字是组件级厂商测量，没有公开逐样本协议，不能全归为最终任务收益。[官方发布说明](https://help.salesforce.com/s/articleView?id=release-notes.rn_einstein_copilot.htm&language=en_US&release=260&type=5)确认默认模板使用HyperClassifier。 | **最直接的服务Agent路由先例**，但它证明专门路由可实用，未证明每轮动态加载长技能正文优于静态工作流。 |
| **Gemini Decision 1 — Google内部产品** | Gemini Notebook选择模型档位／思考程度；Stitch快速UI流程；CC从200多emoji选反应；Search的MCP对抗内容检测。 | [Google发布原文](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)报告Notebook日常查询延迟最多降低40%；其余为已使用功能描述，无完整对照协议、样本量或业务KPI。所有结果均厂商自报。 | 说明低延迟判断可放在控制流程里；模型档位路由与技能加载是不同决策合同，安全检测也不能替代授权。 |
| **Jev — Modem Smart Triggers** | 先用来源、作者、状态作精确过滤，再判事件是否符合自然语言条件，仅匹配才启动完整Agent。 | [实施者功能公告](https://modem.ai/blog/smart-triggers)称已开放使用，每事件低于1秒、约$0.0001。未公开漏报率或全量节省对照。价值机制很清楚：避免无用的完整Agent运行。 | 比“40技能top-k路由”更简单的首个切入点：**是否值得启动此流程**，但须测被漏掉的重要事件。 |
| **Jev — Workday Sana** | 按任务呈现表单、日历、审批卡等交互界面；业务状态、权限、审批仍由Workday流程承担。 | [使用方官方公告](https://investor.workday.com/news-and-events/press-releases/news-details/2026/Sana-Is-the-New-Workday-Home-A-Dynamic-Agentic-Experience-Built-to-Finish-the-Work-Not-Just-Answer-Questions/default.aspx)确认Jev用于动态UI。没有公开JeV独立贡献的随机收益评测；新Home可用，Sana Concierge仍为早期客户、预计2027Q1 GA，不能混称全部功能已成熟。 | 从有限组件中选择的低延迟UX；与skills相邻，但不是技能加载效果证据。 |
| **Jev — Browserbase Stagehand** | 页面可交互节点组成候选，判断动作／目标；代码准备参数、匹配检查和fallback。 | [工程团队报告](https://www.browserbase.com/blog/what-is-jev)描述组件替换与早期测试；作者明确独立Jev Agent演示不等于可生产。需按实际操作与完整浏览任务分别验收。 | 是**候选生成→判断→执行**合同参考；加载器仍要负责候选覆盖与参数／依赖完整。 |
| **Jev — Entagl客服历史回放** | 消息处理决定、专员路由和常驻语义检查。 | [原始评测](https://www.entagl.com/blog/typesafe-jev-benchmark-ai-decision-models)含283构造case产生1357决策及402历史路由。历史选专员Jev在两workspace为91.4%/83.7%，原方案98.1%/97.8%；Jev没收到当前owner信息，输入并不充分匹配。阈值回退也非总有益。作者离线回放不是生产A/B。 | **最重要的状态完整性反例**：上一轮谁负责、已收集哪些信息，必须进入状态；仅看最近消息或提升top-1不能解决。 |
| **Jev — Audiala回滚与保留用途** | 主路由替换23分钟后回滚；保留较窄推荐重排及可缓存地点资格判断。 | [使用方完整复盘](https://audiala.com/blog/jev-in-production)：65场景×3次，稳定通过38→33；路由中位382→294ms，但完整轮次8677→9262ms。推荐4城市均值nDCG@8 .783→.893，却有LLM标签、输入不一致、Jev更慢等限制；保留fallback。不能宣布广泛收益。 | **直接否定“便宜快速分类器自动带来Agent收益”**。路由合同还包括城市、指代、工具控制flags；收益必须看全链。 |

## 不宜作为强证据的条目

Vercel fx命令安全筛查的5–18倍速度说法，本轮只定位到二手索引引述工程师／CEO社交帖子，未核到足够可读的原始方法，因此不把它列为已验证收益。API上架与SDK支持只能证明可集成。其余开放decision模型若只有模型卡、基准和“routing/moderation”推荐用途，应保留为候选供应，不应编造生产客户或ROI。

## 对动态skills加载的重新判断

这些案例说明决策模型的实用核心是**把已有、频繁、边界明确的判断工作做便宜／快，或用低价前置判断避免昂贵后续工作**。它们确实支持研究控制环节，但不支持仅因模型多就建立新的技能平台。

可把当前分支从“每轮从40技能选5个”收窄成三种依次验证的合同：①是否启动工作流；②当前业务状态下应保持、切换还是澄清；③检索已有候选后，哪些技能及依赖必须保留。第一种收益最直接；第二种最贴近真实客服，必须传会话归属和流程状态；第三种才需要动态技能加载实验。

对照先用规则／静态分组、当前路由器、小分类器和简单检索。只有出现可归因的路由开销或必要技能遗漏，并且新方案在完整成功、风险、返工、p95与成本上改善，才继续。主张应是“在声明条件下找到值得替换的判断步骤”，而非“decision models已经证明动态技能加载必然有价值”。
