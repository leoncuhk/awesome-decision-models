# Source register / 来源登记

[Home](../README.md) · [Methodology](methodology.md)

`content_reviewed`: relevant body text inspected, not every linked artifact. `abstract_reviewed`: abstract and publication metadata only. `source_revision`: immutable source-text revision when captured, **not weight provenance**. Unknown fields are not silently filled from memory.

`content_reviewed` 仅表示已检查相关正文，不代表逐个运行所有附件；`abstract_reviewed` 表示摘要与元数据层面的阅读。部分无法打开的模型／数据卡已在相应条目中明确说明。

<a id="jev-launch"></a>
## Introducing System One Models & Jev

- Source: https://typesafe.ai/blog/introducing-system-one-models-and-jev
- Kind: `official_publication`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`

<a id="jev-primitives"></a>
## TypeSafe primitives

- Source: https://docs.typesafe.ai/primitives
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `not captured / live URL`
- Note: Current body reviewed; raw HTML SHA-256 382541e3f343c9e543f3654e1f58bb3e02e893266e684bfc1cc262b19d5184ac. No authenticated previous-body diff: dynamic HTML hash changes do not identify the semantic change. Documentation still defines independent questions, Choice/Score distribution-derived confidence and Noul P(yes) without a separate confidence. Threshold examples are guidance, not validated business calibration or risk bounds.

<a id="jev-confidence"></a>
## TypeSafe confidence semantics

- Source: https://docs.typesafe.ai/confidence
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `not captured / live URL`
- Note: Current body reviewed; raw HTML SHA-256 37a170671fae8d21c2b6fdcd9f07268e37db3934681e448f7c3321900f4b35a7. No authenticated previous-body diff: dynamic HTML hash changes do not identify the semantic change. Documentation still defines independent questions, Choice/Score distribution-derived confidence and Noul P(yes) without a separate confidence. Threshold examples are guidance, not validated business calibration or risk bounds.

<a id="laya-family"></a>
## Laya model family

- Source: https://huggingface.co/convaiinnovations/laya
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`

<a id="laya-specialist"></a>
## Laya Typed-Decisions model card

- Source: https://huggingface.co/convaiinnovations/laya-typed-decisions
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`
- Note: Includes a released-checkpoint calibration warning; the Jev numbers are explicitly an external comparison.

<a id="kev"></a>
## Kev repository

- Source: https://github.com/jaredpalmer/kev/blob/2855ba2a55a80579176a459f78b95d03548cabb5/README.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `2855ba2a55a80579176a459f78b95d03548cabb5`

<a id="kev4b"></a>
## Kev-4B model card

- Source: https://huggingface.co/jaredpalmer/kev-4b
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`

<a id="clm"></a>
## CLM repository

- Source: https://github.com/Contrastive-LM/CLM/blob/bb42c6c5bf914fd449bed2f6ca65be80602cb1f7/README.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `bb42c6c5bf914fd449bed2f6ca65be80602cb1f7`

<a id="clm-base"></a>
## CLM v0.1-8B model card

- Source: https://huggingface.co/Contrastive-LM/CLM-v0.1-8B
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`

<a id="clm-deepswe"></a>
## DeepSWE fixed-split projection head

- Source: https://huggingface.co/Contrastive-LM/deepswe-clm-heads-8k
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`
- Note: Checkpoint and held-out-list SHA-256 values are supplied by the author; binaries were not downloaded or verified here.

<a id="nimble"></a>
## Bespoke Nimble model card

- Source: https://huggingface.co/bespokelabs/Bespoke-Nimble-9B
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`

<a id="nimble-eval"></a>
## Nimble public human-reference benchmark protocol and results

- Source: https://github.com/bespokelabsai/nimble/blob/62076b4f2d365b5879dafcf7f6dd072a1fe76df7/docs/PUBLIC_BENCHMARKS.md
- Kind: `evaluation_report`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `62076b4f2d365b5879dafcf7f6dd072a1fe76df7`
- Note: Project-author-run comparison. Per-run result files are gitignored; protocol/manifests do not amount to a complete public raw-output archive.

<a id="gliner-decide"></a>
## GLiNER2.5-Decide-1B model card

- Source: https://huggingface.co/fastino/GLiNER2.5-Decide-1B
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`
- Note: The 1B card was readable and cross-reports the 340M model. The separate 340M card and fast-decisions dataset card could not be fully inspected in this review.

<a id="gliner-runtime"></a>
## GLiNER2 runtime

- Source: https://github.com/fastino-ai/GLiNER2
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`

<a id="gliclass"></a>
## GLiClass

- Source: https://github.com/Knowledgator/GLiClass
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`

<a id="setfit"></a>
## SetFit

- Source: https://github.com/huggingface/setfit
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`

<a id="qwen-reranker"></a>
## Qwen3-Reranker-0.6B model card

- Source: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`

<a id="outlines"></a>
## Outlines

- Source: https://github.com/dottxt-ai/outlines
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`

<a id="tabicl"></a>
## TabICLv2: A better, faster, scalable, and open tabular foundation model

- Source: https://arxiv.org/abs/2602.11139
- Kind: `paper`; review depth: `abstract_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`
- Note: Version 2 dated 2026-09-16; listed as ICML 2026. Abstract and release metadata reviewed, not an independent benchmark audit.

<a id="routellm"></a>
## RouteLLM

- Source: https://github.com/lm-sys/RouteLLM
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`

<a id="llmrouter"></a>
## LLMRouter

- Source: https://github.com/ulab-uiuc/LLMRouter
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`

<a id="llmrouter-paper"></a>
## LLMRouter: Unified Infrastructure for Developing, Evaluating, and Deploying LLM Routers

- Source: https://arxiv.org/abs/2608.06867
- Kind: `paper`; review depth: `abstract_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`
- Note: 2026-08-07 preprint; do not infer peer review from availability on arXiv.

<a id="vw"></a>
## Vowpal Wabbit contextual bandits tutorial

- Source: https://vowpalwabbit.org/docs/vowpal_wabbit/python/latest/tutorials/python_Contextual_bandits_and_Vowpal_Wabbit.html
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`

<a id="mapie"></a>
## MAPIE

- Source: https://github.com/scikit-learn-contrib/MAPIE
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`

<a id="scoring"></a>
## Strictly Proper Scoring Rules, Prediction, and Estimation

- Source: https://doi.org/10.1198/016214506000001437
- Kind: `paper`; review depth: `abstract_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`
- Note: Gneiting and Raftery, JASA 2007. Publisher/index abstract reviewed.

<a id="calibration"></a>
## On Calibration of Modern Neural Networks

- Source: https://proceedings.mlr.press/v70/guo17a.html
- Kind: `paper`; review depth: `abstract_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`
- Note: Guo et al., ICML 2017. Proceedings abstract/metadata reviewed.

<a id="selective"></a>
## Selective Classification for Deep Neural Networks

- Source: https://arxiv.org/abs/1705.08500v2
- Kind: `paper`; review depth: `abstract_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`
- Note: Geifman and El-Yaniv, 2017. Legacy image-classification setting is not an LLM deployment guarantee.

<a id="defer"></a>
## Consistent Estimators for Learning to Defer to an Expert

- Source: https://proceedings.mlr.press/v119/mozannar20b.html
- Kind: `paper`; review depth: `abstract_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`
- Note: Mozannar and Sontag, ICML 2020.

<a id="crc"></a>
## Conformal Risk Control

- Source: https://arxiv.org/abs/2208.02814v4
- Kind: `paper`; review depth: `abstract_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`
- Note: First submitted 2022; reviewed version v4, 2025. Distinguish original monotonicity assumptions from later generalizations.

<a id="crc-2026"></a>
## Conformal Risk Control for Non-Monotonic Losses

- Source: https://arxiv.org/abs/2602.20151v1
- Kind: `paper`; review depth: `abstract_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`
- Note: 2026-02-23 preprint. Stability-dependent guarantees are not universal per-decision guarantees.

<a id="scoring-review"></a>
## Proper Scoring Rules for Estimation and Forecast Evaluation

- Source: https://doi.org/10.1146/annurev-statistics-042424-050626
- Kind: `paper`; review depth: `abstract_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`
- Note: Waghmare and Ziegel, Annual Review of Statistics and Its Application, 2026 volume; first online 2025. Abstract/index only.

<a id="causal-defer"></a>
## A Causal Target for Learning to Defer Under Hidden Confounding

- Source: https://ojs.aaai.org/index.php/AAAI/article/view/39493
- Kind: `paper`; review depth: `abstract_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`
- Note: AAAI 2026 proceedings abstract. Adjacent research, not a ready-to-deploy router.

<a id="jev-in-the-wild"></a>
## Jev in the Wild: A Data-Driven Analysis of the Jev Model's Functionality, Applications and Ecosystem

- Source: https://arxiv.org/abs/2609.30216
- Kind: `paper`; review depth: `abstract_reviewed`; reviewed: 2026-09-29
- Source revision: `not captured / live URL`
- Note: Jev application ecosystem survey; the abstract was reviewed, but project coding and results were not independently reproduced.

<a id="decision-index"></a>
## Decision Index 0.2 release

- Source: https://huggingface.co/spaces/multimodalart/jev-decision-index/commit/180e621de8bf96962b11a4156b5688d834a47139
- Kind: `evaluation_report`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `180e621de8bf96962b11a4156b5688d834a47139`
- Note: Methodology/release inspected; models and leaderboard were not rerun. Composite index is not raw accuracy.

<a id="independent-bench"></a>
## Decision-model benchmark

- Source: https://github.com/nibzard/decision-model-benchmark
- Kind: `evaluation_report`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`
- Note: Third-party repository/protocol reviewed; this list does not certify every artifact or headline result.

<a id="awesome-system-one"></a>
## Awesome System One

- Source: https://github.com/andyrewlee/awesome-system-one
- Kind: `curated_list`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`

<a id="awesome-jev-zh"></a>
## Awesome Jev 中文

- Source: https://github.com/yzfly/awesome-jev-zh
- Kind: `curated_list`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`

<a id="awesome-routing"></a>
## Awesome LLM Routing and Cascading

- Source: https://github.com/ymoslem/awesome-llm-routing-cascading
- Kind: `curated_list`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`

<a id="awesome-conformal"></a>
## Awesome Conformal Prediction

- Source: https://github.com/valeman/awesome-conformal-prediction
- Kind: `curated_list`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`

<a id="codex-skills"></a>
## OpenAI skill documentation

- Source: https://developers.openai.com/codex/skills/
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`
- Note: Repository-scoped skills do not grant credentials, start schedules, or install themselves into this chat.

<a id="github-schedule"></a>
## GitHub Actions trigger reference

- Source: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`

<a id="gh-clone"></a>
## GitHub CLI: gh repo clone

- Source: https://cli.github.com/manual/gh_repo_clone
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-09-25
- Source revision: `not captured / live URL`

<a id="jevos-repo"></a>
## jevos repository README

- Source: https://github.com/feder-cr/jev/blob/eb74cf78e5377e85fcaa76f6ebc9f82e8b517250/README.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-09-27
- Source revision: `eb74cf78e5377e85fcaa76f6ebc9f82e8b517250`
- Note: Historical README submitted by project author feder-cr in PR #1. Its 0.815 / 2,000 comparison is author-reported, including the Jev 0.927 result; it is not a vendor-certified score or a result for the later v2 weights.

<a id="jevos-release"></a>
## jevos release (jevos-q4_k_m.gguf, jevos-q8_0.gguf)

- Source: https://github.com/feder-cr/jev/releases/tag/jevos
- Kind: `repository`; review depth: `metadata_only`; reviewed: 2026-09-27
- Source revision: `not captured / live URL`
- Note: Historical release URL submitted in PR #1. It returned HTTP 404 at maintainer review on 2026-09-30; the submitted q4 hash 677d126a67d48a6ae965ce80973e7e68c7ab0b13b590a557d8f0cc29a178499f was not independently verified. Preserve this record; see the separate v2 release source.

<a id="jevos-current"></a>
## jevos pinned README and runtime documentation

- Source: https://github.com/feder-cr/jev/tree/9e7d9e8a24e9605bec249045a39df91ff2b58b0d
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-09-30
- Source revision: `9e7d9e8a24e9605bec249045a39df91ff2b58b0d`
- Note: Reviewed README, LICENSE, CLI binary-mode selection, API translation/backend code, engine/engine.py, engine/prompts.py, engine/decisions.py, wiki/small-language-models-explained.md, wiki/measurements.md and wiki/llm-policy-decisions-put-the-rule-in-the-question.md. Documentation describes a 1B model; binary prompt compilation uses instructions and fixed 0/1 answer slots, with logits normalized to P(yes). Base-model provenance, layer count and training recipe were not established. This is source review, not runtime/SDK conformance testing.

<a id="jevos-v2-release"></a>
## jevos-v2 release and asset metadata

- Source: https://github.com/feder-cr/jev/releases/tag/jevos-v2
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-09-30
- Source revision: `not captured / live URL`
- Note: Published 2026-09-29 UTC. Release describes 0.795 on 999 hand-written questions versus 0.757 previously; author-reported, not directly comparable with the old 2,000-question README figure. GitHub API lists jevos-v2-q4_k_m.gguf (619289280 bytes, SHA-256 3cbf010ce06cba932af73346ee683ee98d375dc284c029967eb418472a4993f3) and q8_0. Asset metadata was inspected; binaries were not downloaded or hashed locally.

<a id="awesome-martech-ai"></a>
## Awesome Martech AI guide

- Source: https://github.com/leoncuhk/awesome-martech-ai/blob/d5b63876af2ba6128f4582f2be1c8edf0517dd3d/README.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-09-30
- Source revision: `d5b63876af2ba6128f4582f2be1c8edf0517dd3d`
- Note: Companion maintained by the same repository owner. Reviewed five-layer scope, measurement/evidence standards, applied playbooks and synthetic incrementality-demo limits; navigation inclusion is not independent certification of its linked products.

<a id="clef-launch"></a>
## Cloudflare Clef launch and evaluation report

- Source: https://blog.cloudflare.com/clef-decision-models/
- Kind: `official_publication`; review depth: `content_reviewed`; reviewed: 2026-10-02
- Source revision: `not captured / live URL`
- Note: Published 2026-10-01. Architecture, training description and benchmark table reviewed. Results are vendor-reported; no inference or raw-output audit performed.

<a id="clef-card"></a>
## Clef 27B model card

- Source: https://huggingface.co/Cloudflare/clef/blob/2f3de3dd85f379784083b0814d997ab627200f0c/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-02
- Source revision: `2f3de3dd85f379784083b0814d997ab627200f0c`
- Note: Pinned card describes the joint schema head, Jev/SystemOne wrapper and local encoder default. Repository revision pins reviewed text, not a verified weight hash or the hosted/evaluated deployment.

<a id="clef-flash-card"></a>
## Clef-Flash 9B model card

- Source: https://huggingface.co/Cloudflare/clef-flash/blob/17f0b0ad64efb65d273590632833508766b2aae6/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-02
- Source revision: `17f0b0ad64efb65d273590632833508766b2aae6`
- Note: Pinned card and configuration inspected; inference examples require the custom joint-schema implementation. No model weights downloaded or executed.

<a id="strands-repo"></a>
## Strands Decider repository

- Source: https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/README.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-02
- Source revision: `aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9`
- Note: Reference recipe v19; mechanism and local serving reviewed. Source commit is not an evaluated-weight identifier.

<a id="strands-architecture"></a>
## Strands Decider architecture

- Source: https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/docs/architecture.md
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-02
- Source revision: `aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9`
- Note: Pointer readout, confidence semantics and calibration inspected. For v19 teacher targets, the exact experiment config and results take precedence over the general training description.

<a id="strands-v19-config"></a>
## Strands Decider v19 experiment configuration

- Source: https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/configs/experiments/v19.yaml
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-02
- Source revision: `aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9`
- Note: Inspected configuration: rank-16 LoRA, frozen-torso KL and v14 replay on multi-step rows. The source was read, not executed.

<a id="strands-evaluation"></a>
## Strands Decider evaluation and limitations

- Source: https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/evaluation/README.md
- Kind: `evaluation_report`; review depth: `content_reviewed`; reviewed: 2026-10-02
- Source revision: `aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9`
- Note: Author-reported limitations reviewed, including instruction sensitivity and confidence drift outside short classification.

<a id="strands-probe"></a>
## Strands Decider held-out choice probe results

- Source: https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/research/data/probe_heldout_choice.csv
- Kind: `evaluation_report`; review depth: `content_reviewed`; reviewed: 2026-10-02
- Source revision: `aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9`
- Note: v19 first/last/not/irrelevant rows inspected. These are aggregate CSVs; underlying qsens_hobson-2b-v19.json, per-item predictions and actual sample count were not available in the checkout.

<a id="strands-probe-method"></a>
## Strands Decider question-sensitivity protocol

- Source: https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/evaluation/question_sensitivity.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-02
- Source revision: `aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9`
- Note: Read probe construction and aggregation without executing code. research/scripts/collect.py confirms the CSV uses the held-out choice slice (emotion and massive_intent). Default sampling is not proof of the recorded run denominator.

<a id="strands-research"></a>
## Strands Decider experiment record

- Source: https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/research/README.md
- Kind: `evaluation_report`; review depth: `content_reviewed`; reviewed: 2026-10-02
- Source revision: `aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9`
- Note: Records five promotions despite missed preregistered bars (v13/v14/v16/v17/v18); v19 met its four predictions. Also read v19-seed1 preregistration: stopped at step 1,420 on 2026-09-28, no results taken.

<a id="strands-results"></a>
## Strands Decider original and AWS retrain results

- Source: https://github.com/strands-labs/strands-decider/blob/aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9/evaluation/results.md
- Kind: `evaluation_report`; review depth: `content_reviewed`; reviewed: 2026-10-02
- Source revision: `aa92b075ff297d7bf17c18bf6c676ab4df0fa9a9`
- Note: Original research v19 and AWS retrain are separate runs. No historical probe score is assigned to the published adapter by name alone.

<a id="strands-card"></a>
## Strands Decider published v19 adapter card

- Source: https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v19/blob/bb282d786bc251fd4e3068de3ada9ddbb38127cd/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-02
- Source revision: `bb282d786bc251fd4e3068de3ada9ddbb38127cd`
- Note: Published adapter/head card and LICENSE.md inspected. This release is distinguished from the original research v19 run; no weight bytes were downloaded or independently hashed.

<a id="strands-provenance"></a>
## Strands Decider published adapter provenance

- Source: https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v19/blob/bb282d786bc251fd4e3068de3ada9ddbb38127cd/provenance.json
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-02
- Source revision: `bb282d786bc251fd4e3068de3ada9ddbb38127cd`
- Note: Publisher identifies AWS run v19-p5-run1. Its base revision is explicitly inferred rather than training-time pinned; repository revision and author-supplied provenance are not independently verified weight bytes.

<a id="kev-1-0"></a>
## Kev 1.0 release baseline

