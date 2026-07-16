# Gaps, Risks, and Targets

This ledger records the current limits of confidence. It should be updated by every sprint that changes the architecture, runtime, data contracts, validation, or product boundary.

## Current evidence

As of the foundation doctrine sprint:

- the repository exists and `main` contains an MIT license and Node-oriented `.gitignore`;
- the product title is **Power & Proximity**;
- the first vertical slice is **Blue Corner Diner**;
- the universal-substrate and pack-alias architecture is decided conceptually;
- the v0 entities and major invariants are documented;
- no application framework, package manager, source tree, test harness, or CI workflow has been selected;
- no runtime or balancing proof exists yet.

## Known gaps

### Runtime stack selection

Unknowns:

- TypeScript runtime and package manager;
- browser-first versus CLI-first proof;
- framework, if any;
- schema-validation library;
- test runner;
- graph library versus in-house bounded graph functions.

Target decision artifact:

- `docs/STACK_DECISION.md`

Decision rule:

Choose the smallest stack that can run deterministically in a Replit-like environment, validate JSON content, test graph behavior, and expose a small inspectable proof.

### MVP trait inventory

The design space contains more traits than the first implementation should expose.

Risks:

- duplicated or highly correlated traits;
- opaque actor behavior;
- tuning burden;
- domain aliases masking schema drift.

Target artifacts:

- `docs/TRAIT_MODEL.md`
- `data/traits.json`
- `data/capabilities.json`
- `data/derived-traits.json`

Required validation:

- every base trait has a behavioral definition;
- every derived trait lists dependencies;
- every pack alias resolves to a universal concept;
- protected identity fields are excluded from behavioral weighting.

### Formula normalization and balance

Current formulas are conceptual. Their scales are not yet safe to combine.

Unknowns:

- normalization range;
- weighting conventions;
- clamping behavior;
- temporal decay;
- path-influence underflow;
- critical-mass thresholds;
- deterministic tie-breaking.

Risk:

A mathematically elaborate system may produce uninteresting or illegible play.

Target artifacts:

- `docs/MATH_MODEL.md`
- deterministic fixtures;
- formula unit tests;
- one calibration report using Blue Corner actors.

### Interaction feel before formula tuning

The desired interaction experience must be designed before balancing equations.

Required scenario qualities:

- the player may lack formal authority;
- more than two meaningful options exist when appropriate;
- each option has a clear immediate cost or benefit;
- graph ripples are relevant rather than universal;
- actor reactions can be explained from state;
- relationships can be repaired or worsened over time.

Target artifact:

- `docs/SCENARIO_DESIGN.md`

### Relationship ripple policy

Unknowns:

- propagation depth per event;
- visibility and communication gates;
- event-priority rules;
- how many consequences the player sees immediately;
- when dormant cross-domain relationships generate new events.

Risks:

- event storms;
- arbitrary-feeling reactions;
- hidden causality;
- permanent cascade loops.

Target artifacts:

- `docs/SOCIAL_GRAPH.md`
- `docs/NETWORK_INTELLIGENCE.md`
- graph fixtures and deterministic path tests.

### Memory and story lifecycle

Unknowns:

- memory decay versus hardening;
- repeated-event aggregation;
- contradictory memories;
- rumor, propaganda, correction, and contested stories;
- story recency and domain relevance decay.

Target artifacts:

- `docs/MEMORY_MODEL.md`
- `docs/REPUTATION_STORIES.md`
- recognition fixtures.

### Cross-pack capital conversion

Candidate capital forms exist, but conversion rules do not.

Unknowns:

- what transfers directly;
- what requires a story or relationship bridge;
- whether `Capital` is the final player-facing parent term;
- how access, favors, credibility, legitimacy, heat, and notoriety decay.

Target artifact:

- `docs/CURRENCIES_AND_CAPITAL.md`

### Identity and privacy validation

The doctrine is decided, but enforcement does not exist.

Risks:

- identity fields accidentally used as behavioral shortcuts;
- private fields exposed to actors or players without a visibility path;
- pack data embedding stereotypes;
- institutional bias modeled as an intrinsic property of the targeted actor.

Target artifacts:

- `docs/IDENTITY_CONTEXT_MODEL.md`
- schema-level visibility metadata;
- validators that prevent forbidden direct weight mappings.

### Narrative legibility

Unknowns:

