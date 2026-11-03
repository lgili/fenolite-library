## ADDED Requirements

### Requirement: Factual metadata preserves source and proof bytes
A corrected licence digest SHALL use the registry's stated normalisation and a currently approved
text. Metadata-only repairs SHALL preserve payload, original licence, original notice and fidelity
records; no failed proof SHALL become a pass through metadata editing.

#### Scenario: A raw licence hash was recorded
- **WHEN** the preserved licence text has an already-approved normalised digest
- **THEN** provenance records that digest and the old proof outcome is unchanged

### Requirement: New licence text needs real approval
A newly accepted licence-text digest SHALL have a documented CODEOWNER decision on the actual
preserved text. Matching an upstream file is necessary evidence but SHALL NOT fabricate that decision.

#### Scenario: Upstream bytes match but approval is absent
- **WHEN** a preserved upstream licence has an unregistered digest
- **THEN** the approval remains pending and the licence finding is not waived

### Requirement: Board refreshes have actual complete proof
New board payloads and proof records SHALL come from reviewed CLI plans and real default full proofs,
with exact source/input/output identities and no invented skips or acceptance. CI/publication remain
pending until root verifies the required jobs on the exact published source.

#### Scenario: A fresh conversion still differs
- **WHEN** its full proof reports a difference
- **THEN** retain the failure and do not publish it as a passing refresh
