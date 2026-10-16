# Fine-tuning multimodal decision models: research and acceptance plan

[简体中文](multimodal-decision-finetuning.zh-CN.md) · [Home](../README.md) · [Selection guide](selection-guide.md#image-intent-adaptation) · [Evidence ledger](evidence.md)

Sources reviewed: 2026-10-16. This is a testable research design for general multimodal customer-support intent recognition. No model was trained and no production benefit was demonstrated here. Public implementations, author reports and proposed experiments are distinguished below. Image understanding, intent, calibration and authority to act are separate questions.

## 1. Freeze the question and comparisons

Ask whether short-label generation or direct candidate scoring delivers more useful coverage at a predefined misrouting risk and lower complete handling cost, with the same evidence, labels, backbone and resource budget.

Separate **visible facts**, **the user's intent given contemporaneous context**, and **the permitted next step under identity, policy and evidence constraints**. One screenshot can accompany different requests. Image categories are not automatically intent labels. A screenshot does not establish authenticity, ownership or authorization. Allow multiple intents, unknown, out-of-scope and clarification instead of forcing a business category. Supply changing policies through versioned retrieval rather than relying on memorized weights.

These are proposed experimental arms, not measured results:

| Arm | Inputs and training | Factor to isolate |
| --- | --- | --- |
| B0: OCR + text | Rules or ordinary supervised text classifier; retain a text-only arm | OCR, loss of layout, label separability and cost |
| B1: instruction VLM | Fixed-schema zero/few-shot short-label output | Whether images and context suffice; retrieval augmentation gets a separate arm |
| B2: VLM LoRA-SFT | Short structured labels on the same VLM backbone | Benefit of domain supervision; cap output length and count format failures |
| B3: candidate-distribution LoRA | Same backbone, data, image processing and budget as B2; read legal-option logits | Benefit of readout/objective, after verifying training/serving alignment |

Establish B0/B1/B2 before investing in B3. A short generated label may require only a few tokens, so removing decoding need not materially reduce end-to-end latency. Add a separate scene encoder or multistage classifier only when scene recognition is a demonstrated bottleneck.

## 2. What the public evidence supports

| Source and fixed revision | Inspected finding | Limit |
| --- | --- | --- |
| [MIRE official repository](https://github.com/liujunwen23/MIRE/tree/d101287af90d114c5bf0cbfbd56fe9c52358e3bb) | WWW 2025 challenge covers image scenes and multi-turn intent; the [Qwen2-VL-7B baseline configuration](https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/mire_baseline/configs/qwen2_vl_full_sft.yaml) uses full SFT | No evidence for a decision readout or LoRA effect; public accessibility does not establish commercial dataset rights |
| [EcomMIR author paper](https://zhoushengisnoob.github.io/papers/WWWComp.pdf), [DOI](https://doi.org/10.1145/3701716.3718371) | CN-CLIP scene classification and MiniCPM-V 2.6 intent LoRA, plus cleaning, hierarchical labels, confident pseudo-labels, augmentation and scene model soup | [E28](evidence.md#e28): Round 2 intent F1 0.9420 and scene F1 0.8278 are author-reported combined-system results, not a LoRA-only ablation or a claim of 1,000-example-only training with untouched evaluation-round data |
| [ezjev training code](https://github.com/everettjf/ezjev/tree/8b3d88957c0795bea160c8fbc9c6d2a54b051136) | Separate text prompt per question, option-letter CE + Brier, hard/ordinary replay and development-set temperature fitting | Tokenizer, input IDs and attention mask are used without an image processor/visual training tensors; loading a multimodal class alone does not establish image fine-tuning |
| [Intern-Decision training configuration](https://github.com/InternLM/Intern-Decision/blob/3572c8a68b5df5dafe02d0e093989ba8ec0183bc/configs/training/qwen35.py) and [compiler](https://github.com/InternLM/Intern-Decision/blob/3572c8a68b5df5dafe02d0e093989ba8ec0183bc/src/inputs/schema.py) | Actual multimodal input path; frozen vision tower/projector, language-backbone training, masked answer-token CE | Configuration is not an existing LoRA recipe; original full training data are unavailable; multiple fields do not imply logical consistency |
| [Decision 3.0 wrapper](https://huggingface.co/vllm-sr/d3/blob/225be8b1e2270becab69c5fe05b26f99cbbdd66b/modeling_d3.py) | Inspected `train(True)` raises an inference-only error; custom readout/noncausal attention | Generic Trainer/PEFT cannot simply be assumed to work. Its 255 answer codes are not 255 fixed business classes or evidence of a public multimodal LoRA recipe |
| [decision-pacman training](https://github.com/grapeot/decision-pacman/blob/593ed1f59f4f97ad0bda7287ff304e9667360089/training/train.py) and [report](https://github.com/grapeot/decision-pacman/blob/593ed1f59f4f97ad0bda7287ff304e9667360089/README.md) | Textual game state, teacher/simulator labels and option-distribution LoRA distillation; author reports specialization gains alongside generic-task decline | No screenshot-training or support-domain transfer evidence; teacher-only future simulation must not enter student inference; complete data are absent from the inspected code |

ezjev's MIT code license does not license its weights or training data. Its [model card](https://huggingface.co/everettjf/ezjev-4b-s3/blob/a2faa581dc5e48c0c41ce388d056fed8e8fa6b4d/README.md) warns that some training sources are non-commercial or have unstated terms. Historical author compute spending is not a current training quote. Likewise, reading MIRE/EcomMIR does not replace checking dataset, base, code and weight rights separately. All entries above are source reviews, not reproductions.

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
6. **Verify export and serving.** Compare training, merged/exported artifact and serving outputs on identical inputs: code mapping, logits, temperature, near ties, image processing and failure behavior. A small adapter still needs its backbone at inference. Treat D3 as an inference comparator until a complete training/export path is separately verified.

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

## 7. Minimum research deliverables

Retain task/label specification, source and usage-right inventory, grouped splits and deduplication, versions/budgets, experimental arms, image ablations, per-class errors, calibration/thresholds, full cost and stopping decision. Shared artifacts must use explicitly publishable material; real data and execution authority remain under their own governance. Write training/evaluation scripts after validating the chosen implementation rather than presenting untested commands as a reproduction recipe.

Source identities and review scope are in the [register](sources.md); EcomMIR measurements and protocol limitations are in [E28](evidence.md#e28). This page releases no dataset, model weights or training results.
