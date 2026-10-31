# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/sonde%20xilinx@97acc80c223d75520c03fc44cab63cd9a3202c42 by Fenolite 0.7.0.dev0 on 2026-10-31;
# modified: format conversion to the Fenolite DSL.

import copper
from fenolite.dsl import Design, Module, Net, Part, connect, mm, stack

design = Design("sonde_xilinx")

design.board(
    outline=(
        (mm("3.3"), mm("-32.69")),
        (mm("83.7"), mm("-32.69")),
        (mm("83.7"), mm("10.49")),
        (mm("3.3"), mm("10.49")),
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
    finish="Immersion tin",
)
design.title_block(revision="1", organization="Kicad Demo")

clk_d1 = Net("/CLK-D1")
ctrl_d3 = Net("/CTRL-D3")
done_select = Net("/DONE-SELECT*")
pwr_3_3_5v = Net("/PWR_3,3-5V")
tck_cclk = Net("/TCK-CCLK")
td0_done = Net("/TD0-DONE")
td0_prog_d4 = Net("/TD0-PROG-D4")
tdi_din = Net("/TDI-DIN")
tdi_din_d0 = Net("/TDI-DIN-D0")
tms_prog = Net("/TMS-PROG")
tms_prog_d2 = Net("/TMS-PROG-D2")
vcc_sense_error = Net("/VCC_SENSE-ERROR*")
gnd = Net("GND")
net_d1_k = Net("Net-(D1-K)")
net_j1_pad11 = Net("Net-(J1-Pad11)")
net_u1a_e = Net("Net-(U1A-E)")
net_u1a_o = Net("Net-(U1A-O)")
net_u1b_d = Net("Net-(U1B-D)")
net_u1b_e = Net("Net-(U1B-E)")
net_u1b_o = Net("Net-(U1B-O)")
net_u1c_d = Net("Net-(U1C-D)")
net_u1c_o = Net("Net-(U1C-O)")
net_u1d_d = Net("Net-(U1D-D)")
net_u1d_o = Net("Net-(U1D-O)")
net_u2a_o = Net("Net-(U2A-O)")
vcc = Net("VCC")

design.rules.minimum(
    track_width=mm("0.2032"),
    via_diameter=mm("0.889"),
    hole_size=mm("0.508"),
    edge_clearance=mm("0.01"),
)

c1 = Part(
    "C1",
    "sonde-xilinx:C_Axial_L5.1mm_D3.1mm_P12.50mm_Horizontal",
    footprint="sonde-xilinx:C_Axial_L5.1mm_D3.1mm_P12.50mm_Horizontal",
    value="1uF",
)
c2 = Part(
    "C2",
    "sonde-xilinx:C_Disc_D5.1mm_W3.2mm_P5.00mm",
    footprint="sonde-xilinx:C_Disc_D5.1mm_W3.2mm_P5.00mm",
    value="100pF",
)
c3 = Part(
    "C3",
    "sonde-xilinx:C_Disc_D5.1mm_W3.2mm_P5.00mm_2",
    footprint="sonde-xilinx:C_Disc_D5.1mm_W3.2mm_P5.00mm_2",
    value="100pF",
)
c4 = Part(
    "C4",
    "sonde-xilinx:C_Disc_D5.1mm_W3.2mm_P5.00mm_3",
    footprint="sonde-xilinx:C_Disc_D5.1mm_W3.2mm_P5.00mm_3",
    value="100pF",
)
c5 = Part(
    "C5",
    "sonde-xilinx:C_Disc_D5.1mm_W3.2mm_P5.00mm_4",
    footprint="sonde-xilinx:C_Disc_D5.1mm_W3.2mm_P5.00mm_4",
    value="100pF",
)
d1 = Part(
    "D1",
    "sonde-xilinx:D_A-405_P7.62mm_Horizontal",
    footprint="sonde-xilinx:D_A-405_P7.62mm_Horizontal",
    value="BAT46",
)
d2 = Part(
    "D2",
    "sonde-xilinx:D_A-405_P7.62mm_Horizontal_2",
    footprint="sonde-xilinx:D_A-405_P7.62mm_Horizontal_2",
    value="BAT46",
)
j1 = Part(
    "J1",
    "sonde-xilinx:DSUB-25_Male_EdgeMount_P2.77mm",
    footprint="sonde-xilinx:DSUB-25_Male_EdgeMount_P2.77mm",
    value="DB25MALE",
)
j2 = Part(
    "J2",
    "sonde-xilinx:DSUB-9_Male_EdgeMount_P2.77mm",
    footprint="sonde-xilinx:DSUB-9_Male_EdgeMount_P2.77mm",
    value="DB9MALE",
)
p1 = Part(
    "P1",
    "sonde-xilinx:PinHeader_1x06_P2.54mm_Vertical",
    footprint="sonde-xilinx:PinHeader_1x06_P2.54mm_Vertical",
    value="CONN_6",
)
r1 = Part(
    "R1",
    "sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
    footprint="sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
    value="100",
)
r2 = Part(
    "R2",
    "sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_4",
    footprint="sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_4",
    value="5,1K",
)
r4 = Part(
    "R4",
    "sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_3",
    footprint="sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_3",
    value="47",
)
r5 = Part(
    "R5",
    "sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_5",
    footprint="sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_5",
    value="1K",
)
r6 = Part(
    "R6",
    "sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_6",
    footprint="sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_6",
    value="100",
)
r7 = Part(
    "R7",
    "sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_7",
    footprint="sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_7",
    value="100",
)
r8 = Part(
    "R8",
    "sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_8",
    footprint="sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_8",
    value="100",
)
r9 = Part(
    "R9",
    "sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_9",
    footprint="sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_9",
    value="100",
)
r10 = Part(
    "R10",
    "sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_2",
    footprint="sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_2",
    value="100",
)
r11 = Part(
    "R11",
    "sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_3",
    footprint="sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_3",
    value="100",
)
r12 = Part(
    "R12",
    "sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_3",
    footprint="sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_3",
    value="100",
)
r13 = Part(
    "R13",
    "sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_3",
    footprint="sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_3",
    value="100",
)
r14 = Part(
    "R14",
    "sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_3",
    footprint="sonde-xilinx:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal_3",
    value="100",
)
u1 = Part(
    "U1",
    "sonde-xilinx:DIP-14_W7.62mm_LongPads",
    footprint="sonde-xilinx:DIP-14_W7.62mm_LongPads",
    value="74LS125",
)
u2 = Part(
    "U2",
    "sonde-xilinx:DIP-14_W7.62mm_LongPads",
    footprint="sonde-xilinx:DIP-14_W7.62mm_LongPads",
    value="74LS125",
)

racine = Module("racine")

racine.add(
    c1,
    c2,
    c3,
    c4,
    c5,
    d1,
    d2,
    j1,
    j2,
    p1,
    r1,
    r2,
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
    u1,
    u2,
)
design.add(racine)

connect(clk_d1, j1["3"], r10["2"])
connect(ctrl_d3, j1["5"], r8["2"])
connect(done_select, j1["13"], r4["2"])
connect(pwr_3_3_5v, d2["1"], j2["1"], p1["1"])
connect(tck_cclk, j2["4"], p1["5"], r12["1"])
connect(td0_done, j2["2"], p1["3"], r14["1"])
connect(td0_prog_d4, j1["6"], r6["2"])
connect(tdi_din, j2["3"], p1["4"], r11["1"])
connect(tdi_din_d0, j1["2"], r7["2"])
connect(tms_prog, j2["5"], p1["6"], r13["1"])
connect(tms_prog_d2, j1["4"], r9["2"])
connect(vcc_sense_error, j1["15"], r1["2"])
connect(
    gnd,
    c1["2"],
    c2["2"],
    c3["2"],
    c4["2"],
    c5["2"],
    j1["20"],
    j1["25"],
    j2["6"],
    j2["7"],
    j2["8"],
    j2["9"],
    p1["2"],
    r5["2"],
    u1["2"],
    u1["7"],
    u2["1"],
    u2["4"],
    u2["5"],
    u2["7"],
    u2["9"],
    u2["10"],
    u2["12"],
    u2["13"],
)
connect(net_d1_k, d1["2"], r1["1"])
connect(net_j1_pad11, j1["8"], j1["11"], j1["12"])
connect(net_u1a_e, r6["1"], u1["1"])
connect(net_u1a_o, c3["1"], r2["2"], r14["2"], u1["3"], u2["2"])
connect(net_u1b_d, r7["1"], u1["5"])
connect(net_u1b_e, r8["1"], u1["4"], u1["10"], u1["13"])
connect(net_u1b_o, c2["1"], r11["2"], u1["6"])
connect(net_u1c_d, r10["1"], u1["9"])
connect(net_u1c_o, c5["1"], r12["2"], u1["8"])
connect(net_u1d_d, r9["1"], u1["12"])
connect(net_u1d_o, c4["1"], r13["2"], u1["11"])
connect(net_u2a_o, r4["1"], u2["3"])
connect(vcc, c1["1"], d1["1"], d2["2"], r2["1"], r5["1"], u1["14"], u2["14"])

c1.place(mm("34.62"), mm("-23.8"))
c2.place(mm("40.97"), mm("2.87"), rot=-90)
c3.place(mm("51.13"), mm("-30.15"))
c4.place(mm("49"), mm("2.87"), rot=-90)
c5.place(mm("45"), mm("2.87"), rot=-90)
d1.place(mm("34.62"), mm("-27.61"), rot=180)
d2.place(mm("60.02"), mm("-21.26"), rot=180)
j1.place(mm("5.5116"), mm("-10.8968"), rot=-90)
j2.place(mm("81.61"), mm("-9.8808"), rot=-90, side="bottom")
p1.place(mm("69.672"), mm("-19.863"))
r1.place(mm("21.92"), mm("-26.1368"), rot=180)
r2.place(mm("37.16"), mm("-27.61"))
r4.place(mm("21.92"), mm("4.14"), rot=180)
r5.place(mm("51.13"), mm("-26.34"))
r6.place(mm("21.9327"), mm("-16.18"), rot=180)
r7.place(mm("21.92"), mm("-7.29"), rot=180)
r8.place(mm("21.92"), mm("-12.37"), rot=180)
r9.place(mm("21.92"), mm("-19.482"), rot=180)
r10.place(mm("21.92"), mm("-22.784"), rot=180)
r11.place(mm("62.56"), mm("-6.02"), rot=180)
r12.place(mm("62.56"), mm("-0.94"), rot=180)
r13.place(mm("62.56"), mm("5.41"), rot=180)
r14.place(mm("62.56"), mm("-11.1"), rot=180)
u1.place(mm("27"), mm("-17.45"))
u2.place(mm("40.97"), mm("-17.45"))

design.zone(
    gnd,
    layers=("B.Cu",),
    key="GND/1",
    outline=(
        (mm("82.88"), mm("10.49")),
        (mm("82.88"), mm("-32.69")),
        (mm("5.41"), mm("-32.69")),
        (mm("5.41"), mm("10.49")),
    ),
    clearance=mm("0.508"),
    min_thickness=mm("0.254"),
    thermal_gap=mm("0.508"),
    thermal_spoke_width=mm("0.508"),
)

design.text(
    "B.Cu/text/1",
    "Copper layer",
    (mm("19.38"), mm("-31.42")),
    layer="B.Cu",
    size=mm("1.524"),
    thickness=mm("0.3048"),
)
design.text(
    "F.Cu/text/1",
    "Component Side",
    (mm("18.1"), mm("-31.2")),
    layer="F.Cu",
    size=mm("1.524"),
    thickness=mm("0.3048"),
)
design.text(
    "F.Cu/text/2",
    "TDO-DONE",
    (mm("58.115"), mm("-13.64")),
    layer="F.Cu",
    size=mm("1.524"),
    thickness=mm("0.381"),
)
design.text(
    "F.Cu/text/3",
    "TDI-TIN",
    (mm("58.115"), mm("-8.56")),
    layer="F.Cu",
    size=mm("1.524"),
    thickness=mm("0.381"),
)
design.text(
    "F.Cu/text/4",
    "TCK-CCL",
    (mm("58.115"), mm("-3.48")),
    layer="F.Cu",
    size=mm("1.524"),
    thickness=mm("0.381"),
)
design.text(
    "F.Cu/text/5",
    "TMS-PROG",
    (mm("58.115"), mm("2.235")),
    layer="F.Cu",
    size=mm("1.524"),
    thickness=mm("0.381"),
)
design.text(
    "F.Cu/text/6",
    "VCC",
    (mm("62.56"), mm("-23.8")),
    layer="F.Cu",
    size=mm("1.524"),
    thickness=mm("0.381"),
)
design.text(
    "F.Cu/text/7",
    "GND",
    (mm("62.56"), mm("-18.72")),
    layer="F.Cu",
    size=mm("1.524"),
    thickness=mm("0.381"),
)
design.dimension(
    "Dwgs.User/dimension/1",
    (mm("83.7"), mm("10.49")),
    (mm("3.3"), mm("10.5")),
    offset=mm("-5.08"),
    size=mm("1.524"),
    thickness=mm("0.3048"),
    width=mm("0.3048"),
    extension_offset=mm("0"),
)

copper.apply(
    design,
    {
        "/CLK-D1": clk_d1,
        "/CTRL-D3": ctrl_d3,
        "/DONE-SELECT*": done_select,
        "/PWR_3,3-5V": pwr_3_3_5v,
        "/TCK-CCLK": tck_cclk,
        "/TD0-DONE": td0_done,
        "/TD0-PROG-D4": td0_prog_d4,
        "/TDI-DIN": tdi_din,
        "/TDI-DIN-D0": tdi_din_d0,
        "/TMS-PROG": tms_prog,
        "/TMS-PROG-D2": tms_prog_d2,
        "/VCC_SENSE-ERROR*": vcc_sense_error,
        "GND": gnd,
        "Net-(D1-K)": net_d1_k,
        "Net-(J1-Pad11)": net_j1_pad11,
        "Net-(U1A-E)": net_u1a_e,
        "Net-(U1A-O)": net_u1a_o,
        "Net-(U1B-D)": net_u1b_d,
        "Net-(U1B-E)": net_u1b_e,
        "Net-(U1B-O)": net_u1b_o,
        "Net-(U1C-D)": net_u1c_d,
        "Net-(U1C-O)": net_u1c_o,
        "Net-(U1D-D)": net_u1d_d,
        "Net-(U1D-O)": net_u1d_o,
        "Net-(U2A-O)": net_u2a_o,
        "VCC": vcc,
    },
)
