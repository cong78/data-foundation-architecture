# How to Use This Guide

<div class="decision-brief"><div><small>Use when</small><strong>You know the question but not the right page.</strong></div><div><small>Decision</small><strong>Understand the rationale, locate responsibility, verify a rule, or apply a solution.</strong></div><div><small>Owner</small><strong>The reader making or supporting the decision.</strong></div><div><small>Output</small><strong>Shortest authoritative reading path.</strong></div></div>

## Guidance Philosophy

The main guidance explains **why the foundation is needed and what responsibilities, boundaries, relationships, and decisions define it**. It does not require readers to understand a selected vendor or detailed implementation before they can understand the architecture.

Implementation content is deliberately separated:

- **Architecture** explains rationale, logical structure, ownership, and relationships.
- **Services** explain reusable outcomes and responsibility boundaries.
- **Standards** state mandatory rules and evidence.
- **Decisions** preserve the rationale for important choices.
- **Runbooks** provide actions, assessments, implementation guidance, executable assistance, and reference solutions.
- **Reference Solutions**, inside Runbooks, combine optional technology profiles with reusable records for adopting and evidencing them.

## Start by Intent

| Intent | Start here | Do not start by... |
| --- | --- | --- |
| Understand the whole foundation | [Foundation in One View](foundation-in-one-view.md) | Reading every architecture page in menu order. |
| Complete a task | [Action Playbooks](../playbooks/index.md) | Assembling steps from several standards. |
| Make an architecture decision | [Architecture Overview](../architecture/overview.md) and [Design Principles](principles.md) | Selecting technology before defining the boundary. |
| Understand a platform capability | [Services Overview](../services/index.md) | Treating a reference solution as the service contract. |
| Verify a mandatory rule | [Architecture Decision Policy](../decisions/architecture-decision-policy.md) and [Standards Overview](../standards/index.md) | Relying on a diagram or summary sentence. |
| Apply Databricks or Grafana | [Reference Solutions](../reference-solutions/index.md) under Runbooks | Copying a vendor pattern without the technology-neutral contract. |
| Trace architecture into an owned capability | [Architecture to Delivery](architecture-to-delivery.md) | Treating architecture, service delivery, and operation as separate concerns. |
| Plan adoption | [Runway](../runway.md) and [Maturity Assessment](../assessments/data-foundation-maturity-assessment.md) | Launching all components at once. |
| Record delivery evidence | [Reusable reference records](../reference-solutions/index.md#reusable-reference-records) | Keeping approval and evidence only in presentation material. |

## Content Contracts

| Content type | It answers | Reader action |
| --- | --- | --- |
| Definition and principles | Why, scope, boundary, and decision rules. | Align before design. |
| Architecture | What exists, where it sits, and how it interacts. | Make or review a design decision. |
| Service | What reusable capability the foundation provides and owns. | Design or consume a service contract. |
| Playbook | Who does what, in which order, with which evidence. | Complete a task. |
| Standard | What is mandatory, how it is expressed, executed, and evidenced. | Implement or test a control. |
| Reference solution | How a selected technology can implement the architecture and which decisions and evidence must be retained. | Assess a profile, adapt it, and complete its reference record. |
| Runbook | How an authorized operator diagnoses, contains, recovers, validates, and escalates a known condition. | Operate and exercise a live capability. |
| Runway and assessment | What to build next and how maturity is proven. | Prioritize adoption. |

## Rationale-First Page Contract

Core architecture and service guidance should make these elements easy to find. A page may combine sections when the answer is short, but it should not omit the reasoning.

| Element | Question It Answers |
| --- | --- |
| Purpose | Why does this capability or design exist? |
| Rationale | Which problem does it solve, and why is this direction preferred? |
| Responsibility | What outcome does it own? |
| Scope and boundaries | What is included, excluded, or owned elsewhere? |
| Relationships | How does it depend on and support the rest of the foundation? |
| Principles and decisions | Which rules guide choices when implementations differ? |
| Minimum evidence | What proves that the intended outcome exists? |

Detailed APIs, schemas, deployment steps, product-specific configuration, and vendor mechanics belong in standards, delivery assets, or reference solutions unless they are essential to explaining a boundary.

Design pages depend only on published architecture, service contracts, and standards. Historical decision records are maintained independently and may explain how guidance evolved, but they are not prerequisites for interpreting or implementing the current design.

## Reading Rule

1. Start with the five-stage journey for orientation or a playbook for a known task.
2. Use architecture to understand the rationale, logical boundary, and relationships.
3. Use service pages to locate ownership and standards to verify mandatory rules.
4. Treat a direction as fixed only when it is explicit in published architecture, service guidance, or a mandatory standard.
5. Use reference solutions only after the technology-neutral outcome is clear.
6. Finish delivery work with recorded evidence, the applicable runbook, and the next gate.

<div class="read-next"><strong>Next:</strong> open Foundation in One View for orientation or choose an Action Playbook for execution.</div>
