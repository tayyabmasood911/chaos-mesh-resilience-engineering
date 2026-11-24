# Security Policy

## Supported Versions

The following versions of this project are currently supported with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 1.x.x   | :white_check_mark: |
| < 1.0.0 | :x:                |

## Reporting a Vulnerability

We take the safety and stability of our chaos engineering and resilience testing frameworks seriously. If you discover a vulnerability or potential security flaw, please report it responsibly.

### Disclosure Process

1. **Private Reporting**: Please **DO NOT** file a public GitHub issue. Send your vulnerability report directly via email to **[tayyabmasood911@gmail.com](mailto:tayyabmasood911@gmail.com)** with the subject line `[SECURITY] chaos-mesh-resilience-engineering Vulnerability`.
2. **Details to Include**:
   - Description of the vulnerability and attack vector.
   - Minimal reproduction manifest or experiment script.
   - Affected Chaos Mesh CRD or injection daemon component.
   - Proposed mitigation or remediation patch if available.
3. **Response Timelines**:
   - **Initial Acknowledgement**: Within 24 hours.
   - **Triage & Assessment**: Within 72 hours.
   - **Remediation & Advisory Release**: Coordinated fix within 14 business days.

## Security Controls & Safety Guardrails

- **Namespace Isolation**: Chaos experiments must be scoped strictly using namespace selectors and forbidden from targeting control-plane namespaces (`kube-system`, `chaos-mesh`, `cert-manager`).
- **Emergency Circuit Breaker**: All experiments include automatic abort timers and automated Prometheus SLI monitors that roll back injections if error rate exceeds 1%.
- **RBAC Boundaries**: Chaos CRD privileges must be granted strictly via cluster-scoped RBAC policies with audit logging enabled.

## Safe Harbor

We consider security research conducted in good faith under this policy to be authorized. We will not pursue legal action against researchers who adhere to responsible disclosure principles.
