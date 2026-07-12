# Data Product Workload Template

Use this template to define declarative runtime intent for one data-product workload.

## Workload Identity

| Field | Value |
| --- | --- |
| Workload id |  |
| Version |  |
| Owner |  |
| Product reference |  |
| Contract reference |  |
| Source revision |  |

## Execution

| Field | Value |
| --- | --- |
| Type | Batch / Stream / Service / Notebook / Model / Retrieval / Quality |
| Entry point |  |
| Schedule or trigger |  |
| Timeout and retry |  |
| Idempotency behavior |  |

## Ports and Dependencies

| Direction | Port or Dependency | Version | Purpose |
| --- | --- | --- | --- |
| Input |  |  |  |
| Output |  |  |  |

## Resource Profiles

| Resource | Profile | Scaling or Lifecycle Bounds |
| --- | --- | --- |
| Compute |  |  |
| Storage |  |  |
| Connector |  |  |
| Secret reference |  |  |
| Endpoint |  |  |

## Policy and Service Levels

| Area | Binding or Target |
| --- | --- |
| Identity and purpose |  |
| Classification and residency |  |
| Network policy |  |
| Freshness |  |
| Availability |  |
| Recovery |  |
| Cost budget |  |

## Environments and Promotion

| Environment | Configuration Overlay | Data Controls | Expiry | Approval |
| --- | --- | --- | --- | --- |
| Development |  |  |  |  |
| Test |  |  |  |  |
| Production |  |  | N/A |  |

## Deployment and Rollback

| Field | Value |
| --- | --- |
| Deployment strategy | Rolling / Canary / Blue-green |
| Health checks |  |
| Go-live gates |  |
| Rollback triggers |  |
| Last safe release |  |
| Recovery owner |  |

## Telemetry and Evidence

| Evidence | Location or Identifier |
| --- | --- |
| OpenTelemetry profile |  |
| Lineage events |  |
| Contract and quality tests |  |
| Policy and security checks |  |
| Deployment plan and receipt |  |
| Rollback rehearsal |  |

## Decision

**Status:** Draft / Review / Approved / Active / Suspended / Retired / Exception

**Approvers:**

**Conditions or exception expiry:**
