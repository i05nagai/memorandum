---
title: Software Engineering Law and Principle
---

## Software Engineering Law and Princple


## Conway's Law
https://en.wikipedia.org/wiki/Conway%27s_law

Any organization that designs a system (defined broadly) will produce a design whose structure is a copy of the organization's communication structure.


## Brook's Law

## Choose Boring Technology
Consider how you would solve your immediate problem without adding anything new.


## Conway's Law
Any organization that designs a system (defined broadly) will produce a design whose structure is a copy of the organization's communication structure.


## Goodheart's Law
When a measure becomes a target, it ceases to be a good measure.

## Hyrum's Law
https://www.hyrumslaw.com/

With a sufficient number of users of an API, it does not matter what you promise in the contract:
all observable behaviors of your system will be depended on by somebody.

### Dealwing with Hyrum's lawo
Hyrum’s Law says that every observable behaviour of your API—even those you never documented—has at least one consumer depending on it. Any silent assumption you change can break somebody in production. The refactor therefore has to:

- (1) Discover what behaviour is actually in use.
- (2) Decide which parts you’ll keep, change, or drop.
- (3) Deliver the new implementation without surprises.

Below is a playbook that teams at Google and elsewhere have used to pull this off.

#### 1 Instrument and measure first
Add detailed request/response logging or tap traffic to a mirror (“shadow traffic”).
Record everything you suspect is accidental: field order, default values, error text, timing quirks, etc.
Use the data to rank behaviours by how many (and which) clients rely on them. Google backs every large change with similar A/B diff tests to expose accidental breakage before it reaches prod.

#### 2 Freeze reality into tests
Write a compatibility test-suite that codifies the behaviours you intend to preserve. This becomes the guard-rail for the refactor and a regression net for future work. Abseil, for example, promises API compatibility even while the binary interface is free to change, because its contract tests catch any observable drift.

#### 3 Classify each behaviour

| Category                    | Example                                   | Strategy                             |
| --------------------------- | ----------------------------------------- | ------------------------------------ |
| **Contracted**              | Documented field names, HTTP status codes | Keep & document                      |
| **Incidental but harmless** | Extra JSON keys clients ignore            | Keep for now, schedule later cleanup |
| **Incidental & harmful**    | Leaking internal error stack traces       | Deprecate aggressively               |


#### 4 Design an “escape hatch”
Versioned surface – Ship a /v2 endpoint, new gRPC service, or new SDK namespace. Versioning is the safest way to move fast without pulling the rug from current consumers.
Opt-in flags / Accept headers – Let clients flip a switch to try the stricter behaviour, giving you real-world feedback before you force anyone over.
Compatibility shim – Route old requests through a thin adapter that invokes the new implementation, so there is only one true code path to maintain.

#### 5 Communicate and deprecate deliberately
Advisory deprecation – Start with warnings in logs, docs and release notes; give concrete migration steps.
Compulsory deprecation – After the agreed window (often 6–12 months), failing calls start to error.
Removal – Delete the shim only when telemetry shows near-zero usage. Google formalises this staged approach as part of its deprecation framework.

#### 6 Roll out safely
Canaries & shadow reads – Replay production traffic against the new code and diff responses.
Progressive rollout – Ramp from 1 % to 100 % traffic, watching error budgets and business metrics.
Automatic rollback – Treat the rollout like any other risky release.

#### 7 Delete the legacy path
When the usage curve hits zero (or your contractual sunset date passes), disable the feature flag, remove the adapter, and clean up tests covering deprecated behaviour.

#### 8 Prevent future contamination
Keep the compatibility test-suite and run it in CI for every change.
Require API review for anything user-visible.
Add linters/static analysis to block inadvertent new behaviours (e.g., accidental new JSON fields).

Practical checklist
- [ ] Log full request/response samples in production.
- [ ] Analyse which quirks real clients rely on.
- [ ] Write golden tests that nail down behaviour you will preserve.
- [ ] Build the new API (v2) plus an adapter layer v1 → v2.
- [ ] Release v2 behind an opt-in header; iterate until it passes diff testing on mirrored traffic.
- [ ] Announce a deprecation timeline and publish a migration guide.
- [ ] Ramp remaining clients over; monitor.
- [ ] Remove the adapter and old tests.


## Knuth's optimization principle
Premature optimization is the root of all evil.

## Law of Leaky Abstractions
All non-trivial abstractions, to some degree, are leaky.

## Linus's Law
Given enough eyeballs, all bugs are shallow.


## SOLID
https://en.wikipedia.org/wiki/SOLID


## Reference
- https://www.laws-of-software.com/
