# 2026-10-13 · Multimodal releases, calibration and deployment

[Home](../README.md) · [中文首页](../README.zh-CN.md) · [Models](../docs/models.md) · [Evidence](../docs/evidence.md) · [Sources](../docs/sources.md)

This bounded primary-source review adds Decision 3.0, Intern-Decision and Verdict as three families, plus FluidUse as a deployment resource. It updates the live Index description and reviews all six changes queued by the October 12 [source-watch comment](https://github.com/leoncuhk/awesome-decision-models/issues/2#issuecomment-6127380789). E01–E11 and meaningful previous sources remain historical records. No model inference, external model installation, paid calls or independent reproduction was performed.

## Decision 3.0 identity and mechanism

One family contains six v3.1.0 checkpoints. All six model cards, manifests, configurations, Transformers loaders, runtimes and histories were read at the following fixed repository revisions on October 13. Card parameter counts and nominal base-size labels differ:

| Checkpoint | Card parameters (vision included) | Nominal size label | Reviewed repository revision |
| --- | --- | --- | --- |
| d3 | 26.09B | 27B | [093cffbaa7be](https://huggingface.co/vllm-sr/d3/tree/093cffbaa7be6f5dfe14252ae7e80c396c06dbd9) |
| d3-flash | 8.39B | 9B | [f6075bff3c0f](https://huggingface.co/vllm-sr/d3-flash/tree/f6075bff3c0f7d5704e353d0fb2ebf94888d1691) |
| d3-mini | 4.54B | 4B | [0e78bbdbe3cf](https://huggingface.co/vllm-sr/d3-mini/tree/0e78bbdbe3cf480ed1461c185c9e0c4fa9258011) |
| d3-nano | 2.21B | 2B | [9d9b937f5f11](https://huggingface.co/vllm-sr/d3-nano/tree/9d9b937f5f117f78c030ea7ba677c0b3d328ec58) |
| d3-lite | 0.85B | 0.8B | [3c49f5c0bd48](https://huggingface.co/vllm-sr/d3-lite/tree/3c49f5c0bd48a4b28e29b8ec1f38f56e199f3d61) |
| d3-edge | 0.59B | 0.6B | [20c745653400](https://huggingface.co/vllm-sr/d3-edge/tree/20c745653400d191ecacd99c4eafc0c5900dc15e) |

The manifests separately count loaded text/vision/readout parameters; the [source register](../docs/sources.md) retains each author-supplied package identity hash. The local hashes of the downloaded loader/runtime text match their manifests. This limited text check is not weight-byte verification. A package identity hash, backbone revision, repository commit and evaluated serving version remain distinct.

d3 declares Qwen3.8-27B in its manifest and `qwen3_5` in its running architecture; neither label proves a provenance conflict. Other checkpoints derive from Qwen3.5; edge derives from the 0.8B base with fewer released parameters. All six declare Apache-2.0 and text/image/video inputs.

The [runtime](https://huggingface.co/vllm-sr/d3/blob/093cffbaa7be6f5dfe14252ae7e80c396c06dbd9/d3_runtime.py) uses independent prompt rows and last-position answer-code readout, with masked softmax at T=1.0. A batch processes several rows; it does not encode all questions once in one shared text sequence. Optional reversed-choice averaging is off by default. Full-attention layers are noncausal while DeltaNet remains causal. Public training overlap, decontamination and held-out calibration reports were not established; unknown is preserved without alleging contamination. Runtime/server/documentation commits on October 12 do not establish a new trained model or performance gain.

## Keep evaluation boundaries separate

- [E12](../docs/evidence.md#e12): d3 internal 0.3.1 text/vision composites and MI325X medians. Other model scores come from October 9–10 boards, not a common rerun; several visual datasets are approximate rebuilds. The live page says 0.3.2, but complete dynamic ranks were not audited and no current first place is asserted. The 55/273/553 ms values are single-request medians, not end-to-end P95.
- [E13](../docs/evidence.md#e13): six checkpoints' author-reported full public-kit scores over 140178 requests. These are public-only index aggregates, not 140178 independent task families or raw accuracy.
- [E14](../docs/evidence.md#e14): video Perception Test validation at three choices per question. Defaults sample 2 fps, at most 32 frames. Audio, brief-event recall and streaming reliability are unvalidated.
- [E15](../docs/evidence.md#e15): converter/team-associated M5 Pro 24 GB PyTorch versus Core ML reports, with 231-task exact-label JevBench and 2000-question typed-decisions kept apart from Index. The live article's later flash/Mario addition is not present in the pinned lite/nano/mini conversion inventory. Parity fixtures do not establish universal equivalence.
- [E16](../docs/evidence.md#e16): d3-lite 1000-sample PR throughput (two questions per PR) versus d3-mini's separate maintainer-label agreement. Throughput is not correctness.
- [E17](../docs/evidence.md#e17): an original third-party WebMCP test has 75 authored questions, near-tied model counts, three rule-layer failures and a test-selected Nano variant. The independent jev-ai.pro platform self-reports a TypeSafe connection; Microsoft was tested through decisions-api.dev. Provider-path times and prices are not official direct-vendor figures. Inclusion supplies a concrete failure analysis, not a winner.

The reviewed cards put vLLM-SR Engine support in the dev channel. Ordinary vLLM chat compatibility is not established. Core ML uses its own conversion, precision and context buckets; check those independently before deployment.

## Adjacent releases with distinct mechanisms

**Intern-Decision** has three inspected Qwen3.5 sizes. Its causal skeleton scores multiple fields in one pass, unlike Decision 3.0's separate question rows. HF supports images; the current FluidUse 0.8B conversion is text-only with smaller buckets. Original training and private fitting/validation records remain unavailable. [E18](../docs/evidence.md#e18) records the 96-case exact-distribution calibration pilot, with 24 families and 48 paired settings; expected Brier/ECE is not sampled-label accuracy or a production risk bound. Size/backend-specific temperature must not be transferred blindly.

**Verdict** contributes an inspectable small encoder with an explicit missing-evidence candidate. [E19](../docs/evidence.md#e19) retains the converter's evaluation-versus-serving renderer/calibrator discrepancy. [E20](../docs/evidence.md#e20) preserves the author's severe hard-negative/synonym abstention failure. A trained abstention option is not a distribution-independent guarantee. Rejected LUT8 conversion results remain visible. The independent OpenJev name does not imply an official TypeSafe release.

FluidUse's native managers and Python-assisted bridges are grouped as one deployment entry. Serial bridge queues, timeout shutdown, per-model slots and packages matter to selection. Its unrelated OCR/agent demos and repetitive wrappers are outside this review; support-matrix mentions alone do not justify adding every model.

## Source-watch disposition

| Queued source | Inspected change | Curatorial action |
| --- | --- | --- |
| Kev README | Isolated accelerator probes, explicit CPU/fail-closed behavior and MLX handling; later Modal concurrency change | Add current source pin and deployment note; retain historical weights/quality/calibration limits. |
| CLM README | Only BibTeX title shortened at d5f9ef0 | Add source-review receipt; no new performance or weight claim. |
| GLiNER runtime | Transformers 5/dependency caps and packed DisentangledFlash documentation | Update compatibility scope; no unmeasured end-to-end gain. |
| GLiNER Decide Hub | README/config/schema-extraction integration and decision-model tag | Compare old/new trees: model.safetensors LFS hash and tokenizer blobs unchanged. Metadata identity check is not local weight verification. E04 remains archival. |
| Jev primitives | Current body describes question IDs, independent answers and dependent requests | Refresh source receipt; no authenticated previous-body diff, so do not assert which sentence caused the HTML change. |
| Jev confidence | Current body still defines Choice/Score confidence from distributions and Noul P(yes) | Retain distinction from empirical calibration/risk; dynamic HTML change alone is inconclusive. |

New watch sources stay on the existing allowed GitHub/Hugging Face hosts. No workflow schedule, host allowlist, permissions or synchronization method changes. The [selection guide](../docs/selection-guide.md#6-october-2026-deployment-checks--10-月部署验收) now gives task-specific checks for multi-field encoding, conversion fidelity, actual calibration, abstention and preprocessing rules.

## Validation and publication boundary

Local validation passed the renderer/check, schema/reference/numeric/bilingual/local-link validator, 38 offline unit tests, three disposable-local-remote publishing cases, Python AST/shell syntax checks and manifest verification. The 11 historical evidence records remain byte-for-byte equivalent as JSON objects. A fresh local watcher scan reached all 35 endpoints with zero fetch errors; it established a separate local baseline and made no GitHub Issue writes. Source review is separate from these checks. Publication is authorized as a normal fast-forward main push after a fresh fetch; remote exact commit and CI terminal state must be checked before reporting success.

## 中文摘要

新增 Decision 3.0 六检查点系列、Intern-Decision 三型号系列、Verdict，以及 FluidUse 部署资源。固定卡片／代码／manifest 版本，保留作者声明的包标识而不冒称验证权重；区分基座名义尺寸与实际参数、单题行批处理与多字段共享序列。内部 Index、公共套件、231-task JevBench、视频验证集、PR 吞吐与业务标签一致率分别记录，当前动态榜单未完整核验。

Jev 中介服务不是官方直连；75 问应用测试保留小样本、规则前置错误和测试后选择偏差。Intern 的精确分布试验、Verdict 的服务校准差异与拒答失败提供不同的可靠性检查点。六项 watcher 变化均做出处置，文档／运行库／元数据变化不等同于新权重或能力提升。只做公开来源研究和仓库验证，不运行或安装外部模型，也不改变仓库既有目录、同步、权限或监测调度。
