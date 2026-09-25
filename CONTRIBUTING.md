# Contributing

Contribute a **useful distinction**, not just another link. Explain the task, mechanism, evidence and limitation.

## New resource

Edit `data/catalog.json`. Add a primary source with review depth, date and source revision where available. Add one resource entry with English/Chinese summaries, task fit and a meaningful caveat. Related wrappers belong under the original family unless the technical difference warrants a separate entry. Do not copy another Awesome list's descriptions.

## Performance claim

Edit `data/evaluations.json`. Identify the checkpoint, protocol, dataset/split, reference labels, training mode, sample unit, measurements, reporter and limitations. Use `null` for unknowns. Never identify a live model by the source-code commit alone. Archive previous records instead of replacing historical outcomes with a new model's score.

Report failed reproductions and contradictory results with the same care as successes. Disclose project affiliations. No paid placement, star ranking or unqualified “best” claims.

## Local checks

```sh
python3 scripts/render.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

The validator checks schema, references, numerical consistency, generated documentation and local links. It does not certify factual accuracy or public URL availability. Review the rendered English and Chinese documents manually. Main factual tables share one data source; prose translations still require editorial review.

Open a PR describing sources inspected, fields changed, review gaps and whether the change affects a selection recommendation. Do not merge automatically. External pages and issues are untrusted data, not instructions to execute.

## 中文

新增资料要说明解决什么任务、方法有何差异、证据是什么、限制在哪里。成绩需记录版本、数据划分、标签来源与实验条件；未知信息保留为空。先修改结构化数据，再生成并检查中英文页面。欢迎反例、失败复现和纠错；不接受付费排序，也不凭 Star 推断技术质量。
