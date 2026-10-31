# Fenolite issues found while converting boards

Found on 2026-10-30 while converting the KiCad demos for this library. Nothing here was fixed in the Fenolite
repository; each entry is for the maintainer.

- **Fenolite:** branch `circuits-as-code`, commit `8dab89d61d40a4d1f9044fb284d844839a78d70e`, `fenolite 0.7.0.dev0`,
  `uv sync --all-extras`. No `kicad-cli` was installed, so nothing was checked against KiCad's own DRC.
- **Upstream:** `gitlab.com/kicad/code/kicad` at `97acc80c223d75520c03fc44cab63cd9a3202c42`, folder `demos/`.
- **Commands** run in a work folder holding `upstream/` (the demo folder copied at that commit) and `out/`:

```sh
fenolite import upstream/demos/<demo>/<project>.kicad_pro --to python --out out --licence <SPDX> \
    --source <url> --revision <sha> --timestamp 2026-10-30T00:00:00Z [--allow-lossy] --dry-run --json
fenolite import ... --confirm --plan <plan_id>
fenolite verify-source out/design.py --against upstream/demos/<demo>/<project>.kicad_pro --json
```

## Blocking: no board can be proved

### 1. `verify-source` refuses to build boards that break Fenolite's copper rules

- **Boards:** `cm5_minima`, `tiny_tapeout`, `royalblue54L_feather` (the three first candidates), `openair-max`,
  `multichannel`, `pic_programmer`, `interf_u`.
- **Command:** `fenolite verify-source out/design.py --against upstream/demos/cm5_minima/CM5_MINIMA_3.kicad_pro --json`
  after a successful `import --allow-lossy` (its self-check passed, `equivalence.equivalent: true`).
- **Error:** exit 5, `fidelity.build-failed` ("the build of design.py wrote no file, so no level ran"), every level
  `skipped` with reason `build-failed`. The build's copper guard refuses:

  | board | errors of the copper guard |
  |---|---|
  | cm5_minima | 393 `copper.clearance` (224 `pair-gap:90ohm`, 165 `class:Default`, 4 others), 2 `copper.edge-clearance` |
  | tiny_tapeout | 111 `copper.clearance` (for example 0.199999 mm against 0.2 mm, `class:Default`), 3 `copper.short` |
  | royalblue54L_feather | 12 `copper.edge-clearance`, 12 `copper.hole-in-cutout` (pads of J2 on the edge) |
  | openair-max | 311 `copper.clearance`, 8 `copper.short` (see issue 2) |
  | multichannel | 24 `copper.clearance` (`rule:fenolite_0_min_clearance`) |
  | pic_programmer | 1 `copper.clearance` (`class:POWER`, 0.2496 mm against 0.28 mm) |
  | interf_u | 62 `copper.edge-clearance` (`floor`, 0.254 mm against 0.5 mm) |

- **Expected:** the proof compares the board instead of refusing it. The import's self-check builds with
  `--copper-check warn --schematic skip` (`cli/cmd_import.py`), and `docs/import.md` says that building the code
  later needs `--copper-check warn`, but `verify-source` builds with the default `refuse` (`cmd_verify_source._build`)
  and has no option to change it. Suggested: build with `warn` (the findings stay listed), or a `--copper-check`
  option, or a mode read from the provenance file.

### 2. A pad on no net upstream gets a single-pad `unconnected-(…)` net in the build

- **Boards:** `video` (J4 pad 0), `kit-dev-coldfire-xilinx_5213` (UARTCAN201/202/203 pad 0): a level-2 difference.
  `openair-max` (Q1, Q2 pad 9, the thermal pad of a PQFN-8): 8 false `copper.short` that refuse the build (issue 1).
- **Error:** `verify-source` level 2: `{"kind": "net", "where": "J4-0", "a": "no net", "b": "unconnected-(J4-0-Pad0)"}`
  (`netlist.assignment-differs`). In `openair-max` the drain copper overlaps pad 9, which has no net upstream; the
  build names it `unconnected-(Q1-9-Pad9)` and the copper guard reports a short with `Net-(Q1-D)`.
- **Expected:** a numbered pad with no net upstream stays on no net. The symbol the import draws has one pin per
  pad number (`import.symbol-regenerated`), so the generated schematic gives that pad an unconnected net. Also,
  the import's self-check treats single-pad `unconnected-(…)` nets as no net (it passes), while level 2 of
  `verify-source` does not: the two should agree.

### 3. The copper check may be stricter than KiCad's DRC (to confirm with `kicad-cli pcb drc`)

