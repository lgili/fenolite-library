# Four-board conversion review, 2026-11-01

This is a measured local review of the four existing converted CC-BY-SA-4.0 boards, using clean,
detached Fenolite core `b02e09fea8145442f0af61f571e58a075385df9e` (0.7.0.dev0). The library base is
`83e4ccf76529a45d1129393e6588d566ce69df09`. The [machine-readable receipt](conversion-replay-b02.json)
records exact input and raw-reply hashes, actual exit codes, level states and remaining blockers.

All 24 native input files matched their existing recorded SHA-256 values. They were reconstructed
from the local public corpus cache without network access. This checks the recorded bytes; it is
not a fresh fetch of upstream commit `97acc80c223d75520c03fc44cab63cd9a3202c42`. The original
ECC83 sibling project was retained so explicit project selection could be checked.

The private runtime used its own frozen dev/geo environment. No `kicad-cli`, native DRC, external
renderer oracle, GitHub Actions, tag, release or publication was run. Existing evidence labels and
historical accepted differences were retained; no new acceptance or human review was invented.

## Actual outcomes

| Item | Existing payload proof | Fresh import | Public library replay |
|---|---|---|---|
| ecc83 | exit 5; level 7 and S differ | exit 3, FEN-3004: unmapped `#PWR06` in source drawing | exit 5; import step exits 3 |
| sonde_xilinx | exit 5; level 7 and S differ | exit 3, FEN-3004: reference `U1` has conflicting symbols | exit 5; import step exits 3 |
| video | exit 5; level 7 and S differ | exit 3, FEN-3004: empty source symbol-library name | exit 5; import step exits 3 |
| kit-dev-coldfire-xilinx_5213 | exit 5; level 7 and S differ | exit 3, FEN-3004: unmapped `#PWR0106` in source drawing | exit 5; import step exits 3 |

Every baseline builds with the copy's copper guard in `warn`. Levels 1, 2, 4 and 5 compare equal;
level 3 matches historical footprint-name acceptances, and level 8 matches historical presentation
acceptances. Level 6 is equal except the Coldfire kit, which still matches two historical layer
acceptances. The receipt retains issue/notice counts, including routing left unjudged; an equal
comparison label is not a new native verification. Baseline times were 6.324 s, 8.309 s, 186.012 s and
89.161 s respectively; these are
local elapsed observations, not a controlled benchmark or a release performance promise.

Fresh imports produce no plan, so confirmation and fresh-design proof were not run. Replay reports
the failed first step and an empty-output/payload mismatch. No output-tree digest was filled from
unproduced output. All board payloads, item/provenance records, licences, notices and accepted
differences remain byte-identical to the base.

## Comparison with the historical issue report

The original [issues](../boards/ISSUES.md) cover thirteen demos; these four observations cannot close
claims about the other demos.

| Issue | Observation on this core and these four existing payloads |
|---|---|
| 1, copper guard blocks proof | The four baselines build with `warn`; proof reaches comparison. Fresh conversion is blocked earlier by source-symbol handling. |
| 2, artificial single-pad net | Level 2 is equal for all four baselines, including video and the Coldfire kit. Fresh-import/native-DRC behaviour remains unproved. |
| 3, stricter clearance than KiCad | No KiCad DRC ran; cm5_minima and tiny_tapeout are outside this replay. Remains open. |
| 4, outline stroke loss/noise | Old payloads still differ in outline width. Level 7 now reports `graphic-field` rather than paired missing graphics. Fresh preservation is blocked by import. |
| 5, user-layer table | Coldfire level 6 still uses two historical layer acceptances. No fresh conversion proves table preservation. |
| 6, video bottom field rotation | The old video payload still matches acceptance A003: R39 Reference 270 degrees versus 90 degrees. Not claimed fixed. |
| 7, fenolite.path noise | No raw or accepted `fenolite.path` difference occurs in any of the four baseline replies. |
| 8, ECC83 project selection | The baseline's against set contains only ecc83-pp's three files, despite the sibling project being present. |
| 9, dropped teardrops | complex_hierarchy and royalblue54L_feather were not rerun. Remains open here. |
| 10, S always skipped | S now runs for all four and reports actual differences; it does not silently pass. Fresh drawn-source conversion is blocked. |
| 11, royalblue derive/edge | That board was not rerun. Remains open here. |
| 12, folder-bound plan ids | Existing portable steps contain plain `--confirm`. Public replay reaches import rather than rejecting a stored plan id; source import fails, so reproduction is not proved. |
| 13, apparent missing courtyards | No new missing-courtyard finding is inferred. Coldfire still has two historically accepted level-6 layer differences; exact new-source preservation is unproved. |
| 14, repeated property name | openair-max was not rerun. Remains open here. |

## Reproduction and remaining gates

Stage the native source folders at their recorded hashes under `upstream/`, then use each item's
original `conversion.steps` import arguments with a dry run. Review a successful plan before
confirming it; this attempt never produced one. To compare an existing payload copied under `out/`:

```sh
fenolite verify-source out/design.py --against upstream/demos/ecc83/ecc83-pp.kicad_pro \
  --provenance out/PROVENANCE.json --timestamp 2026-11-01T00:00:00Z --json
fenolite library replay boards/cc-by-sa/kicad-demos/ecc83 --with-current --upstream upstream --json
fenolite library audit . --json
```

Root audit still exits 5 with the same 38 findings: 23 provenance errors, 12 proof failures, two
licence-text errors and one family mismatch. Source-import fixes must precede actual regenerated
payloads and current proof records. The public workflow pin, native-tool execution and exact-head
external branch CI remain separate gates. No board is promoted or declared ready for release.
