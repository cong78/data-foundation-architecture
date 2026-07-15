# Compatibility Policy

## Public Interfaces

The following are versioned public interfaces of this project:

- Published page paths and named architecture concepts.
- Architecture policy ids, decision semantics, and evidence meanings.
- JSON Schemas and YAML API versions under `policies/` and the AI skill packages.
- The three data-contract types and their boundary meanings.
- Product patterns, lifecycle states, service boundaries, target planes, and journey stages.
- Delivery templates and mandatory fields.
- AI skill manifests, schemas, capability ids, and output contracts.

Pure visual styling, spelling, and non-semantic prose are not public interfaces unless they change interpretation or accessibility.

## Versioning

The repository version in `VERSION` follows Semantic Versioning:

- **Patch:** backward-compatible correction or clarification.
- **Minor:** backward-compatible capability, profile, optional field, example, or guidance addition.
- **Major:** incompatible meaning, removed interface, stricter mandatory behavior without transition, or schema and decision change requiring adopter migration.

Schemas and individual policy, profile, contract, workload, skill, and evidence artifacts retain their own versions. A repository release records the compatible set.

## Compatibility Rules

- Stable ids are never reused for a different meaning.
- Compatible additions do not invalidate previously valid artifacts.
- Unknown extension fields are preserved where the underlying format allows them.
- Breaking changes include affected-object analysis, migration instructions, coexistence where feasible, and a retirement date.
- Technology-profile changes cannot silently redefine the technology-neutral outcome.
- A newer evaluator may replace OPA only when decision input, output, identifiers, tests, and evidence semantics remain compatible.

## Support Window

Until version `1.0.0`, releases are incubating and may introduce breaking improvements, but every breaking change still requires a changelog entry and migration note. After `1.0.0`, support the current major version and one preceding major version for migration unless a published security, legal, or safety correction requires faster retirement.

## Deprecation

Deprecation records the replacement, reason, first deprecated version, last supported version, migration steps, owner, and retirement date. Deprecated content remains readable during its support window and cannot disappear from a patch or minor release.
