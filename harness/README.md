# Repo-local AI harness

This directory is the operational entrypoint for agents and maintainers. Prompts are inputs to workflows; they are not the harness itself.

## Fresh-agent entry order

1. Read `AGENTS.md` for repository-wide rules.
2. Read `harness/CODEBASE_MAP.md` for current repository truth.
3. Copy `harness/run-context.example.json` to the ignored `harness/run-context.local.json` and fill the active sprint context.
4. Choose the narrowest matching workflow under `harness/workflows/`.
5. Read only the scoped skills required for that workflow.
6. Use read-only evidence commands before mutation.
7. Run `python3 scripts/validate_harness.py` before handoff.
8. Produce the operator report and compressed handoff artifacts registered in `harness/artifacts.json`.

## Harness components

| Component | Contract |
|---|---|
| Agent rules | `AGENTS.md` |
| Codebase map | `harness/CODEBASE_MAP.md` |
| Harness manifest | `harness/manifest.json` |
| Workflow specs | `harness/workflows/` |
| Run context | `harness/run-context.schema.json` and local/example JSON |
| Artifact registry | `harness/artifacts.json` |
| Validator | `scripts/validate_harness.py` |
| Optional local hook | `.githooks/pre-commit` |
| Scoped skills | `harness/skills/README.md` |
| Operator reports | `harness/reports/` |

## Read-only code intelligence

Use these before inventing or editing:

```bash
git status --short
git branch --show-current
git log --oneline --decorate -12
git ls-files
git grep -n "term"
find . -maxdepth 3 -type f | sort
```

When source code exists, add language-specific symbol/index commands only if they are read-only, reproducible, and documented in `harness/manifest.json`.

## Local hooks

Hooks are opt-in:

```bash
git config core.hooksPath .githooks
```

The pre-commit hook runs the harness validator. CI must not be added until the same validator is proven locally.

## Generated-output policy

- Local run context: `harness/run-context.local.json` (ignored).
- Generated validation and runtime reports: `reports/generated/` (ignored unless a sprint explicitly promotes a file to committed evidence).
- Templates and registries are committed.
- Every committed evidence artifact must be listed in `harness/artifacts.json` or added there in the same change.
