# Infrastructure validation

This branch prepares the external repository tasks of Fenolite c0279, c0273 and c0266. It creates no
pull request, tag, release or Pages deployment. Actual CI on the exact `cac/**` branch head is the
replacement for the originally proposed pull-request proof and is still pending.

## Tool selection

`library.toml` selects the exact public core commit
`b8b24842c1b792a0fcb37a6a7e5ca0270b90efd6`. CI installs its frozen dependency lock in an isolated
venv. A single update to `tools.fenolite` selects the future validated, published feature commit.
The installer checks the installed commit, licence-table equality and capability names; it never
substitutes a moving branch. Synchronise licences.toml with the selected core when updating the pin.

Local block checks used clean core `5d8afc2f5d98375aeb4ee548ae1d30487cb61f86` from an explicitly
selected sibling checkout in this repository's own venv. Device source-register and capability checks
separately selected clean device-packs core `2c9afd54767f811bdd94ef1fcc3e0acda23da97e`. Neither is the
public workflow pin. No complete combined feature integration or its CI is claimed here.

## Measured locally on 2026-11-01

| Check | Actual result |
|---|---|
| Strict infrastructure OpenSpec validation | Valid, no warnings |
| Root `library audit . --json` | Exit 5: 38 existing board findings; no root README/metadata finding |
| `library audit . --item blocks/cc0/FenoliteBlocks/resistor_link --json` | Exit 0 |
| `blocks index blocks/cc0/FenoliteBlocks/resistor_link --check --json` | Exit 0, current canonical record |
| `blocks test FenoliteBlocks:resistor_link --from blocks/cc0/FenoliteBlocks/resistor_link/__init__.py --json` | Exit 0: usage passed, golden equal, two tests passed |
| Exact block workflow Python body | Exit 0, including static import policy and import-side-effect probe |
| Import probe negative controls | File write, socket creation and process creation each refused |
| Shipped licence-copy comparison | One focused test passed; licences.toml matches the public pin and clean block core byte for byte |
| D-id source register | D-0001 and D-0002 validated by the clean device-packs reader |
| Workflow source checks | Five YAML files parse; shell blocks pass bash -n; Python heredocs compile |
| Public tool capability guard | Fails explicitly: blocks index/test and library check/seed unavailable |
| Local feature capability guards | Each exits 0 for its subset: index/test on the clean block core, check/seed on the clean device core |

The original resistor-link item is INFERRED. These are connectivity/package checks, not an independent
electrical or KiCad oracle. Its full CC0 legal text and author dedication are recorded; the closed
licence allow-list has not been relaxed to make it pass.

## Current blockers

The 38 board audit errors comprise 23 provenance errors, 12 proof failures, two licence-text errors and
one family mismatch. They include missing conversion output-tree digests, licence digest disagreements,
S levels skipped without recorded reasons and `apache-2.0` where the licence table expects `apache`.
Every existing board file remains unchanged from `first-boards` commit
`2cdbe73bf3069d22b1959f01cac087f6dbb6cc49`. No proof report or accepted difference was edited by hand.

The public tool pin lacks the newer record, block and seed commands. The records, origin and blocks
jobs therefore fail their capability guards. An [original UNVERIFIED device closure](authored-devices.md)
now supplies one symbol, footprint and device. Its item audits, explicit regeneration, record checks,
six generated review sheets and offline get/build comparison pass locally on detached fixed core
04a9d07e6e8d0140e9d07e2e89379531ecc03ef5. This includes the D-source reader fix required by these
records. The public tool pin, human record review, any LibrePCB seed and release proofs remain future work.

`tools.kicad_image` now pins the official 9.0.2 linux/amd64 manifest after the root worker's public
registry body/header digest verification, documented in [authored-devices](authored-devices.md#official-image-research).
The installer still requires an actual configured-version CLI run before replay, proof or rendering;
no image pull or CLI execution was performed here. The infrastructure checkpoint performed no new
board replay or proof. A later [four-board local review](conversion-replay-b02.md) uses exact core
b02e09fea8145442f0af61f571e58a075385df9e: existing payloads reach comparison, but fresh imports and
public replay are blocked by source-symbol handling. No board payload/proof record was changed,
and the same 38 audit findings remain release blockers.

A subsequent [frozen model-0 replay](conversion-replay-model0.md) selects clean exact core
`dbfd6fc36e18300c4a9aef1983f7130fea4e3b71` and verifies the source0 receipt/schema hashes. All 24
cached inputs still match. ECC83/sonde strict imports now confirm and their fresh proofs compare levels
1–7/S equal, but fail presentation. Video stops at written-drawing connectivity and Coldfire refuses
two layer-table items. The four existing payload proofs and root audit still fail. No payload,
provenance, source terms, accepted difference or public pin changes; raw diagnostics are retained.

Workflow checks here are source parsing, shell syntax, Python compilation and the explicitly executed
local block job. They are not a GitHub Actions run or actionlint proof. Actual branch CI, replay/proof,
release reproducibility and Pages remain unproved.

## Publication configuration still required

The check workflow runs on `cac/**` and `first-boards` pushes, manual dispatch and future contributions.
All items are checked, which includes every changed item. Board matrices use at most two workers.
Audit, records, regeneration, versions, origin, blocks, replay and proof expose independent results.
Renders are review artefacts; optional image generation never promotes evidence or changes accepted
differences. Missing tool capabilities fail the job before rendering; a rendering failure stays visible
as an optional failed step, while audit/records/replay/proof remain the required content gates.

Weekly benchmarks use the current approved tool pin with replay's `--with-current`, rather than the
conversion's recorded tool version. Manual dispatch can select another exact public candidate commit.
The separate scheduled workflow fails visibly and does not gate contribution merges. Its artefact retains
failures and elapsed times, or an explicit not-run report if setup fails. The latest
available table is included on the gallery's benchmark page. Regression issues are disabled by default;
manual `report_issues` or `LIBRARY_BENCH_ISSUES_ENABLED=true` enables one issue per newly failing board,
with an open-title duplicate check. Configure required reviewers for `library-benchmark-issues` first.

Before enabling publication, configure required reviewers on `library-release` and `github-pages`.
Then separately set `LIBRARY_RELEASE_ENABLED=true` and `LIBRARY_PAGES_ENABLED=true`. The workflows
fail explicitly while those switches are unset. No environment protection has been configured by this
local change. The release job validates an existing published release and its tag, runs checks, builds
assets twice and compares bytes, then attaches assets without replacement. It creates no tag or release.
The gallery follows a successful assets job (or an explicit tag dispatch), verifies SHA256SUMS, renders
fresh Fenolite images and publishes only after the configured Pages environment review.
