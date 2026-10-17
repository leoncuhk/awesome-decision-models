# 2026-10-17 · StartLux, DecisionPivot and adaptive computation

[Home](../README.md) · [中文首页](../README.zh-CN.md) · [Mechanism comparison / 机制比较](../docs/decision-readout-and-reasoning.md) · [Evidence](../docs/evidence.md)

## Scope and identities

Add one StartLux v1.1 family (five Instant and three AutoThink checkpoints) and one DecisionPivot evaluation resource. The existing Perplexity family now distinguishes archived v1 from native v1.1; no duplicate family is created. Sources fix arXiv v1, author repository, all eight model cards, DecisionPivot data/generator repositories and native Decider v1.1 code/config. Source revisions do not substitute for local weight hashes. E01–E28 and all 146 earlier source objects remain unchanged.

## Mechanism and evidence

StartLux uses existing LM option-letter rows rather than a new classifier head. Instant changes full-attention masks while linear-attention remains causal; AutoThink keeps causal attention, optionally generates a trace and mixes two distributions. RLCD² trains reasoning against a frozen probability scorer with proper-score and length rewards; the runtime is not the complete training pipeline. Archived v1 text LoRA is not evidence of a released v1.1 image-training recipe. Jev's undisclosed RLCD is not identified with this algorithm.

[E29](../docs/evidence.md#e29) keeps public DI 0.3 development-selected scores separate from the private/full board and existing D3 0.3.2 records. [E30](../docs/evidence.md#e30) records the paper's DecisionPivot release comparison as author-reported; corrected dataset versions, intermediate committed tables, old hosted-reference coverage and later engine reruns remain distinct. Public generators and independently implemented solvers are inspectable assets, not an independent external replication. Task-family exposure is not itself proof of exact test-item leakage.

[E31](../docs/evidence.md#e31) preserves the 9B pre/post-RLCD² forced-reasoning cohort: shorter traces and improved termination with similar accuracy. It is not a universal calibration or end-to-end latency claim. Paper gate 0.9 and current service default 0.6 must not share score labels. Readout-only timing excludes complete conditional reasoning; vLLM accuracy and speed versions differ. Images, context limits, video-disabled launcher, none alarms and policy-conditioned calibration are explicit in the mechanism guide.

## Licensing and maintenance

StartLux code is Apache-2.0; the eight inspected v1.1 weight cards are CC BY-NC 4.0, so commercial use needs separate licensing. DecisionPivot generated core is CC BY 4.0, reused public data retain their own terms, and its code is Apache-2.0. Decider v1.1 declares Apache-2.0; inference settings and full data replay remain separately qualified.

Two watcher endpoints are added on already supported GitHub/Hugging Face hosts. The watcher remains change detection, not performance certification. No schedule, permissions, host allowlist or directory structure is changed. Canonical JSON → five generated documents remains the workflow, with the manual bilingual mechanism guide linked from templates and existing selection/adaptation guides. Final frozen validation and actual publication/CI outcome are reported separately; no model/dependency installation, model run or benchmark reproduction was performed.

## 中文摘要

新增一个 StartLux 系列和一个 DecisionPivot 评测资源，补核现有 Decider v1.1，保留旧版来源。原理比较分开 LM 字母读出与 255 答码头、注意力、监督／RL 训练、条件推理和实际服务策略。E29–E31 分别保存公共 DI 开发选择、作者 DecisionPivot 对比及强制推理子集的 RLCD² 效率证据；不拼完整榜、修正版数据与中间检查点，也不把家族覆盖说成已证实测试题泄漏。公开生成器不等于独立复现，更多思考不能补造缺失上下文，权重非商业许可与推理代码许可分别标明。
