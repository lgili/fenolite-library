## 0. Entry

- [x] 0.1 Read repository instructions, the four original recipes, boards/ISSUES.md and core replay/proof
  contracts; record exact core/source selection. Proof: strict OpenSpec validation and source-hash receipt.
  Passed 2026-11-01: strict validation valid without warnings; existing provenance's 24 native file
  hashes all match staged cached bytes. Original issues 1–12 and later entries 13–14 are retained.

## 1. Actual replay

- [x] 1.1 Reconstruct the original input folders from hash-matching cached bytes and assert the immutable
  core/environment. Proof: input/runtime receipt containing every file hash and exact core SHA.
  Passed 2026-11-01: private detached b02e09fea8145442f0af61f571e58a075385df9e is clean;
  its isolated frozen dev/geo environment installs offline and reports fenolite 0.7.0.dev0. The
  input receipt names all 24 hashes and the recorded source commit for each board. No network used.
- [ ] 1.2 Run baseline proofs and fresh reviewed import/proof commands for ECC83 and sonde xilinx.
  Retain raw exit codes, differences and skips. Proof: actual saved CLI replies and receipt summary.
  Partial measured 2026-11-01: both baseline proofs exit 5 with actual level-7/S differences;
  fresh dry imports exit 3/FEN-3004 (ECC83 unmapped power symbol; sonde conflicting U1 symbols).
  No plan exists, so confirmation and fresh-design proof remain blocked, not passed.
- [ ] 1.3 Run the same commands for video and the Coldfire kit; report any real blocker immediately.
  Proof: actual saved CLI replies and receipt summary.
  Partial measured 2026-11-01: both baseline proofs exit 5; fresh imports exit 3/FEN-3004
  (video empty source library name; Coldfire unmapped power symbol). No fresh plan/proof exists.
- [x] 1.4 Exercise public library replay for all four records with --with-current and the explicit
  local upstream input tree. Preserve step failures and output mismatches; do not repair digests from
  unproduced outputs. Proof: actual replay replies, exit codes and unchanged library item digests.
  Executed 2026-11-01: all four commands exit 5, recording import step exit 3 and an empty-output
  mismatch. This task records those failures, not successful reproduction. All item/provenance,
  licence and notice bytes remain unchanged; no output-tree digest was fabricated.

## 2. Records and closing

- [ ] 2.1 Update only actual generated conversion/proof/provenance/item records, with exact tool/output
  hashes and portable steps. Preserve source licences/notices and introduce no new acceptance waiver.
  Proof: per-item audit, repeated payload digest comparison and source-term byte comparison.
- [ ] 2.2 Compare measured outcomes with the twelve original issues and later entries 13–14. Update
  measured status and one changelog entry. Proof: status matches saved CLI replies; JSON/TOML parse;
  strict OpenSpec validation; clean signed local commit.
- [ ] 2.3 Root runs exact-head external branch CI, approved native-tool gates and any later publication.
  This worker performs no push, pull request, tag or release.