- Source: https://github.com/jaredpalmer/kev/blob/5e42a7a03f28134853dd3ff77461457e921e5ec1/docs/releases/kev-1.0.md
- Kind: `official_publication`; review depth: `content_reviewed`; reviewed: 2026-10-06
- Source revision: `5e42a7a03f28134853dd3ff77461457e921e5ec1`
- Note: Released 2026-10-01; explicitly introduces no newly trained checkpoint. Reviewed context validation, calibration, v2 regressions and release provenance; source pin is not a weight hash.

<a id="kev27-v2"></a>
## Kev-27B v2 model card

- Source: https://github.com/jaredpalmer/kev/blob/5e42a7a03f28134853dd3ff77461457e921e5ec1/docs/model-cards/kev-27b.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-06
- Source revision: `5e42a7a03f28134853dd3ff77461457e921e5ec1`
- Note: Relevant source text reviewed; no model execution or weight-byte verification.

<a id="strands-v21-results"></a>
## Strands Decider v21 release and same-host seed results

- Source: https://github.com/strands-labs/strands-decider/blob/3e94e9d84c620ed5a95f1a3310c3decb971e261c/evaluation/results.md
- Kind: `evaluation_report`; review depth: `content_reviewed`; reviewed: 2026-10-06
- Source revision: `3e94e9d84c620ed5a95f1a3310c3decb971e261c`
- Note: v21 release seed, six-seed selection rule and separate same-host v19/v21b comparison inspected. Historical v19 evidence remains separate; no raw-output replay.

<a id="strands-v21-config"></a>
## Strands Decider released v21b recipe

- Source: https://github.com/strands-labs/strands-decider/blob/3e94e9d84c620ed5a95f1a3310c3decb971e261c/configs/experiments/v21b.yaml
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-06
- Source revision: `3e94e9d84c620ed5a95f1a3310c3decb971e261c`
- Note: Relevant source text reviewed; no model execution or weight-byte verification.

<a id="laya-limits"></a>
## Laya documented operational limitations

- Source: https://github.com/NandhaKishorM/laya/blob/a4a8921afebfd852bba0000475cfb6ab737a124c/README.md#honest-limits
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-06
- Source revision: `a4a8921afebfd852bba0000475cfb6ab737a124c`
- Note: Read the current documented label sensitivity, negation examples and unusable act_probability warning. These include previously reported problems, not newly discovered defects or tests run here.

<a id="clef-hosted"></a>
## Clef Workers AI interface and context limit

- Source: https://developers.cloudflare.com/workers-ai/models/clef/
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-06
- Source revision: `not captured / live URL`
- Note: Hosted context is 65,536 tokens; local encode_record default is a separate setting. Interface schema reviewed, not called.

<a id="pplx-card"></a>
## Perplexity pplx-decider-v1-27b model card

- Source: https://huggingface.co/perplexity-ai/pplx-decider-v1-27b
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-06
- Source revision: `not captured / live URL`
- Note: Card, file listing and API evaluation boundary inspected. The card history link identifies commit 5117a6c7fe73b19308dc1a6b0fb529a40c2ecad4, but the immutable body could not be fetched; this record retains the reviewed live URL rather than claiming a verified source pin. Training data and raw calibration/evaluation artifacts were not established.

<a id="pplx-inference"></a>
## Perplexity local inference wrapper

- Source: https://huggingface.co/perplexity-ai/pplx-decider-v1-27b/blob/main/inference.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-06
- Source revision: `not captured / live URL`
- Note: Read only: custom autojev runtime, choice/noul/score and image input, saved-temperature inference. No dependencies installed and no model code executed.

<a id="pplx-config"></a>
## Perplexity released decision configuration

- Source: https://huggingface.co/perplexity-ai/pplx-decider-v1-27b/blob/main/decision_config.json
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-06
- Source revision: `not captured / live URL`
- Note: Saved temperature 2.207568021892729 and author-supplied run/data/code hashes inspected; hashes alone do not supply the underlying training or calibration datasets.

<a id="ms-decision-launch"></a>
## Microsoft-Decision-1 launch, 2026-10-09

- Source: https://commandline.microsoft.com/microsoft-decision-1-model-foundry/
- Kind: `official_publication`; review depth: `content_reviewed`; reviewed: 2026-10-11
- Source revision: `not captured / live URL`
- Note: Launch text reviewed, including the note that Jev comparisons were added. Vendor evaluation, not independent reproduction; charts and raw items not audited.

<a id="ms-decision-docs"></a>
## Microsoft Foundry decision API and limitations

- Source: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-11
- Source revision: `not captured / live URL`
- Note: Public article body read: model version 1, text/JSON request contract, deployment endpoint and known calibration/wording/safety limits. No deployment created.

<a id="openai-decisions"></a>
## OpenAI Decisions public beta guide

- Source: https://developers.openai.com/api/docs/guides/decisions
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-11
- Source revision: `not captured / live URL`
- Note: Guide body, output examples and refusal branches reviewed. Live documentation has no immutable source/serving pin here. No paid API call. Latency headline is not imported as a measured comparison.

<a id="drex-release"></a>
## Drex v1.5 release and public evaluation

- Source: https://github.com/nace-ai/drex-decision-models/blob/5c3d2220713c732a6820c4cdda51c7c38db991f5/models/drex-v1.5/README.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-11
- Source revision: `5c3d2220713c732a6820c4cdda51c7c38db991f5`
- Note: Pinned release page read. Decision Index 0.3.1 is public-only, 37 tests with a 0.9 tie band; distinguish the older 0.2.1 website. Runner parity checks cover two requests only. Hugging Face card/history unavailable in this review; no weight hash established.

<a id="drex-context"></a>
## Drex local context limits

- Source: https://github.com/nace-ai/drex-decision-models/blob/5c3d2220713c732a6820c4cdda51c7c38db991f5/docs/context-length.md
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-11
- Source revision: `5c3d2220713c732a6820c4cdda51c7c38db991f5`
- Note: Default and maximum apply to state plus one question, with runner-specific slot/limit settings; distinct from the hosted API limits.

<a id="drex-license"></a>
## Drex v1.5 modified Open RAIL-M license

- Source: https://github.com/nace-ai/drex-decision-models/blob/5c3d2220713c732a6820c4cdda51c7c38db991f5/models/drex-v1.5/LICENSE
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-11
- Source revision: `5c3d2220713c732a6820c4cdda51c7c38db991f5`
- Note: Weight-license text read; restrictive model terms differ from the repository Apache-2.0 code license. No deployment/legal suitability judgment.

<a id="drex-training"></a>
## Nace Drex training-overlap disclosure

- Source: https://www.nace.ai/drex
- Kind: `official_publication`; review depth: `content_reviewed`; reviewed: 2026-10-11
- Source revision: `not captured / live URL`
- Note: Live FAQ reports official benchmark training splits plus procedural data. Held-out evaluation is task-trained, not wholly unseen-domain zero-shot. Website 0.2.1 results and later pinned repository 0.3.1 results are separate.

<a id="strands-v1-release"></a>
## Strands October 9 v1 releases

- Source: https://github.com/strands-labs/strands-decider/blob/0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534/CHANGELOG.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-11
- Source revision: `0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534`
- Note: Qwen3.5 v1 and four Gemma 4 variants are new recipes/checkpoints; v1 across backbones is not one identical recipe.

<a id="strands-v1-results"></a>
## Strands Qwen3.5 / Gemma 4 v1 results

- Source: https://github.com/strands-labs/strands-decider/blob/0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534/evaluation/results.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-11
- Source revision: `0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534`
- Note: Release soups, seeds, serving/harness differences and training-overlap disclosures read. Qwen v1 builders not yet on main; raw predictions and weights not audited.

<a id="strands-v1-runtime"></a>
## Strands Gemma 4 serving limits and attention fix

- Source: https://github.com/strands-labs/strands-decider/blob/0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534/docs/inference.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-11
- Source revision: `0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534`
- Note: Gemma models are text-only, main-only at this source revision; 4096 training/serving window. E2B CUDA eager-attention fix changes numerical behavior; pre-fix index is not a reliable post-fix baseline.

<a id="strands-v1-vision"></a>
## Strands Qwen v1 missing-image reliability

- Source: https://github.com/strands-labs/strands-decider/blob/0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534/docs/vision.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-11
- Source revision: `0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534`
- Note: Author paired comparison: missing-image POPE confidence/calibration worsens against v21. Source review, not model reproduction.

<a id="strands-v1-data"></a>
## Strands dataset/source inventory

- Source: https://github.com/strands-labs/strands-decider/blob/0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534/data/sources.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-11
- Source revision: `0ac22a97e584f3ccf87cc9b8cc5fdbad57cdf534`
- Note: Inventory separates training, held-out short calibration/evaluation and dev splits; several dataset revisions remain unpinned. License declarations are source claims.

<a id="decision3-d3"></a>
## Decision 3.0 d3 v3.1.0 model card

- Source: https://huggingface.co/vllm-sr/d3/blob/093cffbaa7be6f5dfe14252ae7e80c396c06dbd9/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `093cffbaa7be6f5dfe14252ae7e80c396c06dbd9`
- Note: Card, MODEL_MANIFEST.json, config.json, modeling_d3.py, d3_runtime.py and repository history read at this revision. October 12 commits describe server/runtime/docs changes after the October 11 v3.1.0 release; a repository revision is not a new capability result. Cards declare text/image/video inputs and Apache-2.0. History: https://huggingface.co/vllm-sr/d3/commits/093cffbaa7be6f5dfe14252ae7e80c396c06dbd9.

<a id="decision3-d3-manifest"></a>
## d3 package manifest

- Source: https://huggingface.co/vllm-sr/d3/blob/093cffbaa7be6f5dfe14252ae7e80c396c06dbd9/MODEL_MANIFEST.json
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `093cffbaa7be6f5dfe14252ae7e80c396c06dbd9`
- Note: Author-supplied package model_sha256: 0e439bebbbbf80d9e1b601c56c55a6fc3a6502b4e396cbbb5f3c3f3acc1d607b; built_utc: 2026-10-11T03:30:34+00:00; loaded parameters including readout: 26086635760. Text/vision/readout counts and base revision are declared by the manifest, not independently counted from tensor bytes. Downloaded modeling_d3.py and d3_runtime.py text hashes match the manifest; no weight bytes were downloaded or hashed.

<a id="decision3-d3-flash"></a>
## Decision 3.0 d3-flash v3.1.0 model card

- Source: https://huggingface.co/vllm-sr/d3-flash/blob/f6075bff3c0f7d5704e353d0fb2ebf94888d1691/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `f6075bff3c0f7d5704e353d0fb2ebf94888d1691`
- Note: Card, MODEL_MANIFEST.json, config.json, modeling_d3.py, d3_runtime.py and repository history read at this revision. October 12 commits describe server/runtime/docs changes after the October 11 v3.1.0 release; a repository revision is not a new capability result. Cards declare text/image/video inputs and Apache-2.0. History: https://huggingface.co/vllm-sr/d3-flash/commits/f6075bff3c0f7d5704e353d0fb2ebf94888d1691.

<a id="decision3-d3-flash-manifest"></a>
## d3-flash package manifest

- Source: https://huggingface.co/vllm-sr/d3-flash/blob/f6075bff3c0f7d5704e353d0fb2ebf94888d1691/MODEL_MANIFEST.json
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `f6075bff3c0f7d5704e353d0fb2ebf94888d1691`
- Note: Author-supplied package model_sha256: 74b71d370f3d9e5731c603dafcb8af4e9134fd2c769c89c5169b031a0418799b; built_utc: 2026-10-11T03:28:26+00:00; loaded parameters including readout: 8393739504. Text/vision/readout counts and base revision are declared by the manifest, not independently counted from tensor bytes. Downloaded modeling_d3.py and d3_runtime.py text hashes match the manifest; no weight bytes were downloaded or hashed.

<a id="decision3-d3-mini"></a>
## Decision 3.0 d3-mini v3.1.0 model card

- Source: https://huggingface.co/vllm-sr/d3-mini/blob/0e78bbdbe3cf480ed1461c185c9e0c4fa9258011/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `0e78bbdbe3cf480ed1461c185c9e0c4fa9258011`
- Note: Card, MODEL_MANIFEST.json, config.json, modeling_d3.py, d3_runtime.py and repository history read at this revision. October 12 commits describe server/runtime/docs changes after the October 11 v3.1.0 release; a repository revision is not a new capability result. Cards declare text/image/video inputs and Apache-2.0. History: https://huggingface.co/vllm-sr/d3-mini/commits/0e78bbdbe3cf480ed1461c185c9e0c4fa9258011.

<a id="decision3-d3-mini-manifest"></a>
## d3-mini package manifest

- Source: https://huggingface.co/vllm-sr/d3-mini/blob/0e78bbdbe3cf480ed1461c185c9e0c4fa9258011/MODEL_MANIFEST.json
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `0e78bbdbe3cf480ed1461c185c9e0c4fa9258011`
- Note: Author-supplied package model_sha256: 9ac186bb30b30c129d7aae03d73932600424963bd4644c2041a9d7120f029af5; built_utc: 2026-10-11T03:27:45+00:00; loaded parameters including readout: 4539918336. Text/vision/readout counts and base revision are declared by the manifest, not independently counted from tensor bytes. Downloaded modeling_d3.py and d3_runtime.py text hashes match the manifest; no weight bytes were downloaded or hashed.

<a id="decision3-d3-nano"></a>
## Decision 3.0 d3-nano v3.1.0 model card

- Source: https://huggingface.co/vllm-sr/d3-nano/blob/9d9b937f5f117f78c030ea7ba677c0b3d328ec58/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `9d9b937f5f117f78c030ea7ba677c0b3d328ec58`
- Note: Card, MODEL_MANIFEST.json, config.json, modeling_d3.py, d3_runtime.py and repository history read at this revision. October 12 commits describe server/runtime/docs changes after the October 11 v3.1.0 release; a repository revision is not a new capability result. Cards declare text/image/video inputs and Apache-2.0. History: https://huggingface.co/vllm-sr/d3-nano/commits/9d9b937f5f117f78c030ea7ba677c0b3d328ec58.

<a id="decision3-d3-nano-manifest"></a>
## d3-nano package manifest

- Source: https://huggingface.co/vllm-sr/d3-nano/blob/9d9b937f5f117f78c030ea7ba677c0b3d328ec58/MODEL_MANIFEST.json
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `9d9b937f5f117f78c030ea7ba677c0b3d328ec58`
- Note: Author-supplied package model_sha256: a2a6dce5e40298a43f904dfbffe799e09e675d964df7477683ee2bc9db04cdd8; built_utc: 2026-10-11T04:33:06+00:00; loaded parameters including readout: 2213763904. Text/vision/readout counts and base revision are declared by the manifest, not independently counted from tensor bytes. Downloaded modeling_d3.py and d3_runtime.py text hashes match the manifest; no weight bytes were downloaded or hashed.

<a id="decision3-d3-lite"></a>
## Decision 3.0 d3-lite v3.1.0 model card

- Source: https://huggingface.co/vllm-sr/d3-lite/blob/3c49f5c0bd48a4b28e29b8ec1f38f56e199f3d61/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `3c49f5c0bd48a4b28e29b8ec1f38f56e199f3d61`
- Note: Card, MODEL_MANIFEST.json, config.json, modeling_d3.py, d3_runtime.py and repository history read at this revision. October 12 commits describe server/runtime/docs changes after the October 11 v3.1.0 release; a repository revision is not a new capability result. Cards declare text/image/video inputs and Apache-2.0. History: https://huggingface.co/vllm-sr/d3-lite/commits/3c49f5c0bd48a4b28e29b8ec1f38f56e199f3d61.

<a id="decision3-d3-lite-manifest"></a>
## d3-lite package manifest

- Source: https://huggingface.co/vllm-sr/d3-lite/blob/3c49f5c0bd48a4b28e29b8ec1f38f56e199f3d61/MODEL_MANIFEST.json
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `3c49f5c0bd48a4b28e29b8ec1f38f56e199f3d61`
- Note: Author-supplied package model_sha256: fda5cfc7bc9063fbb7cd40b50fa9a0963d83a4790a3d6a11a356833fd1171992; built_utc: 2026-10-11T03:45:52+00:00; loaded parameters including readout: 853247040. Text/vision/readout counts and base revision are declared by the manifest, not independently counted from tensor bytes. Downloaded modeling_d3.py and d3_runtime.py text hashes match the manifest; no weight bytes were downloaded or hashed.

<a id="decision3-d3-edge"></a>
## Decision 3.0 d3-edge v3.1.0 model card

- Source: https://huggingface.co/vllm-sr/d3-edge/blob/20c745653400d191ecacd99c4eafc0c5900dc15e/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `20c745653400d191ecacd99c4eafc0c5900dc15e`
- Note: Card, MODEL_MANIFEST.json, config.json, modeling_d3.py, d3_runtime.py and repository history read at this revision. October 12 commits describe server/runtime/docs changes after the October 11 v3.1.0 release; a repository revision is not a new capability result. Cards declare text/image/video inputs and Apache-2.0. History: https://huggingface.co/vllm-sr/d3-edge/commits/20c745653400d191ecacd99c4eafc0c5900dc15e.

<a id="decision3-d3-edge-manifest"></a>
## d3-edge package manifest

- Source: https://huggingface.co/vllm-sr/d3-edge/blob/20c745653400d191ecacd99c4eafc0c5900dc15e/MODEL_MANIFEST.json
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `20c745653400d191ecacd99c4eafc0c5900dc15e`
- Note: Author-supplied package model_sha256: 6e00d04abbdbdf6d35c9e12065769d9edaacc3bfe9404583891797718d239dc8; built_utc: 2026-10-11T05:44:01+00:00; loaded parameters including readout: 594582720. Text/vision/readout counts and base revision are declared by the manifest, not independently counted from tensor bytes. Downloaded modeling_d3.py and d3_runtime.py text hashes match the manifest; no weight bytes were downloaded or hashed.

<a id="decision3-config"></a>
## d3 backbone/runtime architecture configuration

- Source: https://huggingface.co/vllm-sr/d3/blob/093cffbaa7be6f5dfe14252ae7e80c396c06dbd9/config.json
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `093cffbaa7be6f5dfe14252ae7e80c396c06dbd9`
- Note: The manifest names Qwen3.8-27B while runtime model_type is qwen3_5. These identify different layers; no contradiction is inferred. max_position_embeddings is configuration, not validated context quality.

<a id="decision3-loader"></a>
## Decision 3.0 Transformers loader

- Source: https://huggingface.co/vllm-sr/d3/blob/093cffbaa7be6f5dfe14252ae7e80c396c06dbd9/modeling_d3.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `093cffbaa7be6f5dfe14252ae7e80c396c06dbd9`
- Note: Custom AutoModel loader delegates to d3_runtime; stock backbone loading without the custom decision path does not establish System One behavior.

<a id="decision3-runtime"></a>
## Decision 3.0 code readout and multimodal runtime

- Source: https://huggingface.co/vllm-sr/d3/blob/093cffbaa7be6f5dfe14252ae7e80c396c06dbd9/d3_runtime.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `093cffbaa7be6f5dfe14252ae7e80c396c06dbd9`
- Note: Independent prompt rows, last-position 255-code readout, per-row masking and softmax; default question batch size 8. Optional reversed-choice permutation averaging is off by default. Read only, never imported or executed.

