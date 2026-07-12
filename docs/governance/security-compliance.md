# Security and Compliance

Use the [Unified Access Design](../architecture/unified-access-design.md) and [Access Control Standard](../standards/access-control-standard.md) for named-user, workload, delegated, agent, service, and data authorization requirements.

Security and compliance controls must be embedded across ingestion, product creation, consumption, and sharing.

## Control Areas

| Area | Guidance |
| --- | --- |
| Identity | Use strong identity for users, services, pipelines, and AI agents. |
| Access | Enforce least privilege, role-based and attribute-based controls where needed. |
| Classification | Classify data during onboarding and maintain classification through product outputs. |
| Masking | Mask, tokenize, or aggregate sensitive fields based on policy and purpose. |
| Audit | Log access, sharing, administrative changes, and policy decisions. |
| Retention | Apply retention and deletion rules consistently across storage and derived products. |
| Encryption | Encrypt data in transit and at rest using approved key management patterns. |
| Residency | Respect regional, contractual, and regulatory data location constraints. |
| Telemetry hygiene | Prevent sensitive data from being exposed in traces, logs, metrics, events, or labels. |

## AI-Specific Controls

- Validate whether data is approved for AI training, retrieval, agent access, or model evaluation.
- Track which data products are used by AI systems.
- Prevent sensitive data from entering unmanaged prompts, logs, embeddings, or model outputs.
- Apply policy to service accounts and agent identities, not only human users.
- Maintain evidence for compliance reviews and model risk management.
- Treat retrieved content and tool output as untrusted input that cannot redefine agent goals or permissions.
- Limit every agent to registered skills, least-privilege scopes, bounded autonomy, time and cost budgets.
- Require independent approval summaries and step-up authorization for privileged, destructive, external or high-cost actions.
- Isolate and govern conversation, working, preference and organizational memory.
- Test prompt injection, tool misuse, excessive agency, privilege escalation, memory poisoning and data exfiltration.

## Minimum Evidence

- Access approval records.
- Data classification metadata.
- Data lineage and transformation history.
- Quality validation results.
- Sharing agreements and recipient entitlements.
- Audit logs for access and administrative changes.
- Observability evidence for incidents, SLO breaches, and data product health.
- Retention and deletion evidence.
