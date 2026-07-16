# Power & Proximity

**Power & Proximity** is a text-driven social consequence strategy game about how choices travel through relationships, institutions, reputations, and interconnected lives.

> Power is not only what you have. Power is who you can reach.

## Project status

**Foundation design phase.** The repository is establishing product doctrine, portable schemas, validation contracts, and the first bounded vertical slice before committing to a full application stack.

## The experience

Players inhabit a social world where every actor has persistent dispositions, capabilities, relationships, memories, pressures, known stories, and varying proximity to formal or informal power.

A choice does not end when an interaction closes. Its effects can:

- change trust, resentment, gratitude, fear, or loyalty;
- alter relationships between actors who were not directly involved;
- create memories and gradual character drift;
- become a public story that follows someone into another industry;
- build legitimate capacity or trade it for immediate shortcut gain;
- unlock or close access through six-degree-style paths.

The player may occupy a low-power role, such as a dishwasher, junior employee, constituent, activist, caregiver, or remote worker. Influence must often be exercised through relationships rather than direct authority.

## Core design laws

### Consequence travels through relationships

The social graph is not merely a map of who knows whom. It is a map of how information, trust, resentment, opportunity, and influence travel.

### Shortcuts create hidden debt

A shortcut should produce visible immediate gain and hidden future debt.

A legitimate practice should produce visible immediate cost and hidden future capacity.

### Characters are shaped by pressured choices

Characters use continuous dispositions and capabilities rather than fixed moral classes.

```text
Situation -> Choice -> Outcome -> Memory -> Trait Drift -> Habit -> Reputation -> Future Bias
```

A character is not a stat block. A character is the accumulated residue of pressured choices.

### Identity is context, not destiny

Identity, personality, capability, pressure, and reputation are separate parts of the actor model.

Race, gender, sexuality, culture, class, religion, disability, and related identity fields may affect belonging, visibility, vulnerability, representation, and institutional treatment. They must not directly determine intelligence, morality, competence, aggression, trustworthiness, or criminality.

### Stories travel across domains

Reputation is not one global score. Actors carry known stories into new communities:

> "Oh, you're the person who did that."

Each audience may interpret the same story differently. An actor may be celebrated by workers, distrusted by owners, useful to journalists, and treated cautiously by politicians.

## Universal human substrate

Every domain pack uses the same underlying actor and consequence systems. Packs may rename and contextualize shared traits without replacing the engine.

| Universal concept | Politics | Restaurant | Gym | Research | Technology |
|---|---|---|---|---|---|
| Gravitas | Statesmanship | Floor authority | Coach presence | Scholarly authority | Architectural authority |
| Discipline | Campaign endurance | Shift reliability | Training consistency | Methodological rigor | Delivery reliability |
| Cunning | Backroom strategy | Schedule politics | Social maneuvering | Grant politics | Roadmap politics |
| Social grace | Coalition diplomacy | Staff warmth | Group rapport | Collegiality | Team influence |

The governing contract is:

> Traits persist. Stories transfer. Capital converts. Packs reinterpret.

## Planned systems

- actor, identity, capability, and pressure models;
- continuous trait values and derived attributes such as gravitas;
- weighted archetype spectra;
- organizations, industries, and portable domain packs;
- relationship graphs and six-degree pathfinding;
- influence, referrals, vouching, recognition, and ripple propagation;
- memories, self-concept, habits, and character formation;
- story-based fame, infamy, controversy, and audience interpretation;
- merit, network power, nepotism, and opportunity theft;
- institutional trust, legitimacy, truth quality, shortcut gain, and debt;
- deterministic seeded simulation;
- inspectable narrative consequences produced from templates and evidence.

## First vertical slice: Blue Corner Diner

The first bounded domain is a restaurant and commercial corridor. It is small enough to test coherently while supporting labor, ownership, class, health and safety, scheduling, nepotism, landlord pressure, journalism, local politics, and indirect access to power.

An initial dilemma may begin with a dishwasher discovering an unresolved health concern. The available choices should not collapse into only "report" or "remain silent." The actor may warn a coworker, speak privately, document the issue, seek an intermediary, encourage a quiet repair, contact an inspector, expose the problem, or decide the personal risk is too high.

Each route should have a clear cost, a legible outcome, and a ripple through the social graph.

## Foundation direction

The initial implementation is expected to favor:

- TypeScript or another strongly validated web-friendly runtime after an explicit stack decision;
- JSON or similarly inspectable content packs;
- deterministic seeded simulation;
- schema validation and unit tests;
- engine logic separated from domain content;
- a CLI or small browser-visible runtime proof before polished presentation;
- clean Git branches, bounded PRs, and evidence-based closeout.

## Initial non-goals

The foundation sprint will not attempt to build:

- a full city simulation;
- multiplayer, authentication, or a production database;
- a polished 3D social graph;
- city-scale procedural generation;
- runtime LLM-generated narrative;
- monetization or premium auto-mode;
- complete politics, gym, police, research, or technology packs.

## Repo-local AI harness

The repository treats prompts as one artifact inside a larger operating system. A fresh agent should begin with:

1. [AGENTS.md](AGENTS.md)
2. [harness/README.md](harness/README.md)
3. [harness/CODEBASE_MAP.md](harness/CODEBASE_MAP.md)
4. the matching workflow under `harness/workflows/`
5. `python3 scripts/validate_harness.py`

The harness includes run context, workflow contracts, artifact registration, scoped skills, read-only evidence commands, an optional local hook, English operator reporting, and compressed handoff templates.

## Repository discipline

Repository work follows the operational loop:

```text
request -> evidence review -> bounded decision -> mutation -> artifacts -> validation -> report -> next decision
```

See [AGENTS.md](AGENTS.md) for the working contract and [docs/GAPS_RISKS_TARGETS.md](docs/GAPS_RISKS_TARGETS.md) for the current evidence ledger.

## License

Licensed under the [MIT License](LICENSE).