<a id="decision-index-current"></a>
## Decision Index live 0.3.2 title

- Source: https://multimodalart-jev-decision-index.static.hf.space/index.html
- Kind: `evaluation_report`; review depth: `metadata_only`; reviewed: 2026-10-13
- Source revision: `not captured / live URL`
- Note: Static title says 0.3.2 on review day. The complete dynamic ranking and its evaluated versions were not audited. This source does not support a current first-place claim.

<a id="fluiduse"></a>
## FluidUse native Swift/Core ML runtime

- Source: https://github.com/FluidInference/FluidUse/blob/d278e17df85e39e8c21bb64a467da81c39576fcd/README.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `d278e17df85e39e8c21bb64a467da81c39576fcd`
- Note: Decision-model sections inspected, not unrelated OCR/agent functionality. D3Manager, InternDecisionManager and conversion fidelity described. Native managers and Python-assisted bridges are different deployment paths.

<a id="fluiduse-support"></a>
## FluidUse decision-model support and bridge limits

- Source: https://github.com/FluidInference/FluidUse/blob/d278e17df85e39e8c21bb64a467da81c39576fcd/Documentation/DecisionModelSupport.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `d278e17df85e39e8c21bb64a467da81c39576fcd`
- Note: Support matrix, candidate/context limits, serial queue, timeout/cancellation shutdown and per-model quirks read. Smoke checks are serving-path checks, not common quality scores.

<a id="fluiduse-bench"></a>
## FluidUse official-harness and application-path reports

- Source: https://github.com/FluidInference/FluidUse/blob/d278e17df85e39e8c21bb64a467da81c39576fcd/Documentation/OfficialBenchmarks.md
- Kind: `evaluation_report`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `d278e17df85e39e8c21bb64a467da81c39576fcd`
- Note: Converter-run reports read, especially Verdict raw-logit evaluation versus shipped answer path. The reporter claims reproduction; this repository only reviewed those reports. Raw runs not replayed here.

<a id="decision3-apple"></a>
## Decision 3.0 on Apple Silicon

- Source: https://vllm-sr.ai/blog/decision-3-0-on-apple-silicon/
- Kind: `official_publication`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `not captured / live URL`
- Note: October 11 article by Alex Weng / Fluid Inference, reviewed October 13; acknowledges early access from the model team. Converter/team-associated deployment report, not an independent audit. Live post later mentions flash/Mario; inspected d3-coreml revision lists lite/nano/mini only. Download sizes and runtime names differ from FluidUse README snapshots; verify exact package.

<a id="decision3-coreml"></a>
## Decision 3.0 Core ML conversion packages

- Source: https://huggingface.co/FluidInference/d3-coreml/blob/62b6a996e15342bdd3d608030d8f445f11a52367/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `62b6a996e15342bdd3d608030d8f445f11a52367`
- Note: Pinned card and public file inventory inspected: lite, nano and mini. Conversion package bytes were not downloaded or verified. Video host is Python; do not assume all native Swift paths support every media type.

<a id="webmcp-test"></a>
## Natzir Turrado: Schema Usage / WebMCP application test

- Source: https://natzir.com/posicionamiento-buscadores/modelos-decision-en-webmcp/
- Kind: `evaluation_report`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `not captured / live URL`
- Note: Original evaluator report and technical appendix read. Small rule+model pipeline test; test-selected Nano variant disclosed. Prices and times include specific providers/intermediaries, not official direct vendor baselines. Frozen per-model serving/weight revisions not established.

<a id="jev-ai-about"></a>
## Jev AI independent platform disclosure

- Source: https://jev-ai.pro/about
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `not captured / live URL`
- Note: Platform explicitly says it is independently operated from TypeSafe and self-reports a primary TypeSafe API connection. This verifies its disclosure, not its upstream account or served binary. Do not call jev-ai.pro an official direct TypeSafe endpoint.

<a id="intern-repo"></a>
## Intern-Decision architecture and release scope

- Source: https://github.com/internlm/Intern-Decision/blob/3572c8a68b5df5dafe02d0e093989ba8ec0183bc/README.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `3572c8a68b5df5dafe02d0e093989ba8ec0183bc`
- Note: Qwen3.5 language-backbone decision tuning with frozen vision tower/projector. Code/test records/scorers are public; training data, private calibration/validation records and preparation pipelines are omitted. Do not equate a released training script with the original data recipe.

<a id="intern-evaluation"></a>
## Intern-Decision evaluation protocol

- Source: https://github.com/internlm/Intern-Decision/blob/3572c8a68b5df5dafe02d0e093989ba8ec0183bc/docs/EVALUATION.md
- Kind: `evaluation_report`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `3572c8a68b5df5dafe02d0e093989ba8ec0183bc`
- Note: Exact test record paths/counts, backend-specific temperature presets and hash-binding workflow reviewed; no commands run here.

<a id="intern-calibration"></a>
## Intern-Decision known-distribution calibration pilot

- Source: https://github.com/internlm/Intern-Decision/blob/3572c8a68b5df5dafe02d0e093989ba8ec0183bc/docs/CALIBRATION_BENCHMARK.md
- Kind: `evaluation_report`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `3572c8a68b5df5dafe02d0e093989ba8ec0183bc`
- Note: Exact distribution references separate from model-facing inputs; expected Brier includes irreducible randomness; expected ECE uses 10 equal-width bins. Paired families require grouped uncertainty.

<a id="intern-0.8b"></a>
## Intern-Decision-0.8B model card

- Source: https://huggingface.co/internlm/Intern-Decision-0.8B/blob/85a0cc5a99d67ea8d56dfe98115689212867171d/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `85a0cc5a99d67ea8d56dfe98115689212867171d`
- Note: Card read at fixed revision. Separate size-specific temperatures and image support; training overlap and original private calibration records not independently audited.

<a id="intern-2b"></a>
## Intern-Decision-2B model card

- Source: https://huggingface.co/internlm/Intern-Decision-2B/blob/8797836c65fc91a2435b1fb6850b5f0aabd75cc3/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `8797836c65fc91a2435b1fb6850b5f0aabd75cc3`
- Note: Card read at fixed revision. Separate size-specific temperatures and image support; training overlap and original private calibration records not independently audited.

<a id="intern-4b"></a>
## Intern-Decision-4B model card

- Source: https://huggingface.co/internlm/Intern-Decision-4B/blob/0e5e6aa7d6d750e2b1504ba11a8136cb58aeb3cd/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `0e5e6aa7d6d750e2b1504ba11a8136cb58aeb3cd`
- Note: Card read at fixed revision. Separate size-specific temperatures and image support; training overlap and original private calibration records not independently audited.

<a id="intern-inference"></a>
## Intern-Decision 4B masked-next-token inference

- Source: https://huggingface.co/internlm/Intern-Decision-4B/blob/0e5e6aa7d6d750e2b1504ba11a8136cb58aeb3cd/inference.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `0e5e6aa7d6d750e2b1504ba11a8136cb58aeb3cd`
- Note: Complete causal masked assistant skeleton, pre-placeholder logits, per-field candidate softmax and fixed temperature read; no generate call. Causal schema positions may depend on prior field/option text even without gold/predicted answers. Code was not executed.

<a id="verdict-repo"></a>
## Verdict / OpenJev mechanism and negative findings

- Source: https://github.com/Heman10x-NGU/Verdict-open-jev/blob/30f15564821626ca5c1ad5b2638c4eb7078787dd/README.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `30f15564821626ca5c1ad5b2638c4eb7078787dd`
- Note: ModernBERT/GLiClass bounded candidate model, author calibration/abstention tests and severe synonym/hard-negative failures read. Marketing guarantee language is not accepted as a statistical risk guarantee; unrelated overall-rank claims not imported.

<a id="verdict-engine"></a>
## Verdict typed serving renderer and calibration path

- Source: https://github.com/Heman10x-NGU/Verdict-open-jev/blob/30f15564821626ca5c1ad5b2638c4eb7078787dd/core/engine_encoder.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `30f15564821626ca5c1ad5b2638c4eb7078787dd`
- Note: Serving auto-loads per-K calibrator and templates candidate labels; source reviewed only. Code/evaluation renderer and fitted calibrator are distinct.

<a id="verdict-abstention"></a>
## Verdict raw abstention-generalization report

- Source: https://github.com/Heman10x-NGU/Verdict-open-jev/blob/30f15564821626ca5c1ad5b2638c4eb7078787dd/reports/v2/exp_e5_abstention_generalization.json
- Kind: `evaluation_report`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `30f15564821626ca5c1ad5b2638c4eb7078787dd`
- Note: 200 missing-option cases per condition; preserved baseline and hard/synonym/combined counts. Raw report read, experiment not rerun.

<a id="verdict-card"></a>
## Verdict 151M release model card

- Source: https://huggingface.co/heman10x/rlcd-modernbert-151m/blob/8af2496eb63c7fa66d7d234e1f62629380030eb4/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `8af2496eb63c7fa66d7d234e1f62629380030eb4`
- Note: Card declares Apache-2.0, 25-slot capacity and CE+Brier training. Card prose T=1.0716 differs from the shipped per-K artifact and current evaluation T≈1.4265; do not assign its calibration claims to every serving path.

<a id="verdict-calibrator"></a>
## Verdict shipped per-K calibration artifact

- Source: https://huggingface.co/heman10x/rlcd-modernbert-151m/blob/8af2496eb63c7fa66d7d234e1f62629380030eb4/calibrator.json
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `8af2496eb63c7fa66d7d234e1f62629380030eb4`
- Note: Global T=2.8039; per-K values include K=5 T=3.0560, with K including abstention. Fitting provenance is author supplied; artifact bytes read but weight bytes not verified.

<a id="verdict-coreml"></a>
## Verdict Core ML conversion and rejected quantization

- Source: https://huggingface.co/FluidInference/verdict-coreml/blob/835208c443699f1f95c4bed1b177dc916300cffe/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `835208c443699f1f95c4bed1b177dc916300cffe`
- Note: Converter report: FP16 L128/L512, 24 substantive candidates plus abstention. LUT8 failed its 99/100 agreement gate (96/100, four abstention flips) and is not included as a validated package. Published Index-era identity not authenticated against current release.

<a id="kev-current"></a>
## Kev current serving and source-watch review

- Source: https://github.com/jaredpalmer/kev/blob/85ccf56a0afb952323c621055b02876e8498d60c/README.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `85ccf56a0afb952323c621055b02876e8498d60c`
- Note: October 9 README changes add isolated accelerator probes, explicit device fail-closed behavior and MLX handling; latest October 12 commit changes Modal concurrency. These are runtime/serving changes, not new weight or calibration results. Historical Kev evidence retained.

<a id="clm-current"></a>
## CLM citation-only source-watch review

- Source: https://github.com/Contrastive-LM/CLM/blob/d5f9ef0fd9bde185df0ceaad4f4ecc6cfe8c34f6/README.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `d5f9ef0fd9bde185df0ceaad4f4ecc6cfe8c34f6`
- Note: Compared README at bb42c6c5bf914fd449bed2f6ca65be80602cb1f7 with d5f9ef0fd9bde185df0ceaad4f4ecc6cfe8c34f6: only BibTeX title shortened. No new result, weights or calibration inferred.

<a id="gliner-runtime-current"></a>
## GLiNER2 runtime compatibility review

- Source: https://github.com/fastino-ai/GLiNER2/blob/b86d35c02f2c1a4d9840ea50197bd1b6d13b031e/README.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `b86d35c02f2c1a4d9840ea50197bd1b6d13b031e`
- Note: README/history reviewed: Transformers 5 compatibility/dependency caps and DisentangledFlash packed runtime documentation. Schema-extraction loader support changes interface/compatibility; controlled quality or end-to-end speed gain not established here.

<a id="gliner-decide-current"></a>
## GLiNER2.5-Decide-1B current compatibility metadata

- Source: https://huggingface.co/fastino/GLiNER2.5-Decide-1B/blob/67af949e17bebd20f05fe020a971079889e7a462/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-13
- Source revision: `67af949e17bebd20f05fe020a971079889e7a462`
- Note: Compared Hub trees 688cd7ba8917a0855ad3ce929cba5a9998932e79 → 67af949e17bebd20f05fe020a971079889e7a462: README/config change; model.safetensors LFS oid remains 02c567d791aed26550d300064c7f0c0094fd65291503c65969b45b30786e33b3 (4755208228 bytes), tokenizer blobs unchanged. This is repository metadata comparison, not local weight-byte hash verification or a retrain/performance claim.

<a id="decision3-d3-oct15"></a>
## d3 October 15 card and identity review

- Source: https://huggingface.co/vllm-sr/d3/blob/225be8b1e2270becab69c5fe05b26f99cbbdd66b/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-15
- Source revision: `225be8b1e2270becab69c5fe05b26f99cbbdd66b`
- Note: Compared 093cffbaa7be6f5dfe14252ae7e80c396c06dbd9 to 225be8b1e2270becab69c5fe05b26f99cbbdd66b: all 12 safetensors weight/readout Git/LFS identities, decision_config.json blob and manifest identity unchanged; temperature remains 1.0. Changed root blobs: README, MODEL_MANIFEST, d3_runtime and .gitattributes; assets subtree also changes. History describes Index/serving documentation, loading checks and hosted-demo links; d3 additionally documents native vLLM. Manifest SHA-256 4959df7ee964c2fad24a8e853df8e3cda9bae61636fa5650cc1a0fed78539677; author package identity 0e439bebbbbf80d9e1b601c56c55a6fc3a6502b4e396cbbb5f3c3f3acc1d607b. Metadata/source inspection, not local weight-byte verification. The detailed runtime diff was inspected for d3.

<a id="decision3-d3-flash-oct15"></a>
## d3-flash October 15 card and identity review

- Source: https://huggingface.co/vllm-sr/d3-flash/blob/8b35c853b90e777595ec36bacae820fe08ea077a/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-15
- Source revision: `8b35c853b90e777595ec36bacae820fe08ea077a`
- Note: Compared f6075bff3c0f7d5704e353d0fb2ebf94888d1691 to 8b35c853b90e777595ec36bacae820fe08ea077a: all 5 safetensors weight/readout Git/LFS identities, decision_config.json blob and manifest identity unchanged; temperature remains 1.0. Changed root blobs: README, MODEL_MANIFEST, d3_runtime and .gitattributes; assets subtree also changes. History describes Index/serving documentation, loading checks and hosted-demo links; d3 additionally documents native vLLM. Manifest SHA-256 abdafb9f4a3e39595a54b7ca977e6bd7a3279c57745231319e3a171a43976e65; author package identity 74b71d370f3d9e5731c603dafcb8af4e9134fd2c769c89c5169b031a0418799b. Metadata/source inspection, not local weight-byte verification. The detailed runtime diff was inspected for d3.

<a id="decision3-d3-mini-oct15"></a>
## d3-mini October 15 card and identity review

- Source: https://huggingface.co/vllm-sr/d3-mini/blob/97dd054df4b3e0b3beb6af23ab8c82b7c0052e0e/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-15
- Source revision: `97dd054df4b3e0b3beb6af23ab8c82b7c0052e0e`
- Note: Compared 0e78bbdbe3cf480ed1461c185c9e0c4fa9258011 to 97dd054df4b3e0b3beb6af23ab8c82b7c0052e0e: all 3 safetensors weight/readout Git/LFS identities, decision_config.json blob and manifest identity unchanged; temperature remains 1.0. Changed root blobs: README, MODEL_MANIFEST, d3_runtime and .gitattributes; assets subtree also changes. History describes Index/serving documentation, loading checks and hosted-demo links; d3 additionally documents native vLLM. Manifest SHA-256 bc638e17982411f6ad0f524d33d0dc1f0db81ad7995c1bfdf93dba7674df5e48; author package identity 9ac186bb30b30c129d7aae03d73932600424963bd4644c2041a9d7120f029af5. Metadata/source inspection, not local weight-byte verification. The detailed runtime diff was inspected for d3.

<a id="decision3-d3-nano-oct15"></a>
## d3-nano October 15 card and identity review

- Source: https://huggingface.co/vllm-sr/d3-nano/blob/aeb70d4dd53ed25b855c3b0a66394b8fe265db7f/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-15
- Source revision: `aeb70d4dd53ed25b855c3b0a66394b8fe265db7f`
- Note: Compared 9d9b937f5f117f78c030ea7ba677c0b3d328ec58 to aeb70d4dd53ed25b855c3b0a66394b8fe265db7f: all 2 safetensors weight/readout Git/LFS identities, decision_config.json blob and manifest identity unchanged; temperature remains 1.0. Changed root blobs: README, MODEL_MANIFEST, d3_runtime and .gitattributes; assets subtree also changes. History describes Index/serving documentation, loading checks and hosted-demo links; d3 additionally documents native vLLM. Manifest SHA-256 db2139c5b5b7060f8f95150ec70ca2fe7e69e6bf4249e5766df5388bf35977f2; author package identity a2a6dce5e40298a43f904dfbffe799e09e675d964df7477683ee2bc9db04cdd8. Metadata/source inspection, not local weight-byte verification. The detailed runtime diff was inspected for d3.

<a id="decision3-d3-lite-oct15"></a>
## d3-lite October 15 card and identity review

- Source: https://huggingface.co/vllm-sr/d3-lite/blob/9c10703193afc7c7d28c88201c0364bfbbf58320/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-15
- Source revision: `9c10703193afc7c7d28c88201c0364bfbbf58320`
- Note: Compared 3c49f5c0bd48a4b28e29b8ec1f38f56e199f3d61 to 9c10703193afc7c7d28c88201c0364bfbbf58320: all 2 safetensors weight/readout Git/LFS identities, decision_config.json blob and manifest identity unchanged; temperature remains 1.0. Changed root blobs: README, MODEL_MANIFEST, d3_runtime and .gitattributes; assets subtree also changes. History describes Index/serving documentation, loading checks and hosted-demo links; d3 additionally documents native vLLM. Manifest SHA-256 31f0ff94ff26619c0a063ccac803edcfe34c56c92e5c9c50b703b62893f125dd; author package identity fda5cfc7bc9063fbb7cd40b50fa9a0963d83a4790a3d6a11a356833fd1171992. Metadata/source inspection, not local weight-byte verification. The detailed runtime diff was inspected for d3.

<a id="decision3-d3-edge-oct15"></a>
## d3-edge October 15 card and identity review

- Source: https://huggingface.co/vllm-sr/d3-edge/blob/cab71e6ad3461b8086d51ddb572c656babd63b0b/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-15
- Source revision: `cab71e6ad3461b8086d51ddb572c656babd63b0b`
- Note: Compared 20c745653400d191ecacd99c4eafc0c5900dc15e to cab71e6ad3461b8086d51ddb572c656babd63b0b: all 2 safetensors weight/readout Git/LFS identities, decision_config.json blob and manifest identity unchanged; temperature remains 1.0. Changed root blobs: README, MODEL_MANIFEST, d3_runtime and .gitattributes; assets subtree also changes. History describes Index/serving documentation, loading checks and hosted-demo links; d3 additionally documents native vLLM. Manifest SHA-256 3bae8989a6feb36a66bf4d8c44112dc63199d0dc69f564dc895fe368b1e08e59; author package identity 6e00d04abbdbdf6d35c9e12065769d9edaacc3bfe9404583891797718d239dc8. Metadata/source inspection, not local weight-byte verification. The detailed runtime diff was inspected for d3.

