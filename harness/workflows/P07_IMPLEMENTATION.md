# P07 — General bounded implementation

## Repo
Use the repo named in run context.

## Branch or worktree
Use one bounded branch or isolated worktree. Preserve unrelated changes.

## Sprint
Name the issue, PR, or bounded feature.

## Lane
Implementation, schema, content, harness, docs, or validation; choose one primary lane.

## Owned scope
- Edit only named files and contracts.
- Reuse existing helpers and output patterns.
- Generate registered artifacts.

## Forbidden scope
- Unrelated rewrites.
- Silent schema drift.
- New dependencies without an explicit decision artifact.
- Unregistered generated outputs.

## Expected artifacts
List source, data, docs, reports, and runtime evidence paths before editing.

## Validation order
1. Structural/schema validation.
2. Format/lint/typecheck.
3. Unit tests.
4. Build.
5. Runtime proof and generated artifacts.
6. Harness validation.
7. Git/GitHub verification.

## Final handoff
Use the operator report, then compress into the handoff template with commit/PR evidence.

## Parallel safety
Name overlapping files, dependency gates, and whether the lane can merge independently.
