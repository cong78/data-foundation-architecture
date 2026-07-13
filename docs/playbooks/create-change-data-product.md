# Create or Change a Data Product

<div class="decision-brief"><div><small>Use when</small><strong>A reusable product outcome or change is approved.</strong></div><div><small>Decision</small><strong>Build new, change compatibly, version, or consolidate.</strong></div><div><small>Owner</small><strong>Product owner and owning domain team.</strong></div><div><small>Output</small><strong>Release candidate with complete go-live evidence.</strong></div></div>

## Actions

| Step | Action and owner | Evidence |
| ---: | --- | --- |
| 1 | **Product owner:** frame purpose, consumers, value, alignment pattern, owner, and non-goals; search for existing products. | Product brief and reuse decision. |
| 2 | **Product team:** pin input contracts and design output contract, semantic context, ports, policy, SLOs, support, and lifecycle. | Reviewed product design. |
| 3 | **Developer:** declare workload, dependencies, environments, resources, tests, telemetry, release, and rollback. | Versioned workload plan. |
| 4 | **Product team:** implement transformations, quality, lineage, interfaces, documentation, and operational controls. | Immutable candidate artifact. |
| 5 | **CI and reviewers:** test contract, compatibility, quality, security, policy, lineage, reliability, portability, and affected consumers. | Passing test and review evidence. |
| 6 | **Product owner:** prepare migration, communication, release notes, and support for breaking or material change. | Impact and migration record. |
| 7 | **Product team:** submit the exact candidate to product go-live. | Candidate release linked to all evidence. |

## Change Decision

| Condition | Action |
| --- | --- |
| Existing product satisfies the outcome | Reuse or extend it; do not create a duplicate. |
| Change is backward compatible | Release a minor or patch version under the compatibility policy. |
| Schema, meaning, policy, quality, or SLO breaks consumers | Create a major version with migration and coexistence. |
| Consumer-specific logic becomes common | Consolidate it into a shared aggregate product. |

## Done Criteria

- Candidate has one owner, purpose, contract, context, ports, workload, lineage, policy, SLO, support, and rollback target.
- Critical tests pass and unresolved risks are explicit.
- Consumers and dependencies are known before release.

Authoritative inputs: [Product Lifecycle](../architecture/data-product-lifecycle-design.md), [Contract Design](../architecture/data-contract-design.md), [Product Creation Service](../services/data-product-creation-service.md), and [Workload Standard](../standards/data-product-workload-standard.md).
