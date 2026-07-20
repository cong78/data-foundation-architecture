# Guidance Map

Load only the pages required by the active workflow. Paths are relative to the repository root.

| Concern | Authoritative guidance |
| --- | --- |
| Definition, core elements, business value, fields, lifecycle, tests, approval, versioning | `docs/standards/data-contract-standard.md` |
| Placement, contract chain, control architecture, enforcement outcomes | `docs/architecture/data-contract-design.md` |
| Contract system and cross-service enablement | `docs/services/platform-enablement-service.md` |
| Portal authoring, review, workflow, and status experience | `docs/services/data-service-portal.md` |
| Source boundary and ingestion enforcement | `docs/services/data-ingestion-service.md` and `docs/reference-solutions/source-onboarding-template.md` |
| Product definition, creation, go-live, and change | `docs/architecture/data-product-design.md`, `docs/services/data-product-creation-service.md`, and `docs/reference-solutions/data-product-template.md` |
| Consumer purpose, access, obligations, and revocation | `docs/services/data-consumption-service.md` and `docs/architecture/unified-access-design.md` |
| External sharing profile | `docs/services/data-sharing-service.md` and `docs/reference-solutions/data-sharing-design.md` |
| AI consumption profile | `docs/standards/ai-ready-data-standard.md` and `docs/architecture/agentic-data-foundation.md` |
| Catalog, Delta, and physical binding | `docs/standards/catalog-storage-standard.md` |
| Identity and policy enforcement | `docs/standards/access-control-standard.md` |
| Portable representation and interoperability | `docs/standards/open-interoperability-standard.md` |
| Contract telemetry and operational evidence | `docs/standards/otel-telemetry-standard.md` and `docs/services/data-observability-service.md` |
| Contract incidents, changes, recovery, and runbooks | `docs/services/data-foundation-operations-service.md` and `docs/reference-solutions/service-runbook-template.md` |

## Loading Rules

- Always read the Data Contract Standard.
- Read Data Contract Design when selecting or placing a contract.
- Read only the service and profile pages touched by the boundary.
- Read interoperability guidance before claiming ODCS or round-trip conformance.
- Read evidence rules before recommending approval, publication, access, or go-live.
