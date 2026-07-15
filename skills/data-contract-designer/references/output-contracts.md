# Output Contracts

## Contract Design

Return sections in this order:

1. **Decision summary:** boundary, selected type, status, and unresolved blockers.
2. **Parties and purpose:** accountable parties, intended outcome, valid use, prohibited use, and non-goals.
3. **Binding:** stable source, product, port, consumer, environment, version, and effective-period identifiers.
4. **Data promise:** for publishing contracts, start with the embedded product descriptor (product id, name, domain, purpose, owners, lifecycle, ports, SLOs, support, and authoritative links); then provide schema, keys, grain, time meaning, semantics, classification, limitations, and profile-specific terms. Consumption contracts reference the descriptor and do not reproduce it.
5. **Trust and controls:** quality, SLOs, lineage, identity, policy, retention, expiry, revocation, support, and incidents.
6. **Change and lifecycle:** compatibility, notice, migration, exceptions, review, deprecation, and retirement.
7. **Enforcement and tests:** enforcement point, test, severity, failure outcome, telemetry, and evidence authority.
8. **Evidence and approvals:** supplied evidence, gaps, mandatory approvers, and decisions still required.
9. **Next actions:** prioritized actions with owners when known.
10. **Guidance used:** exact repository pages.

Use a YAML or JSON artifact only when requested or when a machine-readable draft materially helps. Label incomplete values `TBD`; do not manufacture values to satisfy a schema.

## Contract Review

Lead with findings ordered by **Blocker**, **Major**, then **Minor**. For every finding include:

- Affected term or boundary.
- Why it matters.
- Evidence or missing evidence.
- Concrete correction.
- Owner or decision authority when known.

Then provide the selected contract type, evidence coverage, compatibility status, approval readiness, residual risks, and smallest next actions.

## Compatibility Result

Return:

- Recommended version: patch, minor, or major.
- Compatibility status: compatible, breaking, or conditional.
- Structural changes.
- Semantic, service, policy, purpose, and lifecycle changes requiring human evidence.
- Affected upstream and downstream contract versions.
- Required tests, approvals, notice, coexistence, migration, rollback, and retirement evidence.

## Decision Language

Use only these readiness statements:

- **Draft ready for review:** complete enough to enter accountable review.
- **Not ready:** one or more blocking terms or evidence items are missing.
- **Conditionally compatible:** no proven breaking change, but material evidence remains incomplete.
- **Breaking change:** major version and managed migration are required unless executable evidence overturns the finding.

Do not use `approved`, `published`, `conformant`, or `go-live ready` unless the corresponding authoritative evidence was supplied.
