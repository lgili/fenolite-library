# Four strict conversions on the L10 model 0 cut

Measured on 2026-11-02 with exact clean Fenolite
`695dee0f1bdf2cff066edad0220c63cf064ae0a2` (0.7.0.dev0, CLI v0, model 0), from external library
base `e22897fe934623bd20a965dc5a8e70efc5458810`. All four strict imports now confirm, and every
fresh proof compares levels 1–7 and S equal. **All four full proofs still exit 5 at level 8.**
There are no accepted differences in the fresh candidates.

The [machine-readable receipt](conversion-replay-lote10.json) retains actual per-level results,
remaining differences, warnings, command exits, input/source/raw-reply hashes and unchanged item
snapshots. Earlier [b02](conversion-replay-b02.md) and [dbfd model 0](conversion-replay-model0.md)
reports remain historical measurements of their own sources.

## Source and input checks

The private detached core tree is `88473c0ca98666eeac31e81b70d47b06340d7db7`. Its supplied read-only
source receipt has SHA-256 `24c6e31dd0b9b3352f3af350742125e474cc47ed0fff805475a866a4ce20a778`;
it records 172 model classes, 1225 fields, 40 extension keys and 20 active-v0 schema hashes.
The model/KEEP-field comparison is unchanged. This is a metadata capture, not a native or full-CI proof.
The exact source/tree, clean status and every schema digest were checked before and after commands.
The frozen dev/geo environment was installed offline outside the source checkout.

All 24 cached native files still match the original item records at upstream commit
`97acc80c223d75520c03fc44cab63cd9a3202c42`. No source was fetched again, upgraded or edited.
ECC83's sibling project remains present, while its explicit proof against set contains only the
main project's three files. Every command also checks its scratch input copies remain unchanged.
No third-party CAD or derived conversion file enters core.

## Actual fresh results

| Item | Strict dry import and reviewed confirmation | Full default proof |
|---|---|---|
| ecc83 | Exit 0; 22 files; no unexpressed items | Exit 5; levels 1–7/S equal; one level-8 `render-pixels` finding |
| sonde_xilinx | Exit 0; 28 files; no unexpressed items | Exit 5; levels 1–7/S equal; two level-8 `render-missing` findings |
| video | Exit 0; 117 files; no unexpressed items | Exit 5; levels 1–7/S equal; eight level-8 `render-pixels` findings |
| kit-dev-coldfire-xilinx_5213 | Exit 0; 113 files; no unexpressed items | Exit 5; levels 1–7/S equal; three level-8 `render-pixels` findings |

Each successful import self-checks levels 1–5. The separate `verify-source` commands actually run
all nine default levels, including strict copper comparison, rules/layers, exact geometry, source
drawings and presentation. No level is skipped or excluded, and every fresh acceptance count is zero.
No loss, acceptance, reference-ignore or tolerance override was added. The standard presentation
defaults remain 1000 ppm with 50 µm board and 127 µm schematic grids; these were not enlarged.

The actual dry-run plans were reviewed for scratch-only paths, new targets, file bytes and SHA-256;
confirmation named each exact plan id. Every confirmed output matched its planned hash. The receipt
keeps temporary candidate hashes separate from authoritative item/provenance output digests.

Video's old `/DQ31` versus `/buspci.sch/DQ31` written-drawing guard no longer blocks its conversion.
The Coldfire kit no longer refuses its two layer-table items, and its actual fresh level 6 compares
equal. The new source's bus and technical-layer handling therefore clears those measured blockers
for these exact inputs. Neither observation is an overall passing fidelity proof.

## Remaining presentation findings

| Item | Actual level-8 scope |
|---|---|
| ecc83 | One schematic region: `0/85762` versus `24831/85762` pixels; the summary lists `#PWR05`/`#PWR07` added and `#FLG05` removed |
| sonde_xilinx | Missing `sheet:sonde xilinx.kicad_sch` on one side and `sheet:sonde_xilinx.kicad_sch` on the other |
| video | One located pixel finding on each of `bus_pci`, `esvideo`, `graphic`, `modul`, `muxdata`, `pal-ntsc`, `rams` and `video`; summaries list added `#PWR` references |
| kit-dev-coldfire-xilinx_5213 | One located pixel finding on each of `in_out_conn`, `kit-dev-coldfire-xilinx_5213` and `xilinx`; summaries list added `#PWR` references |

All exact pixel counts, regions and sheet summaries are in the JSON receipt. These change summaries
do not establish whether the remaining difference is text ink, grouping or another renderer behavior.
No cause, harmlessness, hidden-reference exception or passing independent image oracle is inferred.
The filename-identity finding is retained separately from the pixel findings.

## Unchanged existing payloads and policy

All four existing payloads were also copied to scratch and proved against the same source inputs.
Each exits 5: levels 7 and S differ. Levels 1, 2, 4 and 5 equal; level 3 matches historical footprint-name
acceptances and level 8 matches historical presentation acceptances. Level 6 equals except the kit,
which retains its two historical layer acceptances. The receipt labels historical `accepted` states
and counts separately from fresh equality. Routing/unfilled-zone notices remain visible and are not
a native clearance or routing-safety proof.

The actual root audit still exits 5 with 38 findings: 23 provenance errors, 12 proof failures, two
licence-text errors and one family mismatch. No fresh candidate passes every level, so none replaces
an item. All existing item payloads, `item.json`, `PROVENANCE.json`, `LICENSE`, `NOTICE`, accepted
differences, original portable conversion steps, licence table and public tool pin remain unchanged.
No proof report or output-tree digest was repaired by hand.

## Reproduction and proof boundary

Use each unchanged item's recorded `conversion.steps[0].argv` against its hash-checked input tree,
replace its plain `--confirm` with `--dry-run`, review the real plan and confirm into a new temporary
output folder using that local plan id. Then run:

```sh
fenolite verify-source out/design.py --against <recorded-native-project> \
  --provenance out/PROVENANCE.json --timestamp 2026-11-02T00:00:00Z --json
fenolite library audit . --json
```

The 16 targeted phases comprise four dry imports, four reviewed confirmations, four fresh full
proofs and four existing-payload proofs; audit and no-tool capability discovery are separate calls.
All raw replies remain in local validation scratch with their hashes in the receipt. Elapsed seconds
are local observations, not a controlled benchmark. Public `library replay` was not repeated here.

The [issue ledger](../boards/ISSUES.md) records the scoped improvements and remaining failures.
Import/proof evidence remains `INFERRED`. No KiCad/Altium GUI save, native DRC, independent rendering
oracle, exact-head external CI, push, tag, release or publication is claimed. Other demos, the
remaining presentation findings, incomplete item metadata and the native/CI gates stay open.
