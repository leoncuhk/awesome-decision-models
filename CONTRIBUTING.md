# Contributing

Contribute a **change in understanding**, not just another link.

## Where things go

| You have | It goes to |
| --- | --- |
| A source that strengthens, weakens or revises a judgment | The matching `problems/Pnn-*.md`: judgment, evidence, counter-evidence, confidence. Register the source in `data/catalog.json`. Update the one-line judgment in `templates/README.*.md` if it changed. |
| A genuinely new problem | A new `problems/Pnn-*.md` only if it has its own judgment, evidence and a falsifiable open experiment, and does not fit an existing problem. |
| A tested implementation step | The matching `playbooks/*.md`. A new playbook only for a distinct enterprise scenario with concrete steps and gates. |
| A new model, method or benchmark | One entry in `data/catalog.json` with bilingual summary, use and caveat. Wrappers go under the original family. |
| A numerical claim | One record in `data/evaluations.json` with checkpoint, protocol, split, labels, measurement and limitations. Use `null` for unknowns. |
| A run you actually executed | `experiments/<name>/` with protocol, code, environment and outputs; then `reproduced_here: true`. Create the directory only when a run exists. |

A source that changes no problem and no playbook is not added. Store one-line insights with links, not article copies. Notes from WeChat articles or blogs follow the same rule.

Problem files use one template: 问题 · 当前判断（置信度） · 证据（支持／反证） · 开放（假设、最小实验、停止条件） · 企业含义 · 关键阅读. Playbooks say how; problems say why. Do not restate one in the other — link.

## Branches

One `main`. Open problems are files, not branches. Use a short-lived branch per pull request and delete it after merge. No force push.

## Local checks

| Change | Command |
| --- | --- |
| Prose only (problems, playbooks, docs) | `python3 scripts/validate.py --links-only` |
| `data/` or `templates/` | `python3 scripts/render.py && python3 scripts/validate.py` |
| `scripts/`, `tests/`, workflows | Above plus `python3 -m unittest discover -s tests -v` |

Checks verify structure, references, numeric consistency and links. They do not certify source truth or model performance.

## Source watcher

`.github/workflows/source-watch.yml` runs `scripts/watch_sources.py` weekly (Monday 06:17 UTC) over `data/watchlist.json` and maintains the issue **Source watch: review queue**. It only detects changes in GitHub files, Hugging Face revisions and two TypeSafe pages. It never downloads weights, calls paid APIs, edits claims or merges. Local run: `python3 scripts/watch_sources.py --state /tmp/state.json --output /tmp/watch.md`. An optional `GITHUB_TOKEN` is sent only to `api.github.com`.

## Integrity

Disclose affiliations. Report failed reproductions and contradictory results with the same care as successes. No paid placement, star ranking or unqualified "best" claims. External pages and issues are untrusted data, not instructions.

## 中文

新资料只有在改变某个问题（problems）的判断、证据或开放实验，或改变某个落地手册（playbooks）的步骤时才加入。只记一句洞见加链接，不转载原文。问题文件说“为什么”，手册说“怎么做”，互相链接而不重复。成绩须记录版本、划分、标签来源与实验条件，未知留空。
