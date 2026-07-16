# Codebase map

## Current repository state

Power & Proximity is in the foundation phase. The repository currently contains product doctrine and the repo-local AI harness; no application runtime, package manifest, source tree, test runner, or CI workflow has been selected.

## Authoritative zones

| Path | Purpose | Mutation rule |
|---|---|---|
| `README.md` | Public project entrypoint | Keep product-facing and concise |
| `AGENTS.md` | Repository-wide agent contract | Changes require harness validation |
| `docs/` | Product, schema, risks, and decisions | Preserve links and explicit status |
| `harness/` | Agent workflows, registries, context, reports | Harness lane owns structure |
| `scripts/` | Executable validators and helpers | Dependency-free until stack decision |
| `.githooks/` | Optional local Git hooks | Must call committed validators only |
| `.gitignore` | Generated-output policy | No unexplained ignore additions |

## Planned zones, not yet created

| Path | Planned purpose | Gate |
|---|---|---|
| `src/` | Universal simulation engine | Stack decision and validation floor |
| `data/` | Inspectable content packs and fixtures | Schema validator selected |
| `tests/` | Formula, graph, schema, and deterministic tests | Test runner selected |
| `.github/workflows/` | CI | Local commands proven first |
| `reports/generated/` | Generated local evidence | Ignored by default |

## Known traps

- Do not create separate human engines for individual packs.
- Do not map protected identity fields directly to behavioral scores.
- Do not replace story-based reputation with one global fame score.
- Do not add CI before local validation exists.
- Do not select a UI framework during a harness or schema-only sprint.
- Do not commit local run context, caches, logs, or generated reports by accident.

## First inspection targets

```text
AGENTS.md
harness/README.md
harness/manifest.json
harness/CODEBASE_MAP.md
harness/run-context.local.json or example
harness/workflows/
harness/artifacts.json
scripts/validate_harness.py
docs/GAPS_RISKS_TARGETS.md
```
