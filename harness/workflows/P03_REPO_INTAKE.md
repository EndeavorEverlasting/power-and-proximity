# P03 — Unknown repository intake and first safe action

## Repo
Resolve from remote metadata or local Git evidence.

## Branch or worktree
Inspect the current branch. Use an isolated branch/worktree for bounded mutation.

## Sprint
Repository intake and first safe action.

## Lane
Evidence and harness orientation.

## Owned scope
- Inspect rules, maps, manifests, validators, scripts, generated-output policy, branches, PRs, and CI.
- Populate run context.
- Choose one safe first mutation or stop with an exact blocker.

## Forbidden scope
- Broad implementation before contracts are known.
- Destructive cleanup without preserving useful work.
- Confidence based on filenames alone.

## Expected artifacts
- Updated run context.
- Evidence notes in the operator report.
- One bounded mutation or exact blocker.

## Validation order
1. Repository and Git state.
2. Harness validator.
3. Existing project checks in documented order.
4. Git/GitHub state proof.

## Final handoff
Use `harness/reports/HANDOFF.md`; state proof level and next decision.

## Parallel safety
Do not overlap another lane's files. Intake is read-only until scope is resolved.
