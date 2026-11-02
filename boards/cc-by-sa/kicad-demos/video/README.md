# Video board (KiCad demo video)

Four-layer video board from the KiCad demos, converted to Fenolite code: `design.py`, `copper.py` (tracks, arcs and vias as tables) and the board's own footprints in `lib/`.

- **Upstream:** [`demos/video`](https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/video) of the KiCad source repository, commit `97acc80c223d`.
- **Licence:** CC-BY-SA-4.0 (`LICENSE`); see `NOTICE`.
- **Originally converted:** 2026-10-31 with Fenolite 0.7.0.dev0 (commit `628954b73062`), `fenolite import --to python`, with no item left out.

## Fidelity proof (`fenolite verify-source`)

Item version **1.0.1**, reconverted 2026-11-02 on signed core `de6c6f2f4dd53cdda45b4119f63822b5bd3ea6eb`.
The actual generated proof reports **all nine levels equal**, with no accepted
or skipped difference. The original licence, attribution and notices remain;
the earlier dated conversion notice is preserved in NOTICE. This is an own
comparison proof, with no new native application or routing-safety claim.

| level | status |
| --- | --- |
| 1 | equal |
| 2 | equal |
| 3 | equal |
| 4 | equal |
| 5 | equal |
| 6 | equal |
| 7 | equal |
| S | equal |
| 8 | equal |

## Reproduce

In a folder holding `upstream/` (the KiCad repository at the commit above):

```sh
fenolite import upstream/demos/video/video.kicad_pro --to python --out out --licence CC-BY-SA-4.0 --source https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/video --revision 97acc80c223d75520c03fc44cab63cd9a3202c42 --timestamp 2026-10-31T00:00:00Z --confirm
fenolite verify-source out/design.py --against "upstream/demos/video/video.kicad_pro" --provenance <this folder>/PROVENANCE.json
```
