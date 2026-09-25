# Publishing / 发布说明

## 适用范围

本说明用于将完整文件包发布到目标仓库 `leoncuhk/awesome-decision-models`。只有文件实际推送并完成远端验证后，才应声称已发布或定期任务已启用。

在已授权的本地 GitHub CLI 或 Codex 环境中执行。不需要把 Token、密码、SSH 私钥或 API Key 发到对话、Issue 或仓库。账号权限与某个集成应用的权限不同；读取成功不保证该应用可以写入。

## 已有本地 GitHub CLI 授权

需要 Python 3.10+、Git、GitHub CLI，以及你自己配置的 Git 提交身份。进入解压后的 `awesome-decision-models` 目录：

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
bash scripts/publish.sh leoncuhk/awesome-decision-models
```

脚本会显示目标与变更，并在初始化前确认。它只处理**空仓库**，不覆盖已有提交、不强制推送、不修改全局 Git 配置、不自动合并后续 PR。初次建立空仓库需要一个主分支提交；有历史之后，后续修改应通过分支与 PR。

仅检查发布准备情况，不提交或推送：

```sh
bash scripts/publish.sh leoncuhk/awesome-decision-models --dry-run
```

本地尚未登录时，由你在自己的环境运行 `gh auth login --hostname github.com` 完成授权。遇到权限错误，应修复对应账户／应用的仓库授权；不应把凭据写入项目文件。

## 交给已授权的 Codex

在 Codex 可访问本文件包和目标仓库的环境中使用：

```text
读取本文件包的 AGENTS.md、PUBLISHING.md 和 docs/methodology.md。
目标仓库：leoncuhk/awesome-decision-models。
先运行 validate.py 与单元测试，再核对远端状态。
如果远端仍为空，将本文件包作为首版初始化到默认分支；不要 force push。
如果已有内容，保留原内容，在新分支中比较并提交 PR，不自动合并。
不要复制任何凭据、私有资料或运行缓存到公开仓库。
完成后报告真实 commit / PR 链接和实际 CI 状态；失败就报告失败，不能声称已发布。
```

## 发布后核验

检查首页的中英文互链、模型表、证据与来源链接。确认 Actions 的验证工作流成功。再手动运行 **Weekly source watch**，确认它成功建立 bot Issue 和基线。之后才将定期检查视为已启用。

本仓库的 Skill 是研究维护流程，**不是**自动研究服务；GitHub 定时任务只检测来源变化。两者的具体边界见 [维护说明](docs/maintenance.md)。

## English

In an authorized environment, run `scripts/publish.sh` to initialize an empty repository safely. It validates locally, refuses any existing remote refs, uses an ordinary non-force push and preserves the user's Git identity/configuration. For a nonempty repository, review changes on a branch and open a PR instead.

[GitHub CLI clone documentation](https://cli.github.com/manual/gh_repo_clone) · [GitHub Actions schedule behavior](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)
