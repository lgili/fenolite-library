## ADDED Requirements

### Requirement: Original inputs and immutable tool
The four board replays SHALL use the recorded native input hashes and exact core commit. Source
terms, licences and upstream notices MUST remain intact; no native board material may enter the core.

#### Scenario: A cached input differs
- **WHEN** a cached native file does not match its recorded SHA-256
- **THEN** it is refused as an input and no refreshed proof is claimed

### Requirement: Measured conversion and proof records
Refreshed payloads and proof/provenance records SHALL come from actual CLI commands. Failures and
skips MUST remain visible. New accepted differences, invented oracle results and manually cleaned
proof reports MUST NOT be introduced to make a board pass.

#### Scenario: A conversion still differs
- **WHEN** a new proof reports a difference without an existing matching disposition
- **THEN** the measured failure is retained and reported as a blocker

### Requirement: Scoped status and portable replay
Measured status SHALL identify the tool and affected four boards, compare historical issues without
claiming untested boards resolved, and preserve portable conversion steps without stored plan ids.
CI, native-oracle and release gates SHALL remain open until actually performed.

#### Scenario: A reviewed local plan is confirmed
- **WHEN** conversion bytes are written after local plan review
- **THEN** the portable provenance records equivalent plain-confirm steps and the actual output digest
