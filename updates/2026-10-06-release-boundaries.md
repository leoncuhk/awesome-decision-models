# 2026-10-06 · Release identities and reliability boundaries

[Home](../README.md) · [中文首页](../README.zh-CN.md) · [Models](../docs/models.md) · [Evidence](../docs/evidence.md)

This refresh publishes the earlier [Clef / Strands source review](2026-10-02-clef-strands.md), updates Strands to its current release, adds Perplexity's public model, and corrects deployment and reliability descriptions. The October 2 note remains a dated review, not a description of today's reference checkpoint.

## What changes a technical choice

- **Kev:** [Kev 1.0](https://github.com/jaredpalmer/kev/blob/5e42a7a03f28134853dd3ff77461457e921e5ec1/docs/releases/kev-1.0.md) freezes existing checkpoints; it does not introduce new training. The 27B v2 card describes full-weight fine-tuning and weight averaging, so adapter-only deployment advice is wrong for that version. Author-validated long-context quality differs by size; the server's accepted length is not a quality guarantee. E05 stays as historical evidence.
- **Clef / Clef-Flash:** public multimodal typed-decision candidates, with vendor-run results kept separate from independent reproduction. The [hosted Clef interface](https://developers.cloudflare.com/workers-ai/models/clef/) and local encoder use different context settings. Model-level media support does not establish every endpoint's input contract.
- **Strands:** current hobson-v21 is research v21b. [E08](../docs/evidence.md#e08) separates its release seed from the same-host multi-seed comparison; improved mean Brier is not proof of higher accuracy. [E07](../docs/evidence.md#e07) retains the historical v19 question-change probe without attributing it to v21.
- **Perplexity:** the [official card](https://huggingface.co/perplexity-ai/pplx-decider-v1-27b) makes a local deployment candidate inspectable, while its performance table is API-measured. The catalog does not assume local/API equivalence or import an overall leaderboard. Saved temperature and provenance hashes are not the missing training and calibration artifacts.
- **Laya / Jev:** the [Laya limitations](https://github.com/NandhaKishorM/laya/blob/a4a8921afebfd852bba0000475cfb6ab737a124c/README.md#honest-limits) add previously omitted label/negation and action-head cautions. These are documented limitations, not defects newly reproduced here. [Jev's confidence documentation](https://docs.typesafe.ai/confidence) clarifies that distribution statistics are not independent estimates of operational correctness.

## Evidence and checks

All new claims are source review. No model inference, benchmark reproduction, dependency installation, weight download/hash verification, paid API use or exhaustive external-link crawl was performed. Current source bodies and selected links were read; canonical records keep historical source revisions and unknown weight provenance explicit.

The existing source-change list is extended to the new models; the workflow schedule and permissions are unchanged. The repository structure and canonical JSON-to-document workflow are preserved.

Local checks on Python 3.12.14: structural validation, generated-document consistency and local Markdown links; 38 unit tests; 3 disposable-local-remote publishing cases; Python syntax parsing; publishing-script shell syntax; manifest hashes; and whitespace diff checks passed. These checks validate repository consistency, not scientific truth. Live CI status is reported separately with the published commit.

## 中文摘要

本轮补入 Clef／Clef-Flash、Strands Decider 和 Perplexity，修正 Kev 27B v2 的全权重部署、各型号已验证上下文及校准边界。Strands 使用当前 v21，同时保留 v19 历史实验，不把发布种子差值当作配方提升。补全 Laya 标签／否定句与 action.act_probability 限制，以及 Jev confidence 的分布统计含义。所有结果仍是来源核读，不是独立复现；原证据和目录结构保持可追溯。
