# Data Product Workload Standard

<div class="decision-brief"><div><small>Use when</small><strong>Declaring how a product workload is built and operated.</strong></div><div><small>Decision</small><strong>Is runtime intent portable, controlled, testable, and recoverable?</strong></div><div><small>Owner</small><strong>Workload owner and platform owner.</strong></div><div><small>Output</small><strong>Versioned workload plan and execution receipts.</strong></div></div>

This standard defines the portable, declarative runtime intent for building and operating a data product. It complements the publishing data contract, including its embedded product descriptor; it does not duplicate business or interface semantics.

## Workload Source Document

The workload source document must be version-controlled, machine-validatable, environment-neutral, and exportable. Runtime-specific manifests are generated projections.

```yaml
apiVersion: data.foundation/v1alpha1
kind: DataProductWorkload
metadata:
  id: customer-profile-build
  version: 1.2.0
spec:
  productRef: customer-profile@2.1.0
  contractRef: customer-profile-contract@2.1.0
  sourceRevision: 8f2c1ab
  workload:
    type: batch
    entrypoint: jobs/build_customer_profile.sql
  inputs:
    - portRef: crm-customer-source@3.0.0
  outputs:
    - portRef: customer-profile-table@2.1.0
  resources:
    computeProfile: standard-medium
    storageProfile: governed-product
  policies:
    - pii-restricted
    - eu-residency
  serviceLevels:
    freshness: PT24H
    availability: 99.5
  environments:
    strategy: promote
    targets: [development, test, production]
  deployment:
    strategy: canary
    rollbackOn: [contract_failure, quality_failure, slo_breach]
  telemetry:
    profile: data-product-default
```

## Required Fields

| Area | Requirement |
| --- | --- |
| Identity | Stable workload id, semantic version, owner, and source revision. |
| Product binding | Exact product id and publishing-contract version containing its descriptor. |
| Execution | Workload type, entry point, schedule or trigger, timeout, retry, and idempotency. |
| Ports | Versioned input and output port references. |
| Resources | Portable compute, storage, connector, secret-reference, and endpoint profiles. |
| Policy | Data handling, identity, purpose, network, residency, and approval bindings. |
| Service levels | Freshness, availability, latency, recovery, and cost expectations. |
| Environments | Promotion strategy, target environments, configuration inheritance, and expiry. |
| Deployment | Plan, preview, rollout strategy, health checks, rollback triggers, and rollback target. |
| Telemetry | Required OpenTelemetry profile, lineage emission, release markers, and cost attribution. |

## Validation Stages

| Stage | Required Checks |
| --- | --- |
| Author | Schema, references, naming, ownership, and unsupported fields. |
| Pull request | Contract compatibility, policy, security, quality, lineage, portability, cost, and dependency impact. |
| Plan | Resolved resources, changes, deletions, permissions, approvals, estimated cost, and rollback feasibility. |
| Deploy | Immutable artifact, environment policy, separation of duties, go-live gates, and health checks. |
| Operate | Drift, SLOs, quality, usage, cost, vulnerabilities, contract conformance, and expiry. |

## Environment Rules

- Environment differences are overlays; they must not fork product meaning or contract semantics.
- Secret values never appear in the workload document or generated plan.
- Production uses the same immutable artifact that passed test.
- Every temporary environment has an owner, budget, expiry, and deletion policy.
- Production changes require an approved release record and a tested rollback target.

## Channel Rules

- Portal, API, CLI, CI/CD, and agent skills operate on the same workload resource and task API.
- Every mutating request supports idempotency and returns a durable task id.
- Plans and previews are generated independently of the client channel.
- Agent skills may draft or submit workload changes but cannot bypass policy, approval, or go-live gates.

## Minimum Done Criteria

- JSON Schema or equivalent validation is available in editor, CLI, API, and CI.
- A dry-run plan resolves all references without changing runtime state.
- Generated runtime manifests can be recreated from portable source artifacts.
- Environment promotion preserves product, contract, workload, and artifact identity.
- Drift is detectable and either reconciled or recorded as an approved exception.
- Rollback is automated, rehearsed, observable, and linked to the release record.
