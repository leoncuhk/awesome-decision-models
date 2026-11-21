# Changelog

Each entry records what changed in the repository's knowledge, not every edit. Pre-2026-11-21 dated review notes (`updates/`) and retired documents can be recovered from tag `archive/pre-restructure-2026-11-21/main` or `…/research-dynamic-skill-loading-2026-11` with `git show <tag>:<path>`.

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
