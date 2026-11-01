# Reproducible local board replay

Decided 2026-11-01 under the maintainer's standing recommended-answer authorisation:

- Work in a separate external worktree from infrastructure 83e4ccf76529a45d1129393e6588d566ce69df09.
  This repository has no AGENTS.md; README, CONTRIBUTING and POLICY govern its contents.
- Pin a private detached core checkout and isolated offline dev/geo environment to immutable
  b02e09fea8145442f0af61f571e58a075385df9e. Leave the public workflow pin unchanged until the
  maintainer has published and validated its final feature integration.
- Reconstruct the native input folders only from already cached files whose SHA-256 exactly matches
  the existing recorded proof. Preserve project siblings so the ECC83 project-selection regression
  can be measured. No network or changed upstream revision is required for those matching bytes.
- First record the existing payload's proof, then rerun the original import recipe in a fresh folder.
  Use the actual CLI result for generated files and proof records, including failures and skips.
  Reviewed local plans may be confirmed, but stored replay steps remain portable without plan ids.
- Carry no new acceptance waivers. Historical accepted differences remain review evidence; measure
  their applicability against fresh raw results instead of changing a report by hand.
- Preserve original LICENSE content and upstream NOTICE lines. Any dated conversion notice names
  the actual core and measured scope. Regenerated item manifests list only their actual payloads.
- Save complete command replies and exit codes outside the repository, and commit compact measured
  status where useful. Skipped/unavailable native oracles, unresolved conversions and audit errors
  are blockers, never a passing label. Actual external branch CI and publication remain root-owned.

The old issue report describes thirteen demos; this iteration changes only the four existing converted
items named above. Findings for other boards are not claimed resolved by those four measurements.

## Frozen model 0 replay — Decided 2026-11-01

Replay the same four items at exact core dbfd6fc36e18300c4a9aef1983f7130fea4e3b71, from external
checkpoint 4551805c42547d89f869cdfb2b307a6d9122017f. The private detached core source remains read-only;
its offline dev/geo environment and every temporary input/output are outside both repositories.
Reuse the source0 model receipt and verify its schema hashes against the exact cut. Recheck all 24
cached native input SHA-256 values, including ECC83's sibling project, before any conversion.

Measure fresh strict dry imports first so reader refusals are reported promptly. Review real plans
before confirming into temporary candidate folders; refuse new lossy/acceptance/tolerance flags. Fresh
proofs use the fresh provenance with no new accepted differences. Existing-payload proofs retain their
unchanged historical acceptance metadata and are identified separately, never labelled fresh equality.
A failed fresh candidate does not replace a published item merely because it produced bytes. Preserve
existing item/licence/notice/provenance bytes unless actual acceptable outputs justify their update.

Save full command replies outside the repositories and commit compact actual diagnostics, per-level
states, input/tool/source hashes and dated ISSUES notes. Keep all nonzero exits/skips visible. No source
reader patch, model migration, native Altium claim, external CI, public tool-pin update or publication
is part of this replay. Coordinate reader blockers with the core source owner rather than editing the cut.
