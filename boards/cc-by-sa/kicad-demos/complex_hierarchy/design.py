# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/complex_hierarchy@97acc80c223d75520c03fc44cab63cd9a3202c42 by Fenolite 0.7.0.dev0 on 2026-11-03;
# modified: format conversion to the Fenolite DSL.

import copper
from sheets import ampli_ht as _sheet_ampli_ht
from fenolite.dsl import Design, Net, Part, connect, mm, stack

design = Design("complex_hierarchy")

design.board(
    outline=(
        (mm("-12.1"), mm("-48.2")),
        (mm("88.595"), mm("-48.184")),
        (mm("88.595"), mm("31.826")),
        (mm("-12.1"), mm("31.826")),
    ),
    max_curve_error=mm("0.01"),
    outline_width=mm("0.2032"),
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
design.title_block(title="Actionneur_piezo", organization="Kicad devs", doc_id="Demo")

net_12v = Net("+12V")
vaa = Net("-VAA")
net_12vext = Net("/12Vext")
gnd = Net("GND")
ht = Net("HT")
net_u102_cap = Net("Net-(U102-CAP+)")
net_u102_cap_2 = Net("Net-(U102-CAP-)")
vcc = Net("VCC")

c101 = Part(
    "C101",
    "complex_hierarchy:CP",
    footprint="Capacitor_THT:CP_Axial_L11.0mm_D6.0mm_P18.00mm_Horizontal",
    value="47uF/63V",
)
c102 = Part(
    "C102",
    "complex_hierarchy:CP",
    footprint="Capacitor_THT:CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal",
    value="47uF",
)
c103 = Part(
    "C103",
    "complex_hierarchy:CP",
    footprint="Capacitor_THT:CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal",
    footprint_definition="Capacitor_THT:CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal_2",
    value="10uF",
)
c104 = Part(
    "C104",
    "complex_hierarchy:CP",
    footprint="Capacitor_THT:CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal",
    footprint_definition="Capacitor_THT:CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal_3",
    value="47uF/20V",
)
c105 = Part(
    "C105",
    "complex_hierarchy:CP",
    footprint="Capacitor_THT:CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal",
    footprint_definition="Capacitor_THT:CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal_4",
    value="10uF",
)
d101 = Part(
    "D101",
    "complex_hierarchy:D_Small",
    footprint="Diode_THT:D_DO-41_SOD81_P12.70mm_Horizontal",
    value="1N4007",
)
p101 = Part(
    "P101",
    "complex_hierarchy:CONN_2",
    footprint="TerminalBlock_Altech:Altech_AK300_1x02_P5.00mm_45-Degree",
    value="CONN_2",
)
p102 = Part(
    "P102",
    "complex_hierarchy:CONN_2",
    footprint="TerminalBlock_Altech:Altech_AK300_1x02_P5.00mm_45-Degree",
    footprint_definition="TerminalBlock_Altech:Altech_AK300_1x02_P5.00mm_45-Degree_2",
    value="CONN_2",
)
u101 = Part(
    "U101",
    "complex_hierarchy:7805",
    footprint="Package_TO_SOT_THT:TO-92_HandSolder",
    footprint_definition="Package_TO_SOT_THT:TO-92_HandSolder_7",
    value="78L05",
)
u102 = Part(
    "U102",
    "complex_hierarchy:ICL7660",
    footprint="Package_DIP:DIP-8_W7.62mm_LongPads",
    value="ICL7660",
)

design.add(c101, c102, c103, c104, c105, d101, p101, p102, u101, u102)
_sheet_ampli_ht.sheet(
    design,
    path="ampli_ht_horizontal",
    refs={
        "C201": "C301",
        "C202": "C302",
        "C203": "C303",
        "C204": "C304",
        "D201": "D301",
        "D202": "D302",
        "D203": "D303",
        "D204": "D304",
        "P201": "P301",
        "P202": "P302",
        "Q201": "Q301",
        "Q202": "Q302",
        "Q203": "Q303",
        "Q204": "Q304",
        "R201": "R301",
        "R202": "R302",
        "R203": "R303",
        "R204": "R304",
        "R205": "R305",
        "R206": "R306",
        "R207": "R307",
        "R208": "R308",
        "R209": "R309",
        "R210": "R310",
        "R211": "R311",
        "R212": "R312",
        "R213": "R313",
        "RV201": "RV301",
        "U201": "U301",
    },
    net_12v=net_12v,
    vaa=vaa,
    gnd=gnd,
    ht=ht,
)
_sheet_ampli_ht.sheet(
    design,
    path="ampli_ht_vertical",
    refs={
        "C201": "C201",
        "C202": "C202",
        "C203": "C203",
        "C204": "C204",
        "D201": "D201",
        "D202": "D202",
        "D203": "D203",
        "D204": "D204",
        "P201": "P201",
        "P202": "P202",
        "Q201": "Q201",
        "Q202": "Q202",
        "Q203": "Q203",
        "Q204": "Q204",
        "R201": "R201",
        "R202": "R202",
        "R203": "R203",
        "R204": "R204",
        "R205": "R205",
        "R206": "R206",
        "R207": "R207",
        "R208": "R208",
        "R209": "R209",
        "R210": "R210",
        "R211": "R211",
        "R212": "R212",
        "R213": "R213",
        "RV201": "RV201",
        "U201": "U201",
    },
    net_12v=net_12v,
    vaa=vaa,
    gnd=gnd,
    ht=ht,
)

ampli_ht_horizontal_piezo_in = design.nets["/ampli_ht_horizontal/PIEZO_IN"]
ampli_ht_horizontal_piezo_out = design.nets["/ampli_ht_horizontal/PIEZO_OUT"]
ampli_ht_horizontal_s_out = design.nets["/ampli_ht_horizontal/S_OUT+"]
ampli_ht_horizontal_vpil_0_3_3v = design.nets["/ampli_ht_horizontal/Vpil_0_3,3V"]
ampli_ht_vertical_piezo_in = design.nets["/ampli_ht_vertical/PIEZO_IN"]
ampli_ht_vertical_piezo_out = design.nets["/ampli_ht_vertical/PIEZO_OUT"]
ampli_ht_vertical_s_out = design.nets["/ampli_ht_vertical/S_OUT+"]
ampli_ht_vertical_vpil_0_3_3v = design.nets["/ampli_ht_vertical/Vpil_0_3,3V"]
net_c201_pad2 = design.nets["Net-(C201-Pad2)"]
net_c202_pad1 = design.nets["Net-(C202-Pad1)"]
net_c204_pad1 = design.nets["Net-(C204-Pad1)"]
net_c301_pad2 = design.nets["Net-(C301-Pad2)"]
net_c302_pad1 = design.nets["Net-(C302-Pad1)"]
net_c304_pad1 = design.nets["Net-(C304-Pad1)"]
net_d201_k = design.nets["Net-(D201-K)"]
net_d202_k = design.nets["Net-(D202-K)"]
net_d203_a = design.nets["Net-(D203-A)"]
net_d203_k = design.nets["Net-(D203-K)"]
net_d204_k = design.nets["Net-(D204-K)"]
net_d301_k = design.nets["Net-(D301-K)"]
net_d302_k = design.nets["Net-(D302-K)"]
net_d303_a = design.nets["Net-(D303-A)"]
net_d303_k = design.nets["Net-(D303-K)"]
net_d304_k = design.nets["Net-(D304-K)"]
net_q201_e = design.nets["Net-(Q201-E)"]
net_q202_e = design.nets["Net-(Q202-E)"]
net_q203_e = design.nets["Net-(Q203-E)"]
net_q204_b = design.nets["Net-(Q204-B)"]
net_q204_e = design.nets["Net-(Q204-E)"]
net_q301_e = design.nets["Net-(Q301-E)"]
net_q302_e = design.nets["Net-(Q302-E)"]
net_q303_e = design.nets["Net-(Q303-E)"]
net_q304_b = design.nets["Net-(Q304-B)"]
net_q304_e = design.nets["Net-(Q304-E)"]
net_r212_pad2 = design.nets["Net-(R212-Pad2)"]
net_r213_pad1 = design.nets["Net-(R213-Pad1)"]
net_r312_pad2 = design.nets["Net-(R312-Pad2)"]
net_r313_pad1 = design.nets["Net-(R313-Pad1)"]
net_u201a = design.nets["Net-(U201A--)"]
net_u201b = design.nets["Net-(U201B-+)"]
net_u301a = design.nets["Net-(U301A--)"]
net_u301b = design.nets["Net-(U301B-+)"]

design.rules.netclass(
    "Default",
    clearance=mm("0.3"),
    track_width=mm("0.4"),
    via_diameter=mm("1.651"),
    via_drill=mm("0.6"),
    diff_pair_width=mm("0.4"),
    diff_pair_gap=mm("0.35"),
    diff_pair_via_gap=mm("0.25"),
    nets=(),
)
design.rules.netclass(
    "power",
    clearance=mm("0.3"),
    track_width=mm("0.6"),
    via_diameter=mm("1.651"),
    via_drill=mm("0.6"),
    diff_pair_width=mm("0.4"),
    diff_pair_gap=mm("0.35"),
    diff_pair_via_gap=mm("0.25"),
    nets=(vaa, net_12vext, gnd, ht, vcc),
)

connect(net_12v, c104["1"], d101["1"], u101["3"])
connect(vaa, c103["2"], u102["5"])
connect(net_12vext, d101["2"], p102["1"])
connect(gnd, c101["2"], c102["2"], c103["1"], c104["2"], p101["2"], p102["2"], u101["2"], u102["3"])
connect(ht, c101["1"], p101["1"])
connect(net_u102_cap, c105["1"], u102["2"])
connect(net_u102_cap_2, c105["2"], u102["4"])
connect(vcc, c102["1"], u101["1"], u102["8"])

c101.place(mm("21.793"), mm("-39.421"), rot=180)
c102.place(mm("17.348"), mm("-26.594"), rot=180)
c103.place(mm("60.02"), mm("-21.641"), rot=90)
c104.place(mm("26.619"), mm("-39.294"))
c105.place(mm("39.7"), mm("-22.784"))
d101.place(mm("16.078"), mm("-31.674"), rot=180)
p101.place(mm("-5.1"), mm("-43.1"), rot=-90)
p102.place(mm("-5.2"), mm("-30.6"), rot=-90)
u101.place(mm("24.206"), mm("-29.134"), rot=90)
u102.place(mm("45.415"), mm("-27.864"), rot=90)

design.zone(
    gnd,
    layers=("B.Cu",),
    key="GND/1",
    outline=(
        (mm("87.325"), mm("31.572")),
        (mm("87.325"), mm("-46.914")),
        (mm("-11.608"), mm("-46.914")),
        (mm("-11.608"), mm("31.572")),
    ),
    clearance=mm("0.508"),
    min_thickness=mm("0.254"),
    thermal_gap=mm("0.762"),
    thermal_spoke_width=mm("0.508"),
)

design.text(
    "B.Cu/text/1",
    "Complex hierarchy\nDemo",
    (mm("82"), mm("-37")),
    layer="B.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
    rot=90,
)
design.text(
    "F.Cu/text/1",
    "Complex hierarchy\nDemo",
    (mm("77.4"), mm("-31")),
    layer="F.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)

copper.apply(
    design,
    {
        "+12V": net_12v,
        "-VAA": vaa,
        "/12Vext": net_12vext,
        "/ampli_ht_horizontal/PIEZO_IN": ampli_ht_horizontal_piezo_in,
        "/ampli_ht_horizontal/PIEZO_OUT": ampli_ht_horizontal_piezo_out,
        "/ampli_ht_horizontal/S_OUT+": ampli_ht_horizontal_s_out,
        "/ampli_ht_horizontal/Vpil_0_3,3V": ampli_ht_horizontal_vpil_0_3_3v,
        "/ampli_ht_vertical/PIEZO_IN": ampli_ht_vertical_piezo_in,
        "/ampli_ht_vertical/PIEZO_OUT": ampli_ht_vertical_piezo_out,
        "/ampli_ht_vertical/S_OUT+": ampli_ht_vertical_s_out,
        "/ampli_ht_vertical/Vpil_0_3,3V": ampli_ht_vertical_vpil_0_3_3v,
        "GND": gnd,
        "HT": ht,
        "Net-(C201-Pad2)": net_c201_pad2,
        "Net-(C202-Pad1)": net_c202_pad1,
        "Net-(C204-Pad1)": net_c204_pad1,
        "Net-(C301-Pad2)": net_c301_pad2,
        "Net-(C302-Pad1)": net_c302_pad1,
        "Net-(C304-Pad1)": net_c304_pad1,
        "Net-(D201-K)": net_d201_k,
        "Net-(D202-K)": net_d202_k,
        "Net-(D203-A)": net_d203_a,
        "Net-(D203-K)": net_d203_k,
        "Net-(D204-K)": net_d204_k,
        "Net-(D301-K)": net_d301_k,
        "Net-(D302-K)": net_d302_k,
        "Net-(D303-A)": net_d303_a,
        "Net-(D303-K)": net_d303_k,
        "Net-(D304-K)": net_d304_k,
        "Net-(Q201-E)": net_q201_e,
        "Net-(Q202-E)": net_q202_e,
        "Net-(Q203-E)": net_q203_e,
        "Net-(Q204-B)": net_q204_b,
        "Net-(Q204-E)": net_q204_e,
        "Net-(Q301-E)": net_q301_e,
        "Net-(Q302-E)": net_q302_e,
        "Net-(Q303-E)": net_q303_e,
        "Net-(Q304-B)": net_q304_b,
        "Net-(Q304-E)": net_q304_e,
        "Net-(R212-Pad2)": net_r212_pad2,
        "Net-(R213-Pad1)": net_r213_pad1,
        "Net-(R312-Pad2)": net_r312_pad2,
        "Net-(R313-Pad1)": net_r313_pad1,
        "Net-(U102-CAP+)": net_u102_cap,
        "Net-(U102-CAP-)": net_u102_cap_2,
        "Net-(U201A--)": net_u201a,
        "Net-(U201B-+)": net_u201b,
        "Net-(U301A--)": net_u301a,
        "Net-(U301B-+)": net_u301b,
        "VCC": vcc,
    },
)

design.load_schematic("schematic.toml")

design.kicad_project(
    "native/project.kicad_pro",
    sha256="55438416ca7fd46b5bad22da2693e9c43240060977d06daabcba084aa17e2804",
    preserve_minimums=True,
)
