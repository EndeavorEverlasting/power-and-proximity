# P12 — Closeout and handoff compression

## Repo
Confirm exact repository remote.

## Branch or worktree
Confirm branch/worktree and clean status.

## Sprint
Name the issue/PR being closed or handed off.

## Lane
Closeout and evidence reporting.

## Owned scope
- Run validators in declared order.
- Collect artifacts, commit SHA, branch state, push/PR evidence, and exact skips.
- Update issue/PR/report state where in scope.

## Forbidden scope
- New feature work during closeout.
- Claiming higher proof than achieved.
- Hiding failures, skipped checks, or lingering files.

## Expected artifacts
- Completed operator report.
- Compressed handoff.
- Registered validation/runtime artifacts when applicable.

## Validation order
1. Project-specific checks.
2. Harness validator.
3. Artifact registry review.
4. Working-tree and ignored-candidate review.
5. GitHub branch/PR status.

## Final handoff
State repo, branch/worktree, sprint, lane, changes, artifacts, validation, proof, gaps, lingering files, and next decision.

## Parallel safety
Closeout must not mutate files owned by an active parallel lane without coordination.
