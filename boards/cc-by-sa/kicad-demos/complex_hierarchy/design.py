# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/complex_hierarchy@97acc80c223d75520c03fc44cab63cd9a3202c42 by Fenolite 0.7.0.dev0 on 2026-10-31;
# modified: format conversion to the Fenolite DSL.

import copper
from fenolite.dsl import Design, Module, Net, Part, connect, mm, stack

design = Design("complex_hierarchy")

design.board(
    outline=(
        (mm("-12.1"), mm("-48.2")),
        (mm("88.595"), mm("-48.184")),
        (mm("88.595"), mm("31.826")),
        (mm("-12.1"), mm("31.826")),
    ),
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
ampli_ht_horizontal_piezo_in = Net("/ampli_ht_horizontal/PIEZO_IN")
ampli_ht_horizontal_piezo_out = Net("/ampli_ht_horizontal/PIEZO_OUT")
ampli_ht_horizontal_s_out = Net("/ampli_ht_horizontal/S_OUT+")
ampli_ht_horizontal_vpil_0_3_3v = Net("/ampli_ht_horizontal/Vpil_0_3,3V")
ampli_ht_vertical_piezo_in = Net("/ampli_ht_vertical/PIEZO_IN")
ampli_ht_vertical_piezo_out = Net("/ampli_ht_vertical/PIEZO_OUT")
ampli_ht_vertical_s_out = Net("/ampli_ht_vertical/S_OUT+")
ampli_ht_vertical_vpil_0_3_3v = Net("/ampli_ht_vertical/Vpil_0_3,3V")
gnd = Net("GND")
ht = Net("HT")
net_c201_pad2 = Net("Net-(C201-Pad2)")
net_c202_pad1 = Net("Net-(C202-Pad1)")
net_c204_pad1 = Net("Net-(C204-Pad1)")
net_c301_pad2 = Net("Net-(C301-Pad2)")
net_c302_pad1 = Net("Net-(C302-Pad1)")
net_c304_pad1 = Net("Net-(C304-Pad1)")
net_d201_k = Net("Net-(D201-K)")
net_d202_k = Net("Net-(D202-K)")
net_d203_a = Net("Net-(D203-A)")
net_d203_k = Net("Net-(D203-K)")
net_d204_k = Net("Net-(D204-K)")
net_d301_k = Net("Net-(D301-K)")
net_d302_k = Net("Net-(D302-K)")
net_d303_a = Net("Net-(D303-A)")
net_d303_k = Net("Net-(D303-K)")
net_d304_k = Net("Net-(D304-K)")
net_q201_e = Net("Net-(Q201-E)")
net_q202_e = Net("Net-(Q202-E)")
net_q203_e = Net("Net-(Q203-E)")
net_q204_b = Net("Net-(Q204-B)")
net_q204_e = Net("Net-(Q204-E)")
net_q301_e = Net("Net-(Q301-E)")
net_q302_e = Net("Net-(Q302-E)")
net_q303_e = Net("Net-(Q303-E)")
net_q304_b = Net("Net-(Q304-B)")
net_q304_e = Net("Net-(Q304-E)")
net_r212_pad2 = Net("Net-(R212-Pad2)")
net_r213_pad1 = Net("Net-(R213-Pad1)")
net_r312_pad2 = Net("Net-(R312-Pad2)")
net_r313_pad1 = Net("Net-(R313-Pad1)")
net_u102_cap = Net("Net-(U102-CAP+)")
net_u102_cap_2 = Net("Net-(U102-CAP-)")
net_u201a = Net("Net-(U201A--)")
net_u201b = Net("Net-(U201B-+)")
net_u301a = Net("Net-(U301A--)")
net_u301b = Net("Net-(U301B-+)")
vcc = Net("VCC")

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
design.rules.minimum(
    clearance=mm("0.2"),
    track_width=mm("0.2032"),
    via_diameter=mm("0.889"),
    hole_size=mm("0.508"),
    edge_clearance=mm("0.01"),
)

c101 = Part(
    "C101",
    "complex_hierarchy:CP_Axial_L11.0mm_D6.0mm_P18.00mm_Horizontal",
    footprint="complex_hierarchy:CP_Axial_L11.0mm_D6.0mm_P18.00mm_Horizontal",
    value="47uF/63V",
)
c102 = Part(
    "C102",
    "complex_hierarchy:CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal",
    footprint="complex_hierarchy:CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal",
    value="47uF",
)
c103 = Part(
    "C103",
    "complex_hierarchy:CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal_2",
    footprint="complex_hierarchy:CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal_2",
    value="10uF",
)
c104 = Part(
    "C104",
    "complex_hierarchy:CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal_3",
    footprint="complex_hierarchy:CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal_3",
    value="47uF/20V",
)
c105 = Part(
    "C105",
    "complex_hierarchy:CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal_4",
    footprint="complex_hierarchy:CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal_4",
    value="10uF",
)
d101 = Part(
    "D101",
    "complex_hierarchy:D_DO-41_SOD81_P12.70mm_Horizontal",
    footprint="complex_hierarchy:D_DO-41_SOD81_P12.70mm_Horizontal",
    value="1N4007",
)
p101 = Part(
    "P101",
    "complex_hierarchy:Altech_AK300_1x02_P5.00mm_45-Degree",
    footprint="complex_hierarchy:Altech_AK300_1x02_P5.00mm_45-Degree",
    value="CONN_2",
)
p102 = Part(
    "P102",
    "complex_hierarchy:Altech_AK300_1x02_P5.00mm_45-Degree_2",
    footprint="complex_hierarchy:Altech_AK300_1x02_P5.00mm_45-Degree_2",
    value="CONN_2",
)
u101 = Part(
    "U101",
    "complex_hierarchy:TO-92_HandSolder_7",
    footprint="complex_hierarchy:TO-92_HandSolder_7",
    value="78L05",
)
u102 = Part(
    "U102",
    "complex_hierarchy:DIP-8_W7.62mm_LongPads",
    footprint="complex_hierarchy:DIP-8_W7.62mm_LongPads",
    value="ICL7660",
)
c301 = Part(
    "C301",
    "complex_hierarchy:C_Disc_D5.0mm_W2.5mm_P5.00mm_5",
    footprint="complex_hierarchy:C_Disc_D5.0mm_W2.5mm_P5.00mm_5",
    value="15nF",
)
c302 = Part(
    "C302",
    "complex_hierarchy:C_Disc_D5.0mm_W2.5mm_P5.00mm_6",
    footprint="complex_hierarchy:C_Disc_D5.0mm_W2.5mm_P5.00mm_6",
    value="150nF",
)
c303 = Part(
    "C303",
    "complex_hierarchy:C_Disc_D5.0mm_W2.5mm_P5.00mm_7",
    footprint="complex_hierarchy:C_Disc_D5.0mm_W2.5mm_P5.00mm_7",
    value="4.7nF",
)
c304 = Part(
    "C304",
    "complex_hierarchy:C_Disc_D5.0mm_W2.5mm_P5.00mm_8",
    footprint="complex_hierarchy:C_Disc_D5.0mm_W2.5mm_P5.00mm_8",
    value="820pF",
)
d301 = Part(
    "D301",
    "complex_hierarchy:D_DO-35_SOD27_P7.62mm_Horizontal_5",
    footprint="complex_hierarchy:D_DO-35_SOD27_P7.62mm_Horizontal_5",
    value="1N4148",
)
d302 = Part(
    "D302",
    "complex_hierarchy:D_DO-35_SOD27_P7.62mm_Horizontal_6",
    footprint="complex_hierarchy:D_DO-35_SOD27_P7.62mm_Horizontal_6",
    value="1N4148",
)
d303 = Part(
    "D303",
    "complex_hierarchy:D_DO-35_SOD27_P7.62mm_Horizontal_7",
    footprint="complex_hierarchy:D_DO-35_SOD27_P7.62mm_Horizontal_7",
    value="1N4148",
)
d304 = Part(
    "D304",
    "complex_hierarchy:D_DO-35_SOD27_P7.62mm_Horizontal_8",
    footprint="complex_hierarchy:D_DO-35_SOD27_P7.62mm_Horizontal_8",
    value="1N4148",
)
p301 = Part(
    "P301",
    "complex_hierarchy:Altech_AK300_1x02_P5.00mm_45-Degree_5",
    footprint="complex_hierarchy:Altech_AK300_1x02_P5.00mm_45-Degree_5",
    value="CONN_2",
)
p302 = Part(
    "P302",
    "complex_hierarchy:Altech_AK300_1x02_P5.00mm_45-Degree_6",
    footprint="complex_hierarchy:Altech_AK300_1x02_P5.00mm_45-Degree_6",
    value="CONN_2",
)
q301 = Part(
    "Q301",
    "complex_hierarchy:TO-92_HandSolder_5",
    footprint="complex_hierarchy:TO-92_HandSolder_5",
    value="MPSA92",
)
q302 = Part(
    "Q302",
    "complex_hierarchy:TO-92_HandSolder_2",
    footprint="complex_hierarchy:TO-92_HandSolder_2",
    value="MPSA42",
)
q303 = Part(
    "Q303",
    "complex_hierarchy:TO-92_HandSolder_6",
    footprint="complex_hierarchy:TO-92_HandSolder_6",
    value="MPSA92",
)
q304 = Part(
    "Q304",
    "complex_hierarchy:TO-92_HandSolder_2",
    footprint="complex_hierarchy:TO-92_HandSolder_2",
    value="MPSA42",
)
r301 = Part(
    "R301",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
    value="1K",
)
r302 = Part(
    "R302",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_8",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_8",
    value="22K",
)
r303 = Part(
    "R303",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_9",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_9",
    value="22K",
)
r304 = Part(
    "R304",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
    value="470",
)
r305 = Part(
    "R305",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_10",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_10",
    value="220K",
)
r306 = Part(
    "R306",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
    value="47",
)
r307 = Part(
    "R307",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
    value="47",
)
r308 = Part(
    "R308",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
    value="1K",
)
r309 = Part(
    "R309",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_5",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_5",
    value="220K",
)
r310 = Part(
    "R310",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_5",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_5",
    value="220K",
)
r311 = Part(
    "R311",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_11",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_11",
    value="5,6K",
)
r312 = Part(
    "R312",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
    value="1K",
)
r313 = Part(
    "R313",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_7",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_7",
    value="4,7K",
)
rv301 = Part(
    "RV301",
    "complex_hierarchy:Potentiometer_Bourns_3266W_Vertical",
    footprint="complex_hierarchy:Potentiometer_Bourns_3266W_Vertical",
    value="4,7K",
)
u301 = Part(
    "U301",
    "complex_hierarchy:DIP-8_W7.62mm_LongPads",
    footprint="complex_hierarchy:DIP-8_W7.62mm_LongPads",
    value="LM358N",
)
c201 = Part(
    "C201",
    "complex_hierarchy:C_Disc_D5.0mm_W2.5mm_P5.00mm",
    footprint="complex_hierarchy:C_Disc_D5.0mm_W2.5mm_P5.00mm",
    value="15nF",
)
c202 = Part(
    "C202",
    "complex_hierarchy:C_Disc_D5.0mm_W2.5mm_P5.00mm_2",
    footprint="complex_hierarchy:C_Disc_D5.0mm_W2.5mm_P5.00mm_2",
    value="150nF",
)
c203 = Part(
    "C203",
    "complex_hierarchy:C_Disc_D5.0mm_W2.5mm_P5.00mm_3",
    footprint="complex_hierarchy:C_Disc_D5.0mm_W2.5mm_P5.00mm_3",
    value="4.7nF",
)
c204 = Part(
    "C204",
    "complex_hierarchy:C_Disc_D5.0mm_W2.5mm_P5.00mm_4",
    footprint="complex_hierarchy:C_Disc_D5.0mm_W2.5mm_P5.00mm_4",
    value="820pF",
)
d201 = Part(
    "D201",
    "complex_hierarchy:D_DO-35_SOD27_P7.62mm_Horizontal",
    footprint="complex_hierarchy:D_DO-35_SOD27_P7.62mm_Horizontal",
    value="1N4148",
)
d202 = Part(
    "D202",
    "complex_hierarchy:D_DO-35_SOD27_P7.62mm_Horizontal_2",
    footprint="complex_hierarchy:D_DO-35_SOD27_P7.62mm_Horizontal_2",
    value="1N4148",
)
d203 = Part(
    "D203",
    "complex_hierarchy:D_DO-35_SOD27_P7.62mm_Horizontal_3",
    footprint="complex_hierarchy:D_DO-35_SOD27_P7.62mm_Horizontal_3",
    value="1N4148",
)
d204 = Part(
    "D204",
    "complex_hierarchy:D_DO-35_SOD27_P7.62mm_Horizontal_4",
    footprint="complex_hierarchy:D_DO-35_SOD27_P7.62mm_Horizontal_4",
    value="1N4148",
)
p201 = Part(
    "P201",
    "complex_hierarchy:Altech_AK300_1x02_P5.00mm_45-Degree_3",
    footprint="complex_hierarchy:Altech_AK300_1x02_P5.00mm_45-Degree_3",
    value="CONN_2",
)
p202 = Part(
    "P202",
    "complex_hierarchy:Altech_AK300_1x02_P5.00mm_45-Degree_4",
    footprint="complex_hierarchy:Altech_AK300_1x02_P5.00mm_45-Degree_4",
    value="CONN_2",
)
q201 = Part(
    "Q201",
    "complex_hierarchy:TO-92_HandSolder",
    footprint="complex_hierarchy:TO-92_HandSolder",
    value="MPSA92",
)
q202 = Part(
    "Q202",
    "complex_hierarchy:TO-92_HandSolder_2",
    footprint="complex_hierarchy:TO-92_HandSolder_2",
    value="MPSA42",
)
q203 = Part(
    "Q203",
    "complex_hierarchy:TO-92_HandSolder_3",
    footprint="complex_hierarchy:TO-92_HandSolder_3",
    value="MPSA92",
)
q204 = Part(
    "Q204",
    "complex_hierarchy:TO-92_HandSolder_4",
    footprint="complex_hierarchy:TO-92_HandSolder_4",
    value="MPSA42",
)
r201 = Part(
    "R201",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
    value="1K",
)
r202 = Part(
    "R202",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_2",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_2",
    value="22K",
)
r203 = Part(
    "R203",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_3",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_3",
    value="22K",
)
r204 = Part(
    "R204",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
    value="470",
)
r205 = Part(
    "R205",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_5",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_5",
    value="220K",
)
r206 = Part(
    "R206",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
    value="47",
)
r207 = Part(
    "R207",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
    value="47",
)
r208 = Part(
    "R208",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
    value="1K",
)
r209 = Part(
    "R209",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_5",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_5",
    value="220K",
)
r210 = Part(
    "R210",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_5",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_5",
    value="220K",
)
r211 = Part(
    "R211",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_6",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_6",
    value="5,6K",
)
r212 = Part(
    "R212",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
    value="1K",
)
r213 = Part(
    "R213",
    "complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_7",
    footprint="complex_hierarchy:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_7",
    value="4,7K",
)
rv201 = Part(
    "RV201",
    "complex_hierarchy:Potentiometer_Bourns_3266W_Vertical",
    footprint="complex_hierarchy:Potentiometer_Bourns_3266W_Vertical",
    value="4,7K",
)
u201 = Part(
    "U201",
    "complex_hierarchy:DIP-8_W7.62mm_LongPads",
    footprint="complex_hierarchy:DIP-8_W7.62mm_LongPads",
    value="LM358N",
)

ampli_ht_horizontal = Module("ampli_ht_horizontal")
ampli_ht_vertical = Module("ampli_ht_vertical")

ampli_ht_horizontal.add(
    c301,
    c302,
    c303,
    c304,
    d301,
    d302,
    d303,
    d304,
    p301,
    p302,
    q301,
    q302,
    q303,
    q304,
    r301,
    r302,
    r303,
    r304,
    r305,
    r306,
    r307,
    r308,
    r309,
    r310,
    r311,
    r312,
    r313,
    rv301,
    u301,
)
ampli_ht_vertical.add(
    c201,
    c202,
    c203,
    c204,
    d201,
    d202,
    d203,
    d204,
    p201,
    p202,
    q201,
    q202,
    q203,
    q204,
    r201,
    r202,
    r203,
    r204,
    r205,
    r206,
    r207,
    r208,
    r209,
    r210,
    r211,
    r212,
    r213,
    rv201,
    u201,
)
design.add(c101, c102, c103, c104, c105, d101, p101, p102, u101, u102, ampli_ht_horizontal, ampli_ht_vertical)

connect(net_12v, c104["1"], d101["1"], u101["3"], u201["8"], u301["8"])
connect(vaa, c103["2"], u102["5"], u201["4"], u301["4"])
connect(net_12vext, d101["2"], p102["1"])
connect(ampli_ht_horizontal_piezo_in, p301["1"], r301["2"])
connect(ampli_ht_horizontal_piezo_out, p302["1"], r306["1"], r307["1"])
connect(ampli_ht_horizontal_s_out, r309["1"], r310["1"], rv301["3"])
connect(ampli_ht_horizontal_vpil_0_3_3v, c301["1"], u301["3"], u301["6"], u301["7"])
connect(ampli_ht_vertical_piezo_in, p201["1"], r201["2"])
connect(ampli_ht_vertical_piezo_out, p202["1"], r206["1"], r207["1"])
connect(ampli_ht_vertical_s_out, r209["1"], r210["1"], rv201["3"])
connect(ampli_ht_vertical_vpil_0_3_3v, c201["1"], u201["3"], u201["6"], u201["7"])
connect(
    gnd,
    c101["2"],
    c102["2"],
    c103["1"],
    c104["2"],
    c202["2"],
    c203["2"],
    c204["2"],
    c302["2"],
    c303["2"],
    c304["2"],
    p101["2"],
    p102["2"],
    p201["2"],
    p202["2"],
    p301["2"],
    p302["2"],
    q203["3"],
    q303["3"],
    r205["2"],
    r208["2"],
    r213["2"],
    r305["2"],
    r308["2"],
    r313["2"],
    u101["2"],
    u102["3"],
)
connect(ht, c101["1"], d201["2"], d301["2"], p101["1"], q202["3"], q302["3"], r204["1"], r304["1"])
connect(net_c201_pad2, c201["2"], r202["1"], r203["2"])
connect(net_c202_pad1, c202["1"], r201["1"], r202["2"])
connect(net_c204_pad1, c204["1"], r211["2"])
connect(net_c301_pad2, c301["2"], r302["1"], r303["2"])
connect(net_c302_pad1, c302["1"], r301["1"], r302["2"])
connect(net_c304_pad1, c304["1"], r311["2"])
connect(net_d201_k, d201["1"], d202["2"])
connect(net_d202_k, d202["1"], q201["2"], r205["1"])
connect(net_d203_a, d203["2"], q201["3"], q202["2"])
connect(net_d203_k, d203["1"], d204["2"])
connect(net_d204_k, d204["1"], q203["2"], q204["3"], r211["1"])
connect(net_d301_k, d301["1"], d302["2"])
connect(net_d302_k, d302["1"], q301["2"], r305["1"])
connect(net_d303_a, d303["2"], q301["3"], q302["2"])
connect(net_d303_k, d303["1"], d304["2"])
connect(net_d304_k, d304["1"], q303["2"], q304["3"], r311["1"])
connect(net_q201_e, q201["1"], r204["2"])
connect(net_q202_e, q202["1"], r206["2"], r210["2"])
connect(net_q203_e, q203["1"], r207["2"], r209["2"])
connect(net_q204_b, q204["2"], r208["1"])
connect(net_q204_e, q204["1"], r212["1"])
connect(net_q301_e, q301["1"], r304["2"])
connect(net_q302_e, q302["1"], r306["2"], r310["2"])
connect(net_q303_e, q303["1"], r307["2"], r309["2"])
connect(net_q304_b, q304["2"], r308["1"])
connect(net_q304_e, q304["1"], r312["1"])
connect(net_r212_pad2, r212["2"], u201["1"])
connect(net_r213_pad1, r213["1"], rv201["1"])
connect(net_r312_pad2, r312["2"], u301["1"])
connect(net_r313_pad1, r313["1"], rv301["1"])
connect(net_u102_cap, c105["1"], u102["2"])
connect(net_u102_cap_2, c105["2"], u102["4"])
connect(net_u201a, rv201["2"], u201["2"])
connect(net_u201b, c203["1"], r203["1"], u201["5"])
connect(net_u301a, rv301["2"], u301["2"])
connect(net_u301b, c303["1"], r303["1"], u301["5"])
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
c301.place(mm("18.745"), mm("-18.593"), rot=180)
c302.place(mm("13.792"), mm("-22.022"))
c303.place(mm("13.792"), mm("-15.164"))
c304.place(mm("38.049"), mm("4.14"))
d301.place(mm("25.095"), mm("-21.133"))
d302.place(mm("32.715"), mm("-17.704"), rot=180)
d303.place(mm("45.415"), mm("-2.464"), rot=90)
d304.place(mm("41.605"), mm("-2.464"), rot=90)
p301.place(mm("-5.1"), mm("-15"), rot=-90)
p302.place(mm("81.2"), mm("-13.7"), rot=90)
q301.place(mm("31.445"), mm("-11.354"))
q302.place(mm("50.495"), mm("-10.084"))
q303.place(mm("51.003"), mm("0.965"), rot=180)
q304.place(mm("29.794"), mm("-3.48"), locked=True)
r301.place(mm("10.363"), mm("-21.26"), rot=180)
r302.place(mm("10.617"), mm("-17.704"), rot=180)
r303.place(mm("2.997"), mm("-15.037"))
r304.place(mm("45.415"), mm("-13.894"), rot=180)
r305.place(mm("37.795"), mm("-18.974"))
r306.place(mm("73.355"), mm("-8.814"), rot=180)
r307.place(mm("73.355"), mm("-2.464"), rot=180)
r308.place(mm("25.603"), mm("1.346"), rot=180)
r309.place(mm("56.845"), mm("-10.084"), rot=-90)
r310.place(mm("61.29"), mm("-10.084"), rot=-90)
r311.place(mm("41.605"), mm("1.346"), rot=180)
r312.place(mm("26.111"), mm("-5.004"), rot=180)
r313.place(mm("2.235"), mm("2.616"), rot=90)
rv301.place(mm("-6.655"), mm("0.076"), rot=180)
u301.place(mm("7.315"), mm("-3.734"), rot=90)
c201.place(mm("18.618"), mm("9.474"), rot=180)
c202.place(mm("13.665"), mm("6.045"))
c203.place(mm("13.665"), mm("12.776"))
c204.place(mm("38.176"), mm("30.048"))
d201.place(mm("27.635"), mm("5.918"))
d202.place(mm("27.635"), mm("8.966"))
d203.place(mm("44.78"), mm("23.571"), rot=90)
d204.place(mm("40.97"), mm("23.571"), rot=90)
p201.place(mm("-5.385"), mm("11.633"), rot=-90)
p202.place(mm("81.1925"), mm("12.4575"), rot=90)
q201.place(mm("31.445"), mm("15.316"))
q202.place(mm("49.225"), mm("15.062"))
q203.place(mm("51.765"), mm("23.825"), rot=180)
q204.place(mm("30.556"), mm("25.73"))
r201.place(mm("9.855"), mm("7.061"), rot=180)
r202.place(mm("9.855"), mm("10.236"), rot=180)
r203.place(mm("9.855"), mm("12.776"), rot=180)
r204.place(mm("46.685"), mm("8.966"), rot=180)
r205.place(mm("22.555"), mm("15.316"), rot=-90)
r206.place(mm("73.355"), mm("19.126"), rot=180)
r207.place(mm("73.355"), mm("22.936"), rot=180)
r208.place(mm("26.365"), mm("28.016"), rot=180)
r209.place(mm("56.21"), mm("16.713"), rot=-90)
r210.place(mm("60.02"), mm("16.586"), rot=-90)
r211.place(mm("44.399"), mm("26.873"), rot=180)
r212.place(mm("34.493"), mm("20.142"), rot=180)
r213.place(mm("2.87"), mm("26.746"), rot=90)
rv201.place(mm("-6.655"), mm("25.476"), rot=180)
u201.place(mm("7.315"), mm("24.206"), rot=90)

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
