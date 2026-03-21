# GitHub Cheat Sheet

## Branch

```bash
git checkout -b feat/short-description   # create + switch
git checkout main                        # switch to main
git branch -d feat/short-description    # delete local branch after merge
```

**Naming:** `feat/`, `fix/`, `docs/`, `chore/` + short description. No spaces — use hyphens.

---

## Commit

```bash
git add path/to/file.md                 # stage specific files (preferred)
git add -A                              # stage everything (use carefully)
git commit -m "$(cat <<'EOF'
type(scope): short subject (50 chars max)

Longer explanation of why, not what. Wrap at 72 chars.
Reference issues: Closes #42

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

**Types:** `feat` · `fix` · `docs` · `chore` · `refactor` · `test`
**Subject:** imperative mood — "add X", not "added X" or "adds X"

---

## Push

```bash
git push                                # push current branch
git push -u origin feat/my-branch      # first push of a new branch
```

---

## Pull Request

1. Push branch to GitHub
2. `gh pr create --title "Short title" --body "..."`  (or open in browser)
3. Review diff: `gh pr diff 123` or `git diff main...HEAD`
4. Merge: `gh pr merge 123 --squash` (or locally — see below)

**Issue linking in PR body:** `Closes #42` auto-closes the issue on merge.

---

## Merge (local — when GitHub token can't merge)

```bash
git checkout main
git merge --squash feat/my-branch      # squash all commits into one
git commit -m "feat: describe what merged"
git push
git branch -d feat/my-branch           # clean up
```

---

## Tags & Releases

```bash
git tag v1.2.0                         # lightweight tag
git tag -a v1.2.0 -m "Release notes"  # annotated tag (preferred)
git push origin v1.2.0                 # push tag
gh release create v1.2.0 --title "v1.2.0" --notes "What changed"
```

---

## Quick Reference

| Command | What it does |
|---------|-------------|
| `git status` | See what's changed |
| `git log --oneline -10` | Last 10 commits |
| `git diff` | Unstaged changes |
| `git diff --staged` | Staged changes |
| `git stash` | Shelve uncommitted work |
| `git stash pop` | Restore shelved work |
| `gh pr list` | Open PRs |
| `gh issue list` | Open issues |
