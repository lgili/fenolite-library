# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/ecc83@97acc80c223d75520c03fc44cab63cd9a3202c42 by Fenolite 0.7.0.dev0 on 2026-11-03;
# modified: format conversion to the Fenolite DSL.

import copper
from fenolite.dsl import Design, Module, Net, Part, connect, mm, stack

design = Design("ecc83-pp")

design.board(
    outline=(
        (mm("21.285"), mm("-9.83")),
        (mm("73.355"), mm("-9.83")),
        (mm("73.355"), mm("36.525")),
        (mm("21.285"), mm("36.525")),
    ),
    outline_width=mm("0.127"),
)
design.stackup(
    stack.silkscreen(color="White"),
    stack.mask(mm("0.01"), color="Green"),
    stack.copper(mm("0.035")),
    stack.core(mm("1.51"), material="FR4", epsilon_r="4.5", loss_tangent="0.02"),
    stack.copper(mm("0.035")),
    stack.mask(mm("0.01"), color="Green"),
    stack.silkscreen(color="White"),
)

gnd = Net("GND")
net_p1_pm = Net("Net-(P1-PM)")
net_p2_p1 = Net("Net-(P2-P1)")
net_p3_p1 = Net("Net-(P3-P1)")
net_p4_p1 = Net("Net-(P4-P1)")
net_p4_pm = Net("Net-(P4-PM)")
net_u1a_g = Net("Net-(U1A-G)")
net_u1a_k = Net("Net-(U1A-K)")
net_u1b_k = Net("Net-(U1B-K)")

design.rules.netclass(
    "Default",
    clearance=mm("0.4"),
    track_width=mm("0.8"),
    via_diameter=mm("1.2"),
    via_drill=mm("0.6"),
    diff_pair_width=mm("0.2"),
    diff_pair_gap=mm("0.25"),
    diff_pair_via_gap=mm("0.25"),
    nets=(),
)

c1 = Part("C1", "ecc83-pp:CP", footprint="Capacitor_THT:CP_Radial_D10.0mm_P5.00mm", value="10uF")
c2 = Part("C2", "ecc83-pp:C", footprint="Capacitor_THT:C_Disc_D4.7mm_W2.5mm_P5.00mm", value="680nF")
p1 = Part("P1", "ecc83-pp:CONN_2", footprint="Footprints:Altech_AK300_1x02_P5.00mm_45-Degree", value="IN")
p2 = Part(
    "P2",
    "ecc83-pp:CONN_2",
    footprint="Footprints:Altech_AK300_1x02_P5.00mm_45-Degree",
    footprint_definition="Footprints:Altech_AK300_1x02_P5.00mm_45-Degree_2",
    value="OUT",
)
p3 = Part(
    "P3",
    "ecc83-pp:CONN_2",
    footprint="Footprints:Altech_AK300_1x02_P5.00mm_45-Degree",
    footprint_definition="Footprints:Altech_AK300_1x02_P5.00mm_45-Degree_3",
    value="POWER",
)
p4 = Part(
    "P4",
    "ecc83-pp:CONN_2",
    footprint="Footprints:Altech_AK300_1x02_P5.00mm_45-Degree",
    footprint_definition="Footprints:Altech_AK300_1x02_P5.00mm_45-Degree_4",
    value="CONN_2",
)
p5 = Part(
    "P5",
    "ecc83-pp:CONN_1",
    footprint="Footprints:MountingHole_3.2mm_M3_DIN965_Pad",
    value="MOUNTING_HOLE",
)
p6 = Part(
    "P6",
    "ecc83-pp:CONN_1",
    footprint="Footprints:MountingHole_3.2mm_M3_DIN965_Pad",
    footprint_definition="Footprints:MountingHole_3.2mm_M3_DIN965_Pad_2",
    value="MOUNTING_HOLE",
)
p7 = Part(
    "P7",
    "ecc83-pp:CONN_1",
    footprint="Footprints:MountingHole_3.2mm_M3_DIN965_Pad",
    footprint_definition="Footprints:MountingHole_3.2mm_M3_DIN965_Pad_3",
    value="MOUNTING_HOLE",
)
p8 = Part(
    "P8",
    "ecc83-pp:CONN_1",
    footprint="Footprints:MountingHole_3.2mm_M3_DIN965_Pad",
    footprint_definition="Footprints:MountingHole_3.2mm_M3_DIN965_Pad_4",
    value="MOUNTING_HOLE",
)
r1 = Part(
    "R1",
    "ecc83-pp:R",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal",
    value="1.5K",
)
r2 = Part(
    "R2",
    "ecc83-pp:R",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal",
    footprint_definition="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal_2",
    value="1.5K",
)
r3 = Part(
    "R3",
    "ecc83-pp:R",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal",
    footprint_definition="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal_2",
    value="100K",
)
r4 = Part(
    "R4",
    "ecc83-pp:R",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal",
    footprint_definition="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal_3",
    value="47K",
)
u1 = Part("U1", "ecc83-pp:ECC83", footprint="Footprints:Valve_ECC-83-1", value="ECC83")

