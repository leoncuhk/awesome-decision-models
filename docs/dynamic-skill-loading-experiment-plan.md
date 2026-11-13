# Dynamic skill loading for an enterprise service agent: references, insights and experiment plan

[Evidence and value review (Chinese)](dynamic-skill-loading-value-review.zh-CN.md) · [Home](../README.md) · [中文](dynamic-skill-loading-experiment-plan.zh-CN.md) · [Evidence ledger](evidence.md) · [Selection guide](selection-guide.md) · [Methodology](methodology.md)

Version v1, 2026-11-12. Status: **research plan and source review only.** No model, router, agent or dataset has been run for this document. Numbers are reported by the cited authors unless marked otherwise. The target enterprise is described as an **anonymized archetype**, and no customer data or identifying business details appear here.

> 2026-11-13 review: Stages 1–4 remain conditional options. Apply Stage 0 first; read the historical source-table shorthand with the qualifications below.

### Stage 0: establish a remediable bottleneck

Compare the incumbent, statically pruned/metadata-first loading, an adjudicated sufficient-skill diagnostic reference, and simple retrieval with fallback. Freeze executor, policy, visible evidence and caching. Use a small authorized real-task diagnostic set, reporting natural traffic and stress cases separately. If the reference does not improve outcomes, repair execution/evaluation first; if static pruning suffices, do not build a loader; if simple retrieval passes acceptance, use existing components. Expand the matrix only after multi-turn omissions/interference demonstrably affect task utility. Size and thresholds require pilot evidence and business costs, not universal assumptions about 40 skills, recall .98 or fixed percentage-point gains.

### Primary-source qualifications from this review

- Skill Shadowing v2 retains 38 task/model pairs with at least 4-point isolated skill benefit; the 202-library drop is 21 percentage points. Non-significant context effects are not absent; Sonnet context point estimates are at least as large as shadowing.
- Demystifying reports precision29.6→3.3 alongside success36.4→39.3; offline retrieval is not fed into the execution arm.
- Workday eager-loading zero at100 skills is32k overflow; its24 activation-code retrieval tasks do not measure business execution.
- Wix7.8% is conditional on1000 risk-enriched conversations;90.5% counts only skill-description tokens in a ten-skill family, not overall bills.
- Dialpad45.0% averages five judges, ranging33.8–58.6 for that model; deterministic checks give90.6%. Its500 synthetic scenarios/mocked tools do not establish production completion.
- Comparative Retrieval uses different corpus sizes639/690/875 across measurements; headline retrieval has117 queries and measures neither task completion nor latency.

## 0. Summary

- **Question.** For one enterprise whose service agent covers *dozens* of skills, does routing each turn to a small scoped set of skills (dynamic loading) beat exposing every skill at once, on task success, policy violations and billed cost?
- **Evidence boundary.** Some studies show selection and task-success degradation as libraries grow; others show worse retrieval without worse task success. Diagnose context, candidate confusion and execution separately. These sources do not establish that this enterprise needs dynamic loading.
- **What this plan adds.** A staged, preregistered comparison against an **oracle-routing diagnostic reference**. It separates three benefits that are often conflated: quality, cost, and governance.
- **Acceptance.** Task outcomes, consequential-error constraints and full cost. Missing an acceptable skill set, fallback and irrelevant loading are diagnostic metrics; one annotated gold skill need not be necessary or unique.

---

## Part I. The most valuable references

Only sources that change the design are kept. Grades: **P** = production data, **E** = controlled experiment, **V** = vendor documentation or claim.

### I.1 Skill-library scaling and its mechanism

