# Contributing

## Before Changing Guidance

1. Read `GOVERNANCE.md` and `COMPATIBILITY.md`.
2. Identify the affected journey stage, architecture layer or plane, service, standard, playbook, evidence, and adopter profile.
3. Classify the change as editorial, compatible guidance, breaking architecture, or urgent correction.
4. Open or update an architecture decision when the change affects boundaries, ownership, public interfaces, normative meaning, or technology defaults.

## Authoring Rules

- Keep principles directional, rules atomic, and criteria observable.
- Use the Architecture Decision Policy for normative architecture content.
- Preserve stable ids and avoid renaming concepts without migration guidance.
- Keep the technology-neutral contract separate from reference-solution bindings.
- Add evidence rather than unsupported maturity or implementation claims.
- Mark unknown or unexecuted runtime behavior as `not-assessed`.
- Update source Markdown and machine-readable artifacts; never edit generated `site/` output.

## Local Validation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/validate_architecture_policies.py
opa fmt --fail policies/rego
opa check --strict policies/rego
opa test policies/rego -v
mkdocs build --strict
python scripts/check_internal_links.py site
python scripts/check_navigation.py
python scripts/check_release_readiness.py
```

Run the validation commands for both AI skills when guidance paths, templates, schemas, examples, or output contracts change.

## Pull Request Evidence

Describe:

- Problem and intended outcome.
- Change class and version impact.
- Affected public interfaces and adopters.
- Decisions, alternatives, and migration behavior.
- Tests and evidence produced.
- Remaining risks or explicit exceptions.

Do not claim conformance from documentation existence alone. A conformance claim requires an applicable standard, explicit scope, test result, and retained evidence.
