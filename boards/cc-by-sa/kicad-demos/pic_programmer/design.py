# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/pic_programmer@97acc80c223d75520c03fc44cab63cd9a3202c42 by Fenolite 0.7.0.dev0 on 2026-10-31;
# modified: format conversion to the Fenolite DSL.

import copper
from fenolite.dsl import Design, Module, Net, Part, connect, mm, stack

design = Design("pic_programmer")

design.board(
    outline=(
        (mm("-26.34"), mm("-59.36")),
        (mm("73.99"), mm("-59.36")),
        (mm("133.68"), mm("-59.36")),
        (mm("133.68"), mm("39.7")),
        (mm("-26.34"), mm("39.7")),
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
design.title_block(title="SERIAL PIC PROGRAMMER")

clock_rb6 = Net("/CLOCK-RB6")
data_rb7 = Net("/DATA-RB7")
pc_clock_out = Net("/PC-CLOCK-OUT")
pc_data_in = Net("/PC-DATA-IN")
pc_data_out = Net("/PC-DATA-OUT")
vpp_mclr = Net("/VPP/MCLR")
vpp_on = Net("/VPP_ON")
pic_sockets_vcc_pic = Net("/pic_sockets/VCC_PIC")
gnd = Net("GND")
net_c5_pad1 = Net("Net-(C5-Pad1)")
net_d1_a = Net("Net-(D1-A)")
net_d1_k = Net("Net-(D1-K)")
net_d10_a = Net("Net-(D10-A)")
net_d11_a = Net("Net-(D11-A)")
net_d11_k = Net("Net-(D11-K)")
net_d12_a = Net("Net-(D12-A)")
net_d2_a = Net("Net-(D2-A)")
net_d4_a = Net("Net-(D4-A)")
net_d6_a = Net("Net-(D6-A)")
net_d8_a = Net("Net-(D8-A)")
net_d9_a = Net("Net-(D9-A)")
net_q1_b = Net("Net-(Q1-B)")
net_q2_b = Net("Net-(Q2-B)")
net_q2_c = Net("Net-(Q2-C)")
net_q3_b = Net("Net-(Q3-B)")
net_r12_pad1 = Net("Net-(R12-Pad1)")
net_r13_pad1 = Net("Net-(R13-Pad1)")
net_r15_pad1 = Net("Net-(R15-Pad1)")
net_r16_pad1 = Net("Net-(R16-Pad1)")
net_r8_pad1 = Net("Net-(R8-Pad1)")
net_u4_fb = Net("Net-(U4-FB+)")
net_u4_vc = Net("Net-(U4-Vc)")
vcc = Net("VCC")
vpp = Net("VPP")

design.rules.netclass(
    "POWER",
    clearance=mm("0.28"),
    track_width=mm("0.8"),
    via_diameter=mm("1.6"),
    via_drill=mm("0.6"),
    diff_pair_width=mm("0.28"),
    diff_pair_gap=mm("0.28"),
    diff_pair_via_gap=mm("0.25"),
    nets=(gnd, vcc),
)
design.rules.minimum(
    track_width=mm("0.25"),
    via_diameter=mm("0.9"),
    hole_size=mm("0.5"),
    edge_clearance=mm("0.01"),
)

c1 = Part(
    "C1",
    "Capacitor_THT:CP_Axial_L18.0mm_D6.5mm_P25.00mm_Horizontal",
    footprint="Capacitor_THT:CP_Axial_L18.0mm_D6.5mm_P25.00mm_Horizontal",
    value="100µF",
)
c2 = Part(
    "C2",
    "Capacitor_THT:CP_Axial_L18.0mm_D6.5mm_P25.00mm_Horizontal_2",
    footprint="Capacitor_THT:CP_Axial_L18.0mm_D6.5mm_P25.00mm_Horizontal_2",
    value="220uF",
)
c3 = Part(
    "C3",
    "Capacitor_THT:C_Axial_L12.0mm_D6.5mm_P20.00mm_Horizontal",
    footprint="Capacitor_THT:C_Axial_L12.0mm_D6.5mm_P20.00mm_Horizontal",
    value="22uF/25V",
)
c4 = Part(
    "C4",
    "Capacitor_THT:C_Disc_D5.1mm_W3.2mm_P5.00mm",
    footprint="Capacitor_THT:C_Disc_D5.1mm_W3.2mm_P5.00mm",
    value="0",
)
c5 = Part(
    "C5",
    "Capacitor_THT:C_Disc_D5.1mm_W3.2mm_P5.00mm_2",
    footprint="Capacitor_THT:C_Disc_D5.1mm_W3.2mm_P5.00mm_2",
    value="10nF",
)
c9 = Part(
    "C9",
    "Capacitor_THT:C_Disc_D5.1mm_W3.2mm_P5.00mm_2",
    footprint="Capacitor_THT:C_Disc_D5.1mm_W3.2mm_P5.00mm_2",
    value="220nF",
)
d1 = Part(
    "D1",
    "Diode_THT:D_DO-35_SOD27_P12.70mm_Horizontal",
    footprint="Diode_THT:D_DO-35_SOD27_P12.70mm_Horizontal",
    value="1N4004",
)
d2 = Part(
    "D2",
    "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal_2",
    footprint="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal_2",
    value="BAT43",
)
d3 = Part(
    "D3",
    "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal_3",
    footprint="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal_3",
    value="BAT43",
)
d4 = Part(
    "D4",
    "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal_4",
    footprint="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal_4",
    value="BAT43",
)
d5 = Part(
    "D5",
    "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal_5",
    footprint="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal_5",
    value="BAT43",
)
d6 = Part(
    "D6",
    "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal_4",
    footprint="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal_4",
    value="BAT43",
)
d7 = Part(
    "D7",
    "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal_6",
    footprint="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal_6",
    value="BAT43",
)
d8 = Part("D8", "LED_THT:LED_D5.0mm_2", footprint="LED_THT:LED_D5.0mm_2", value="RED-LED")
d9 = Part("D9", "LED_THT:LED_D5.0mm_2", footprint="LED_THT:LED_D5.0mm_2", value="GREEN-LED")
d10 = Part(
    "D10",
    "Diode_THT:D_DO-35_SOD27_P12.70mm_Horizontal_2",
    footprint="Diode_THT:D_DO-35_SOD27_P12.70mm_Horizontal_2",
    value="SCHOTTKY",
)
d11 = Part(
    "D11",
    "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal",
    footprint="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal",
    value="BAT43",
)
d12 = Part("D12", "LED_THT:LED_D5.0mm", footprint="LED_THT:LED_D5.0mm", value="YELLOW-LED")
j1 = Part(
    "J1",
    "Connector_Dsub:DSUB-9_Socket_Horizontal_P2.77x2.84mm_EdgePinOffset7.70mm_Housed_MountingHolesOffset9.12mm",
    footprint="Connector_Dsub:DSUB-9_Socket_Horizontal_P2.77x2.84mm_EdgePinOffset7.70mm_Housed_MountingHolesOffset9.12mm",
    value="DB9-FEMAL",
)
jp1 = Part(
    "JP1",
    "Jumper:SolderJumper-2_P1.3mm_Open_TrianglePad1.0x1.5mm",
    footprint="Jumper:SolderJumper-2_P1.3mm_Open_TrianglePad1.0x1.5mm",
    value="JUMPER",
)
l1 = Part(
    "L1",
    "Inductor_THT:L_Radial_D7.8mm_P5.00mm_Fastron_07HCP",
    footprint="Inductor_THT:L_Radial_D7.8mm_P5.00mm_Fastron_07HCP",
    value="22uH",
)
p1 = Part(
    "P1",
    "TerminalBlock_Altech:Altech_AK300_1x02_P5.00mm_45-Degree",
    footprint="TerminalBlock_Altech:Altech_AK300_1x02_P5.00mm_45-Degree",
    value="CONN_2",
)
p101 = Part(
    "P101",
    "MountingHole:MountingHole_4.3mm_M4",
    footprint="MountingHole:MountingHole_4.3mm_M4",
    value="CONN_1",
)
p102 = Part(
    "P102",
    "MountingHole:MountingHole_4.3mm_M4_2",
    footprint="MountingHole:MountingHole_4.3mm_M4_2",
    value="CONN_1",
)
p103 = Part(
    "P103",
    "MountingHole:MountingHole_4.3mm_M4_2",
    footprint="MountingHole:MountingHole_4.3mm_M4_2",
    value="CONN_1",
)
p104 = Part(
    "P104",
    "MountingHole:MountingHole_4.3mm_M4_2",
    footprint="MountingHole:MountingHole_4.3mm_M4_2",
    value="CONN_1",
)
p105 = Part(
    "P105",
    "MountingHole:MountingHole_4.3mm_M4_2",
    footprint="MountingHole:MountingHole_4.3mm_M4_2",
    value="CONN_1",
)
p106 = Part(
    "P106",
    "MountingHole:MountingHole_4.3mm_M4_2",
    footprint="MountingHole:MountingHole_4.3mm_M4_2",
    value="CONN_1",
)
q1 = Part("Q1", "footprints:TO-92", footprint="footprints:TO-92", value="BC237")
q2 = Part("Q2", "footprints:TO-92_2", footprint="footprints:TO-92_2", value="BC307")
q3 = Part("Q3", "footprints:TO-92", footprint="footprints:TO-92", value="BC307")
r1 = Part(
    "R1",
    "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
    value="10K",
)
r2 = Part(
    "R2",
    "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_11",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_11",
    value="10K",
)
r3 = Part(
    "R3",
    "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_12",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_12",
    value="10K",
)
r4 = Part(
    "R4",
    "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_2",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_2",
    value="10K",
)
r5 = Part(
    "R5",
    "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_13",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_13",
    value="10K",
)
r6 = Part(
    "R6",
    "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_12",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_12",
    value="10K",
)
r7 = Part(
    "R7",
    "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_14",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_14",
    value="10K",
)
r8 = Part(
    "R8",
    "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_15",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_15",
    value="1K",
)
r9 = Part(
    "R9",
    "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_2",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_2",
    value="2.2K",
)
r10 = Part(
    "R10",
    "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_2",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_2",
    value="5,1K",
)
r11 = Part(
    "R11",
    "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_3",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_3",
    value="22K",
)
r12 = Part(
    "R12",
    "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_4",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_4",
    value="470",
)
r13 = Part(
    "R13",
    "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_5",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_5",
    value="470",
)
r14 = Part(
    "R14",
    "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_6",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_6",
    value="470",
)
r15 = Part(
    "R15",
    "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_7",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_7",
    value="6.2K",
)
r16 = Part(
    "R16",
    "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_2",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_2",
    value="62K",
)
r17 = Part(
    "R17",
    "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_8",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_8",
    value="22K",
)
r18 = Part(
    "R18",
    "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_9",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_9",
    value="220",
)
r19 = Part(
    "R19",
    "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_10",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_10",
    value="2.2K",
)
r20 = Part(
    "R20",
    "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_4",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_4",
    value="2.2K",
)
r21 = Part(
    "R21",
    "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_4",
    footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_4",
    value="470",
)
rv1 = Part("RV1", "footprints:RV2X4", footprint="footprints:RV2X4", value="1K")
u2 = Part(
    "U2",
    "Package_DIP:DIP-14_W7.62mm_LongPads",
    footprint="Package_DIP:DIP-14_W7.62mm_LongPads",
    value="74HC125",
)
u3 = Part(
    "U3",
    "Package_TO_SOT_THT:TO-220-3_Horizontal_TabDown",
    footprint="Package_TO_SOT_THT:TO-220-3_Horizontal_TabDown",
    value="7805",
)
u4 = Part(
    "U4",
    "Package_DIP:DIP-8_W7.62mm_LongPads",
    footprint="Package_DIP:DIP-8_W7.62mm_LongPads",
    value="LT1373",
)
c6 = Part(
    "C6",
    "Capacitor_THT:C_Disc_D5.1mm_W3.2mm_P5.00mm_3",
    footprint="Capacitor_THT:C_Disc_D5.1mm_W3.2mm_P5.00mm_3",
    value="100nF",
)
c7 = Part(
    "C7",
    "Capacitor_THT:C_Disc_D5.1mm_W3.2mm_P5.00mm_3",
    footprint="Capacitor_THT:C_Disc_D5.1mm_W3.2mm_P5.00mm_3",
    value="100nF",
)
p2 = Part(
    "P2",
    "Package_DIP:DIP-28_W7.62mm_Socket_LongPads",
    footprint="Package_DIP:DIP-28_W7.62mm_Socket_LongPads",
    value="SUPP28",
)
p3 = Part("P3", "footprints:40tex-Ell600", footprint="footprints:40tex-Ell600", value="SUPP40")
u1 = Part(
    "U1",
    "Package_DIP:DIP-8_W7.62mm_Socket_LongPads",
    footprint="Package_DIP:DIP-8_W7.62mm_Socket_LongPads",
    value="24Cxx",
)
u5 = Part(
    "U5",
    "Package_DIP:DIP-18_W7.62mm_Socket_LongPads",
    footprint="Package_DIP:DIP-18_W7.62mm_Socket_LongPads",
    value="PIC_18_PINS",
)
u6 = Part(
    "U6",
    "Package_DIP:DIP-8_W7.62mm_Socket_LongPads_2",
    footprint="Package_DIP:DIP-8_W7.62mm_Socket_LongPads_2",
    value="PIC_8_PINS",
)

pic_sockets = Module("pic_sockets")

pic_sockets.add(c6, c7, p2, p3, u1, u5, u6)
design.add(
    c1,
    c2,
    c3,
    c4,
    c5,
    c9,
    d1,
    d2,
    d3,
    d4,
    d5,
    d6,
    d7,
    d8,
    d9,
    d10,
    d11,
    d12,
    j1,
    jp1,
    l1,
    p1,
    p101,
    p102,
    p103,
    p104,
    p105,
    p106,
    q1,
    q2,
    q3,
    r1,
    r2,
    r3,
    r4,
    r5,
    r6,
    r7,
    r8,
    r9,
    r10,
    r11,
    r12,
    r13,
    r14,
    r15,
    r16,
    r17,
    r18,
    r19,
    r20,
    r21,
    rv1,
    u2,
    u3,
    u4,
    pic_sockets,
)

connect(clock_rb6, p2["27"], p3["39"], r13["2"], u1["6"], u5["12"], u6["6"])
connect(data_rb7, p2["28"], p3["40"], r12["2"], u1["5"], u2["12"], u5["13"], u6["7"])
connect(pc_clock_out, j1["7"], r5["1"], r6["1"])
connect(pc_data_in, j1["8"], u2["11"])
connect(pc_data_out, j1["4"], r3["1"], r4["1"])
connect(vpp_mclr, p2["1"], p3["1"], r18["2"], u5["4"], u6["4"])
connect(vpp_on, j1["3"], r1["1"], r2["1"])
connect(
    pic_sockets_vcc_pic,
    c6["1"],
    c7["1"],
    jp1["2"],
    p2["20"],
    p3["11"],
    p3["32"],
    q3["1"],
    r21["2"],
    u1["8"],
    u5["14"],
    u6["1"],
)
connect(
    gnd,
    c1["2"],
    c2["2"],
    c3["2"],
    c4["2"],
    c5["2"],
    c6["2"],
    c7["2"],
    d3["2"],
    d5["2"],
    d7["2"],
    d8["1"],
    d9["1"],
    d12["1"],
    j1["5"],
    p1["1"],
    p2["8"],
    p2["19"],
    p3["8"],
    p3["12"],
    p3["31"],
    q1["3"],
    r2["2"],
    r4["2"],
    r6["2"],
    r15["2"],
    r17["2"],
    u1["1"],
    u1["2"],
    u1["3"],
    u1["4"],
    u2["1"],
    u2["4"],
    u2["7"],
    u2["10"],
    u2["13"],
    u3["2"],
    u4["6"],
    u4["7"],
    u5["5"],
    u6["8"],
)
connect(net_c5_pad1, c5["1"], r10["2"])
connect(net_d1_a, d1["2"], p1["2"])
connect(net_d1_k, c2["1"], d1["1"], u3["1"])
connect(net_d10_a, d10["2"], l1["1"], u4["8"])
connect(net_d11_a, d11["2"], r19["1"])
connect(net_d11_k, d11["1"], q1["1"], r11["1"])
connect(net_d12_a, d12["2"], r21["1"])
connect(net_d2_a, d2["2"], d3["1"], r1["2"], u2["2"])
connect(net_d4_a, d4["2"], d5["1"], r3["2"], u2["5"])
connect(net_d6_a, d6["2"], d7["1"], r5["2"], u2["9"])
connect(net_d8_a, d8["2"], r9["2"])
connect(net_d9_a, d9["2"], r14["2"])
connect(net_q1_b, q1["2"], r8["2"])
connect(net_q2_b, c9["2"], q2["2"], r7["2"], r11["2"])
connect(net_q2_c, q2["1"], r9["1"], r17["1"], r18["1"])
connect(net_q3_b, q3["2"], r19["2"], r20["2"])
connect(net_r12_pad1, r12["1"], u2["6"])
connect(net_r13_pad1, r13["1"], u2["8"])
connect(net_r15_pad1, r15["1"], rv1["1"])
connect(net_r16_pad1, r16["1"], rv1["3"])
connect(net_r8_pad1, r8["1"], u2["3"])
connect(net_u4_fb, rv1["2"], u4["2"])
connect(net_u4_vc, c4["1"], r10["1"], u4["1"])
connect(
    vcc,
    c1["1"],
    d2["1"],
    d4["1"],
    d6["1"],
    jp1["1"],
    l1["2"],
    q3["3"],
    r14["1"],
    r20["1"],
    u2["14"],
    u3["3"],
    u4["5"],
)
connect(vpp, c3["1"], c9["1"], d10["1"], q2["3"], r7["1"], r16["2"])

c1.place(mm("10.49"), mm("-21.133"), rot=180)
c2.place(mm("-15.418"), mm("-9.83"))
c3.place(mm("34.112"), mm("-37.77"), rot=-90)
c4.place(mm("14.3"), mm("-47.93"))
c5.place(mm("29.54"), mm("-50.47"))
c9.place(mm("43.002"), mm("-50.216"))
d1.place(mm("-21.7"), mm("-10.3"), rot=90)
d2.place(mm("7.95"), mm("18.237"), rot=180)
d3.place(mm("7.95"), mm("21.92"), rot=180)
d4.place(mm("7.95"), mm("11.887"), rot=180)
d5.place(mm("7.95"), mm("8.585"), rot=180)
d6.place(mm("7.95"), mm("25.095"), rot=180)
d7.place(mm("7.95"), mm("15.316"), rot=180)
d8.place(mm("56.21"), mm("-22.53"), rot=180)
d9.place(mm("56.21"), mm("-12.37"), rot=180)
d10.place(mm("37.16"), mm("-42.85"), rot=180)
d11.place(mm("39.065"), mm("-19.355"))
d12.place(mm("56.21"), mm("-2.845"), rot=180)
j1.place(mm("-17.4"), mm("20.2"), rot=-90)
jp1.place(mm("48.082"), mm("-2.21"), side="bottom")
l1.place(mm("25.73"), mm("-37.77"), rot=-90)
p1.place(mm("-18.2"), mm("-40"), rot=-90)
p101.place(mm("-22.53"), mm("35.89"))
p102.place(mm("58.75"), mm("35.89"))
p103.place(mm("129.87"), mm("35.89"))
p104.place(mm("129.87"), mm("-55.55"))
p105.place(mm("58.75"), mm("-55.55"))
p106.place(mm("-22.53"), mm("-55.55"))
q1.place(mm("46.05"), mm("-30.15"))
q2.place(mm("48.082"), mm("-39.294"), rot=180)
q3.place(mm("42.24"), mm("-2.21"))
r1.place(mm("-12.37"), mm("18.11"))
r2.place(mm("-12.37"), mm("14.554"))
r3.place(mm("-12.37"), mm("11.125"))
r4.place(mm("-12.37"), mm("7.823"))
r5.place(mm("-12.243"), mm("25.476"))
r6.place(mm("-12.243"), mm("21.92"))
r7.place(mm("39.7"), mm("-45.39"))
r8.place(mm("39.065"), mm("-8.941"))
r9.place(mm("39.065"), mm("-22.53"))
r10.place(mm("14.3"), mm("-51.74"))
r11.place(mm("40.081"), mm("-29.007"), rot=90)
r12.place(mm("35.255"), mm("21.92"), rot=90)
r13.place(mm("40.335"), mm("11.76"), rot=-90)
r14.place(mm("39.065"), mm("-12.37"))
r15.place(mm("18.11"), mm("-21.26"))
r16.place(mm("18.11"), mm("-24.816"))
r17.place(mm("56.21"), mm("-31.42"), rot=90)
r18.place(mm("52.4"), mm("-31.42"), rot=90)
r19.place(mm("49.225"), mm("-16.18"), rot=180)
r20.place(mm("44.78"), mm("2.235"), rot=180)
r21.place(mm("58.115"), mm("2.235"), rot=180)
rv1.place(mm("27.635"), mm("-9.195"), rot=180)
u2.place(mm("15.57"), mm("19.38"), rot=90)
u3.place(mm("-3.48"), mm("-28.88"))
u4.place(mm("10.49"), mm("-42.85"))
c6.place(mm("96.85"), mm("12.395"), rot=-90)
c7.place(mm("98.755"), mm("-28.88"), rot=-90)
p2.place(mm("107.645"), mm("-49.2"))
p3.place(mm("75.26"), mm("-49.2"))
u1.place(mm("79.07"), mm("9.22"))
u5.place(mm("107.899"), mm("7.95"))
u6.place(mm("79.07"), mm("20.65"))

design.zone(
    gnd,
    layers=("B.Cu",),
    key="GND/1",
    outline=(
        (mm("123.52"), mm("38.43")),
        (mm("132.41"), mm("28.905")),
        (mm("132.41"), mm("-46.025")),
        (mm("119.71"), mm("-58.09")),
        (mm("-18.72"), mm("-58.09")),
        (mm("-25.705"), mm("-51.105")),
        (mm("-25.705"), mm("27.635")),
        (mm("-13.64"), mm("38.43")),
    ),
    clearance=mm("0.508"),
    min_thickness=mm("0.3"),
    thermal_gap=mm("0.508"),
    thermal_spoke_width=mm("0.635"),
)

design.text(
    "B.Cu/text/1",
    "J-P CHARRAS",
    (mm("-5.385"), mm("37.16")),
    layer="B.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)
design.text(
    "B.Cu/text/2",
    "PIC PROGRAMMER V03",
    (mm("24.46"), mm("34.62")),
    layer="B.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)
design.text(
    "F.Cu/text/1",
    "+8/12V",
    (mm("-18.5"), mm("-44.5")),
    layer="F.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)
design.text(
    "F.Cu/text/2",
    "JP-CHARRAS",
    (mm("-5.385"), mm("37.16")),
    layer="F.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)
design.text(
    "F.Cu/text/3",
    "13V ADJUST",
    (mm("23.19"), mm("-4.75")),
    layer="F.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)
design.text(
    "F.Cu/text/4",
    "PIC PROGRAMMER V03",
    (mm("25.095"), mm("32.08")),
    layer="F.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)
design.text(
    "F.Cu/text/5",
    "VCC ON",
    (mm("62.9"), mm("-0.9")),
    layer="F.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)
design.text(
    "F.Cu/text/6",
    "VPP ON",
    (mm("63.195"), mm("-19.355")),
    layer="F.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)
design.text(
    "F.Cu/text/7",
    "PWR ON",
    (mm("63.83"), mm("-11.1")),
    layer="F.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)
design.text(
    "F.Cu/text/8",
    "I2C PROM",
    (mm("66.37"), mm("14.3")),
    layer="F.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)
design.text(
    "F.Cu/text/9",
    "1=>>",
    (mm("67.64"), mm("-51.105")),
    layer="F.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)
design.text(
    "F.Cu/text/10",
    "1=>>",
    (mm("71.45"), mm("9.22")),
    layer="F.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)
design.text(
    "F.Cu/text/11",
    "1=>>",
    (mm("71.45"), mm("20.65")),
    layer="F.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)
design.text(
    "F.Cu/text/12",
    "PIC 40 PINS",
    (mm("82.245"), mm("-54.915")),
    layer="F.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)
design.text(
    "F.Cu/text/13",
    "PIC 8 PINS",
    (mm("83.515"), mm("32.08")),
    layer="F.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)
design.text(
    "F.Cu/text/14",
    "1=>>",
    (mm("100.66"), mm("7.95")),
    layer="F.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)
design.text(
    "F.Cu/text/15",
    "1=>>",
    (mm("102"), mm("-51.3")),
    layer="F.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)
design.text(
    "F.Cu/text/16",
    "PIC 18 PINS",
    (mm("111.455"), mm("32.715")),
    layer="F.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)
design.text(
    "F.Cu/text/17",
    "PIC 28 PINS",
    (mm("112.725"), mm("-54.915")),
    layer="F.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)

copper.apply(
    design,
    {
        "/CLOCK-RB6": clock_rb6,
        "/DATA-RB7": data_rb7,
        "/PC-CLOCK-OUT": pc_clock_out,
        "/PC-DATA-IN": pc_data_in,
        "/PC-DATA-OUT": pc_data_out,
        "/VPP/MCLR": vpp_mclr,
        "/VPP_ON": vpp_on,
        "/pic_sockets/VCC_PIC": pic_sockets_vcc_pic,
        "GND": gnd,
        "Net-(C5-Pad1)": net_c5_pad1,
        "Net-(D1-A)": net_d1_a,
        "Net-(D1-K)": net_d1_k,
        "Net-(D10-A)": net_d10_a,
        "Net-(D11-A)": net_d11_a,
        "Net-(D11-K)": net_d11_k,
        "Net-(D12-A)": net_d12_a,
        "Net-(D2-A)": net_d2_a,
        "Net-(D4-A)": net_d4_a,
        "Net-(D6-A)": net_d6_a,
        "Net-(D8-A)": net_d8_a,
        "Net-(D9-A)": net_d9_a,
        "Net-(Q1-B)": net_q1_b,
        "Net-(Q2-B)": net_q2_b,
        "Net-(Q2-C)": net_q2_c,
        "Net-(Q3-B)": net_q3_b,
        "Net-(R12-Pad1)": net_r12_pad1,
        "Net-(R13-Pad1)": net_r13_pad1,
        "Net-(R15-Pad1)": net_r15_pad1,
        "Net-(R16-Pad1)": net_r16_pad1,
        "Net-(R8-Pad1)": net_r8_pad1,
        "Net-(U4-FB+)": net_u4_fb,
        "Net-(U4-Vc)": net_u4_vc,
        "VCC": vcc,
        "VPP": vpp,
    },
)
