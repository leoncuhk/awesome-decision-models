# Maintenance / 维护说明

[Home](../README.md) · [Curator skill](../.agents/skills/decision-models-curator/SKILL.md)

## Three separate capabilities

The skill defines **how to investigate**. GitHub permissions determine **what can be read or written**. A workflow defines **when a script runs**. None silently provides the other two. Creating `SKILL.md` does not install a skill into a chat session or run an AI agent on a schedule. Repository-scoped skill discovery depends on the host; see the [OpenAI skill documentation](https://developers.openai.com/codex/skills/).

## What the included watcher does

`data/watchlist.json` selects 12 primary-source endpoints. The watcher checks GitHub file blobs, Hugging Face model-repository revisions and two official documentation pages. These are **change signals**, not semantic reviews. A Hugging Face revision may change only a README; an HTML hash may change because of page rendering.

The first successful run establishes a baseline. Later runs compare against it. Network/API errors preserve the last successful value and are separately reported; partial failure also makes the run fail visibly. The watcher never downloads weights, executes model code, calls a paid AI API, edits scientific claims or auto-merges changes.

### Local report mode

Python 3.10+ is required. No third-party Python package is needed.

```sh
python3 scripts/watch_sources.py \
  --state /tmp/decision-models-state.json \
  --output /tmp/decision-models-watch.md
```

Network access is required for a live scan. Without a GitHub token, public GitHub rate limits apply. An optional `GITHUB_TOKEN` is used **only** for `api.github.com`, not for Hugging Face or TypeSafe. Do not paste tokens into issues, Markdown or chat.

### Scheduled issue mode

The workflow runs weekly on Monday at **06:17 UTC**, or manually with **Actions → Weekly source watch → Run workflow**. It must first be present on the default branch, and GitHub Actions/Issues must be permitted for the repository. These conditions are not established merely by possessing the files.

It uses the automatically supplied workflow token with `contents: read` and `issues: write`. No `contents: write`, model-service secret or personal access token is needed. A bot-owned issue titled **Source watch: review queue** stores the baseline in a machine-readable comment in its body. Material changes/errors are preserved as issue comments, and the body shows the latest check. Keep that issue available; malformed stored state causes a visible failure rather than a silent reset.

Scheduling is best effort. GitHub can delay scheduled runs, and public-repository schedules may be disabled after prolonged inactivity. Check the last successful run instead of assuming the list is fresh. See [GitHub's trigger reference](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows).

## Turn a change into an update

Review the original source and establish whether the change concerns documentation, runtime, weights, calibration, data or a new evaluation. Use the curator skill's procedure. Update canonical records only after inspection; preserve previous evidence and source identifiers. A genuinely changed conclusion belongs in `updates/`, with a reason and the supporting protocol.

The workflow watches known sources; it is **not exhaustive discovery of new papers or projects**. Periodic human/agent research should search for new primary sources, inspect citations and specialist lists, and add useful entries via PR. The initial source register is a bounded review, not a claim of exhaustive coverage.

## Security and validation

The scripts allow only specified HTTPS hosts, refuse redirects, bound response sizes and timeouts, retry reads but not writes, and never execute fetched content. Watcher issue mode is restricted to GitHub Actions. New hosts require an explicit code/config review. CI uses `pull_request`, not privileged `pull_request_target`, and does not pass write secrets to untrusted PR code. The checkout action is pinned to its reviewed `v7.0.1` commit; Dependabot proposes later changes for review.

Offline checks verify data structure, references, numeric consistency, bilingual fields, generated files and local Markdown links. They do not validate benchmark truth or reachability of every external URL. Source-watcher tests use synthetic/mock responses. A passing unit suite is **not** a successful live network run.

## 中文

首版已经包含定期检查的代码，但只有发布到仓库默认分支并允许 Actions／Issues 后才可能执行。第一次运行建立基线，以后报告变化；失败保留上次成功版本。每周运行的是来源检测脚本，不是无人值守的 AI 研究员。

复核时要区分“页面变化”“运行库更新”“权重更新”和“新实验结果”。只有证据支持时才修改结论。新项目发现仍需定期研究，不能仅靠监控现有链接。Skill 文件也不会自动安装到当前对话，更不会自动取得写权限。
