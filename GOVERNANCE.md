# Project Governance

## Purpose

This repository governs the architecture language, standards, schemas, examples, skills, and decision evidence for the Data Foundation Architecture. It does not own an adopter's runtime platform, risk acceptance, product go-live, or operational support decisions.

## Decision Roles

| Role | Accountability |
| --- | --- |
| Project steward | Maintains scope, release integrity, navigation, and final repository decisions. |
| Architecture owner | Owns principles, target architecture, service boundaries, and architecture decisions. |
| Standard owner | Owns normative rules, policy bundles, test requirements, exceptions, and review dates. |
| Implementation-profile owner | Owns technology mappings without changing the technology-neutral architecture contract. |
| Adopter | Selects profiles, supplies implementation and operational evidence, and owns local risk decisions. |
| Reviewer | Challenges correctness, interoperability, security, operability, and compatibility with evidence. |

Named people and teams belong in the repository hosting platform, CODEOWNERS configuration, or adopter governance register. Do not embed personal ownership in portable architecture artifacts.

## Change Classes

| Class | Examples | Required review | Version impact |
| --- | --- | --- | --- |
| Editorial | Grammar, broken links, presentation, non-semantic clarification. | Documentation review and automated checks. | Patch. |
| Compatible guidance | New optional guidance, example, template field, profile, or backward-compatible schema addition. | Affected architecture or standard owner plus automated checks. | Minor. |
| Breaking architecture | Removed or redefined requirement, changed identifier meaning, incompatible schema, lifecycle, decision, evidence, or service boundary. | Project steward, affected owners, adopter impact review, migration and deprecation plan. | Major. |
| Urgent correction | Security, legal, safety, or materially incorrect guidance. | Expedited owner review with documented rationale and follow-up. | Patch or major according to compatibility impact. |

## Proposal and Decision Flow

1. Open a change proposal describing the problem, scope, affected public interfaces, alternatives, adopters, risks, migration, evidence, and target release.
2. Express new normative behavior through the Architecture Policy Language and update applicable standards and tests.
3. Update architecture, services, playbooks, standards, templates, examples, skills, and generated artifacts together when their contracts are affected.
4. Run all repository checks and record unresolved findings or exceptions.
5. Obtain the reviews required by the change class.
6. Merge with changelog and compatibility notes.
7. Publish an immutable release tag and retain superseded guidance for the supported compatibility window.

## Normative Authority

Normative requirements are identified by stable policy ids and uppercase BCP 14 keywords. Narrative examples and technology profiles cannot weaken them. When pages conflict, the active machine-readable policy and its cited authoritative standard take precedence until the inconsistency is corrected.

## Review Cadence

- Active standards and profiles are reviewed at least annually and after material regulatory, security, platform, or interoperability changes.
- Deprecated interfaces retain migration guidance and a retirement date.
- Evidence and implementation claims are reviewed at the cadence declared by the adopter; stale evidence becomes `not-assessed` rather than remaining a pass.

## Release Decision

A release requires a clean strict documentation build, internal-link validation, schema and example validation, policy tests, skill validation, changelog entry, and compatibility classification.
