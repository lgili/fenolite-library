# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/microwave@97acc80c223d75520c03fc44cab63cd9a3202c42 by Fenolite 0.7.0.dev0 on 2026-11-03;
# modified: format conversion to the Fenolite DSL.

from fenolite.dsl import Design, Part, mm

design = Design("microwave")

design.board(
    outline=(
        (mm("-40.31"), mm("-18.72")),
        (mm("251.79"), mm("-18.72")),
        (mm("251.79"), mm("101.93")),
        (mm("-40.31"), mm("101.93")),
    ),
    outline_width=mm("0.3048"),
)

design.rules.netclass(
    "Default",
    clearance=mm("0.254"),
    track_width=mm("0.254"),
    via_diameter=mm("0.889"),
    via_drill=mm("0.635"),
    diff_pair_width=mm("0.2"),
    diff_pair_gap=mm("0.25"),
    diff_pair_via_gap=mm("0.25"),
    nets=(),
)

poly_1 = Part(
    "POLY",
    "Imported:POLY",
    footprint="POLY",
    footprint_definition="Imported:POLY",
    value="VAL**",
    name="POLY_1",
    board_only=True,
)
poly_2 = Part(
    "POLY",
    "Imported:POLY_2",
    footprint="POLY",
    footprint_definition="Imported:POLY_2",
    value="VAL**",
    name="POLY_2",
    board_only=True,
)
poly_3 = Part(
    "POLY",
    "Imported:POLY_3",
    footprint="POLY",
    footprint_definition="Imported:POLY_3",
    value="VAL**",
    name="POLY_3",
    board_only=True,
)
poly_4 = Part(
    "POLY",
    "Imported:POLY_3",
    footprint="POLY",
    footprint_definition="Imported:POLY_3",
    value="VAL**",
    name="POLY_4",
    board_only=True,
)

design.add(poly_1, poly_2, poly_3, poly_4)

poly_1.place(mm("103.17968"), mm("17.21084"))
poly_2.place(mm("103.18984"), mm("21.54408"))
poly_3.place(mm("103.2"), mm("19.38"))
poly_4.place(mm("103.2"), mm("44.78"))

design.line(
    "Dwgs.User/line/1",
    (mm("62.4076"), mm("20.38076")),
    (mm("64.10178"), mm("20.38076")),
    layer="Dwgs.User",
    width=mm("0.3048"),
)
design.line(
    "Dwgs.User/line/2",
    (mm("102.84694"), mm("20.54332")),
    (mm("103.50988"), mm("20.54332")),
    layer="Dwgs.User",
    width=mm("0.3048"),
)
design.line(
    "Dwgs.User/line/3",
    (mm("103.50988"), mm("20.54332")),
    (mm("103.50988"), mm("20.55348")),
    layer="Dwgs.User",
    width=mm("0.3048"),
)

design.kicad_project(
    "native/project.kicad_pro",
    sha256="ea9d9b756ae3b51d485c2dcb904f09aaee0190e4b584f038c3094536e7a9334a",
    preserve_minimums=True,
)
