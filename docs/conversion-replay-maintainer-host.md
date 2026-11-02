# Four strict conversions on the maintainer host

Measured 2026-11-02 on clean signed core
`1918e63214a7d0123e1f5fa8ef095c73fd2e1472`, package `0.7.0.dev0`, model 0,
CLI v0, against library base `4932137d10f74289f7009f2252f67cdf229a471f`.
All 24 original native input hashes match. Four actual dry-import plans were
reviewed for new scratch-only targets and confirmed by their exact plan IDs;
all 280 written files match their planned SHA-256 values.

| Board | Strict import | Full default proof |
| --- | --- | --- |
| video | exit 0, 117 files | exit 0; all levels 1–8/S equal, zero accepted differences |
| kit-dev-coldfire-xilinx_5213 | exit 0, 113 files | exit 3; explicit bold on `in_out_conn.kicad_sch:text[Volt].effects` cannot be rendered faithfully by the current mask renderer |
| ecc83 | exit 0, 22 files | exit 5; levels 1–7/S equal; one 72-pixel level-8 finding |
| sonde_xilinx | exit 0, 28 files | exit 5; levels 1–7/S equal; two missing root-sheet panel findings caused by differing filename identities |

The Coldfire refusal produces no measured per-level results. It preserves the
explicit style instead of substituting default ink. ECC83's finding is
`72/57480` versus `0/57480` in the recorded region. Sonde's panels are
`sheet:sonde xilinx.kicad_sch` and `sheet:sonde_xilinx.kicad_sch`; this is an
identity finding, not evidence of a visual loss. The [machine receipt](conversion-replay-maintainer-host.json)
retains the exact error, region, levels, input and raw-reply hashes.

Every proof used the default complete level selection, without a loss flag,
acceptance, reference exclusion or tolerance override. The successful Video
proof includes strict copper comparison. It is an own-comparison result;
no native application save, native DRC, independent rendering oracle, release
or exact-head CI result is inferred. Final combined model-0 capture and the
prepared model-1 activation remain pending.

All 958 authoritative board files, terms, original proofs and acceptances remain
byte-identical in this diagnostic phase. No candidate replaces a published
item here. The current root audit still exits 5 with 38 findings: 23 provenance,
12 proof, two licence-text and one family finding. The public tool pin remains
unchanged. Earlier b02, model-0 and L10 reports remain historical measurements.

The external `fenolite-cac-library-current` scratch contains the 12 actual
import/confirmation/proof replies, reviewed plans and copied inputs; its raw
reply hashes are in the machine receipt. The local continuation has no push.
