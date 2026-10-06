# 2026-10-02 · Clef and Strands Decider source review

[Home](../README.md) · [中文首页](../README.zh-CN.md) · [Model cards](../docs/models.md) · [Evidence ledger](../docs/evidence.md)

This review adds **Clef / Clef-Flash** as one model family and **Strands Decider** as another. It adds source-change endpoints to the existing watcher, without changing its schedule. Existing entries and historical results are retained. This is source review, not model execution or benchmark reproduction.

## Clef / Clef-Flash

Cloudflare's [October 1 announcement](https://blog.cloudflare.com/clef-decision-models/) and pinned [Clef](https://huggingface.co/Cloudflare/clef/blob/2f3de3dd85f379784083b0814d997ab627200f0c/README.md) / [Clef-Flash](https://huggingface.co/Cloudflare/clef-flash/blob/17f0b0ad64efb65d273590632833508766b2aae6/README.md) cards describe multimodal backbones and a joint schema head. The local examples use custom typed-decision helpers. The announcement's 64K context claim is distinct from the local encoder's documented 16,384-token default; neither is an end-to-end application validation.

[E06](../docs/evidence.md#e06) retains a counterexample to universal superiority from the vendor's own comparison: When2Call accuracy is 72.37% for Clef, 65.58% for Clef-Flash and 80.97% for Jev. Exact cohorts, deployment revisions and raw predictions were not audited. Other benchmark metrics and latency boundaries are not combined into a ranking.

## Strands Decider

The [pinned architecture](https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/docs/architecture.md) supplies an inspectable pointer-head baseline. The [exact v19 configuration](https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/configs/experiments/v19.yaml) uses parent-v14 replay on multi-step rows; it should not be simplified to direct 4B-teacher training merely because the general architecture page describes the earlier teacher.

[E07](../docs/evidence.md#e07) preserves four question-change conditions rather than treating the approximately 94% answer-retention summary as accuracy. The probe keeps state and options fixed, changes the instruction, and uses held-out choice tasks. The archived CSV does not establish the historical sample denominator. Confidence-band evidence is primarily short-classification evidence; the source documents drift on other inputs.

The experiment record distinguishes five promotions despite missed preregistered criteria from **v19, which met its own four predictions**. Its seed-only replication was stopped without results. Other AWS retraining results exist. The published v19 adapter and original research v19 are different runs, so historical probe findings are not silently assigned to the downloadable release.

## Selection impact and remaining work

Both are useful candidates for controlled application experiments. This review does not change the requirement to compare against simple baselines, evaluate actual business outcomes, and set risk thresholds on representative calibration data. Text/image judgment, instruction-following and causal improvement from an action remain different questions. Full training-data audits, inference tests, weight verification and independent reproductions remain open.

## 中文摘要

本次新增 Clef／Clef-Flash 一个系列，以及 Strands Decider，并把相关来源接入已有变化检查清单。Clef 保留多模态、联合 schema 判断与定制推理的特点，同时记录 When2Call 上并未胜出的厂商自评结果。Strands 保留 pointer head、LoRA 与训练记录，明确“问题改变而答案不变”的探针含义、置信度跨分布漂移、五次未达预注册标准却晋级的历史，以及尚未完成的 v19 单独种子复测。v19 自身满足了预注册预测；后续 AWS 重训与原始研究检查点不能混为一谈。两者都只是具体应用实验的候选，不构成生产可靠性背书。

## Repository checks completed

Python 3.12.14: generated-document check and structural validator passed; 36 unit tests passed; all 3 local disposable-remote publishing cases passed; publishing-script shell syntax and `git diff --check` passed. These are repository checks, not model inference, public-link certification or benchmark reproduction.
