## ADDED Requirements

### Requirement: Repository licensing and provenance
Repository-owned files SHALL use CC0-1.0. Each item MUST retain its own licence, notices and provenance.
The README SHALL state the test/benchmark purpose and that items are not used for machine-learning training.

#### Scenario: Existing boards retained
- **WHEN** this infrastructure change is compared with its base
- **THEN** no file under boards changes

### Requirement: Immutable tool selection
Workflows SHALL install the exact public Fenolite commit named in library.toml. A job needing an
unavailable command MUST fail visibly and MUST NOT report a missing or skipped check as passing.

#### Scenario: Feature pin not ready
- **GIVEN** a public pin without blocks index
- **WHEN** the block job runs
- **THEN** it fails and names the missing capability

### Requirement: Independent checks and deferred publication
CI SHALL expose audit, records, blocks, replay, proof, renders and benchmark reports. Release and gallery
publication MUST require explicit protected-environment approval and MUST NOT create a tag or pull request.

#### Scenario: Local preparation
- **WHEN** infrastructure is prepared locally
- **THEN** no remote branch, tag, pull request, release or Pages deployment is created

### Requirement: Original block package
The new block item SHALL contain only original CC0 material, one exported BlockDef, canonical block.json,
usage, tests and a golden. Index and block tests MUST run with the selected local feature checkout.

#### Scenario: Record matches source
- **WHEN** blocks index --check runs with the implemented feature checkout
- **THEN** the committed record matches and no write is planned
