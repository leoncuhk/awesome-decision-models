# 2026-10-18 · Runtime correctness, benchmark identity and risk budgets

[Home](../README.md) · [中文首页](../README.zh-CN.md) · [Protocol comparison](../docs/selection-guide.md#decision-index-protocols) · [Evidence](../docs/evidence.md#e32)

## Reviewed changes

- **StartLux:** fixed list-form `criteria`/`options` normalization before wide-candidate tournaments, including a 26-choice plus none slot. Mapping-form routing already worked. The optional vLLM dependency is now 0.31.0, distinct from the paper accuracy stack. All eight previously pinned v1.1 model-repository revisions remain unchanged. These are request/dependency changes, not new weights or measured accuracy.
- **Strands:** request-local token offsets avoid a concurrency race in pointer probabilities; tokenizer locking and prefix-cache fallback address shared state. Eval/calibrate now reuse serving preparation, so CPU/MPS kernel/dtype and calibration artifacts must be matched to deployment. Five v1 seed-0 training configs are newly inspectable; Qwen mix/teacher inputs and Gemma code data still prevent full replay. Historical overlap, CUDA and missing-image findings remain.
- **Drex:** update the existing family with v2.0 rather than create a duplicate. Fixed GitHub code/card, public HF snapshot, 16 safetensors shard identities and the pointer head's published LFS SHA-256 are now inspectable. These are publisher metadata identities, not independently verified tensor bytes or a manifest tying the benchmark run to those weights. Qwen3.6 branding uses a Qwen3_5Moe runtime; the loader retains language only and drops vision. Default state-plus-one-question context is 16384, configurable maximum 131072. Custom weight license restrictions remain. [E32](../docs/evidence.md#e32) preserves the author JevBench counts (198/231 versus Jev 1.13.0 200/231), without a significance or overall-winner claim.
- **Artificial Analysis Decision Index:** one new evaluation resource, methodology 1.0. Its four equal-weight components, private knowledge items, filtered safety subset and conditional non-hallucination denominator differ from the HF-hosted community index. No current rank or leaderboard score imported; neither index certifies calibration or end-to-end service performance.
- **Risk-budget paper:** one new reliability resource, arXiv v1 by Messoudi and Mansar. Fixed-sequence LTT certifies a binary policy's population FOR under independent Fit/Cal and same-population iid assumptions. It does not certify each answer, arbitrary multiclass/image policies or shifted traffic. No certificate triggers policy fallback. Six English-text datasets/single seed and constructed retrieval mixtures limit empirical transfer. The paired adaptation guides now state these conditions; no empirical gain imported.

## Source and publication boundaries

The source register pins five runtime/config commits and four Drex release/runtime/weight/license records, plus the two new methodology sources. All 177 prior source objects and E01–E31 are preserved. There are 52 selected resources, 18 core families, 188 sources and 32 evidence records. Watcher endpoints remain at 39; no new host, permission or schedule is added. Canonical JSON → bilingual generation remains the workflow. Source inspection is not reproduction: no third-party code, model weights, installers or billable inference were executed. Frozen local checks and the exact published commit/CI outcome are reported separately.

## 中文摘要

现有 StartLux 更新长选项请求归约及 vLLM 依赖，八个权重库 revision 未变；Strands 更新每请求偏移／分词并发、服务与评测准备一致性，五份配置不等于缺失数据已公开。现有 Drex 系列补入 v2.0 的固定 HF snapshot、16 分片与 head 的发布者 LFS 标识，未下载核验张量；基座视觉配置不等于本模型支持图片。E32 保留公共 JevBench 作者对比中的负面结果，不推断显著胜负。新增 AA 同名指数方法与风险预算预印本，分开发布者、任务、私有覆盖、条件风险及校准抽样保证；不拼总榜，不当作逐题正确或图像领域迁移的证明。旧来源与历史证据保留，监测权限和目录／同步方式不变。
