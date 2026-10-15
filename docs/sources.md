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

