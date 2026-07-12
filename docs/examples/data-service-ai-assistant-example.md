# Data Service AI Assistant Example

This example defines a safe first release of the Data Service AI Assistant. It supports product discovery, contract drafting, and submission for review through the Data Service Portal.

## Release Scope

| Capability | Autonomy | Status Change |
| --- | --- | --- |
| Search and explain products | A0 Explain | None. |
| Draft a contract | A2 Draft | None until user saves. |
| Submit a product for review | A3 Confirmed action | Draft to review. |

External sharing, entitlement grants, publication, retirement, deletion and infrastructure changes are excluded from the first release.

## Agent Manifest

```yaml
agent_id: data-service-portal-assistant
version: 1.0.0
owner: data-foundation-product-team
goal: Help authenticated users discover products and prepare governed product work.
maximum_autonomy: A3
prohibited_goals:
  - grant entitlements
  - publish or delete products
  - bypass product go-live controls or policy
identity:
  workload: spiffe://company.example/data-foundation/portal-assistant
  delegated_user: required
llm_profile: enterprise-reasoning-standard
skills:
  - product.search@1
  - contract.draft@1
  - product.submit_review@1
budgets:
  max_turns: 12
  max_tool_calls: 20
  timeout_seconds: 120
  cost_class: low
memory:
  conversation: 24h
  working: task_lifetime
  preference: explicit_opt_in
```

## Read Skill

```yaml
skill_id: product.search
version: 1.0.0
description: Find live products that fit an authenticated user's purpose.
side_effect: read
input_schema:
  type: object
  required: [purpose]
  properties:
    purpose: {type: string, maxLength: 500}
    domain: {type: string}
    product_type: {type: string}
    health: {enum: [healthy, attention, incident]}
output_schema:
  type: object
  required: [products, observed_at]
  properties:
    products: {type: array}
    observed_at: {type: string, format: date-time}
authorization:
  policy: catalog.read_for_purpose
tool:
  operation_id: searchProducts
  api: catalog-openapi-v1
```

## Draft Skill

```yaml
skill_id: contract.draft
version: 1.0.0
description: Draft an ODCS contract from approved product and source context.
side_effect: draft
input_schema:
  type: object
  required: [product_id, purpose]
  properties:
    product_id: {type: string}
    purpose: {type: string}
    source_ids: {type: array, items: {type: string}}
output_schema:
  type: object
  required: [odcs_document, validation, assumptions]
authorization:
  roles: [product_owner, contract_editor]
context:
  - product descriptor
  - source contracts
  - classification
  - enterprise contract profile
approval:
  rule: user_reviews_before_save
```

## Confirmed Action Skill

```yaml
skill_id: product.submit_review
version: 1.0.0
description: Submit one draft product version to its go-live workflow.
side_effect: reversible_write
input_schema:
  type: object
  required: [product_id, product_version, idempotency_key]
  properties:
    product_id: {type: string}
    product_version: {type: string}
    idempotency_key: {type: string}
authorization:
  roles: [product_owner]
  policy: product.submit_review
approval:
  rule: explicit_confirmation
  preview_fields: [product_id, product_version, failed_gates, impacted_owners]
tool:
  operation_id: submitProductReview
  api: product-workflow-openapi-v1
reliability:
  timeout_seconds: 20
  retries: 0
  compensation: withdraw_review_before_first_approval
```

## Example Interaction

1. User asks: “Find a healthy customer product for approved churn analysis.”
2. Assistant calls `product.search@1` with authenticated purpose and policy-filtered context.
3. Assistant returns products with contract, health, freshness and source links.
4. User asks for a contract draft for the selected product.
5. Assistant calls `contract.draft@1`, validates the ODCS artifact and highlights assumptions.
6. User edits and saves the draft through the contract service.
7. Assistant proposes `product.submit_review@1` and shows the exact product version, gate status and effect.
8. User confirms; policy authorizes the call and the workflow returns a review id.
9. Assistant displays a receipt with product, contract, workflow, approval and trace identifiers.

## MVP Acceptance Tests

- A user cannot discover restricted products outside their purpose and attributes.
- Search answers cite product and contract versions plus observation time.
- Contract drafts validate against the pinned ODCS schema.
- Unsupported assumptions are shown separately from sourced facts.
- Submission cannot target a different product or version than the approved preview.
- Duplicate submission with the same idempotency key has no additional effect.
- Prompt injection in product descriptions or retrieved documents cannot add skills or permissions.
- Every run emits agent, model profile, skill, tool, user, purpose, product, contract, approval, trace, latency, token and cost evidence.