- template grammar;
- explanation depth;
- repetition controls;
- distinction between private memory, public story, and player-facing narration.

Risk:

Numbers may be correct while characters still feel like spreadsheets.

Target artifacts:

- `docs/NARRATIVE_MODEL.md`
- narrative templates;
- snapshot tests.

### Auto-mode

Auto-mode is a future feature where shaped actors or networks continue according to accumulated dispositions, capabilities, stories, relationships, pressures, and capital.

Risks:

- loss of player agency;
- pay-to-skip incentives;
- random-feeling automation;
- invisible harmful choices;
- premature monetization distorting the base game.

Forbidden in the foundation implementation sprint.

Target artifact:

- `docs/AUTO_MODE.md` in a later design-only lane.

### Three-dimensional graph presentation

A cohesive 3D social graph remains a product ambition, not a foundation requirement.

Unknowns:

- whether 3D improves comprehension;
- accessibility and performance;
- useful dimensions and filters;
- how to avoid visual clutter.

Required gate:

Prove graph queries and causal usefulness in text or 2D before implementing 3D.

## Risks by severity

| Risk | Severity | Mitigation |
|---|---:|---|
| Building separate engines for each pack | High | Universal schema and alias validation |
| Overengineering math before interaction feel | High | Scenario-first calibration |
| Graph becomes decorative | High | Require path, access, recognition, or ripple effects |
| Scope expands into a full city | High | Blue Corner vertical-slice boundary |
| Identity becomes behavioral stereotype | High | Separate schema and forbidden mapping validation |
| Too many traits obscure behavior | High | MVP trait audit and correlation review |
| Event storms overwhelm the player | Medium | Visibility, relevance, depth, and priority gates |
| Story system becomes a global score in disguise | Medium | Audience-specific valence and source stories |
| Randomness hides causality | Medium | Seeded randomness and explanation output |
| Narrative templates repeat | Medium | Tags, variants, cooldowns, and snapshot review |
| Framework decision creates avoidable debt | Medium | Explicit stack-decision sprint |
| Generated artifacts or caches pollute PRs | Medium | `.gitignore`, status checks, explicit artifact policy |

## First targets to inspect in the next implementation sprint

```text
README.md
AGENTS.md
docs/VISION.md
docs/SCHEMA_OVERVIEW.md
docs/GAPS_RISKS_TARGETS.md
.gitignore
LICENSE
```

Then determine whether the repo contains or needs:

```text
package.json
tsconfig.json
src/
data/
tests/
scripts/
.github/workflows/
```

## Recommended next sprint order

### Sprint A: stack and validation floor

Lane: harness and technical decision.

Owned scope:

- select minimal runtime, package manager, schema validator, and test runner;
- create deterministic hello-simulation fixture;
- add format, typecheck, test, and build commands;
- add CI only after local commands are proven.

Forbidden scope:

- full game mechanics;
- UI framework beyond what the proof requires;
- additional packs.

### Sprint B: universal actor schema

Lane: schema and validation.

Owned scope:

- actor, identity, traits, capabilities, derived traits, pressure, visibility;
- gravitas proof;
- pack alias validation.

### Sprint C: graph and story schema

Lane: engine contracts.

Owned scope:

- relationship edges;
- path queries;
- memories;
- stories, audience valence, and recognition.

### Sprint D: Blue Corner fixtures

Lane: content pack.

Owned scope:

- bounded cast;
- organizations;
- relationships;
- actions and scenario fixtures;
- no diner-specific branching inside universal engine code.

### Sprint E: deterministic runtime proof

Lane: runtime and validation.

Owned scope:

- one small interaction chain;
- same seed, same output;
- direct effect, ripple, memory, story, and narrative artifact;
- evidence report.

## Foundation forbidden scope

Until the validation floor and v0 schema are proven, do not build:

- a full city simulation;
- a polished 3D graph;
- database, authentication, multiplayer, or production deployment;
- runtime LLM narrative generation;
- premium economy or monetization;
- full politics, gym, public safety, research, or tech packs;
- city-scale procedural actor generation;
- integrations with The Blacksmith Guild.

## Required closeout questions

Every future sprint should answer:

1. What evidence was reviewed?
2. What bounded decision was made?
3. What repository or GitHub state changed?
4. What artifacts were produced?
5. What validation ran, in what order?
6. What proof level was achieved?
7. What remains unknown or forbidden?
8. What is the next bounded decision?
