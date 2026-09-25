# Validation record · 2026-09-25

## Completed locally

- Python 3.13.5: all repository Python files parsed.
- `python3 scripts/validate.py`: passed schema, source references, bilingual fields, numerical consistency, generated-file synchronization and local Markdown link/anchor checks.
- `python3 -m unittest discover -s tests -v`: **34 tests passed**.
- `python3 tests/integration_publish.py`: **3 local integration cases passed**: dry run leaves the remote empty; initialization publishes the intended files to a disposable local bare repository; a second attempt refuses to overwrite existing commits.
- `bash -n scripts/publish.sh`: passed.
- Workflow/Dependabot YAML parsed locally; workflow trigger/job keys checked.

The integration test replaces `gh` with a fixture and uses local temporary Git remotes. It performs **no GitHub writes** and does not establish live authorization.

## Not claimed

No model inference, benchmark reproduction, paid API calls, full external-link crawl, model-weight hash verification or live GitHub Actions run was performed. Source review and offline repository tests are different activities. Individual review depths are recorded in [the source register](docs/sources.md).

The watcher uses mocked network responses in unit tests. A first real run is still required to establish reachable endpoints, repository issue permissions and the update baseline.

## Re-run

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 tests/integration_publish.py
bash -n scripts/publish.sh
```

中文：本文件记录已实际完成的本地检查。34 项单元测试和 3 个本地发布模拟用例通过，不代表已经推送 GitHub，也不代表复现了任何模型成绩。
