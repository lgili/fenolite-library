# Design

Entry 2026-11-04: library worktree `claude/library-growth-af26a4` at c58cdf2 (v1.0.0 preparation of
`cac/library-completion`). Core: the library's pinned Fenolite commit e7673c81, extracted read-only with
`git archive` into a scratch folder and run with `uv`; the Fenolite repository is not edited.

## 1. Item shape

Each authored footprint is one item folder `footprints/cc0/<Namespace>/<name>/`:

- `package.toml`: a `fenolite.package.v0` record with `generator = "explicit"`, holding the pads, graphics
  and component bodies that Fenolite's c0260 family generator (`chip`, `molded`, `gullwing`, …) draws from
  the row's toleranced dimensions, plus the stored dimension keys (`pins`, `pitch`, `body`, `span`, `lead`)
  and `family`. The pinned core's record parser (the one `library audit` and `library check` use) reads only
  explicit package records: a c0260 family record fails the audit with `generate: unknown key` (gap G-1
  below). So the expander runs the generator in-process and writes its output as the explicit record; the
  complete family record, the generator stamp (`gullwing/1 manufacturer drawing/1; land: …`) and the
  generator's findings are kept in `PROVENANCE.json` `generation`.
- `generated/<Namespace>.pretty/<name>.kicad_mod`: exactly what the CI `regenerate` job writes from an
  explicit record (`write_footprint(prepare_authored_definition(footprint_def(record)), target=9)`), compared
  byte for byte.
- `generated/<Namespace>.3dshapes/<name>.step` when the record has bodies: Fenolite's own extrusion of the
  record's bodies (`backends.step.write_bodies`), not a vendor model. No Altium PcbLib is committed (the
  explicit-record path of the CI job does not plan one; a per-item PcbLib would cost 96 KiB each).
- `item.json`, `LICENSE` (the CC0-1.0 legal code whose normalised digest licences.toml already accepts,
  `0dd25be0…`, so no licence review is claimed), `NOTICE`, `PROVENANCE.json` (`origin = "authored"`,
  `upstream = null`, `sources` = the D-ids, and a `datasheets` member listing each document's URL, title,
  revision and date and the table rows used).

Each authored symbol is one item folder `symbols/cc0/<Namespace>/<name>/` with a `fenolite.pins.v0`
record and `generated/pins.kicad_sym`: functional symbols (R, C, L, diodes, transistors, op-amp, regulator,
connectors) place their pins and draw lines explicitly on the 2.54 mm grid (`symbols_table.py`). MCU-style
multi-unit symbols are pin tables of real devices laid out by the c0261 generator; they come in M3 with the
devices that need them.

Names follow the core's naming rule (`docs/formats/library/naming.md`). Generic names
(`CHIP0603_B1.6x0.8`) are used where the body nominal is the datasheet's: the generator refuses a name that
disagrees with the record's numbers (`package.name-mismatch`). Packages read from one manufacturer's drawing
use the rule's manufacturer form (`SOIC8_Diodes`, `SOT223_Diodes`), which makes no generic size claim.
Imperial and metric chip codes are both given in the title, summary and tags (`0603 (1608 metric)`).

Namespaces group items like a KiCad library: `FenoliteResistorSMD`, `FenoliteCapacitorSMD`,
`FenoliteInductorSMD`, `FenoliteDiodeSMD`, `FenolitePackageSOT`, `FenolitePackageSO`,
`FenolitePackageDFN_QFN`, `FenolitePackageQFP`, `FenolitePackageBGA`, `FenolitePackageTO`,
`FenolitePackageDIP`, `FenoliteResistorTHT`, `FenoliteCapacitorTHT`, `FenoliteConnectorHeader`,
`FenoliteConnectorSocket`, `FenoliteTerminalBlock`, `FenoliteConnectorUSB`, `FenoliteCrystal` and
`FenoliteSymbols`.

## 2. Families and order of work

Ordered by how many real boards they cover:

| batch | family | generator | milestone |
|---|---|---|---|
| 1 | chip R, C, L, ferrite bead (01005 to 2512; capacitors to 3640) | `chip` | M1 |
| 2 | SOD-123/-123F/-323/-323F/-523, SMA/SMB/SMC, MiniMELF, PowerDI-123 | `molded` | M1 |
| 3 | SOT-23/-23-5/-23-6, SOT-223, SOT-89, SOT-323/-363, SOT-523, SOT-563 | `gullwing` (`sides`, `tab`) | M1 |
| 4 | SOIC, SSOP, TSSOP, MSOP (dual rows) | `gullwing` | M1 |
| 5 | generic symbols per device class | pins (explicit, generated) | M1 |
| 6 | DFN/SON, QFN with exposed pad, LQFP/TQFP | `nolead`, `gullwing` quad | M2 |
| 7 | TO-220, TO-247, TO-92, TO-252 (DPAK), TO-263 (D2PAK) | `to` | M2 |
| 8 | DIP 4 to 40, axial and radial through-hole | `dip`; axial/radial: gap | M2 |
| 9 | pin headers and sockets, 1.27/2.00/2.54 mm, 1 to 40 pins, 1 and 2 rows | `header` | M2 |
| 10 | BGA grid families | `grid` | M3 |
| 11 | terminal blocks, USB, crystals and oscillators | `connector`, `nolead`; gaps | M3 |
| 12 | generic devices binding symbol and footprint | device records | M3 |
| 13 | imported items from checked upstream libraries | `library seed` / import | M4 |

Families with no c0260 generator (axial and radial through-hole parts, USB receptacles with shell
tabs, 4-pad crystal packages with unequal pads) are reported as generator proposals for the core. Until a
generator exists they are not drawn pad by pad here.