| Source | Grade | Key result | Why it matters here |
| --- | --- | --- | --- |
| [More Skills, Worse Agents? Skill Shadowing (Databricks, 2605.24050)](https://arxiv.org/html/2605.24050) | E | Pass rate drops by up to 21% going from a few helpful skills to 202. **Up to 68% of the drop is wrong-skill selection.** The context-overhead effect is indistinguishable from zero. | Puts the problem in *selection*. Making context cheaper alone will not fix it. |
| [Demystifying Agent Skills (Princeton/Stanford et al., 2608.14036)](https://arxiv.org/html/2608.14036v1) | E | From a pool of 5 to 100 skills, actual-use precision falls **29.6% → 3.3%**. With similar distractors, embedding top-1 falls 70.5% → 53.4%. | **Similarity between skills** hurts more than count. Experiments need confusable libraries, not just larger ones. |
| [Progressive Disclosure of Agent Skills (Workday, 2609.35692)](https://arxiv.org/html/2609.35692v1) | E | Eager loading collapses to 0 at 100 skills. Frontmatter-first loading recovers 0.79–1.00 with up to 81.7% fewer tokens, at +15% latency. Some cells are non-monotone. | The remedy works, but measures retrieval only, on synthetic skills. |
| [Toollery (Huawei, 2609.22218)](https://arxiv.org/pdf/2609.22218) | E | A Qwen3-8B tool-selection score goes 97.0 at ≤10 candidates → 38.5 at 457. Retrieval plus offline intent queries brings it back to 79.4. | Shows a cheap *loader* design, and a near-duplicate failure mode. |
| [Comparative Retrieval over Large Skill Libraries (Praetorian, 2608.06196)](https://arxiv.org/html/2608.06196) | E | 690 enterprise skills: hybrid BM25 + embedding hit@5 = 0.735. A skill graph **hurt** by 11.2 pts. **Queries written by the authors inflated hit@5 by 21–44 pts.** | Methods warning. Evaluation queries must come from users or independent writers. |
| [Anthropic, Advanced tool use](https://www.anthropic.com/engineering/advanced-tool-use) | V/E | Tool Search: internal MCP eval 49% → 74% (Opus 4). Guidance: keep 3–5 hot tools always loaded and defer the rest. | Vendor confirmation of the pattern. No task counts or variance published. |

### I.2 Customer-service evidence

| Source | Grade | Key result | Why it matters here |
| --- | --- | --- | --- |
| [Deterministic Executability Gating (Wix, 2608.01050)](https://arxiv.org/pdf/2608.01050) | **P** | 757k customer-care messages. A state-predicate gate removed 59.4% of the candidates left after semantic matching, and skill-description context fell 90.5% in total. With all skills exposed, the model chose a skill production would have blocked in **7.8%** of 1,000 replays. | The only production CS number. It supports a **code gate after the router**. It measures selection, not outcomes. |
| [Agentic Workflow Executors in Customer Support (Dialpad, 2610.14346)](https://arxiv.org/html/2610.14346) | E | 80 skills mined from about 350k real transcripts. **Even with the correct skill given**, the best model passes 45.0%, and the best open model under 20B, 21.6%. | Routing is not the whole problem. It sets a ceiling on what loading can contribute. |
| [T1-Bench (Capital One, 2606.11070)](https://arxiv.org/html/2606.11070v1) | E | 25 domains, 76 tools. The agent classifies the domain before fetching tools. Best Pass^3 is 41%. **All models score 0 when 8 or 11 domains are combined.** | Multi-domain composition can collapse completely. |
| [AgentChangeBench (2510.18170)](https://arxiv.org/html/2510.18170) | E | Goal shifts mid-dialogue on τ-bench domains. Recovery ranges from 92.2% to 48.6% depending on model and domain. | Topic switching is the hard case for per-turn routing. |
| [CRM-Agent-Bench (Salesforce, 2610.32004)](https://arxiv.org/html/2610.32004) | E | 555 tasks, 9 domains, per-turn graph routing to a scoped capability. Strict success 64–84%. | The closest public harness design to this plan (release not confirmed). |

### I.3 Router-evaluation lessons from this repository's ledger

| Entry | Lesson |
| --- | --- |
| [E20](evidence.md#e20) | Missing-option abstention recall: 75.5% → 18% with hard negatives, and → 10% with synonyms added. Test the "none / escalate" option against **near-miss skills**. |
| [E34](evidence.md#e34) | Wrong picks and false abstentions trade off. Report both, each with its own denominator. |
| [E35](evidence.md#e35) | Calibration took ECE from 54% to 2% while correctness AUROC stayed 50%. A low ECE does not make confidence useful for gating. |
| [E37](evidence.md#e37) | Point-estimate thresholds broke in 147 of 190 evaluations. Bounded rules (Learn-then-Test) held empirically but do not transfer under shift. |
| [E19](evidence.md#e19), [E38](evidence.md#e38) | The serving path changes calibration and moves confidences across thresholds. Accept a router only on the exact serving path. |
| [E17](evidence.md#e17) | Errors came from a rule pre-filter the model never saw. Evaluate rule layers as their own component. |
| [E01](evidence.md#e01) | A specialist adapted in-domain was far ahead of its base model. A small supervised router may beat any hosted decision API. |

### I.4 Decision-model routers relevant to this plan

[Gemini Decisions API / Gemini Decision 1](https://aistudio.google.com/docs/decisions-api) was announced on 2026-11-11 ([Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)) and is now included in the [catalog](models.md). It scores up to 1,000 independent typed questions per call, and choice questions take up to 255 options. Google lists tool selection and routing among its uses. Its docs note that a choice question spreads probability across the options **even when none fits**. Benchmarks are vendor claims. In-repo alternatives for the router role include [Microsoft-Decision-1](models.md), D3, Intern-Decision and Verdict (see [models](models.md)). **Under this plan, none of these is preferred over a supervised baseline without the Part III tests.**

### I.5 Public data usable as proxies

| Asset | Why use it | Caveat |
| --- | --- | --- |
| [ABCD](https://github.com/asappresearch/abcd) (MIT) | **One retail business with 55 subflows**, written agent guidelines, actions, and subflow labels. A subflow maps to a skill and the guidelines map to the skill body. | English, 2021, likely in pretraining data. |
| [τ-bench family](https://github.com/sierra-research/tau2-bench) (MIT) | Policies, tools, database state, user simulator, pass^k. Merging its domains into one agent creates the "flat" condition. | Public and widely trained on. Pre-v1.0.1 results are not comparable. |
| [AgentChangeBench](https://arxiv.org/html/2510.18170) | Goal-shift sequences. | License not stated. |
| [MASSIVE](https://huggingface.co/datasets/AmazonScience/massive) (CC-BY-4.0), [CLINC150](https://github.com/clinc/oos-eval), [BANKING77](https://github.com/PolyAI-LDN/task-specific-datasets) | Chinese (zh-CN) intents, explicit out-of-scope, fine-grained near-duplicates. | Single-turn intent data, not skills. |
| [SGD / SGD-X](https://github.com/google-research-datasets/dstc8-schema-guided-dialogue) (CC BY-SA 4.0) | Several services per domain give natural confusable skills. SGD-X tests wording sensitivity. | Schemas, not policies. |

There is no public Chinese, multi-skill, policy-bearing customer-service benchmark. The enterprise's own traffic is required for the decisive tier.

---

## Part II. Insights

1. **Diagnose the bottleneck first.** Similarity can impede identification, while long bodies can overflow or interfere. One study does not establish selection as the universal bottleneck; skill granularity is a variable to test.
2. **Dynamic loading can introduce omissions.** An omission bottlenecks execution when a necessary capability is excluded and alternatives, wider retrieval or clarification cannot recover it. Track acceptable skill sets and task outcomes, not only recall of one gold artifact.
3. **The benefit has three separable parts, each with different evidence.**
   - *Quality*: moderate experimental evidence, and no customer-service end-to-end evidence.
   - *Cost*: description tokens may fall, but include extra calls and fallback. Caching depends on the actual request sequence; Anthropic Tool Search retains stable system/core-tool caching, so dynamic loading does not inherently break it.
   - *Governance*: ownership, versioning, tests and rollback also work with static loading. Do not attribute all modularity benefits to dynamic loading.
4. **Correct selection still requires execution.** Dialpad evaluates judges on synthetic scenarios and mocked tools; it is not a live failure rate or a bound on this system. Use a locally adjudicated sufficient-skill reference to test whether better selection changes task outcomes.
5. **Guardrails must never depend on routing.** Red lines, escalation and identity checks belong in an always-on core enforced in code. Otherwise a misroute also removes the protection.
6. **Code gates are cheap, auditable precision.** Removing skills whose preconditions are false (entitlement, order state, already-applied settings) cut real-traffic candidates by more than half at Wix, without any model call.
7. **A decision model is a candidate router, not a default.** Calibration claims do not carry over to an enterprise's own thresholds (E35, E37), and abstention collapses on near-miss options (E20). The supervised small classifier is the baseline to beat.

---

## Part III. Experiment plan for the enterprise archetype

### III.1 Enterprise archetype (anonymized)

- **Service:** a large Chinese-language consumer subscription service. Text chat on several IM channels. Mixed service and sales conversations.
- **Skill inventory (target about 40), grouped into eight families:**

| Family | Example skills | Known confusable pairs |
| --- | --- | --- |
| Account | login, identity verification, profile change, account closure | closure vs. subscription cancellation |
| Billing and membership | purchase, renewal, payment failure, invoice | renewal vs. auto-renew complaint |
| Refunds and cancellation | refund request, cancellation, downgrade, retention offer | refund vs. cancellation vs. downgrade |
| Orders and appointments | booking, rescheduling, no-show policy | reschedule vs. cancel booking |
| Safety and reporting | report a user, privacy request, fraud warning | report vs. general complaint |
| Product guidance | feature how-to, service explanation | how-to vs. troubleshooting |
| Sales consultation | package comparison, price questions, promotion eligibility | price question vs. discount request |
| Complaints and escalation | complaint intake, human handoff | complaint vs. refund |

- **Current system:** a closed-set intent classifier (about 10–15 intents), workflow templates and human handoff.
- **Red lines (always-on core):** no outcome guarantees, no unauthorized discounts, mandatory handoff triggers, privacy handling.

Each skill is specified as: description (≤1 paragraph), procedure body, **tool whitelist**, **preconditions** (gate predicates), and links to red-line rules. The taxonomy and granularity are fixed **by the business owner** before any labelling.

### III.2 Hypotheses (preregistered)

| ID | Hypothesis | Falsified if |
| --- | --- | --- |
| H1 | Flat top-1 selection degrades with K, and more steeply on confusable libraries than on diverse ones at equal K | No significant slope difference at K=40 |
| H2 | A scoped loader (k=5) reaches recall@5 ≥ 0.98 on independently written queries at K=40 confusable | No loader arm reaches 0.98 |
| H3 | End to end, Oracle − Flat ≥ 5 pp pass^4 at K≈40 | Paired difference < 3 pp |
| H4 | With prompt caching on, Routed's billed-cost advantage is under half its token advantage | Billed ratio ≈ token ratio |
| H5 | On topic-switch dialogues, per-turn routing with hysteresis beats per-conversation routing and memoryless per-turn routing | No difference, or the reverse |
| H6 | A deterministic executability gate cuts blocked-skill selections with no loss in task success | Success drops, or blocked selections do not fall |

### III.3 Tiers, cheapest first

**Tier 1: router-only, public proxies** (hours, classification calls only, local models)

- **Library:** the 55 ABCD subflows converted into skill cards at K ∈ {10, 30, 55} × {diverse, confusable}. Confusable distractors are paraphrased near-duplicates written by a separate author or model, plus SGD sibling services. Add a MASSIVE zh-CN scenario set for Chinese.
- **Queries:** real dialogue turns (gold = subflow). Abstention items come from CLINC out-of-scope plus **gold-removed hard negatives**, following the E20 protocol.
- **Arms:**
  - R0: flat LLM choice over all K
  - R1: frontmatter progressive disclosure
  - R2: BM25 + embedding
  - R3: R2 + offline intent queries per skill
  - R4: typed decision model with choice + none/escalate
  - R5: small supervised classifier (**baseline**)
  - R6: two-level family → skill
- **Metrics:** recall@{1,3,5,10}; risk–coverage and AURC; wrong-pick rate on absent-gold items and false-abstain rate on present-gold items, kept separate; ECE **and** correctness AUROC; p50/p95 latency; cost per 1k routes.
- **Statistics:** about 1,000 items per cell, paired bootstrap clustered by dialogue, McNemar between arms. Thresholds are fitted on a calibration split with Learn-then-Test and reported on held-out data.
- **Stop rule:** if no arm reaches recall@5 ≥ 0.98 at K=55 confusable, redesign the granularity or add a fallback before Tier 2.

**Tier 2: router-only on the enterprise's own turns** (days of labelling, private, offline)

- About 1,500 turns sampled from real conversations, stratified by family and oversampling the confusable pairs and topic switches. Report this stress set separately; retain natural-traffic calibration/test sets for threshold, escalation and total-cost acceptance, or preregister identifiable sampling weights. Split training, development, calibration and test by conversation and time. Two independent annotators assign the gold skill and mark "skill exists / missing". Report agreement, and adjudicate disagreements.
- Run the same arms as Tier 1 on the enterprise's own skill cards at K ∈ {10, 20, 40}. This is the uncontaminated Chinese test of H1, H2 and H6.

**Tier 3: end-to-end with simulated users** (the largest compute tier)

- **Harness:** τ-style tasks written for about 40 enterprise skills, with mock tools and database state. A pilot runs first on merged τ-bench domains to debug the harness.
- **Arms:**
  - Flat
  - Flat with prompt caching (cost only)
  - **Oracle diagnostic reference** (the independently labelled complete set of required skills at each turn, with identical permissions, evidence and executor; include multi-skill dependencies rather than only the family label; no mathematical upper-bound claim)
  - Routed: best Tier-2 loader, k=5, executability gate and always-on core
  - Routed without gate
  - Routed without stickiness
  - Progressive disclosure
  - **A/A** (Flat run twice)
- **Controls:** same model and skill text in every arm; shuffled skill order in Flat; fixed simulator and seed; human audit of about 50 transcripts.
- **Metrics:** pass^4, policy-violation rate, billed cost per resolved task, latency per turn, failures attributed to the loader vs. to execution, and goal-shift recovery.
- **Power:** 300 tasks × 4 trials is an initial budget, not a promised detectable effect. The independent unit for pass^4 is the task. Estimate baseline, paired discordance and task dependence in a separate pilot; preregister alpha, power and multiplicity rules, then size the study using task-level paired power simulation.
- **Stop rules:**
  - If the A/A spread exceeds half of (Oracle − Flat), fix the harness.
  - If Oracle − Flat < 3 pp **and** the billed cost gain is < 20%, quality and cost do not justify dynamic loading. Decide on governance alone.
  - Compute routing efficiency η only when the oracle reference is complete and the lower confidence bound of Oracle − Flat is clearly positive; otherwise report uncertainty. If η = (Routed − Flat)/(Oracle − Flat) is < 0.5, return to Tier 2. Do not reject routing based on an unreliable reference.

**Tier 4: shadow, then canary** (production, after explicit approval)

- **Shadow:** the router runs alongside the existing classifier with no user impact. Disagreements are sampled for human review, and drift is checked weekly.
- **Canary:** about 5% of traffic, with automatic rollback on escalation-rate, complaint-rate or red-line triggers.
- Thresholds are re-validated after any change to the model, serving path or calibrator.

### III.4 Threats to validity

| Threat | Control |
| --- | --- |
| Queries written by the skill authors | Real user turns, or independent query writers |
| Skill-description quality | Identical text in every arm; test wording effects separately (SGD-X style) |
| Contamination in public proxies | Interpret only paired, within-run differences; Tier 2 and Tier 3 on private data are decisive |
| Prompt caching | Always report billed cost with caching on |
| Simulator and judge bias | Fixed models, human audit, reported agreement |
| Thresholds that do not transfer | Learn-then-Test, held-out re-check, re-check after drift |
| Forking paths | Preregister H1–H6, arms, metrics and stop rules; publish negative results |

### III.5 Where human judgment remains

- **Skill taxonomy and granularity.** These are business and liability boundaries, and the evidence says they dominate the outcome.
- **The relative cost of a misroute vs. an escalation.** This picks the operating point on the risk–coverage curve.
- **Contents of the always-on core.**
- **Gold labels and promotion decisions.**

---

## Part IV. Conclusions the experiment is designed to reach

The plan is built so that **every outcome yields a decision**, including null results.

| Observed outcome | Conclusion | Action |
| --- | --- | --- |
| H2 holds, H3 holds, η ≥ 0.7, and actual Routed versus Flat meets preregistered success, policy-violation and full-cost acceptance with uncertainty intervals | Dynamic loading improves service quality at this scale, and the router captures most of the available gain | Adopt routed + gated + always-on core; proceed to Tier 4 |
| H2 holds, H3 fails (Oracle − Flat < 3 pp), H4 shows a real billed saving | The benefit is cost, not quality | Adopt only if the saving matters at volume. Keep Flat with caching as the fallback |
| H3 fails and there is no cost gain | This experiment shows no quality/cost case for dynamic loading; execution as the root cause remains unproven | Stop expanding loader work; diagnose execution, evidence, evaluation and power. Governance can be implemented separately |
| H2 fails on confusable libraries | The current system misses the target; cause remains unresolved | Diagnose labels, visible evidence, candidate recall, model and granularity separately; fix the supported cause and re-run Tier 1 and 2 |
| R5 (supervised) ≥ R4 (decision model) | Hosted decision models are not needed for this router | Use the small local classifier; revisit when the taxonomy changes |
| R4 > R5, with valid held-out thresholds | A typed decision model is worth its cost and dependency | Adopt with per-release threshold re-validation (E19, E38) |
| H5 holds | Topic switching needs stateful routing | Ship hysteresis; add goal-shift tests to regression |
| H6 holds | Code gates may help without another model call; include state-fetch and maintenance costs | Make preconditions mandatory in every skill card |

**Do not presuppose a winning outcome.** Earlier expectations such as a 3–8-point gain had no local pilot basis. The stages above are conditional options; complete Stage 0 value diagnosis before expanding them.


[REFLEX paper and user trajectory: bounded agent control / 论文与用户轨迹对照](agent-control-reflex-trajectory.zh-CN.md) separates faster bounded control from skill loading, and specifies matched latency/quality experiments.
