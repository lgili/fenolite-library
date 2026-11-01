## ADDED Requirements

### Requirement: Original unverified item closure
The library SHALL contain one original CC0 symbol, explicit footprint and device with matching ids,
versions and provenance. Records MUST use registered D-ids and remain UNVERIFIED without human review.
The device SHALL depend on the exact symbol and footprint item versions.

#### Scenario: Authored closure audited
- **WHEN** the three new items are audited with the selected core
- **THEN** each item passes schema, licence, provenance, dependency and source checks

### Requirement: Reproducible explicit outputs
Committed native symbol and footprint outputs SHALL reproduce from the explicit records using the core
record/backend APIs. The workflow MUST NOT send explicit records to a family-only generator or waive
findings to force a successful check.

#### Scenario: Explicit generation repeated
- **WHEN** each record is generated twice
- **THEN** both outputs equal the committed files byte for byte

### Requirement: Offline local vendoring proof
A local three-item distribution SHALL support reviewed get of the device closure and an offline build.
The proof MUST block network access, preserve item pins and compare the used definitions with an
authored-record build. No external seed, published release, tag or board modification is authorised.

#### Scenario: Device closure used offline
- **WHEN** the local get plan is confirmed and the design builds with socket creation blocked
- **THEN** all three items are pinned and the used definitions match the authored records

### Requirement: Image facts remain distinct from execution
Official KiCad image URLs and manifest metadata SHALL be recorded as read-only research. A candidate
digest MUST NOT be presented as runtime-verified until the selected image runs the expected CLI version.

#### Scenario: Digest found without a pull
- **WHEN** the official registry page names a 9.0.2 manifest
- **THEN** the report records its architecture and leaves runtime verification open