## 3. Sources and their licences

Package dimensions are facts. Each document is read for its numbers only; no drawing, CAD file or 3D model
is copied. Every document is registered as a D-id in `sources.toml` (reserved block D-0390 to D-0599, so
the other sessions' D-ids do not collide) and listed in each item's `PROVENANCE.json` `datasheets` member
with URL, title, revision and date.

| source | used for | licence of the document | status |
|---|---|---|---|
| YAGEO RC_L chip resistor data sheet, version 14 (2025-11-14) | chip resistor bodies 0075 to 2512 | YAGEO copyright, facts only | read 2026-11-04 |
| Vishay D/CRCW e3, document 20035, revision 14-Apr-2026 | cross-check of resistor bodies | Vishay copyright, facts only | read 2026-11-04 |
| Vishay VJ Commercial Series MLCC, document 45199, revision 08-May-2026 | chip capacitor bodies 0402 to 3640 | Vishay copyright, facts only | read 2026-11-04 |
| Vishay ILBB-0603 ferrite bead data sheet | ferrite bead 0603 | Vishay copyright, facts only | read 2026-11-04 |
| Diodes Incorporated package files (SOD, SOT, SO, TSSOP, MSOP, SMA/SMB/SMC, MiniMELF) | outline dimensions and suggested pad layouts | Diodes copyright, facts only | read 2026-11-04 |
| Texas Instruments, onsemi and Microchip package drawings | QFN/DFN, QFP, TO, DIP, BGA | manufacturer copyright, facts only | M2/M3 |
| Würth Elektronik header, socket and terminal block data sheets | headers, sockets, terminal blocks | manufacturer copyright, facts only | M2/M3 |
| LibrePCB libraries | imported items | per repository (CC0-1.0 for LibrePCB_Base) | each repository checked before import |
| SparkFun, Adafruit, Digi-Key and other open libraries | imported items | to be checked per repository | verdict register; unclear ones left out |

A source whose licence is unclear is left out and listed for the maintainer. KiCad's official libraries and
the platforms POLICY.md names are never read for items.

## 4. Proof of every item

A batch enters only when every item in it:

1. **Reads back**: `fenolite library check <item> --json` parses the record and the generated
   `.kicad_mod` / `.kicad_sym`, runs the library rules (courtyard, pad clearance, pin-1 marker, sources)
   and exits 0 with no error finding.
2. **Regenerates**: `fenolite library generate package.toml --out generated --dry-run --json` (or
   `library symbol`) plans files whose SHA-256 equal the committed outputs, as the CI `regenerate` job does.
3. **Renders**: the footprint review sheet that `library check` writes renders without error, and the
   footprint is placed in a scratch design built with `fenolite build` once per batch.
4. **Passes the policy**: `fenolite library audit . --item <item> --json` exits 0 (licence family, digest,
   provenance, sources, notice).

Batch proofs run the same core code through its Python API in one process (one interpreter start per batch,
not per item) and then the CLI on a sample; heavy jobs go through `fenolite-heavy`. A failing item is fixed
or left out, never waived.

## 5. Size targets

| milestone | content | items (footprints + symbols) |
|---|---|---|
| M1 | batches 1 to 5 | at least 120 |
| M2 | batches 6 to 9 (headers and sockets alone give about 300) | at least 700 |
| M3 | batches 10 to 12 | at least 1500 |
| M4 | imports from checked upstream libraries | at least 5000 |

## 6. Shared files

`sources.toml`, `library.toml`, `CHANGELOG.md` and `licences.toml` belong to the v1.0.0 preparation too.
Edits to them are small, append-only and in separate commits, so they rebase on `cac/library-completion`.
No new licence text digest is added: authored items use the already accepted CC0 text.

## Gaps found in the core (proposals; the core is not edited here)

- G-1: `catalog.records.parse_record` (audit, check) refuses the c0260 family keys (`generate`, `terminal`,
  `arrangement`, `polarity`, `side`, `tab`, `ep`, …), while the CI `regenerate` job and `library generate`
  accept family records. Proposal: let the record parser accept a c0260 family record (or `generator =
  "<family>"` with its keys) so items can keep the family record as their single source.
- G-2: the gullwing generator has no exposed pad (SO-8EP, MSOP-EP, TSSOP-EP, HSOP); the molded generator
  refuses a span equal to the body (MiniMELF / MELF cylinders); no generator for unequal two-pad packages
  (PowerDI-123, SOD-123FL with a large pad), SOT-89 (centre tab on the lead side), axial and radial
  through-hole parts, USB receptacles with shell tabs, or 4-pad crystal packages.
- G-3: a package read from one drawing with an unusual nominal pitch (Diodes SOT23: D typ 0.915) cannot be
  placed on the JEDEC 0.95 mm pitch without a second source; SOT-23-3 waits for one.

## Decisions

- 2026-11-04: authored items use the CC0 legal-code text already accepted in licences.toml (digest
  0dd25be0…), so no licence review entry is fabricated.
- 2026-11-04: lands come from the manufacturer's suggested pad layout when the document gives one
  (`[land]`, the record keeps `evidence = "INFERRED"` since no board proof exists); otherwise from the core's
  calculator table `lands/1` (INFERRED).
- 2026-11-04: items carry explicit records generated by the c0260 generators (gap G-1), the KiCad footprint
  and Fenolite's STEP body; no per-item PcbLib.
- 2026-11-04: D-ids registered only for documents an item uses (D-0390 to D-0422 with gaps); documents read
  but not used (MiniMELF, PowerDI-123, SOT23, SOT89, SOT523, SO-8EP, TSSOP-16) stay unregistered.