<a id="decision3-runtime-oct15"></a>
## d3 package-verification scope update

- Source: https://huggingface.co/vllm-sr/d3/blob/225be8b1e2270becab69c5fe05b26f99cbbdd66b/d3_runtime.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-15
- Source revision: `225be8b1e2270becab69c5fe05b26f99cbbdd66b`
- Note: Diff against October 12 runtime read: fast/full check runtime-loaded files, excluding Markdown/assets/license/packaging; release additionally hashes all listed files and reports unlisted non-hidden files. Loading integrity policy change, not a retrain or temperature fit. Downloaded text SHA-256 2d90e93ac06b9ca4a84e0610ab9acfa2d6793ea4b40eec1b4a3da47577bdea37. No fetched code executed.

<a id="vllm-d3-pr"></a>
## Native vLLM Decision 3.0 integration and author tests

- Source: https://github.com/vllm-project/vllm/pull/61565
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-15
- Source revision: `89cab550862e4b7f08d70c19682121362d7dd0c5`
- Note: Merged 2026-10-14T17:10:56Z as 89cab550862e4b7f08d70c19682121362d7dd0c5. PR body SHA-256 0ae4020db2a05e5caa67309f962810bed64cb36b9f67c49b740080acf75f12a5. Author tests d3/mini/edge on MI325X; flash/nano/lite, CUDA, tensor parallelism and LoRA unmeasured. Latest official release rechecked after reconnect: v0.31.0 (Oct 5), predating the merge. Card separately reports an Oct 15 MI300X nightly check. No model execution here.

<a id="vllm-d3-docs"></a>
## vLLM structured decisions at the D3 merge

- Source: https://github.com/vllm-project/vllm/blob/89cab550862e4b7f08d70c19682121362d7dd0c5/docs/models/structured_decisions_models.md
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-15
- Source revision: `89cab550862e4b7f08d70c19682121362d7dd0c5`
- Note: Pinned D3 section and generic endpoint distinctions read alongside the latest official docs. D3 is a custom classify/pooling code-readout model, not ordinary chat generation. Noncausal full attention disables prefix caching/chunked prefill. Generic label-reading descriptions do not all apply to D3.

<a id="vllm-d3-code"></a>
## vLLM D3 classification model implementation

- Source: https://github.com/vllm-project/vllm/blob/89cab550862e4b7f08d70c19682121362d7dd0c5/vllm/model_executor/models/d3.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-15
- Source revision: `89cab550862e4b7f08d70c19682121362d7dd0c5`
- Note: Model source and relevant config/strategy patches read: detect decision_config.json, load readout.safetensors as FP32 score head, one classify read per question. Shared media features do not imply one shared noncausal text encoding. Read only.

<a id="decision-index-text-oct15"></a>
## Decision Index 0.3.2 text aggregate snapshot

- Source: https://multimodalart-jev-decision-index.static.hf.space/data/v03.json
- Kind: `evaluation_report`; review depth: `content_reviewed`; reviewed: 2026-10-15
- Source revision: `not captured / live URL`
- Note: Generated 2026-10-14T09:16:12Z, retrieved/rechecked Oct 15; SHA-256 e51e388fd9f7be8d82662bc349c1971147ffc64be2072568aca96820941b4133. 166 entries versus the card's older 149 count. Formula: public/same-skills/new-domains 0.2/0.5/0.3, private-scale equating and 0.9-point tie band. d3 66.26 and linne-oak 65.61 share rank_tie=1. Published aggregates inspected; hidden items/raw runs not audited.

<a id="decision-index-vision-oct15"></a>
## Decision Index 0.3.2 vision aggregate snapshot

- Source: https://multimodalart-jev-decision-index.static.hf.space/data/vision.json
- Kind: `evaluation_report`; review depth: `content_reviewed`; reviewed: 2026-10-15
- Source revision: `not captured / live URL`
- Note: Generated 2026-10-14T09:16:14Z, retrieved/rechecked Oct 15; SHA-256 66c74cfaa91f899cafc0fe2b639feca7febd611d9c7f5da42435fafc2e0a36f6. 34 entrants versus the card's older 33 count. Public/private equally weighted. d3 full/public/private 71.26/74.08/68.45. Published aggregates only; hidden items, uncertainty and raw runs not independently audited.

<a id="decision-index-scoring-oct15"></a>
## Decision Index 0.3.2 scoring-change description

- Source: https://multimodalart-jev-decision-index.static.hf.space/index.html
- Kind: `evaluation_report`; review depth: `content_reviewed`; reviewed: 2026-10-15
- Source revision: `not captured / live URL`
- Note: HTML/JavaScript read without execution; SHA-256 3da5b93fcf055c01566ef4553cb24c06a03217960e245f0a055ac33140a8f649. Changelog says GPQA/MMLU-Pro/BBH same-skill sets had been omitted for 37 models; scoring was corrected, GSM8K rebuilt and ForecastBench retired. JSON endpoints identified from page source. This extends the Oct 13 title-only inspection; score revisions do not establish retraining.

<a id="financial-documents"></a>
## Stefan Jansen: Testing Jev on Financial Documents

- Source: https://insights.ml4trading.io/p/testing-jev-on-financial-documents
- Kind: `evaluation_report`; review depth: `content_reviewed`; reviewed: 2026-10-15
- Source revision: `not captured / live URL`
- Note: Published Oct 13; body and methods appendix reviewed Oct 15; HTML SHA-256 c81fd362a36c238a5d99882f529f587ced4fc6af30678b7e8930d63d7046c0db. Original evaluator outside model team, with TypeSafe-provided API access for an unpaid evaluation and a vendor-suggested post-hoc prompt. Runs attributed to jev-1.13.0 (Sep 21–Oct 7) from experiment record and sampled recheck; original compact files lack version fields. Complete frozen code/prediction archive not audited. Label construction, population selection and split limitations retained.

<a id="semantic-feature-cookbook"></a>
## TypeSafe autoresearch semantic features with CatBoost

- Source: https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-15
- Source revision: `not captured / live URL`
- Note: Full code/output and Markdown read; Markdown SHA-256 24e0854e5a5846c269142d2a57abfb8aa90d63c37231b03036ed08f1e9989b72. Cached run dated 2026-08-03: jev-1.12 plus claude-sonnet-5; alternate proposer branch not run. 2000 wine notes, 1200 development / 800 test, five rounds; 38 questions become 67 columns. Source describes cache replay, but notebook/cache/API not executed here. Critic-score reconstruction, not financial or visual-intent evidence.

<a id="trl-sft-guide"></a>
## TRL SFT: generic VLM/PEFT support boundaries

- Source: https://huggingface.co/docs/trl/en/sft_trainer
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-15
- Source revision: `not captured / live URL`
- Note: Relevant VLM/PEFT dataset-format sections reviewed; live HTML SHA-256 2f26af56edf5f6e5e8038221679f1bdd04251d49d0cecfadb0c38f15d495b68c. Generic trainer documentation for supported models, not a demonstrated D3 noncausal readout training/export or serving-LoRA recipe. No training, dependency installation or image upload performed.

<a id="mire-challenge"></a>
## MIRE: official multimodal scene and dialogue-intent challenge

- Source: https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/README.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-16
- Source revision: `d101287af90d114c5bf0cbfbd56fe9c52358e3bb`
- Note: README, task/data description and evaluation script inspected. Screenshot scene classification and multi-turn intent recognition are separate tasks; public baseline is not a typed decision readout. Dataset distribution/usage terms need their own review; no dataset downloaded or model run.

<a id="mire-full-sft"></a>
## MIRE: Qwen2-VL-7B full-SFT baseline configuration

- Source: https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/mire_baseline/configs/qwen2_vl_full_sft.yaml
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-16
- Source revision: `d101287af90d114c5bf0cbfbd56fe9c52358e3bb`
- Note: Configuration explicitly sets finetuning_type: full, qwen2_vl template and 0.1 validation fraction. This establishes the baseline configuration, not reproducibility of competition scores or a LoRA recipe.

<a id="ecommir-paper"></a>
## EcomMIR: multimodal intent recognition competition solution

- Source: https://zhoushengisnoob.github.io/papers/WWWComp.pdf
- Kind: `paper`; review depth: `content_reviewed`; reviewed: 2026-10-16
- Source revision: `not captured / live URL`
- Note: Four-page author-hosted WWW Companion 2025 paper read, including sections 2–3 and Tables 1–3; DOI 10.1145/3701716.3718371. PDF SHA-256 3918aa06dd0b8592eaba7a9b5046fba111b0e2b86fa4bfbe1629102dba478b57. CN-CLIP scene model and MiniCPM-V 2.6 LoRA intent model use multiple data/model interventions, including Round 1 pseudo-labels. Tables are author reports; exact scored example IDs, full outputs and independent replay not established here. No image/data/model execution.

<a id="ezjev-training"></a>
## ezjev: text candidate-logit LoRA training and replay

- Source: https://github.com/everettjf/ezjev/tree/8b3d88957c0795bea160c8fbc9c6d2a54b051136
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-16
- Source revision: `8b3d88957c0795bea160c8fbc9c6d2a54b051136`
- Note: README and parts/train.py/parts/loop.py inspected. Per-question text tokenization, candidate lm_head row projection, candidate CE+Brier, replay and development NLL temperature search. Training inputs are input_ids/attention_mask; no image processor/pixel tensors. Multimodal class detection is not image fine-tuning. Historical job spending is not a current cost estimate; MIT code does not cover data/weights. No code executed.

<a id="ezjev-s3-card"></a>
## ezjev-4b-s3: lineage, calibration and training-data license warning

- Source: https://huggingface.co/everettjf/ezjev-4b-s3/blob/a2faa581dc5e48c0c41ce388d056fed8e8fa6b4d/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-16
- Source revision: `a2faa581dc5e48c0c41ce388d056fed8e8fa6b4d`
- Note: Card reviewed for LoRA/merged lineage, replay, development-set temperature and explicit non-commercial/unstated training-data license warning. Source revision pins the card, not locally hashed weights; JevBench self-test not reproduced and no new score imported.

<a id="intern-training"></a>
## Intern-Decision: multimodal full-language training configuration

- Source: https://github.com/InternLM/Intern-Decision/blob/3572c8a68b5df5dafe02d0e093989ba8ec0183bc/configs/training/qwen35.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-16
- Source revision: `3572c8a68b5df5dafe02d0e093989ba8ec0183bc`
- Note: Configuration and src/model/qwen.py reviewed: freeze_vision=True, freeze_projector=True, freeze_language=False, standard XTuner CELossConfig; real pixel_values/image_grid_thw flow through frozen visual features. Existing configuration trains the language backbone, not a LoRA adapter. Dependency-level CE execution not rerun; private original training/calibration data prevent complete replay.

<a id="intern-training-inputs"></a>
## Intern-Decision: masked labels and causal placeholder input compilation

- Source: https://github.com/InternLM/Intern-Decision/blob/3572c8a68b5df5dafe02d0e093989ba8ec0183bc/src/inputs/schema.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-16
- Source revision: `3572c8a68b5df5dafe02d0e093989ba8ec0183bc`
- Note: src/inputs/schema.py, masked.py, dataset.py and inference/hf_backend.py reviewed. Assistant skeleton contains placeholders; target answer symbols are separately placed in labels, then aligned for next-token CE. Multimodal tokenizer carries pixels/grid. Later causal fields see prior placeholders, not completed gold/predicted answers; no automatic consistency or field independence claim. Length/marker checks inspected, not executed.

<a id="d3-training-boundary"></a>
## Decision 3.0: inference-only wrapper training boundary

- Source: https://huggingface.co/vllm-sr/d3/blob/225be8b1e2270becab69c5fe05b26f99cbbdd66b/modeling_d3.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-16
- Source revision: `225be8b1e2270becab69c5fe05b26f99cbbdd66b`
- Note: Inspected wrapper train(True) explicitly raises inference-only RuntimeError; save_pretrained is unsupported. Custom readout/noncausal inference should not be treated as a generic Trainer/PEFT training recipe. This source finding does not establish absence of unpublished or separately engineered training paths; no remote model code executed.

<a id="pacman-training"></a>
## decision-pacman: textual-state decision distillation and generality trade-off

- Source: https://github.com/grapeot/decision-pacman/tree/593ed1f59f4f97ad0bda7287ff304e9667360089
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-16
- Source revision: `593ed1f59f4f97ad0bda7287ff304e9667360089`
- Note: README and training/train.py reviewed. Chat-template text states, language-side LoRA and option-letter soft-target CE; no image tensors in inspected trainer. Teacher-only lookahead used for labeling is excluded from student evaluation inputs. Author reports task gains with worse generic JevBench performance; complete generated training data and all evaluated artifacts not audited here. No game/model run and no score imported as independent evidence.

<a id="startlux-paper"></a>
## StartLux-Decision: AutoThink and RLCD² technical report v1

- Source: https://arxiv.org/html/2610.17309v1
- Kind: `paper`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `not captured / live URL`
- Note: arXiv v1 submitted 2026-10-12. Relevant full-text sections 2–6, Tables 2/4 and Appendices A/B/D reviewed. Paper describes three-stage training, frozen probability scorer, proper-score/length reward and policy-aware calibration. DI public is development-selected and contributes 20% of the full board; private 80% unevaluated. DecisionPivot is author-built/evaluated despite claimed exclusion from model selection. HTML SHA-256 2c8109f3f0d4bca33bc9bc742b7e674941261f36f01ce16c226e86d659bebcae. No training, inference or independent reproduction.

<a id="startlux-repo"></a>
## StartLux v1.1: family and inference-package release

- Source: https://github.com/StartLuxLabs/StartLux-Decision/blob/cb1d11f1ac9e9b43b95ef3a6468fa29b607c40fd/README.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `cb1d11f1ac9e9b43b95ef3a6468fa29b607c40fd`
- Note: README/repository tree and Apache-2.0 LICENSE reviewed. Five Instant sizes and three AutoThink sizes, with separate v1 archive and quantized formats. Public package is inference/server code; archived v1 LoRA does not establish the complete v1.1/RLCD² training pipeline. Published gate 0.9, runtime default 0.6; engine reruns are not the paper release run. No external code executed.

<a id="startlux-api"></a>
## StartLux API: gates, confidence and none_probability

- Source: https://github.com/StartLuxLabs/StartLux-Decision/blob/cb1d11f1ac9e9b43b95ef3a6468fa29b607c40fd/docs/api.md
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `cb1d11f1ac9e9b43b95ef3a6468fa29b607c40fd`
- Note: Request/response, per-question processing, maximum-probability gate, transformed confidence and none/renormalization semantics reviewed. none_probability is documented as an alarm score, not calibrated absence probability. Current defaults must not inherit paper metrics; threshold 0.2 is an author diagnostic, not a deployment risk guarantee.

<a id="startlux-pipeline"></a>
## StartLux inference: separate question rows and adaptive readout

- Source: https://github.com/StartLuxLabs/StartLux-Decision/blob/cb1d11f1ac9e9b43b95ef3a6468fa29b607c40fd/startlux_decide/pipeline.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `cb1d11f1ac9e9b43b95ef3a6468fa29b607c40fd`
- Note: pipeline.py, readout.py, prompt.py, controls.py and modelcfg.py inspected. Existing LM option-letter projection, max(P) gate, 25/75 mixture, 26-code limit and group/final tournament, loop detection and default last-4000-character post-thought tail. Causal prefix reuse is a runtime optimization; it is not one joint backbone row for every question. No package imported or executed.

<a id="startlux-engines"></a>
## StartLux serving: backend, context and media boundaries

- Source: https://github.com/StartLuxLabs/StartLux-Decision/blob/cb1d11f1ac9e9b43b95ef3a6468fa29b607c40fd/docs/engines.md
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `cb1d11f1ac9e9b43b95ef3a6468fa29b607c40fd`
- Note: Engine settings and docs/benchmarks.md reviewed. vLLM 0.19.1 release runs differ from 0.31 single-readout speed checks; complete AutoThink includes thought and second readout. Launcher 0.31 enables up to 8 images, video=0; 0.19.1 is text-only. Instant default whole-prefill cap 131072 after author-reported long-prefill crashes; causal context config 262144. These are engineering limits, not full-context quality validation.

<a id="startlux-v1-training"></a>
## StartLux archived v1: text LoRA example is not v1.1 RLCD² training

- Source: https://github.com/StartLuxLabs/StartLux-Decision/blob/cb1d11f1ac9e9b43b95ef3a6468fa29b607c40fd/v1/finetune/finetune_lora.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `cb1d11f1ac9e9b43b95ef3a6468fa29b607c40fd`
- Note: Archived trainer and v1/docs/finetuning.md read. AutoTokenizer/text rows, selected LM-head letter projection and language linear-layer LoRA are inspectable. This is an earlier text adaptation example, not the released v1.1 three-stage training/data/RLCD² package or verified image fine-tuning. Author generic sample-size/speed advice not adopted as a measured recommendation.

<a id="startlux-site"></a>
## StartLux author release article

- Source: https://decision.startlux.com/
- Kind: `official_publication`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `not captured / live URL`
- Note: Release body reviewed as author interpretation; live HTML SHA-256 bf65d3c8d5f141d429e88db8d74b6164a6b5eac63d7747ffcdcb1008c053bcbb. Accuracy, development benchmark selection and latency claims checked against fixed paper/code/cards. Readout-only latency excludes reasoning-generation cost. Promotional superiority statements not adopted as independent or full-board rankings.

<a id="startlux-27b-autothink"></a>
## startlux-models/StartLux-Decision-v1.1-27B-AutoThink model card

- Source: https://huggingface.co/startlux-models/StartLux-Decision-v1.1-27B-AutoThink/blob/dd62d5cd84a483d75bdd548880bbf08bdd3f67a4/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `dd62d5cd84a483d75bdd548880bbf08bdd3f67a4`
- Note: Card and model metadata inspected; source revision pins text/repository identity, not locally hashed weight bytes. Nominal size and CC BY-NC 4.0 declared. Quantized ports are deployment variants, not new families; no weights downloaded or model run. config.json and decision_config.json also inspected: Qwen3_5ForConditionalGeneration runtime, A–Z IDs, per-type temperatures and 26-code/group-reduction settings. Exact base provenance not inferred from class name.

<a id="startlux-0p8b-instant"></a>
## startlux-models/StartLux-Decision-v1.1-0.8B-Instant model card

- Source: https://huggingface.co/startlux-models/StartLux-Decision-v1.1-0.8B-Instant/blob/6496ae641cc71b149ce9dad69bd97f2a44e7bf11/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `6496ae641cc71b149ce9dad69bd97f2a44e7bf11`
- Note: Card and model metadata inspected; source revision pins text/repository identity, not locally hashed weight bytes. Nominal size and CC BY-NC 4.0 declared. Quantized ports are deployment variants, not new families; no weights downloaded or model run.

