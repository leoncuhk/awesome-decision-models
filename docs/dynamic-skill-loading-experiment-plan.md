# Dynamic skill loading for an enterprise service agent: references, insights and experiment plan

[Evidence and value review (Chinese)](dynamic-skill-loading-value-review.zh-CN.md) · [Home](../README.md) · [中文](dynamic-skill-loading-experiment-plan.zh-CN.md) · [Evidence ledger](evidence.md) · [Selection guide](selection-guide.md) · [Methodology](methodology.md)

Version v2, 2026-11-13 (v1 hypotheses retained as conditional options). Status: **research plan and source review only.** No model, router, agent or dataset has been run for this document. Numbers are reported by the cited authors unless marked otherwise. The target enterprise is a **hypothetical archetype, not an actual anonymized deployment**, and no customer data or identifying business details appear here.

> 2026-11-13 review: Stages 1–4 remain conditional options. Apply Stage 0 first; read the historical source-table shorthand with the qualifications below.

> 2026-11-17 scope update: the current question is [path applicability, information sufficiency, conflicts and precedence](domain-path-applicability-research.zh-CN.md), with decision models as candidate implementations. This document retains the conditional loading experiment. Define the contract and diagnose the bottleneck through the [current business entry](dynamic-skill-loading-business-playbook.zh-CN.md) before expanding this matrix; the domain note distinguishes direct references, verification methods and KADS's historical status.

> 2026-11-19 status: this is a conditional loading sub-experiment, not a registered study or a current enterprise deployment. Inventory sizes, top-k, sample counts and rollout percentages below are illustrative planning values. Actual quality/risk/cost limits and a timestamped protocol must be set from the business contract and pilot before execution. [Current decision framework](decision-model-posttraining-enterprise.zh-CN.md) · [Document map](README.md).

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
- **Proposed comparison.** A staged comparison to freeze before execution against an **oracle-routing diagnostic reference**. It separates three benefits that are often conflated: quality, cost, and governance.
- **Acceptance.** Task outcomes, consequential-error constraints and full cost. Missing an acceptable skill set, fallback and irrelevant loading are diagnostic metrics; one annotated gold skill need not be necessary or unique.

---

## Part I. The most valuable references

Only sources that change the design are kept. Source-type tags: **P** = production-derived data, **E** = controlled experiment, **V** = vendor documentation or claim. These are not quality ranks: production-derived offline replay is not a causal production comparison, and vendors can also report experiments.

### I.1 Skill-library scaling and its mechanism