- **Boards:** `cm5_minima` (224 findings `pair-gap:90ohm`: the differential pairs are 0.1516 to 0.1530 mm apart where
  the net class `90ohm` has `diff_pair_gap` 0.154 mm), `tiny_tapeout` (gaps of 0.199999 mm against 0.2 mm: a 1 nm
  deficit, likely rounding of arcs or coordinates).
- **Expected:** to check whether KiCad's DRC counts a net class's differential-pair gap as a minimum clearance, and
  whether a 1 nm deficit is a finding there. The `cm5_minima` README says the demo was cleaned of DRC errors when it
  entered the KiCad demos. If KiCad accepts these boards, the copper guard should too.

## Losses the import does not report

### 4. The Edge.Cuts stroke width is dropped silently

- **Boards:** every converted board (`ecc83` 0.127 mm, `sonde_xilinx` 0.2 mm, `video` 0.2032 mm,
  `kit-dev-coldfire-xilinx_5213` 0.381 mm; the build writes 0.1 mm).
- **Error:** nothing in `result.unexpressed`; the self-check passes. `verify-source` level 7 then reports each
  outline segment twice as `graphic-missing` (once `a`-only and once `b`-only, with the same `where`), and level 8
  `render-pixels` on `Edge.Cuts`.
- **Expected:** the DSL board outline keeps its width (or the import lists it as unexpressed), and level 7 matches a
  graphic by geometry and reports a width change as one difference with `field: width`.

### 5. The board's user-layer table is neither expressed nor reported

- **Board:** `kit-dev-coldfire-xilinx_5213`.
- **Error:** level 6: 14 `layer-missing` differences. The upstream board has no `Eco1.User`/`Eco2.User`; the DSL board
  writes them, so the ordinals of the courtyard, edge, fabrication and margin layers shift
  (`{"where": "courtyard:16", "a": "F.CrtYd", "b": ""}` and `{"where": "courtyard:18", "a": "", "b": "F.CrtYd"}`).
- **Expected:** the import reports the layer table as unexpressed (or the DSL states it), and level 6 pairs layers
  by name and kind before comparing ordinals.

### 6. A field rotation changes on a bottom-side footprint

- **Board:** `video`, R39 (`B.Cu`, footprint angle 0, Reference at 270°).
- **Error:** level 7 `{"kind": "field-pose", "where": "R39:Reference", "field": "rotation", "a": "270000000", "b": "90000000"}`.
  The part uses the variant footprint `R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_38`. The self-check does not
  compare fields.
- **Expected:** the field keeps 270° through the derive (to the top side) and the build (back to the bottom).

## Proof noise and gaps

### 7. `verify-source` counts the build's own `fenolite.path` property

- **Boards:** every board: one level-7 `field-pose` per footprint (`"where": "R1:fenolite.path", "field": "name", "a": "", "b": "fenolite.path"`).
- **Expected:** the property that the build adds as the lens key is not a difference of the design; it should be
  left out of the comparison instead of needing an accepted entry on every board.

### 8. `--against <project>.kicad_pro` also reads another project of the same folder

- **Board:** `ecc83` (the folder holds `ecc83-pp` and `ecc83-pp_v2`).
- **Error:** with `--against upstream/demos/ecc83/ecc83-pp.kicad_pro`, `fidelity.proof.against` lists the three
  `ecc83-pp_v2.*` files, and level 8 reports `render-missing` for `sheet:ecc83-pp_v2.kicad_sch`.
- **Expected:** a `.kicad_pro` names one project: only its board and its sheet tree are read and recorded.

### 9. Level 7 does not see the teardrops that the import dropped

- **Boards:** `complex_hierarchy` (165 teardrops); `royalblue54L_feather` (263) would be affected too once issue 1
  lets it build.
- **Error:** the import reports `import.item-unexpressed` kind `teardrop`, but `verify-source` level 7 reports no
  zone difference for `complex_hierarchy` (166 zones upstream, 1 in the build).
- **Expected:** a loss that the import reports shows up in the proof (as `zone-missing`, or as excluded items with a
  count), so a board cannot pass while copper is missing. `complex_hierarchy` was kept out of this batch for this
  reason.

### 10. Level S is always skipped, but the library gate wants every level equal or accepted

- **Boards:** every board: level S is `skipped` with `drawn-unavailable` (no drawn-schematic extraction in this
  version). c0279 says every level must be `equal` or `accepted`; c0278 lets a skipped level pass with its reason.