racine = Module("racine")

racine.add(c1, c2, p1, p2, p3, p4, p5, p6, p7, p8, r1, r2, r3, r4, u1)
design.add(racine)

connect(gnd, c1["2"], p1["1"], p2["2"], p3["2"], r2["2"], r3["2"], r4["2"])
connect(net_p1_pm, p1["2"], r4["1"], u1["2"])
connect(net_p2_p1, c2["1"], p2["1"], r3["1"])
connect(net_p3_p1, c1["1"], p3["1"], u1["6"])
connect(net_p4_p1, p4["1"], u1["9"])
connect(net_p4_pm, p4["2"], u1["4"], u1["5"])
connect(net_u1a_g, r1["1"], u1["1"], u1["7"])
connect(net_u1a_k, c2["2"], r1["2"], u1["8"])
connect(net_u1b_k, r2["1"], u1["3"])

c1.place(mm("41.605"), mm("-0.305"), rot=90)
c2.place(mm("37.16"), mm("25.095"), rot=90)
p1.place(mm("66.37"), mm("5.41"), rot=90)
p2.place(mm("28.27"), mm("12.776"), rot=-90)
p3.place(mm("28.27"), mm("0.711"), rot=-90)
p4.place(mm("45.542"), mm("31.191"))
p5.place(mm("25.095"), mm("-6.02"))
p6.place(mm("69.545"), mm("-6.02"))
p7.place(mm("69.545"), mm("32.715"))
p8.place(mm("25.095"), mm("32.715"))
r1.place(mm("36.271"), mm("7.95"), rot=-90)
r2.place(mm("56.21"), mm("-4.115"), rot=180)
r3.place(mm("33.985"), mm("25.095"), rot=180)
r4.place(mm("64.465"), mm("17.475"), rot=-90)
u1.place(mm("49.225"), mm("13.665"))

design.zone(
    gnd,
    layers=("B.Cu",),
    key="GND/1",
    outline=(
        (mm("72.085"), mm("35.89")),
        (mm("72.085"), mm("-8.687")),
        (mm("22.555"), mm("-8.56")),
        (mm("22.555"), mm("35.89")),
    ),
    clearance=mm("0.635"),
    min_thickness=mm("0.381"),
    thermal_gap=mm("0.254"),
    thermal_spoke_width=mm("0.50038"),
)

copper.apply(
    design,
    {
        "GND": gnd,
        "Net-(P1-PM)": net_p1_pm,
        "Net-(P2-P1)": net_p2_p1,
        "Net-(P3-P1)": net_p3_p1,
        "Net-(P4-P1)": net_p4_p1,
        "Net-(P4-PM)": net_p4_pm,
        "Net-(U1A-G)": net_u1a_g,
        "Net-(U1A-K)": net_u1a_k,
        "Net-(U1B-K)": net_u1b_k,
    },
)

design.load_schematic("schematic.toml")

design.kicad_project(
    "native/project.kicad_pro",
    sha256="8a943fac4b0cc3ed4fa83ccc83a6e15b9326178845ada0aa906df63f0672e975",
    preserve_minimums=True,
)
