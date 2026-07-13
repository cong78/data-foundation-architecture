# Data Observability Service

## Definition

The data observability service observes data products end to end through both **system telemetry** and **data product telemetry**. It uses OpenTelemetry as the standard model for collecting, correlating, and exporting telemetry across ingestion, transformation, product publication, consumption, and sharing.

The goal is to make data trust measurable. A consumer should be able to understand whether a data product is fresh, complete, reliable, used, compliant, and fit for purpose.

## Scope

| In Scope | Out of Scope |
| --- | --- |
| OpenTelemetry conventions, collectors, exporters, dashboards, alerts, and product telemetry standards. | Replacing the enterprise observability platform. |
| Product health across freshness, quality, reliability, usage, cost, incidents, and lineage correlation. | Owning business decisions about acceptable product quality. |
| Data product signals such as volume, distribution, anomaly, usage, cost, and business-rule changes. | Storing sensitive business data inside traces, logs, labels, or metrics. |
| Health signals, alert context, incident correlation, and recovery evidence. | Coordinating support, incident command, problem, change, release, communication, or improvement workflows; these belong to the [Data Foundation Operations Service](data-foundation-operations-service.md). |

## Observability Dimensions

| Dimension | Telemetry Type | What It Observes | Example Signals |
| --- | --- | --- | --- |
| System health | **System** | Runtime and platform behavior. | Pipeline latency, job failures, API errors, queue lag, storage errors, retries. |
| Data quality | **Data product** | Fitness of data against product contract and expectations. | Completeness, validity, uniqueness, consistency, anomaly scores, failed records. |
| Freshness | **Both** | Runtime delivery delay and whether the product meets its freshness SLO. | Source lag and job completion (**system**); last product update and freshness breach (**product**). |
| Lineage and impact | **Both** | Runtime movement plus product and consumer dependencies. | Job, run, and dataset events (**system**); product version and affected consumers (**product**). |
| Usage and adoption | **Data product** | Whether and how consumers use the product. | Active consumers, query and API use by product, AI usage, unused interfaces, reuse rate. |
| Cost and efficiency | **Both** | Runtime resource cost and product-level cost-to-serve. | Compute and storage consumption (**system**); unit cost, duplicate processing, and cost by product or consumer (**product**). |
| Business data insights | **Data product** | Domain-level behavior visible in product data. | Volume anomalies, distribution shifts, threshold breaches, process exceptions. |

### Telemetry Boundary

| Type | Core Question | Primary Ownership | Typical Scope |
| --- | --- | --- | --- |
| System telemetry | Is the platform or service operating correctly? | Platform and service owners. | Runtime, infrastructure, API, pipeline, queue, storage, network, and deployment. |
| Data product telemetry | Is the product trustworthy, used, compliant, and meeting its contract? | Data product owner, steward, and reliability owner. | Quality, freshness, availability, usage, consumer impact, business behavior, and cost-to-serve. |
| Correlated telemetry | How did a system event affect a product and its consumers? | Shared operational responsibility. | Source-to-runtime-to-product-to-consumer trace, incident, and impact evidence. |

System signals become product telemetry only when they are evaluated in product context. For example, a successful job is system telemetry; whether that job produced the expected product version within its freshness SLO is data product telemetry.

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

Observability owns detection and health evidence. The [Data Foundation Operations Service](data-foundation-operations-service.md) owns coordinated response, operational records, communication, recovery validation, and improvement. Both share stable service, product, release, incident, and correlation identifiers.

OpenTelemetry describes operational telemetry; OpenLineage describes runtime data lineage. Correlate both using canonical product, dataset, job, run, and trace identifiers instead of forcing either standard to replace the other.

Use the [OpenTelemetry Telemetry Standard](../standards/otel-telemetry-standard.md) for required attributes, metrics, trace expectations, and telemetry hygiene.

## Telemetry Model

| Lifecycle Point | System Telemetry | Data Product Telemetry |
| --- | --- | --- |
| Source extraction | Source connection, extraction duration, retry, failure, source lag. | Expected source version, record-volume expectation, source contract status. |
| Source-aligned landing | Landing success, storage operation, batch or event id, quarantine operation. | Received volume, rejected-record rate, schema conformance, source-product freshness. |
| Transformation | Job duration, runtime status, dependency status, compute and memory use. | Product version produced, transformation lineage, expected output volume, cost-to-produce. |
| Validation | Rule-engine execution, test duration, test-system errors. | Quality result, threshold breach, anomaly score, failed fields, go-live readiness. |
| Publication | Catalog and interface publication status, API deployment status. | Product, contract and semantic-context versions, freshness timestamp, product availability. |
| Consumption | Query or API latency, error, throughput, rate limit, adapter status. | Consumer, purpose, product usage, SLO experience, access decision, cost-to-serve. |
| Sharing | Delivery job status, transfer latency, endpoint failure. | Recipient entitlement, minimized package, export volume, purpose, expiry, revocation. |

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
