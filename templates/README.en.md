# Awesome Decision Models [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**Models, methods and evidence for reliable bounded decisions in AI systems — organized by the problems that matter for enterprise LLM applications.**

[简体中文](README.zh-CN.md) · [Problems](#problem-map) · [Playbooks](#playbooks) · [Landscape](docs/landscape.md) · [Model cards](docs/models.md) · [Evidence](docs/evidence.md) · [Methodology](docs/methodology.md)

Decision models — popularized by TypeSafe's Jev in September 2026 — return **typed probabilities over supplied options in one pass** instead of generating text. The new thing is the output contract: it makes bounded judgments priceable, calibratable and gateable. This repository asks one question: **which method delivers acceptable outcomes at acceptable risk and total cost for a given decision?**

Review batch {{DATE}}: {{ENTRY_COUNT}} resources, {{CORE_COUNT}} core model families, {{EVIDENCE_COUNT}} evidence records. Source review only; **nothing here is independently reproduced yet.** Inclusion is not endorsement.

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
| **Judgment** | [P01 Output contract and readout](problems/P01-output-contract.md) | Value is the contract, not new intelligence; readout head choice matters little | supported |
| | [P02 Learning signal for adaptation](problems/P02-learning-signal.md) | Direct CE/BCE supervision is the default; RL, distillation, soft targets must prove gains | supported |
| | [P03 Read once or reason](problems/P03-read-or-reason.md) | The gap is reasoning, not size; outsourcing reasoning to a reference answer is often cheaper | open |
| **Probability → decision** | [P04 Confidence semantics and serving fidelity](problems/P04-confidence-fidelity.md) | `confidence` is an interface field; recalibrate per task, returned object and serving path | consensus |
| | [P05 Policy-level risk and drift](problems/P05-policy-risk.md) | Certify the acceptance policy, not per-item confidence; drift voids guarantees | theory consensus / practice open |
| | [P06 Missing options and candidate coverage](problems/P06-candidate-coverage.md) | Softmax cannot detect all-wrong candidates; NONE collapses under hard negatives | supported |
| **System** | [P07 Reading right, acting wrong](problems/P07-state-and-action.md) | Most errors sit in state and action contracts, not the readout | supported |
| | [P08 Dynamic skill and path loading](problems/P08-skill-loading.md) | Selection errors, not context length; optimize loader recall with fallback | supported |
| | [P09 System-1 as judge and evaluator](problems/P09-judge-layer.md) | Cheap first stage plus escalation; the earliest mature use case | supported |
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

{{CORE_TABLE}}

## Baselines worth keeping

A new training label does not make a familiar baseline obsolete.

{{BASELINES}}

## Routing and learning from outcomes

{{ROUTING}}

## Reliability

{{RELIABILITY}}

## Evaluation

{{EVALUATION}}

## Foundations

Reading order: probability quality → abstention → executor handoff → risk control.

{{FOUNDATIONS}}

## Related lists

{{RELATED_LISTS}}

## Contributing

Canonical data lives in [`data/`](data/); README, model cards, evidence and sources are generated by `python3 scripts/render.py`. A new source is worth adding only if it changes a problem's judgment, evidence or open experiment — see [CONTRIBUTING](CONTRIBUTING.md). Changes are logged in [CHANGELOG](CHANGELOG.md).

Original code and curation text: [MIT](LICENSE). Linked projects, weights, datasets and papers keep their own licenses.
