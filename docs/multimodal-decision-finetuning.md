# Fine-tuning multimodal decision models: research and acceptance plan

[简体中文](multimodal-decision-finetuning.zh-CN.md) · [Home](../README.md) · [Selection guide](selection-guide.md#image-intent-adaptation) · [Evidence ledger](evidence.md)

Sources reviewed: 2026-10-17. This is a testable research design for general multimodal customer-support intent recognition. No model was trained and no production benefit was demonstrated here. Public implementations, author reports and proposed experiments are distinguished below. Image understanding, intent, calibration and abstention policy are separate questions.

**Research question.** Given domain images and the dialogue visible at decision time, how much intent recognition can be accepted under predefined consequential-error risk and complete-cost limits, while clarifying or handing off evidence-insufficient cases? Fine-tuning a decision model is one possible means, not the research goal. The scenario owner must set numerical risk, cost and minimum-useful-gain criteria before model/threshold selection; no universal pass line is assumed.

<a id="quick-route"></a>
## One-page experiment route

Use this route to test whether domain post-training improves a defined decision. **No candidate is a proven winner, and adaptation can reduce quality.** The [reading list](#reading-list) separates peer-reviewed methods, preprints and engineering assets.

| Gate | Concrete deliverable before continuing | Continue / stop |
| --- | --- | --- |
| 1. Contract and split | Evidence available at decision time, independent label agreement, labels/unknowns/error costs/rights; train, development, calibration and final test split by group/time/duplicate family. See [data](#3-resolve-data-and-label-uncertainty-first). | Resolve label ambiguity and leakage before training; future context never enters an earlier input. |
| 2. Baselines and candidate gates | Frozen zero/few-shot VLM, VLM with available page guidance/retrieval, D3/Intern inference where supported, text-only and OCR+text; record label access and total budget. See [comparisons](#1-freeze-the-question-and-comparisons) and [candidate gates](#candidate-gates). | Missing evidence calls for retrieval/clarification; select trainable paths by verified support, not an assumed quality ranking. |
| 3. Small learning check | Actual trainable parameters/gradients, tiny-subset fit, image removal/swaps, token/readout alignment. See [visual path](#4-verify-the-visual-path-and-objective-before-training). | Fix failed paths first; tiny-fit success is not generalization. |
| 4. Controlled adaptation | B2 short-label SFT versus B3 candidate scoring on the same exact base/data/visual processing/budget; finite dev search and learning curves. See [order](#5-experiment-order-and-stopping-rules). | Cross-backbone comparisons answer system selection; retain normal replay and generic regression cases. |
| 5. Calibration and rejection | Separate calibration, actual routing/selection policy, unknown/OOS and clarification; freeze gate/temperature/thresholds. See [acceptance](#6-accept-quality-risk-and-cost-together). | A probability/confidence field is not a risk guarantee; use only a method whose assumptions match the target risk. |
| 6. Frozen acceptance | Paired grouped test results/uncertainty, consequential errors, coverage, full cost and train/export/serving parity. | Continue only for a predefined coverage gain over the strongest frozen baseline within critical-risk/cost limits; otherwise correct evidence/data/engineering or stop. |

Record each gate's artifacts in a versioned experiment manifest. This is a design to implement after rights and runtime verification, not an untested command sequence.

## 1. Freeze the question and comparisons

The task is intent recognition from domain images and contemporaneous dialogue, with clarification or human handoff when evidence cannot identify the request. Compare to the strongest frozen baseline under predefined risk/cost conditions; post-training, short labels and direct candidate scoring are candidate means whose effects must be tested.

Label **visible facts**, **the user's intent given contemporaneous context**, and **evidence sufficiency** separately. One screenshot can accompany different requests. Image categories are not automatically intent labels. Allow multiple intents, unknown, out-of-scope and clarification. Versioned page guidance/retrieval can supply background available at decision time; it cannot invent a missing user goal.

### Preregister falsifiable hypotheses

Start with identifiability and independent annotator agreement, then the strongest OCR/VLM/page-guidance/retrieval baseline. Only test adaptation after diagnosing a remaining domain-learning bottleneck. Predeclare the endpoint, group unit, splits, model-search budget, candidate policies and stop rules. Use development data for model/template/learning choices, independent calibration data for probability/policy fitting, and final testing only for acceptance.

| Hypothesis / paper-to-test link | Test that could refute it | Decision |
| --- | --- | --- |
| H1: images plus visible dialogue identify the intended labels; MIRE/EcomMIR and MIntRec2.0 motivate scene/intent/OOS separation. | Independent label disagreement or genuinely ambiguous same-image contexts remain after improving the contract; page guidance/retrieval does not supply the missing user intent. | Revise labels/evidence or clarify; do not scale training to hide non-identifiability. |
| H2: domain adaptation adds useful coverage over the strongest frozen baseline at critical-risk/cost limits; EcomMIR supplies a worked adaptation example, not this outcome. | Paired held-out coverage differences and uncertainty do not meet the predefined useful gain, or consequential errors/cost worsen. | Retain the stronger baseline or stop; include existing decision checkpoints as candidates only after their training path is verified. |
| H3: candidate scoring improves a declared quality/calibration/cost target versus short-label SFT; the readout/objective comparison motivates B2/B3. | Same exact base/data/scale/budget B2/B3 shows no useful benefit; a cross-backbone result does not answer this hypothesis. | Choose the simpler/stronger validated system; do not credit a readout for base/training-history changes. |
| H4: the selected policy uses image evidence and generalizes to new UI/time/language/OOS; visual feedback/judge papers and calibration/selective-risk work motivate checks. | Image-essential ablations, frozen shift sets or actual-policy risk/coverage/cost fail; judge agreement masks visual errors. | Fix evidence/path/data/thresholds or stop; a missing-evidence response is itself evaluated, not automatically safe. |

The primary endpoint is the change in accepted intent-label coverage relative to the strongest baseline under the predefined critical-risk constraint, accompanied by uncertainty, per-class errors and complete cost. Improved offline F1, easier implementation or lower calibration error alone does not establish success. The paper links propose mechanisms and tests; peer review is not evidence of success in this scenario.

**Engineering support and demonstrated quality are separate.** Qwen3.5 or another supported VLM with SFT/LoRA is a candidate experimental baseline, not a recommendation established to outperform D3. The primary sources reviewed here do not establish a direct multimodal comparison with the same task, data, scale and training/inference budget. Easier implementation is not effectiveness evidence. Keep D3 as a serious inference comparator on the same held-out image/context inputs; report any unequal target-label access or adaptation budget.

For mechanism attribution, B2 and B3 must start from the same exact backbone checkpoint and hold data, scale, visual processing and budget fixed. Comparing a newly adapted Qwen VLM with a released D3 model tests the complete systems under their disclosed conditions; it cannot isolate the benefit of a different readout, objective or training recipe. The B0/B1/B2/B3 sequence is an evaluation plan, not a quality ranking or a requirement to choose only Qwen3.5.

These are proposed experimental arms, not measured results:

| Arm | Inputs and training | Factor to isolate |
| --- | --- | --- |
| B0: OCR + text | Rules or ordinary supervised text classifier; retain a text-only arm | OCR, loss of layout, label separability and cost |
| B1: instruction VLM | Fixed-schema zero/few-shot short-label output | Whether images and context suffice; retrieval augmentation gets a separate arm |
| B2: VLM LoRA-SFT | Short structured labels on the same VLM backbone | Benefit of domain supervision; cap output length and count format failures |
| B3: candidate-distribution LoRA | Same backbone, data, image processing and budget as B2; read legal-option logits | Benefit of readout/objective, after verifying training/serving alignment |
| C: continue a decision checkpoint | Domain adaptation of an existing D3/Intern or other decision checkpoint only after verifying the image training path; compare to that same checkpoint without adaptation | Keep target splits and budget explicit. Cross-family results select systems; this is not the B2/B3 readout ablation. Vis text-only training is not a multimodal C arm |

Establish B0/B1/B2 before investing in B3. A short generated label may require only a few tokens, so removing decoding need not materially reduce end-to-end latency. Add a separate scene encoder or multistage classifier only when scene recognition is a demonstrated bottleneck.

## 2. What the public evidence supports

| Source and fixed revision | Inspected finding | Limit |
| --- | --- | --- |
| [MIRE official repository](https://github.com/liujunwen23/MIRE/tree/d101287af90d114c5bf0cbfbd56fe9c52358e3bb) | WWW 2025 challenge covers image scenes and multi-turn intent; the [Qwen2-VL-7B baseline configuration](https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/mire_baseline/configs/qwen2_vl_full_sft.yaml) uses full SFT | No evidence for a decision readout or LoRA effect; public accessibility does not establish commercial dataset rights |
| [EcomMIR author paper](https://zhoushengisnoob.github.io/papers/WWWComp.pdf), [DOI](https://doi.org/10.1145/3701716.3718371) | CN-CLIP scene classification and MiniCPM-V 2.6 intent LoRA, plus cleaning, hierarchical labels, confident pseudo-labels, augmentation and scene model soup | [E28](evidence.md#e28): Round 2 intent F1 0.9420 and scene F1 0.8278 are author-reported combined-system results, not a LoRA-only ablation or a claim of 1,000-example-only training with untouched evaluation-round data |
| [ezjev training code](https://github.com/everettjf/ezjev/tree/8b3d88957c0795bea160c8fbc9c6d2a54b051136) | Separate text prompt per question, option-letter CE + Brier, hard/ordinary replay and development-set temperature fitting | Tokenizer, input IDs and attention mask are used without an image processor/visual training tensors; loading a multimodal class alone does not establish image fine-tuning |
| [Intern-Decision training configuration](https://github.com/InternLM/Intern-Decision/blob/3572c8a68b5df5dafe02d0e093989ba8ec0183bc/configs/training/qwen35.py) and [compiler](https://github.com/InternLM/Intern-Decision/blob/3572c8a68b5df5dafe02d0e093989ba8ec0183bc/src/inputs/schema.py) | Actual multimodal input path; frozen vision tower/projector, language-backbone training, masked answer-token CE | Configuration is not an existing LoRA recipe; original full training data are unavailable; multiple fields do not imply logical consistency |
| [Decision 3.0 wrapper](https://huggingface.co/vllm-sr/d3/blob/225be8b1e2270becab69c5fe05b26f99cbbdd66b/modeling_d3.py) | Official wrapper `train(True)` raises an inference-only error; custom readout/noncausal attention | Generic Trainer/PEFT cannot simply be assumed to work. Its 255 answer codes are not 255 fixed business classes or evidence of a public multimodal LoRA recipe |
| [Vis Decisions 0.6.1 text training](https://github.com/Blockether/vis-decisions/blob/d73768e3c18d89d11f6b9a774b87d64ccd55f27d/src/blockether/vis_decisions/_d3_trainer.py) | Separate D3 text-model implementation; full text-backbone training or LoRA adapters **plus a trainable 255-code readout**, candidate CE and merged FP32/ONNX export code | Edge/Lite guide; code also accepts Nano. `from_local` keeps text weights and discards vision; only token IDs enter the model. This establishes an inspectable text adaptation path, not out-of-box multimodal training or an independently reproduced result |
| [decision-pacman training](https://github.com/grapeot/decision-pacman/blob/593ed1f59f4f97ad0bda7287ff304e9667360089/training/train.py) and [report](https://github.com/grapeot/decision-pacman/blob/593ed1f59f4f97ad0bda7287ff304e9667360089/README.md) | Textual game state, teacher/simulator labels and option-distribution LoRA distillation; author reports specialization gains alongside generic-task decline | No screenshot-training or support-domain transfer evidence; teacher-only future simulation must not enter student inference; complete data are absent from the inspected code |

The official inference wrapper is a packaging boundary, not proof that D3 cannot be fine-tuned. [Vis code](https://github.com/Blockether/vis-decisions/blob/d73768e3c18d89d11f6b9a774b87d64ccd55f27d/src/blockether/vis_decisions/_d3.py) reconstructs a separate `Qwen3_5TextModel`; its training path has no image/video tower or visual tensors. A proposed image adaptation must retain or restore the matching visual path/processor, verify pixels and grid metadata, and recheck gradients, readout and multimodal export/serving parity. Source inspection here did not run training/export; community speed or quality claims are not imported.

The newer [Intern-Decision paper v1](https://arxiv.org/html/2610.22131v1) reports 17,880 training samples, including 5,500 image-bearing samples, with full language-backbone tuning and frozen vision/projector. This is evidence of image-bearing training, not a LoRA quality result. Its seven-suite numerical comparison is on text tasks; visual demonstrations are qualitative, public Jevbench informed development, and matched-data ablations are missing. The reviewed paper does not provide a matched multimodal D3 comparison or establish release of the full raw training data.

The [October 17 mechanism review](decision-readout-and-reasoning.md) adds StartLux v1.1: a public inference/server package and archived v1 text LoRA example, not a verified complete multimodal v1.1/RLCD² training recipe. The weights are non-commercial; use it as a conditional comparator after checking rights and the exact runtime.

ezjev's MIT code license does not license its weights or training data. Its [model card](https://huggingface.co/everettjf/ezjev-4b-s3/blob/a2faa581dc5e48c0c41ce388d056fed8e8fa6b4d/README.md) warns that some training sources are non-commercial or have unstated terms. Historical author compute spending is not a current training quote. Likewise, reading MIRE/EcomMIR does not replace checking dataset, base, code and weight rights separately. All entries above are source reviews, not reproductions.

<a id="candidate-gates"></a>
### Candidate adaptation gates

| Candidate | Currently inspected starting point | Gate before image adaptation |
| --- | --- | --- |
| D3 | Official multimodal inference comparator; separate Vis Edge/Lite text full/LoRA path, with Nano additionally accepted in code. | Vis drops vision. Restore/retain the actual image path, verify gradients and multimodal export, then test quality; this is separate engineering, not an architectural ban on fine-tuning. |
| Intern-Decision | Image-bearing full-language training and masked answer-token code path; frozen vision/projector. | Exact checkpoint/template/backend identity; full-parameter budget versus separately validated LoRA targets; paper text results do not validate image-domain effectiveness. |
| Qwen3.5 / another supported VLM | Candidate short-label generative SFT/LoRA baseline; model/processor/trainer support must be verified. | B2/B3 share the exact starting checkpoint and evidence. Easier tooling does not demonstrate superiority to a decision-tuned D3 or Intern model. |

## 3. Resolve data and label uncertainty first

A proposed data contract includes anonymous grouping ID, decision timestamp, language, UI/template version, image reference, contemporaneous text, candidates and definitions, adjudicated labels, evidence sufficiency, disagreement and usage rights. These are schema suggestions, not a request to upload real records to a public repository.

Specify primary versus secondary intent, ambiguity rules, facts requiring the image, useful clarification and steps controlled by external policy. Independently relabel and adjudicate disagreements. Persistent disagreement calls for fixing the taxonomy before scaling models. Historical operator actions can be wrong and are not automatic gold labels.

Separate training, development, calibration and final testing using conversation/user groups and source, time, near-duplicate image, screenshot-template and UI-family boundaries. Group duplicates before splitting and document the rule; learned preprocessing, pseudo-label selection and model selection stay inside allowed training/development partitions. Later messages or resolutions can help human label construction but must not enter earlier decision inputs. Generate teacher labels for the training pool, not as repeatedly consulted answers to the final test.

Retain both natural traffic proportions and a separate enriched stress set: rare/confusable intents, same image with different context, image-only ambiguity, missing/wrong images, small text, crops, blur, new layouts, languages, negation, exceptions, contradictions, all-wrong candidate sets and malicious instructions embedded in images. Stress-set enrichment is not a traffic prevalence estimate. Test whether image flips/crops or removal of short utterances preserve the label; a useful clarification or handoff request must not be deleted mechanically because a paper filtered similar text.

## 4. Verify the visual path and objective before training

An image reference is not an image feature. Use the checkpoint's matching processor/chat template; inspect actual `pixel_values`, grid/position metadata, visual tokens and attention masks reaching the correct model. Check whether truncation removes decisive evidence. Frozen visual parameters still require visual encoding. Compare image removal, image swaps and text-only ablations; unchanged outputs may mean either the question needs no image or the image path is broken, so diagnose the cause.

A possible single-choice objective is:

\[
p_\theta(k\mid x,C)=\frac{\exp(z_k/T)}{\sum_{j\in C}\exp(z_j/T)},\quad
L=-\log p_\theta(y\mid x,C)+\lambda\sum_{k\in C}(p_\theta(k)-\mathbf{1}[k=y])^2.
\]

This is an objective to test, not an established optimum. Brier weight, temperature and training budget need development/calibration protocols. Probabilities or a Brier term do not establish empirical calibration. A single positive temperature preserves argmax for the same candidate set and cannot repair label ordering. Multilabel tasks require their own target/output specification rather than a mutually exclusive softmax.

Distinguish candidate-subset CE, full-vocabulary answer-token CE and a separate classification head: normalization, competing outputs and export paths differ. Intern-Decision's reviewed configuration uses standard XTuner CE with supervision retained only at answer-code positions: full-vocabulary answer-token training, unlike ezjev's candidate-subset CE. Its compiler places `<decision>` placeholders in the input; target codes enter labels only. Later causal fields see preceding placeholders, not preceding predictions/gold answers. This is neither an autoregressive chain of completed answers nor proof of field independence.

Check answer-code tokenization in the actual complete prompt, answer positions, legal candidates and padding. Remap labels when shuffling options and test order sensitivity. B2 supervises the agreed answer portion; B3 computes loss at its agreed readout. Do not leak targets or silently discard overlength inputs, broken images or unmappable labels.

## 5. Experiment order and stopping rules

1. **Freeze versions and budgets.** Record base/weights, processor, template, code commits, dependencies, resolution, precision, candidates, context, seeds, training tokens/examples and budget. A model-repository revision need not change weights or training.
2. **Check learnability on a tiny batch.** Inspect loss, gradients, actual trainable parameters, visual inputs and answer positions. Overfit a tiny training subset as pipeline diagnosis, not generalization evidence.
3. **Test language-side LoRA as a starting hypothesis.** Freezing vision/projector reduces trainable parameters but requires verification of the exact class, target modules and gradients. This is a proposed experiment; Intern's full-language-parameter configuration must not be relabeled as LoRA. Select rank, learning rate and epochs through finite development search and explicit early stopping, not copied defaults.
4. **Attribute errors before adding data.** Separate OCR/vision, missing context, ambiguous taxonomy, rule bypasses, template/readout, knowledge, calibration and permission failures. Combine hard examples with ordinary replay and plot learning curves by data/budget to detect narrow overfitting.
5. **Distill only after demonstrated value.** Specify teacher evidence, label provenance and filtering; generate within the training pool and audit hard labels/soft distributions by intent/language. Preserve generic and boundary regression sets because specialization can reduce generality.
6. **Verify export and serving.** Compare training, merged/exported artifact and serving outputs on identical inputs: code mapping, logits, temperature, near ties, image processing and failure behavior. A small adapter still needs its backbone at inference. For image tasks, keep D3 as an inference comparator until the image training/export path is verified; the separate Vis text adaptation path does not validate image training.

Preference/feedback learning is an optional later arm only if residual errors concern visual factuality or candidate preference and auditable pair labels are available. Borrow RLAIF-V/LLaVA-Critic ideas conditionally, compare against supervised adaptation with the same base/evidence/budget, and audit teacher/judge errors. Keep feedback generation inside the training pool and check source/image overlap with evaluation data. A preference model is not a replacement for the intent contract or human-adjudicated final labels.

## 6. Accept quality, risk and cost together

| Dimension | Predefined reporting |
| --- | --- |
| Task quality | Macro-F1, per-class precision/recall, critical confusions and high-risk false negatives; separate multi-intent/unknown |
| Automation policy | Coverage and accepted-set error at a frozen threshold, clarification/handoff burden; unknown labels versus system abstention |
| Uncertainty | Paired comparisons and intervals at conversation/user independence units; no winner from insufficient samples; natural and stress populations separate |
| Probability quality | NLL/Brier on independent calibration data; ECE bins, temperature scope and freeze time explicit; final test used for acceptance |
| Shift and groups | Time, language, source, UI, rare intents, missing evidence and failure rates |
| System economics | OCR/retrieval/preprocessing, model, queue, retries, review and correction; hardware, concurrency, cache, cold/warm behavior, P50/P95, throughput and timeouts |

A possible primary target is useful coverage under a predefined misrouting risk and uncertainty constraint, with additional limits on consequential false negatives and complete handling cost. Observed finite-sample error is not a statistical upper bound. Risk-control guarantees need their own [assumption checks](methodology.md#what-to-measure). Include correction cost per request instead of comparing token prices alone.

Stop scaling training when taxonomy is unstable, intent is not identifiable from the evidence, the visual path fails, serving templates disagree, critical errors persist or gains do not cover maintenance cost. Report offline F1, teacher agreement, schema validity, conversion parity and actual handling outcomes separately. Successful offline acceptance still requires a separately authorized shadow evaluation, human sampling and rollback design. No deployment or real-request processing was performed for this plan.

Treat calibration, error ranking and classification quality as separate measurements. [Guo et al.](https://proceedings.mlr.press/v70/guo17a.html) fit temperature on held-out calibration data; a common positive temperature preserves the fixed-candidate argmax. The [UAI 2024 confidence study](https://proceedings.mlr.press/v244/cattelan24a.html) motivates separate risk–coverage/AURC evaluation, but its ImageNet score choices are not validated defaults for dynamic-candidate VLMs. D3/API `confidence >= 0.9` does not imply error <= 10% on accepted domain cases; check the actual statistic and returned policy.

The [pinned D3 package](https://huggingface.co/vllm-sr/d3/blob/225be8b1e2270becab69c5fe05b26f99cbbdd66b/d3_runtime.py) defines choice/score confidence as one minus normalized entropy for multiple candidates, not an estimated probability that the selected label is correct. Other backends can use different definitions. Separate probability-map fitting from threshold certification, or use a procedure accounting for adaptive choices; repeatedly choosing models, temperatures and gates on one calibration set does not inherit an untouched-calibration guarantee.

[Conformal Risk Control](https://proceedings.iclr.cc/paper_files/paper/2024/hash/f3549ef9b5ff520a7e41ff3cc306ab2b-Abstract-Conference.html) controls expected risk under exchangeability and bounded monotone-loss conditions. It is not a per-item or arbitrary fixed-calibration-set high-probability guarantee. Accepted-set error can be non-monotone in a threshold, so standard CRC cannot be attached automatically. Choose a method matching the risk definition and data dependence; validate again after routing, candidate reduction or distribution shift.

For final comparisons, pair the same conversation/request groups and report the quality/coverage/cost differences with group-aware uncertainty. Freeze model, policy and thresholds before looking at final outcomes; record all attempted development arms. State a minimum useful gain and allowed consequential-error/cost limits beforehand. A noisy mean gain, lower calibration error alone or ONNX parity alone is insufficient to continue.

The Oct14 [risk-budgeted System One preprint](https://arxiv.org/html/2610.19811v1) studies binary policies: score `s(X)` predicts a positive event, Action 0 on `s(X) < tau` has `FOR = P(Y=1 | s(X)<tau)`, and Action 1 is the conservative fallback. Its fixed-sequence LTT result requires a frozen scorer/ordered threshold family derived from Fit independently of iid Cal from the same deployment population. With error level delta, the probability over calibration samples of certifying a population-risk-violating policy is bounded by delta. This is not each answer's probability of correctness, a promise that every finite test estimate stays below budget, or an automatic multiclass/image/shift guarantee. No certificate means fallback for the policy, distinct from per-input abstention. Six English-text datasets/single seed are author evidence; no local replication or numeric gain is claimed.

## 7. Minimum research deliverables

Retain preregistered hypotheses, owner-defined risk/cost/useful-gain limits, task/label specification, source and usage-right inventory, grouped splits and deduplication, versions/budgets, experimental arms, image ablations, per-class errors, calibration/thresholds, full cost and stopping decision. Shared artifacts must use explicitly publishable material; real data and execution authority remain under their own governance. Write training/evaluation scripts after validating the chosen implementation rather than presenting untested commands as a reproduction recipe.

Source identities and review scope are in the [register](sources.md); EcomMIR measurements and protocol limitations are in [E28](evidence.md#e28). This page releases no dataset, model weights or training results.

<a id="reading-list"></a>
## 8. Layered reading list and what to borrow

Publication status and evidence strength are separate axes. Peer review does not make results independent of model authors or prove transfer to this domain. This repository reviewed sources and did not run these models. Use the papers for testable design choices, not a combined leaderboard.

### Peer-reviewed papers

| Formal title / venue | Useful implementation question | Evidence boundary |
| --- | --- | --- |
| [EcomMIR: Towards Intelligent Multimodal Intent Recognition in E-Commerce Dialogue Systems](https://doi.org/10.1145/3701716.3718371) — WWW Companion 2025 (Companion Proceedings of the ACM Web Conference 2025), four-page challenge solution | CN-CLIP scene classification with Greedy Soup; MiniCPM-V 2.6 intent LoRA, hierarchical labels/cleaning and pseudo-label selection. | Author combined-system competition report, not a WWW main research-track study or isolated LoRA effect. Round 1 unlabeled test inputs enter training: a transductive component, not a 1,000-example-only supervised protocol. This does not establish Round 2 leakage. See [E28](evidence.md#e28). |
| [MIntRec2.0: A Large-scale Benchmark Dataset for Multimodal Intent Recognition and Out-of-scope Detection in Conversations](https://openreview.net/forum?id=nY9nITZQjc) — ICLR 2024; [official repository](https://github.com/thuiar/MIntRec2.0) | Intent/OOS labels and multi-party, multi-turn text/audio/video context; in-scope and outlier-exposure objectives. | Television conversations are not support screenshots or a LoRA experiment. Repository body inspected; OpenReview verification blocked full-paper access in this review. |
| [RLAIF-V: Open-Source AI Feedback Leads to Super GPT-4V Trustworthiness](https://openaccess.thecvf.com/content/CVPR2025/html/Yu_RLAIF-V_Open-Source_AI_Feedback_Leads_to_Super_GPT-4V_Trustworthiness_CVPR_2025_paper.html) — CVPR 2025 | Visual factuality checks, AI preference construction and DPO-style preference learning; audit teacher feedback before distillation. | Author alignment results concern visual response trustworthiness, not domain intent utility. Later repository LoRA support does not make every paper result LoRA. Dataset NC/research-use notices and base/API terms require review. |
| [LLaVA-Critic: Learning to Evaluate Multimodal Models](https://openaccess.thecvf.com/content/CVPR2025/html/Xiong_LLaVA-Critic_Learning_to_Evaluate_Multimodal_Models_CVPR_2025_paper.html) — CVPR 2025 | Fine-tune LLaVA-OneVision with pointwise/pairwise critic instructions and CE over judgments/justifications; inspect GPT-4o-assisted label bias. | A generative visual critic is not a direct candidate-logit classifier or domain-outcome validator. Do not infer uninspected adapter/full-parameter settings or use its own teacher agreement as gold. |
| [VL-RewardBench: A Challenging Benchmark for Vision-Language Generative Reward Models](https://openaccess.thecvf.com/content/CVPR2025/html/Li_VL-RewardBench_A_Challenging_Benchmark_for_Vision-Language_Generative_Reward_Models_CVPR_2025_paper.html) — CVPR 2025 | Check whether a judge detects visual evidence failures on curated, human-verified preference cases. | A benchmark, not a training recipe. Source pools include RLAIF-V/RLHF-V: audit example/image/source overlap before treating it as held out. Benchmark-author evaluation is distinct from this repository reproducing it. |
| [On Calibration of Modern Neural Networks](https://proceedings.mlr.press/v70/guo17a.html) — ICML 2017 | Fit temperature on separate calibration data and assess probability quality. | Fixed-candidate argmax/top-1 accuracy does not improve from a common positive temperature; deployment/shift calibration remains empirical. |
| [How to Fix a Broken Confidence Estimator: Evaluating Post-hoc Methods for Selective Classification with Deep Neural Networks](https://proceedings.mlr.press/v244/cattelan24a.html) — UAI 2024 | Distinguish accuracy from error ranking and evaluate risk–coverage/AURC. | The 84-ImageNet-classifier study does not establish the best confidence score for dynamic labels or VLMs. |
| [Conformal Risk Control](https://proceedings.iclr.cc/paper_files/paper/2024/hash/f3549ef9b5ff520a7e41ff3cc306ab2b-Abstract-Conference.html) — ICLR 2024 | Match bounded-loss, monotonicity and exchangeability assumptions to a precisely defined risk. | Expected-risk control is not a per-decision correctness promise; arbitrary accepted-set conditional error is not automatically covered. |

### Preprints and engineering assets

| Source / status | What it establishes | Open question |
| --- | --- | --- |
| [Calibration and Risk-Budgeted Decisions with System One Models](https://arxiv.org/html/2610.19811v1) — arXiv v1, 2026-10-14 | Specify binary FOR, fixed scorer/threshold family, independent Fit/Cal/Test and conservative fallback before LTT certification. | Author-reported six English-text datasets/single seed; calibration-sample population-risk control is not per-item correctness or an image/multiclass/shift guarantee. |
| [Intern-Decision: Efficient Multimodal Decision Making with Autoregressive Masked Language Modeling](https://arxiv.org/html/2610.22131v1) — arXiv v1, 2026-10-15 | Image-bearing full-language training and a multi-field causal masked readout, with frozen vision/projector. | Text-suite metrics and qualitative visual examples do not supply a matched D3 multimodal comparison or a LoRA result; full raw training-data release not established. |
| [StartLux-Decision: AutoThink Decision Models with Reinforcement Learning for Calibrated Deliberative Decisions](https://arxiv.org/html/2610.17309v1) — arXiv v1, 2026-10-12 | Candidate probabilities, adaptive reasoning and policy-aware calibration; [mechanism audit](decision-readout-and-reasoning.md). | Public DI development selection, author-built DecisionPivot and NC weights constrain interpretation and use; not a demonstrated domain image-training recipe. |
| [MIRE: Multimodal Intent Recognition for Dialogue Systems challenge baseline](https://github.com/liujunwen23/MIRE/tree/d101287af90d114c5bf0cbfbd56fe9c52358e3bb) — WWW2025 challenge engineering repository | Qwen2-VL-7B **full SFT** baseline for scene/intent tasks. | This is not EcomMIR's implementation, a LoRA result, or a separate peer-reviewed method paper verified here. |
| [Vis Decisions 0.6.1 D3 path](https://github.com/Blockether/vis-decisions/blob/d73768e3c18d89d11f6b9a774b87d64ccd55f27d/src/blockether/vis_decisions/_d3_trainer.py) — third-party engineering | Text full/LoRA plus trainable code head and merged export implementation. | Removed vision tower; not verified multimodal adaptation or an independent benchmark reproduction. |

Read in order: domain intent adaptation → OOS/clarification → visual feedback → candidate/critic scoring → judge checks → calibration and rejection. Peer-reviewed methods can inform an experiment without proving that fine-tuning will improve its target decision. Review depth, versions and access gaps are in the [source register](sources.md).
