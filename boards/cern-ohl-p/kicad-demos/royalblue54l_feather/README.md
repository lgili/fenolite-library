# RoyalBlue54L Feather (KiCad demo)

Eight-layer Feather-format nRF54L board by Lord's Boards from the KiCad demos, converted to Fenolite code: `design.py`, `copper.py` (tracks, arcs and vias as tables) and the board's own footprints in `lib/`.

- **Upstream:** [`demos/royalblue54L_feather`](https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/royalblue54L_feather) of the KiCad source repository, commit `97acc80c223d`.
- **Licence:** CERN-OHL-P-2.0 (`LICENSE`); see `NOTICE`.
- **Converted:** 2026-10-31 with Fenolite 0.7.0.dev0 (commit `628954b73062`), `fenolite import --to python`, with no item left out.

## Fidelity proof (`fenolite verify-source`)

Result: **pass-with-accepted**. Each accepted difference is listed with its reason in `PROVENANCE.json` (`fidelity.accepted`).

| level | status |
|---|---|
| 1 | equal |
| 2 | equal |
| 3 | accepted |
| 4 | equal |
| 5 | equal |
| 6 | equal |
| 7 | accepted |
| 8 | accepted |
| S | skipped |

## Reproduce

In a folder holding `upstream/` (the KiCad repository at the commit above):

```sh
fenolite import upstream/demos/royalblue54L_feather/RoyalBlue54L-Feather.kicad_pro --to python --out out --licence CERN-OHL-P-2.0 --source https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/royalblue54L_feather --revision 97acc80c223d75520c03fc44cab63cd9a3202c42 --timestamp 2026-10-31T00:00:00Z --confirm
fenolite verify-source out/design.py --against "upstream/demos/royalblue54L_feather/RoyalBlue54L-Feather.kicad_pro" --provenance <this folder>/PROVENANCE.json
```