<a id="startlux-2b-instant"></a>
## startlux-models/StartLux-Decision-v1.1-2B-Instant model card

- Source: https://huggingface.co/startlux-models/StartLux-Decision-v1.1-2B-Instant/blob/f1e6cd147dda82c9ffa3e8e725d5c1f175566fb1/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `f1e6cd147dda82c9ffa3e8e725d5c1f175566fb1`
- Note: Card and model metadata inspected; source revision pins text/repository identity, not locally hashed weight bytes. Nominal size and CC BY-NC 4.0 declared. Quantized ports are deployment variants, not new families; no weights downloaded or model run.

<a id="startlux-4b-instant"></a>
## startlux-models/StartLux-Decision-v1.1-4B-Instant model card

- Source: https://huggingface.co/startlux-models/StartLux-Decision-v1.1-4B-Instant/blob/416088f77cfce09633906a3675c7cd2e5dabcf10/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `416088f77cfce09633906a3675c7cd2e5dabcf10`
- Note: Card and model metadata inspected; source revision pins text/repository identity, not locally hashed weight bytes. Nominal size and CC BY-NC 4.0 declared. Quantized ports are deployment variants, not new families; no weights downloaded or model run.

<a id="startlux-9b-instant"></a>
## startlux-models/StartLux-Decision-v1.1-9B-Instant model card

- Source: https://huggingface.co/startlux-models/StartLux-Decision-v1.1-9B-Instant/blob/18a17f734966b213b2f00fa9c915e8b9af2a9b20/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `18a17f734966b213b2f00fa9c915e8b9af2a9b20`
- Note: Card and model metadata inspected; source revision pins text/repository identity, not locally hashed weight bytes. Nominal size and CC BY-NC 4.0 declared. Quantized ports are deployment variants, not new families; no weights downloaded or model run.

<a id="startlux-27b-instant"></a>
## startlux-models/StartLux-Decision-v1.1-27B-Instant model card

- Source: https://huggingface.co/startlux-models/StartLux-Decision-v1.1-27B-Instant/blob/32e7d35d74db615c4a059181efbf21c5421f3561/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `32e7d35d74db615c4a059181efbf21c5421f3561`
- Note: Card and model metadata inspected; source revision pins text/repository identity, not locally hashed weight bytes. Nominal size and CC BY-NC 4.0 declared. Quantized ports are deployment variants, not new families; no weights downloaded or model run.

<a id="startlux-4b-autothink"></a>
## startlux-models/StartLux-Decision-v1.1-4B-AutoThink model card

- Source: https://huggingface.co/startlux-models/StartLux-Decision-v1.1-4B-AutoThink/blob/23dd4c513ef387705bb13fd8caadc2d5c863082f/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `23dd4c513ef387705bb13fd8caadc2d5c863082f`
- Note: Card and model metadata inspected; source revision pins text/repository identity, not locally hashed weight bytes. Nominal size and CC BY-NC 4.0 declared. Quantized ports are deployment variants, not new families; no weights downloaded or model run.

<a id="startlux-9b-autothink"></a>
## startlux-models/StartLux-Decision-v1.1-9B-AutoThink model card

- Source: https://huggingface.co/startlux-models/StartLux-Decision-v1.1-9B-AutoThink/blob/efc649d8493b5b7353cf2ed6da0cdcbc215958ef/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `efc649d8493b5b7353cf2ed6da0cdcbc215958ef`
- Note: Card and model metadata inspected; source revision pins text/repository identity, not locally hashed weight bytes. Nominal size and CC BY-NC 4.0 declared. Quantized ports are deployment variants, not new families; no weights downloaded or model run.

<a id="decisionpivot-data"></a>
## DecisionPivot v1.1: fixed dataset card, scorer and table identities

- Source: https://huggingface.co/datasets/startlux-models/DecisionPivot/blob/b6a65d303f3f8689d293869aff3db41f944984c6/README.md
- Kind: `evaluation_report`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `b6a65d303f3f8689d293869aff3db41f944984c6`
- Note: README, CHANGES, EXPOSURE, score.py and committed headline CSVs inspected. v1.1 corrected 10/13 core generators on Oct8; Oct14 rename from DecideBench changes no items. 7800 core examples, grouped pair accuracy distinct from 34104 reused-reference items and seven-layer scores. auto_at_5/auto_at_1 are benchmark hindsight risk-coverage diagnostics, not pre-certified deployment thresholds. Pinned headline tables include intermediate research systems and do not numerically match the paper release table; old hosted Jev core runs were not carried into corrected v1.1. No silent mapping of those runs to final checkpoints; no independent scoring replay. Core CC BY 4.0, reference source terms separate, code Apache-2.0.

<a id="decisionpivot-generators"></a>
## DecisionPivot: public generators, independent solvers and audit code

- Source: https://github.com/StartLuxLabs/DecisionPivot/tree/2b7000f312ccbbdce4e8625b56d8a8186ea0047a
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `2b7000f312ccbbdce4e8625b56d8a8186ea0047a`
- Note: README/tree, docs/AUDIT.md and generators/regenerate.py inspected; 13 generator and corresponding solver paths present. Dataset docs retain old relative gen_v4 paths; current public repository has generators/, solvers/ and docs/. Assets improve inspectability, but regeneration/audits/models were not run here. Solver implementation independence is not an independent external model evaluation. Related procedural training families do not by themselves prove exact item overlap.

<a id="pplx-v11-card"></a>
## Perplexity Decider v1.1: native head, attention and deployment card

- Source: https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b/blob/14c9d90137962d300f3de95633f7b6535e80c5ce/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `14c9d90137962d300f3de95633f7b6535e80c5ce`
- Note: Card and anonymous model metadata inspected: Apache-2.0, Qwen3.8-27B identity with Qwen3_5 runtime, separate 255x5120 readout and noncausal full-attention. v1.1 is not the old v1/API artifact. Card still contains private-repository wording although inspected metadata is public/ungated; no weights downloaded or access configured. Its own numerical DI table is not imported as a new comparable result without a fully matched protocol.

<a id="pplx-v11-runtime"></a>
## Perplexity Decider v1.1: fixed native code and calibration configuration

- Source: https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b/blob/14c9d90137962d300f3de95633f7b6535e80c5ce/source/src/autojev/model.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `14c9d90137962d300f3de95633f7b6535e80c5ce`
- Note: model.py, config.json and decision_config.json reviewed. Native Qwen3_5Model plus 255-row readout, noncausal full-attention, saved temperature 1.0087417621345625, valid-option normalization and 8192-token prepare limit. Card states training/evaluation image cap 512x512 versus larger configurable inference default. Training source/config/data-manifest paths exist; full raw dataset and end-to-end reproduction not audited. Earlier v1 source snapshots retained.

<a id="vis-d3-guide"></a>
## Vis: third-party D3 Edge/Lite text training scope

- Source: https://github.com/Blockether/vis/blob/7589e04daa7af13ccd0c5b3c03a5e402c7f4abfb/resources/vis-docs/decision-models.md#choose-and-train-d3
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `7589e04daa7af13ccd0c5b3c03a5e402c7f4abfb`
- Note: Choose-and-train-D3 section and vis-decisions README/pyproject inspected. Guide requires >=0.6.0; reviewed code declares 0.6.1 at d73768e3c18d89d11f6b9a774b87d64ccd55f27d. Published bundles list Edge/Lite; code also whitelists Nano, not all six D3 sizes. Bundles remove image/video encoder. Direct site request returned 403; body was read through web retrieval and fixed to this public Markdown source. Author RAM/speed claims not imported or independently reproduced.

<a id="vis-d3-training"></a>
## Vis Decisions: text D3 full/LoRA gradients and candidate loss

- Source: https://github.com/Blockether/vis-decisions/blob/d73768e3c18d89d11f6b9a774b87d64ccd55f27d/src/blockether/vis_decisions/_d3_trainer.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `d73768e3c18d89d11f6b9a774b87d64ccd55f27d`
- Note: Pinned _d3_trainer.py, d3_training.py, _trainer.py and tests/test_d3_training.py inspected. Rows become token IDs from text/JSON state, question and integer target; no pixel/grid input. Full mode trains text backbone plus 255-row readout; LoRA freezes base backbone weights, trains adapters AND the complete readout. CE uses valid candidate-code logits, with unpadded per-row backward/gradient accumulation. Optional max_input_tokens cuts state tails during training, unlike the default overlength rejection. Checkpoint saves merged weights and separate readout. Test source checks changed/merged weights but tests/models were not executed here. No matched multimodal D3-versus-Qwen3.5 SFT/LoRA comparison on the same task/data/scale/budget was established by the reviewed sources; implementation availability is not effect evidence.

<a id="vis-d3-export"></a>
## Vis Decisions: text-only D3 reconstruction and merged FP32/ONNX export

- Source: https://github.com/Blockether/vis-decisions/blob/d73768e3c18d89d11f6b9a774b87d64ccd55f27d/src/blockether/vis_decisions/_d3.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `d73768e3c18d89d11f6b9a774b87d64ccd55f27d`
- Note: Pinned _d3.py, d3_training.py, _trainer.py and scripts/export_d3.py inspected. from_local filters language_model.* tensors; load_checkpoint instantiates Qwen3_5TextModel with no vision tower. Forward accepts only input_ids, with noncausal full-attention and causal linear-attention. _cpu_state folds LoRA deltas into saved text weights; readout saved separately; ONNX input is input_ids and code includes PyTorch/ONNX logits/argmax parity checks. These are implementation findings, not a locally verified export or independent quality result. FP32 text conversion does not establish multimodal parity.

<a id="intern-paper-v1"></a>
## Intern-Decision paper v1: image-bearing training versus text-suite evidence

- Source: https://arxiv.org/html/2610.22131v1
- Kind: `paper`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `not captured / live URL`
- Note: arXiv v1 submitted 2026-10-15. Training composition, objective/setup, evaluation Tables 2–3, qualitative section 6, and recovered settings/data composition in Appendices A/B reviewed. Authors report 17880 samples / 23500 decisions, including 5500 image-bearing samples; language backbone trained, vision/projector frozen, not a LoRA effect report. Seven-suite accuracy is text-task evidence, while visual demonstrations are selected qualitative trajectories. Authors acknowledge missing matched-data ablations and public Jevbench use during development. No matched multimodal comparison with D3 on the same task/data/scale/budget established; composition and selected examples do not establish public availability of full training data. Paper hashes/log checks are author reports, not local verification. HTML SHA-256 ede54b2b807b943b4182ca0c1dd27cfa37211062d43433f1c3fc403ab9a3a103. No model run or new accuracy number imported.

<a id="mintrec2-repo"></a>
## MIntRec2.0: conversational multimodal intent and out-of-scope benchmark

- Source: https://github.com/thuiar/MIntRec2.0/blob/38cb8bf1841cfb9b410aa6a8731394ca5ba74a39/README.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `38cb8bf1841cfb9b410aa6a8731394ca5ba74a39`
- Note: Official author README/task-framework sections reviewed. Authors identify the paper as ICLR 2024, OpenReview nY9nITZQjc. Text/audio/video, multi-party multi-turn context, in-scope CE and outlier exposure/OOS handling are relevant methodological leads. This is television-dialogue data, not screenshot-domain LoRA evidence. Publisher page/PDF/API were blocked by HTTP 403/browser verification in this review; full paper body was not obtained. Data/rights not downloaded or audited, no score imported. Reviewed artifact SHA-256 249fdd77eed4ef38dfb6e72dbc780e0b597766ce8d23b34150de7a2b8a94b645.

<a id="rlaifv-paper"></a>
## RLAIF-V: Open-Source AI Feedback Leads to Super GPT-4V Trustworthiness

- Source: https://openaccess.thecvf.com/content/CVPR2025/html/Yu_RLAIF-V_Open-Source_AI_Feedback_Leads_to_Super_GPT-4V_Trustworthiness_CVPR_2025_paper.html
- Kind: `paper`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `not captured / live URL`
- Note: CVPR 2025 publisher PDF reviewed for feedback construction, deconfounding/divide-and-conquer visual checking, preference learning and inference feedback. Relevant sections read; author outcomes are not new independent results here. Visual factuality/preferences do not establish intent classification or domain utility. No numerical performance imported and no model run. Reviewed artifact SHA-256 1f7cb72d41d680d0773620c4681eff406f74c4c72aad32d5a65b1a9e07e8ef72.

<a id="rlaifv-terms"></a>
## RLAIF-V: LoRA support and dataset/research-use restrictions

- Source: https://github.com/RLHF-V/RLAIF-V/blob/83d917b2e8118ca8e7877a796d72af9bb3e6b356/README.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `83d917b2e8118ca8e7877a796d72af9bb3e6b356`
- Note: Training/LoRA/DPO and license sections inspected. Repository LoRA support does not establish that all paper results use LoRA. README labels code Apache-2.0, dataset CC BY-NC 4.0, and adds research-use/base-model/API notices; no blanket commercial-use conclusion. No dataset/model/dependency download or training. Reviewed artifact SHA-256 3a2a2f80df2f7224137d584823fcd6476c53b1794f6e618fd99ccb7ecfea0783.

<a id="llava-critic-paper"></a>
## LLaVA-Critic: Learning to Evaluate Multimodal Models

- Source: https://openaccess.thecvf.com/content/CVPR2025/html/Xiong_LLaVA-Critic_Learning_to_Evaluate_Multimodal_Models_CVPR_2025_paper.html
- Kind: `paper`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `not captured / live URL`
- Note: CVPR 2025 publisher metadata and PDF sections on data/model/training reviewed. LLaVA-OneVision 7B/72B fine-tuned on critic instructions, with standard CE over generated judgments and justifications; pointwise/pairwise supervision includes GPT-4o-assisted labels. Do not identify this with a direct candidate-logit classifier or assert an uninspected LoRA/full-parameter setting. Evaluation quality and domain decision utility require separate validation. No accuracy number or independent run imported. Reviewed artifact SHA-256 382689036ff4e1eb41ef62ae1a98632199aec567016cc5ab2e9ee578d7916dd8.

<a id="vl-rewardbench-paper"></a>
## VL-RewardBench: A Challenging Benchmark for Vision-Language Generative Reward Models

- Source: https://openaccess.thecvf.com/content/CVPR2025/html/Li_VL-RewardBench_A_Challenging_Benchmark_for_Vision-Language_Generative_Reward_Models_CVPR_2025_paper.html
- Kind: `paper`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `not captured / live URL`
- Note: CVPR 2025 publisher PDF/data-construction and evaluation sections reviewed. 1250 curated/human-verified visual preference examples probe generative reward/judge models; benchmark is not a training recipe. Source pools include RLAIF-V/RLHF-V and others, so training/evaluation source/example/image overlap needs auditing. Read benchmark-author evaluation as its own evidence; no independent rerun or domain-quality conclusion here. Reviewed artifact SHA-256 7d55ad6cf701d7c5cd2f0859a872eeb6c37367d4d7c810c87dfc4b62c97880d5.

<a id="guo-calibration-methods"></a>
## On Calibration of Modern Neural Networks: temperature fitting method review

- Source: https://proceedings.mlr.press/v70/guo17a.html
- Kind: `paper`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `not captured / live URL`
- Note: ICML 2017 proceedings PDF temperature-scaling section reviewed, supplementing the preserved earlier abstract-level source. Fit a scalar temperature on separate calibration data; a positive common temperature preserves fixed-candidate argmax and therefore does not itself raise top-1 accuracy. Empirical calibration on studied classifiers is not a domain/shift/selection guarantee. No new performance record. Reviewed artifact SHA-256 df7c93f97204f8a3c2b10f6d5bf5265baac25f00c1ae3b473a3e1dbc102dacb2.

<a id="selective-confidence-uai2024"></a>
## How to Fix a Broken Confidence Estimator: Evaluating Post-hoc Methods for Selective Classification with Deep Neural Networks

- Source: https://proceedings.mlr.press/v244/cattelan24a.html
- Kind: `paper`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `not captured / live URL`
- Note: UAI 2024 / PMLR 244 proceedings PDF abstract/method/experiment scope reviewed. Study of post-hoc confidence scores on 84 ImageNet classifiers motivates evaluating error ranking and risk-coverage/AURC separately from classification accuracy. Does not establish the best score for dynamic-candidate VLM decisions, or certify a new domain threshold. No score/claimed multiplier imported. Reviewed artifact SHA-256 e9728ea686ce094db10fba05ec9204f9e88e308fbe3dfa3d6265a7ee04720574.

<a id="crc-iclr2024"></a>
## Conformal Risk Control: published theorem assumptions

- Source: https://proceedings.iclr.cc/paper_files/paper/2024/hash/f3549ef9b5ff520a7e41ff3cc306ab2b-Abstract-Conference.html
- Kind: `paper`; review depth: `content_reviewed`; reviewed: 2026-10-17
- Source revision: `not captured / live URL`
- Note: ICLR 2024 publisher PDF formulation, exchangeability/monotone-bounded-loss conditions and non-monotonic counterexample reviewed. Main guarantee controls expected risk under its assumptions, not per-item correctness or arbitrary fixed-calibration-set high-probability risk. Accepted-set conditional error need not be monotone in a score threshold, so the generic algorithm cannot be attached without a matching formulation. Preserves earlier arXiv source snapshots; no implementation/run performed. Reviewed artifact SHA-256 0fff32a0254a47f06a399522b83ba463d0ca62f71e3a0e094985d80cba166c0c.

<a id="startlux-wide-options"></a>
## StartLux: normalize list-form criteria/options before tournament routing

- Source: https://github.com/StartLuxLabs/StartLux-Decision/commit/83fe6c7d61a687a6e17f118b4f7d8f429f5d3a01
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-18
- Source revision: `83fe6c7d61a687a6e17f118b4f7d8f429f5d3a01`
- Note: Commit patch, fixed pipeline and fake-backend test cases read, not executed. List/tuple criteria or options now normalize before wide-choice routing, including 26 choices plus a none slot; previously those forms could return 422 while mapping-form routing already worked. Tournament stages add computation and can change candidate coverage; this is a request-handling fix, not a new weight or accuracy result. All eight v1.1 HF repository revisions still match the separately registered Oct17 card pins.

<a id="startlux-vllm-pin"></a>
## StartLux: optional vLLM extra pinned to 0.31.0

- Source: https://github.com/StartLuxLabs/StartLux-Decision/commit/4b2026c96c0c5d4f5257745b3a03caf428fc730f
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-18
- Source revision: `4b2026c96c0c5d4f5257745b3a03caf428fc730f`
- Note: pyproject/README dependency change inspected: optional vllm extra 0.19.1 to 0.31.0. Published accuracy runs used the earlier stack; installing the current extra does not recreate that execution snapshot. No dependencies installed, advisory assessment or runtime parity test performed.

<a id="strands-request-offsets"></a>
## Strands: request-local pointer offsets and tokenizer/cache concurrency fixes

