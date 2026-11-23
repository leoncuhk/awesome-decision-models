# P11 多模态判断的后训练

成熟度：**有据，陷阱多** · 层：多模态 · 落地：[多模态后训练](../playbooks/multimodal-posttraining.md)

## 问题

用企业的图文客服数据（截图＋意图标签，可补历史上下文）后训练一个决策模型。什么路径真的训练了视觉？图像到底提供了多少增量？在本地硬件上能否完成？

## 当前判断

1. **视觉路径常常没有真正参与训练。** “能看图推理”和“能用图训练”是两回事，每个候选都要逐项核实。
2. **意图依赖证据，不等于截图类别。** 同一张图在不同上下文下可能是不同诉求，所以 image-only、context-only、OCR＋context、image＋context 四组对照必须都做。
3. **先过技术门槛，再比较质量。** 视觉输入、mask、梯度、保存重载、服务概率，逐项过关后才扩大数据。

置信度：中。

## 证据

- 视觉丢失或冻结的实例：
  - D3 官方 wrapper 拒绝训练；第三方 Vis 的训练路径只保留文本权重，去掉了视觉塔；
  - mlx-decision 拒绝图像训练；
  - Strands v2 只用文本训练，继承下来的图像输入不等于做过图像适配；
  - ezjev 没有视觉张量路径。
- 真正带图训练的实例：
  - Intern-Decision：17,880 条样本中 5,500 条带图，冻结视觉塔与 projector，训练语言骨干；走 CUDA/XTuner，不是 LoRA；
  - MLX-VLM：有图像条件、completion-only 的语言侧 adapter 源码路径；
  - Jev-Decision：Qwen3-VL-2B 上 pointer head 加 LoRA 的代码先例，没有公开结果；
  - **Unsloth `FastDecisionModel`**（2026-11）：Qwen3.5 VLM 加 Clef 式联合头，LoRA 只加在语言侧，视觉冻结但参与前向；源码测试包含图像影响输出及梯度路径断言（需区分测试替身与真实VLM），并有 Apple Silicon（MLX）路径。这是值得验证的图文决策头实现候选，作者基准只覆盖文本任务（[源码](https://github.com/unslothai/unsloth/blob/8b7cde79ebf5a901b2fd936bbee214fb8c7562c7/tests/test_decision_images.py)）。
- MIRE / WWW2025（23 类场景加 23 类意图）：官方基线是 Qwen2-VL-7B 全参 SFT。前三名线上分差只有 0.0034，用到了伪标签、model soup 和模型合并，无法归因到单项技巧（[E33](../docs/evidence.md#e33)、[E28](../docs/evidence.md#e28)）。
- 冻结视觉参数仍需执行视觉编码器；冻结不等于关闭视觉输入。

## 开放

- 本轮未确认可直接回答本次中文图文客服受控适配增量的公开证据。
- H1：可见输入能确定目标，且图像提供增量信息。
- H2：受限适配相对最强冻结基线，能降低每案件净成本。
- H3：特定读出或训练改动提供独立价值。

预注册的推翻条件和实验矩阵见 [playbook](../playbooks/multimodal-posttraining.md)。

## 企业含义

在 M5 Pro 48GB 上：主候选 Qwen3.5-4B，图像条件语言侧 QLoRA；回退用 Qwen3.5-2B；Intern-Decision 作为参照系统。读出有两种实现可比：MLX-VLM 的生成式短标签 SFT，以及 Unsloth MLX 的决策头训练。按 G0–G4 关卡推进。

## 关键阅读

[Intern-Decision](https://arxiv.org/html/2610.22131v1) · [MLX-VLM training](https://github.com/Blaizzy/mlx-vlm/blob/2ceff4c14b991370a459d14eb49d1bedf4fb9e84/docs/training.md) · [MIRE](https://github.com/liujunwen23/MIRE/tree/d101287af90d114c5bf0cbfbd56fe9c52358e3bb) · [EcomMIR](https://zhoushengisnoob.github.io/papers/WWWComp.pdf) · [VLTest](https://arxiv.org/html/2610.30794v1)
