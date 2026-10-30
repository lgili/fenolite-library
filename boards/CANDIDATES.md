# Board candidates

Inventory of public boards considered for `boards/`, made on 2026-10-30. Nothing listed here is copied into this
repository unless it appears under `boards/<family>/` with its `LICENSE`, `NOTICE` and `PROVENANCE.json`.

- **licence**: an SPDX id, read from the licence file at the pinned commit (not from a hosting label or a README
  alone).
- **format**: from the `.kicad_pcb` header (`version`, `generator_version`). Fenolite reads KiCad 8 to 10 directly;
  older files need `kicad-cli pcb upgrade` (KiCad 10) first, which the import does on a copy.
- **Cu / parts**: copper layers and footprints counted in the board file.
- **in?**: whether the licence is on the allow-list of `../POLICY.md`. The last column says whether the board was
  converted in this batch, and why not. Blocking Fenolite problems are numbered as in [`ISSUES.md`](ISSUES.md).

## KiCad demos

Repository `https://gitlab.com/kicad/code/kicad`, folder `demos/`, commit
`97acc80c223d75520c03fc44cab63cd9a3202c42` (master on 2026-10-30) for every row. `K` below stands for
`https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos`.

| project | URL | commit | licence | licence text | format | Cu | parts | in? | status, why |
|---|---|---|---|---|---|---|---|---|---|
| tiny_tapeout (TinyTapeout 4+ demo board, Pat Deegan) | [K/tiny_tapeout](https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/tiny_tapeout) | `97acc80c` | Apache-2.0 | `demos/tiny_tapeout/LICENSE.txt` (Apache 2.0 terms, no appendix); title block "Licensed under Apache 2.0", "(C) 2023 Pat Deegan" | KiCad 9.0 (`20241229`) | 4 | 309 | **in** | not converted: proof blocked (issue 1: 111 clearances, 3 shorts); 336 items unexpressed, including the board outline (closed by footprint J15's Edge.Cuts) and 131 stitching footprints |
| royalblue54L_feather (Lord's Boards) | [K/royalblue54L_feather](https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/royalblue54L_feather) | `97acc80c` | CERN-OHL-P-2.0 | `demos/royalblue54L_feather/LICENSE`; README "released under CERN-OHL-V2-P" | KiCad 9.0 (`20241229`) | 8 | 71 | **in** | not converted: proof blocked (issue 1); 543 items unexpressed: all 183 vias (blind/buried, `via-span`), 263 teardrops, 71 texts, footprint J1 (issue 11) |
| cm5_minima (CM5 MINIMA rev 3, Pierluigi Colangeli) | [K/cm5_minima](https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/cm5_minima) | `97acc80c` | CERN-OHL-S-2.0 | `demos/cm5_minima/LICENSE.txt` | KiCad 10 development (`20250513`, 9.99) | 6 | 112 | **in** | not converted: proof blocked (issues 1 and 3: 393 copper findings); the import passes with 57 items unexpressed. To review before entry: 8 footprints of `CM5IO.pretty` have EasyEDA-style names and EasyEDA 3D model paths (possibly made from the EasyEDA/LCSC library; POLICY, "never accepted") |
| ecc83 (project `ecc83-pp`) | [K/ecc83](https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/ecc83) | `97acc80c` | CC-BY-SA-4.0 | no file in the folder; repository `LICENSE.README`: "Licensed under CC BY-SA 4.0: All the demo files provided in demos/*"; text `LICENSE.CC-BY-SA-4.0` | KiCad 9.0 (`20241229`) | 2 | 15 | **in** | **converted**: `cc-by-sa/kicad-demos/ecc83`; lossless import; proof pass-with-accepted |
| sonde xilinx | [K/sonde xilinx](https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/sonde%20xilinx) | `97acc80c` | CC-BY-SA-4.0 | as ecc83 | KiCad 9.0 (`20241229`) | 2 | 25 | **in** | **converted**: `cc-by-sa/kicad-demos/sonde_xilinx`; 9 items left out (8 copper texts, 1 dimension); proof pass-with-accepted |
| video | [K/video](https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/video) | `97acc80c` | CC-BY-SA-4.0 | as ecc83 | KiCad 9.0 (`20241229`) | 4 | 189 | **in** | **converted**: `cc-by-sa/kicad-demos/video`; 3 items left out (2 dimensions, 1 copper text); proof pass-with-accepted |
| kit-dev-coldfire-xilinx_5213 | [K/kit-dev-coldfire-xilinx_5213](https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/kit-dev-coldfire-xilinx_5213) | `97acc80c` | CC-BY-SA-4.0 | as ecc83 | KiCad 9.0 (`20241229`) | 4 | 160 | **in** | **converted**: `cc-by-sa/kicad-demos/kit-dev-coldfire-xilinx_5213`; 7 items left out (5 copper texts, silkscreen material); proof pass-with-accepted |
| complex_hierarchy | [K/complex_hierarchy](https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/complex_hierarchy) | `97acc80c` | CC-BY-SA-4.0 | as ecc83 | KiCad 9.0 (`20241229`) | 2 | 68 | **in** | not converted: the import drops 165 teardrops that the proof does not see (issue 9) |
| interf_u | [K/interf_u](https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/interf_u) | `97acc80c` | CC-BY-SA-4.0 | as ecc83 | KiCad 9.0 (`20241229`) | 2 | 25 | **in** | not converted: proof blocked (issue 1: 62 edge clearances) |
| multichannel (`multichannel_mixer`) | [K/multichannel](https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/multichannel) | `97acc80c` | CC-BY-SA-4.0 | as ecc83 | KiCad 9.0 (`20241229`); the folder also holds an unrouted copy (`20241030`, 8.99) | 2 | 114 | **in** | not converted: proof blocked (issue 1: 24 clearances) |
| pic_programmer | [K/pic_programmer](https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/pic_programmer) | `97acc80c` | CC-BY-SA-4.0 | as ecc83 | KiCad 10.0 (`20260206`) | 2 | 63 | **in** | not converted: proof blocked (issue 1: 1 clearance); 19 copper texts unexpressed |
| microwave | [K/microwave](https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/microwave) | `97acc80c` | CC-BY-SA-4.0 | as ecc83 | KiCad 9.0 (`20241229`) | 2 | 4 | **in** | not converted: three of its four footprints share the reference `POLY` and are dropped (`duplicate-ref`) |
| openair-max (Open Air Max, AirGradient) | [K/openair-max](https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/openair-max) | `97acc80c` | CC-BY-SA-4.0 | `demos/openair-max/LICENSE.txt` (CC BY-SA 4.0 legal code); schematic comment "CC-BY-SA" | KiCad 9.0 (`20241229`) | 4 | 210 | **in, on hold** | not converted: 196 footprints are `easyeda2kicad:` footprints (converted from the EasyEDA/LCSC library), which POLICY's platform rule asks to review first; also blocked by issues 1 and 2 |
| jetson-agx-thor-baseboard (Antmicro) | [K/jetson-agx-thor-baseboard](https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/jetson-agx-thor-baseboard) | `97acc80c` | Apache-2.0 | `demos/jetson-agx-thor-baseboard/LICENSE`; README "Copyright (c) 2025-2026 Antmicro", "published under the Apache-2.0 license" | KiCad 9.0 (`20241229`) | 10 | 1 125 | **in** | later: very large (82 MB board, 19 835 tracks, 3 235 vias) |
| vme-wren (VME White Rabbit node, CERN BE-CEM) | [K/vme-wren](https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/vme-wren) | `97acc80c` | CC-BY-SA-4.0 by `LICENSE.README`; the CERN project's own CERN-OHL variant is to be confirmed upstream | no file in the folder; worksheet `cern-ohl-left.kicad_wks` | KiCad 9.0 (`20241229`) | 12 | 1 508 | **in** | later: very large (68 MB board); confirm the upstream licence first |
| stickhub | [K/stickhub](https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/stickhub) | `97acc80c` | CC-BY-NC-SA-4.0 with a commercial-use exemption | `demos/stickhub/LICENSE.md` | KiCad 10 development (`20250907`) | 2 | 94 | **no** | non-commercial licence |
| constraints | [K/constraints](https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/constraints) | `97acc80c` | CC-BY-SA-4.0 | as ecc83 | KiCad 10 development (`20260624`) | 2 | 0 | no | not a board: a drawing of geometric constraints, no footprint |
| simulation | [K/simulation](https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/simulation) | `97acc80c` | CC-BY-SA-4.0 | as ecc83 | schematics only (13 projects) | – | – | no | no board |

Notes:

- **Two licence statements.** `LICENSE.README` of the KiCad repository says that all files of `demos/` are under
  CC BY-SA 4.0, while five demo folders carry their own licence file (Apache-2.0, CERN-OHL-P, CERN-OHL-S, CC BY-SA 4.0
  and CC BY-NC-SA 4.0). For those five, the folder's own licence (the authors' grant) is taken. For the demos without
  a licence file, the CC BY-SA 4.0 statement of `LICENSE.README` is taken. `docs/research/board-library.md` assumed
  GPL-2+ for these older demos, but no GPL statement covers `demos/` at the pinned commit. A reviewer may want to
  confirm this reading.
- **Authors.** The older demos name no individual author or copyright holder; their items say "KiCad project".
- **Modified upstream.** `cm5_minima` and `royalblue54L_feather` were modified by the KiCad project when they entered
  the demos (their READMEs say so). The originals are `github.com/piecol/CM5_MINIMA_REV3` and the Lord's Boards
  repository, which a later batch could convert instead.

## Other sources

Commit: the default branch's HEAD on 2026-10-30. Licence: the first line of the licence file was read in each
repository. None of these was converted in this batch: the KiCad demos came first, and issue 1 would block any
board whose copper the Fenolite guard rejects. Boards in KiCad 5 to 7 need `kicad-cli` 10 for the upgrade, which
this environment did not have.

| project | URL | commit | licence | licence text | format | Cu | parts | in? | status, why |
|---|---|---|---|---|---|---|---|---|---|
| Antmicro lpddr4-testbed | https://github.com/antmicro/lpddr4-testbed | `93e67cfc3f267443d9b637073688457e8f5c1f91` | Apache-2.0 | `LICENSE` | KiCad 9.0 (`20241229`) | 6 | 68 | **in** | next: small, current format. Antmicro and OSHW logo footprints on the board |
| Antmicro ov9281-camera-board | https://github.com/antmicro/ov9281-camera-board | `ea69666fa06f66a0691e50eebff9356cc2a08e32` | Apache-2.0 | `LICENSE` | KiCad 9.0 (`20241229`) | 4 | 82 | **in** | next: small, current format; logo footprints |
| Antmicro hdmi-mipi-bridge | https://github.com/antmicro/hdmi-mipi-bridge | `6c683289a3191ee6c92cf4f9065ca9b6cb2c0784` | Apache-2.0 | `LICENSE` | KiCad 7 (`20221018`): needs an upgrade | 4 | 121 | **in** | medium; logo footprints |
| Antmicro raspberry-pi-cm4-csi-adapter | https://github.com/antmicro/raspberry-pi-cm4-csi-adapter | `c69ae13fbcd7c879f9e21386e9785ea9e6c029dc` | Apache-2.0 | `LICENSE` | KiCad 5 (`20171130`): needs an upgrade | 4 | 19 | **in** | tiny; old format |
| Antmicro jetson-nano-baseboard | https://github.com/antmicro/jetson-nano-baseboard | `d8d0b2d71ab4cc4bcdb204a09f78be40d4c8cda3` | Apache-2.0 | `LICENSE` | KiCad 9.0 (`20241229`) | 8 | 391 | **in** | later: large (27 MB) |
| Antmicro sdi-mipi-video-converter-hw | https://github.com/antmicro/sdi-mipi-video-converter-hw | `5e181748d4a3a20ef88889025bc3085ef7652e36` | Apache-2.0 | `LICENSE` | KiCad 9.0 (`20241229`) | 8 | 396 | **in** | later: large (25 MB) |
| Antmicro kria-k26-devboard | https://github.com/antmicro/kria-k26-devboard | `9ead4dfc5b29fa9308206ccdfe013dd8f6d93b67` | Apache-2.0 | `LICENSE` | KiCad 7 (`20221018`) | 8 | 660 | **in** | later: very large (54 MB) |
| Antmicro jetson-orin-baseboard | https://github.com/antmicro/jetson-orin-baseboard | `34f0e7f5fbca441191e20ed55d93cf8614e12bed` | Apache-2.0 | `LICENSE` | KiCad 8.0 (`20240108`) | 8 | 681 | **in** | later: very large (36 MB) |
| CERN OHWR: AIDAinnova TLU, PSU prototype | https://gitlab.com/ohwr/cussans/aidainnova_tlu-hw (`hardware/KiCad/PSU_Prototyping/`) | `fb0751f0913f54d335b4e1ba41965f340256959d` | CERN-OHL-S-2.0 | `LICENSE` | KiCad 9.0 (`20241229`) | 2 | 47 | **in** | next (the CERN board of the batch): small; the only KiCad board of the repository (the TLU boards are Cadence) |
| CERN OHWR: Macbeth (Synchrotron SOLEIL) | https://gitlab.com/ohwr/project/macbeth | `5e339d8fde71c07dd9b5ebac33dd2321c47bc0c0` | CERN-OHL-S-2.0 | `licenses/cern_ohl_s_v2.txt` | KiCad 8.0 (`20240108`) | 12 | 1 566 | **in** | later: very large (61 MB); "Synchrotron SOLEIL's name and logo cannot be used without permission", two SOLEIL logo footprints on the board |
| CERN OHWR: mdior (DI/OT RTM) | https://gitlab.com/ohwr/project/mdior | `cac6b1bcb86ddbd2baab95120e12ea747770830a` | none in the repository (`.ohwr.yaml` and the board's silkscreen say CERN-OHL-W-2.0 or later) | – | KiCad 9.0 (`20241229`) | 6 | 237 | **no, for now** | no licence file; would be a good medium CERN board once the maintainers add one |
| CERN OHWR: timex3 | https://gitlab.com/ohwr/project/timex3 | `68878a4c8d9e2e524951a895af9826fd761d8888` | CERN-OHL-1.1 | `licenses/CERN-OHL-v1.1.txt` | legacy KiCad `.brd` (2013) | – | – | **no** | v1.1 is not on the allow-list (v1.2 and v2 are); legacy format |
| CERN OHWR: f-watch | https://gitlab.com/ohwr/project/f-watch | `102fcc56ed2237c1340b527cdd4478025e4ad4a3` | none for the hardware (`mec/LICENSE` covers the mechanics) | – | KiCad 4 (`version 3`, 2014) | – | – | **no** | no hardware licence file; legacy format |
| MNT Reform protected battery pack | https://source.mnt.re/reform/reform (`reform2-protected-batterypack-pcb/`) | `9dcb9a8df504f7c448625f463d4340d86197ee82` | CERN-OHL-S-2.0 | `LICENSES/CERN-OHL-S v2.txt`; root `LICENSE` (CERN-OHL-S v2, then GPLv3 for software) | KiCad 6 (`20211014`): needs an upgrade | 2 | 38 | **in** | next (the MNT board of the batch): small. Trademarks: the README says the "MNT" and "MNT REFORM" logos "may not be used in derived works"; the badge footprint `mref-protected-batterypack-badge` must be removed by a recorded step, and `trademarks.restricted` set until then |
| MNT Reform motherboard 3.0 | https://source.mnt.re/reform/reform (`reform2-motherboard30-pcb/`) | `9dcb9a8df504f7c448625f463d4340d86197ee82` | CERN-OHL-S-2.0 | as above | KiCad 8.0 (`20240108`) | 6 | 529 | **in** | later: large; `mntreform` logo and badge footprints |
| Libre Solar bms-c1 | https://github.com/LibreSolar/bms-c1 | `0ca09706f49906bdc73f6ccf99635de349d47474` | CERN-OHL-W-2.0 | `LICENCE`; README agrees (documentation CC BY-SA 4.0) | KiCad 9.0 (`20241229`) | 4 | 210 | **in** | next (the Libre Solar board of the batch): medium, current format; `LIBRESOLAR_LOGO` footprint; libraries are git submodules (their licences not read; the footprints are embedded in the board) |
| Libre Solar mppt-2420-hc | https://github.com/LibreSolar/mppt-2420-hc | `b1c11fee826d40b0465eae3dd58a15a336be2d7c` | CERN-OHL-W-2.0 | `LICENCE` (README states no licence) | KiCad 5 (`20171130`): needs an upgrade | 4 | 172 | **in** | old format |

Notes:

- **Antmicro.** All eight repositories have a root `LICENSE` whose text is the Apache License 2.0; four keep the
  template line "Copyright [yyyy] [name of copyright owner]", the others "Copyright 20xx Antmicro". No NOTICE file.
  Apache-2.0 §6 grants no trademark rights, and every board carries an Antmicro logo footprint: list it under
  `trademarks.marks` and keep it out of the gallery. Research section 4.5 asks to contact Antmicro before featuring
  their boards.
- **CERN OHWR.** Most OHWR boards probed are Altium or Cadence, or hold no board; no small or medium KiCad board with
  a licence file was found under `ohwr/project/` apart from those listed. The TLU PSU prototype lives in a personal
  sub-namespace of the OHWR group.
- **MNT Research.** Two subfolders of the repository carry other licences (`reform2-oled-pcb/KiCad-SSD1306_OLED-0.91-128x32/`
  MIT, `reform2-keyboard4-pcb/keyswitches.pretty/` CC BY-SA 4.0). The repository provides `symbol-for-derived-works/`
  footprints for derived boards. Whether every `*-badge` footprint holds the MNT logo was not checked by rendering.
- **Not confirmed:** the licences of the bms-c1 library submodules; no trademark file exists for Antmicro or Libre
  Solar beyond Apache-2.0 §6 and CERN-OHL.
