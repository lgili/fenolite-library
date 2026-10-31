# Coldfire MCF5213 development kit (KiCad demo)

Four-layer development board for a Coldfire MCF5213 with a Xilinx CPLD from the KiCad demos, converted to Fenolite code: `design.py`, `copper.py` (tracks, arcs and vias as tables) and the board's own footprints in `lib/`.

- **Upstream:** [`demos/kit-dev-coldfire-xilinx_5213`](https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/kit-dev-coldfire-xilinx_5213) of the KiCad source repository, commit `97acc80c223d`.
- **Licence:** CC-BY-SA-4.0 (`LICENSE`); see `NOTICE`.
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
| 6 | accepted |
| 7 | accepted |
| 8 | accepted |
| S | skipped |

## Reproduce

In a folder holding `upstream/` (the KiCad repository at the commit above):

```sh
fenolite import upstream/demos/kit-dev-coldfire-xilinx_5213/kit-dev-coldfire-xilinx_5213.kicad_pro --to python --out out --licence CC-BY-SA-4.0 --source https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/kit-dev-coldfire-xilinx_5213 --revision 97acc80c223d75520c03fc44cab63cd9a3202c42 --timestamp 2026-10-31T00:00:00Z --confirm
fenolite verify-source out/design.py --against "upstream/demos/kit-dev-coldfire-xilinx_5213/kit-dev-coldfire-xilinx_5213.kicad_pro" --provenance <this folder>/PROVENANCE.json
```
