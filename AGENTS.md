# Agent Operating Contract

This repository uses harness discipline for software, documentation, automation, deployment, GitHub, and agent work.

## Harness entrypoint

Prompts are one input artifact inside the harness; they are not the harness itself.

A fresh agent must enter in this order:

1. read this file;
2. read `harness/README.md`;
3. inspect `harness/CODEBASE_MAP.md`;
4. populate or review the active run context using `harness/run-context.example.json`;
5. choose the narrowest matching workflow in `harness/workflows/`;
6. load only the scoped skills required for that workflow;
7. review `harness/artifacts.json` before generating outputs;
8. run `python3 scripts/validate_harness.py` before final handoff.

Machine-readable harness references live in `harness/manifest.json`. Local run state belongs in the ignored `harness/run-context.local.json`; generated reports belong under the ignored `reports/generated/` unless explicitly promoted and registered as committed evidence.

## Required operating context

Every sprint or handoff must name:

- repository;
- branch or isolated worktree;
- issue, PR, or sprint;
- lane;
- owned scope;
- forbidden scope;
- expected artifacts;
- validation order when one is specified.

## Operational loop

```text
request
-> evidence review
-> bounded decision
-> repository / Git / GitHub mutation
-> artifacts
-> validation
-> report
-> next decision
```

Evidence comes before confidence. Do not claim completion from intention, filenames, or prose alone.

## Completion evidence

Use the strongest available proof:

- passing tests, linters, typechecks, builds, or schema validators;
- generated reports, fixtures, logs, or runtime artifacts;
- commit SHA;
- branch or worktree state;
- push confirmation;
- PR creation or mutation;
- merge, tag, release, deployment, or runtime evidence when in scope.

Do not claim a higher proof level from a lower one.

## Repository intake

For an unknown or newly created repository, inspect before inventing:

1. repository metadata and default branch;
2. current files and recent commits;
3. open issues and pull requests;
4. existing names, contracts, helpers, validators, and output patterns;
5. branch protections and CI when available.

For a local checkout, begin with:

```bash
git status --short
git branch --show-current
git log --oneline --decorate -5
```

Preserve useful work before destructive cleanup. If the worktree is dirty and the lane does not own those changes, use an isolated worktree or stop with the exact blocker.

## Scope control

- Keep changes bounded to owned scope.
- Avoid unrelated rewrites.
- Search existing contracts before inventing replacements.
- Keep engine logic separate from domain content.
- Do not silently stage or commit unrelated files.
- Do not leave generated files, logs, caches, or undocumented ignore candidates behind.

## Branch and PR policy

- Use one bounded branch per sprint.
- Default foundation branch: `feature/power-proximity-foundation`.
- Prefer draft PRs until validation is complete.
- PR bodies must state mission, lane, owned scope, forbidden scope, artifacts, validation, gaps, and next decision.
- Keep docs, schemas, engine changes, content packs, harness changes, and runtime proofs separable when practical.

## Validation order

Unless a sprint defines a stricter order:

1. structural validation: required files and schema shape;
2. static validation: formatting, lint, typecheck;
3. unit validation: deterministic formulas and graph behavior;
4. build validation;
5. runtime proof with generated artifacts;
6. harness validation;
7. Git and GitHub state verification.

Record exact skips. “Not applicable” is different from “not run.”

## Product safety contracts

- Identity is not a shortcut for behavior, morality, intelligence, competence, aggression, trustworthiness, or criminality.
- Packs may alias and weight universal traits, but should not fork the human engine without evidence.
- Reputation transfers through stories and audience interpretation, not one universal fame score.
- Randomness must be seedable where deterministic proof is required.
- Narrative output must explain causal changes rather than obscure them.

## Sequential prompt suite

Use the established sequence when applicable:

- **P03**: unknown repository intake and first safe action;
- **P06**: repository or PR cleanup;
- **P07**: general bounded implementation;
- **P14**: broken PR repair;
- **P15**: merge or release;
- **P20**: execute a selected Opportunity Discovery row;
- **P12**: closeout.

Task-specific rules override generic closeout behavior. Repo-local workflow specifications for P03, P07, and P12 live under `harness/workflows/`; add further workflows only when they have a distinct operational contract.

## Required final handoff

Every repo sprint report should include:

- repo;
- branch/worktree;
- issue/PR/sprint;
- lane;
- files changed;
- artifacts generated;
- validation commands and results;
- commit SHA and push/PR evidence;
- known gaps and risks;
- untracked, modified, or ignored candidates;
- next bounded decision.

Use `harness/reports/OPERATOR_REPORT.md` for full evidence and `harness/reports/HANDOFF.md` for compressed transfer.

Do not substitute a rewritten prompt, plan, or handoff for requested repository work.
