# 2026-10-16 · Multimodal fine-tuning research and evidence boundaries

[Home](../README.md) · [中文首页](../README.zh-CN.md) · [Research plan](../docs/multimodal-decision-finetuning.md) · [中文研究方案](../docs/multimodal-decision-finetuning.zh-CN.md)

## Research and resources

The new paired research guides specify general multimodal customer-support intent experiments. They compare OCR/text, a fixed-schema VLM, short-label LoRA-SFT and a matched candidate-logit LoRA arm. Facts, intent and permitted actions remain separate; unknown/multilabel cases, contemporaneous evidence, grouped splits, image ablations, calibration, export parity and complete handling costs are explicit. These are proposed experiments, not training results or deployments.

Three resources are added without creating new core model families: MIRE/EcomMIR evaluation, ezjev text candidate-logit training and decision-pacman distillation. Nine source snapshots fix the inspected public code/cards or paper identity. MIRE's official Qwen2-VL baseline is full SFT. ezjev and the reviewed Pac-Man trainer use text inputs, so their training mechanisms do not establish image fine-tuning. The ezjev card warns of non-commercial/unstated training-data terms. The Pac-Man report preserves lost generality alongside specialization gains; no numerical result is imported as an independent reproduction.

Intern-Decision's card now identifies its inspected full-language-parameter training configuration, frozen visual components and masked full-vocabulary answer-token CE. Gold codes stay in labels; causal fields see earlier placeholders, not completed answers. Decision 3.0's inspected wrapper rejects train(True) as inference-only. Neither generic PEFT documentation nor a compatible base model proves a working D3 multimodal training/export path. Historical model/source/evaluation evidence remains intact.

## EcomMIR evidence

[E28](../docs/evidence.md#e28) records author-reported Round 2 intent F1 0.9420 and scene F1 0.8278 from the primary four-page paper. These are different tasks and combined interventions. Round 1 pseudo-labels, cleaning, hierarchy, augmentation and scene model soup prevent attributing the result to LoRA alone or describing it as 1,000-example-only training with untouched evaluation-round data. Exact scored IDs, full outputs, checkpoint hashes, F1 aggregation details and independent replay remain unestablished. Training hardware is not serving latency or complete cost.

## Validation scope

Canonical JSON → five generated documents remains the synchronization path; the deeper paired guides are manual documents linked from the existing guide and bilingual templates. No directory reorganization, watcher changes, dependency installation or model execution is required. E01–E27 and the 137 earlier source objects are preserved unchanged. Frozen final files are checked with renderer consistency, structural/link validation, offline unit tests, disposable-local-remote publishing tests, Python/shell syntax and manifest hashes. Actual publication commit and CI status belong in the completion report, not a prewritten success claim.

## 中文摘要

新增通用多模态客服微调研究方案的中英文版本，明确对照实验、输入与标签、图像训练链路、损失与占位符、LoRA／蒸馏、导出及风险—成本验收。新增三项有边界的训练／评测资源与九条来源记录，核心模型系列数不变。E28 单列 EcomMIR 两项作者报告，保留伪标签与组合干预限制；不把文本训练、全参数配置或推理 wrapper 误称为现成的图像 LoRA 配方。未执行训练、推理、部署或成绩复现。
