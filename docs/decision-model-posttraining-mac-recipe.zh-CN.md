# Mac训练准入：候选可行性与Skill／工具判断示例

核查日期：2026-11-19。目标硬件为M5 Pro、48GB。本页是官方文档、源码与模型卡核查；没有下载权重、执行模型前向或训练，不给出实测效果或训练耗时承诺。[企业后训练总览](decision-model-posttraining-enterprise.zh-CN.md)负责方法与选型；本页只提供一条训练链路备选，**Laya尚未通过企业效果选型，不能因可在Mac训练就优先采用。**

## 先核前列候选的训练准入

下面区分“值得研究”与“已能在目标机完成训练”。未在M5 Pro 48GB测量真实前向、反向、峰值内存、swap或导出重载；公开CUDA脚本不能据此视为Mac配方。

| 对象 | 发布训练产物与输入合同 | Mac上的下一步及停止条件 |
|---|---|---|
| SII-Decision | 4B／27B分别基于Qwen3.5／3.8；原始底座蒸馏，需`gold_target`、教师`train_target`和原版`p0`；发布wrapper为多GPU | 先审数据转换、adapter加载及算子支持，再尝试代表性小批次；不能将企业硬标签直接代入并声称复现原法 |
| Kev | 有`--data`与`--init_from`的领域适配，训练器含MPS分支；MLX服务与训练分开 | 是直接自有标签适配的优先工程核查对象；混合递归结构的MPS backward、内存或保存重载失败时，先定位后决定移植或换算力 |
| Intern-Decision | CUDA／XTuner、全语言参数训练及冻结视觉部分 | 是多字段／视觉条件下的专项候选；改为Mac LoRA需独立验证，不能沿用原训练效果承诺 |
| PRDO | 全参训练，包含rollout与参考模型；论文48GB独显另配约125GB主机内存 | 仅服务保留推理的选择性判断；48GB统一内存不等价，现阶段没有可直接执行的Mac复现配方 |
| Nimble | 开放9B的候选token监督／LoRA；新托管v4／v4.1另论 | 先借鉴数据构造并做匹配消融；MLX推理支持不证明CUDA训练代码可直接迁移 |

