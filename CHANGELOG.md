# Changelog

All notable changes to the Data Foundation Architecture guidance are recorded here. The project follows Semantic Versioning for its declared public guidance interfaces.

## Unreleased

### Added

- Read-only Data Foundation Architecture Agent foundation with portable contracts and a company-assistant OpenAPI adapter.
- Agentic-by-design model for all foundation services, coordinated through the Data Service AI Assistant with contract-bounded specialist agents and typed skills.
- Consolidated selected implementation profiles and reusable records as Reference Solutions within Delivery.
- Decoupled published guidance from historical decision records so design and service pages can evolve independently.
- Placed Platform Architecture Design first in Architecture Core Guidance as the home for platform architecture and integration design.
- Established Platform Architecture as the technology-neutral capability-composition view.
- Defined cross-cutting technical capabilities as Platform Enablement and mapped their use across every data service.
- Reworked the data-domain foundation position into a layered visual of shared capabilities, ownership handoff, domain responsibilities, products, ports, and runtime placement.
- Replaced the Data Foundation Model conceptual flow with a layered, linked view of ownership, product progression, contract gates, and cross-cutting controls.
- Renamed the six-plane Target Architecture to Architecture Blueprint and the delivery-oriented blueprint to Implementation Blueprint.
- Renamed the shared agentic guidance to Agentic Data Service Design to emphasize service-level application across the foundation.
- Moved executable architecture rules into Decisions as the Architecture Decision Policy and removed them from the Standards catalog.
- Renamed the Delivery guidance area to Runbooks and reframed it as the execution layer for actions, assessments, implementation guidance, and reference solutions.
- Removed the standalone Learn from Examples section to keep Runbooks focused on actionable guidance and reusable reference solutions.
- Renamed Architecture Assistance to Agentic Architecture and placed it directly after Implementation Guidance.
- Reframed the Architecture to Operations Map as Architecture to Delivery, with data services as the owned delivery entities for building and operating the foundation.
- Removed the duplicate Choose an Action entry from Start Here; it remains under Runbooks.
- Reframed Definition and Scope around enterprise use-case admission, source-versus-foundation boundaries, and evidence-based direct, federated, projected, or replicated access decisions.
- Clarified the interoperability principle as Open and portable by design, leaving detailed artifact requirements to the Open Interoperability Standard.
- Clarified the portal principle as One service portal as the front door.
- Renamed the AI principle to AI readiness is embedded and clarified its data-product implications.
- Renamed the Principles page and navigation label to Design Principles.

### Changed

- Reorganized guidance around rationale-first architecture, separated vendor reference solutions and delivery assistance, and clarified why each foundation service exists.
- Data Foundation Architect skill `1.5.1` uses the canonical shared-capability design terminology.
- Release-readiness validation normalizes Markdown before checking deprecated architecture terms.

## 0.1.0 - 2026-07-15

### Added

- Initial consolidated foundation, architecture, service, playbook, standard, governance, assessment, template, reference-solution, and AI-skill guidance.
- Machine-readable architecture decision policy and executable OPA example.
- Architecture design taxonomy for service-specific, shared-capability, and integration designs.
- Service-to-design and target-plane mapping, shared platform capability design, and integration design.
- Publication-readiness validation for version metadata and canonical content structure.
- Apache License 2.0 for open use, modification, and distribution.

### Changed

- Data Foundation Architect skill updated to version 1.5.0 with design classification and cross-service integration guidance.
- Nine service pages consolidated as the authoritative location for definition, boundaries, architecture, capabilities, interfaces, controls, role-based actions, references, and done criteria.
- Shared controls and runtimes are consistently described as capabilities within one data foundation.
- Core glossary definitions and minimum completion criteria strengthened across standards and reference solutions.
- Mermaid rendering made deterministic across initial page loads and instant navigation.

### Status

- Incubating guidance release intended for controlled pilots.
- Runtime conformance is not implied by publishing this repository.
