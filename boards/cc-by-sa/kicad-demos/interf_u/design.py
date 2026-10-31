# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/interf_u@97acc80c223d75520c03fc44cab63cd9a3202c42 by Fenolite 0.7.0.dev0 on 2026-10-31;
# modified: format conversion to the Fenolite DSL.

import copper
from fenolite.dsl import Design, Net, Part, connect, mm, stack

design = Design("interf_u")

design.board(
    outline=(
        (mm("-20.625"), mm("-65.71")),
        (mm("94.945"), mm("-65.71")),
        (mm("94.945"), mm("33.35")),
        (mm("72.085"), mm("33.35")),
        (mm("72.085"), mm("42.494")),
        (mm("-9.195"), mm("42.494")),
        (mm("-9.195"), mm("40.97")),
        (mm("-9.195"), mm("33.35")),
        (mm("-20.625"), mm("33.35")),
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
design.title_block(title="Demo", revision="2.C", organization="Kicad")

net_8mh_out = Net("/8MH-OUT")
ack = Net("/ACK")
autofd = Net("/AUTOFD-")
bit0 = Net("/BIT0")
bit1 = Net("/BIT1")
bit2 = Net("/BIT2")
bit3 = Net("/BIT3")
bit4 = Net("/BIT4")
bit5 = Net("/BIT5")
bit6 = Net("/BIT6")
bit7 = Net("/BIT7")
bust = Net("/BUST+")
clklca = Net("/CLKLCA")
cs1 = Net("/CS1-")
d0 = Net("/D0")
d1 = Net("/D1")
d2 = Net("/D2")
d3 = Net("/D3")
d4 = Net("/D4")
d5 = Net("/D5")
d6 = Net("/D6")
d7 = Net("/D7")
dir = Net("/DIR")
done = Net("/DONE")
enbbuf = Net("/ENBBUF")
error = Net("/ERROR-")
init = Net("/INIT-")
led1 = Net("/LED1")
led2 = Net("/LED2")
ma0 = Net("/MA0")
ma1 = Net("/MA1")
ma10 = Net("/MA10")
ma11 = Net("/MA11")
ma12 = Net("/MA12")
ma13 = Net("/MA13")
ma14 = Net("/MA14")
ma15 = Net("/MA15")
ma16 = Net("/MA16")
ma2 = Net("/MA2")
ma3 = Net("/MA3")
ma4 = Net("/MA4")
ma5 = Net("/MA5")
ma6 = Net("/MA6")
ma7 = Net("/MA7")
ma8 = Net("/MA8")
ma9 = Net("/MA9")
matchl = Net("/MATCHL")
md0 = Net("/MD0")
md1 = Net("/MD1")
md2 = Net("/MD2")
md3 = Net("/MD3")
md4 = Net("/MD4")
md5 = Net("/MD5")
md6 = Net("/MD6")
md7 = Net("/MD7")
oe = Net("/OE-")
pc_a0 = Net("/PC-A0")
pc_a1 = Net("/PC-A1")
pc_a10 = Net("/PC-A10")
pc_a11 = Net("/PC-A11")
pc_a2 = Net("/PC-A2")
pc_a3 = Net("/PC-A3")
pc_a4 = Net("/PC-A4")
pc_a5 = Net("/PC-A5")
pc_a6 = Net("/PC-A6")
pc_a7 = Net("/PC-A7")
pc_a8 = Net("/PC-A8")
pc_a9 = Net("/PC-A9")
pc_aen = Net("/PC-AEN")
pc_db0 = Net("/PC-DB0")
pc_db1 = Net("/PC-DB1")
pc_db2 = Net("/PC-DB2")
pc_db3 = Net("/PC-DB3")
pc_db4 = Net("/PC-DB4")
pc_db5 = Net("/PC-DB5")
pc_db6 = Net("/PC-DB6")
pc_db7 = Net("/PC-DB7")
pc_ior = Net("/PC-IOR")
pc_iow = Net("/PC-IOW")
pc_rd = Net("/PC-RD")
pc_rst = Net("/PC-RST")
pc_wr = Net("/PC-WR")
pe = Net("/PE+")
prog = Net("/PROG-")
ref10 = Net("/REF10")
ref11 = Net("/REF11")
ref4 = Net("/REF4")
ref5 = Net("/REF5")
ref6 = Net("/REF6")
ref7 = Net("/REF7")
ref8 = Net("/REF8")
ref9 = Net("/REF9")
rstl = Net("/RSTL")
sel_lpt = Net("/SEL_LPT")
slct = Net("/SLCT+")
slctin = Net("/SLCTIN-")
strobe = Net("/STROBE")
wr = Net("/WR-")
wr_reg = Net("/WR_REG")
gnd = Net("GND")
net_c3_pad1 = Net("Net-(C3-Pad1)")
net_d1_a = Net("Net-(D1-A)")
net_d2_a = Net("Net-(D2-A)")
net_u3_y0 = Net("Net-(U3-Y0)")
net_u3_y1 = Net("Net-(U3-Y1)")
net_u3_y2 = Net("Net-(U3-Y2)")
net_u3_y3 = Net("Net-(U3-Y3)")
net_u5_cs2 = Net("Net-(U5-CS2)")
net_u9_p_a3 = Net("Net-(U9-P/A3)")
vcc = Net("VCC")

design.rules.netclass(
    "Power",
    clearance=mm("0.254"),
    track_width=mm("0.5"),
    via_diameter=mm("1.6"),
    via_drill=mm("0.6"),
    diff_pair_width=mm("0.2"),
    diff_pair_gap=mm("0.25"),
    diff_pair_via_gap=mm("0.25"),
    nets=(gnd, vcc),
)
design.rules.minimum(via_diameter=mm("0.9"), hole_size=mm("0.5"))

bus1 = Part("BUS1", "interf_u:BUS_PC", footprint="interf_u:BUS_PC", value="BUSPC")
c1 = Part(
    "C1",
    "interf_u:CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal",
    footprint="interf_u:CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal",
    value="47uF",
)
c2 = Part(
    "C2",
    "interf_u:C_Disc_D3.0mm_W2.0mm_P2.50mm",
    footprint="interf_u:C_Disc_D3.0mm_W2.0mm_P2.50mm",
    value="47pF",
)
c3 = Part(
    "C3",
    "interf_u:C_Disc_D3.0mm_W2.0mm_P2.50mm",
    footprint="interf_u:C_Disc_D3.0mm_W2.0mm_P2.50mm",
    value="47pF",
)
c4 = Part(
    "C4",
    "interf_u:CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal_2",
    footprint="interf_u:CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal_2",
    value="47uF",
)
c5 = Part(
    "C5",
    "interf_u:CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal_3",
    footprint="interf_u:CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal_3",
    value="47uF",
)
c6 = Part(
    "C6",
    "interf_u:CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal",
    footprint="interf_u:CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal",
    value="47uF",
)
d1_2 = Part("D1", "interf_u:LED_D5.0mm", footprint="interf_u:LED_D5.0mm", value="LED")
d2_2 = Part("D2", "interf_u:LED_D5.0mm_2", footprint="interf_u:LED_D5.0mm_2", value="LED")
g1 = Part("G1", "interf_u:tux", footprint="interf_u:tux", value="LOGO", board_only=True)
jp1 = Part(
    "JP1",
    "interf_u:PinHeader_2x08_P2.54mm_Vertical",
    footprint="interf_u:PinHeader_2x08_P2.54mm_Vertical",
    value="CONN_8X2",
)
p1 = Part(
    "P1",
    "interf_u:DSUB-25_Female_Horizontal_P2.77x2.84mm_EdgePinOffset9.90mm_Housed_MountingHolesOffset11.32mm",
    footprint="interf_u:DSUB-25_Female_Horizontal_P2.77x2.84mm_EdgePinOffset9.90mm_Housed_MountingHolesOffset11.32mm",
    value="DB25FEMELLE",
)
r1 = Part(
    "R1",
    "interf_u:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal",
    footprint="interf_u:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal",
    value="100K",
)
r2 = Part(
    "R2",
    "interf_u:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal_2",
    footprint="interf_u:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal_2",
    value="1K",
)
r3 = Part(
    "R3",
    "interf_u:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal_3",
    footprint="interf_u:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal_3",
    value="10K",
)
r4 = Part(
    "R4",
    "interf_u:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal_3",
    footprint="interf_u:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal_3",
    value="330",
)
r5 = Part(
    "R5",
    "interf_u:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal_4",
    footprint="interf_u:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal_4",
    value="330",
)
rr1 = Part("RR1", "interf_u:R_Array_SIP10", footprint="interf_u:R_Array_SIP10", value="9x1K")
u1 = Part("U1", "interf_u:DIP-20_W7.62mm", footprint="interf_u:DIP-20_W7.62mm", value="74LS245")
u2 = Part("U2", "interf_u:DIP-20_W7.62mm", footprint="interf_u:DIP-20_W7.62mm", value="74LS688")
u3 = Part("U3", "interf_u:DIP-20_W7.62mm", footprint="interf_u:DIP-20_W7.62mm", value="74LS541")
u5 = Part("U5", "interf_u:DIP-32_W15.24mm", footprint="interf_u:DIP-32_W15.24mm", value="628128")
u8 = Part("U8", "interf_u:DIP-24_W7.62mm", footprint="interf_u:DIP-24_W7.62mm", value="EP600")
u9 = Part("U9", "interf_u:PGA120", footprint="interf_u:PGA120", value="4003APG120")
x1 = Part(
    "X1",
    "interf_u:Crystal_HC18-U_Horizontal",
    footprint="interf_u:Crystal_HC18-U_Horizontal",
    value="8MHz",
)

design.add(
    bus1,
    c1,
    c2,
    c3,
    c4,
    c5,
    c6,
    d1_2,
    d2_2,
    g1,
    jp1,
    p1,
    r1,
    r2,
    r3,
    r4,
    r5,
    rr1,
    u1,
    u2,
    u3,
    u5,
    u8,
    u9,
    x1,
)

connect(net_8mh_out, r2["1"], u9["K1"])
connect(ack, p1["10"], u9["K13"])
connect(autofd, p1["14"], u9["C12"])
connect(bit0, p1["2"], u9["D12"])
connect(bit1, p1["3"], u9["E13"])
connect(bit2, p1["4"], u9["F12"])
connect(bit3, p1["5"], u9["G13"])
connect(bit4, p1["6"], u9["H13"])
connect(bit5, p1["7"], u9["H12"])
connect(bit6, p1["8"], u9["J13"])
connect(bit7, p1["9"], u9["H11"])
connect(bust, p1["11"], u9["J12"])
connect(clklca, u8["16"], u9["L4"], u9["M4"])
connect(cs1, u5["22"], u9["A10"])
connect(d0, u1["18"], u8["21"], u9["N2"])
connect(d1, u1["17"], u9["N8"])
connect(d2, u1["16"], u9["N9"])
connect(d3, u1["15"], u9["M9"])
connect(d4, u1["14"], u9["M10"])
connect(d5, u1["13"], u9["N11"])
connect(d6, u1["12"], u9["M11"])
connect(d7, u1["11"], u9["L12"])
connect(dir, u1["1"], u8["17"])
connect(done, u8["20"], u9["L11"])
connect(enbbuf, u1["19"], u8["22"])
connect(error, p1["15"], u9["D13"])
connect(init, p1["16"], u9["E12"])
connect(led1, r4["2"], u9["M3"])
connect(led2, r5["2"], u9["F13"])
connect(ma0, u5["12"], u9["A11"])
connect(ma1, u5["11"], u9["B2"])
connect(ma10, u5["23"], u9["C9"])
connect(ma11, u5["25"], u9["D2"])
connect(ma12, u5["4"], u9["F3"])
connect(ma13, u5["28"], u9["C1"])
connect(ma14, u5["3"], u9["D1"])
connect(ma15, u5["31"], u9["F1"])
connect(ma16, u5["2"], u9["C8"])
connect(ma2, u5["10"], u9["D3"])
connect(ma3, u5["9"], u9["C2"])
connect(ma4, u5["8"], u9["E1"])
connect(ma5, u5["7"], u9["C13"])
connect(ma6, u5["6"], u9["F2"])
connect(ma7, u5["5"], u9["B3"])
connect(ma8, u5["27"], u9["G1"])
connect(ma9, u5["26"], u9["A4"])
connect(matchl, u2["19"], u8["2"])
connect(md0, u5["13"], u9["C6"])
connect(md1, u5["14"], u9["A5"])
connect(md2, u5["15"], u9["B6"])
connect(md3, u5["17"], u9["A6"])
connect(md4, u5["18"], u9["A7"])
connect(md5, u5["19"], u9["A8"])
connect(md6, u5["20"], u9["A9"])
connect(md7, u5["21"], u9["B8"])
connect(oe, u5["24"], u9["B9"])
connect(pc_a0, bus1["62"], u3["3"], u9["M6"])
connect(pc_a1, bus1["61"], u3["2"], u9["N4"])
connect(pc_a10, bus1["52"], u2["11"], u9["L8"])
connect(pc_a11, bus1["51"], u2["8"])
connect(pc_a2, bus1["60"], u3["4"], u9["M5"])
connect(pc_a3, bus1["59"], u3["5"], u9["K2"])
connect(pc_a4, bus1["58"], u2["17"], u9["H3"])
connect(pc_a5, bus1["57"], u2["2"], u9["J2"])
connect(pc_a6, bus1["56"], u2["15"], u9["J1"])
connect(pc_a7, bus1["55"], u2["13"], u9["H2"])
connect(pc_a8, bus1["54"], u2["4"], u9["H1"])
connect(pc_a9, bus1["53"], u2["6"], u9["N7"])
connect(pc_aen, bus1["42"], u2["1"], u9["N10"])
connect(pc_db0, bus1["40"], u1["2"])
connect(pc_db1, bus1["39"], u1["3"])
connect(pc_db2, bus1["38"], u1["4"])
connect(pc_db3, bus1["37"], u1["5"])
connect(pc_db4, bus1["36"], u1["6"])
connect(pc_db5, bus1["35"], u1["7"])
connect(pc_db6, bus1["34"], u1["8"])
connect(pc_db7, bus1["33"], u1["9"])
connect(pc_ior, bus1["14"], u3["7"])
connect(pc_iow, bus1["13"], u3["6"])
connect(pc_rd, u3["13"], u8["14"], u9["M8"])
connect(pc_rst, bus1["2"], u3["8"], u3["9"])
connect(pc_wr, u3["14"], u8["7"], u9["N6"])
connect(pe, p1["12"], u9["L13"])
connect(prog, u8["19"], u9["M12"])
connect(ref10, jp1["2"], rr1["9"], u2["12"])
connect(ref11, jp1["4"], rr1["8"], u2["9"])
connect(ref4, jp1["14"], rr1["3"], u2["18"])
connect(ref5, jp1["16"], rr1["2"], u2["3"])
connect(ref6, jp1["10"], rr1["5"], u2["16"])
connect(ref7, jp1["6"], rr1["7"], u2["14"])
connect(ref8, jp1["12"], rr1["4"], u2["5"])
connect(ref9, jp1["8"], rr1["6"], u2["7"])
connect(rstl, u3["12"], u8["11"])
connect(sel_lpt, u8["18"], u9["L2"])
connect(slct, p1["13"], u9["N13"])
connect(slctin, p1["17"], u9["F11"])
connect(strobe, p1["1"], u9["A12"])
connect(wr, u5["29"], u9["A13"])
connect(wr_reg, u8["13"], u8["15"])
connect(
    gnd,
    bus1["1"],
    bus1["31"],
    c1["2"],
    c2["2"],
    c3["2"],
    c4["2"],
    c5["2"],
    c6["2"],
    d1_2["1"],
    d2_2["1"],
    jp1["1"],
    jp1["3"],
    jp1["5"],
    jp1["7"],
    jp1["9"],
    jp1["11"],
    jp1["13"],
    jp1["15"],
    p1["18"],
    p1["19"],
    p1["20"],
    p1["21"],
    p1["22"],
    p1["23"],
    p1["24"],
    p1["25"],
    u1["10"],
    u2["10"],
    u3["1"],
    u3["10"],
    u3["19"],
    u5["16"],
    u8["1"],
    u8["12"],
    u9["B7"],
    u9["C4"],
    u9["C10"],
    u9["G2"],
    u9["G11"],
    u9["K3"],
    u9["K11"],
    u9["L7"],
)
connect(net_c3_pad1, c3["1"], r1["1"], r2["2"], x1["2"])
connect(net_d1_a, d1_2["2"], r4["1"])
connect(net_d2_a, d2_2["2"], r5["1"])
connect(net_u3_y0, u3["18"], u8["3"])
connect(net_u3_y1, u3["17"], u8["4"])
connect(net_u3_y2, u3["16"], u8["5"])
connect(net_u3_y3, u3["15"], u8["6"])
connect(net_u5_cs2, r3["1"], u5["30"])
connect(net_u9_p_a3, c2["1"], r1["2"], u9["L1"], x1["1"])
connect(
    vcc,
    bus1["3"],
    bus1["29"],
    c1["1"],
    c4["1"],
    c5["1"],
    c6["1"],
    r3["2"],
    rr1["1"],
    u1["20"],
    u2["20"],
    u3["20"],
    u5["32"],
    u8["23"],
    u8["24"],
    u9["B11"],
    u9["B12"],
    u9["C3"],
    u9["C11"],
    u9["D11"],
    u9["G12"],
    u9["L3"],
    u9["L10"],
    u9["M7"],
)

bus1.place(mm("31.445"), mm("38.43"), locked=True)
c1.place(mm("-16.815"), mm("-16.18"))
c2.place(mm("21.305"), mm("-8.56"))
c3.place(mm("21.305"), mm("-0.94"))
c4.place(mm("70.688"), mm("-47.803"), rot=180)
c5.place(mm("-13.005"), mm("13.03"), rot=-90)
c6.place(mm("59.385"), mm("11.76"))
d1_2.place(mm("55.58"), mm("-61.94"))
d2_2.place(mm("65.71"), mm("-61.92"))
g1.place(mm("34"), mm("-53"))
jp1.place(mm("16.205"), mm("5.41"), rot=-90)
p1.place(mm("82.1"), mm("-27.6"), rot=90, locked=True)
r1.place(mm("17.475"), mm("-0.94"), rot=90)
r2.place(mm("27.635"), mm("-8.56"), rot=-90)
r3.place(mm("-7.925"), mm("-42.85"), rot=180)
r4.place(mm("51.765"), mm("-58.09"), rot=180)
r5.place(mm("71.958"), mm("-57.963"))
rr1.place(mm("-4.115"), mm("13.03"))
u1.place(mm("51.765"), mm("24.46"), rot=90)
u2.place(mm("-4.115"), mm("24.46"), rot=90)
u3.place(mm("23.825"), mm("24.46"), rot=90)
u5.place(mm("-13.005"), mm("-23.8"), rot=90)
u8.place(mm("23.825"), mm("12.903"), rot=90)
u9.place(mm("58.115"), mm("-17.45"), rot=180)
x1.place(mm("13.665"), mm("-7.29"), rot=-90)

design.zone(
    gnd,
    layers=("B.Cu",),
    key="GND/1",
    outline=(
        (mm("93.675"), mm("33.35")),
        (mm("93.675"), mm("-64.44")),
        (mm("-19.355"), mm("-64.44")),
        (mm("-19.355"), mm("33.35")),
    ),
    min_thickness=mm("0.2"),
    thermal_gap=mm("0.508"),
    thermal_spoke_width=mm("0.508"),
)

design.text(
    "B.Cu/text/1",
    "1",
    (mm("-15.545"), mm("-63.17")),
    layer="B.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)
design.text(
    "B.Cu/text/2",
    "V02",
    (mm("75.895"), mm("-61.9")),
    layer="B.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.381"),
)
design.text(
    "B.Cu/text/3",
    "INTERF_U",
    (mm("88.595"), mm("-54.28")),
    layer="B.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
    rot=90,
)
design.text(
    "F.Cu/text/1",
    "2",
    (mm("-18.085"), mm("-60.63")),
    layer="F.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)
design.text(
    "F.Cu/text/2",
    "V02",
    (mm("75.895"), mm("-61.9")),
    layer="F.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.381"),
)
design.text(
    "F.Cu/text/3",
    "INTERF_U",
    (mm("83.515"), mm("-54.28")),
    layer="F.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
    rot=90,
)
design.text(
    "F.SilkS/text/1",
    "V02",
    (mm("83.515"), mm("30.81")),
    layer="F.SilkS",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.381"),
)
design.text(
    "F.SilkS/text/2",
    "INTERF_U",
    (mm("84.785"), mm("27")),
    layer="F.SilkS",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.381"),
)
design.dimension(
    "Cmts.User/dimension/1",
    (mm("-20.625"), mm("33.35")),
    (mm("-20.625"), mm("-65.71")),
    offset=mm("-5.334"),
    layer="Cmts.User",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.20066"),
    width=mm("0.20066"),
    extension_offset=mm("0"),
)
design.dimension(
    "Cmts.User/dimension/2",
    (mm("94.945"), mm("-65.71")),
    (mm("-20.625"), mm("-65.71")),
    offset=mm("5.83946"),
    layer="Cmts.User",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.21082"),
    width=mm("0.21082"),
    extension_offset=mm("0"),
)

copper.apply(
    design,
    {
        "/8MH-OUT": net_8mh_out,
        "/ACK": ack,
        "/AUTOFD-": autofd,
        "/BIT0": bit0,
        "/BIT1": bit1,
        "/BIT2": bit2,
        "/BIT3": bit3,
        "/BIT4": bit4,
        "/BIT5": bit5,
        "/BIT6": bit6,
        "/BIT7": bit7,
        "/BUST+": bust,
        "/CLKLCA": clklca,
        "/CS1-": cs1,
        "/D0": d0,
        "/D1": d1,
        "/D2": d2,
        "/D3": d3,
        "/D4": d4,
        "/D5": d5,
        "/D6": d6,
        "/D7": d7,
        "/DIR": dir,
        "/DONE": done,
        "/ENBBUF": enbbuf,
        "/ERROR-": error,
        "/INIT-": init,
        "/LED1": led1,
        "/LED2": led2,
        "/MA0": ma0,
        "/MA1": ma1,
        "/MA10": ma10,
        "/MA11": ma11,
        "/MA12": ma12,
        "/MA13": ma13,
        "/MA14": ma14,
        "/MA15": ma15,
        "/MA16": ma16,
        "/MA2": ma2,
        "/MA3": ma3,
        "/MA4": ma4,
        "/MA5": ma5,
        "/MA6": ma6,
        "/MA7": ma7,
        "/MA8": ma8,
        "/MA9": ma9,
        "/MATCHL": matchl,
        "/MD0": md0,
        "/MD1": md1,
        "/MD2": md2,
        "/MD3": md3,
        "/MD4": md4,
        "/MD5": md5,
        "/MD6": md6,
        "/MD7": md7,
        "/OE-": oe,
        "/PC-A0": pc_a0,
        "/PC-A1": pc_a1,
        "/PC-A10": pc_a10,
        "/PC-A11": pc_a11,
        "/PC-A2": pc_a2,
        "/PC-A3": pc_a3,
        "/PC-A4": pc_a4,
        "/PC-A5": pc_a5,
        "/PC-A6": pc_a6,
        "/PC-A7": pc_a7,
        "/PC-A8": pc_a8,
        "/PC-A9": pc_a9,
        "/PC-AEN": pc_aen,
        "/PC-DB0": pc_db0,
        "/PC-DB1": pc_db1,
        "/PC-DB2": pc_db2,
        "/PC-DB3": pc_db3,
        "/PC-DB4": pc_db4,
        "/PC-DB5": pc_db5,
        "/PC-DB6": pc_db6,
        "/PC-DB7": pc_db7,
        "/PC-IOR": pc_ior,
        "/PC-IOW": pc_iow,
        "/PC-RD": pc_rd,
        "/PC-RST": pc_rst,
        "/PC-WR": pc_wr,
        "/PE+": pe,
        "/PROG-": prog,
        "/REF10": ref10,
        "/REF11": ref11,
        "/REF4": ref4,
        "/REF5": ref5,
        "/REF6": ref6,
        "/REF7": ref7,
        "/REF8": ref8,
        "/REF9": ref9,
        "/RSTL": rstl,
        "/SEL_LPT": sel_lpt,
        "/SLCT+": slct,
        "/SLCTIN-": slctin,
        "/STROBE": strobe,
        "/WR-": wr,
        "/WR_REG": wr_reg,
        "GND": gnd,
        "Net-(C3-Pad1)": net_c3_pad1,
        "Net-(D1-A)": net_d1_a,
        "Net-(D2-A)": net_d2_a,
        "Net-(U3-Y0)": net_u3_y0,
        "Net-(U3-Y1)": net_u3_y1,
        "Net-(U3-Y2)": net_u3_y2,
        "Net-(U3-Y3)": net_u3_y3,
        "Net-(U5-CS2)": net_u5_cs2,
        "Net-(U9-P/A3)": net_u9_p_a3,
        "VCC": vcc,
    },
)
