# Changelog

## [Unreleased]

- `bench.yml` runs the recorded `verify-source` step read-only, as the `proof` job of `check.yml` does since
  1.0.0; its first run (41954400114) failed ecc83 (two project files, FEN-2001) and the Coldfire kit.

## [1.0.0] - 2026-11-05

First release (Fenolite changes c0266, c0273, c0279): the authored `FenoliteDevices` device, symbol and
footprint items, the reviewed seeded `LibrePCBBaseReview` resistor set, the authored `FenoliteBlocks`
`resistor_link` block and six converted KiCad demo boards with a usable licence (CC-BY-SA-4.0; never the
non-commercial demo licence): ecc83, interf_u, kit-dev-coldfire-xilinx_5213, microwave, multichannel and
pic_programmer. `release.yml` attaches the assets to the published GitHub Release after `check.yml` passes on
the tag; it never creates the tag or the release.

- Pin Fenolite `e7673c81`: the public head `468d8a61` of `cac/dev-rewrite`, which has every command the jobs
  require, plus c0266 tasks 6.1 (review sheets independent of the Python version) and 6.2 (a device review
  stores the digest of the record as written). `licences.toml` equals its shipped copy. `e7673c81` must be
  published unchanged before the jobs can install it.
- Move out tiny_tapeout, complex_hierarchy, video, openair-max, sonde_xilinx and royalblue54l_feather: converted
  with cores before c0355, their replay or proof fails on the pin (decided 2026-11-05 by the coordinator). They
  stay in git history; their refresh after a core fix is the v1.1 item.
- The `proof` job runs the recorded `verify-source` step read-only (its project file, levels, KiCad version and
  target) instead of the upstream folder with default options; ecc83, with two project files, ended in FEN-2001.
- `bench.yml` lets `fenolite library replay` fetch the pinned upstream itself instead of passing `--upstream`.
- Renew the sheet hashes of the four reviewed LibrePCB items under Luiz Carlos Gili's approval of 2026-11-04:
  record digests, geometry, dependencies and the four pin-grid warnings are unchanged; the sheets differ only in
  the viewer code and the gzip header byte (`docs/librepcb-sheet-renewal-20261104.json`).

- Integrate nine complete, previously sealed 1.0.2 board items with unchanged source terms and zero accepted differences. Nine item proof/version audits pass; the root audit changes from 21 to two unchanged Royal errors. Preserve Microwave’s measured no-copper/no-schematic scopes and all Royal L7, public-pin, CI and release gates.

- Integrate the four explicitly re-approved LibrePCB resistor-subset records with corrected D-0005 source, exact contractual review receipts and deterministic native outputs. Preserve earlier approvals and all existing board audit/CI/release blockers.

- Preserve exact963f9cc0 diagnostic proof/record receipts for nine passing board conversions, including Microwave’s measured no-copper/no-schematic scopes. Retain Video L6, Royal L7, root-path alias and OpenAir blockers explicitly; authoritative board data and the public tool pin remain unchanged.

- Record fresh strict all-level equality for Tiny, Complex, Multichannel, Interf and ECC83 on clean diagnostic corec2f555d0; preserve Royal’s genuine derived-cache failures and all existing payload bytes. Public pin, release eligibility and CI remain pending.

- Record Luiz Carlos Gili’s explicit approval of the four CURRENT renderer
  sheets and exact reviewed CLI acceptance receipts (c0338/c0333), retaining
  all warnings. This does not close CI or release gates.

- Prepare the reviewed official KiCad10.0.6 immutable CI container pin required
  by common-tool derived padvia proofs (c0333). Registry manifests/config hashes
  reconcile with the core pin; historical9.0.2 is retained in the review record.
  Actual container version execution, final public core pin and CI remain pending.

- Record actual local combined-source full proof equality for Tiny Tapeout,
  Multichannel, Interf and ECC83 with zero accepted differences; retain the
  measured Complex cache blocker and immutable payload/source terms. Public
  tool pin, final CI and payload replacement remain pending (c0333).

- Restore the already-approved authored CC0 licence text from the clean core
  registry (c0333/S-1097). Prove every pre-existing core and library text digest
  remains accepted; retain all board payload bytes and other policy settings.

- Measure all ten remaining converted boards on immutable diagnostic core d348705f
  (c0333): Microwave passes without acceptance; nine retain explicit blockers.
  Preserve all 969 authoritative files and the public tool pin pending final CI.

- Register three preserved original licence texts after explicit CODEOWNER
  approval, with exact upstream/hash and separate decision records (c0333).
  Correct factual digest metadata without changing licences or proof results;
  audit findings reduce from27 to21, all still-visible conversion/proof work.

- Canonicalise Tiny Tapeout's Apache family path and RoyalBlue's lowercase
  library identity (c0333), preserving payloads and original upstream names.
  The now-readable RoyalBlue record exposes previously masked proof and
  provenance findings; all remaining findings stay visible.

- Correct seven raw-versus-normalised licence-digest records using an already
  approved text (c0333); retain every payload, licence, original notice and
  historical fidelity result. Metadata versions become 1.0.1. The diagnostic
  audit reduces 32 findings to 25 without waiving the remaining blockers.

- Refresh Video and Sonde to 1.0.1 on signed core de6c6f2f: actual full nine-level
  proofs pass without acceptance and both portable replays reproduce their
  packaged trees. Preserve upstream terms and public tool pin; the root audit
  retains 32 unrelated findings. See docs/item-refresh-maintainer-host.md.

- Repeat the four strict conversions on signed core 1918e632: Video passes all
  nine levels without acceptance; ECC83 and sonde retain presentation findings,
  and Coldfire explicitly refuses unsupported bold rendering. Preserve existing
  item payloads, upstream terms and proofs; the audit still has 38 findings.

- Measure four licensed-board conversions on immutable b02e09fe, dbfd6fc3 and L10 695dee0f.
  All four L10 strict imports confirm and levels 1–7/S compare equal; full proofs retain presentation
  failures. Preserve all board payloads, source terms, proof records and accepted differences (c0282).
- Add an original UNVERIFIED FenoliteDevices symbol/footprint/device closure, explicit-record
  regeneration and local offline-vendoring proofs against the documented D-source checker fix;
  pin the registry-verified official KiCad 9.0.2 amd64 manifest, with CLI execution still required.
- Prepare repository licensing, immutable tool selection, independent validation/publication workflows
  and an original CC0 resistor-link block. Existing board conversions and proof records are unchanged.
