#!/usr/bin/env bash
# Initialize ONLY an empty GitHub repository. No force push and no global config edits.
set -euo pipefail
repo="${1:-leoncuhk/awesome-decision-models}"
mode="${2:-}"
case "$repo" in
  *[!A-Za-z0-9_./-]*|/*|*/|*/*/*|*..*) echo "Invalid owner/repository identifier." >&2; exit 2 ;;
esac
case "$repo" in */*) ;; *) echo "Use owner/repository." >&2; exit 2 ;; esac
if [ -n "$mode" ] && [ "$mode" != "--yes" ] && [ "$mode" != "--dry-run" ]; then
  echo "Usage: bash scripts/publish.sh [owner/repository] [--yes|--dry-run]" >&2; exit 2
fi
for tool in git gh python3; do
  command -v "$tool" >/dev/null 2>&1 || { echo "Required: $tool. Install it in your own environment before publishing." >&2; exit 2; }
done
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$root/scripts/validate.py"
python3 -m unittest discover -s "$root/tests" -v
gh auth status --hostname github.com
permission="$(gh api "repos/$repo" --jq '.permissions.push')"
[ "$permission" = "true" ] || { echo "Authenticated account does not report push permission." >&2; exit 3; }
branch="$(gh api "repos/$repo" --jq '.default_branch')"
[ -n "$branch" ] && [ "$branch" != "null" ] || branch=main
git check-ref-format "refs/heads/$branch" >/dev/null
work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT
gh repo clone "$repo" "$work/repository"
cd "$work/repository"
refs="$(git ls-remote --refs origin)"
if [ -n "$refs" ]; then
  echo "REFUSED: repository is not empty. Use a reviewed branch/PR; this initializer never overwrites existing work." >&2
  exit 4
fi
# The user controls their identity. Do not infer or silently set a public email.
git var GIT_AUTHOR_IDENT >/dev/null
git var GIT_COMMITTER_IDENT >/dev/null
python3 - "$root" "$work/repository" <<'PY'
import shutil,sys
from pathlib import Path
src,dst=map(Path,sys.argv[1:])
def ignored(folder,names):
    return {n for n in names if n in {'.git','__pycache__','.venv','reports','.source-watch-state.json'} or n=='.env' or n.startswith('.env.') or n.endswith(('.pyc','.pyo'))}
shutil.copytree(src,dst,dirs_exist_ok=True,ignore=ignored)
PY
git symbolic-ref HEAD "refs/heads/$branch"
git add --all
git diff --cached --stat
if [ "$mode" = "--dry-run" ]; then
  echo "Dry run complete: validated and staged in a disposable clone. Nothing committed or pushed."
  exit 0
fi
if [ "$mode" != "--yes" ]; then
  printf 'Create the initial commit on %s:%s? [y/N] ' "$repo" "$branch"
  read -r answer
  case "$answer" in y|Y|yes|YES) ;; *) echo "Cancelled; no remote changes."; exit 0 ;; esac
fi
git commit -m "docs: publish evidence-backed decision-model catalog"
# Ordinary non-force push protects concurrent initialization by another writer.
git push origin "HEAD:refs/heads/$branch"
echo "Published to https://github.com/$repo on $branch. Check Actions for actual workflow results."