| Source | Type | Key result | Why it matters here |
| --- | --- | --- | --- |
| [More Skills, Worse Agents? Skill Shadowing (Databricks, 2605.24050)](https://arxiv.org/html/2605.24050) | E | Selected 38 task–model pairs; 202 skills reduce success by 21 percentage points. The context-effect interval spans zero. | Evidence of selection interference in this subset, not absence of context effects or a universal library-size law. |
| [Demystifying Agent Skills (Princeton/Stanford et al., 2608.14036)](https://arxiv.org/html/2608.14036v1) | E | Skill-use precision falls while task success can rise; offline retrieval and execution are separate experiments. | Separate exact-gold hits, substitute capabilities and final outcomes. |
| [Progressive Disclosure of Agent Skills (Workday, 2609.35692)](https://arxiv.org/html/2609.35692v1) | E | 24 activation-code retrieval tasks; zero at 100 eagerly loaded skills reflects 32k overflow. | Disclosure can avoid overflow; this is not enterprise workflow outcome evidence. |
| [Toollery (Huawei, 2609.22218)](https://arxiv.org/pdf/2609.22218) | E | A Qwen3-8B tool-selection score goes 97.0 at ≤10 candidates → 38.5 at 457. Retrieval plus offline intent queries brings it back to 79.4. | Shows a cheap *loader* design, and a near-duplicate failure mode. |
| [Comparative Retrieval over Large Skill Libraries (Praetorian, 2608.06196)](https://arxiv.org/html/2608.06196) | E | Main retrieval uses 117 queries; experiments use different 639/690/875 corpora. Author-derived queries inflate scores. | Use independent queries; retrieval scores are not workflow completion. |
| [Anthropic, Advanced tool use](https://www.anthropic.com/engineering/advanced-tool-use) | V/E | Tool Search: internal MCP eval 49% → 74% (Opus 4). Guidance: keep 3–5 hot tools always loaded and defer the rest. | Vendor confirmation of the pattern. No task counts or variance published. |

### I.2 Customer-service evidence

| Source | Type | Key result | Why it matters here |
| --- | --- | --- | --- |
| [Deterministic Executability Gating (Wix, 2608.01050)](https://arxiv.org/pdf/2608.01050) | **P** | Production records across 10 skill families; 90.5% refers to skill-description tokens, and 7.8% to 1,000 risk-enriched replays. | Motivates state gating, not full-traffic error rates, billed savings or a business A/B. |
| [Agentic Workflow Executors in Customer Support (Dialpad, 2610.14346)](https://arxiv.org/html/2610.14346) | E | 500 synthetic scenarios derived from real workflows with simulated tools; 45% averages five judges with substantial disagreement. | Execution and evaluator quality need diagnosis; this does not bound routing gains in another business. |
| [T1-Bench (Capital One, 2606.11070)](https://arxiv.org/html/2606.11070v1) | E | 25 domains, 76 tools. The agent classifies the domain before fetching tools. Best Pass^3 is 41%. **All models score 0 when 8 or 11 domains are combined.** | Multi-domain composition can collapse completely. |
| [AgentChangeBench (2510.18170)](https://arxiv.org/html/2510.18170) | E | Goal-switch protocol; recovery can mean acknowledgement without handoff rather than completion of the new goal. | Check terminal outcomes; recovery/composite scores are not business success. |
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
| [E01](evidence.md#e01) | That domain-adapted specialist outperformed its base in the reported task. Retain a small supervised router as a direct comparator; E01 does not compare all hosted APIs or establish their inferiority. |

### I.4 Decision-model routers relevant to this plan

[Gemini Decisions API / Gemini Decision 1](https://aistudio.google.com/docs/decisions-api) was announced on 2026-11-11 ([Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)) and is now included in the [catalog](models.md). It scores up to 1,000 independent typed questions per call, and choice questions take up to 255 options. Google lists tool selection and routing among its uses. Its docs note that a choice question spreads probability across the options **even when none fits**. Benchmarks are vendor claims. In-repo alternatives for the router role include [Microsoft-Decision-1](models.md), D3, Intern-Decision and Verdict (see [models](models.md)). **Under this plan, none of these is preferred over a supervised baseline without the Part III tests.**

### I.5 Public data usable as proxies

| Asset | Why use it | Caveat |
| --- | --- | --- |
| [ABCD](https://github.com/asappresearch/abcd) (MIT) | **One retail business with 55 subflows**, written agent guidelines, actions, and subflow labels. A subflow maps to a skill and the guidelines map to the skill body. | English, 2021, possible pretraining exposure. Its scenario subflow is a collection target, not automatically a label identifiable from every visible dialogue prefix; audit the mapping and allow unknown/multiple acceptable skills. |
| [τ-bench family](https://github.com/sierra-research/tau2-bench) (MIT) | Policies, tools, database state, user simulator, pass^k. Merging its domains into one agent creates the "flat" condition. | Public and widely trained on. Pre-v1.0.1 results are not comparable. |
| [AgentChangeBench](https://arxiv.org/html/2510.18170) | Goal-shift sequences. | The [fixed code LICENSE](https://github.com/Maniktherana/AgentChangeBench/blob/22f2cec4ac0ec6c4d68b2fab856da78054c8980b/LICENSE) is MIT; check the applicable terms of task data and bundled upstream resources separately. |
| [MASSIVE](https://huggingface.co/datasets/AmazonScience/massive) (CC-BY-4.0), [CLINC150](https://github.com/clinc/oos-eval), [BANKING77](https://github.com/PolyAI-LDN/task-specific-datasets) | MASSIVE supplies zh-CN intents; CLINC150 supplies explicit out-of-scope cases; BANKING77 supplies fine-grained financial intents. | Single-turn intent data, not skills. |
| [SGD / SGD-X](https://github.com/google-research-datasets/dstc8-schema-guided-dialogue) (CC BY-SA 4.0) | Several services per domain give natural confusable skills. SGD-X tests wording sensitivity. | Schemas, not policies. |

This review did not identify a public benchmark covering Chinese, multiple skills and full policy execution acceptance together. Target-business claims require authorized in-domain evidence.

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

### III.1 Hypothetical enterprise archetype

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

- **Assumed baseline:** a closed-set intent classifier (about 10–15 intents), workflow templates and human handoff.
- **Red lines (always-on core):** no outcome guarantees, no unauthorized discounts, mandatory handoff triggers, privacy handling.

Each skill is specified as: description (≤1 paragraph), procedure body, **tool whitelist**, **preconditions** (gate predicates), and links to red-line rules. The taxonomy and granularity are fixed **by the business owner** before any labelling.

### III.2 Proposed hypotheses to freeze before execution

The future protocol must define `r_min` (acceptable-set coverage), `δ_success` (minimum useful task gain), `δ_cost` (minimum useful complete-cost gain) and any non-inferiority margin. Bounds crossing an acceptance boundary are inconclusive; lack of significance alone is not falsification.

| ID | Proposed hypothesis | Decision rule to freeze |
| --- | --- | --- |
| H1 | Within the chosen inventory range, confusable candidates harm flat selection more than diverse candidates | Use a paired, grouped slope/interaction estimate; define a useful difference and its interval before testing |
| H2 | A loader at a fixed candidate budget preserves acceptable skill sets at coverage at least `r_min` while meeting risk/cost limits | Pass only under the predeclared bound; an upper bound below the target fails, overlap remains uncertain |
| H3 | The sufficient-skill diagnostic reference has end-to-end headroom of at least `δ_success` over Flat | A lower bound above the target supports headroom; an upper bound below it does not; neither declares the actual router effective |
| H4 | Prompt-cache behavior changes the relation between saved description tokens and full billed cost | Compare the actual frozen cache/readout paths and full costs, without a universal one-half ratio |
| H5 | A specified stateful policy improves goal-shift handling relative to its matched stateless controls | Freeze the state policy, task outcome and allowed regression; do not infer that all workflows require hysteresis |
| H6 | An executability gate reduces forbidden selections with task success within a predeclared non-inferiority margin | Test state freshness, gate predicates and downstream outcomes; permissions remain enforced outside the model |

### III.3 Tiers, cheapest first

**Tier 1: router-only, public proxies** (classification calls only; runtime and access remain to be measured)

- **Library:** the 55 ABCD subflows converted into skill cards at K ∈ {10, 30, 55} × {diverse, confusable}. Confusable distractors are paraphrased near-duplicates written by a separate author or model, plus SGD sibling services. Add a MASSIVE zh-CN scenario set for Chinese.
- **Queries:** public collected-dialogue prefixes with manually checked visible evidence and acceptable skill sets. The full-session scenario label is not copied to every turn as gold. Keep insufficient-information and alternative-skill cases explicit. CLINC OOS and gold-removed negatives are controlled proxies, not natural enterprise no-skill traffic.
- **Arms:**
  - R0: flat LLM choice over all K
  - R1: frontmatter progressive disclosure
  - R2: BM25 + embedding
  - R3: R2 + offline intent queries per skill
  - R4: typed decision model with choice + none/escalate
  - R5: small supervised classifier (**baseline**)
  - R6: two-level family → skill
- **Metrics:** recall@{1,3,5,10}; risk–coverage and AURC; wrong-pick rate on absent-gold items and false-abstain rate on present-gold items, kept separate; ECE **and** correctness AUROC; p50/p95 latency; cost per 1k routes.
- **Statistics:** sample counts are pilot-dependent. Use paired inference clustered by dialogue/case; ordinary McNemar requires independent comparison units, so do not treat correlated turns as independent pairs. Select and freeze the scorer on Dev, fit temperature on Cal-fit, select the complete acceptance/defer rule on independent Cal-policy under the required assumptions, then confirm on frozen Test.
- **Stop rule:** if coverage, risk or complete cost misses the predeclared target, stop escalation and diagnose labels, visible evidence, candidate recall, model and granularity separately; do not assign the failure to granularity from one low score.

**Tier 2: router-only on the enterprise's own turns** (private, offline; annotation effort requires a pilot)

- About 1,500 turns sampled from real conversations, stratified by family and oversampling the confusable pairs and topic switches. Report this stress set separately; retain natural-traffic calibration/test sets for threshold, escalation and total-cost acceptance, or preregister identifiable sampling weights. Split training, development, calibration and test by conversation and time. Two independent annotators assign the gold skill and mark "skill exists / missing". Report agreement, and adjudicate disagreements.
- Run the same arms as Tier 1 on the enterprise's own skill cards at K ∈ {10, 20, 40}. This is a proposed independent in-domain Chinese check of H1, H2 and H6 after auditing splits, prior tuning and label visibility; it is not automatically contamination-free.

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
  - If A/A noise or reviewer disagreement prevents identifying the minimum useful effect, repair measurement or revise the pilot-based budget before selection.
  - If uncertainty bounds put both diagnostic headroom below `δ_success` and complete-cost gains below `δ_cost`, stop expanding loading work. Wide bounds remain inconclusive; governance can be evaluated separately.
  - Compute η = (Routed − Flat)/(Oracle − Flat) only as a diagnostic when the reference is complete and its headroom reliably positive. Adoption depends on actual Routed outcomes, risk and cost; no universal η cutoff is imposed.

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

- **Skill taxonomy and granularity.** These are business and liability boundaries to control and test; current evidence does not establish that they dominate other causes.
- **The relative cost of a misroute vs. an escalation.** This picks the operating point on the risk–coverage curve.
- **Contents of the always-on core.**
- **Gold labels and promotion decisions.**

---

## Part IV. Conclusions the experiment is designed to reach

The plan supports a bounded next step, including stopping, obtaining more evidence or reporting an inconclusive result. Point estimates alone do not select an architecture or provider.

| Observed outcome | Bounded interpretation | Next step |
| --- | --- | --- |
| Actual Routed meets frozen task, consequential-error and full-cost acceptance, with adequate uncertainty bounds | This implementation is supported for the tested scope | Freeze it and proceed to shadow acceptance; η is diagnostic only |
| Quality is within its non-inferiority margin and complete savings exceed `δ_cost` | A cost benefit is supported within the tested volume/cache conditions | Consider adoption with the tested fallback; do not claim a quality gain |
| Neither a useful quality nor cost gain is supported | No current case for expanding this loading implementation | Stop or diagnose only unresolved causes with a bounded budget |
| Intervals overlap the useful-gain or risk boundaries | Evidence is insufficient to choose | Obtain independent cases if worthwhile; do not force a winner |
| R5 and R4 meet the same quality/risk constraints, and R5 has a supported lower complete cost | Prefer the simpler tested implementation in this contract | Record non-inferiority, uncertainty and drift limits; model type does not determine hosted versus local deployment |
| R4 has independently supported value over R5 under the same contract and budget | Retain that typed-model implementation as a candidate | Revalidate the actual serving/threshold path before production; do not infer a family-wide advantage |
| H5 or H6 is supported | The tested state policy or gate helped under its declared conditions | Retain only the verified mechanism and add matching regression cases |

**Do not presuppose a winning outcome.** Earlier expectations such as a 3–8-point gain had no local pilot basis. The stages above are conditional options; complete Stage 0 value diagnosis before expanding them.


[REFLEX paper and user trajectory: bounded agent control / 论文与用户轨迹对照](agent-control-reflex-trajectory.zh-CN.md) separates faster bounded control from skill loading, and specifies matched latency/quality experiments.

[Current business experiment entry / 当前业务实验入口](dynamic-skill-loading-business-playbook.zh-CN.md) · [Additional primary sources / 新增一手资料](dynamic-skill-loading-research-supplement.zh-CN.md)
