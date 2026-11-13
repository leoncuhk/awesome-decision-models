# Protocol illustrations, not a benchmark

Read the [business playbook](../../dynamic-skill-loading-business-playbook.zh-CN.md) first. All eight JSONL cases are fictional examples authored for this repository; no customer data is included. Policy `subscription-demo-v1` is the fictional policy in that playbook.

- `input`: information visible before the decision; missing/unknown state remains null.
- `acceptable_capability_sets`: alternative sufficient sets, each inner list is conjunctive. They describe required capabilities for a possible episode, not immediate authorization for writes. These examples have one set each; real annotation may have multiple valid sets.
- `forbidden_actions`: invariants checked across the full episode, not simply against the router label.
- `expected_terminal_assertion`: intended outcome identifier; a future harness must implement its explicit state/communication checks. It is not executable test code.
- `run-record.json`: a blank reporting contract, with all measurements null. Replace with a separate run record; retain raw results privately where needed. Fill data/model/runtime/skill revisions before comparing runs.

The fixtures do not provide skill implementations, model adapters or an experiment runner. Parse checks verify format only. They must not be used to claim accuracy, calibration, ROI, or production readiness.
