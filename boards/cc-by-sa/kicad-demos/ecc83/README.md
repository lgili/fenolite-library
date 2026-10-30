# ECC83 valve amplifier (KiCad demo ecc83-pp)

Two-layer through-hole valve amplifier board (project ecc83-pp) from the KiCad demos, converted to Fenolite code: `design.py` (parts, nets, rules, stack-up, outline, zones, placements), `copper.py` (tracks and vias as tables) and the board's own footprints in `lib/`.

- **Upstream:** [`demos/ecc83`](https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/ecc83) of the KiCad source repository, commit `97acc80c223d`.
- **Licence:** CC BY-SA 4.0 (`LICENSE`), as stated for all KiCad demos in the repository's `LICENSE.README`. This item stays under CC BY-SA 4.0; see `NOTICE`.
- **Size:** 15 parts, 9 nets, 59 tracks, 0 vias, 1 zone(s); modules: racine.
- **Converted:** 2026-10-30 with Fenolite 0.7.0.dev0 (commit `8dab89d61d40`), `fenolite import --to python --allow-lossy`.

## Left out by the conversion

- nothing: the DSL expresses every item of the board.
- the drawn schematic: the build generates its own schematic until change c0276 imports drawings.

## Fidelity proof (`fenolite verify-source`, 2026-10-30)

Result: **pass-with-accepted**, level S skipped. Each accepted difference is listed with its reason in `PROVENANCE.json` (`fidelity.accepted`).

| level | what | status | accepted entries |
|---|---|---|---|
| 1 | components | equal |  |
| 2 | netlist | equal |  |
| 3 | footprints and pads | accepted | 1 |
| 4 | placement | equal |  |
| 5 | routing (strict, item by item) | equal |  |
| 6 | rules and stack-up | equal |  |
| 7 | exact geometry | accepted | 5 |
| 8 | presentation (rendered layers and sheets) | accepted | 2 |
| S | drawn schematic | skipped |  |

Level S is skipped (`drawn-unavailable`): this Fenolite version has no drawn-schematic extraction.

## Reproduce

In a folder holding `upstream/` (the KiCad repository at the commit above):

```sh
fenolite import upstream/demos/ecc83/ecc83-pp.kicad_pro --to python --out out --licence CC-BY-SA-4.0 --source https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/ecc83 --revision 97acc80c223d75520c03fc44cab63cd9a3202c42 --timestamp 2026-10-30T00:00:00Z --allow-lossy --dry-run
fenolite import ... --confirm --plan <plan_id>
fenolite verify-source out/design.py --against upstream/demos/ecc83/ecc83-pp.kicad_pro --provenance <this folder>/PROVENANCE.json
```

Converted from the open-source design `ecc83` of the KiCad demos (https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/ecc83), licence CC-BY-SA-4.0. Not endorsed by the authors.
