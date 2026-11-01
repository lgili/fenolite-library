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
- [x] 1.2 Run baseline proofs and fresh reviewed import/proof commands for ECC83 and sonde xilinx.
  Retain raw exit codes, differences and skips. Proof: actual saved CLI replies and receipt summary.
  Historical b02 measurement 2026-11-01: both baseline proofs exit 5 with actual level-7/S differences;
  fresh dry imports exit 3/FEN-3004 (ECC83 unmapped power symbol; sonde conflicting U1 symbols).
  No b02 plan existed. Completed command execution on frozen dbfd6fc3: both strict dry runs and
  exact-plan confirmations exit 0; both fresh proofs run all nine levels with zero accepted differences
  and exit 5 at presentation only. Levels 1–7/S equal. This is measured execution, not a passing proof.
- [ ] 1.3 Run the same commands for video and the Coldfire kit; report any real blocker immediately.
  Proof: actual saved CLI replies and receipt summary.
  Partial measured 2026-11-01: both baseline proofs exit 5; fresh imports exit 3/FEN-3004
  (video empty source library name; Coldfire unmapped power symbol). No fresh plan/proof exists.
  Frozen dbfd6fc3 continuation: video now exits 5/FEN-5001 at the written-drawing connectivity guard;
  kit exits 7/FEN-7001 for two layer-table items. No plan/confirmation/fresh proof, so this remains open.
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
  Still open at dbfd6fc3: neither fresh candidate passes all levels, and video/kit produce no plan.
  Existing payload/provenance/item/licence/notice bytes and acceptances remain unchanged by policy.
- [x] 2.2 Compare measured outcomes with the twelve original issues and later entries 13–14. Update
  measured status and one changelog entry. Proof: status matches saved CLI replies; JSON/TOML parse;
  strict OpenSpec validation; clean signed local commit.
  Completed in the frozen-cut continuation: portable diagnostics and issues 15–16 retain actual
  nonzero results; JSON/TOML and SHA assertions plus strict validation pass. One changelog entry.
- [ ] 2.3 Root runs exact-head external branch CI, approved native-tool gates and any later publication.
  This worker performs no push, pull request, tag or release.

## 3. Frozen model 0 cut replay — 2026-11-01

- [x] 3.1 Verify the exact dbfd6fc3 model 0 source receipt/schema hashes, isolated read-only core/runtime,
  external 4551805c base and all 24 unchanged cached inputs. Proof: runtime/source/input SHA receipt.
  Passed: exact clean core/tree and all 20 source0 schema digests checked before/after commands;
  all 24 cached native files retain their recorded hashes. Isolated frozen dev/geo install was offline.
- [x] 3.2 Execute the four strict fresh import dry runs, review/confirm actual successful plans in tmp,
  and run available fresh plus existing-payload fidelity proofs. Preserve real refusals/differences,
  per-level states and skipped reasons. Proof: saved actual replies and measured summary; no new acceptance.
  Executed all four dry imports, two reviewed confirmations, two fresh full proofs and four baseline
  proofs. The receipt validates actual exits 0/5/7 and explicitly marks the two unavailable fresh proofs
  not-run, with no invented per-level result. Neither fresh full proof passes. No new loss/accept flag.
- [x] 3.3 Reconcile ISSUES and compact diagnostics with the actual cut and historical b02 findings;
  preserve terms/item bytes where new payloads do not satisfy policy. Proof: parse/audit, input and
  payload/terms SHA comparison, strict OpenSpec and signed local review commit. Root-owned task 2.3
  remains open; no push or native/external CI claim.
  Passed diagnostic reconciliation: JSON/TOML parse and source/input/payload/terms SHA assertions;
  strict OpenSpec valid without warnings. Actual audit still exits 5 with the same 38 findings, retained
  as blockers. Only documentation/diagnostics change, in the signed local review commit.
