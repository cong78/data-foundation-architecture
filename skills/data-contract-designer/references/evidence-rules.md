# Evidence Rules

## Evidence Levels

| Level | Meaning | Permitted statement |
| --- | --- | --- |
| Supplied | A resolvable artifact, test, approval, runtime record, or observation was provided. | State what the evidence directly proves and its observation time. |
| Declared | A target or assertion appears in a draft contract without execution evidence. | Describe it as a proposed or declared term. |
| Missing | Required evidence was not supplied or cannot be resolved. | Record a gap, owner, and evidence needed. |
| Conflicting | Sources disagree or refer to different versions or times. | Report the conflict and block the affected conclusion. |

## Integrity Rules

- Do not infer approval from a person's name, workflow state, meeting note, or draft signature field.
- Do not infer runtime conformance from schema validity or successful publication.
- Do not treat current health as proof of historical SLO attainment.
- Do not treat Unity Catalog metadata, a Delta table, an API specification, or a legal agreement as the complete data contract.
- Tie evidence to exact contract, source, product, port, consumer, environment, policy, and runtime versions.
- Record observation time and authority for mutable evidence.
- Treat screenshots and copied text as weaker than resolvable system records.
- Mark compatibility conditional when semantic or runtime evidence is incomplete.

## Blocking Evidence Gaps

Block an approval or publication recommendation when any applicable item is missing:

- Accountable parties and exact boundary bindings.
- Purpose, valid and prohibited use, classification, or policy authority.
- Required schema, semantics, quality, service level, lineage, or support terms.
- Critical contract-specific tests and runtime binding.
- Compatibility and impact assessment for a change.
- Consumer migration for a breaking change.
- Expiry and revocation evidence for consumption or sharing.
- Required security, privacy, legal, product, source, or consumer approval.