- Source: https://github.com/strands-labs/strands-decider/commit/6039cf8b64c6074e75804000c07ac3d4cce795f7
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-18
- Source revision: `6039cf8b64c6074e75804000c07ac3d4cce795f7`
- Note: Patch and current infer implementation reviewed. Per-question offsets are returned with each request instead of shared mutable last offsets, preventing concurrent pointer lookups from using another request; tokenizer reconfiguration is locked and an unforkable-prefix-cache fallback flag is sticky. These can affect returned probabilities and service reliability; no trained-weight or benchmark gain inferred. External tests not executed.

<a id="strands-serving-eval"></a>
## Strands: eval/calibrate use serving model preparation

- Source: https://github.com/strands-labs/strands-decider/commit/930e6d5de16309be32579f5631a7369a3322140c
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-18
- Source revision: `930e6d5de16309be32579f5631a7369a3322140c`
- Note: collect_logits now takes the prepared SystemOneEngine model, aligning CPU fp32 torso and MPS/CPU kernel setup with serving instead of a bare eval().to(device). Torch eval/calibrate supports cuda/mps/cpu and rejects mlx; MLX remains serving/ask only. Backend-specific temperature/logits need revalidation; no newly measured calibration or accuracy values imported.

<a id="strands-v1-configs"></a>
## Strands: five published v1 seed-0 training configurations and missing-input disclosure

- Source: https://github.com/strands-labs/strands-decider/commit/94f1cc1d491ebc456140103ea60c5f7daa21eca8
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-18
- Source revision: `94f1cc1d491ebc456140103ea60c5f7daa21eca8`
- Note: Five v1 configs and current training README reviewed. Release averages seeds 0/1/2 then calibrates; committed configs describe seed 0. Qwen config identifies four unavailable mix inputs plus teacher_g28 distributions; Gemma configs depend on externally built code_v27. File hashes and settings improve provenance but do not provide those bytes/builders or full replay. Preserves historical overlap, CUDA and missing-image findings.

<a id="aa-decision-index-v1"></a>
## Artificial Analysis Decision Index methodology 1.0

- Source: https://artificialanalysis.ai/methodology/decision-index
- Kind: `evaluation_report`; review depth: `content_reviewed`; reviewed: 2026-10-18
- Source revision: `not captured / live URL`
- Note: Full methodology reviewed on Oct18, version 1.0 (October 2026). Four 25% components: private 500-item AA-Omniscience-Decision (accuracy and non-hallucination 12.5% each), 513 text-only HLE MCQs, When2Call, and average of three WildGuardTest F1 scores on 835 selected rows. Non-hallucination uses wrong/(wrong+IDK), not overall error. API choice argmax/yes>=0.5 versus structured-output LM protocol. Private items/raw runs unaudited; no leaderboard score/rank imported. Separate publisher/protocol from the HF-hosted community Decision Index. Reviewed HTML SHA-256 24f3ec44ed73d844e7ff5c64fc9e0fa09f82eb4be8cfab327451ba303bacadee.

<a id="system-one-risk-budget-v1"></a>
## Calibration and Risk-Budgeted Decisions with System One Models

- Source: https://arxiv.org/html/2610.19811v1
- Kind: `paper`; review depth: `content_reviewed`; reviewed: 2026-10-18
- Source revision: `not captured / live URL`
- Note: Messoudi and Mansar, arXiv v1 submitted Oct14; formulation, fixed-sequence LTT theorem, six English-text datasets, single-seed split protocol, limitations and appendix read. Frozen scorer/ordered threshold family come from Fit independently of iid Cal; guarantee bounds probability over calibration samples of certifying a population-risk-violating policy, not per-input correctness. Risk is FOR=P(Y=1|s(X)<tau) in the negative-action subset. No certificate means fallback policy, not per-item abstention. Query separation and constructed retrieval mixtures limit transfer; no empirical score/multiplier imported or local reproduction. Reviewed HTML SHA-256 c391dbf1dac6388435d99a154bc04fba4820e8c1384bfc715a3602f1861eeebf.

<a id="drex-v2-release"></a>
## Drex v2.0 fixed release card and public evaluation scope

- Source: https://github.com/nace-ai/drex-decision-models/blob/be8ba7c8157241b9393862e9fcec104d0dc5caff/models/drex-v2.0/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-18
- Source revision: `be8ba7c8157241b9393862e9fcec104d0dc5caff`
- Note: Full card reviewed. Qwen3.6-35B-A3B identity with Qwen3_5Moe runtime; language tower only. Public 37-task DI, public 231-item JevBench, 400-item DecideBench v1.1 and game/email claims are different protocols; only JevBench counts imported in E32. Author reports, not independent reproduction; exact evaluated weights are not linked by a run manifest to the current HF snapshot.

<a id="drex-v2-hf"></a>
## Drex v2.0 pinned HF model card/config and published LFS identities

- Source: https://huggingface.co/nace-ai/drex-v2.0/tree/3e6d164cb5c8cf264eec167905cc2448d89ea97d
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-18
- Source revision: `3e6d164cb5c8cf264eec167905cc2448d89ea97d`
- Note: Public ungated snapshot last modified Oct15. Card, config and safetensors index read; HF API blobs metadata enumerates 16 safetensors shards and head.pt. Published head.pt LFS SHA-256 6837d5c40f66de5bf08ab3eb0315985281ce85d711c3a86b3fbbb025d194c5af. Canonical sorted filename-to-{sha256,size} JSON for those 17 files has SHA-256 63d602e7cce6a8386b002e7d09904b63d89267eb99eaa791ce67407eeaf71f26. Metadata identities were inspected, not independently verified by downloading tensors; they do not identify evaluated binaries. Vision config is present in base packaging but the reviewed runtime uses language only.

<a id="drex-v2-runtime"></a>
## Drex fixed runtime: language-only MoE loading and independent question rows

- Source: https://github.com/nace-ai/drex-decision-models/blob/be8ba7c8157241b9393862e9fcec104d0dc5caff/kev/model.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-18
- Source revision: `be8ba7c8157241b9393862e9fcec104d0dc5caff`
- Note: load_backbone extracts language_model from Qwen3_5MoeForConditionalGeneration and discards the remaining wrapper/vision tower. Hybrid backbones use independent causal question rows, recomputing state without prefix caching; supported fork paths can reuse prefixes. A batched request is not proof of one shared all-question encoding. Code and serving/checkpoint interfaces read only, never imported/executed.

<a id="drex-v2-license"></a>
## Drex v2.0 Nace.AI Open RAIL-M weight license

- Source: https://huggingface.co/nace-ai/drex-v2.0/blob/3e6d164cb5c8cf264eec167905cc2448d89ea97d/LICENSE
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-18
- Source revision: `3e6d164cb5c8cf264eec167905cc2448d89ea97d`
- Note: Full model license read: commercial-use thresholds, competitor exclusions and downstream use restrictions remain material; separate licensing can be required. Code, model, data and complementary material have distinct terms. Public access is not unrestricted open source; this is a source description, not legal advice.

<a id="group-time-cv-docs"></a>
## scikit-learn: grouped/time-aware cross-validation and held-out selection

- Source: https://scikit-learn.org/stable/modules/cross_validation.html
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-18
- Source revision: `not captured / live URL`
- Note: Official documentation reviewed Oct18: separate model selection from final holdout, fit preprocessing within training folds, keep groups disjoint and use time-aware evaluation for temporal targets. Stratification does not override group/time constraints. Proposed screenshot connected-component grouping and separate calibration roles are curatorial design choices, not an implemented sklearn experiment. No library installed or CV run on real data.

<a id="binomial-interval-reference"></a>
## NIST/SEMATECH: binomial confidence intervals

- Source: https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-18
- Source revision: `not captured / live URL`
- Note: Official handbook section reviewed: Wilson and binomial-tail interval methods, including small-sample cautions. Guide examples (8/10 Wilson interval, zero-error one-sided bounds) are fictional arithmetic calculations under iid/fixed-policy assumptions, not model results or guarantees for correlated screenshots/adaptive selection. No real sample size, labels or predictions published.

<a id="mire-organizer-2025"></a>
## Multimodal Intent Recognition in E-Commerce: Challenges, Innovations, and Lightweight Solutions

- Source: https://doi.org/10.1145/3701716.3719642
- Kind: `paper`; review depth: `content_reviewed`; reviewed: 2026-10-18
- Source revision: `not captured / live URL`
- Note: Organizer paper by Junwen Liu et al., WWW Companion 2025 pp.3008–3011, full four-page public-paper copy read using local PDF text extraction; SHA-256 9393318023f3072fdcf0b4d8646231565df577b0f5a0c859b48c8578eab86f81. Sections 2–4, award Table 1 and abstract/conclusion reviewed. Confirms 23+23 tasks, competition data/resource constraints, method summaries and separate expert evaluation. Earlier remote ACM access was blocked; this review obtained the text. Table 1 awards are not an exact per-team F1 leaderboard; broad baseline-to-top-team claims are not imported as reproducible effects.

<a id="mire-contract-oct18"></a>
## MIRE fixed data, generation, submission and scoring contract audit

- Source: https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/mire_baseline/cal_acc.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-18
- Source revision: `d101287af90d114c5bf0cbfbd56fe9c52358e3bb`
- Note: Read both READMEs, all three configs, convert2submit.py, cal_acc.py and ten demo records at the fixed revision. Instruction contains dialogue/candidates even when input is empty; images are separate and output is a target. Local scoring uses weighted F1/P/R and accuracy over label strings, despite a misleading multilabel docstring. Conversion aligns predictions by row index, not an ID join. Full SFT, sample read cap, context/generation caps and competition limits are distinct. Public demo images were not available/read; no downloaded code executed.

<a id="mire-tianchi-rules"></a>
## MIRE official phases, resource rules and composite final review

- Source: https://tianchi.aliyun.com/competition/entrance/532277
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-18
- Source revision: `not captured / live URL`
- Note: Public rendered official introduction inspected in an anonymous browser Oct18. Preliminary and semifinal test phases precede expert review Jan22–27 2025; final placement combines online and expert evaluation. Rules state <10B, at most three model calls per sample and total output within 100 tokens, private deployability and full inference code; prohibit private-domain training data/commercial LLM API calls in the contest. No credentials, registration, dataset download or submission performed. Publication/usage rights remain separate.

<a id="mire-tianchi-scoring"></a>
## MIRE official task labels and all-class weighted-F1 definition

- Source: https://tianchi.aliyun.com/competition/entrance/532277/information
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-18
- Source revision: `not captured / live URL`
- Note: Public rendered official task/data page inspected Oct18. Contains the complete active 23 scene and 23 intent labels; data description 1000 annotated training, 10000 preliminary and 10000 new semifinal examples. Score is weighted F1 across all classification labels, not an equal mean of two task F1 values. Submission CSV needs id and predict. Exact class supports/task proportions/raw labels were not obtained.

<a id="mire-tianchi-semifinal"></a>
## MIRE official semifinal leaderboard: exact three-team score columns

- Source: https://tianchi.aliyun.com/competition/entrance/532277/rankingList
- Kind: `evaluation_report`; review depth: `content_reviewed`; reviewed: 2026-10-18
- Source revision: `not captured / live URL`
- Note: Rendered algorithm leaderboard reviewed Oct18: selected later algorithm round (复赛; English UI Final Round), distinct from composite expert-final placement. scale 0.9085 / intent 0.9265 / scene 0.8676, 拥抱LLM 0.9070 / 0.9420 / 0.8278, Dynamic Challengers 0.9051 / 0.9365 / 0.8339. Best-submission dates Jan19/Jan19/Jan18 2025. Preserve official score column; do not derive it by task averaging or infer exact task counts. Public board inspected, underlying submissions/predictions not independently replayed.

<a id="mire-tianchi-final"></a>
## MIRE official final composite awards: gold, silver and bronze

- Source: https://tianchi.aliyun.com/competition/entrance/532277/customize583
- Kind: `official_publication`; review depth: `content_reviewed`; reviewed: 2026-10-18
- Source revision: `not captured / live URL`
- Note: Rendered official final-results table inspected Oct18: Dynamic Challengers gold/final rank1, 拥抱LLM silver/rank2, scale bronze/rank3. These are composite final awards, not semifinal online score ranks. Exact expert/composite numeric scores not published in this inspected table; no invented final-score column.

<a id="intentiongpt-abstract"></a>
## IntentionGPT: Boosting E-commerce User Intent Recognition with Self-data Augmentation and Structure-aware Retrieval

- Source: https://doi.org/10.1145/3701716.3718370
- Kind: `paper`; review depth: `abstract_reviewed`; reviewed: 2026-10-18
- Source revision: `not captured / live URL`
- Note: Publisher SIGWEB WWW25 Companion TOC abstract and DOI identity inspected; full paper not obtained. Describes self-data augmentation, collaborative noise filtering, structure-aware retrieval and model soups; author claims first place. Organizer overview independently attributes matching method families to gold team Dynamic Challengers. Exact submission/checkpoint/code mapping and backbone/training details not verified. Do not confuse with IntentGPT or unrelated same-name chat applications.

<a id="cusmer-abstract"></a>
## CuSMer: Multimodal Intent Recognition in Customer Service via Data Augment and LLM Merge

- Source: https://doi.org/10.1145/3701716.3718373
- Kind: `paper`; review depth: `abstract_reviewed`; reviewed: 2026-10-18
- Source revision: `not captured / live URL`
- Note: Publisher SIGWEB WWW25 Companion TOC abstract and DOI identity inspected; full paper not obtained. Two author-described pipelines: pseudo-labeling→fine-tuning→LLM merging and image augmentation→fine-tuning→LLM merging. Abstract first-round third/final-round first is an online-stage claim, not composite gold. Organizer overview gives scale diversity/confidence sampling and Breadcrumbs/TIES merge descriptions; these are attributed overview claims, not a code audit or isolated causal effect.

<a id="cusmer-team-identity"></a>
## CuSMer author page: scale@DLUT bronze-medal identity

- Source: https://binglin-wu.github.io/
- Kind: `official_publication`; review depth: `content_reviewed`; reviewed: 2026-10-18
- Source revision: `not captured / live URL`
- Note: Author news/publication page read: CuSMer authors and scale@DLUT bronze at this exact competition align with official scale final rank3. Dalian university news separately describes online/final-round first and composite bronze. An author page establishes attribution, not release of source code, evaluated weights or independent replication.

<a id="strands-init-from-oct19"></a>
## Strands: continuing released adapter and head training

- Source: https://github.com/strands-labs/strands-decider/commit/e69edb2650d87ecdd28e6ff0563c5a40d716f1f1
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-25
- Source revision: `e69edb2650d87ecdd28e6ff0563c5a40d716f1f1`
- Note: Commit patches for loader, training and README inspected. init_from now preserves and trains the trained adapter and pointer/slot head rather than replacing a head and freezing the torso. Architecture conflicts are rejected, fitted temperatures reset, checkpoint KL anchoring supported. Vision loader explicitly refuses trainable mode. This is a text adaptation implementation change, not a new released checkpoint or measured quality gain; upstream tests inspected, not executed.

<a id="gliner-ddp-oct20"></a>
## GLiNER2: distributed training gradient synchronization fix

- Source: https://github.com/fastino-ai/GLiNER2/commit/fe3145e065958f9d6f738cdc891acff0cd673efc
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-25
- Source revision: `fe3145e065958f9d6f738cdc891acff0cd673efc`
- Note: Patch inspected: register ExtractorOutput as a pytree dataclass, disable static_graph by default, and touch every trainable parameter with a zero term per distributed step. Author identifies previously silent rank-local gradient drift. Applies to multi-GPU training; it does not prove that any published Decide checkpoint used the defective path or was retrained. No new weight/performance conclusion.

<a id="kev-data-contract-oct22"></a>
## Kev: complete-question identity for data splits and conflict detection

- Source: https://github.com/jaredpalmer/kev/commit/ac8e24524695cfb2d5147bf8063c3db3ef9276e6
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-25
- Source revision: `ac8e24524695cfb2d5147bf8063c3db3ef9276e6`
- Note: Data-preparation code and test patches inspected. Conflict identity now includes type/instructions/criteria; different rubrics for one state are retained, summaries distinguish forms, and variants of the same state stay in one partition. This fixes adaptation data handling, not held-out accuracy or published weights.

<a id="kev-score-decimal-oct22"></a>
## Kev: preserve exact JSON score fractions before label validation

- Source: https://github.com/jaredpalmer/kev/commit/e7ae8fd5fda9d40865d3a9de90f074feb0735985
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-25
- Source revision: `e7ae8fd5fda9d40865d3a9de90f074feb0735985`
- Note: Converter and synthetic-data parser patches inspected. Decimal parsing prevents fractional JSON scores near an integer from being rounded into a valid ordinal label. Non-score fields retain conventional JSON conversion. No trainer/model code executed or accuracy inferred.

<a id="startlux-prism-oct22"></a>
## StartLux-Prism: GGUF CUDA runtime, parity scope and licensing

- Source: https://github.com/StartLuxLabs/StartLux-Prism/tree/f32ed8eee9d89ea56dde03a978cf4128d2bbf497
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-25
- Source revision: `f32ed8eee9d89ea56dde03a978cf4128d2bbf497`
- Note: README and docs/testing.md at this source revision inspected; upstream Decision README integration commit 18256c5cfb4ce6dd184583886a3ca1e437522a94 reviewed. Supports causal v1/v1.1 AutoThink 4B/9B/27B, not bidirectional Instant. Q8_0/W4A8, shared-state branching, images with mmproj and optional thoughts. Internal bit invariance/parity tests are author reports, not equivalence to BF16 on all inputs. Activation-range calibration is quantization calibration, distinct from probability calibration. v1.1 allow_none defaults on versus off in the other package; gate remains 0.6 versus paper 0.9. Own code has no chosen license; vendored files Apache-2.0, model weights CC BY-NC 4.0. No speed multiplier imported.

<a id="drex-apple-oct23"></a>
## Drex v2.0: Q4_K_M Apple deployment and corrected engine limits

- Source: https://github.com/nace-ai/drex-decision-models/blob/f2afd75f714997fe8a950888252b833f2c5198f9/models/drex-v2.0/apple-silicon.md
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-25
- Source revision: `f2afd75f714997fe8a950888252b833f2c5198f9`
- Note: Full page and release-card patch read. Q4_K_M deployment added for Kapitsa v0.2.15 and Nace llama.cpp/Ollama forks. Author timing is a short-ticket localhost sequential median on M5 Pro 48GB; repeat-state cache and cold calls are distinct. llama.cpp tested at 36GB, all three at 48GB: not validation of every Mac/workload. Quantized output accuracy/calibration equivalence is not established by speed/fit. Retain modified model license separately from runtime licenses.

<a id="kapitsa-systemone-v0215"></a>
## Kapitsa v0.2.15: shared recurrent state, branch readout and limits

- Source: https://github.com/nace-ai/kapitsa/blob/5c489cc69b397d2088aa165f9017129b4a724b7a/docs/systemone.md
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-25
- Source revision: `5c489cc69b397d2088aa165f9017129b4a724b7a`
- Note: System One docs read at resolved v0.2.15 commit. Reuses a checkpointed state with separate question branches and unquantized F32 pointer head; transformer layers remain quantized. Default sequence/state/branch/packed caps are each 16384, separately configurable; 131072 capacity is not verified quality. Cache equality to four decimals and upstream tests are author assertions, not this repository running them. No execution or install.

