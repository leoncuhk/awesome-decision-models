# Fine-tuning multimodal decision models: research and acceptance plan

[简体中文](multimodal-decision-finetuning.zh-CN.md) · [Home](../README.md) · [Selection guide](selection-guide.md#image-intent-adaptation) · [Evidence ledger](evidence.md)

Sources reviewed: 2026-10-27 (Mac implementation and acceptance planning; earlier evidence retains its original dates). This is a testable research design for general multimodal customer-support intent recognition. No model was trained and no production benefit was demonstrated here. Public implementations, author reports and proposed experiments are distinguished below. Image understanding, intent, calibration and abstention policy are separate questions.

This is the maintained implementation plan: [Mac small-data route](#mac-implementation), [matched matrix](#experiment-matrix) and [research evidence](#7-minimum-research-deliverables). The [October 26 source audit](../updates/2026-10-26-multimodal-training-and-evidence.md) and October 22 survey remain historical references; no parallel implementation report is added.

**Research question.** With a few thousand manually labeled images, can a resource-bounded local system reduce per-case total decision cost while meeting critical-risk limits, and can controlled experiments distinguish data/scorer gains from a new learning mechanism? All implementation, training and acceptance steps below are pending execution.

<a id="quick-route"></a>
## One-page experiment route

Use this route to test whether domain post-training improves a defined decision. **No candidate is a proven winner, and adaptation can reduce quality.** The [reading list](#reading-list) separates peer-reviewed methods, preprints and engineering assets.

| Gate | Required artifact and pass condition | Fail / stop |
| --- | --- | --- |
| G0 · Contract | Rights, observable input/labels, independent groups, split manifest and owner-set error/review/latency/compute costs; [data](#data-schema). | Unidentifiable targets, missing rights or insufficient independent support: revise or stop that arm. |
| G1 · Technical smoke | A future authorized 32–64-example synthetic/non-sensitive pipeline check, including longest inputs/backward/save/reload; [Mac route](#mac-implementation). | Lost visual evidence, wrong masks, invalid gradients, memory pressure or reload mismatch: fix before scaling. |
| G2 · Baselines and bounded adaptation | Rules/OCR/frozen features, one small frozen VLM and its matched frozen-head/QLoRA arms; finite Dev search and at least three preregistered seeds; [matrix](#experiment-matrix). | If the inexpensive baseline meets the target, do not add model complexity merely to create a research story. |
| G3 · Frozen acceptance | Separate Cal-fit/Cal-policy, locked Test; paired per-case cost reduction above a minimum useful gain and acceptable critical risk; [acceptance](#6-accept-quality-risk-and-cost-together). | Inconclusive intervals, failing risk/cost/parity or test-guided selection: no success claim; keep negative findings. |
| G4 · Conditional external check | Only after separate authorization: shadow evaluation, human audit and rollback plan. | Offline success grants no permission to deploy or process real requests. |

All gates are planned work. This document authorizes no installation, weight/sample download, training, upload, production processing or deployment. Reuse identified completed checks when the artifact and question are unchanged.

<a id="six-principles"></a>
### Six principles translated into experiments

| Principle | Concrete experiment / artifact |
| --- | --- |
| Intent depends on evidence, not the screenshot category alone. | Independent annotation of visible facts, contemporaneous intent and sufficiency; same-image/different-context cases. |
| Typed outputs and direct logits are mechanisms, not accuracy guarantees. | D0 inference comparator; B2/B3 with the exact same base and explicit normalization/readout. |
| Domain supervision must add useful information. | Strong B0/B1 baselines first; grouped learning curves and one-factor adaptation, including ordinary replay. |
| More reasoning cannot supply missing evidence. | Deterministic arithmetic/rules; optional frozen hard-case AutoThink comparison only on evidence-complete inputs. |
| Probability, calibration and an acceptable policy differ. | Separate development/calibration/test roles, error costs and risk–coverage; no universal confidence cutoff. |
| Deployment is part of the model being evaluated. | Image/token/template, concurrent request, precision/device/calibrator regression and complete cost on the same frozen policy. |

Start at the [data schema](#data-schema), [split protocol](#split-protocol) and [minimal matrix](#experiment-matrix); finish with the [result template](#result-template) and [decision tree](#decision-tree). These are proposed procedures for a small domain-screenshot dataset, not a released dataset or an experimental result.

## 1. Freeze the question and comparisons

Define exactly what is observed: an image, contemporaneous context if actually present, the user's intent, observable evidence, evidence sufficiency, and the policy-permitted next step. These are different annotation targets. If the existing labels describe only image categories, do not invent conversation context, intent or correct actions. Scope that first experiment to what its inputs identify, or separately authorize the missing annotation. Keep normal known cases, missing images, missing context, image–text conflicts, unknown intents and OOS distinct. Two annotators independently audit a representative sample plus enriched ambiguous/rare cases and adjudicate disagreements; do not force a label when the input itself is insufficient.

The main output is a short label plus a defined score, with evidence location and optional concise explanation separate. Long chain-of-thought is not a substitute for evidence grounding. Changing prices/status/policies remain time-valid input evidence, as specified in [learned judgment](#learned-judgment).

### Preregister falsifiable hypotheses

| Question | Test that could refute it | Decision |
| --- | --- | --- |
| H1: the visible input identifies the requested target and images add information. | Independent annotation remains ambiguous, or context/OCR/frozen features explain all useful signal. | Revise the target/evidence; no image-learning claim from image labels alone. |
| H2: bounded adaptation improves the business decision. | Paired per-independent-case cost reduction versus the strongest frozen baseline has a confidence lower bound no greater than the preregistered minimum useful gain, or critical risk fails. | Keep the baseline, collect independent evidence or stop. More F1 alone is insufficient. |
| H3: a specified readout/training change adds value. | Same exact base, labels, visual processing and optimization/search budget explain the apparent gain; a frozen head or stronger post-hoc scorer closes it. | Report the useful system change, without attributing it to a representation breakthrough. |
| H4, optional research: paired semantic-preserving supervision plus missing/conflicting-necessary-evidence supervision improves unseen-template/time coverage at fixed error risk. | Ordinary equal-volume augmentation, a strong scorer/calibration baseline or a budget-matched Rep2Act transfer arm matches it. | It remains a novelty-to-check hypothesis; open only after the first-pass business/image-learning checks justify it. See [research evidence](#7-minimum-research-deliverables). |

**Business endpoint:** reduction in total expected error/review/latency/compute cost per independent case, with owner-set critical-risk limits and a minimum worthwhile effect fixed before selection. Useful coverage at the same risk, macro-F1 and probability quality are supporting endpoints. A separate research endpoint tests H4 with controlled ablations; neither endpoint is established here.

Training support determines which experiment is feasible, not which model wins. A matched unadapted/adapted small VLM tests adaptation; comparison with a released D3/Intern/Clef system tests complete systems with different training histories. Report label access, scale, quantization, visual resolution and total search/inference budgets; do not credit a readout for changing the backbone.

<a id="experiment-matrix"></a>
### Minimal matrix: required first pass, then gated extensions

Use one frozen task/split; all features, exemplars and heads fit only on Train. Complete finite model/prompt/scorer selection on Dev, then take only preregistered frozen baselines and final candidates into the same locked Test. Start with the inexpensive arms; one small VLM is enough initially. If the task has no real context, omit context-only comparisons explicitly rather than synthesize evidence.

| Arm | Configuration | What it tests |
| --- | --- | --- |
| B0-R / B0-T | Existing deterministic rules; an ordinary supervised text classifier when real text exists | Operational floor and target separability; count rule failures. |
| B0-O | Frozen OCR plus the same context/text classifier | Increment from OCR; include OCR errors and preprocessing cost. |
| F0 | Frozen image/text encoder features plus regularized linear head | Low-cost supervised fusion without VLM adaptation; normalization/head choices stay within Dev. |
| B1 | One exact 2B-class VLM, zero-shot and separately Train-only few-shot short labels | Unadapted comparator; freeze template, image pixels/tokens and invalid-output handling. Retrieval/page guidance is a separate matched arm. |
| F1 | The same B1 backbone frozen, a supervised small head at a verified feature position | Whether a head suffices; this needs a separately validated feature/head implementation, not generic SFT CLI support. |
| B2 | The same quantized B1 base, image-conditioned language-side QLoRA, completion-only short-label SFT | Increment from adapter learning over B1/F1; frozen vision is still used. Use at least three preregistered seeds and a bounded Dev search. |
| B3-CE / B3-Brier, gated | B2's exact base/data/processor/adapter budget; candidate-subset CE, then the same implementation plus explicit Brier term | Readout/objective attribution; the first comparison also changes normalization, while the second isolates the added loss. |
| D0 / I0 / C, gated | Disclosed-size D3 or Intern inference; continue a decision checkpoint only after platform/image-training/export gates | Serious system comparators when the target resource/privacy budget permits. D3 has small variants; do not treat the whole family as 27B. CUDA training does not imply a Mac recipe. |

Match inputs, label access, quantization and image processing wherever a causal comparison requires it; disclose remaining differences and the same finite tuning budget. Compare each trained system under preregistered maximum-softmax/temperature, energy and Mahalanobis-style scorers where their outputs/features support them. Fit centroids/covariance on Train only, choose regularization/feature position on Dev, calibrate/freeze subsequently, and count scorer memory/latency. Do not invent energy from verbal confidence or apply it across incomparable dynamic candidate sets.

Record seed IDs before running; retain every attempt and never select the best Test seed. Report between-seed variability separately from uncertainty over independent cases; seeds and repeated screenshots are not additional independent cases. A baseline already meeting the business target is a valid stopping result. AutoThink, distillation and the H4 research branches are optional, budgeted hypotheses rather than first-pass requirements.

## 2. What the public evidence supports

Read the [MIRE competition case](mire-case-study.md#tasks) for complete labels, actual IO/code, [official final prizes versus online scores](mire-case-study.md#finalists) and top-three method boundaries; it is a sourced case, not a new domain result.

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
| Native Mac VLM | [Pinned MLX-VLM](https://github.com/Blaizzy/mlx-vlm/blob/2ceff4c14b991370a459d14eb49d1bedf4fb9e84/docs/training.md) has local-image completion-only SFT and quantized-base language adapters. | Prefer one 2B candidate for G1; freeze vision by default, verify real pixels/masks/gradients, longest-input memory and reload. Source support is not a local run. |
| D3 classic / Turbo | Classic Vis adaptation is text only; Turbo shares state across independent question branches and its official wrapper rejects training. D3 has nano/mini/flash as well as larger releases. | Keep exact model/runtime identity; API alias and inference capacity do not verify a native Mac image-training recipe. |
| Intern-Decision | Image-bearing full-language tuning with frozen vision/projector exists in the CUDA/XTuner path. | Not an existing Mac LoRA recipe; preserve its placeholder/answer-code contract and separately verify any port/export. |
| Qwen2/2.5/3-VL and Qwen3.5 | Official QwenVL and separate ms-swift recipes remain inspectable image-training references; Mac uses its own verified MLX model/processor path. | Do not transfer CUDA/Transformers support to MLX or transfer Qwen3-VL dispatch to Qwen3.5 by name. B2/B3 use the same exact base and evidence. |
| Decider / Clef | Decider image inference and experimental Clef community training remain separate. [MLX-VLM Clef](https://github.com/Blaizzy/mlx-vlm/blob/2ceff4c14b991370a459d14eb49d1bedf4fb9e84/mlx_vlm/models/clef/README.md) supports image/video decision inference. | Clef's [call contract](https://github.com/Blaizzy/mlx-vlm/blob/2ceff4c14b991370a459d14eb49d1bedf4fb9e84/mlx_vlm/models/clef/clef.py) needs question/option spans and qtype; ordinary shifted-SFT CLI does not certify training its joint head. |
| mlx-decision / mlx-lm | mlx-decision rejects media in training; mlx-lm text support is a different scope from mlx-vlm. | Neither restriction nor text support establishes MLX-VLM image/head trainability. Keep framework, inference and training path explicit. |

## 3. Resolve data and label uncertainty first

<a id="data-schema"></a>
### A minimal local data schema

The following is invented notation, not a real record, usable prompt or public-data upload request. Store actual assets, text, identities and labels in an authorized local/private system; opaque IDs alone do not anonymize screenshots. Keep the label taxonomy/candidate definitions in a versioned sidecar. Separate annotation-only later outcomes from model-visible evidence, and verify evidence timestamps before feature extraction.

```json
{
  "record_id": "synthetic-001",
  "image_ref": "LOCAL_ONLY",
  "visible_text": "SYNTHETIC_PLACEHOLDER",
  "evidence_cutoff": "SYNTHETIC_TIMESTAMP",
  "guidance_version": null,
  "conversation_group": "GROUP_A",
  "user_group": "GROUP_B",
  "near_duplicate_group": "DUP_A",
  "leakage_component": "COMPONENT_A",
  "ui_family": "UI_A",
  "ui_version": "v0",
  "language": "und",
  "label_schema_version": "labels-v1",
  "task_mode": "single_intent",
  "intents": ["INTENT_A"],
  "observable_evidence": ["SYNTHETIC_REGION_A"],
  "evidence_status": "sufficient",
  "permitted_next_step": null,
  "unknown_reason": null,
  "annotation_status": "independently_reviewed_and_adjudicated",
  "rights_status": "LOCAL_REVIEW_REQUIRED",
  "split": "unassigned"
}
```

Audit readability at the actual inference resize/crop/compression, not just the original resolution: can annotators read the decisive text and distinguish the UI state, and does OCR retain it? Separate blur/small text/missing regions/redaction loss from semantic confusion. Freeze permissible preprocessing; a crop or flip that removes evidence or reverses a UI relation is not label-preserving augmentation.

If a record contains only an image category, leave absent context/intent/action fields unavailable; no synthetic conversational history is gold. Define `task_mode` before modeling. Single-intent uses an agreed primary-label tie rule; multi-intent uses a set target and per-label precision/recall (plus exact-set score when useful), not an exclusive softmax. `unknown` means the taxonomy cannot assign a known class; `out_of_scope` means a known scope mismatch; `insufficient`/`needs_clarification` concerns missing evidence. They may coexist with a partial intent. State their precedence and annotation/output rules explicitly. A model's low-confidence abstention is a **policy output**, not automatically one of these gold labels.

Have at least two annotators independently assess an agreed audit subset, enriched with ambiguous/rare cases and a separate representative sample. Record label-wise agreement, disagreements and adjudication, rather than only a pooled agreement score. Expand the audit where disagreement concentrates. Historical operator actions and teacher labels are provisional evidence, not automatic gold. If the same visible image/text admits multiple plausible intents, request context or revise the contract before training.

<a id="learned-judgment"></a>
### Learn judgment while supplying changing facts as evidence

Train separate targets for intent, evidence sufficiency/reason and permitted next step; evaluate their joint consistency. Keep user goal distinct from image category and from a guess about a missing fact. Use matched same-image/different-goal cases, readable/unreadable evidence, contradictions and genuine unknown intents with independent adjudication. Suggested routing labels do not authorize execution.

Changing prices, entitlements, order status, policy dates and taxonomy descriptions belong in versioned, time-valid retrieval/tool evidence. Train how to use the supplied evidence, recognize absent/stale/conflicting facts and ask a discriminating question; do not make recall of mutable facts the learning objective. Hold out fact values and later policy versions, and compare a frozen retrieval baseline to adaptation. A missing fact calls for retrieval, a missing user goal for clarification, and an unknown intent for open-set handling; low confidence alone does not identify which one.

[Rep2Act/VAD-R](https://arxiv.org/html/2609.32653v1) motivates testing answerability and actual abstention separately; [VLTest](https://arxiv.org/html/2610.30794v1) motivates matched image/text controls with re-adjudicated answers. Current execution design is maintained in [§5](#mac-implementation) and [§6](#6-accept-quality-risk-and-cost-together); the [October 26 audit](../updates/2026-10-26-multimodal-training-and-evidence.md) retains its historical source scope.

<a id="output-contract"></a>
### Short-label scores must be defined before calibration

Chinese class names can have different token lengths. Do not use only their first-token probability or a generated verbal confidence as a class score. Prefer fixed short IDs mapped to versioned labels, with explicit unknown/insufficient definitions where the task warrants them; verify the actual tokenizer and full template prefix rather than assuming an ID is one token. If single-token IDs are unavailable, specify complete candidate-sequence log-probability and any length normalization, compare the scoring convention on Dev, or implement a separately verified classifier head.

Constrained decoding guarantees a valid label format, not OOS recognition. Candidate-subset softmax always normalizes the listed choices; combine it with an independently evaluated evidence-sufficiency/rejection/distance score when needed, and calibrate the actual complete policy. Keep the short business output separate from evidence spans and concise explanation. Ordinary completion-only SFT sees gold answer text only in the supervised continuation; Intern's marker-only labels and Clef's schema spans require their own training contracts, not a copy-paste into shifted SFT.

<a id="split-protocol"></a>
### Leakage-resistant split protocol

1. **Inventory before allocation.** Count usable images and independent conversations/users, exact/near duplicates, UI/template families, dates, labels and missing evidence. Audit exact hashes plus visual/OCR similarity and manually inspect suspicious pairs; a perceptual hash alone neither proves identity nor catches every near duplicate. Record excluded/corrupt assets and reasons.
2. **Form leakage components.** Link records sharing the chosen independence unit (same conversation/user) or an actual duplicate/near-identical rendered instance; take connected components so transitive links cannot cross partitions. Derived crops, augmentations and paraphrases inherit the parent's component and split. A giant component is a limitation to resolve, not a reason to break the grouping rule. Keep abstract UI family separate from instance-duplicate grouping.
3. **Declare populations.** For expected traffic, keep representative prevalence with no component overlap. Also freeze a later-time and/or previously unseen UI/page-family holdout when those generalization claims matter; report it separately, not as a representative mixture. A familiar-UI split cannot demonstrate new-page generalization. Enriched rare/error stress sets have their own denominators. Temporal splits do not automatically enforce user/duplicate isolation: check both constraints.
4. **Lock roles and membership.** A data steward may use labels to allocate per-class support before model selection, then hide final-test labels/content from prompt/model/hard-case development. Train fits weights/features/augmentation; Dev selects checkpoint, schema, prompt, rank, learning rate, epochs, Brier weight and routing design. Cal fits the frozen model's probability mapping/policy; Test measures frozen acceptance once. No test content or errors feed retrieval examples, pseudo-labels, synthetic hard cases, calibration or model selection.
5. **Use CV only inside development.** When a fixed Dev split is unstable, use group-aware folds (optionally stratified when feasible), or forward-time folds if the target is future traffic; never sacrifice group/time isolation for label balance. Keep outer Test and final Cal untouched. Preprocessing and generated examples are fitted within each training fold. Report fold/group counts, missing classes and selection variability. OOF predictions from several models are not automatically a valid calibrator for a refitted model; recalibrate the final artifact or use a justified cross-fitting procedure. See [official grouped/time CV guidance](https://scikit-learn.org/stable/modules/cross_validation.html).
6. **Version changes.** Fix split IDs/hashes and a leakage audit before the first comparison. If a Dev hard case moves into Train, retire that development measurement and replace/version Dev. Inspect final-test errors only after freezing/reporting acceptance; once those errors guide changes, that test is development history and a new untouched acceptance set is needed.

Retain a predeclared separate stress set: rare/confusable intents, same image with different text, missing/wrong images, tiny text/blur, unseen UI/languages, negation/exceptions/contradictions, all-wrong candidates and malicious instructions embedded in images. Adjudicate expected behavior per case. Enrichment is not traffic prevalence, and final-test errors never generate training hard cases.

<a id="sample-size"></a>
### Small-sample support and uncertainty

For a few thousand manually labeled images, first count independent cases/conversations/users, labels, duplicate families and genuinely observable targets. Image count is not independent sample count. The following is **only an invented 3,000-record annotation budget**, not a prescribed ratio or evidence that every class/risk has enough support:

| Role | Illustrative count | Exclusive use |
| --- | --- | --- |
| Train | 1,500 | Fit features/heads/adapters; derive augmentation only after original groups are assigned. |
| Dev | 300 | Finite model/prompt/hyperparameter/scorer selection and early stopping. |
| Cal-fit | 300 | Fit a probability map for the final frozen artifact. |
| Cal-policy | 300 | Select only a finite preregistered policy/threshold family with an applicable multiple-testing/risk procedure. |
| Locked Test | 600 | Confirm the frozen comparison once; no checkpoint, seed, prompt, scorer or threshold search. |

Allocate whole groups, not individual images. Same case, conversation, near-duplicate instance and every derived crop/paraphrase stay together; combine transitive links into leakage components. Define new-customer, unseen-template and later-time targets separately, with distinct test populations/counts. An abstract template key need not connect every case into one giant component; do not create that component and then split it arbitrarily. Label balance cannot override independence/time boundaries. For small Dev, group CV belongs inside development; it does not replace the independent locked Test or make cross-fitted scores automatically valid for a refitted artifact. [Leakage and reproducibility](https://arxiv.org/html/2207.07048v1) motivates a model/data information sheet, not a certificate that this split is safe.

Before training, publish an internal class/group count table across all five roles, separately for known/unknown/OOS/insufficient/conflicting inputs and each claimed shift. Mark absent-class recall as not estimable; combine classes only for semantic reasons. Enriched stress tests do not estimate traffic prevalence. If independent support is inadequate, narrow claims, collect independent labels or report exploratory results; no fixed split fraction solves it.

**Risk-denominator check, invented iid arithmetic only:** for one preregistered frozen policy with zero errors among `n` independent accepted cases in the relevant risk population, the one-sided 95% exact binomial upper bound is `1 - 0.05^(1/n)`. At `n=100` it is about 2.95%; a bound below 1% needs at least 299 zero-error accepted opportunities, and below 0.1% at least 2,995. The denominator is neither all 600 Test cases nor repeated seed predictions; it is the applicable independent accepted subgroup. Cluster dependence, selected thresholds, multiple subgroup claims and distribution shift invalidate a naive application of this simple example. An apparent zero-error result can therefore remain uncertifiable. See the [interval reference](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm).

Freeze the checkpoint/template/candidate handling before Cal-fit; do not turn Cal-policy into a second Dev. When support cannot sustain the separate roles, use only a justified procedure accounting for joint selection or label the policy exploratory. Evaluate final probability quality and policy outcomes on untouched Test.

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

<a id="preflight"></a>
### Training preflight: retain a pass/fail record

- Freeze task/labels/rights and split hashes; verify zero group/duplicate overlap and no later-context/target leakage. Record per-class support and the primary risk/cost/useful-gain limits before scores.
- Pin model/weight identity, processor/template, code, trainable module names/counts, dtype/device and optimizer settings. Inspect which LoRA/readout parameters actually receive gradients; frozen vision must still supply image features.
- Decode several training batches with image dimensions, visual grids/token counts, answer positions/masks and label-to-code mapping; targets must be in supervision only. Report length distribution and every truncation/exclusion instead of silently dropping difficult examples.
- Fit a tiny Train subset as a debugging check; compare image removal/swaps on adjudicated image-essential examples, option permutations with label remapping, padding and unknowns. Tiny-fit success does not establish generalization or a correct visual path by itself.
- Predeclare finite search/seed/step/token/compute budgets, early-stopping rule, development metric and regression cases. Keep augmentation label-preserving and inside Train; record ordinary-versus-hard sampling rather than optimizing only selected hard cases.
- Confirm a supported multimodal training/merge/serving path. Failure at the D3/Intern gate means retain inference baseline or stop C; do not bypass an inference-only wrapper by assumption. No commands in this document have been tested as a training recipe.

<a id="evidence-ablations"></a>
### Evidence ablations before architecture expansion

On the same predeclared independent groups, compare image-only, context-only, OCR+context and full image+context; omit unavailable context explicitly. Keep candidate definitions/guidance and preprocessing budgets fixed. OCR is derived visual evidence, not a no-image-information control. Test logo/template shortcuts with semantics-audited removal or changes; if the changed region is necessary evidence, relabel sufficiency/intent rather than demanding invariance.

For matched visual-change/text-change four-cell tests, adjudicate original, image-only edit, text-only edit and joint edit. A random swapped image can change the correct answer; it must not blindly inherit the label. Distinguish valid meaning-preserving changes from meaning/evidence-changing ones. Add missing/conflicting modalities, natural unknowns/OOS, unseen-template/time challenges and grouped training-size curves. Representative natural-frequency Test and deliberately enriched stress sets keep separate denominators and costs. A synthetic black-box mask is not a complete model of missing evidence.

Run these checks before adding graphs, another encoder, reasoning or an H4 research branch; reuse valid controls for unchanged artifacts while testing genuinely new combinations. Image-invariant outputs can mean either that the task needs no image or that the path is broken; use adjudicated image-essential cases to distinguish them.

## 5. Experiment order and stopping rules

<a id="mac-implementation"></a>
### MacBook M5 Pro: one small image-conditioned adaptation first

This is a conditional implementation plan, not a measured fit/speed claim. [Apple's configuration specifications](https://www.apple.com/macbook-pro/specs/) list 24/48/64 GB M5 Pro paths depending on the chip variant. The target machine's configuration is unconfirmed. Start with one 2B-class 4-bit candidate and microbatch 1; consider 4B only after measured resource headroom and a business/research reason. No 8B training-capacity or completion-time promise follows from the chip name.

| Target unified memory | Planned resource gate |
| --- | --- |
| 24 GB | Keep the first 2B candidate, bounded media cache, checkpointing and microbatch 1; stop or revise if representative longest-input backward/save/reload has unacceptable pressure/swap. |
| 48 GB | Same initial gate; additional capacity may preserve necessary image/context tokens, but must be measured before changing the model/batch. |
| 64 GB | Same initial gate; a 4B arm is conditional on useful headroom and expected value, not required simply because memory is larger. |
| Unknown/other | Confirm the target configuration and run G1 later; do not substitute another connected computer or a model-file size. |

First implementation candidate: `Qwen3-VL-2B-Instruct` in an MLX 4-bit conversion. `Qwen3.5-2B` is a second candidate only if a defined failure/resource issue warrants another arm. Pin **both** the original and conversion repositories, processor/template/config and code; repository revisions identify source/artifact snapshots, not an independent weight-byte audit:

| Candidate | Original HF revision | MLX 4-bit HF revision |
| --- | --- | --- |
| Qwen3-VL-2B-Instruct | [89644892…](https://huggingface.co/Qwen/Qwen3-VL-2B-Instruct/tree/89644892e4d85e24eaac8bacfd4f463576704203) | [9c4f5209…](https://huggingface.co/mlx-community/Qwen3-VL-2B-Instruct-4bit/tree/9c4f5209e57b31f4b9dfba735de3fb983739c9cc) |
| Qwen3.5-2B | [15852e8c…](https://huggingface.co/Qwen/Qwen3.5-2B/tree/15852e8c16360a2fea060d615a32b45270f8a8fc) | [674aaa72…](https://huggingface.co/mlx-community/Qwen3.5-2B-4bit/tree/674aaa7240b91e8012fcad5d791b7dfe5ba90207) |

The four inspected metadata records declare Apache-2.0; [MLX-VLM's code](https://github.com/Blaizzy/mlx-vlm/blob/2ceff4c14b991370a459d14eb49d1bedf4fb9e84/LICENSE) is MIT. Verify the actual artifacts/dependencies/data rights separately. At pinned MLX-VLM `2ceff4c14b991370a459d14eb49d1bedf4fb9e84` (Oct26 2026 23:23:46 UTC), [the training entry](https://github.com/Blaizzy/mlx-vlm/blob/2ceff4c14b991370a459d14eb49d1bedf4fb9e84/mlx_vlm/train.py) is `python -m mlx_vlm.train`; do not copy obsolete `lora.py` examples. The [current training guide](https://github.com/Blaizzy/mlx-vlm/blob/2ceff4c14b991370a459d14eb49d1bedf4fb9e84/docs/training.md) documents local-image JSONL, completion-only SFT and LoRA/quantized-base adapters.

The inspected chain is image-aware [`VisionDataset`](https://github.com/Blaizzy/mlx-vlm/blob/2ceff4c14b991370a459d14eb49d1bedf4fb9e84/mlx_vlm/trainer/vlm/sft/dataset.py) → processor pixels/grid → [`vlm_sft_loss`](https://github.com/Blaizzy/mlx-vlm/blob/2ceff4c14b991370a459d14eb49d1bedf4fb9e84/mlx_vlm/trainer/vlm/sft/runtime.py) shifted input/assistant mask → [Qwen visual embeddings](https://github.com/Blaizzy/mlx-vlm/blob/2ceff4c14b991370a459d14eb49d1bedf4fb9e84/mlx_vlm/models/qwen3_vl/qwen3_vl.py) injected into the language model → [`nn.value_and_grad`](https://github.com/Blaizzy/mlx-vlm/blob/2ceff4c14b991370a459d14eb49d1bedf4fb9e84/mlx_vlm/trainer/common/engine.py). [Default adapter preparation](https://github.com/Blaizzy/mlx-vlm/blob/2ceff4c14b991370a459d14eb49d1bedf4fb9e84/mlx_vlm/trainer/peft/utils.py) freezes the whole base and selects language transformer layers. Thus this is **image-conditioned language-side adaptation with frozen vision**, not text-only training and not visual-tower fine-tuning. No gradients or resource limits have been measured here. Ordinary shifted SFT does not implement Intern's placeholder supervision or Clef's schema head.

| Stage | Planned work and required artifact | Pass / fail / stop |
| --- | --- | --- |
| G0 | Rights/task/annotation audit, independent-group and cost manifests; [split](#sample-size) and [output contract](#output-contract). | Ambiguous/unavailable target or rights: stop that arm before samples are processed. |
| G1 | After execution authorization, 32–64 non-sensitive synthetic/authorized examples for pipeline smoke; a separate 16–32-example Train overfit check; batch/mask/gradient and reload report. | Nonzero visual inputs and expected image-sensitive behavior; finite loss/gradients, changed adapters, unchanged frozen weights and reload parity. These debugging examples establish no business gain. |
| G2 | B0/F0, B1/F1 and bounded B2, at least three fixed seeds; grouped learning curves and error analysis. | No residual learnable gap or no worthwhile gain: retain baseline/stop. Do not implement all research branches at once. |
| G3 | Freeze one selection on Dev, then Cal-fit/Cal-policy and one locked Test; paired business and risk report. | Cost-gain lower bound exceeds `delta_cost`, critical risk and parity pass; otherwise fail/inconclusive. |
| G4 | Only under separate authorization: natural-traffic shadow evaluation with real review costs, user nonresponse and failure accounting. | Offline success does not grant live-data/deployment authorization. |

**Unexecuted G1 example only.** `/local/...` paths are invented placeholders for already pinned local artifacts. No installer, downloader or sample upload is included. `validation.jsonl` contains a Train/Dev-authorized smoke subset or Dev, never Cal/Test. The stable label ID below is synthetic; verify its tokenization in the exact full prompt before choosing it.

```json
{"images":["images/synthetic-status.png"],"messages":[{"role":"user","content":"Classify the synthetic page. Labels: L0=status inquiry; L1=other."},{"role":"assistant","content":"L0"}]}
```

```sh
python -m mlx_vlm.train \
  --model /local/pinned-model --data /local/derived-data \
  --train-type lora --train-on-completions --seed 0 \
  --batch-size 1 --gradient-accumulation-steps 4 \
  --lora-rank 8 --lora-alpha 16 --learning-rate 1e-5 \
  --grad-checkpoint --max-seq-length 2048 --iters 100 \
  --cache-size 4 --steps-per-eval 25 --val-batches -1 \
  --adapter-file /local/run/weights.safetensors
```

These are smoke starting settings, not optimal hyperparameters or a ready-made classifier-head trainer. This version counts `iters` as microsteps: 100 with accumulation 4 gives 25 optimizer updates. Accumulation does not reduce the peak of one microbatch. Inspect actual visual tokens, retained text and completion targets before applying the 2048 limit; never lower resolution until decisive text disappears merely to fit memory. Measure peak MLX/process memory, memory pressure/swap, step/wall time and save/reload on representative longest inputs; 4-bit file size is not training memory, and averages hide length outliers.

Save model/processor/template IDs, dependency lock, split/data hashes, seed, trainable-module list and `adapter_config.json` with the adapter. This version restores weights with a **fresh optimizer and no saved RNG state**, so continuation is not exact resume. Reload the same artifact and compare scores/outputs under predefined tolerances; changed quantization/fusing/export/backend needs a separate parity and calibration gate. Hard-case collection, replay, distillation and feedback remain later, rights-checked options after a diagnosed benefit.

<a id="serving-regression"></a>
### Serving regression after every trained/exported/backend change

| Case | Frozen comparison and failure rule |
| --- | --- |
| Isolated versus concurrent requests | Interleave deliberately different state/questions/options; compare each request with its isolated output at a prespecified numeric tolerance. Check answer-token offsets, row order and cache isolation; another request must never alter option identity. |
| Short/long and image/text mixtures | Verify processor, pixels/grid, truncation side and actual retained evidence; batch padding, missing/corrupt images and near-limit inputs must have explicit counted outcomes. |
| Train/eager, merged/exported and serving artifacts | Same cases/candidate mapping; record logits/probability and label differences, especially near ties. Never assume an adapter merge/export preserves the visual/readout path. |
| Device/precision/quantization/backend | Record each combination independently; dtype/kernel changes can change logits. Revalidate its matched calibrator/policy rather than reusing a temperature silently. |
| Calibration/gates | Pin calibrator ID, fit population, candidate set, entropy/max-probability definition, rejection and reasoning policy; reject mismatched artifacts. |
| Load and failures | Record concurrency/batch/context/image budgets, cold/warm cache, sample count, p50/p95, throughput, memory, timeout/invalid-output rate and retries. Include failures/clarifications in the population and complete cost. |

The [Oct18 runtime review](../updates/2026-10-18-weekly-review.md) documents why request-local offsets and serving/eval preparation matter. This checklist is proposed regression coverage, not a claim that any listed backend passes it. Small timing samples give unstable p95; report counts and workload, not a universal speedup.

## 6. Accept quality, risk and cost together

The primary business measure is total expected cost per independent case: error severity/correction, human review, waiting/latency and compute, with an explicit unit/weight convention that avoids double counting. Define `Delta_cost = mean(C_baseline - C_candidate)` on paired cases. The owner preregisters a minimum useful gain `delta_cost` and critical-risk limits. Success requires the confidence lower bound of `Delta_cost` to exceed `delta_cost` **and** every required high-risk constraint to pass. If review quality/cost or downstream outcomes are assumed rather than observed, disclose sensitivity scenarios and call the result an offline cost proxy, not demonstrated production benefit.

| Dimension | Predefined reporting |
| --- | --- |
| Business, primary | Per-case error/review/latency/compute cost components; paired net reduction and interval versus strongest frozen baseline; minimum worthwhile effect and stop decision. |
| Task, supporting | Macro-F1, each class recall/precision, critical confusions, joint intent/sufficiency/action correctness; multilabel/unknown/OOS/insufficient separate. |
| Selective policy | Cost/risk–coverage curves, useful coverage at the same critical-risk ceiling, accepted errors/accepted independent cases, false refusals and review/clarification burden. |
| Uncertainty | Paired cluster bootstrap at the preregistered case/conversation/user unit when support permits; seed variability reported separately, not pooled as independent cases. |
| Probability / OOS | Frozen-Test Brier/NLL/ECE and defined bins, OOS AUROC/operating point and scorer costs; independent probability fitting and policy selection. |
| Shift / system | New customer, template, time, language and evidence conditions separately; complete P50/P95, peak memory/pressure/swap, failures/retries, cold/warm cache and hardware/batching. |

At least three preregistered training seeds expose instability; select any single deployable candidate or fixed ensemble using Dev before calibration, never the best Test seed. Apply the same paired case resamples across systems; do not multiply sample size by seeds, paraphrases or repeated screenshots. Predeclare the primary contrast, interval level and finite exploratory comparison family; adjust confirmatory multiple comparisons or mark them exploratory. Report rare-group support and sensitivity to the clustering choice. Bootstrap uncertainty for average cost does not automatically certify a high-risk tail or shifted population.

Use Cal-fit only for the frozen artifact's probability mapping, Cal-policy for its finite preregistered policy/threshold family, and locked Test for one confirmation. [Learn then Test v5](https://arxiv.org/html/2110.01052v5) frames risk control as valid hypothesis tests plus family-wise error control; an applicable loss/risk definition, valid p-values, independence/data assumptions and accounted-for selection are required. It does not license arbitrary threshold search or certify future template/time shift. Choose the method and its failure fallback before seeing Test. The [zero-error count example](#sample-size) is an adequacy check, not a calibration certificate.

Stop scaling when targets/rights are unresolved, the visual/label path fails, parity differs, critical risk is unsupported or cost gain fails the minimum. Keep negative/inconclusive results. Any later shadow evaluation or deployment needs separate authorization and a new operational protocol; no real requests were processed here.

Treat calibration, error ranking and classification quality as separate measurements. [Guo et al.](https://proceedings.mlr.press/v70/guo17a.html) fit temperature on held-out calibration data; a common positive temperature preserves the fixed-candidate argmax. The [UAI 2024 confidence study](https://proceedings.mlr.press/v244/cattelan24a.html) motivates separate risk–coverage/AURC evaluation, but its ImageNet score choices are not validated defaults for dynamic-candidate VLMs. D3/API `confidence >= 0.9` does not imply error <= 10% on accepted domain cases; check the actual statistic and returned policy.

The [pinned D3 package](https://huggingface.co/vllm-sr/d3/blob/225be8b1e2270becab69c5fe05b26f99cbbdd66b/d3_runtime.py) defines choice/score confidence as one minus normalized entropy for multiple candidates, not an estimated probability that the selected label is correct. Other backends can use different definitions. Separate probability-map fitting from threshold certification, or use a procedure accounting for adaptive choices; repeatedly choosing models, temperatures and gates on one calibration set does not inherit an untouched-calibration guarantee.

[Conformal Risk Control](https://proceedings.iclr.cc/paper_files/paper/2024/hash/f3549ef9b5ff520a7e41ff3cc306ab2b-Abstract-Conference.html) controls expected risk under exchangeability and bounded monotone-loss conditions. It is not a per-item or arbitrary fixed-calibration-set high-probability guarantee. Accepted-set error can be non-monotone in a threshold, so standard CRC cannot be attached automatically. Choose a method matching the risk definition and data dependence; validate again after routing, candidate reduction or distribution shift.

Final comparisons keep the preregistered per-case cost endpoint and risk constraints above; lower ECE, ONNX parity or a favorable seed alone is not acceptance.

The Oct14 [risk-budgeted System One preprint](https://arxiv.org/html/2610.19811v1) studies binary policies: score `s(X)` predicts a positive event, Action 0 on `s(X) < tau` has `FOR = P(Y=1 | s(X)<tau)`, and Action 1 is the conservative fallback. Its fixed-sequence LTT result requires a frozen scorer/ordered threshold family derived from Fit independently of iid Cal from the same deployment population. With error level delta, the probability over calibration samples of certifying a population-risk-violating policy is bounded by delta. This is not each answer's probability of correctness, a promise that every finite test estimate stays below budget, or an automatic multiclass/image/shift guarantee. No certificate means fallback for the policy, distinct from per-input abstention. Six English-text datasets/single seed are author evidence; no local replication or numeric gain is claimed.

## 7. Minimum research deliverables

Treat three levels separately: **engineering reproduction** means identified code/artifacts and the visual/gradient/reload path actually ran; **rigorous application evidence** means locked, leakage-audited, matched business improvements with uncertainty and failure disclosure; **possible mechanism contribution** additionally needs a novelty check and stronger controlled evidence. Successful LoRA fitting alone establishes none of the latter two, and no paper or breakthrough is promised.

Only after the first-pass image/adaptation benefit, open one candidate question: **at the same backbone, annotation and optimization-step budgets, does semantic-preserving paired supervision plus necessary-evidence missing/conflict supervision improve unseen-template/time coverage under a fixed error-risk ceiling over ordinary LoRA with strong post-hoc scoring/calibration and a budget-matched Rep2Act transfer arm?** This is a falsifiable, novelty-to-check proposal, not a confirmed innovation.

Compare equal-volume ordinary augmentation, semantic-preserving pairs only, evidence-changing pairs only, and their combination. Split original groups first; derivatives inherit the parent partition. Missing necessary evidence changes the sufficiency/action target and may change intent identifiability: adjudicate it rather than demanding the old label. Do not manufacture every missing case with a black rectangle and teach that shortcut. Use natural gaps/conflicts and multiple audited transformations. Cross training methods with fixed scorers, and frozen representations with changed scorers; if a distance scorer removes the advantage, do not claim a representation breakthrough.

[Rep2Act/VAD-R](https://arxiv.org/html/2609.32653v1) already combines answerability heads/LoRA and action alignment; [VLTest](https://arxiv.org/html/2610.30794v1) motivates four-cell perturbation controls. [The Oct12 text-intent personalization preprint](https://arxiv.org/html/2610.20652v1) reports OOS rejection damage and scorer-dependent recovery, so temperature/energy/Mahalanobis controls on the same adapted backbone are required when technically meaningful; its text-only results do not establish VLM effects. [EMNLP 2025 decomposition work](https://aclanthology.org/2025.emnlp-main.949/) already uses structured interaction summaries before small-model intent extraction; a decomposed pipeline is not by itself new. Read against the existing [novelty protocol](multimodal-decision-research-protocol.md), without requiring its interactive/causal branches for this static study.

Retain preregistration, rights and independent-group/split manifests, label disagreements, exact models/code/templates, dependency lock, all seed/search attempts, learning curves, ablations, scores, uncertainty, complete costs and stop decisions. Public artifacts are limited to the plan/protocol, non-sensitive synthetic examples and specifically authorized aggregate results. Images, annotations, logs and adapters can all reveal sensitive information and are not uploaded by default. This page releases no dataset, weights or results; [E01–E36](evidence.md) remain historical source claims.

<a id="result-template"></a>
### Copyable experiment/result record

One row per run and population; fill planned fields before running, leave unmeasured values blank, and retain rejected/failed arms. All placeholders below are generic; store real artifacts privately unless explicitly publishable.

| Field | Required content |
| --- | --- |
| Identity / plan | Run ID, hypothesis, parent comparator, sole changed factor, intended population, owner-set maximum critical risk/complete cost, minimum useful cost reduction and supporting coverage target, stop rule and search budget |
| Data / labels | Local manifest/split hashes, label version/mode/definitions, evidence cutoff, rights, group/duplicate audit, per-partition class/group counts and annotation disagreements |
| Artifacts / training | Exact base/weights/code/processor/template/readout; trainable modules, LoRA rank, loss/Brier normalization/weight, seed, optimizer/LR/steps/examples/tokens, sampling/replay and used label access |
| Policy / calibration | Frozen candidate order/reduction, probability/confidence definition, Cal-fit/Cal-policy membership, calibrator/gate/threshold IDs and fit time; assumptions and certificate status (or no certificate) |
| Quality | Macro-F1 with label list/undefined rule; each class TP/FP/FN/support/recall interval, confusion matrix; multilabel/unknown/OOS/insufficient and critical errors separately; format/timeouts included |
| Selective behavior | Accepted errors / accepted count, accepted / all eligible requests, clarification/handoff and failure fractions; grouped paired difference and interval versus the frozen baseline; representative/stress/shift results separate |
| Probability | Test NLL/Brier conventions/ECE bins; if an arm lacks usable class probabilities, mark not available rather than fabricate them from its verbal confidence |
| Cost / regression | Hardware/dtype/device/backend, batch/concurrency/image/context budgets; complete p50/p95/throughput/cost/memory/counts, queue/retries/OCR/review; serving-regression pass/fail and parity tolerance |
| Outcome / limits | Predefined pass/fail/inconclusive decision, limiting classes/groups, failed checks, next single-factor change, review date and new holdout requirement after test-guided changes |

Aggregate all images/turns, model calls, evidence processing and retries/review/correction to the independent case before comparing total cost; fix the rule for multiple errors within a case beforehand. Show measured counts/unit prices and assumed-cost sensitivity separately. Report intent quality and the frozen accept/clarify policy; higher macro-F1 alone does not establish net business gain. Keep seed/fold variability distinct from case-sampling uncertainty; an interval is not a deployment guarantee.

<a id="decision-tree"></a>
### Continue, collect, repair or stop

```mermaid
flowchart TD
    A[Freeze task, labels and evidence] --> B{Identifiable and reliable labels?}
    B -- No --> C[Clarify evidence or revise taxonomy]
    B -- Yes --> D{Independent support and clean splits?}
    D -- No --> E[Collect groups or narrow claims]
    D -- Yes --> F[Run B0, B1 and D0]
    F --> G{Learnable domain gap after error audit?}
    G -- No --> H[Retain baseline or repair evidence/tools]
    G -- Yes --> I[B2; B3 or C only after gates]
    I --> J{Frozen test risk, gain, cost and parity pass?}
    J -- No --> K[Stop expansion; report inconclusive/failure]
    J -- Yes --> L[Plan separately authorized shadow evaluation]
```

Training stops early for leakage, ambiguous targets, broken visual/readout paths, non-finite loss or serving mismatch. Expansion stops when the preregistered useful-gain/risk/cost criteria fail or are not estimable. After the finite Dev search, do not keep trying models on Test until one passes. If B2 adds no useful gain, retain the stronger baseline; B3, C, distillation and reasoning are optional hypotheses, not an obligation to keep increasing complexity.

<a id="reading-list"></a>
## 8. Layered reading list and what to borrow

Publication status and evidence strength are separate axes. Peer review does not make results independent of model authors or prove transfer to this domain. This repository reviewed sources and did not run these models. Use the papers for testable design choices, not a combined leaderboard.

### Peer-reviewed papers

| Formal title / venue | Useful implementation question | Evidence boundary |
| --- | --- | --- |
| [Organizer competition overview](https://doi.org/10.1145/3701716.3719642) — WWW Companion 2025 | Task/resource definitions, three-team methods and composite award table; full text now reviewed. | Organizer report, not an independent ablation; exact online values come from the stage-specific official board, not an inferred final score. |
| [EcomMIR: Towards Intelligent Multimodal Intent Recognition in E-Commerce Dialogue Systems](https://doi.org/10.1145/3701716.3718371) — WWW Companion 2025 (Companion Proceedings of the ACM Web Conference 2025), four-page challenge solution | CN-CLIP scene classification with Greedy Soup; MiniCPM-V 2.6 intent LoRA, hierarchical labels/cleaning and pseudo-label selection. | Author combined-system competition report, not a WWW main research-track study or isolated LoRA effect. Round 1 unlabeled test inputs enter training: a transductive component, not a 1,000-example-only supervised protocol. This does not establish Round 2 leakage. See [E28](evidence.md#e28). |
| [MIntRec2.0: A Large-scale Benchmark Dataset for Multimodal Intent Recognition and Out-of-scope Detection in Conversations](https://openreview.net/forum?id=nY9nITZQjc) — ICLR 2024; [official repository](https://github.com/thuiar/MIntRec2.0) | Intent/OOS labels and multi-party, multi-turn text/audio/video context; in-scope and outlier-exposure objectives. | Television conversations are not support screenshots or a LoRA experiment. Repository body inspected; OpenReview verification blocked full-paper access in this review. |
| [RLAIF-V: Open-Source AI Feedback Leads to Super GPT-4V Trustworthiness](https://openaccess.thecvf.com/content/CVPR2025/html/Yu_RLAIF-V_Open-Source_AI_Feedback_Leads_to_Super_GPT-4V_Trustworthiness_CVPR_2025_paper.html) — CVPR 2025 | Visual factuality checks, AI preference construction and DPO-style preference learning; audit teacher feedback before distillation. | Author alignment results concern visual response trustworthiness, not domain intent utility. Later repository LoRA support does not make every paper result LoRA. Dataset NC/research-use notices and base/API terms require review. |
| [LLaVA-Critic: Learning to Evaluate Multimodal Models](https://openaccess.thecvf.com/content/CVPR2025/html/Xiong_LLaVA-Critic_Learning_to_Evaluate_Multimodal_Models_CVPR_2025_paper.html) — CVPR 2025 | Fine-tune LLaVA-OneVision with pointwise/pairwise critic instructions and CE over judgments/justifications; inspect GPT-4o-assisted label bias. | A generative visual critic is not a direct candidate-logit classifier or domain-outcome validator. Do not infer uninspected adapter/full-parameter settings or use its own teacher agreement as gold. |
| [VL-RewardBench: A Challenging Benchmark for Vision-Language Generative Reward Models](https://openaccess.thecvf.com/content/CVPR2025/html/Li_VL-RewardBench_A_Challenging_Benchmark_for_Vision-Language_Generative_Reward_Models_CVPR_2025_paper.html) — CVPR 2025 | Check whether a judge detects visual evidence failures on curated, human-verified preference cases. | A benchmark, not a training recipe. Source pools include RLAIF-V/RLHF-V: audit example/image/source overlap before treating it as held out. Benchmark-author evaluation is distinct from this repository reproducing it. |
| [On Calibration of Modern Neural Networks](https://proceedings.mlr.press/v70/guo17a.html) — ICML 2017 | Fit temperature on separate calibration data and assess probability quality. | Fixed-candidate argmax/top-1 accuracy does not improve from a common positive temperature; deployment/shift calibration remains empirical. |
| [How to Fix a Broken Confidence Estimator: Evaluating Post-hoc Methods for Selective Classification with Deep Neural Networks](https://proceedings.mlr.press/v244/cattelan24a.html) — UAI 2024 | Distinguish accuracy from error ranking and evaluate risk–coverage/AURC. | The 84-ImageNet-classifier study does not establish the best confidence score for dynamic labels or VLMs. |
| [Conformal Risk Control](https://proceedings.iclr.cc/paper_files/paper/2024/hash/f3549ef9b5ff520a7e41ff3cc306ab2b-Abstract-Conference.html) — ICLR 2024 | Match bounded-loss, monotonicity and exchangeability assumptions to a precisely defined risk. | Expected-risk control is not a per-decision correctness promise; arbitrary accepted-set conditional error is not automatically covered. |
| [Small Models, Big Results: Achieving Superior Intent Extraction through Decomposition](https://aclanthology.org/2025.emnlp-main.949/) — EMNLP 2025 | Structured interaction summaries before small-model intent extraction are prior work, not a novel decomposition here. | Metadata/abstract reviewed; UI trajectories differ from single screenshots. No numerical result or complete artifact audit imported. |

### Preprints and engineering assets

| Source / status | What it establishes | Open question |
| --- | --- | --- |
| [Calibration and Risk-Budgeted Decisions with System One Models](https://arxiv.org/html/2610.19811v1) — arXiv v1, 2026-10-14 | Specify binary FOR, fixed scorer/threshold family, independent Fit/Cal/Test and conservative fallback before LTT certification. | Author-reported six English-text datasets/single seed; calibration-sample population-risk control is not per-item correctness or an image/multiclass/shift guarantee. |
| [Intern-Decision: Efficient Multimodal Decision Making with Autoregressive Masked Language Modeling](https://arxiv.org/html/2610.22131v1) — arXiv v1, 2026-10-15 | Image-bearing full-language training and a multi-field causal masked readout, with frozen vision/projector. | Text-suite metrics and qualitative visual examples do not supply a matched D3 multimodal comparison or a LoRA result; full raw training-data release not established. |
| [StartLux-Decision: AutoThink Decision Models with Reinforcement Learning for Calibrated Deliberative Decisions](https://arxiv.org/html/2610.17309v1) — arXiv v1, 2026-10-12 | Candidate probabilities, adaptive reasoning and policy-aware calibration; [mechanism audit](decision-readout-and-reasoning.md). | Public DI development selection, author-built DecisionPivot and NC weights constrain interpretation and use; not a demonstrated domain image-training recipe. |
| [MIRE: Multimodal Intent Recognition for Dialogue Systems challenge baseline](https://github.com/liujunwen23/MIRE/tree/d101287af90d114c5bf0cbfbd56fe9c52358e3bb) — WWW2025 challenge engineering repository | Qwen2-VL-7B **full SFT** baseline for scene/intent tasks. | This is not EcomMIR's implementation, a LoRA result, or a separate peer-reviewed method paper verified here. |
| [Vis Decisions 0.6.1 D3 path](https://github.com/Blockether/vis-decisions/blob/d73768e3c18d89d11f6b9a774b87d64ccd55f27d/src/blockether/vis_decisions/_d3_trainer.py) — third-party engineering | Text full/LoRA plus trainable code head and merged export implementation. | Removed vision tower; not verified multimodal adaptation or an independent benchmark reproduction. |
| [Learn then Test](https://arxiv.org/html/2110.01052v5) — v5, 2022-09-29 | Freeze the risk/loss, valid tests and finite policy family before calibration. | Relevant method reviewed; guarantees depend on assumptions and multiplicity control, not arbitrary drift. |
| [Leakage and the Reproducibility Crisis in ML-based Science](https://arxiv.org/html/2207.07048v1) — v1, 2022-07-14 | Audit independence, future information, development selection and model/data information sheets. | A methodological reference, not verification of this proposed dataset or split. |
| [Does Personalization Break Trust?](https://arxiv.org/html/2610.20652v1) — v1, 2026-10-12 | Hold the scorer fixed while changing adaptation, then hold representation fixed while changing scorer. | Text-intent author study; pseudo-OOS/forgetting and incomplete recovery limit transfer. No VLM score, local run or code-license verification imported. |

For experimental allocation and uncertainty, use the [official grouped/time CV documentation](https://scikit-learn.org/stable/modules/cross_validation.html) and [NIST binomial-interval reference](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm) with their stated assumptions; neither establishes this dataset's independence or sufficient size.

Read in order: domain intent adaptation → OOS/clarification → visual feedback → candidate/critic scoring → judge checks → calibration and rejection. Peer-reviewed methods can inform an experiment without proving that fine-tuning will improve its target decision. Review depth, versions and access gaps are in the [source register](sources.md).
