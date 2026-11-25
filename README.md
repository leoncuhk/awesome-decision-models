# Awesome Decision Models [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**Models, methods and evidence for reliable bounded decisions in AI systems — organized by the problems that matter for enterprise LLM applications.**

[简体中文](README.zh-CN.md) · [Problems](#problem-map) · [Playbooks](#playbooks) · [Landscape](docs/landscape.md) · [Model cards](docs/models.md) · [Evidence](docs/evidence.md) · [Methodology](docs/methodology.md)

Decision models — popularized by TypeSafe's Jev in September 2026 — typically return **typed distributions over supplied options**. Direct readout is common; reasoning, per-question passes and service orchestration vary by product. The new thing is the output contract: it makes bounded judgments priceable, calibratable and gateable. This repository asks one question: **which method delivers acceptable outcomes at acceptable risk and total cost for a given decision?**

Review batch 2026-11-25: 100 resources, 38 core model families, 46 evidence records. Source review only; **nothing here is independently reproduced yet.** Inclusion is not endorsement.

## How this repository is organized

| Layer | Answers | Where |
| --- | --- | --- |
| Problems | What is known, what is open, how confident we are | [problems/](problems/) — one file per problem: judgment, evidence, counter-evidence, open experiments (Chinese) |
| Playbooks | How to do it in an enterprise | [playbooks/](playbooks/) — general pipeline plus scenario guides (Chinese) |
| Reference | Facts to look up | [landscape](docs/landscape.md), generated [model cards](docs/models.md), [evidence](docs/evidence.md), [sources](docs/sources.md) |
| Rules | How evidence is judged | [methodology](docs/methodology.md), [contributing](CONTRIBUTING.md) |

<a id="problem-map"></a>
## Problem map

Maturity: **consensus** = multiple sources incl. third-party controls; **supported** = controlled but narrow evidence; **open** = key evidence missing.

| | Problem | Current judgment | Maturity |
| --- | --- | --- | --- |
| **Judgment** | [P01 Output contract and readout](problems/P01-output-contract.md) | Specify the output contract; simple heads are a supported baseline, not universally equivalent | supported |
| | [P02 Learning signal for adaptation](problems/P02-learning-signal.md) | Direct CE/BCE supervision is the default; RL, distillation, soft targets must prove gains | supported |
| | [P03 Read once or reason](problems/P03-read-or-reason.md) | Reasoning and reference guidance can help; measure task-specific quality and full cost | open |
| **Probability → decision** | [P04 Confidence semantics and serving fidelity](problems/P04-confidence-fidelity.md) | `confidence` is an interface field; recalibrate per task, returned object and serving path | consensus |
| | [P05 Policy-level risk and drift](problems/P05-policy-risk.md) | Certify the acceptance policy, not per-item confidence; drift voids guarantees | theory consensus / practice open |
| | [P06 Missing options and candidate coverage](problems/P06-candidate-coverage.md) | Softmax cannot detect all-wrong candidates; NONE collapses under hard negatives | supported |
| **System** | [P07 Reading right, acting wrong](problems/P07-state-and-action.md) | Probe facts and actions separately to distinguish evidence, contract and model failures | supported |
| | [P08 Dynamic skill and path loading](problems/P08-skill-loading.md) | Selection errors, not context length; optimize loader recall with fallback | supported |
| | [P09 System-1 as judge and evaluator](problems/P09-judge-layer.md) | Cheap first-stage judging plus escalation is a candidate; production maturity remains unproven | supported |
| | [P10 Partial feedback and heterogeneous repair](problems/P10-repair-actions.md) | Ask, fetch, re-retrieve and defer are different interventions; research frontier | open |
| **Multimodal** | [P11 Multimodal post-training](problems/P11-multimodal.md) | Vision is often not actually trained; validate the visual path before comparing quality | supported |
| **Selection** | [P12 Fragmented benchmarks and selection economics](problems/P12-benchmarks-and-selection.md) | Rank is not a selection signal; gate on license, trainability, hardware, serving fidelity | consensus |

<a id="playbooks"></a>
## Playbooks

| Playbook | Use when |
| --- | --- |
| [General pipeline](playbooks/decision-pipeline.md) | Any enterprise decision: contract → method and base → data → training → acceptance |
| [Multimodal post-training](playbooks/multimodal-posttraining.md) | Screenshots plus intent labels; local Mac training; G0–G4 gates |
| [Skill routing selector](playbooks/skill-routing.md) | Service agent with tens of skills; loader training, staged experiments H1–H6 |

## Core models

Mechanism and suggested experiment only; version boundaries, licenses and limitations are in the [model cards](docs/models.md). No combined leaderboard: zero-shot, fine-tuned and Best-of-N results answer different questions.

| Model | Mechanism | Suggested experiment |
| --- | --- | --- |
| [Jev / TypeSafe](https://typesafe.ai) · [card](docs/models.md#jev) | Hosted typed judgments: probabilities over supplied choices, propositions and ordinal rubrics. | Managed typed-judgment comparator or frozen semantic-feature generator; compare supervised baselines under the same task and label policy. Keep deterministic business rules in code; separately validate semantic judgments. |
| [Laya classic encoders (package 0.5 defaults to Vega)](https://github.com/NandhaKishorM/laya) · [card](docs/models.md#laya) | Classic 421M / 322M encoder checkpoints with dynamic option heads; package 0.5 now defaults to a separate Vega frozen-reader engine unless a classic checkpoint is selected. | Use explicitly selected classic encoders as low-resource supervised controls; consider Vega fitted-head learning as a separate hypothesis with its own baseline and held-out acceptance. |
| [Kev](https://github.com/jaredpalmer/kev) · [card](docs/models.md#kev) | Qwen-based typed decision family with a dynamic pointer head; Kev 1.0 freezes existing checkpoints as a release baseline. | An inspectable starting point for domain-supervised decision models. |
| [Contrastive Language Models (CLM)](https://github.com/Contrastive-LM/CLM) · [card](docs/models.md#clm) | Separate state and action representations with learned projection heads on a frozen language-model encoder. | Reusable candidate catalogs, tool selection and domain-trained Best-of-N selection. |
| [Bespoke Nimble](https://github.com/bespokelabsai/nimble) · [card](docs/models.md#nimble) | Open Qwen3.5-9B supervised decision adapter, distinct from the later Nimble hosted v4/v4.1 service. | A transparent baseline for evidence-sensitive judgments and minimal-edit training examples. |
| [GLiNER2.5-Decide](https://huggingface.co/fastino/GLiNER2.5-Decide-1B) · [card](docs/models.md#gliner-decide) | Schema-conditioned local classification with runtime labels and multiple decision heads. | Compact operational classification; inspect the runtime for supported cross-field constraints. |
| [GLiClass (v4 family; v4.1 Edge metadata only)](https://github.com/Knowledgator/GLiClass) · [card](docs/models.md#gliclass) | Label-conditioned classification family: v4 adds decoder-KV/label scoring and multimodal Qwen variants; v4.1 Edge is an incompletely documented artifact. | Dynamic intent/label classification comparator, choosing single-label or multilabel semantics and measuring task-specific calibration. |
| [jevos (current v5; historical v2)](https://github.com/feder-cr/jev) · [card](docs/models.md#jevos) | Local CPU typed decisions in a Jev-shaped API: v5 adds documented choice and early score support alongside yes/no, with OpenVINO INT8 and GGUF assets. | A CPU inference comparator for short policy/triage decisions; validate each supported type and the exact released artifact before considering adaptation. |
| [Clef / Clef-Flash / Clef-Omni](https://huggingface.co/Cloudflare/clef) · [card](docs/models.md#clef) | Cloudflare typed-decision family: dense Clef/Flash and October 9 Clef-Omni use joint schema scoring; Clairic is a separate extraction family. | Compare bounded judgments using required text/image/audio/video evidence, at matched workload risk and full-system cost. |
| [Strands Decider (v1 pointer / v2 code readout)](https://github.com/strands-labs/strands-decider) · [card](docs/models.md#strands-decider) | Qwen / Gemma decision family: v1 adapter-and-pointer releases and November 17 Gemma 4 E2B v2 merged code-readout release have different training and serving contracts. | Compare v1 and v2 on the same bounded text decisions; audit the actual domain-training starting point and exported inference path before selecting a recipe. |
| [Perplexity Decider (current v1.3; archival v1 / v1.1 / v1.2)](https://huggingface.co/perplexity-ai/pplx-decider-v1.3) · [card](docs/models.md#pplx-decider) | v1.3 typed-decision and optional span-location family; 27B Qwen3.8 and distilled Flash 4B Qwen3.5, with distinct earlier versions. | A self-hosted comparator for text/image judgments after task-specific validation. |
| [Microsoft-Decision-1.1](https://ai.azure.com/catalog/models/Microsoft-Decision-1.1) · [card](docs/models.md#ms-decision) | GA hosted typed decisions on Gemma4, including images. | Compare classification, routing and rubric judgments. |
| [OpenAI Decisions API / GPT-6 Luna](https://developers.openai.com/api/docs/guides/decisions) · [card](docs/models.md#openai-decisions) | GA typed-judgment API for text and images. | Managed classification, routing and ordinal scoring. |
| [Google Gemini Decision 1 / Decisions API](https://aistudio.google.com/docs/models/gemini-decision-1) · [card](docs/models.md#gemini-decision-1) | November11 hosted model for text, image, audio, video and PDF judgments with shared-input isolated questions. | Compare multimodal triage, media policy checks and routing at fixed evidence, risk and complete cost. |
| [Nace Drex v1.5 / v2.0 / Max v1](https://github.com/nace-ai/drex-decision-models) · [card](docs/models.md#drex) | Drex family: text pointer-head v1.5/v2.0 and dense 27B multimodal Max v1 with a fixed 255-code readout. | Compare local text/JSON decisions and Max CUDA image judgments; match precision, readout, evidence and context before comparing releases. |
| [vLLM-SR D3 / Turbo / Ultra / D3.1-nano](https://huggingface.co/collections/vllm-sr/decision-30) · [card](docs/models.md#decision3) | Multimodal typed-decision family with distinct classic per-question, Turbo/Ultra shared-state and November 12 D3.1-nano releases. | Matched text/image/video decision comparisons, with small D3.1-nano as a separate capability candidate and Ultra as a larger reference; verify adaptation separately. |
| [Intern-Decision](https://github.com/internlm/Intern-Decision) · [card](docs/models.md#intern-decision) | Qwen3.5 multimodal 0.8B/2B/4B family; multiple typed fields scored from one causal masked assistant skeleton. | Compare multi-field cost and field/order sensitivity against per-question models; test image-grounded judgments. |
| [Verdict / OpenJev](https://github.com/Heman10x-NGU/Verdict-open-jev) · [card](docs/models.md#verdict) | 151M ModernBERT/GLiClass candidate classifier with an explicit insufficient-evidence option and per-K calibration. | Compact intent classification and missing-option tests; compare native serving probabilities with the exact evaluation renderer/calibrator. |
| [StartLux-Decision v1.1 (Instant / AutoThink)](https://github.com/StartLuxLabs/StartLux-Decision) · [card](docs/models.md#startlux-decision) | Option-letter LM readout: Instant uses prompt-bidirectional full-attention; causal AutoThink conditionally reasons and fuses two distributions. | Compare one-pass versus selective computation on evidence-complete decisions, at matched risk and complete cost; commercial use requires separate weight authorization. |
| [Baseten mammoth-1 / elephant-1 / joey-1](https://huggingface.co/baselabs/mammoth-1) · [card](docs/models.md#baseten-decision) | Qwen-based 27B / 9B / 2B typed-decision family using shared-prefix evidence and separate question readouts; Joey is the smaller October sibling. | Matched independent-question comparisons across 2B / 9B / 27B, keeping public-suite and replicated-index evaluations separate. |
| [Jeffan (31B-1710 / 4B-2010 / 9B and 27B-1211)](https://huggingface.co/tattrongvu/Jeffan-31b-1710) · [card](docs/models.md#jeffan) | Text decision releases with distinct compute policies: older Gemma 31B selective rereading and newer Qwen 9B / 27B bidirectional code-readout models with optional layer loops. | Compare bounded text decisions at fixed loop/reread policies and full request cost, then validate domain/language transfer separately. |
| [SII-Decision (4B / 27B)](https://github.com/amazingljy1206/SII-Decision) · [card](docs/models.md#sii-decision) | Reasoning-to-readout self-distillation into non-generative typed decisions; open 4B and 27B releases. | Capability and distillation comparator; evaluate exact released checkpoints separately from enterprise adaptation. |
| [GLiDE / Fastino](https://fastino.ai/blog/glide-decision-model-family) · [card](docs/models.md#glide) | Five-size open-weight decision family plus a native customer training API. | Add a small-model/readout comparator and, if data may leave the enterprise, a managed domain-adaptation route. |
| [Liquid d1 / d1.2](https://docs.liquid.ai/lfm/models/decision-models) · [card](docs/models.md#liquid-d1) | Open d1-2B/Omni-2B and separate hosted d1.2/ultra decision products. | Study a small non-Qwen implementation and multi-label contract; evaluate hosted and local artifacts separately. |
| [Mapika Decider](https://github.com/Mapika/decider) · [card](docs/models.md#mapika-decider) | Open typed-decision family with supervised training/data builders; previously sourced but missing a core catalog entry. | Compare an inspectable supervised implementation and its per-type calibration; study environment learning only with matching feedback. |
| [RSI-Jev v7.0-VL](https://github.com/Shanghua-Gao/RSI-Jev) · [card](docs/models.md#rsi-jev) | Open Qwen decision implementation with public full training code and a truncated3B derivative. | Prioritize code inspection and a small own-label comparison, including simple readout/LoRA controls. |
| [Jeff 1.1 / j-geuter](https://github.com/j-geuter/Jeff) · [card](docs/models.md#jgeuter-jeff) | Open decision training implementation, distinct from Jeffan; published weights/data have noncommercial restrictions. | Study data/training mechanics; for commercial use train an appropriately licensed base on authorized own data. |
| [JAD-S1 v0.5](https://huggingface.co/DreamBlooms/JAD-S1-7B-A1B-v0.5) · [card](docs/models.md#jad) | Diffusion/MoE-based closed-option decision adapter with single-mask readout. | A different-backbone/readout research control if the local task justifies it. |
| [H2O Lightning 4B](https://huggingface.co/h2oai/h2o-lightning-4b) · [card](docs/models.md#h2o-lightning) | Open Qwen4B typed-decision engine; this is a catch-up inclusion, not a November20 weight release. | Small typed-inference comparator after protocol and prompt settings are fixed. |
| [MNN-Pocket-0.3B-Dec](https://huggingface.co/taobao-mnn/MNN-Pocket-0.3B-Dec) · [card](docs/models.md#mnn-pocket-dec) | Small Chinese/English choice, proposition and ordinal pointer-head package. | Very small Chinese readout/cost control, paired with a trained multilingual encoder. |
| [IBM Granite Switch / decision adapter](https://huggingface.co/blog/ibm-granite/granite-switch-4-1) · [card](docs/models.md#granite-switch) | A reusable decision adapter alongside chat, guard and ASR capabilities on Granite4.1. | Study decision/chat sharing and cache-aware adapters when a larger resident base is justified. |
| [Ant Digital LingDT-Decision-1.0](https://maas.antdigital.com/models/modelservice-1792325631780001741) · [card](docs/models.md#ant-lingdt) | Hosted typed decision service with native question-dependency DAG. | Domestic hosted contract/dependency reference; evaluate access and data governance separately. |
| [Respan Span-02](https://www.respan.ai/blog/introducing-span-2) · [card](docs/models.md#span-02) | Open decision serving artifact with a specialized quantized Rust/CUDA engine and optional reasoning. | Study self-hosted inference and budgeted reasoning as separate serving controls. |
| [Decisio tuned v3 / Tachara AI](https://github.com/aminry/decisio) · [card](docs/models.md#decisio) | November20 Gemma12B tuned release with calibrated and commit serving policies and multiple precision ports. | A fresh serving/readout comparator; evaluate calibrated policy, commit policy and calculator under the same contract. |
| [Valen-Decision1.5](https://github.com/Valen-Team/Valen) · [card](docs/models.md#valen-decision) | Multimodal typed-decision family with native published-checkpoint domain training, separate from its ONNX/GGUF/ANE conversions. | Prioritize an inspectable native-checkpoint LoRA comparator for proprietary data on compatible hardware; keep original and direct CE controls. |
| [LemonDecider 4B (inclusionAI / Ant)](https://huggingface.co/inclusionAI/LemonDecider) · [card](docs/models.md#lemondecider) | Open Qwen3.5-4B typed model with a255-option readout, inference code and a1.2M-row training mix; complete public trainer not located in this review. | Open4B inference comparator and license-reviewed replay-data source; direct checkpoint fine-tuning requires a verified training loader and export path. |
| [Adjudex4B v7 / NewsBang](https://huggingface.co/newsbang/adjudex-4b-v7) · [card](docs/models.md#adjudex) | Qwen3.5-4B typed readout with public full-weight training/continuation code; a high-scoring candidate in the fixed small-model screen. | Prioritize native continuation qualification and frozen domain evaluation alongside another trainable4B candidate; verify held-out gains before scaling full-weight training. |
| [Chinese Decision Pointer4B](https://huggingface.co/quincyqiang/chinese-decision-pointer-4b) · [card](docs/models.md#chinese-decision-pointer) | Qwen3.5-4B candidate-pointer model with Chinese training material and public LoRA implementation. | Include as a Chinese-oriented LoRA experiment alongside the high-scoring Adjudex and the Valen training control, after exact native loader/save/serve verification. |

## Baselines worth keeping

A new training label does not make a familiar baseline obsolete.

- **[SetFit](https://github.com/huggingface/setfit)** — Few-shot sentence-transformer adaptation followed by a classification head.
- **[Qwen3-Reranker](https://huggingface.co/Qwen/Qwen3-Reranker-0.6B)** — Task-trained query/document reranking.
- **[Outlines](https://github.com/dottxt-ai/outlines)** — Constrained structured output for ordinary language models.
- **[TabICLv2](https://arxiv.org/abs/2602.11139)** — A tabular foundation model for classification and regression.
- **[FluidUse / decision-model Core ML deployment](https://github.com/FluidInference/FluidUse)** — Apple deployment resource with native Swift managers and Python-assisted Core ML bridges, including Decision 3.0.
- **[Semantic features + supervised predictor](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery)** — LLM-proposed questions and Jev judgments turn text into features for a supervised CatBoost predictor.
- **[ezjev text candidate-logit LoRA](https://github.com/everettjf/ezjev/tree/8b3d88957c0795bea160c8fbc9c6d2a54b051136)** — Inspectable per-question candidate CE+Brier, replay and temperature fitting on a Qwen3.5 text-training path.
- **[decision-pacman decision distillation](https://github.com/grapeot/decision-pacman/tree/593ed1f59f4f97ad0bda7287ff304e9667360089)** — Text-state teacher/simulator labels train a small option-distribution LoRA student.
- **[Qwen VLM image-supervised SFT / LoRA](https://github.com/QwenLM/Qwen3-VL/blob/96588727e44c78b25ba03ea03b8e12f7e64fd0da/qwen-vl-finetune/README.md)** — Inspectable image-supervised routes: official QwenVL, ms-swift Qwen3.5, and pinned MLX-VLM image-conditioned language adapters for Mac experiments.
- **[DFIP / Decision-Focused Inference Path](https://arxiv.org/html/2610.36804v1)** — Paired native-baseline systems study audits resident acceleration, exposed answers and external arrivals separately.
- **[DICE / Direct Item Choice Estimation](https://arxiv.org/html/2610.34124v1)** — Supervised item choice with candidate-isolated shared-prefix attention and separately calibrated recommendation confidence.
- **[Clairic / Clairic-Flash (typed extraction)](https://blog.cloudflare.com/open-clairic/)** — Adjacent typed extraction/estimation family: November 18 redesign uses parallel slot autoregressive extraction plus specialized numerical heads, separate from Clef closed-option decisions.
- **[Unsloth decision-model training (FastDecisionModel / DecisionTrainer)](https://unsloth.ai/docs/basics/train-your-own-decision-model-with-unsloth)** — General trainer that turns a fine-tunable LLM, including Qwen3.5 VLMs, into a Clef-style joint-head decision model, with calibration, merged export, a local Jev-compatible Decision API and an Apple Silicon (MLX) LoRA path.
- **[SGLang /v1/decisions (zero-training readout)](https://docs.sglang.io/docs/supported-models/decision_models)** — Native SGLang endpoint that turns any chat model into a typed-decision service by reading single-token label log-probabilities after one prefill per question.
- **[NanoJev](https://github.com/TianyuCodings/NanoJev)** — MIT Qwen3-0.6B decision-head model with dynamic 2-255 candidates and an end-to-end training pipeline.

## Routing and learning from outcomes

- **[RouteLLM](https://github.com/lm-sys/RouteLLM)** — Routes between stronger and cheaper language models using learned signals.
- **[LLMRouter](https://github.com/ulab-uiuc/LLMRouter)** — Research infrastructure for building and comparing routing strategies.
- **[Vowpal Wabbit](https://github.com/VowpalWabbit/vowpal_wabbit)** — Online-learning and contextual-bandit tooling.
- **[Parlant rule matching / Jev integration](https://github.com/emcie-co/parlant)** — Pinned CX engine implementation batches per-rule propositions over shared state and resolves declared rule relationships.
- **[Modem Smart Triggers](https://modem.ai/blog/smart-triggers)** — Implementer-described product gates event-triggered agent runs with exact filters and a semantic condition.
- **[Enterprise multi-turn intent learning (Amazon study)](https://aclanthology.org/2026.customnlp4u-1.8/)** — Evidence-guided and self-critique teacher labeling, followed by separate domain/intent/issue RoBERTa classifiers for real ecommerce conversations.
- **[JevAgentHarness / AgentDecisionBench](https://github.com/JevAgentHarness/JevAgentHarness)** — Delegates an agent's multiple-choice steps to a decision model with per-choice confidence thresholds fitted on the agent's own trajectories, and trains a 4B model on post-mistake states.
- **[JevRSI (System-2 improves the System-1 harness)](https://github.com/usail-hkust/JevRSI)** — A System-2 LLM asynchronously writes procedures, state-memory programs and world-model programs that feed a fast decision model, instead of taking over decisions.

## Reliability

- **[MAPIE](https://github.com/scikit-learn-contrib/MAPIE)** — Prediction-set, uncertainty and conformal-risk tooling.
- **[Calibration and Risk-Budgeted Decisions with System One Models](https://arxiv.org/html/2610.19811v1)** — Preprint separates probability calibration from fixed-sequence LTT certification of a binary decision policy under a risk budget.
- **[RouteGuard / Cost-Aware Abstention](https://arxiv.org/html/2610.31657v1)** — Calibration-selected cost-aware ticket routing separates probability calibration from error discrimination.
- **[Rep2Act / VAD-R](https://arxiv.org/html/2609.32653v1)** — Evidence-gap annotation and answerability-to-action alignment; newly cataloged Sep26 preprint.

## Evaluation

- **[HF-hosted Decision Index (archival releases and live board)](https://huggingface.co/spaces/multimodalart/jev-decision-index)** — A broader decision benchmark index with explicit aggregation rules.
- **[Nimble public evaluations](https://github.com/bespokelabsai/nimble/blob/62076b4f2d365b5879dafcf7f6dd072a1fe76df7/docs/PUBLIC_BENCHMARKS.md)** — Human-reference subsets, paired comparisons and calibration reporting.
- **[Decision-model benchmark](https://github.com/nibzard/decision-model-benchmark)** — Third-party code and protocols for decision-model comparisons.
- **[Financial-document decision tests](https://insights.ml4trading.io/p/testing-jev-on-financial-documents)** — Original-evaluator comparison of Jev and supervised text/TF-IDF models on earnings, 8-K labels and SEC follow-up.
- **[MIRE / WWW2025 multimodal intent competition](https://github.com/liujunwen23/MIRE/tree/d101287af90d114c5bf0cbfbd56fe9c52358e3bb)** — Parallel 23-class scene and 23-class dialogue-intent tasks, official full-SFT baseline, and sourced gold/silver/bronze methods and semifinal scores.
- **[DecisionPivot v1.1](https://huggingface.co/datasets/startlux-models/DecisionPivot/tree/b6a65d303f3f8689d293869aff3db41f944984c6)** — 13 generated contrast families, programmatic labels and public generator/solver/scoring assets; separate reused-public-task reference track.
- **[Artificial Analysis Decision Index](https://artificialanalysis.ai/methodology/decision-index)** — Hosted-and-open decision-model index; v2 (Nov8) scores 50×(1+accuracy−Brier), so calibration enters the headline number, and moves 45% of items to private data.
- **[Commit or Abstain? Missing Legal Authority](https://arxiv.org/html/2610.29961v1)** — Third-party provider comparison exposes wrong acceptance versus unnecessary abstention on constructed CaseHOLD.
- **[VLTest joint image-text testing](https://arxiv.org/html/2610.30794v1)** — Oct22 method uses matched original/image/text/joint controls and checks that mutations preserve the expected answer.
- **[Beyond Ranking: calibrated relevance scoring](https://arxiv.org/html/2611.11480v1)** — Same-candidate relevance ranking and held-out probability calibration.
- **[System1 perturbation and question-interference audit](https://arxiv.org/html/2611.12521v1)** — Audits distribution-derived confidence, bundled questions and perturbation explanations.
- **[Decision models for RAG conflict typing](https://arxiv.org/html/2610.36915v1)** — Flat conflict classification, decomposition and confidence-gated cascades.
- **[Entity matching using decision models](https://arxiv.org/html/2610.34626v1)** — Zero-shot record-pair matching with prompt, robustness and cascade comparisons.
- **[Jev time-series decision benchmark](https://arxiv.org/html/2610.33410v1)** — Evaluates serialized sequences, event types and directional predictions.
- **[Confidence Is Not a Promise / Typed Deciders Audit](https://arxiv.org/html/2610.36311v1)** — Reference audit separates confidence ordering, selective-accuracy promises and their failure under shift.
- **[Entagl customer-routing replay](https://www.entagl.com/blog/typesafe-jev-benchmark-ai-decision-models)** — Implementer-reported labeled decisions and replay of historical customer-routing decisions.
- **[JEVal v2](https://arxiv.org/html/2610.03935v2)** — Multidomain English/Chinese evaluation of local typed decisions, reasoning limits and workflow composition.
- **[To Jev or Not to Jev (System-1 models as LLM judges)](https://arxiv.org/abs/2611.00505)** — Pre-registered comparison of 14 System-1 decision models with four generative judges on eleven judge benchmarks, including reference-guided judging, calibration and injected-instruction robustness.
- **[Reading Right, Acting Wrong (agent-loop decision diagnosis)](https://arxiv.org/abs/2610.18579)** — Pairs each agent next-action question with independent factual probes on the same state to separate misreading from wrong action.
- **[System1-Arena](https://arxiv.org/abs/2610.21244)** — Benchmark of nearly 100K questions asking which decisions can be left to System-1 models, spanning classification and agentic tasks.

## Foundations

Reading order: probability quality → abstention → executor handoff → risk control.

- **[Strictly Proper Scoring Rules (2007)](https://doi.org/10.1198/016214506000001437)** — Why log loss and other proper scores target truthful distributions.
- **[On Calibration of Modern Neural Networks (2017)](https://proceedings.mlr.press/v70/guo17a.html)** — Empirical calibration and post-hoc temperature scaling.
- **[Selective Classification (2017)](https://arxiv.org/abs/1705.08500v2)** — Classification with abstention and risk/coverage trade-offs.
- **[Learning to Defer to an Expert (2020)](https://proceedings.mlr.press/v119/mozannar20b.html)** — Jointly learn prediction and handoff to an expert.
- **[Conformal Risk Control (2022; reviewed v4)](https://arxiv.org/abs/2208.02814v4)** — Calibrate risk-controlling procedures under stated conditions.
- **[Non-Monotonic Conformal Risk Control (2026)](https://arxiv.org/abs/2602.20151v1)** — Extends the risk-control discussion beyond monotone losses.
- **[Proper Scoring Rules: 2026 review](https://doi.org/10.1146/annurev-statistics-042424-050626)** — A recent review of estimation and forecast evaluation.
- **[Causal Learning to Defer (AAAI 2026)](https://ojs.aaai.org/index.php/AAAI/article/view/39493)** — Studies handoff learning with hidden confounding.
- **[Jev in the Wild (2026)](https://arxiv.org/abs/2609.30216)** — Data-driven survey and analysis of 2,170 public GitHub Jev projects, including early growth, application domains and decision-use patterns.
- **[Post-Rationale Distribution Optimization (PRDO v2)](https://arxiv.org/html/2609.38850v2)** — Proper-score optimization of each sampled rationale’s answer distribution for selective prediction.

## Related lists

- **[Awesome System One](https://github.com/andyrewlee/awesome-system-one)** — Closest ecosystem list; useful for discovery.
- **[Awesome Jev 中文](https://github.com/yzfly/awesome-jev-zh)** — Chinese-language Jev ecosystem resources.
- **[Awesome LLM Routing and Cascading](https://github.com/ymoslem/awesome-llm-routing-cascading)** — Specialist routing and cascading bibliography.
- **[Awesome Conformal Prediction](https://github.com/valeman/awesome-conformal-prediction)** — Specialist uncertainty and conformal prediction resources.
- **[Awesome Martech AI](https://github.com/leoncuhk/awesome-martech-ai)** — Marketing data, intelligence, decision, activation and measurement resources with applied playbooks.

## Contributing

Canonical data lives in [`data/`](data/); README, model cards, evidence and sources are generated by `python3 scripts/render.py`. A new source is worth adding only if it changes a problem's judgment, evidence or open experiment — see [CONTRIBUTING](CONTRIBUTING.md). Changes are logged in [CHANGELOG](CHANGELOG.md).

Original code and curation text: [MIT](LICENSE). Linked projects, weights, datasets and papers keep their own licenses.