固定版本、源码和模型卡见[产物矩阵](decision-model-posttraining-platform-audit.zh-CN.md#可训练产物矩阵)与[PRDO审计](decision-model-posttraining-method-audit.zh-CN.md#8-prdo-v2全文复核怎样改变当前路线)。工程smoke只决定是否可运行；企业数据上的质量、风险、完整成本才决定是否采用。

## 实现附录：资源较低的链路示例

**本文以官方Laya多语种322M checkpoint示范`laya.train`的监督训练、独立校准和拒判链路。** 配方对应较短文本与候选相关性判断；中文／中英混合时需评测多语种检查点，纯英语也可比较English 421M。代码接口可审查是保留这个实现样例的理由，不能据此选出企业效果胜者；模型质量及复杂规则、长上下文或图像任务的路线由总览中的证据和验收门槛决定。[官方训练说明](https://github.com/NandhaKishorM/laya/blob/d1282e791d71e92f24f816ff3836e4fd1c2ded4a/docs/finetune.md)、[多语种模型](https://huggingface.co/convaiinnovations/laya-multilingual)

另一个中文公开输出面板中，多语种Laya也弱于对照；换多语种不自动解决任务。这不能解释JEVal原差距的成因，原评测仍需精确权重与输入配置复验，不能由“英文版”或“512上下文”单因定论。任务内微调高分也需排除空输入、标签先验和同源模板捷径；负面证据与检查点/输入审计见总览及[方法核查](decision-model-posttraining-method-audit.zh-CN.md)。本页保留配方，不代表已决定投资该模型。

任务先定义为：用户请求和当时可见状态，加一个候选 Skill／工具的真实描述／必要正文，判断该候选是否应加载；所有候选都不成立时返回无适用项。每候选使用固定的中性 `A/B` 选项，把候选内容放入 `state`，避免将变化的工具名当成固定输出类。先检索少量候选再逐个判断，保留候选召回率与判断准确率两套指标；多个候选可同时适用，不能把多工具需求强制标成唯一标签。

下面的`soft-ce`仅展示一个监督基线，不是已选出的最优目标。公开Laya三种子同协议实验没有复现出它对`rlcd`的稳定准确率优势；两者都需要在相同起点、数据、更新预算和种子下比较。该结论针对Laya的实现，不能替代其他架构上的方法判断，也不等于两种方法等价。严格适当评分规则的数学性质不证明目标流量已校准。[配对多种子结果](https://github.com/NandhaKishorM/laya/blob/d1282e791d71e92f24f816ff3836e4fd1c2ded4a/research/scripts/step4_benchmark/GATE_D_RESULTS.md)

## 方案比较

| 路线 | 已核查事实 | 本轮判断 |
|---|---|---|
| **官方 Laya** | Apache-2.0；多语种321,908,998参数；官方有MPS／CPU训练、逐行问题JSONL、CE／RLCD、冻结encoder、选项打乱及校准接口 | 已确认训练入口可审查，未确认企业质量达标；只保留为资源较低的链路备选。MPS训练默认fp32，需要显式开启梯度检查点 |
| **LayaStudio MLX LoRA** | 独立Apache-2.0项目；确实实现encoder LoRA及完整decision head训练、模型合并和加载；依赖laya-mlx | 是真实Mac训练方案，但不是官方训练器。当前数据集共用一份questions schema，不能直接消费逐行变化候选集合；固定A/B候选相关性任务可用，作为内存／速度备选 |
| **GLiClass** | Apache-2.0；可训练动态标签分类；instruct-edge仅32.7M，v4-edge约439.8M；两者不是同一版本或同一能力 | 32.7M适合廉价基线，v4可列比较候选；当前上游通用train.py默认随机切分，不应原样作为独立评估协议；未核验MPS真实训练 |
| **Kev** | Apache-2.0；Qwen底座加LoRA／pointer head；train.py有MPS分支，MLX主要用于服务；0.8B已开放 | 上表直接领域适配候选；本实现附录未给出其目标机配方。训练可行性与是否生成推理、领域效果分别核查 |
| **静态embedding／小分类头 ToolRouter** | 模型MIT、数据标CC-BY4.0；约8MB；只有7种已知工具的identity head被训练，未见工具走固定语义分数 | 必留便宜基线；不能据其接口支持任意候选，就说训练已学会任意新工具路由 |

源码依据：[Laya train](https://github.com/NandhaKishorM/laya/blob/d1282e791d71e92f24f816ff3836e4fd1c2ded4a/laya/train.py)、[LayaStudio engine](https://github.com/biplovgautam/LayaStudio/blob/71f1a01466e247c4ac9a8afe681e3491cb0f2e06/layastudio/engine.py)、[GLiClass训练](https://github.com/Knowledgator/GLiClass/blob/af82d425c0259a6f46f240bb0633fcdab821eaea/train.py)、[Kev训练](https://github.com/jaredpalmer/kev/blob/2074cc44256200bb37540103fa4572901faa10f3/kev/train.py)、[ToolRouter方法与限制](https://huggingface.co/stanley-nv/toolrouter/blob/b2607a34877cc9211ec1e715c703966bf5f20c2a/docs/REPORT.md)。LayaStudio的作者报告可用于确定应测什么，不能直接移植为M5 Pro上的预期成绩；`laya-mlx`本身仍将训练列为范围外，LoRA来自Studio而非该运行时。

## 数据与验收边界

**主数据应来自实际要路由的Skill／工具目录与请求。** 同名、近义和适用条件不同的候选要保留正文依据。`read`日志只能说明曾加载，未加载不等于不需要；未知标签应跳过，不能自动造负例。需要人工核对或独立标注的正例、相邻能力硬负例、无工具需求、候选缺失、否定／目标撤销及多工具需求。路由结果不能越过执行层的权限、状态和参数校验。

先按原始请求／会话／任务来源分组切分Train、Dev、Cal-fit、Cal-policy、Test，之后才做候选配对、翻译、改写或选项顺序增强。同一原始请求派生的正负例必须同组。分别报告已见工具的新请求与未见工具／新版本描述；中文不能用英语集替代。Cal-fit拟合温度，独立Cal-policy选择完整接受／转交规则，Test只作冻结评估。若小样本探索共用校准数据，须明确选择偏差，不声称满足原独立校准风险界的前提。

| 公共材料 | 能提供什么 | 不能替代什么 |
|---|---|---|
| [ToolRet-Training-20w](https://huggingface.co/datasets/mangopy/ToolRet-Training-20w) | HF原始字段为`query`、`positive`、`negative`（另有`id`、`prompt`）；正负项是工具文档字符串，可作候选条件判断预热；原仓为Apache-2.0 | HF卡未明确填写该汇总数据的license；还需保留组成来源的许可。英语工具检索不等于中文Skill效果，默认负例也不保证没有替代合法工具 |
| [When2Call](https://huggingface.co/datasets/nvidia/When2Call) | CC-BY4.0；何时调用、何时追问、工具不可用的外部诊断；test含显式决策类型 | 训练文件是tools＋messages，非调用回答没有显式类别，不能凭正则可靠区分直接答／追问／拒判；不要把test转成训练 |
| [stanley-nv/tool-routing-data](https://huggingface.co/datasets/stanley-nv/tool-routing-data) | CC-BY4.0；已发布工具级分离与other标签，适合小规模管道诊断 | 全部由LLM／模板生成、无真实用户或人工核验，只有英语单工具请求；作者说明部分测试曾参与开发 |
| [xLAM 60k](https://huggingface.co/datasets/Salesforce/xlam-function-calling-60k) | CC-BY4.0；工具规格和调用目标 | 当前为需接受访问条件的gated数据，匿名原文返回401；没有天然覆盖真实Skill无适用项 |
| [SkillRouter](https://github.com/zhengyanzhao1997/SkillRouter) | 大目录、完整Skill正文与检索／重排的外部参考 | 公开核心评测仅75题，发布脚本以CUDA为前提；本轮未确认数据卡单独许可，不作为未经审查的默认训练源 |

ToolRet正例被移出候选集合可生成“当前候选无可用项”的受控反例，但必须同时排除其他合法等价工具；它不代表自然流量中的无工具需求。CLINC OOS可检查开放集管道，不能当真实工具／Skill路由的独立效果证据。已公开工具题也可能进入预训练或现成决策模型的适配集，需要新请求和留出工具验证迁移。

## 固定版本与训练起步

| 对象 | 核查版本 |
|---|---|
| Laya代码 | `d1282e791d71e92f24f816ff3836e4fd1c2ded4a`，2026-11-18，项目版本0.4.37 |
| 多语种权重 | `convaiinnovations/laya-multilingual@92d22143468d8af669dc1a5a0480a2b21b4fe56e`，Apache-2.0 |
| English权重 | `convaiinnovations/laya@e333cb7c823cd1787276228260f56d02fbf5180b`，Apache-2.0 |
| LayaStudio参考 | `71f1a01466e247c4ac9a8afe681e3491cb0f2e06` |
| ToolRet训练数据 | `mangopy/ToolRet-Training-20w@fdf5a317455b1e60785de7ba587496aa6cc878e4` |
| When2Call数据 | `nvidia/When2Call@0582f7749df63a96fdc3070932e83e72396ace53` |

首轮不训练一个通用Jev复制品，也不训练路由后执行器。固定一个候选召回方式；比较原版Laya、监督后训练Laya、简单embedding／词法基线。先100条或少量更新验证真实forward、backward、保存重载与内存，再决定完整训练。322M全参数fp32的权重＋梯度＋Adam一二阶状态静态约5.2GB，**不包含激活、临时张量和运行时缓存**；48GB是合理起点，不是已测峰值或可行性保证。MPS算子、吞吐、swap及内存必须在目标机记录。

复用单一源码checkout，在其独立环境准备；若已有同一上游则复用，不再clone。以下为待目标机执行的命令，依赖解析后保存锁定版本：

```bash
git clone https://github.com/NandhaKishorM/laya.git
cd laya
git checkout d1282e791d71e92f24f816ff3836e4fd1c2ded4a
uv venv --python 3.12
source .venv/bin/activate
uv pip install -e .
uv pip freeze > requirements-resolved.txt
```

确认MPS设备，再按固定revision下载多语种权重至独立本地目录：

```bash
python - <<'PY'
import torch
from huggingface_hub import snapshot_download
assert torch.backends.mps.is_available(), "当前Python环境没有可用MPS"
print("PyTorch:", torch.__version__, "MPS available")
snapshot_download(
    "convaiinnovations/laya-multilingual",
    revision="92d22143468d8af669dc1a5a0480a2b21b4fe56e",
    local_dir="base-multilingual",
    allow_patterns=["rl_agent_config.json", "model.safetensors", "encoder/*", "tokenizer/*"],
)
PY
```

官方`--dry-run`不载入模型权重参与计算，但其checkpoint解析仍可能下载`model.safetensors`，因此不要把它解释为完全不下载权重。上面的显式下载固定了模型版本；权重仓库revision和代码commit是两个独立标识。冻结的多语种配置为`max_len=1024`、`head_max_len=256`、温度全1；仓库日期不代表新增训练日期。

一条**示意格式**，不作训练／评测样本：

```json
{"state":{"request":"把这份PDF中的表格整理成Excel","candidate":{"name":"pdf","description":"读取和提取PDF文字与表格"}},"questions":{"load":{"type":"choice","instructions":"依据当前请求和候选的实际能力，是否需要加载该候选？","criteria":{"A":"需要该候选完成请求的一部分","B":"不需要或该候选不适用"}}},"expected":{"load":"A"}}
```

候选配对标签需要多工具语义：该例的PDF能力成立，不排斥Excel能力同时成立。`A/B`标签顺序在服务端固定；必须另测顺序交换并正确映射回标签，不把分数变化当改好了。候选正文、请求状态、选项模板、截断预算保持训练／评估／服务一致。

官方Python API比CLI多暴露MPS检查点及校准切分控制，建议以此起步：

先在同一目录准备五份已按原始请求分组隔离的`train.jsonl`、`dev.jsonl`、`cal-fit.jsonl`、`cal-policy.jsonl`、`test.jsonl`。下面代码保存为`train_router.py`后执行`python train_router.py`；这不是自动生成标签或下载业务数据的脚本。

```python
from laya.train import TrainConfig, finetune

report = finetune(
    "train.jsonl", "./base-multilingual", "./route-model",
    TrainConfig(
        loss="soft-ce", epochs=2, micro_batch=1, grad_accum=16,
        encoder_lr=1e-5, head_lr=1e-4, max_len=1024, head_max_len=256,
        amp=False, gradient_checkpointing=True,
        calib_frac=0.0, calib_max=0, eval_data="dev.jsonl", seed=42,
    ), device="mps",
)
```

这是工程起步配置，未在目标机调优。正式比较时，分别从同一冻结基座运行`loss="soft-ce"`与`loss="rlcd"`，至少记录多种子差值和失败；每组使用不同输出目录，不能接着上一组的已训练权重继续跑。若改为多个候选的单题`choice`，官方支持`shuffle_options=("choice",)`。`freeze_encoder=True`可作便宜head-only基线。不要沿用trainer默认item随机校准切分去处理同请求的多候选派生样本。

固定A/B示例协议可直接用实际推理runtime收集独立校准记录。下面代码保存为`calibrate_router.py`，执行`python calibrate_router.py`。它只拟合温度，没有更新模型权重，也没有替你决定业务拒判门槛：

```python
import json
import laya
from laya.calibrate import records_from_labeled

agent = laya.load("./route-model", device="mps")
pairs = []
with open("cal-fit.jsonl", encoding="utf-8") as source:
    for line in source:
        if not line.strip():
            continue
        row = json.loads(line)
        assert set(row["questions"]) == {"load"}
        assert row["questions"]["load"]["type"] == "choice"
        assert list(row["questions"]["load"]["criteria"]) == ["A", "B"]
        label = row["expected"]["load"]
        assert label in {"A", "B"}
        target = [float(label == "A"), float(label == "B")]
        pairs.append((row["state"], row["questions"], {"load": target}))
assert pairs, "校准集为空"
records = records_from_labeled(agent, pairs)
assert len(records) == len(pairs), "部分校准问题未编码，需先检查数据"
fitted = agent.fit_temperatures(records)
agent.save_calibration("route-calibration.json")
print(fitted)
```

新进程须先`agent = laya.load("./route-model", device="mps")`，再`agent.load_calibration("route-calibration.json")`。每个候选读取`agent.predict(state, questions)["answers"]["load"]["probabilities"]["A"]`。在独立`cal-policy.jsonl`上选择完整规则，冻结后用于Test：概率达到规则阈值时选入，全部低于阈值返回空集合／交回主Agent处理。不能把B的高置信度当成应该加载候选。规则需按正例误触发、漏载及请求分组的风险—覆盖选择，不能以多数负例拉低总体错误率来掩盖错误加载；Test不参与选择。仅做经验阈值扫描不自动得到有限样本风险证书，若需风险界须另核方法假设和独立性。

温度缩放不改变argmax，不能据此宣称准确率提高。多候选只用一个全局A/B问题，`questions.json`可以复用；若改为逐请求变化的choice候选集合，运行时必须重建问题，不能依赖trainer仅保存首个版本的`questions.json`。[校准源码](https://github.com/NandhaKishorM/laya/blob/d1282e791d71e92f24f816ff3836e4fd1c2ded4a/laya/calibrate.py)、[Agent保存／加载接口](https://github.com/NandhaKishorM/laya/blob/d1282e791d71e92f24f816ff3836e4fd1c2ded4a/laya/agent.py)

最终至少报告每请求候选召回、路由precision／recall、无适用项误触发与漏判、多工具集合覆盖、覆盖率—错误率、分组置信区间、校准误差及完整检索＋判定延迟／内存。各候选共享请求，不是独立样本。进一步的工具执行成功与任务完成率需要冻结执行器后另验，单凭路由标签分数不能推断。

当前可确认的是：有适配该任务的数据格式和官方Mac训练／保存／校准入口。没有训练完成、模型优于基线、48GB实际峰值或真实任务效果的本地证据。

本轮实际检查：从固定版本读取训练与校准源码；执行官方`train_cli.py --help`成功，并用官方parser解析`soft-ce`、MPS、批大小、梯度累积、长度及seed等参数；本文JSON示例和Python代码块通过语法检查。未安装训练依赖、下载模型权重或执行forward／backward。CLI入口检查与源码核查不替代目标机训练smoke；目标机完成后保存实际依赖版本、命令、日志、跳过样本数、checkpoint与校准文件，再报告效果。
