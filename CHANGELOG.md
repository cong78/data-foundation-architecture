# Changelog

All notable changes to the Data Foundation Architecture guidance are recorded here. The project follows Semantic Versioning for its declared public guidance interfaces.

## Unreleased

- Removed the detailed Runbook Contract from Architecture to Delivery.
- Renamed End-to-End Architecture Scenarios to End-to-End Service Scenarios and moved the page from Architecture into Services.
- Added consistent Context, Forces, Decision, Consequences, and Verification reasoning to every core architecture design.
- Added four end-to-end architecture scenarios and a technology-neutral authority map for decision ownership, enforcement, and evidence.
- Added a schema-validated architecture registry with typed relationships, CI validation, and an Architecture mode in the interactive knowledge graph.
- Simplified Definition and Principles to a concise definition, one foundation-boundary test, clear accountability, and nine decision principles; removed repeated access, domain, workflow, and exception detail.
- Removed the redundant How to Read the Structure section from the Architecture Knowledge Graph.
- Added Foundation in One View as the orientation step before readers follow the staged Foundation Journey.
- Simplified the Service-to-Design Map to service architecture, integration, and blueprint placement; moved supporting-design dependencies into each service and kept technology profiles in Reference Solutions.
- Reworked Architecture Views into a five-level decision path with explicit routing to each authoritative detailed design.
- Clarified that data contracts define provider-consumer promises, while identity, purpose, policy, workflow gates, and service authority bound agent autonomy.
- Moved Architecture Knowledge Graph from Start Here into Architecture, beside the architecture navigation and design maps.
- Replaced the Architecture Overview core-logic flowchart with a layered, clickable value flow, governance rail, trust rail, and explicit architectural rule.
- Renamed Documentation Knowledge Graph to Architecture Knowledge Graph across navigation and guidance references.
- Added an interactive documentation knowledge graph generated from navigation and page references, an information-architecture quality assessment, and a CI freshness check.
- Consolidated the separate Governance section into one Platform Governance Design under Architecture, covering authority, control placement, lifecycle governance, assurance, forums, exceptions, and evidence.
- Renamed Data Product Developer Experience to Developer Experience Design across navigation and architecture guidance.
- Renamed Shared Platform Capabilities to Platform Enablement Design across navigation, architecture guidance, service references, and skill context.
- Added a visual definition model showing source authority, the shared data-foundation responsibility, governed data products, purpose-bound consumers, and the boundary rule between them.
- Prevented journey stage names from breaking into fragments by giving the clickable stage header a stable responsive layout.
- Combined definition, scope, and design principles into one Definition and Principles page placed immediately after Foundation in One View.
- Removed the duplicated five-stage sequence from Foundation in One View and made each richer Why Each Stage Matters row a direct link to its applicable guidance.
- Reworked Data Product Lifecycle Design into Data Product Design as the authoritative definition, boundary, design-element, ownership, lifecycle, contract-alignment, and go-live guide for a data product.
- Moved the action-to-playbook selector into How to Use This Guide so the foundation view remains focused on rationale, journey, and structure.
- Added a strategy-to-outcome opening that explains why a shared data foundation is essential to enterprise data and AI execution.
- Aligned the Deliver journey stage with its end state: governed data products are brought live, with testing retained as a go-live control rather than the stated outcome.

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

- Removed OpenLineage as an architecture standard and retained technology-neutral, exportable lineage requirements with stable identifiers and interoperability tests.
- Replaced specialized terminology with clearer language for source artifacts, stable identifiers, published schemas, standard profiles, and primary service designs.
- Replaced service-level Done Criteria with Target User Experience outcomes for each service persona and journey.
- Structured every Target User Experience as user intent, action, required service behavior, and observable result so product owners and engineers can share end-to-end acceptance scenarios.
- Simplified the five-stage foundation journey into a numbered sequence and added a distinct request sequence to the Architecture Blueprint.
- Replaced the Action and Evidence Map with a plain-language Challenge, Action, Value, and Proof view for every journey stage.
- Promoted the supporting-model comparison into a structural map showing how journey, architecture, planes, services, products, and runway work together.
- Reorganized guidance around rationale-first architecture, separated vendor reference solutions and delivery assistance, and clarified why each foundation service exists.
- Data Foundation Architect skill `1.5.1` uses the standard shared-capability design terminology.
- Release-readiness validation normalizes Markdown before checking deprecated architecture terms.

## 0.1.0 - 2026-07-15

### Added

- Initial consolidated foundation, architecture, service, playbook, standard, governance, assessment, template, reference-solution, and AI-skill guidance.
- Machine-readable architecture decision policy and executable OPA example.
- Architecture design taxonomy for service-specific, shared-capability, and integration designs.
- Service-to-design and target-plane mapping, shared platform capability design, and integration design.
- Publication-readiness validation for version metadata and required content structure.
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