<a id="pplx-v12-card"></a>
## Perplexity Decider v1.2: joint requests and retrained data mixture

- Source: https://huggingface.co/perplexity-ai/pplx-decider-v1.2/blob/cce0f3f80033e9d89d80831d5281fd72124aacce/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-25
- Source revision: `cce0f3f80033e9d89d80831d5281fd72124aacce`
- Note: Full card, file tree and tag-only commit inspected. Native 27B release changes joint attention/request format and training mix; benchmark train-split inclusion and decontamination are author disclosures. 262144 configured length versus about 32k training, longer log spot-check only. Temperature 1.382 fitted in joint format; transfer calibration is not guaranteed. Packed BF16 fast path has near-tie differences; FP8 is optional and shifts probabilities. Current cce0f3f commit adds only a discovery tag over release parent 225c913: not another weight release. Public tree readable; card still says private, download access/weights not tested.

<a id="pplx-flash-v12-card"></a>
## Perplexity Decider Flash v1.2: distilled 4B and grouping regressions

- Source: https://huggingface.co/perplexity-ai/pplx-decider-flash-v1.2/blob/9ff7cf9838e59df461c276b7699d56b244d2af58/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-25
- Source revision: `9ff7cf9838e59df461c276b7699d56b244d2af58`
- Note: Full card, public file tree and tag-only commit inspected. Qwen3.5-4B probability distillation/model soup; separate 255x2560 head, joint format and T=1.554. Author recommends one question per request; grouping can hurt independent-candidate tasks. Joint-format calibration cannot be assumed optimal after changing grouping. Current revision adds a metadata tag only; weights/evaluated binary mapping not locally verified.

<a id="decision-index-v04-method"></a>
## HF community Decision Index: private-only text Full and separate vision formula

- Source: https://huggingface.co/spaces/multimodalart/jev-decision-index/blob/5b9973d31e1b3cff2702ed61e518306ddb279b91/methodology.html
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-25
- Source revision: `5b9973d31e1b3cff2702ed61e518306ddb279b91`
- Note: Methodology HTML source sections on v0.4, v0.3 and vision inspected, plus current README. Text v0.4 Full weights private same-skill/new-domain 60/40 after public-scale mapping; public scores no longer contribute. Private new-domain task set is revised, selected by consistency of stock-model ordering, and unavailable for audit. Vision remains 50% public/50% private same-skill; text 0.9-point tie grouping retained. Upstream removes live archival files at this commit; historical source pins/evidence here retained. Current board labels 0.4.1; no scores/ranks imported.

<a id="baseten-decision-report"></a>
## Base Labs: mammoth-1 / elephant-1 technical report

- Source: https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models
- Kind: `official_publication`; review depth: `content_reviewed`; reviewed: 2026-10-25
- Source revision: `not captured / live URL`
- Note: Full method, data-evolution, training, results and future-directions sections reviewed. Language fine-tuning, frozen vision, block full-attention and CE+Brier; public DI feedback informs Mix1–8. Report says text-only training, conflicting with current card image-training wording. Public ablation and private DI/author AA replica are different evaluations. No ranks or gains imported; no independent contamination or tensor audit.

<a id="mammoth-card-oct25"></a>
## Mammoth-1 current card: image-input claim and conflicting training description

- Source: https://huggingface.co/baselabs/mammoth-1
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-25
- Source revision: `not captured / live URL`
- Note: Current card read, but fixed historical blob/API reads inaccessible; no source hash inferred. MIT declaration, trained length16384, candidate-limit and request rejection contract reviewed. Card says text/image decision training; technical report says text alone. Image support and image supervision/quality remain separate. Public data recipe does not equal fully inspectable training data. Current live scores are not assigned to an inferred weight revision.

<a id="jeffan-card-oct25"></a>
## Jeffan-31b-1710: model card and published conditional-reread engine

- Source: https://huggingface.co/tattrongvu/Jeffan-31b-1710/blob/cebfa86c2bed2b5c83b12e44de4374b20c87fd79/inference/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-25
- Source revision: `cebfa86c2bed2b5c83b12e44de4374b20c87fd79`
- Note: Card and full inference README reviewed. Text-only Gemma-4-31B-it letter-logit scorer; no disclosed training recipe/data or independent overlap audit. Engine conditionally repeats whole input below0.9 and replaces first distribution; submitted policy is not uniformly single-pass. Card8192 versus engine98304 capacity; public-suite observed lengths do not validate arbitrary context. Simulated96GB cap on B200 is not measured RTX hardware. No rank/score imported.

<a id="jeffan-license-oct25"></a>
## Jeffan: license-only change to Apache-2.0

- Source: https://huggingface.co/tattrongvu/Jeffan-31b-1710/commit/cebfa86c2bed2b5c83b12e44de4374b20c87fd79
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-25
- Source revision: `cebfa86c2bed2b5c83b12e44de4374b20c87fd79`
- Note: Inspected five-file license/README/pyproject diff: Apache-2.0 replaces CC BY-NC4.0 for weights and MIT for inference code. No weight file listed as changed. This revision is a source/license identity, not an evaluated tensor hash or new quality result. Upstream base terms still need checking.

<a id="routeguard-paper-v1"></a>
## Cost-Aware Abstention for LLM-Based IT Ticket Classification

- Source: https://arxiv.org/html/2610.31657v1
- Kind: `paper`; review depth: `content_reviewed`; reviewed: 2026-10-25
- Source revision: `not captured / live URL`
- Note: Sachin Gupta, Oct22 v1. Full paper reviewed:47,837 tickets/eight labels, train/cal/test33486/4784/9567; LLM common test1000/cal500 per condition. Cost and calibration conclusions are author reports. Constant self-confidence remains nondiscriminative after isotonic calibration. Labels/training access differ across trained versus prompted models; prompt/budget and provider/precision ablations are confounded. Random split, idealized correct human triage/fixed costs, historical endpoints: no temporal/production or universal LLM claim.

<a id="routeguard-code"></a>
## RouteGuard fixed code/README and inaccessible external archive

- Source: https://github.com/sachinkg12/RouteGuard/tree/22a2c3988281bc7b2249fa8ce985678442ff1af3
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-25
- Source revision: `22a2c3988281bc7b2249fa8ce985678442ff1af3`
- Note: Code/README inspected at Sep10 commit; paper submission Oct22 is separate. MIT code. Text-free vectors/manifest claimed in Zenodo concept DOI10.5281/zenodo.22609128, but archive inaccessible in review; exact artifact version/hash not verified. README pending-arXiv wording stale. No recomputation executed, publisher receipt is not independent reproduction.

<a id="commit-or-abstain-paper-v1"></a>
## Commit or Abstain? Missing Legal Authority evaluation

- Source: https://arxiv.org/html/2610.29961v1
- Kind: `paper`; review depth: `content_reviewed`; reviewed: 2026-10-25
- Source revision: `not captured / live URL`
- Note: M.Mikail Demir, Oct21 v1 under review; full methods/results/limitations and appendices inspected. Third-party relative to evaluated providers, not reproduced here. Constructed CaseHOLD absent-correct-option subset1670/5314, explicit none option. Opposite wrong-pick/false-abstention errors retained in E34. Public pre2021 text may overlap pretraining despite perturbation checks. One English legal task and constructed absence do not establish real legal retrieval/citation reliability. Hosted snapshot identities and full human-review costs unresolved.

<a id="commit-or-abstain-code"></a>
## Commit or Abstain fixed prompts, logs and result summaries

- Source: https://github.com/mmikaildemir/commit-or-abstain/tree/f3d49c6de7d5943bb1981c0a55d504f1bae5fa33
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-25
- Source revision: `f3d49c6de7d5943bb1981c0a55d504f1bae5fa33`
- Note: README at Oct21 commit inspected: paired data, exact prompts, raw API logs, cost/result summaries and recalculation scripts listed. No code executed or artifacts regenerated here. MIT code; CaseHOLD material retains upstream terms. Stored evaluations are reported evidence, not this repository rerunning them.

<a id="qwen-vl-train-oct26"></a>
## QwenVL official image SFT and LoRA trainer

- Source: https://github.com/QwenLM/Qwen3-VL/blob/96588727e44c78b25ba03ea03b8e12f7e64fd0da/qwen-vl-finetune/qwenvl/train/train_qwen.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `96588727e44c78b25ba03ea03b8e12f7e64fd0da`
- Note: Trainer body inspected: Qwen2-VL/2.5-VL/3-VL dense/MoE class dispatch, matching AutoProcessor, PEFT attention projections, supervised data module, model and processor saving. This dispatch is not Qwen3.5 support. Latest inspected tree commit is Jan30 2026, not an Oct26 feature release. No model code executed. Repository LICENSE is Apache-2.0; selected checkpoint/data terms are separate.

<a id="qwen-vl-data-oct26"></a>
## QwenVL official visual tensors and answer masking

- Source: https://github.com/QwenLM/Qwen3-VL/blob/96588727e44c78b25ba03ea03b8e12f7e64fd0da/qwen-vl-finetune/qwenvl/data/data_processor.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `96588727e44c78b25ba03ea03b8e12f7e64fd0da`
- Note: Image processing, pixel_values/image_grid_thw, multimodal positions and assistant-label masking inspected. The ordinary collator slices tokens to model_max_length; audit retained evidence and labels rather than assume overlength examples fail closed. Source-path inspection is not a successful training or export run.

<a id="qwen-vl-training-readme-oct26"></a>
## QwenVL training formats, dependencies and scope

- Source: https://github.com/QwenLM/Qwen3-VL/blob/96588727e44c78b25ba03ea03b8e12f7e64fd0da/qwen-vl-finetune/README.md
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `96588727e44c78b25ba03ea03b8e12f7e64fd0da`
- Note: Read image/conversation format, full/LoRA flags and dependencies. Image markers must match media. Documentation examples are starting points, not a locally verified environment; MoE/ZeRO restrictions and the exact model class matter. Do not use its random validation fraction as a group/time split protocol.

<a id="swift-qwen35-guide-oct26"></a>
## ms-swift Qwen3.5/3.6/3.8 image-bearing LoRA guide

- Source: https://github.com/modelscope/ms-swift/blob/942be5a6120d46443f1b1940f2902c3757e312a5/docs/source_en/BestPractices/Qwen3_8-Best-Practice.md
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `942be5a6120d46443f1b1940f2902c3757e312a5`
- Note: Read image/messages custom format, dense Qwen3.5-4B LoRA with OCR data, MoE training, inference and version caveats. Source also describes Qwen3.6/3.8 but this review does not validate every replacement checkpoint/backend. Repository LICENSE Apache-2.0 inspected. Oct26 tree head concerns RLHF log-softmax performance, not a new image-training release; demonstration memory/time is not a local measurement.

<a id="swift-qwen35-example-oct26"></a>
## ms-swift Qwen3.5 image OCR LoRA example

- Source: https://github.com/modelscope/ms-swift/blob/942be5a6120d46443f1b1940f2902c3757e312a5/examples/models/qwen3_5/transformers.sh
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `942be5a6120d46443f1b1940f2902c3757e312a5`
- Note: Qwen3.5-35B-A3B, OCR image dataset, LoRA and adapter inference example inspected without running it. Explicit model/template/data wiring is stronger than API compatibility; rank, learning rate, random split and hardware comments are not recommended business defaults.

<a id="swift-qwen35-loader-oct26"></a>
## ms-swift Qwen3.5 multimodal model loader

- Source: https://github.com/modelscope/ms-swift/blob/942be5a6120d46443f1b1940f2902c3757e312a5/swift/model/models/qwen.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `942be5a6120d46443f1b1940f2902c3757e312a5`
- Note: Qwen3_5Loader uses Qwen3_5ForConditionalGeneration; dense 0.8B/2B/4B/9B model registration and model architecture/visual hooks inspected. This is distinct from Qwen3-VL trainer dispatch. No weights loaded or optimizer run.

<a id="swift-qwen35-template-oct26"></a>
## ms-swift Qwen3.5 visual template and position handling

- Source: https://github.com/modelscope/ms-swift/blob/942be5a6120d46443f1b1940f2902c3757e312a5/swift/template/templates/qwen.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `942be5a6120d46443f1b1940f2902c3757e312a5`
- Note: Qwen3_5Template derives from the visual template; image grids, multimodal position handling and packing/version guard inspected. Template handles role whitespace/thinking formatting; freeze the exact render and serving parity in any later experiment. No local runtime verification.

<a id="intern-visual-release"></a>
## Intern-Decision original public training-code release

- Source: https://github.com/InternLM/Intern-Decision/commit/63292c8b5e0f5d410a7159e0f1c14475b828839a
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `63292c8b5e0f5d410a7159e0f1c14475b828839a`
- Note: GitHub commit metadata: Sep26 2026 08:03:14 UTC, training/inference/demo/evaluation release. Config, dataset, masked tokenizer, model and verification blobs match the Oct22 tree inspected here. Oct22 adds report/community/citation documentation. This is deeper review of an existing path, not a new Oct26 release or reproduction.

<a id="intern-visual-data-oct26"></a>
## Intern-Decision hard-label and local-image training contract

- Source: https://github.com/InternLM/Intern-Decision/blob/565350244af860e1c276768cd80bdd9b8be93913/docs/DATA.md
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `565350244af860e1c276768cd80bdd9b8be93913`
- Note: Read canonical JSONL, ordered local images resolved against MEDIA_ROOT, hard targets outside model evidence, 62 single-token symbols and strict row errors. Explicitly excludes original training data, private calibration/validation records, media and preparation pipelines. This document does not disclose the mixture; the separate paper does report its composition.

<a id="intern-visual-loader-oct26"></a>
## Intern-Decision actual UniversalDataset construction

- Source: https://github.com/InternLM/Intern-Decision/blob/565350244af860e1c276768cd80bdd9b8be93913/src/inputs/dataset.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `565350244af860e1c276768cd80bdd9b8be93913`
- Note: UniversalDatasetConfig.build constructs UniversalDataset(JsonlDataset), whose __getitem__ calls tokenize_fn(row, media_root). The qwen35.py class_name string alone does not identify the constructed dataset. Strict cache counts and no replacement rows; source only.

<a id="intern-visual-masking-oct26"></a>
## Intern-Decision visual tokenization, labels and collator

- Source: https://github.com/InternLM/Intern-Decision/blob/565350244af860e1c276768cd80bdd9b8be93913/src/inputs/masked.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `565350244af860e1c276768cd80bdd9b8be93913`
- Note: MaskedQwen3VLTokenizeFunction adds marker, validates one-token codes, passes images to the processor and calculates multimodal positions. Collator supplies pixels/grid and shifts marker targets to preceding logits. Config uses full-vocabulary masked CE, not candidate-subset CE or a supplied LoRA recipe. No training run.

<a id="intern-visual-model-oct26"></a>
## Intern-Decision frozen visual-feature injection

- Source: https://github.com/InternLM/Intern-Decision/blob/565350244af860e1c276768cd80bdd9b8be93913/src/model/qwen.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `565350244af860e1c276768cd80bdd9b8be93913`
- Note: DecisionQwen._prepare_llm_inputs computes frozen visual features and injects them into language embeddings; image input with missing grid or text-only forward rejects. Frozen vision/projector are enforced. Text-only batches participate in frozen visual collectives without becoming image training evidence. No local gradient audit.

<a id="intern-visual-save-oct26"></a>
## Intern-Decision checkpoint verification boundaries

- Source: https://github.com/InternLM/Intern-Decision/blob/565350244af860e1c276768cd80bdd9b8be93913/scripts/verify_checkpoint.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `565350244af860e1c276768cd80bdd9b8be93913`
- Note: Verifier checks unchanged saved visual tensors, at least one changed language-layer weight and per-rank load audit files. Related scripts/train.sh uses fresh work directory, local MODEL_PATH/tokenizer/processor and canonical user-supplied JSONL; qwen35.py requests final HF output without auto-resume. This checks specified tensor conditions, not inference quality, full export equivalence or release-data replay. None executed here.

<a id="d3-turbo-card"></a>
## D3-Turbo card: state reuse, localization and API alias

- Source: https://huggingface.co/vllm-sr/d3-turbo/blob/a0f3e9e59ebd1202fe1d4de1c4c0f9a986758cbb/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `a0f3e9e59ebd1202fe1d4de1c4c0f9a986758cbb`
- Note: HF metadata: created Oct19 2026; latest tree Oct20 15:49:39 UTC. Card scope, Box/Track, API alias and evaluation caveats reviewed. Text/vision Index values are author estimates against a 0.3.2 snapshot, not official/current board results; no new numeric result imported. Box always emits a box, including absent targets; presence needs a separate judgment. Card/LICENSE declare Apache-2.0. No tensor download or inference.

<a id="d3-turbo-runtime"></a>
## D3-Turbo prefix_bidir StateOnce implementation

- Source: https://huggingface.co/vllm-sr/d3-turbo/blob/a0f3e9e59ebd1202fe1d4de1c4c0f9a986758cbb/d3_runtime.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `a0f3e9e59ebd1202fe1d4de1c4c0f9a986758cbb`
- Note: Read attention/StateOnce implementation: state attends within state; each question branch reads cached state and its own block. Full-attention state K/V plus causal DeltaNet recurrent/convolution state are reused. This is not cross-question joint attention as in Decider v1.2. Package switch can revert to per-question rows. No runtime executed.

<a id="d3-turbo-wrapper"></a>
## D3-Turbo wrapper still refuses training and generic saving

- Source: https://huggingface.co/vllm-sr/d3-turbo/blob/a0f3e9e59ebd1202fe1d4de1c4c0f9a986758cbb/modeling_d3.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `a0f3e9e59ebd1202fe1d4de1c4c0f9a986758cbb`
- Note: train(True) raises inference-only RuntimeError; save_pretrained and push_to_hub are not generic training export paths. Separate implementations remain possible, but image training/LoRA cannot be inferred from multimodal inference or the Qwen architecture. No local test of the wrapper.

<a id="d3-turbo-config"></a>
## D3-Turbo fixed decision configuration

- Source: https://huggingface.co/vllm-sr/d3-turbo/blob/a0f3e9e59ebd1202fe1d4de1c4c0f9a986758cbb/decision_config.json
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `a0f3e9e59ebd1202fe1d4de1c4c0f9a986758cbb`
- Note: prefix_bidir, 255 code IDs, FP32 readout, T=1, validated_length=32768 and Box calibration assets inspected alongside config/manifest. Manifest supplies hashes, not this review independently hashing weights. Backbone context capacity is distinct from validated_length/long-context card mode; localization calibration does not calibrate intent risk.

<a id="d3-turbo-eval-runtime"></a>
## D3-Turbo external evaluator runtime note

