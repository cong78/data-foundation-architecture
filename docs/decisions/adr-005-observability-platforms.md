# ADR-005: System and Product Observability Platforms

## Status

Accepted — 2026-07-15

## Context

Foundation operators need service, infrastructure, pipeline, API, and workload health for incident response and reliability management. Product owners and consumers need freshness, quality, lineage, volume, usage, contract, and product SLO evidence.

Grafana Cloud is selected for platform-level system observability. Databricks system tables, product quality results, and Unity Catalog lineage are selected as primary product-observability authorities. Without a common telemetry protocol and identifiers, these tools would create disconnected dashboards and competing incident evidence.

## Decision

Use Grafana Cloud as the system-observability platform and Databricks plus Unity Catalog as the data-product-observability platform. Use OpenTelemetry and OTLP as the standard instrumentation and transport profile for foundation services and workloads.

Correlate system and product evidence with stable service, product, contract, run, consumer, environment, release, incident, and trace identifiers. Grafana Cloud owns platform health visualization and alert routing; Databricks and Unity Catalog remain authoritative for platform-native product quality, lineage, usage, and runtime metadata. The Data Service Portal displays governed projections and links rather than becoming another telemetry authority.

## Consequences

- Platform operators use one system-health and incident-observability experience.
- Product owners retain product-quality, lineage, usage, and contract context close to the data platform.
- OpenTelemetry reduces instrumentation coupling and supports collector or backend replacement.
- Cross-platform correlation requires controlled attributes, cardinality, retention, clock behavior, and sensitive-data hygiene.
- Alerts must identify the owning service or product and resolve to an actionable runbook.
- Neither Grafana nor Databricks alone represents complete end-to-end product trust; correlated evidence is required.

## Evidence

- [Observability Design](../reference-solutions/observability-design.md)
- [OpenTelemetry Standard](../standards/otel-telemetry-standard.md)
- [Data Observability Service](../services/data-observability-service.md)
- [Data Foundation Operations Service](../services/data-foundation-operations-service.md)

## Applicable Policy Decisions

- The [OpenTelemetry Standard](../standards/otel-telemetry-standard.md) governs instrumentation and correlation.
- The [Data Product Management Standard](../standards/data-product-management-standard.md) governs product SLO and trust evidence.
- The [Agent, Skill and LLM Standard](../standards/agent-skill-llm-standard.md) governs end-to-end AI traces when applicable.
- Backend-specific implementation changes must preserve OTel attributes, evidence authority, alert ownership, and trace correlation semantics.

## Review Date

2027-07-15, or earlier if observability vendors, telemetry standards, incident processes, product evidence authorities, or data-residency controls materially changes.
