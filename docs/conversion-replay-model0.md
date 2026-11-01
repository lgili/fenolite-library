# Four-board replay against the frozen model 0 cut

On 2026-11-01 the four recorded conversions were rerun using clean, detached Fenolite
`dbfd6fc36e18300c4a9aef1983f7130fea4e3b71` (0.7.0.dev0, CLI v0, model 0). The external library
base is `4551805c42547d89f869cdfb2b307a6d9122017f`. This continues the historical
[b02 review](conversion-replay-b02.md); it does not replace that measurement.

The [diagnostic receipt](conversion-replay-model0.json) records all 24 native input SHA-256 values,
the exact core tree and source0 receipt/schema hashes, actual exit codes, every level's status,
difference counts, raw-reply hashes and unchanged item snapshots. The source0 receipt SHA-256 is
`c389d3071f4b50263131fc6b2a2114ac8186196b47a93eebbeb537d837f41d14`.
Core and schema checks ran before and after every command. The private frozen dev/geo environment
and all temporary outputs were outside both repository payload trees. No core source was edited.

Input bytes were reused from the cache and match upstream commit
`97acc80c223d75520c03fc44cab63cd9a3202c42` as recorded by each item. This is a byte check, not a
fresh network fetch. The six ECC83 files include the sibling project; explicit selection still uses
only the main project's three files in the proof's against set.

## Actual fresh results

| Item | Strict import | Fresh full proof |
|---|---|---|
| ecc83 | Dry run and reviewed confirmation exit 0; 22 files, no unexpressed items | Exit 5: levels 1–7 and S equal; one level-8 `render-pixels` difference |
| sonde_xilinx | Dry run and reviewed confirmation exit 0; 28 files, no unexpressed items | Exit 5: levels 1–7 and S equal; two level-8 `render-missing` differences |
| video | Exit 5, FEN-5001 / `import.unequal`; no plan | Not run: the strict import produced no confirmed design |
| kit-dev-coldfire-xilinx_5213 | Exit 7, FEN-7001 / `import.item-unexpressed`: two `layer-table` items; no plan | Not run: the strict import produced no confirmed design |

Both successful imports self-check only levels 1–5. The subsequent `verify-source` commands really
ran all default levels 1–7, S and 8 with zero accepted differences; they are not passing proofs.
ECC83's level-8 comparison reports pixels `0/85762` versus `24831/85762` in the schematic region
`158877000,76454000–185166000,102616000`. Its change summary names `#PWR05` and `#PWR07` added
and `#FLG05` removed. Sonde reports the source sheet `sonde xilinx.kicad_sch` missing on one side
and generated `sonde_xilinx.kicad_sch` missing on the other. Level S compares equal for both;
these presentation findings are retained rather than waived or inferred to be harmless.

Video reaches the written-schematic connectivity guard. The actual error says `RR1-3` is on
`/DQ31` in code and `/buspci.sch/DQ31` in the drawing, a split, with 537 more findings. Nothing is
written. The Coldfire kit now explicitly refuses the two layer-table items instead of reaching the
old unmapped-power-symbol error. No lossy flag was added to proceed past that refusal.

For ECC83 and sonde, the initial dry run reported `plan.not-staged` because the default cache was
unwritable. The documented absolute `FENOLITE_STATE_DIR` selected a writable private state folder.
Confirmation named the original reviewed plan id, and every resulting file matched its planned
SHA-256. These local plan ids are diagnostic receipts, not new portable provenance steps.

## Existing payloads and policy

All four unchanged existing payloads were also copied to scratch and proved against the original
inputs. Each exits 5: levels 7 and S differ. Levels 1, 2, 4 and 5 compare equal. Level 3 remains
`accepted` under historical footprint-name dispositions; level 8 remains `accepted` under historical
presentation dispositions. Level 6 is equal except the Coldfire kit, which uses two historical layer
acceptances. The JSON keeps these accepted counts distinct from equality and from the fresh candidates.
Routing notices, including unjudged/unfilled zones, remain visible; comparison equality is not a
native DRC or routing-safety claim.

The root audit exits 5 with 38 findings: 23 provenance errors, 12 proof failures, two licence-text
errors and one family mismatch. These failures were measured again, not copied as a passing baseline.

No fresh candidate satisfies the library's full proof requirement without new dispositions, so none
replaces an item. Every existing payload, `item.json`, `PROVENANCE.json`, `LICENSE`, `NOTICE`,
accepted difference and conversion step remains byte-identical to the library base. Temporary
candidate hashes are diagnostic only; no output-tree digest or recorded proof was fabricated.
The public tool pin is unchanged. No public library-replay command was rerun in this continuation;
the four actual imports and available proofs are the measured scope.

## Historical issues and remaining gates

The [issue ledger](../boards/ISSUES.md) retains the original thirteen-demo scope. On these four boards:

| Original issue | Measured scope on the frozen cut |
|---|---|
| 1, copper guard | Existing payloads reach comparison with the copy's guard in `warn`. Successful fresh imports/proofs also reach comparison; this is not clearance validation. |
| 2, artificial single-pad net | Level 2 equals for all four existing payloads and both fresh candidates. No new native DRC claim. |
| 3, clearance versus KiCad DRC | No native DRC run and the originally affected boards are outside this replay. Open. |
| 4, outline stroke | Fresh ECC83/sonde level 7 equals. Existing ECC83, sonde and kit payloads each have four `graphic-field` differences; video has 22. Video/kit have no fresh proof. |
| 5, user-layer table | Fresh kit import explicitly refuses two layer-table items; preservation remains unproved. |
| 6, bottom field rotation | Existing video's historical presentation acceptance remains; no fresh video proof. |
| 7, `fenolite.path` noise | No raw or accepted `fenolite.path` difference in these existing-payload or fresh replies. |
| 8, project selection | ECC83 proofs select only `ecc83-pp`'s three files although its sibling is present. |
| 9, teardrops | The originally affected boards were not rerun. Open here. |
| 10, S skipped | S actually runs for all four existing payloads and differs; both fresh candidates compare S equal. No missing-S acceptance. |
| 11, royalblue derive/edge | That board was not rerun. Open here. |
| 12, portable replay | Reviewed local confirmation works for two imports; public library replay was not rerun. No new stored plan ids in provenance. |
| 13, courtyards | No new missing-courtyard inference; the kit still has no fresh proof. |
| 14, repeated property name | openair-max was not rerun. Open here. |

Reproduce using each unchanged item's original `conversion.steps[0].argv`, replacing its plain
`--confirm` with `--dry-run`. Review only a successful plan, then confirm that plan in a separate
temporary output folder. Run `verify-source out/design.py --against <original-project> --provenance
out/PROVENANCE.json --timestamp 2026-11-01T00:00:00Z --json` without acceptance or level filters.
The diagnostic receipt's original recipes supply exact public URLs and relative project paths.

Actual CLI evidence labels are retained: the successful imports/proofs are `INFERRED`, while the
Coldfire import refusal is `UNVERIFIED`. Elapsed seconds are local observations, not a controlled
benchmark. No native KiCad/Altium save, DRC, GUI review,
independent rendering oracle, exact-head external CI, push, tag, release or publication was performed.
Those gates and the unresolved import/presentation/provenance findings remain open.