- Source: https://huggingface.co/vllm-sr/d3-turbo/blob/a0f3e9e59ebd1202fe1d4de1c4c0f9a986758cbb/.eval_results/vllm-sr__d3-turbo.yaml
- Kind: `evaluation_report`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `a0f3e9e59ebd1202fe1d4de1c4c0f9a986758cbb`
- Note: Oct19 evaluator metadata says native AutoModel.system_one used because vLLM nightly did not then support prefix_bidir. This historical limitation does not prove current nightly failure. SR Engine and native upstream vLLM are separate paths; bucket logs/metrics not audited or reproduced, and no scores imported.

<a id="clef-community-training"></a>
## Community Clef adapter and FP32 head training loop

- Source: https://github.com/MersivMedia/clef-finetune/blob/c83f7bc1acc23c81ad0de838510c59c48bf60c79/src/clef_finetune/train.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `c83f7bc1acc23c81ad0de838510c59c48bf60c79`
- Note: Oct2 v0.1.0 source: resolve_images -> encode_record(processor) -> collate_records -> model -> CE/Brier loss/backward; adapter and head saved separately. Code LICENSE Apache-2.0 inspected. Static image-to-loss wiring is not a real-weight image-training run; community implementation does not reproduce proprietary RLCD.

<a id="clef-community-status"></a>
## Community Clef fine-tuning explicit unverified cases

- Source: https://github.com/MersivMedia/clef-finetune/blob/c83f7bc1acc23c81ad0de838510c59c48bf60c79/docs/KNOWN_ISSUES.md
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `c83f7bc1acc23c81ad0de838510c59c48bf60c79`
- Note: Maintainer explicitly reports no real Clef/Clef-Flash GPU training, no image/video training test, no multi-GPU/QLoRA validation; tiny random CPU plumbing only. Documents option sorting, exact LoRA module regex after reload and FP32 head handling. These tests were not rerun here. Ordinal EMD is supervised loss, not RLCD.

<a id="mlx-image-training-boundary"></a>
## mlx-decision rejects media in training records

- Source: https://github.com/armbues/mlx-decision/blob/d3e239a8c8c2afb362725f94c5076b90221168a5/src/mlx_decision/data/format.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `d3e239a8c8c2afb362725f94c5076b90221168a5`
- Note: Training parser rejects nonempty images/videos and images embedded in state. Mac image inference cannot establish multimodal adaptation. Read only; no port or local model run.

<a id="mlx-training-scope"></a>
## mlx-decision provisional training scope

- Source: https://github.com/armbues/mlx-decision/blob/d3e239a8c8c2afb362725f94c5076b90221168a5/docs/TRAINING.md
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `d3e239a8c8c2afb362725f94c5076b90221168a5`
- Note: Docs explicitly exclude image training and LoRA/full adaptation of Clef/pplx/d3/H2O-Lightning/d1; supported fitting changes only the head/readout with networks frozen. No conclusion about all MLX frameworks or future versions. Does not change the separate historical FluidUse records.

<a id="rep2act-paper-v1"></a>
## From Knowing to Abstaining / VAD-R / Rep2Act v1

- Source: https://arxiv.org/html/2609.32653v1
- Kind: `paper`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `not captured / live URL`
- Note: Sep26 2026 v1; read benchmark design, method, metrics and appendix. Evidence-gap labels and separate routing supervision motivate annotation experiments. A-Acc measures answer/abstain action agreement, not final-answer correctness. Author-defined balanced split/model judges limit transfer. Paper CC BY 4.0; no release code/data endpoint or reusable dataset license established here. No performance number imported or experiment reproduced.

<a id="vltest-paper-v1"></a>
## VLTest joint image-text failure diagnosis v1

- Source: https://arxiv.org/html/2610.30794v1
- Kind: `paper`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `not captured / live URL`
- Note: Oct22 2026 v1; read method, controls, oracle and limitations. Four matched cells and expected-answer preservation support robustness-test design; seed-correct filtering differs from representative traffic risk. Treat as reviewed preprint, without independently verifying its TOSEM header/publication status. Paper CC BY 4.0; no scores imported.

<a id="vltest-code"></a>
## VLTest replication-code scope and missing run settings

- Source: https://github.com/beanduan22/VLTest/blob/b5861f2f990a63a1b8d0af37881471cf9034e66f/README.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-26
- Source revision: `b5861f2f990a63a1b8d0af37881471cf9034e66f`
- Note: Oct22 fixed README and MIT LICENSE read. Local seed manifest, external models/assets, separate pilot proxy thresholds and human annotation audit required. Additional open/API model adapters and concrete budget/threshold placeholders remain for the researcher. Paper automated-oracle description must not be equated to a complete out-of-box reproduction from this README. No dependencies installed or code executed; underlying dataset/image terms separate.

<a id="mlx-vlm-training-oct27"></a>
## MLX-VLM pinned image-conditioned SFT and CLI

- Source: https://github.com/Blaizzy/mlx-vlm/blob/2ceff4c14b991370a459d14eb49d1bedf4fb9e84/docs/training.md
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-27
- Source revision: `2ceff4c14b991370a459d14eb49d1bedf4fb9e84`
- Note: Oct26 2026 23:23:46 UTC tree reviewed; head change concerns model README listings, not a newly introduced training feature. Read current training guide and train.py: local image JSONL, completion-only masks, quantized-base language adapters, CLI flags, microstep counting, memory metrics and saving. Restoring weights uses a fresh optimizer; optimizer/RNG state is not saved. LICENSE is MIT. Source inspection only; no environment installed, weights fetched or training run.

<a id="mlx-vlm-visual-loss-oct27"></a>
## MLX-VLM image features and shifted completion loss

- Source: https://github.com/Blaizzy/mlx-vlm/blob/2ceff4c14b991370a459d14eb49d1bedf4fb9e84/mlx_vlm/trainer/vlm/sft/runtime.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-27
- Source revision: `2ceff4c14b991370a459d14eb49d1bedf4fb9e84`
- Note: Read runtime plus VisionDataset, common engine and Qwen3-VL model: nonempty media without features rejects; pixels/grid reach model; targets and completion mask shift by one; visual embeddings merge with text; nn.value_and_grad supplies training. Default frozen vision still conditions language adapters. No actual gradient/quality/memory test, nor blanket support for custom decision heads.

<a id="mlx-vlm-language-adapters-oct27"></a>
## MLX-VLM frozen-base language adapter targets

- Source: https://github.com/Blaizzy/mlx-vlm/blob/2ceff4c14b991370a459d14eb49d1bedf4fb9e84/mlx_vlm/trainer/peft/utils.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-27
- Source revision: `2ceff4c14b991370a459d14eb49d1bedf4fb9e84`
- Note: Read base freezing, language-transformer target discovery, QuantizedLinear adapter handling and load preparation. Actual module names/gradients must be audited after loading the exact checkpoint; general LoRA support is not a per-checkpoint successful image run or permission to train vision. No code executed.

<a id="mlx-vlm-clef-inference-oct27"></a>
## MLX-VLM Clef image inference and custom call contract

- Source: https://github.com/Blaizzy/mlx-vlm/blob/2ceff4c14b991370a459d14eb49d1bedf4fb9e84/mlx_vlm/models/clef/clef.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-27
- Source revision: `2ceff4c14b991370a459d14eb49d1bedf4fb9e84`
- Note: Read fixed Clef model and its README: predict accepts image/video evidence, while __call__ requires question_spans, option_spans and qtype. Its joint-schema head cannot be assumed trainable through ordinary shifted-SFT CLI. Distinct from mlx-decision media-training rejection and community CUDA fine-tuning.

<a id="qwen3vl-2b-original-oct27"></a>
## Qwen/Qwen3-VL-2B-Instruct pinned candidate metadata

- Source: https://huggingface.co/Qwen/Qwen3-VL-2B-Instruct/tree/89644892e4d85e24eaac8bacfd4f463576704203
- Kind: `model_card`; review depth: `metadata_only`; reviewed: 2026-10-27
- Source revision: `89644892e4d85e24eaac8bacfd4f463576704203`
- Note: Read HF API revision metadata: exact repository SHA and Apache-2.0 declaration verified. Original and conversion are separate artifacts; quantization fidelity, processor/template compatibility, weight bytes and trainability not locally tested. No weight download. Model choice is a proposed experiment, not a quality or capacity result.

<a id="qwen3vl-2b-mlx-oct27"></a>
## mlx-community/Qwen3-VL-2B-Instruct-4bit pinned candidate metadata

- Source: https://huggingface.co/mlx-community/Qwen3-VL-2B-Instruct-4bit/tree/9c4f5209e57b31f4b9dfba735de3fb983739c9cc
- Kind: `model_card`; review depth: `metadata_only`; reviewed: 2026-10-27
- Source revision: `9c4f5209e57b31f4b9dfba735de3fb983739c9cc`
- Note: Read HF API revision metadata: exact repository SHA and Apache-2.0 declaration verified. Original and conversion are separate artifacts; quantization fidelity, processor/template compatibility, weight bytes and trainability not locally tested. No weight download. Model choice is a proposed experiment, not a quality or capacity result.

<a id="qwen35-2b-original-oct27"></a>
## Qwen/Qwen3.5-2B pinned candidate metadata

- Source: https://huggingface.co/Qwen/Qwen3.5-2B/tree/15852e8c16360a2fea060d615a32b45270f8a8fc
- Kind: `model_card`; review depth: `metadata_only`; reviewed: 2026-10-27
- Source revision: `15852e8c16360a2fea060d615a32b45270f8a8fc`
- Note: Read HF API revision metadata: exact repository SHA and Apache-2.0 declaration verified. Original and conversion are separate artifacts; quantization fidelity, processor/template compatibility, weight bytes and trainability not locally tested. No weight download. Model choice is a proposed experiment, not a quality or capacity result.

<a id="qwen35-2b-mlx-oct27"></a>
## mlx-community/Qwen3.5-2B-4bit pinned candidate metadata

- Source: https://huggingface.co/mlx-community/Qwen3.5-2B-4bit/tree/674aaa7240b91e8012fcad5d791b7dfe5ba90207
- Kind: `model_card`; review depth: `metadata_only`; reviewed: 2026-10-27
- Source revision: `674aaa7240b91e8012fcad5d791b7dfe5ba90207`
- Note: Read HF API revision metadata: exact repository SHA and Apache-2.0 declaration verified. Original and conversion are separate artifacts; quantization fidelity, processor/template compatibility, weight bytes and trainability not locally tested. No weight download. Model choice is a proposed experiment, not a quality or capacity result.

<a id="apple-m5-pro-memory-oct27"></a>
## Apple MacBook Pro M5 Pro memory configurations

- Source: https://www.apple.com/macbook-pro/specs/
- Kind: `official_docs`; review depth: `content_reviewed`; reviewed: 2026-10-27
- Source revision: `not captured / live URL`
- Note: Official specification lists M5 Pro 24GB, configurable 48GB and 64GB subject to chip variant. This supports conditional resource planning only: no inspected user machine is identified here, and no training-capacity, runtime or speed is certified. Specification is a live page reviewed Oct27.

<a id="learn-then-test-v5"></a>
## Learn then Test risk-control framework v5

- Source: https://arxiv.org/html/2110.01052v5
- Kind: `paper`; review depth: `content_reviewed`; reviewed: 2026-10-27
- Source revision: `not captured / live URL`
- Note: Version history: first Oct3 2021; v5 Sep29 2022. Relevant risk-control/selective-classification and multiple-testing sections reviewed; displayed typesetting date is not treated as a new release. Valid p-values, frozen candidate family, appropriate data/loss assumptions and FWER control matter. No theorem or certification implemented here; do not infer a guarantee under clustered observations or template/time shift.

<a id="leakage-reproducibility-v1"></a>
## Leakage and the Reproducibility Crisis in ML-based Science v1

- Source: https://arxiv.org/html/2207.07048v1
- Kind: `paper`; review depth: `content_reviewed`; reviewed: 2026-10-27
- Source revision: `not captured / live URL`
- Note: Jul14 2022 v1; leakage taxonomy, independence/future-information/selection issues and model information-sheet motivation reviewed. Methodological reference, not an audit of a private dataset. No numerical study result imported or code rerun.

<a id="personalization-oos-v1"></a>
## Does Personalization Break Trust? Few-Shot Intent Adaptation v1

- Source: https://arxiv.org/html/2610.20652v1
- Kind: `paper`; review depth: `content_reviewed`; reviewed: 2026-10-27
- Source revision: `not captured / live URL`
- Note: Oct12 2026 text-encoder intent preprint. Read adaptation/scorer contrasts and limitations: OOS quality can degrade, scorer changes partly recover it, pseudo-OOS and forgetting remain. Motivates same-backbone temperature/energy/Mahalanobis controls; no VLM effect or score imported. An anonymized code link is reported but its contents/license were not audited or run.

<a id="intent-decomposition-emnlp2025"></a>
## Small Models, Big Results: Intent Extraction through Decomposition

- Source: https://aclanthology.org/2025.emnlp-main.949/
- Kind: `paper`; review depth: `abstract_reviewed`; reviewed: 2026-10-27
- Source revision: `not captured / live URL`
- Note: ACL Anthology metadata/abstract reviewed: EMNLP main proceedings, November 2025; structured interaction summarization then a fine-tuned small intent model on UI trajectories. Prior-work boundary only; full methods/artifacts and performance claims not imported. No claim that its task equals a single-image business classifier.

<a id="qwen35-4b-selection-oct27"></a>
## Qwen3.5-4B official VLM and template selection audit

- Source: https://huggingface.co/Qwen/Qwen3.5-4B/blob/851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a/README.md
- Kind: `model_card`; review depth: `content_reviewed`; reviewed: 2026-10-27
- Source revision: `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a`
- Note: Read official card, API revision/license, config and chat_template.jinja. Native vision-language 4B, Apache-2.0, thinking default and explicit template branch. Author benchmark tables motivate a candidate, not a same-protocol business win or M5 memory/gradient result. No numerical claims imported, weights downloaded or model executed.

<a id="qwen35-4b-mlx-selection-oct27"></a>
## Community Qwen3.5-4B MLX quantization config and provenance gap

- Source: https://huggingface.co/mlx-community/Qwen3.5-4B-4bit/blob/0e7ffd5c629ef7719d4cbc04069232580bfa9d9c/config.json
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-27
- Source revision: `0e7ffd5c629ef7719d4cbc04069232580bfa9d9c`
- Note: Read public API file list, config, tokenizer_config and chat_template.jinja. Preserves qwen3_5/vision_config and affine 4-bit group64. No README/LICENSE file or API license declaration found in this snapshot. Trace upstream provenance and retain official notices before future use; do not treat original Apache terms as a complete conversion audit. No weight-byte/quantization-fidelity/capacity test.

<a id="mlx-vlm-qwen35-visual-oct27"></a>
## MLX-VLM Qwen3.5 image embeddings and visual fusion

- Source: https://github.com/Blaizzy/mlx-vlm/blob/2ceff4c14b991370a459d14eb49d1bedf4fb9e84/mlx_vlm/models/qwen3_5/qwen3_5.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-27
- Source revision: `2ceff4c14b991370a459d14eb49d1bedf4fb9e84`
- Note: Read distinct Qwen3.5 vision tower, pixels/grid processing, embedding insertion, image-feature/token count rejection and language-model construction. Do not transfer a Qwen3-VL model path merely from naming. Source inspection only; no checkpoint loaded or image forward/backward run.

<a id="mlx-vlm-qwen35-language-oct27"></a>
## MLX-VLM Qwen3.5 training-mode DeltaNet dispatch and adapter module names

- Source: https://github.com/Blaizzy/mlx-vlm/blob/2ceff4c14b991370a459d14eb49d1bedf4fb9e84/mlx_vlm/models/qwen3_5/language.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-27
- Source revision: `2ceff4c14b991370a459d14eb49d1bedf4fb9e84`
- Note: Read training use_kernel=not self.training dispatch and hybrid layer implementation, including DeltaNet in_proj_qkv/z/b/a and out_proj. Adapter targets must reflect actual modules, not copied q/k/v/o-only lists. MTP is not a decision classifier. No local gradient, model quality or hardware claim.

<a id="mlx-vlm-qwen35-delta-oct27"></a>
## MLX-VLM Qwen3.5 chunked/reference training path

- Source: https://github.com/Blaizzy/mlx-vlm/blob/2ceff4c14b991370a459d14eb49d1bedf4fb9e84/mlx_vlm/models/qwen3_5/gated_delta.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-27
- Source revision: `2ceff4c14b991370a459d14eb49d1bedf4fb9e84`
- Note: Read gated_delta_update use_kernel=False fallback to chunked/reference MLX ops. Architecture is not sufficient grounds to assert inference-only. No tests from this third-party package were executed; actual full-checkpoint image-conditioned gradients remain a gate.

<a id="jev-decision-2b-selection-oct27"></a>
## Jev-Decision Qwen3-VL-2B pointer-head precedent and release limits

- Source: https://github.com/yeyan00/Jev-Decision/blob/811bf5083a12622b0e63a98084312a91ac119b80/README.md
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-27
- Source revision: `811bf5083a12622b0e63a98084312a91ac119b80`
- Note: Read README, pinned tree, config and MIT LICENSE. Declares Qwen3-VL-2B, frozen-vision LoRA, dynamic pointer readout and image/text inputs. No public checkpoint/evaluation-result artifacts found in inspected tree; README gives no numeric outcome/checkpoint link. PyTorch/CUDA-oriented, not native MLX. ScienceQA mixture imposes NC/SA concerns on derived weights. This newly audited precedent does not retrospectively justify an earlier choice or prove business gains.

<a id="jev-decision-2b-data-oct27"></a>
## Jev-Decision image processor and visual tensor collator

- Source: https://github.com/yeyan00/Jev-Decision/blob/811bf5083a12622b0e63a98084312a91ac119b80/src/jev_decision/data.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-27
- Source revision: `811bf5083a12622b0e63a98084312a91ac119b80`
- Note: Read local-image message construction, processor.apply_chat_template and concatenation of pixel_values/image_grid_thw into model batches. Actual image path in code, not compatibility inference; no data downloaded or samples run.

<a id="jev-decision-2b-loss-oct27"></a>
## Jev-Decision visual backbone, pointer loss and frozen-vision LoRA code

- Source: https://github.com/yeyan00/Jev-Decision/blob/811bf5083a12622b0e63a98084312a91ac119b80/src/jev_decision/model.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-27
- Source revision: `811bf5083a12622b0e63a98084312a91ac119b80`
- Note: Read AutoModelForImageTextToText, multimodal_inputs forwarding, final hidden-state decision/option pointer readout, hard/soft CE, freeze/head/LoRA and save code. This supports an inspectable implementation, not a completed model release or measured effect. No code executed.

<a id="jev-decision-2b-train-oct27"></a>
## Jev-Decision optimization entry for head/LoRA training

- Source: https://github.com/yeyan00/Jev-Decision/blob/811bf5083a12622b0e63a98084312a91ac119b80/src/jev_decision/train.py
- Kind: `repository`; review depth: `content_reviewed`; reviewed: 2026-10-27
- Source revision: `811bf5083a12622b0e63a98084312a91ac119b80`
- Note: Read configured processor, trainable parameters, AdamW and accelerator.backward(loss), head/LoRA stages and validation selection. Code-level trainability differs from published weights/results, Mac support and local reproduction. No training run.

