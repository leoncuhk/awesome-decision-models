# Changelog

Each entry records what changed in the repository's knowledge, not every edit. Pre-2026-11-21 dated review notes (`updates/`) and retired documents can be recovered from tag `archive/pre-restructure-2026-11-21/main` or `…/research-dynamic-skill-loading-2026-11` with `git show <tag>:<path>`.

## 2026-11-25 · First-principles learning-to-practice checklist

- Replaced the generic implementation-step table with12 checkable tasks in the existing pipeline: problem/architecture/sample tracing,data and baselines,native training qualification,gradient/save checks,controlled adaptation,calibration,frozen testing and business validation.
- Each task has a deliverable or gate. Distinguishes toy/debug checks,software correctness,held-out model gains and production outcomes;conditional teacher/distillation/reasoning/RL work follows diagnosed failures rather than a fixed upgrade chain.
- Planning/synthesis only;no task marked completed,no enterprise data or training run created.

## 2026-11-25 · Perplexity v1.3 enterprise continuation qualification

- Reviewed official training/evaluation report and complete native27B release. Classified v1.3 as a strong candidate requiring a differentiable training adapter,not an executable original training recipe. Added concrete data,gradient/mask,head,calibration,export and GPU gates in the existing pipeline.
- Corrected one-request/one-forward and isolated-question independence claims. Locate remains a separate adapter/forward path;continued backbone training requires renewed extraction qualification. v1.1 trainer is not protocol-v4 compatible by model-name substitution.
- E47 distinguishes LLM-relabeled query accuracy and production judge agreement from human gold,domain adaptation and business outcomes. Existing46 evidence records preserved;no model training/inference or customer-data access.

## 2026-11-25 · Keep only the two accepted structure diagrams

- Retained the layered backbone and readout comparison plates as SVG sources plus PNG previews (four files). Removed the superseded01–04 flow diagrams, their Mermaid sources and obsolete render config after a verified recovery archive.
- Updated current links and captions; kept the scientific explanations, version-pinned sources and original external figure URLs. Prior files remain recoverable from Git commit0868acf and the locally verified backup receipt.

## 2026-11-25 · Neural-network structure plates

- Replaced flow-oriented diagrams as the primary visual entry with two layered neural-network plates: embedding/decoder stack/residual blocks/linear operators, and four aligned readout structures with tensor shapes and trainable parameter boundaries.
- Kept prior data-flow/computation diagrams as auxiliary material. PRDO retains its vocabulary head and original causal backbone; no unsupported Qwen3.5 attribution or new classifier head.
- SVG and PNG inspected; existing pinned architecture evidence reused. No model execution.

## 2026-11-25 · Qwen architecture and decision-training deltas

- Added four editable Mermaid/SVG/PNG diagrams in the existing landscape: dense Qwen backbone, residual block, synchronized Kev/Valen/Adjudex readouts,and PRDO main-stage computation graph. Linked official Qwen-Next and PRDO originals with variant boundaries.
- Pinned configs distinguish dense Qwen3.5-4B/3.8-27B from MoE family marketing. Source checks distinguish Kev hybrid causal rows,Valen four-role Mixer and released decision-question visibility,Adjudex255-slot initialization,and parameter-selection modes.
- PRDO keeps its original causal LM/vocabulary head. No-grad discrete sampling differs from differentiable recomputation; labels feed only the loss,reference stays frozen,and shared parameters update. Qwen3 experiments are not labeled Qwen3.5.
- Documentation and rendered-figure checks only; no model training/inference or new effectiveness claim.

## 2026-11-23 · Coverage-first small-model selection

- Corrected the familiar-project selection bias: screen all346 fixed DI configurations by3–6.5B total served parameters, yielding69 candidates with explicit access/review gaps. Small-model CSV records score, tie group, exact current artifact and training eligibility; current artifacts are not automatically the benchmark's original weights.
- Added Adjudex4B v7's native full-weight continuation and Chinese Decision Pointer4B's native LoRA/head preservation, with E46's frozen comparison. Original45 evidence records preserved. Higher-scoring weights with restricted rights or no established trainer remain in the coverage record rather than silently disappearing.
- Selection now distinguishes high-score training qualification from ready LoRA workflows and target-Mac portability; no new inference/training or enterprise performance claimed. The goal is a stable, conditional experimental shortlist, not another universal winner.

## 2026-11-23 · Enterprise fine-tuning audit and conditional implementation choices

- Rechecked the current problem/playbook structure; retained one home per judgment. The pipeline now gives a hardware-conditional first experiment and four concrete receipts, rather than a new global model ranking.
- Corrected Unsloth qualifications: MLX includes nonquantized full-finetuning as well as LoRA; quantized training has narrower constraints. Pinned calibration reporting uses two-fold row cross-fitting, not simply in-sample reporting. Tiny/mocked tests do not prove real Qwen/VLM or target-Mac training. The prior November21 “first/default/LoRA-only” claims should be read with this correction.
- Lemon weights, inference code and data are public; a complete trainer/direct native-checkpoint continuation path was not established. Retracted the stronger training-code availability claim while retaining the dataset and inference reference.
- Separated independent multi-label BCE from alternative valid action sets; unified evaluation compares the business policy first and only compares proper scores for matching probability semantics. Scoped per-skill thresholds, soft-label rules and reasoning/size claims; removed the unsupported50% cascade cutoff.
- PRDO main-stage token KL is distinct from the inactive score-function KL coefficient; direct-answer SFT is the paper baseline. Added Inner Jev v2 and GLiDE v1 training/ablation evidence without replacing historical results or claiming a new algorithm winner.
- Source/static review only. No weights downloaded, model training/inference, enterprise data access, target-M5 measurement or production claim.

## 2026-11-23 · Decision input format and data views

