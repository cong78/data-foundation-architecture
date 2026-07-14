# Onboard a Source

<div class="decision-brief"><div><small>Use when</small><strong>New source data is required by governed products.</strong></div><div><small>Decision</small><strong>Approve source, pattern, contract, and operating profile.</strong></div><div><small>Owner</small><strong>Foundation ingestion owner with source owner.</strong></div><div><small>Output</small><strong>Validated source-aligned product and handoff.</strong></div></div>

## Preconditions

| Required | Evidence |
| --- | --- |
| Source owner and purpose | Accountable system owner and intended downstream outcomes. |
| Delivery option | File push, connector pull, API, CDC, or event stream feasibility. |
| Risk context | Classification, privacy, residency, retention, availability, and continuity needs. |

## Actions

| Step | Action and owner | Evidence |
| ---: | --- | --- |
| 1 | **Requester:** submit source, purpose, consumers, volume, cadence, and criticality through the portal. | Source onboarding record. |
| 2 | **Source and ingestion owners:** agree the Source System Ingestion Contract, change obligations, replay, support, and SLOs. | Approved Source System Ingestion Contract. |
| 3 | **Security and platform:** select identity, network, secret, connector, runtime, storage, and retention profile. | Approved technical plan. |
| 4 | **Ingestion team:** implement receipt, provenance, schema validation, quarantine, replay, lineage, and telemetry. | Tested ingestion release. |
| 5 | **Platform and steward:** validate the source-aligned output, classification, quality, freshness, limitations, and access against the same contract. | Published Source System Ingestion Contract. |
| 6 | **Operations:** activate dashboards, alerts, runbook, incident route, continuity, and recovery test. | Operational readiness evidence. |
| 7 | **Platform owner:** publish the validated product and handoff to domain teams. | Catalog entry, port, owner, support, and release record. |

## Stop Conditions

- Source owner will not accept availability, semantics, or change obligations.
- Data cannot be lawfully or securely processed in the selected boundary.
- No supported ingestion pattern can meet integrity, replay, or SLO needs.
- Parallel extraction bypasses the centrally managed ingestion service.

## Done Criteria

- Raw receipt is restricted, replayable, traceable, and quarantines invalid input.
- Validated source-aligned output has an approved contract, owner, lineage, quality, SLO, access, and support route.
- Failure, recovery, schema change, and source interruption are tested.

Authoritative inputs: [Ingestion Service](../services/data-ingestion-service.md), [Ingestion Design](../architecture/data-ingestion-design.md), and [Source Onboarding Template](../delivery-templates/source-onboarding-template.md).
