#!/usr/bin/env python3
"""Dependency-free validator for the repo-local AI harness."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REQUIRED_FILES = [
    "AGENTS.md",
    "README.md",
    "harness/README.md",
    "harness/manifest.json",
    "harness/CODEBASE_MAP.md",
    "harness/run-context.schema.json",
    "harness/run-context.example.json",
    "harness/artifacts.json",
    "harness/workflows/P03_REPO_INTAKE.md",
    "harness/workflows/P07_IMPLEMENTATION.md",
    "harness/workflows/P12_CLOSEOUT.md",
    "harness/skills/README.md",
    "harness/reports/OPERATOR_REPORT.md",
    "harness/reports/HANDOFF.md",
    "scripts/validate_harness.py",
    ".githooks/pre-commit",
]

WORKFLOW_HEADINGS = [
    "## Repo",
    "## Branch or worktree",
    "## Sprint",
    "## Lane",
    "## Owned scope",
    "## Forbidden scope",
    "## Expected artifacts",
    "## Validation order",
    "## Final handoff",
    "## Parallel safety",
]

CONTEXT_KEYS = [
    "repo",
    "branchOrWorktree",
    "sprint",
    "lane",
    "ownedScope",
    "forbiddenScope",
    "expectedArtifacts",
    "validationOrder",
    "evidenceReviewed",
    "nextDecision",
]


def load_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - validator must report malformed input
        errors.append(f"{path}: invalid JSON: {exc}")
        return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=None)
    parser.add_argument("--report", default=None)
    args = parser.parse_args()

    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parents[1]
    errors: list[str] = []
    checks: list[dict[str, object]] = []

    for relative_path in REQUIRED_FILES:
        if not (root / relative_path).is_file():
            errors.append(f"missing required file: {relative_path}")
    checks.append(
        {
            "name": "required-files",
            "ok": not any(error.startswith("missing required") for error in errors),
        }
    )

    manifest = load_json(root / "harness/manifest.json", errors)
    context = load_json(root / "harness/run-context.example.json", errors)
    registry = load_json(root / "harness/artifacts.json", errors)
    load_json(root / "harness/run-context.schema.json", errors)

    if isinstance(manifest, dict):
        references = []
        for key in [
            "entrypoint",
            "agentRules",
            "codebaseMap",
            "artifactRegistry",
            "validator",
            "hook",
        ]:
            references.append(manifest.get(key))
        references += list(manifest.get("workflows", []))
        references += list(manifest.get("skills", []))
        references += list(manifest.get("reports", []))
        run_context = manifest.get("runContext", {})
        references += [run_context.get("schema"), run_context.get("example")]

        for reference in references:
            if not isinstance(reference, str) or not reference:
                errors.append(f"manifest has invalid reference: {reference!r}")
            elif not (root / reference).is_file():
                errors.append(f"manifest reference does not exist: {reference}")
    checks.append(
        {
            "name": "manifest-references",
            "ok": not any("manifest" in error for error in errors),
        }
    )

    if isinstance(context, dict):
        for key in CONTEXT_KEYS:
            if key not in context:
                errors.append(f"run context missing required key: {key}")
        for key in [
            "ownedScope",
            "forbiddenScope",
            "expectedArtifacts",
            "validationOrder",
        ]:
            if key in context and (
                not isinstance(context[key], list) or not context[key]
            ):
                errors.append(f"run context {key} must be a non-empty list")
    checks.append(
        {
            "name": "run-context",
            "ok": not any("run context" in error for error in errors),
        }
    )

    for relative_path in [
        "harness/workflows/P03_REPO_INTAKE.md",
        "harness/workflows/P07_IMPLEMENTATION.md",
        "harness/workflows/P12_CLOSEOUT.md",
    ]:
        path = root / relative_path
        text = path.read_text(encoding="utf-8") if path.is_file() else ""
        for heading in WORKFLOW_HEADINGS:
            if heading not in text:
                errors.append(f"{relative_path}: missing heading {heading}")
    checks.append(
        {
            "name": "workflow-contracts",
            "ok": not any("missing heading" in error for error in errors),
        }
    )

    if isinstance(registry, dict):
        artifact_ids: set[str] = set()
        for item in registry.get("artifacts", []):
            artifact_id = item.get("id")
            path = item.get("path")
            policy = item.get("commitPolicy")
            if not artifact_id or artifact_id in artifact_ids:
                errors.append(f"artifact id missing or duplicated: {artifact_id!r}")
            artifact_ids.add(artifact_id)
            if not path or not policy:
                errors.append(
                    f"artifact {artifact_id!r} missing path or commitPolicy"
                )
            if policy == "committed" and path and not (root / path).is_file():
                errors.append(f"committed artifact missing: {path}")
    checks.append(
        {
            "name": "artifact-registry",
            "ok": not any("artifact" in error for error in errors),
        }
    )

    result = {
        "ok": not errors,
        "root": str(root),
        "checks": checks,
        "errors": errors,
    }
    rendered = json.dumps(result, indent=2)
    print(rendered)

    if args.report:
        output = root / args.report
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered + "\n", encoding="utf-8")

    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
