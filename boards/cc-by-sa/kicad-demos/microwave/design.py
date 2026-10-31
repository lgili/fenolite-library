# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/microwave@97acc80c223d75520c03fc44cab63cd9a3202c42 by Fenolite 0.7.0.dev0 on 2026-10-31;
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
)

design.rules.minimum(
    track_width=mm("0.254"),
    via_diameter=mm("0.889"),
    hole_size=mm("0.508"),
    edge_clearance=mm("0.1524"),
)

poly_1 = Part(
    "POLY",
    "Imported:POLY",
    footprint="Imported:POLY",
    value="VAL**",
    name="POLY_1",
    board_only=True,
)
poly_2 = Part(
    "POLY",
    "Imported:POLY_2",
    footprint="Imported:POLY_2",
    value="VAL**",
    name="POLY_2",
    board_only=True,
)
poly_3 = Part(
    "POLY",
    "Imported:POLY_3",
    footprint="Imported:POLY_3",
    value="VAL**",
    name="POLY_3",
    board_only=True,
)
poly_4 = Part(
    "POLY",
    "Imported:POLY_3",
    footprint="Imported:POLY_3",
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
