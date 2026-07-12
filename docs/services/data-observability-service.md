# Data Observability Service

## Definition

The data observability service observes data products end to end from both **system telemetry** and **data insight telemetry**. It uses OpenTelemetry as the standard model for collecting, correlating, and exporting telemetry across ingestion, transformation, product publication, consumption, and sharing.

The goal is to make data trust measurable. A consumer should be able to understand whether a data product is fresh, complete, reliable, used, compliant, and fit for purpose.

## Scope

| In Scope | Out of Scope |
| --- | --- |
| OpenTelemetry conventions, collectors, exporters, dashboards, alerts, and product telemetry standards. | Replacing the enterprise observability platform. |
| Product health across freshness, quality, reliability, usage, cost, incidents, and lineage correlation. | Owning business decisions about acceptable product quality. |
| Data insight signals such as volume, distribution, anomaly, and business rule changes. | Storing sensitive business data inside traces, logs, labels, or metrics. |

## Observability Dimensions

| Dimension | What It Observes | Example Signals |
| --- | --- | --- |
| System health | Runtime and platform behavior. | Pipeline latency, job failures, API errors, queue lag, storage errors, retries. |
| Data quality | Fitness of data against product expectations. | Completeness, validity, uniqueness, consistency, anomaly scores, failed records. |
| Freshness | Whether data is updated within expected time windows. | Last successful load, event delay, source lag, product freshness SLO. |
| Lineage and impact | How data moves from source to product to consumer. | Source version, transformation run, product version, downstream dependency. |
| Usage and adoption | How consumers use data products. | Query volume, API calls, active consumers, AI model usage, unused products. |
| Cost and efficiency | Resource consumption and waste. | Compute time, storage growth, expensive queries, duplicate processing. |
| Business data insights | Domain-level changes visible in the data. | Volume anomalies, distribution shifts, threshold breaches, process exceptions. |

## Core Capabilities

- OpenTelemetry collector and exporter patterns.
- Standard telemetry schema for data foundation services.
- Data product health dashboard.
- Product-level quality, freshness, and availability SLOs.
- Lineage-aware trace correlation from source to consumer.
- Alerting for data incidents and reliability breaches.
- Anomaly detection for data volumes, distributions, and business rules.
- Usage insights for BI, application, platform, AI agent, and model consumers.
- Incident workflow integration and post-incident evidence capture.
- Observability metadata publication to the data catalog.

## Architecture Guidance

OpenTelemetry should not only observe infrastructure. It should carry data product context through traces, metrics, logs, and events. For example, a failed transformation trace should be linkable to the product version, source batch, quality rule, affected consumers, and incident record.

The observability service should avoid creating a separate truth from the catalog. Product metadata, ownership, classification, lineage, and lifecycle status should be synchronized with the catalog and governance services.

OpenTelemetry describes operational telemetry; OpenLineage describes runtime data lineage. Correlate both using canonical product, dataset, job, run, and trace identifiers instead of forcing either standard to replace the other.

Use the [OpenTelemetry Telemetry Standard](../standards/otel-telemetry-standard.md) for required attributes, metrics, trace expectations, and telemetry hygiene.

## Telemetry Model

| Lifecycle Point | Signals |
| --- | --- |
| Source extraction | Source availability, source lag, schema version, record count, extraction duration. |
| Landing | Landing success, rejected records, quarantine count, storage path, ingestion batch or event id. |
| Transformation | Job duration, rule execution, transformation version, dependency status. |
| Validation | Quality rule result, threshold breach, anomaly score, failed fields, go-live status. |
| Publication | Product version, contract version, freshness timestamp, catalog publication status. |
| Consumption | Consumer identity, access channel, latency, query or API status, usage purpose. |
| Sharing | Recipient entitlement, delivery status, export count, expiry, revocation status. |

## Controls

- Every live data product has freshness and quality SLOs.
- Every foundation service emits OpenTelemetry-compatible telemetry.
- Telemetry includes product, domain, environment, owner, and classification attributes.
- Data incidents are linked to affected products and consumers.
- Sensitive values are not exposed in logs, traces, labels, metric attributes, or events.
- Observability dashboards are available to product owners, engineers, and support teams.

## Done Criteria

- OpenTelemetry conventions are documented and used by foundation services.
- Product health dashboard shows freshness, quality, reliability, usage, incidents, and cost.
- Alerts are routed to accountable owners.
- Incidents can be traced from affected consumer back to product, pipeline, and source.
- Observability evidence is available for go-live approval, audit, and operational review.
- OTLP telemetry and OpenLineage events are accepted by independent reference receivers.
