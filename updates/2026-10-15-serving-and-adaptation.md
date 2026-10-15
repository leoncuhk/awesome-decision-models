# 2026-10-15 · Serving, semantic features and domain adaptation

[Home](../README.md) · [中文首页](../README.zh-CN.md) · [Models](../docs/models.md) · [Evidence](../docs/evidence.md) · [Selection guide](../docs/selection-guide.md)

This review updates Decision 3.0/Jev and adds two method/evaluation resources, not new model families. E01–E20 and their source snapshots remain intact. No external model was installed or run, no paid API was called, and no private images or business details were collected.

## Decision 3.0 identity and evaluation

Six old/new root trees, manifests and calibration configurations were compared. All weight/readout Git/LFS identities and manifest model identities remain unchanged; temperature stays 1.0. This is source/metadata verification, not a local tensor-byte hash check.

| Checkpoint | Previous → reviewed source revision | Weight/readout files compared | Model identity / calibration |
| --- | --- | --- | --- |
| d3 | `093cffbaa7be` → [`225be8b1e227`](https://huggingface.co/vllm-sr/d3/tree/225be8b1e2270becab69c5fe05b26f99cbbdd66b) | 12 | unchanged / 未变 |
| d3-flash | `f6075bff3c0f` → [`8b35c853b90e`](https://huggingface.co/vllm-sr/d3-flash/tree/8b35c853b90e777595ec36bacae820fe08ea077a) | 5 | unchanged / 未变 |
| d3-mini | `0e78bbdbe3cf` → [`97dd054df4b3`](https://huggingface.co/vllm-sr/d3-mini/tree/97dd054df4b3e0b3beb6af23ab8c82b7c0052e0e) | 3 | unchanged / 未变 |
| d3-nano | `9d9b937f5f11` → [`aeb70d4dd53e`](https://huggingface.co/vllm-sr/d3-nano/tree/aeb70d4dd53ed25b855c3b0a66394b8fe265db7f) | 2 | unchanged / 未变 |
| d3-lite | `3c49f5c0bd48` → [`9c10703193af`](https://huggingface.co/vllm-sr/d3-lite/tree/9c10703193afc7c7d28c88201c0364bfbbf58320) | 2 | unchanged / 未变 |
| d3-edge | `20c745653400` → [`cab71e6ad346`](https://huggingface.co/vllm-sr/d3-edge/tree/cab71e6ad3461b8086d51ddb572c656babd63b0b) | 2 | unchanged / 未变 |

The inspected d3 runtime diff changes verification scope: fast/full inspect loaded files; release additionally hashes documentation/assets and checks unlisted files. New scores, charts, demo links and serving descriptions do not establish retraining. Latest model-repository pointers were rechecked after the execution environment reconnected and still match these pins.

[E21](../docs/evidence.md#e21) records Index 0.3.2 JSON retrieved October 15, generated October 14 and rechecked unchanged after reconnect. d3 has text 66.26 and vision 71.26. The text board puts d3 and linne-oak in the same first tie band (0.9 points). JSON contains 166 text entries and 34 vision entrants versus the card's earlier 149/33 counts. A stale count or numerical lead is not an uncontested winner. The board changelog describes omitted scoring sets corrected and public-suite changes; historical 0.3.1/private/public-only evidence stays separate. Hidden items and full raw runs remain unaudited.

## Two distinct serving paths

[E22](../docs/evidence.md#e22) separates updated AutoModel timings from vLLM-SR Engine batching. Reported 27 text requests/s at p99 under 1 s has a specific closed-loop load, source build and overload policy. Default batching changes near-tie decisions; former unbatched byte parity is not a default-mode guarantee. Startup assumes local weights and excludes CLI image pulls.

[E23](../docs/evidence.md#e23) records native vLLM support merged October 14 at [89cab550](https://github.com/vllm-project/vllm/commit/89cab550862e4b7f08d70c19682121362d7dd0c5) via [PR #61565](https://github.com/vllm-project/vllm/pull/61565), at 17:10:56 UTC. Latest official v0.31.0 was published October 5, rechecked after reconnect; support therefore requires a post-merge source/nightly build as reviewed. The pinned [official mechanism](https://github.com/vllm-project/vllm/blob/89cab550862e4b7f08d70c19682121362d7dd0c5/docs/models/structured_decisions_models.md#decision-30) uses a custom classify readout and one independent prompt per question. Shared vision features do not imply one shared noncausal text encoding. Prefix caching/chunked prefill are off; schema/error/confidence/usage semantics differ from the package runtime. PR measurements cover d3/mini/edge on MI325X, not LoRA/CUDA; the later MI300X nightly check in the card is separate. Installation commands were not executed.

## Task evidence and semantic features

The [original financial-document report](https://insights.ml4trading.io/p/testing-jev-on-financial-documents), published October 13, discloses TypeSafe-provided API access for an unpaid evaluation and a vendor-suggested post-hoc prompt. [E24](../docs/evidence.md#e24), [E25](../docs/evidence.md#e25) and [E26](../docs/evidence.md#e26) keep earnings, filing-category and 90-day SEC follow-up protocols separate. Hindsight screening, unequal text windows, full-corpus TF-IDF preprocessing, residual company overlap and absence of forward-time separation limit conclusions. Later scoring evidence is not assumed to have entered the model input; historical pretraining exposure remains unknown. Same-sample hints and 99%-precision thresholds are post-hoc diagnostics, not validated live gates. No complete raw replay was performed here.

The [official feature-discovery cookbook](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery) describes an August 3 cached wine-review experiment, not a new October model release. [E27](../docs/evidence.md#e27) distinguishes direct Jev judgments, fixed semantic features and supervised CatBoost training. Development-only search and a conditional held-out bootstrap do not establish financial or visual-intent generalization.

## Image intent and domain adaptation

The bilingual [selection workflow](../docs/selection-guide.md#image-intent-adaptation) distinguishes image content from intent using contemporaneous context. It proposes OCR+text, VLM and multimodal-decision baselines, unknown/clarification policies, error-led adaptation, conversation/time/near-duplicate splits and held-out calibration. SFT, parameter-efficient training and distillation are conditional experiments requiring verified backbone/head/processor/export support. Generic text ModernBERT LoRA or VLM trainer documentation does not establish a D3 multimodal recipe. Intent remains separate from authority to act. These are curatorial methods, not measured business outcomes.

## Validation and publication scope

Canonical JSON → bilingual generation → existing validation remains the workflow. Two watcher endpoints are added on already allowed GitHub/TypeSafe hosts. Host allowlists, schedules, permissions, directory structure and synchronization remain unchanged. Local checks passed: renderer consistency, schema/references/numerical records/bilingual fields/local links, 38 offline unit tests, three disposable-local-remote publishing cases, Python AST/shell syntax and manifest hashes. All 121 historical source objects and 20 evidence objects remain exactly equivalent as JSON. A separate fresh local watcher baseline reached all 37 endpoints with zero fetch errors; no GitHub Issue was written. Final frozen files are rechecked before a normal main commit/push after fresh fetch; exact remote commit and CI terminal state are verified in the completion report.

## 中文摘要

更新 d3 的 0.3.2 评测和两条服务路径：六型号权重／校准标识未变，变化主要是文档和运行加载校验；原生 vLLM 已合入但尚未进入正式版。新榜单快照含共享第一平局带，不能以涨分或排名宣称重训提升。保留每题独立前向、批处理数值差异、硬件、并发、过载和冷启动边界。

新增财务文档原评测及语义特征＋监督预测资源。事实提取、公共标签和未来机构行为需要不同协议；API 支持、回顾筛选、事后提示和时间／来源划分限制均明确。葡萄酒案例不证明金融或多模态泛化。补充通用图片意图适配流程，无客户图片、雇主信息或私人案例；来源阅读不等于模型复现。