- Decision pipeline §4: layered input structure (current turn, recent turns, summary, business state, options), a history-window ablation, truncation and leakage notes, and the rule that the master dataset is canonical while Unsloth and paper formats are derived views.

## 2026-11-21 · Readout paradigms, LemonDecider, harness collaboration

- Sources: three WeChat articles (readout paradigms; LemonDecider; JevRSI) checked against primary sources, plus the SGLang decisions docs, NanoJev, JevAgentHarness and System1-Arena found while verifying them.
- Added entries: LemonDecider 4B (core), SGLang `/v1/decisions` and NanoJev (baselines), System1-Arena (evaluation), JevAgentHarness and JevRSI (routing).
- Landscape: readout-paradigm × engineering-constraint table. Decision pipeline: zero-training and Harness control arms in step 1, LemonDecider and SGLang candidate rows, data hygiene and replay guidance. P01/P02/P03/P07/P12 and the skill-routing playbook updated.

## 2026-11-21 · Method views, PRDO and unified evaluation

- Decision pipeline: added a table that maps each method (decision-head CE, teacher soft, generative SFT, GRPO, DPO/KTO, PRDO, partial feedback) to its extra data, inference contract, training compute and implementation. Each training view is derived from one master dataset with one frozen split.
- Added how to run PRDO (mechanism, data, base, code paths, resources, controls) and a unified evaluation protocol.
- Maintenance: direct commits to `main` after local checks; pull requests only for external contributions.

## 2026-11-21 · Unsloth decision-model training

- Source: a WeChat translation of the Unsloth guide, checked against the official docs and the pinned source (`8b7cde79`).
- Added the Unsloth `FastDecisionModel` / `DecisionTrainer` entry. It is now the default implementation for the LoRA arm in the [general pipeline](playbooks/decision-pipeline.md) and the B3 decision-head arm in [multimodal post-training](playbooks/multimodal-posttraining.md). It is also the first public decision-head trainer with an Apple Silicon path.
- Updated P02 (hard/soft and anchoring are one-parameter ablations), P11 (an image-conditioned decision-head trainer exists) and P12 (a training entry is no longer scarce; license becomes the gate).
- Boundaries recorded: random row holdout reused for calibration; vendor-only benchmarks; AGPL-3.0-only decision modules.

## 2026-11-21 · Reorganize by field problems and playbooks

- Knowledge layer: [problems/](problems/) P01–P12, one field problem per file with judgment, confidence, evidence, counter-evidence and open experiments. This replaces dated notes, theses and research branches.
- Implementation layer: [playbooks/](playbooks/): general [decision pipeline](playbooks/decision-pipeline.md) (merged selection and enterprise post-training guides), [multimodal post-training](playbooks/multimodal-posttraining.md) (restored from PR #5 and condensed), [skill routing selector](playbooks/skill-routing.md) (restored from the dynamic skill-loading plan).
- Reference: new [landscape](docs/landscape.md); model cards now cover every entry; README keeps mechanism and suggested experiment only.
- Retired: 25 `updates/` notes (summarized below), multimodal survey and protocol (now P10), MIRE case study (now P11), branch review, document map, `VALIDATION.md`, publishing script, manifest. PR #5, PR #6 and `research/jev-utility-2026-11-13` were folded in and closed.
- Added: Artificial Analysis Decision Index v2, *To Jev or Not to Jev* (arXiv 2611.00505), *Reading Right, Acting Wrong* (arXiv 2610.18579).

## 2026-11 (before restructure)

- **11-20 release coverage**: the model pool had missed releases; core families grew from 22 to 35. Clairic was added as adjacent typed extraction. New weights, catch-up entries and old omissions were recorded separately.
- **11-20 enterprise consolidation**: 15 post-training documents merged into one guide. Adoption order: direct supervision, then verified teacher labels, then PRDO for reasoning-preserving subtasks. CAPS and RLAF were held in reserve with explicit reopen conditions.
- **11-20 conversation fact check**: no new leaderboard picks a default winner; CAPS and PRDO require their own feedback and reasoning contracts.
- **11-19 customer-service implementations**: Parlant, Modem and Entagl reviewed at the source level; 12 isolated Parlant protocol observations kept.
- **11-19 enterprise post-training**: citation audit of the enterprise route; Amazon multi-turn intent study added (E43, E44).
- **11-17 domain path applicability**: path applicability, information sufficiency, conflict and priority separated as distinct judgments.
- **11-13 Jev utility**: high-frequency, evidence-complete, finite-answer and reversible judgments are where value appears. Gemini Decision 1 added.
- **11-01**: confidence policies and serving fidelity; risk-budgeted LTT preprint; Drex Max.

## 2026-10

- **10-26**: image-intent fine-tuning support and evidence supervision; D3-Turbo shared-state audit.
- **10-25**: joint requests, adaptation correctness and abstention; HF Decision Index 0.4 moved text Full to private items.
- **10-22**: multimodal research survey (heterogeneous repair actions proposal; now Q4).
- **10-18**: runtime correctness, benchmark identity, risk budgets; E32.
- **10-17**: StartLux v1.1 and DecisionPivot (E29–E31); D3 text-only training path clarified.
- **10-16**: multimodal fine-tuning research guide; MIRE/EcomMIR, ezjev, decision-pacman added.
- **10-15**: native vLLM D3, Index 0.3.2 scoring changes, semantic-feature pipeline.
- **10-13**: Decision 3.0, Intern-Decision, Verdict, FluidUse; E12–E20.
- **10-11 / 10-06 / 10-02**: Clef, Strands Decider, Perplexity Decider; release identity rules.

## 2026-09

- **09-30**: jevos contribution (PR #1) reviewed.
- **09-25**: initial source review: task-first map, seven core families, five evidence records, source register, watcher.
