# Tasks

- [x] 1. Read entry contracts, record decisions and validate this change before authoring payloads.
  Proof: strict OpenSpec validation; clean library/core refs recorded.
  Passed 2026-11-01: strict valid; library 2ce4d2f and core 7645b893 were clean on entry.
- [x] 2. Author the symbol, explicit footprint and device items, registered sources and original provenance.
  Proof: parse all records and audit each item with the selected clean core; preserve any CLI blockers.
  Passed 2026-11-01 on clean 7645b893: all three records parse and each item audit exits 0.
  The separate library check exits 5 with five source-unknown findings: its register reader only
  recognises S-ids, while the library's required D-0003 is registered and accepted by the item audit.
  This core integration blocker is reported and is not waived or disguised with source aliases.
- [x] 3. Generate/repeat native outputs and make the regeneration workflow handle explicit records.
  Proof: repeated byte comparison, workflow source checks and record checks without waived findings.
  Generation and the exact regeneration workflow pass on 7645b893. Two repeats equal committed
  output bytes. The S-only register failure on 7645b893 was fixed by the core worker in 04a9d07e.
  Final external record checks on a clean detached copy of that hash exit 0 without waivers;
  repeated generation and exact workflow body pass, and a reviewed plan produces six HTML sheets.
  These sheets were not accepted as human review and record evidence remains UNVERIFIED.
- [x] 4. Exercise the temporary local three-item distribution, reviewed get and offline build.
  Proof: sockets blocked, literal dependency pins preserved and authored/vendored definitions compared.
  Passed initially on 7645b893 and rerun for final data on detached 04a9d07e: reviewed offline get pins
  all three exact items, both builds and the
  frozen dry run pass, native used definitions/board model/connectivity equal the direct-record build.
  Socket and subprocess creation were denied throughout get/build. Only the authored subset was
  used; no board or published release was built. Informational policy/value findings remain visible.
- [x] 5. Document results, image URLs, remaining blockers and one changelog entry; commit with exact identity.
  Proof: focused checks, strict validation, git diff --check, unchanged board tree and clean signed commit.
  Passed 2026-11-01: exact record/audit/generation/sheet/offline proofs pass on detached 04a9d07e;
  workflow YAML, 19 Python heredocs, shell syntax, metadata/import controls, ruff/format and both strict
  changes validate. The root registry receipt authorises the official image pin; its expected-version
  CLI job stays required and unrun here. Board tree remains 15fa5f749fbeb0a4a020b947d4f2a6f2bf5c55b7.
  Exact user identity, one sign-off and clean local commit verified; no push, tag or release performed.
- [ ] 6. Complete human/external CI and release proofs only when separately authorised.
  Open: no review/oracle, upstream seed, push, PR, tag or published release is performed here.
