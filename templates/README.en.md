# Awesome Decision Models [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**Models, methods and evidence for reliable decisions in AI systems.**

[简体中文](README.zh-CN.md) · [Model cards](docs/models.md) · [Evidence ledger](docs/evidence.md) · [Selection guide](docs/selection-guide.md) · [Methodology](docs/methodology.md) · [Sources](docs/sources.md)

A curated guide to systems that **classify, score, rank, verify, route or abstain** rather than primarily generate prose. The central question is not which model has the most impressive headline, but **which method delivers acceptable outcomes at acceptable risk and total cost for a particular task**.

**Source review: {{DATE}}.** {{ENTRY_COUNT}} selected resources, including {{CORE_COUNT}} core model families and {{EVIDENCE_COUNT}} contextualized evidence records. This edition reviews public sources; **it does not claim independent model reproduction**. Review depth and unresolved gaps are recorded in the [source register](docs/sources.md). Inclusion is not an endorsement or a production-readiness certification.

## Contents

- [Start with the task](#start-with-the-task)
- [Core models](#core-models)
- [Baselines worth keeping](#baselines-worth-keeping)
- [Routing and learning from outcomes](#routing-and-learning-from-outcomes)
- [Reliability and evaluation](#reliability-and-evaluation)
- [Foundations and recent research](#foundations-and-recent-research)
- [Related lists](#related-lists)
- [Maintenance and contribution](#maintenance-and-contribution)

## Start with the task

Here, **decision model** is an organizing label, not a claim that all these projects form one new, unified discipline. *Typed decisions* describes an output contract; *System One* is terminology used by some projects; *RLCD*, contrastive learning and supervised classification are different training approaches. Routing and selective prediction concern what the system does with a judgment.

| Your bottleneck | A useful starting comparison | Do not confuse it with |
| --- | --- | --- |
| Understand a message or check a bounded requirement | Typed models, label classifiers and a supervised baseline | Optimizing the effect of a downstream action |
| Choose among many reusable candidates | Dual encoders, rerankers and domain-trained selectors | Proving the best available candidate is correct |
| Choose an executor: model, tool or person | Routing and learning to defer, using actual executor outcomes | A generic task-difficulty score |
| Decide whether to automate | Held-out calibration, risk–coverage evaluation and abstention | Trusting a field named `confidence` |
| Learn which action improves an outcome | Contextual bandits or suitable causal methods | Predicting correlations from historical logs |

These are **curatorial starting points, not measured winners**. See the [selection guide](docs/selection-guide.md) for the decision contract and a minimal evaluation plan.

## Core models

The table compares mechanisms and use cases, **not incompatible benchmark scores**. Each row links to primary material; version-specific details and licensing notes are in the [model cards](docs/models.md).

{{CORE_TABLE}}

### Read these results in context

{{EVIDENCE_LINKS}}

**No combined accuracy leaderboard:** zero-shot classification, workflow fine-tuning and Best-of-N selection answer different questions. Local GPU forward time and remote API round-trip time are also different measurements.

## Baselines worth keeping

A new training label is not evidence that a familiar baseline is obsolete. These alternatives help isolate gains from the data, output contract, architecture and training objective.

{{BASELINES}}

Also retain a deterministic rule or ordinary supervised classifier where the task permits. A model should earn its complexity against the simplest credible alternative.

## Routing and learning from outcomes

{{ROUTING}}

For executor selection, collect **task, available evidence, executor, outcome, latency and cost**. Observed success for one selected executor does not reveal how every alternative would have performed. See the learning-to-defer and causal references below.

## Reliability and evaluation

{{RELIABILITY}}

{{EVALUATION}}

A useful scorecard includes task quality, consequential errors, calibration, risk–coverage, subgroup/shift behavior and full-system cost. Fix the acceptance threshold on calibration data, not on the final test set. Keep sampling automatically accepted cases so confidently wrong decisions remain visible.

## Foundations and recent research

Reading order: probability quality → abstention → executor handoff → risk control. Dates are publication/version dates, not a claim of exhaustive coverage of the latest literature. Abstract-only reviews are labeled in the source register.

{{FOUNDATIONS}}

## Related lists

These maintainers provide complementary discovery paths. This repository adds a task-first comparison and claim-level evidence records; it does not copy their collections or sort by stars.

{{RELATED_LISTS}}

## Maintenance and contribution

The factual catalog lives in [`data/catalog.json`](data/catalog.json); numerical claims live in [`data/evaluations.json`](data/evaluations.json). Generated Markdown must stay synchronized with those records.

```sh
python3 scripts/render.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

A [repository-scoped curator skill](.agents/skills/decision-models-curator/SKILL.md) defines the research/review procedure. A [weekly source watcher](.github/workflows/source-watch.yml) checks selected sources for changes and maintains an issue for review. **It does not run an AI researcher, update scientific claims, merge changes or require a paid model API.** See [maintenance](docs/maintenance.md) for setup, security, scheduling limits and manual use.

Read [CONTRIBUTING](CONTRIBUTING.md) before adding a project or result. Negative findings, changed assumptions and corrections are welcome. [Initial review notes](updates/2026-09-25.md) preserve the original qualifications; the [October 6 release review](updates/2026-10-06-release-boundaries.md) records the latest additions, corrections and remaining gaps. [Publishing instructions](PUBLISHING.md) explain how to initialize an empty repository safely.

Original code and curation text: [MIT](LICENSE). Linked projects, model weights, datasets and papers retain their own licenses. A source-text revision does **not** pin a model's weights.