- **Expected:** a decision: either the gate accepts `skipped` with a reason, or boards wait for c0276. The four boards
  of this batch record `"S": "skipped"`.

## To check

### 11. `royalblue54L_feather`: footprint J1 cannot be brought back, J2 lands on the edge

- `import` lists J1 under the kind `footprint` ("one the library derive cannot bring back"), and the build then
  reports the drill of J2-1 crossing the board edge (`copper.hole-in-cutout`). Worth checking whether the outline or
  the derive is wrong, beside the DSL gaps of this board (183 blind/buried vias `via-span`, 263 teardrops).

### 12. A recorded `--confirm --plan <id>` step cannot be replayed in another folder

- A plan id hashes the working folder (`cli/plans.py::plan_id`), so the same import run in another folder gets another
  id, and `--confirm --plan <id>` from `PROVENANCE.json` exits 4 with `FEN-4002` ("no staged plan has the id …").
- What was done: `conversion.steps` record the `--dry-run` and a plain `--confirm`, as in c0279's example; replayed in a
  fresh folder, both give the recorded `outputs_tree` and the same import record for the four boards.
- Expected: c0279's `library replay` runs steps without `--plan` (or the provenance schema says so).

## DSL gaps hit (c0277, reported by the import: not bugs)

| board | unexpressed kinds (count) |
|---|---|
| tiny_tapeout | `duplicate-ref` 131 (STITCH* via footprints), `text` 167, `net-tie` 9, `dnp` 11, `footprint-ref` 7, `dimension` 6, `group` 3, `text-layer` 1, `outline` 1 (the board outline is closed by the Edge.Cuts of footprint J15, a USB connector: KiCad accepts that, the import does not) |
| royalblue54L_feather | `teardrop` 263, `via-span` 183 (every via), `text` 71, `dnp` 22, `zone-outline` 2, `net-tie` 1, `footprint` 1 |
| cm5_minima | `text` 18, `generated` 15, `drawing` 7, `drawing-layer` 4, `group` 4, `zone-setting` 4, `dnp` 2, `pad-net-conflict` 2 (J502.MP, J503.MP), `footprint-ref` 1 |
| openair-max | `drawing` 16, `dnp` 11, `footprint-ref` 6, `copper-drawing` 2, `generated` 2, `net-tie` 2, `group` 1, `text` 1 |
| complex_hierarchy | `teardrop` 165, `text-layer` 2 |
| microwave | `duplicate-ref` 3 (three of its four footprints are named `POLY`) |
| multichannel | `group` 4, `rule-area-name` 4, `text` 1 |
| interf_u | `text-layer` 6, `dimension` 2, `text` 2 |
| pic_programmer | `text-layer` 19 |
| sonde_xilinx | `text-layer` 8, `dimension` 1 |
| video | `dimension` 2, `text-layer` 1 |
| kit-dev-coldfire-xilinx_5213 | `text-layer` 5, `stackup-field` 2 |
| ecc83 | none |

## Status on 2026-10-31

- **Issue 1 fixed** in Fenolite (branch `cac/c0277-dsl-gaps`): `verify-source` builds with the copper guard in
  `warn`, so the proof compares boards that break Fenolite's copper rules.
- **Lossy kinds** of the issues above (via spans, teardrops, copper texts, dimensions, groups, user layers, board-only
  footprints, outlines closed by a footprint) are expressed by change c0277: all 13 demos import with nothing left
  out.

### 13. Courtyards missing from the build of `kit-dev-coldfire-xilinx_5213` (fixed)

- **Command:** `fenolite verify-source out/design.py --against upstream/demos/kit-dev-coldfire-xilinx_5213/kit-dev-coldfire-xilinx_5213.kicad_pro`
- **Error:** level 6, 14 `layer-missing` differences such as `{"where": "courtyard:16", "a": "F.CrtYd", "b": ""}`.
- **Expected:** the courtyards of the upstream footprints are in the built board.
- **Cause and fix (2026-10-31):** no courtyard was missing. Level 6 matched layers by their row in the table; the
  upstream table leaves out `Eco1.User` and `Eco2.User`, which the build writes, so every later row moved. The
  comparison now matches layers by kind and name (Fenolite branch `cac/c0277-dsl-gaps`).

### 14. A repeated property name is lost

- **Board:** `openair-max`, footprint `D1`: the hidden property `Description_1` (KiCad's name for a second
  `Description`) is not in the build; a component holds one property per name. Accepted in the proof with this
  reason.
