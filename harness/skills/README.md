# Scoped repo skills

Skills are small repo-local operating contracts, not broad prompts. Use only those required by the selected workflow.

## `repo-evidence`

**Use when:** entering a repo, resolving current state, or validating a handoff.

**Inputs:** Git state, repo map, manifests, issue/PR metadata, generated-output policy.

**Outputs:** evidence list, confidence boundary, exact blockers, next safe decision.

**Must not:** mutate source before scope is resolved; infer runtime health from documentation alone.

## `product-safety`

**Use when:** changing actor, trait, identity, pack, reputation, narrative, or institutional schemas.

**Checks:**
- identity is not used as a shortcut for behavior or capability;
- packs alias universal traits instead of forking the human engine;
- reputation remains story- and audience-based;
- narrative output preserves causal explanation;
- randomness is seedable where proof requires determinism.

## `harness-maintenance`

**Use when:** adding workflows, validators, reports, hooks, or registries.

**Checks:**
- every new harness file is referenced from `harness/manifest.json` or the artifact registry;
- generated outputs have a documented commit policy;
- local hooks call committed scripts;
- validator failures are actionable English messages;
- no vendor-specific agent dependency becomes mandatory.
