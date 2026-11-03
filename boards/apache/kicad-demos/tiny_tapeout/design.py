# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/tiny_tapeout@97acc80c223d75520c03fc44cab63cd9a3202c42 by Fenolite 0.7.0.dev0 on 2026-10-31;
# modified: format conversion to the Fenolite DSL.

import copper
from fenolite.dsl import Design, Module, Net, Part, arc_to, connect, mm, stack

design = Design("tinytapeout-demo")

design.board(
    outline=(
        (mm("-43.5"), mm("-43.5")),
        arc_to((mm("-42.62132"), mm("-45.62132")), (mm("-40.5"), mm("-46.5"))),
        (mm("-20.27"), mm("-46.5")),
        arc_to((mm("-19.987157"), mm("-46.382843")), (mm("-19.87"), mm("-46.1"))),
        (mm("-19.87"), mm("-39.9")),
        arc_to((mm("-19.790343"), mm("-39.63269")), (mm("-19.545"), mm("-39.500001"))),
        arc_to((mm("-19.324512"), mm("-39.572691")), (mm("-19.220002"), mm("-39.779999"))),
        arc_to((mm("-19.169852"), mm("-39.871065")), (mm("-19.07"), mm("-39.9"))),
        (mm("-11.43"), mm("-39.9")),
        arc_to((mm("-11.330147"), mm("-39.871065")), (mm("-11.280001"), mm("-39.78"))),
        arc_to((mm("-11.17549"), mm("-39.57269")), (mm("-10.955"), mm("-39.5"))),
        arc_to((mm("-10.709658"), mm("-39.632691")), (mm("-10.630001"), mm("-39.9"))),
        (mm("-10.63"), mm("-46.1")),
        arc_to((mm("-10.512843"), mm("-46.382843")), (mm("-10.23"), mm("-46.5"))),
        (mm("58"), mm("-46.5")),
        arc_to((mm("60.12132"), mm("-45.62132")), (mm("61"), mm("-43.5"))),
        (mm("61"), mm("31.5")),
        arc_to((mm("60.12132"), mm("33.62132")), (mm("58"), mm("34.5"))),
        (mm("-40.5"), mm("34.5")),
        arc_to((mm("-42.62132"), mm("33.62132")), (mm("-43.5"), mm("31.5"))),
    ),
    copper=4,
)
design.stackup(
    stack.silkscreen(color="White"),
    stack.mask(mm("0.01"), color="Blue"),
    stack.copper(mm("0.035")),
    stack.prepreg(
        mm("0.06813"),
        material="R-1551(W)",
        epsilon_r="4.3",
        loss_tangent="0.02",
        color="FR4 natural",
    ),
    stack.prepreg(
        mm("0.06813"),
        material="R-1551(W)",
        epsilon_r="4.3",
        loss_tangent="0.02",
        color="FR4 natural",
    ),
    stack.copper(mm("0.035")),
    stack.core(mm("1.13"), material="R-1566(W)", epsilon_r="4.6", loss_tangent="0.02", color="FR4 natural"),
    stack.copper(mm("0.035")),
    stack.prepreg(
        mm("0.06813"),
        material="R-1551(W)",
        epsilon_r="4.3",
        loss_tangent="0.02",
        color="FR4 natural",
    ),
    stack.prepreg(
        mm("0.06813"),
        material="R-1551(W)",
        epsilon_r="4.3",
        loss_tangent="0.02",
        color="FR4 natural",
    ),
    stack.copper(mm("0.035")),
    stack.mask(mm("0.01"), color="Blue"),
    stack.silkscreen(color="White"),
    impedance_controlled=True,
)
design.title_block(
    title="TinyTapeout 4+ Demoboard ",
    date="2023-12-13",
    revision="0.9.4",
    organization="Psychogenic Technologies",
    doc_id="See LICENSE.txt for details",
    responsible="Licensed under Apache 2.0",
    approver="(C) 2023 Pat Deegan",
)
design.user_layers(9, names={"User.9": "plugins.config"})

net_1v8 = Net("+1V8")
net_3v3 = Net("+3V3")
net_5v = Net("+5V")
cc1 = Net("/CC1")
cc2 = Net("/CC2")
rp2040_dvdd = Net("/RP2040/DVDD")
rp2040_qspi_clk = Net("/RP2040/QSPI_CLK")
rp2040_qspi_sd0 = Net("/RP2040/QSPI_SD0")
rp2040_qspi_sd1 = Net("/RP2040/QSPI_SD1")
rp2040_qspi_sd2 = Net("/RP2040/QSPI_SD2")
rp2040_qspi_sd3 = Net("/RP2040/QSPI_SD3")
rp2040_run = Net("/RP2040/RUN")
rp2040_swclk = Net("/RP2040/SWCLK")
rp2040_swdio = Net("/RP2040/SWDIO")
crvrst = Net("/~{CRVRST}")
caravel_csb = Net("Caravel_CSB")
caravel_d0 = Net("Caravel_D0")
caravel_d1 = Net("Caravel_D1")
caravel_sck = Net("Caravel_SCK")
gnd = Net("GND")
hk_csb = Net("HK_CSB")
hk_sck = Net("HK_SCK")
hk_sdi = Net("HK_SDI")
hk_sdo = Net("HK_SDO")
mux_sel = Net("MUX_SEL")
net_c1_pad2 = Net("Net-(C1-Pad2)")
net_c3_pad1 = Net("Net-(C3-Pad1)")
net_c30_pad1 = Net("Net-(C30-Pad1)")
net_d1_a = Net("Net-(D1-A)")
net_d2_a = Net("Net-(D2-A)")
net_d3_a = Net("Net-(D3-A)")
net_d4_a = Net("Net-(D4-A)")
net_jp1_b = Net("Net-(JP1-B)")
net_jp2_b = Net("Net-(JP2-B)")
net_jp3_b = Net("Net-(JP3-B)")
net_jp4_b = Net("Net-(JP4-B)")
net_jp5_b = Net("Net-(JP5-B)")
net_jp6_b = Net("Net-(JP6-B)")
net_jp7_b = Net("Net-(JP7-B)")
net_jp8_b = Net("Net-(JP8-B)")
net_r1_pad2 = Net("Net-(R1-Pad2)")
net_r10_pad2 = Net("Net-(R10-Pad2)")
net_r11_pad2 = Net("Net-(R11-Pad2)")
net_r13_pad1 = Net("Net-(R13-Pad1)")
net_r14_pad1 = Net("Net-(R14-Pad1)")
net_r2_pad2 = Net("Net-(R2-Pad2)")
net_r3_pad2 = Net("Net-(R3-Pad2)")
net_r4_pad2 = Net("Net-(R4-Pad2)")
net_r5_pad2 = Net("Net-(R5-Pad2)")
net_r6_pad2 = Net("Net-(R6-Pad2)")
net_u1_a = Net("Net-(U1-A)")
net_u1_b = Net("Net-(U1-B)")
net_u1_c = Net("Net-(U1-C)")
net_u1_d = Net("Net-(U1-D)")
net_u1_dp = Net("Net-(U1-DP)")
net_u1_e = Net("Net-(U1-E)")
net_u1_f = Net("Net-(U1-F)")
net_u1_g = Net("Net-(U1-G)")
net_u6_xin = Net("Net-(U6-XIN)")
net_u6_xout = Net("Net-(U6-XOUT)")
net_u7_io2 = Net("Net-(U7-IO2)")
net_u7_io3 = Net("Net-(U7-IO3)")
rpio29 = Net("RPIO29")
rp_proj_clk = Net("RP_proj_clk")
sdi_out0 = Net("SDI/out0")
sdo_out1 = Net("SDO/out1")
vbus = Net("VBUS")
boot_mode = Net("boot_mode")
cinc_out3 = Net("cinc/out3")
ctrl_ena = Net("ctrl_ena")
ctrl_sel_inc = Net("ctrl_sel_inc")
gpio = Net("gpio")
in0 = Net("in0")
in1 = Net("in1")
in2 = Net("in2")
in3 = Net("in3")
in4 = Net("in4")
in5 = Net("in5")
in6 = Net("in6")
in7 = Net("in7")
mio33 = Net("mio33")
mio35 = Net("mio35")
mio37 = Net("mio37")
mprj_io0 = Net("mprj_io0")
out0 = Net("out0")
out1 = Net("out1")
out2 = Net("out2")
out3 = Net("out3")
out4 = Net("out4")
out5 = Net("out5")
out6 = Net("out6")
out7 = Net("out7")
project_clk = Net("project_clk")
uio0 = Net("uio0")
uio1 = Net("uio1")
uio2 = Net("uio2")
uio3 = Net("uio3")
uio4 = Net("uio4")
uio5 = Net("uio5")
uio6 = Net("uio6")
uio7 = Net("uio7")
usb_d = Net("usb_d+")
usb_d_2 = Net("usb_d-")
usrclk2 = Net("usrclk2")
xclk = Net("xclk")
crst_out2 = Net("~{crst}/out2")
ctrl_sel_rst = Net("~{ctrl_sel_rst}")
project_rst = Net("~{project_rst}")

design.rules.netclass(
    "clk",
    clearance=mm("0.2"),
    track_width=mm("0.245"),
    via_diameter=mm("0.65"),
    via_drill=mm("0.3"),
    diff_pair_width=mm("0.2"),
    diff_pair_gap=mm("0.25"),
    diff_pair_via_gap=mm("0.25"),
    nets=(rp_proj_clk, project_clk, xclk),
)
design.rules.netclass(
    "config",
    clearance=mm("0.2"),
    track_width=mm("0.2"),
    via_diameter=mm("0.65"),
    via_drill=mm("0.3"),
    diff_pair_width=mm("0.2"),
    diff_pair_gap=mm("0.25"),
    diff_pair_via_gap=mm("0.25"),
    nets=(hk_csb, hk_sck, hk_sdi, hk_sdo, ctrl_ena, ctrl_sel_inc, ctrl_sel_rst),
)
design.rules.netclass(
    "iobidir",
    clearance=mm("0.2"),
    track_width=mm("0.245"),
    via_diameter=mm("0.62"),
    via_drill=mm("0.3"),
    diff_pair_width=mm("0.2"),
    diff_pair_gap=mm("0.25"),
    diff_pair_via_gap=mm("0.25"),
    nets=(uio0, uio1, uio2, uio3, uio4, uio5, uio6, uio7),
)
design.rules.netclass(
    "ioin",
    clearance=mm("0.2"),
    track_width=mm("0.245"),
    via_diameter=mm("0.62"),
    via_drill=mm("0.3"),
    diff_pair_width=mm("0.2"),
    diff_pair_gap=mm("0.25"),
    diff_pair_via_gap=mm("0.25"),
    nets=(in0, in1, in2, in3, in4, in5, in6, in7),
)
design.rules.netclass(
    "ioout",
    clearance=mm("0.2"),
    track_width=mm("0.245"),
    via_diameter=mm("0.62"),
    via_drill=mm("0.3"),
    diff_pair_width=mm("0.2"),
    diff_pair_gap=mm("0.25"),
    diff_pair_via_gap=mm("0.25"),
    nets=(sdi_out0, sdo_out1, cinc_out3, out0, out1, out2, out3, out4, out5, out6, out7, crst_out2),
)
design.rules.netclass(
    "pwr",
    clearance=mm("0.23"),
    track_width=mm("0.25"),
    via_diameter=mm("0.65"),
    via_drill=mm("0.3"),
    diff_pair_width=mm("0.2"),
    diff_pair_gap=mm("0.25"),
    diff_pair_via_gap=mm("0.25"),
    nets=(net_1v8, net_3v3, gnd),
)
design.rules.netclass(
    "pwrhi",
    clearance=mm("0.25"),
    track_width=mm("0.3"),
    via_diameter=mm("0.8"),
    via_drill=mm("0.4"),
    diff_pair_width=mm("0.2"),
    diff_pair_gap=mm("0.25"),
    diff_pair_via_gap=mm("0.25"),
    nets=(net_5v, vbus),
)
design.rules.netclass(
    "usbdiff",
    clearance=mm("0.2"),
    track_width=mm("0.23"),
    via_diameter=mm("0.6"),
    via_drill=mm("0.3"),
    diff_pair_width=mm("0.23"),
    diff_pair_gap=mm("0.165"),
    diff_pair_via_gap=mm("0.25"),
    nets=(usb_d, usb_d_2),
)
design.rules.minimum(
    track_width=mm("0.16"),
    via_diameter=mm("0.3"),
    hole_size=mm("0.2"),
    edge_clearance=mm("0.3"),
)

g_1 = Part(
    "G***",
    "flyingcarsfootprints:PsychoLogo",
    footprint="flyingcarsfootprints:PsychoLogo",
    value="LOGO",
    name="G_1",
    board_only=True,
)
g_2 = Part("G***", "Imported:LOGO", footprint="Imported:LOGO", value="LOGO", name="G_2", board_only=True)
g_3 = Part("G***", "Imported:LOGO_2", footprint="Imported:LOGO_2", value="LOGO", name="G_3", board_only=True)
g_4 = Part(
    "G***",
    "flyingcarsfootprints:PsychoLogoSmall",
    footprint="flyingcarsfootprints:PsychoLogoSmall",
    value="LOGO",
    name="G_4",
    board_only=True,
)
ref_1 = Part(
    "REF**",
    "Logos:Z2A_logo",
    footprint="Logos:Z2A_logo",
    value="Z2A_logo",
    name="REF_1",
    board_only=True,
)
ref_2 = Part(
    "REF**",
    "OSHW:OSHW_BADGE",
    footprint="OSHW:OSHW_BADGE",
    value="OSHW_BADGE",
    name="REF_2",
    board_only=True,
)
ref_3 = Part(
    "REF**",
    "Logos:TT_logo",
    footprint="Logos:TT_logo",
    value="TT_logo",
    name="REF_3",
    board_only=True,
)
stitch1_1 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_1",
    board_only=True,
)
stitch1_2 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_2",
    board_only=True,
)
stitch1_3 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_3",
    board_only=True,
)
stitch1_4 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_4",
    board_only=True,
)
stitch1_5 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_5",
    board_only=True,
)
stitch1_6 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_6",
    board_only=True,
)
stitch1_7 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_7",
    board_only=True,
)
stitch1_8 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_8",
    board_only=True,
)
stitch1_9 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_9",
    board_only=True,
)
stitch1_10 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_10",
    board_only=True,
)
stitch1_11 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_11",
    board_only=True,
)
stitch1_12 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_12",
    board_only=True,
)
stitch1_13 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_13",
    board_only=True,
)
stitch1_14 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_14",
    board_only=True,
)
stitch1_15 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_15",
    board_only=True,
)
stitch1_16 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_16",
    board_only=True,
)
stitch1_17 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_17",
    board_only=True,
)
stitch1_18 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_18",
    board_only=True,
)
stitch1_19 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_19",
    board_only=True,
)
stitch1_20 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_20",
    board_only=True,
)
stitch1_21 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_21",
    board_only=True,
)
stitch1_22 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_22",
    board_only=True,
)
stitch1_23 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_23",
    board_only=True,
)
stitch1_24 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_24",
    board_only=True,
)
stitch1_25 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_25",
    board_only=True,
)
stitch1_26 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_26",
    board_only=True,
)
stitch1_27 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_27",
    board_only=True,
)
stitch1_28 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_28",
    board_only=True,
)
stitch1_29 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_29",
    board_only=True,
)
stitch1_30 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_30",
    board_only=True,
)
stitch1_31 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_31",
    board_only=True,
)
stitch1_32 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_32",
    board_only=True,
)
stitch1_33 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_33",
    board_only=True,
)
stitch1_34 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_34",
    board_only=True,
)
stitch1_35 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_35",
    board_only=True,
)
stitch1_36 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_36",
    board_only=True,
)
stitch1_37 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_37",
    board_only=True,
)
stitch1_38 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_38",
    board_only=True,
)
stitch1_39 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_39",
    board_only=True,
)
stitch1_40 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_40",
    board_only=True,
)
stitch1_41 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_41",
    board_only=True,
)
stitch1_42 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_42",
    board_only=True,
)
stitch1_43 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_43",
    board_only=True,
)
stitch1_44 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_44",
    board_only=True,
)
stitch1_45 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_45",
    board_only=True,
)
stitch1_46 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_46",
    board_only=True,
)
stitch1_47 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_47",
    board_only=True,
)
stitch1_48 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_48",
    board_only=True,
)
stitch1_49 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_49",
    board_only=True,
)
stitch1_50 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_50",
    board_only=True,
)
stitch1_51 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_51",
    board_only=True,
)
stitch1_52 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_52",
    board_only=True,
)
stitch1_53 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_53",
    board_only=True,
)
stitch1_54 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_54",
    board_only=True,
)
stitch1_55 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_55",
    board_only=True,
)
stitch1_56 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_56",
    board_only=True,
)
stitch1_57 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_57",
    board_only=True,
)
stitch1_58 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_58",
    board_only=True,
)
stitch1_59 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_59",
    board_only=True,
)
stitch1_60 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_60",
    board_only=True,
)
stitch1_61 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_61",
    board_only=True,
)
stitch1_62 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_62",
    board_only=True,
)
stitch1_63 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_63",
    board_only=True,
)
stitch1_64 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_64",
    board_only=True,
)
stitch1_65 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_65",
    board_only=True,
)
stitch1_66 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_66",
    board_only=True,
)
stitch1_67 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_67",
    board_only=True,
)
stitch1_68 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_68",
    board_only=True,
)
stitch1_69 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_69",
    board_only=True,
)
stitch1_70 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_70",
    board_only=True,
)
stitch1_71 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_71",
    board_only=True,
)
stitch1_72 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_72",
    board_only=True,
)
stitch1_73 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_73",
    board_only=True,
)
stitch1_74 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_74",
    board_only=True,
)
stitch1_75 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_75",
    board_only=True,
)
stitch1_76 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_76",
    board_only=True,
)
stitch1_77 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_77",
    board_only=True,
)
stitch1_78 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_78",
    board_only=True,
)
stitch1_79 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_79",
    board_only=True,
)
stitch1_80 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_80",
    board_only=True,
)
stitch1_81 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_81",
    board_only=True,
)
stitch1_82 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_82",
    board_only=True,
)
stitch1_83 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_83",
    board_only=True,
)
stitch1_84 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_84",
    board_only=True,
)
stitch1_85 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_85",
    board_only=True,
)
stitch1_86 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_86",
    board_only=True,
)
stitch1_87 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_87",
    board_only=True,
)
stitch1_88 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_88",
    board_only=True,
)
stitch1_89 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_89",
    board_only=True,
)
stitch1_90 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_90",
    board_only=True,
)
stitch1_91 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_91",
    board_only=True,
)
stitch1_92 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_92",
    board_only=True,
)
stitch1_93 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_93",
    board_only=True,
)
stitch1_94 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_94",
    board_only=True,
)
stitch1_95 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_95",
    board_only=True,
)
stitch1_96 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_96",
    board_only=True,
)
stitch1_97 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_97",
    board_only=True,
)
stitch1_98 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_98",
    board_only=True,
)
stitch1_99 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_99",
    board_only=True,
)
stitch1_100 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_100",
    board_only=True,
)
stitch1_101 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_101",
    board_only=True,
)
stitch1_102 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_102",
    board_only=True,
)
stitch1_103 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_103",
    board_only=True,
)
stitch1_104 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_104",
    board_only=True,
)
stitch1_105 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_105",
    board_only=True,
)
stitch1_106 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_106",
    board_only=True,
)
stitch1_107 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_107",
    board_only=True,
)
stitch1_108 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_108",
    board_only=True,
)
stitch1_109 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_109",
    board_only=True,
)
stitch1_110 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_110",
    board_only=True,
)
stitch1_111 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_111",
    board_only=True,
)
stitch1_112 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_112",
    board_only=True,
)
stitch1_113 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_113",
    board_only=True,
)
stitch1_114 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_114",
    board_only=True,
)
stitch1_115 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_115",
    board_only=True,
)
stitch1_116 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_116",
    board_only=True,
)
stitch1_117 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_117",
    board_only=True,
)
stitch1_118 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_118",
    board_only=True,
)
stitch1_119 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_119",
    board_only=True,
)
stitch1_120 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_120",
    board_only=True,
)
stitch1_121 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_121",
    board_only=True,
)
stitch1_122 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_122",
    board_only=True,
)
stitch1_123 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_123",
    board_only=True,
)
stitch1_124 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_124",
    board_only=True,
)
stitch1_125 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_125",
    board_only=True,
)
stitch1_126 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_126",
    board_only=True,
)
stitch1_127 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_127",
    board_only=True,
)
stitch1_128 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_128",
    board_only=True,
)
stitch1_129 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_129",
    board_only=True,
)
stitch1_130 = Part(
    "STITCH1",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH1_130",
    board_only=True,
)
stitch2 = Part(
    "STITCH2",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    board_only=True,
)
stitch3 = Part(
    "STITCH3",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    board_only=True,
)
stitch4 = Part(
    "STITCH4",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    board_only=True,
)
stitch5 = Part(
    "STITCH5",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    board_only=True,
)
stitch6_1 = Part(
    "STITCH6",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH6_1",
    board_only=True,
)
stitch6_2 = Part(
    "STITCH6",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH6_2",
    board_only=True,
)
stitch6_3 = Part(
    "STITCH6",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    name="STITCH6_3",
    board_only=True,
)
stitch7 = Part(
    "STITCH7",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    board_only=True,
)
stitch8 = Part(
    "STITCH8",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    board_only=True,
)
stitch9 = Part(
    "STITCH9",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    board_only=True,
)
stitch10 = Part(
    "STITCH10",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    board_only=True,
)
stitch11 = Part(
    "STITCH11",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    board_only=True,
)
stitch12 = Part(
    "STITCH12",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    board_only=True,
)
stitch13 = Part(
    "STITCH13",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    board_only=True,
)
stitch14 = Part(
    "STITCH14",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    board_only=True,
)
stitch15 = Part(
    "STITCH15",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    board_only=True,
)
stitch16 = Part(
    "STITCH16",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    board_only=True,
)
stitch17 = Part(
    "STITCH17",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    board_only=True,
)
stitch18 = Part(
    "STITCH18",
    "flyingcarsfootprints:StitchingVia-0.3mm",
    footprint="flyingcarsfootprints:StitchingVia-0.3mm",
    value="StitchingVia-0.3mm",
    board_only=True,
)
ttlogo = Part("TTLOGO", "Logos:TT_logo_2", footprint="Logos:TT_logo_2", value="TT_logo", board_only=True)
z2alogo = Part("Z2ALOGO", "Logos:Z2A_logo_2", footprint="Logos:Z2A_logo_2", value="Z2A_logo", board_only=True)
kibuzzard_63fe0d11 = Part(
    "kibuzzard-63FE0D11",
    "Imported:kibuzzard-63FE0D11",
    footprint="Imported:kibuzzard-63FE0D11",
    value="G***",
    board_only=True,
)
c1 = Part(
    "C1",
    "Capacitor_SMD:C_0603_1608Metric",
    footprint="Capacitor_SMD:C_0603_1608Metric",
    value="1uF",
    properties={
        "Characteristics": "1u 10V XR 0603",
        "MPN": "CL10A105KA8NNNC",
        "MPN_ALT": "C0603C105K4RAC7411",
    },
)
c2 = Part(
    "C2",
    "Capacitor_SMD:C_0402_1005Metric_6",
    footprint="Capacitor_SMD:C_0402_1005Metric_6",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "JLC": "",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
        "Part number": "",
    },
)
c3 = Part(
    "C3",
    "Capacitor_SMD:C_0603_1608Metric_8",
    footprint="Capacitor_SMD:C_0603_1608Metric_8",
    value="6800pF",
    properties={"DNP": "DNP", "JLC": "", "MPN": "", "Part number": ""},
    dnp=True,
)
c4 = Part(
    "C4",
    "Capacitor_SMD:C_0402_1005Metric_13",
    footprint="Capacitor_SMD:C_0402_1005Metric_13",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "JLC": "",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
        "Part number": "",
    },
)
c5 = Part(
    "C5",
    "Capacitor_SMD:C_0603_1608Metric_12",
    footprint="Capacitor_SMD:C_0603_1608Metric_12",
    value="1uF",
    properties={
        "Characteristics": "1u 10V XR 0603",
        "DigikeyPN": "",
        "JLC": "",
        "MPN": "CL10A105KA8NNNC",
        "MPN_ALT": "C0603C105K4RAC7411",
        "Part number": "",
    },
)
c6 = Part(
    "C6",
    "Capacitor_SMD:C_0805_2012Metric_2",
    footprint="Capacitor_SMD:C_0805_2012Metric_2",
    value="10uF",
    properties={
        "Characteristics": "10u 10V XR 0805",
        "JLC": "C237493",
        "MPN": "CL21B106KOQNNNF",
        "MPN_ALT": "LMK212AB7106MG-T",
        "Part number": "",
    },
)
c7 = Part(
    "C7",
    "Capacitor_SMD:C_0805_2012Metric_3",
    footprint="Capacitor_SMD:C_0805_2012Metric_3",
    value="10uF",
    properties={
        "Characteristics": "10u 10V XR 0805",
        "JLC": "C237493",
        "MPN": "CL21B106KOQNNNF",
        "MPN_ALT": "LMK212AB7106MG-T",
        "Part number": "",
    },
)
c8 = Part(
    "C8",
    "Capacitor_SMD:C_0402_1005Metric_11",
    footprint="Capacitor_SMD:C_0402_1005Metric_11",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "JLC": "",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
        "Part number": "",
    },
)
c9 = Part(
    "C9",
    "Capacitor_SMD:C_0603_1608Metric_15",
    footprint="Capacitor_SMD:C_0603_1608Metric_15",
    value="1uF",
    properties={
        "Characteristics": "1u 10V XR 0603",
        "DigikeyPN": "",
        "JLC": "",
        "MPN": "CL10A105KA8NNNC",
        "MPN_ALT": "C0603C105K4RAC7411",
        "Part number": "",
    },
)
c10 = Part(
    "C10",
    "Capacitor_SMD:C_0805_2012Metric",
    footprint="Capacitor_SMD:C_0805_2012Metric",
    value="22uF",
    properties={
        "Characteristics": "22u 6V XR 0805",
        "JLC": "C86816",
        "MPN": "CL21A226KOQNNNG",
        "MPN_ALT": "GRM21BR61A226ME51K",
        "Part number": "",
    },
)
c11 = Part(
    "C11",
    "Capacitor_SMD:C_0603_1608Metric_2",
    footprint="Capacitor_SMD:C_0603_1608Metric_2",
    value="1uF",
    properties={
        "Characteristics": "1u 10V XR 0603",
        "MPN": "CL10A105KA8NNNC",
        "MPN_ALT": "C0603C105K4RAC7411",
    },
)
c12 = Part(
    "C12",
    "Capacitor_SMD:C_0402_1005Metric",
    footprint="Capacitor_SMD:C_0402_1005Metric",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "JLC": "",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
        "Part number": "",
    },
)
c13 = Part(
    "C13",
    "Capacitor_SMD:C_0402_1005Metric_2",
    footprint="Capacitor_SMD:C_0402_1005Metric_2",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "JLC": "",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
        "Part number": "",
    },
)
c14 = Part(
    "C14",
    "Capacitor_SMD:C_0402_1005Metric_3",
    footprint="Capacitor_SMD:C_0402_1005Metric_3",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "JLC": "",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
        "Part number": "",
    },
)
c15 = Part(
    "C15",
    "Capacitor_SMD:C_0603_1608Metric_3",
    footprint="Capacitor_SMD:C_0603_1608Metric_3",
    value="1uF",
    properties={
        "Characteristics": "1u 10V XR 0603",
        "DigikeyPN": "",
        "JLC": "",
        "MPN": "CL10A105KA8NNNC",
        "MPN_ALT": "C0603C105K4RAC7411",
        "Part number": "",
    },
)
c16 = Part(
    "C16",
    "Capacitor_SMD:C_0603_1608Metric_4",
    footprint="Capacitor_SMD:C_0603_1608Metric_4",
    value="10uF",
    properties={
        "Characteristics": "10u 10V XR 0603",
        "DigikeyPN": "490-GRT188R61C106KE13JCT-ND",
        "JLC": "",
        "MPN": "CL10A106MP8NNNC",
        "MPN_ALT": "GRT188R61C106KE13J ",
        "Part number": "",
    },
)
c17 = Part(
    "C17",
    "Capacitor_SMD:C_0603_1608Metric_5",
    footprint="Capacitor_SMD:C_0603_1608Metric_5",
    value="1uF",
    properties={
        "Characteristics": "1u 10V XR 0603",
        "DigikeyPN": "",
        "JLC": "",
        "MPN": "CL10A105KA8NNNC",
        "MPN_ALT": "C0603C105K4RAC7411",
        "Part number": "",
    },
)
c18 = Part(
    "C18",
    "Capacitor_SMD:C_0402_1005Metric_4",
    footprint="Capacitor_SMD:C_0402_1005Metric_4",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "JLC": "",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
        "Part number": "",
    },
)
c19 = Part(
    "C19",
    "Capacitor_SMD:C_0402_1005Metric_5",
    footprint="Capacitor_SMD:C_0402_1005Metric_5",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "JLC": "",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
        "Part number": "",
    },
)
c20 = Part(
    "C20",
    "Capacitor_SMD:C_0402_1005Metric_7",
    footprint="Capacitor_SMD:C_0402_1005Metric_7",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "JLC": "",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
        "Part number": "",
    },
)
c21 = Part(
    "C21",
    "Capacitor_SMD:C_0603_1608Metric_6",
    footprint="Capacitor_SMD:C_0603_1608Metric_6",
    value="10uF",
    properties={
        "Characteristics": "10u 10V XR 0603",
        "DigikeyPN": "490-GRT188R61C106KE13JCT-ND",
        "JLC": "",
        "MPN": "CL10A106MP8NNNC",
        "MPN_ALT": "GRT188R61C106KE13J ",
        "Part number": "",
    },
)
c22 = Part(
    "C22",
    "Capacitor_SMD:C_0402_1005Metric_8",
    footprint="Capacitor_SMD:C_0402_1005Metric_8",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "JLC": "",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
        "Part number": "",
    },
)
c23 = Part(
    "C23",
    "Capacitor_SMD:C_0402_1005Metric_9",
    footprint="Capacitor_SMD:C_0402_1005Metric_9",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "JLC": "",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
        "Part number": "",
    },
)
c24 = Part(
    "C24",
    "Capacitor_SMD:C_0402_1005Metric_8",
    footprint="Capacitor_SMD:C_0402_1005Metric_8",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "JLC": "",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
        "Part number": "",
    },
)
c25 = Part(
    "C25",
    "Capacitor_SMD:C_0603_1608Metric_7",
    footprint="Capacitor_SMD:C_0603_1608Metric_7",
    value="1uF",
    properties={
        "Characteristics": "1u 10V XR 0603",
        "DigikeyPN": "",
        "JLC": "",
        "MPN": "CL10A105KA8NNNC",
        "MPN_ALT": "C0603C105K4RAC7411",
        "Part number": "",
    },
)
c26 = Part(
    "C26",
    "Capacitor_SMD:C_0402_1005Metric_10",
    footprint="Capacitor_SMD:C_0402_1005Metric_10",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "JLC": "",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
        "Part number": "",
    },
)
c27 = Part(
    "C27",
    "Capacitor_SMD:C_0402_1005Metric_11",
    footprint="Capacitor_SMD:C_0402_1005Metric_11",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "JLC": "",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
        "Part number": "",
    },
)
c28 = Part(
    "C28",
    "Capacitor_SMD:C_0402_1005Metric_12",
    footprint="Capacitor_SMD:C_0402_1005Metric_12",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "JLC": "",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
        "Part number": "",
    },
)
c42 = Part(
    "C42",
    "Capacitor_SMD:C_0603_1608Metric_11",
    footprint="Capacitor_SMD:C_0603_1608Metric_11",
    value="1uF",
    properties={
        "Characteristics": "1u 10V XR 0603",
        "DigikeyPN": "",
        "JLC": "",
        "MPN": "CL10A105KA8NNNC",
        "MPN_ALT": "C0603C105K4RAC7411",
        "Part number": "",
    },
)
c43 = Part(
    "C43",
    "Capacitor_SMD:C_0402_1005Metric_20",
    footprint="Capacitor_SMD:C_0402_1005Metric_20",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
        "Part number": "",
    },
)
c56 = Part(
    "C56",
    "Capacitor_SMD:C_0402_1005Metric_21",
    footprint="Capacitor_SMD:C_0402_1005Metric_21",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "JLC": "",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
        "Part number": "",
    },
)
c57 = Part(
    "C57",
    "Capacitor_SMD:C_0603_1608Metric_13",
    footprint="Capacitor_SMD:C_0603_1608Metric_13",
    value="1uF",
    properties={
        "Characteristics": "1u 10V XR 0603",
        "DigikeyPN": "",
        "JLC": "",
        "MPN": "CL10A105KA8NNNC",
        "MPN_ALT": "C0603C105K4RAC7411",
        "Part number": "",
    },
)
c58 = Part(
    "C58",
    "Capacitor_SMD:C_0402_1005Metric_22",
    footprint="Capacitor_SMD:C_0402_1005Metric_22",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "JLC": "",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
        "Part number": "",
    },
)
c59 = Part(
    "C59",
    "Capacitor_SMD:C_0603_1608Metric_10",
    footprint="Capacitor_SMD:C_0603_1608Metric_10",
    value="1uF",
    properties={
        "Characteristics": "1u 10V XR 0603",
        "DigikeyPN": "",
        "JLC": "",
        "MPN": "CL10A105KA8NNNC",
        "MPN_ALT": "C0603C105K4RAC7411",
        "Part number": "",
    },
)
c60 = Part(
    "C60",
    "Capacitor_SMD:C_0402_1005Metric_23",
    footprint="Capacitor_SMD:C_0402_1005Metric_23",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "JLC": "",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
        "Part number": "",
    },
)
c61 = Part(
    "C61",
    "Capacitor_SMD:C_0603_1608Metric_14",
    footprint="Capacitor_SMD:C_0603_1608Metric_14",
    value="1uF",
    properties={
        "Characteristics": "1u 10V XR 0603",
        "DigikeyPN": "",
        "JLC": "",
        "MPN": "CL10A105KA8NNNC",
        "MPN_ALT": "C0603C105K4RAC7411",
        "Part number": "",
    },
)
d1 = Part(
    "D1",
    "LED_SMD:LED_0603_1608Metric",
    footprint="LED_SMD:LED_0603_1608Metric",
    value="Yellow",
    properties={
        "Characteristics": "Yellow LED",
        "JLC": "C72038",
        "MPN": "LTST-C190YKT",
        "MPN_ALT": "TLMY1000-GS15",
        "Part number": "",
    },
)
d2 = Part(
    "D2",
    "LED_SMD:LED_0603_1608Metric_2",
    footprint="LED_SMD:LED_0603_1608Metric_2",
    value="Yellow",
    properties={
        "Characteristics": "Yellow LED",
        "JLC": "C72038",
        "MPN": "LTST-C190YKT",
        "MPN_ALT": "TLMY1000-GS15",
        "Part number": "",
    },
)
d3 = Part(
    "D3",
    "LED_SMD:LED_0603_1608Metric",
    footprint="LED_SMD:LED_0603_1608Metric",
    value="Yellow",
    properties={
        "Characteristics": "Yellow LED",
        "JLC": "C72038",
        "MPN": "LTST-C190YKT",
        "MPN_ALT": "TLMY1000-GS15",
        "Part number": "",
    },
)
d4 = Part(
    "D4",
    "LED_SMD:LED_0603_1608Metric_3",
    footprint="LED_SMD:LED_0603_1608Metric_3",
    value="Yellow",
    properties={
        "Characteristics": "Yellow LED",
        "JLC": "C72038",
        "MPN": "LTST-C190YKT",
        "MPN_ALT": "TLMY1000-GS15",
        "Part number": "",
    },
)
f1 = Part(
    "F1",
    "Fuse:Fuse_0805_2012Metric",
    footprint="Fuse:Fuse_0805_2012Metric",
    value="350mA",
    properties={
        "Characteristics": "PTC Reset Fuse, 350mA Hold, 0805",
        "JLC": "C1884490",
        "MPN": "0ZCK0035FF2G",
        "MPN_ALT": "SMD0805B035TF",
        "Part number": "",
    },
)
fid1 = Part(
    "FID1",
    "Fiducial:Fiducial_1mm_Mask2mm",
    footprint="Fiducial:Fiducial_1mm_Mask2mm",
    value="Fiducial",
)
fid2 = Part(
    "FID2",
    "Fiducial:Fiducial_1mm_Mask2mm",
    footprint="Fiducial:Fiducial_1mm_Mask2mm",
    value="Fiducial",
)
fid3 = Part(
    "FID3",
    "Fiducial:Fiducial_1mm_Mask2mm",
    footprint="Fiducial:Fiducial_1mm_Mask2mm",
    value="Fiducial",
)
j1 = Part(
    "J1",
    "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical",
    footprint="Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical",
    value="Conn_01x06",
    dnp=True,
)
j2 = Part(
    "J2",
    "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical",
    footprint="Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical",
    value="Conn_01x04",
    dnp=True,
)
j3 = Part(
    "J3",
    "TinyTapeout:PinSocket_2x06_P2.54mm_PMODHost1A_4",
    footprint="TinyTapeout:PinSocket_2x06_P2.54mm_PMODHost1A_4",
    value="613012243121",
    properties={"MPN": "613012243121", "MPN_ALT": "PPTC062LJBN-RC"},
)
j4 = Part(
    "J4",
    "TinyTapeout:TT04_BREAKOUT_SMB",
    footprint="TinyTapeout:TT04_BREAKOUT_SMB",
    value="TT04_BREAKOUT_REVB",
    properties={"Characteristics": "", "DigikeyPN": "609-3124-ND x 2", "MPN": "95157-440LF x 2"},
)
j5 = Part(
    "J5",
    "TinyTapeout:PinSocket_2x06_P2.54mm_PMODHost1A_5",
    footprint="TinyTapeout:PinSocket_2x06_P2.54mm_PMODHost1A_5",
    value="613012243121",
    properties={"MPN": "613012243121", "MPN_ALT": "PPTC062LJBN-RC"},
)
j6 = Part(
    "J6",
    "TinyTapeout:PinSocket_2x06_P2.54mm_PMODHost1A_6",
    footprint="TinyTapeout:PinSocket_2x06_P2.54mm_PMODHost1A_6",
    value="613012243121",
    properties={"MPN": "613012243121", "MPN_ALT": "PPTC062LJBN-RC"},
)
j7 = Part(
    "J7",
    "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical_SMD_Pin1Right",
    footprint="Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical_SMD_Pin1Right",
    value="Conn_01x02",
    properties={"Characteristics": "", "MPN": "10129380-902001BLF", "MPN_ALT": "GEC02SABN-M30"},
)
j8 = Part(
    "J8",
    "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical_2",
    footprint="Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical_2",
    value="Conn_01x03",
    dnp=True,
)
j9 = Part(
    "J9",
    "Connector_PinHeader_2.54mm:PinHeader_1x24_P2.54mm_Vertical",
    footprint="Connector_PinHeader_2.54mm:PinHeader_1x24_P2.54mm_Vertical",
    value="Conn_01x24",
    properties={"MPN": "PRPC024SAAN-RC"},
    dnp=True,
)
j12 = Part(
    "J12",
    "TinyTapeout:PinSocket_2x06_P2.54mm_PMODHost1A",
    footprint="TinyTapeout:PinSocket_2x06_P2.54mm_PMODHost1A",
    value="613012243121",
    properties={"MPN": "613012243121", "MPN_ALT": "PPTC062LJBN-RC"},
)
j13 = Part(
    "J13",
    "TinyTapeout:PinSocket_2x06_P2.54mm_PMODHost1A_2",
    footprint="TinyTapeout:PinSocket_2x06_P2.54mm_PMODHost1A_2",
    value="613012243121",
    properties={"MPN": "613012243121", "MPN_ALT": "PPTC062LJBN-RC"},
)
j14 = Part(
    "J14",
    "TinyTapeout:PinSocket_2x06_P2.54mm_PMODHost1A_3",
    footprint="TinyTapeout:PinSocket_2x06_P2.54mm_PMODHost1A_3",
    value="613012243121",
    properties={"MPN": "613012243121", "MPN_ALT": "PPTC062LJBN-RC"},
)
j15 = Part(
    "J15",
    "TinyTapeout:GCT_USB4500-03-0-A_REVA",
    footprint="TinyTapeout:GCT_USB4500-03-0-A_REVA",
    value="USB4500-03-0-A_REVA",
    properties={"MANUFACTURER": "GCT", "MAXIMUM_PACKAGE_HEIGHT": "2.46mm", "MPN": "USB4500-03-0-A"},
)
j16 = Part(
    "J16",
    "TinyTapeout:TT_BREAKOUT_PINHEADER_PLACEHOLDER_WITHPAD",
    footprint="TinyTapeout:TT_BREAKOUT_PINHEADER_PLACEHOLDER_WITHPAD",
    value="2x20_P2.54mm_Pinheader",
    properties={"MPN": "95157-440LF", "MPN_ALT": "M20-8762042"},
    board_only=True,
)
j17 = Part(
    "J17",
    "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical",
    footprint="Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical",
    value="Conn_01x03",
    dnp=True,
)
j18 = Part(
    "J18",
    "TinyTapeout:TT_BREAKOUT_PINHEADER_PLACEHOLDER_WITHPAD_2",
    footprint="TinyTapeout:TT_BREAKOUT_PINHEADER_PLACEHOLDER_WITHPAD_2",
    value="2x20_P2.54mm_Pinheader",
    properties={"MPN": "95157-440LF", "MPN_ALT": "M20-8762042"},
    board_only=True,
)
jp1 = Part(
    "JP1",
    "TinyTapeout:SolderJumper-2_Bridged_Throughole1",
    footprint="TinyTapeout:SolderJumper-2_Bridged_Throughole1",
    value="SolderJumper_2_Bridged",
)
jp2 = Part(
    "JP2",
    "TinyTapeout:SolderJumper-2_Bridged_Throughole1_2",
    footprint="TinyTapeout:SolderJumper-2_Bridged_Throughole1_2",
    value="SolderJumper_2_Bridged",
)
jp3 = Part(
    "JP3",
    "TinyTapeout:SolderJumper-2_Bridged_Throughole1_3",
    footprint="TinyTapeout:SolderJumper-2_Bridged_Throughole1_3",
    value="SolderJumper_2_Bridged",
)
jp4 = Part(
    "JP4",
    "TinyTapeout:SolderJumper-2_Bridged_Throughole1_4",
    footprint="TinyTapeout:SolderJumper-2_Bridged_Throughole1_4",
    value="SolderJumper_2_Bridged",
)
jp5 = Part(
    "JP5",
    "TinyTapeout:SolderJumper-2_Bridged_Throughole1_5",
    footprint="TinyTapeout:SolderJumper-2_Bridged_Throughole1_5",
    value="SolderJumper_2_Bridged",
)
jp6 = Part(
    "JP6",
    "TinyTapeout:SolderJumper-2_Bridged_Throughole1_6",
    footprint="TinyTapeout:SolderJumper-2_Bridged_Throughole1_6",
    value="SolderJumper_2_Bridged",
)
jp7 = Part(
    "JP7",
    "TinyTapeout:SolderJumper-2_Bridged_Throughole1_7",
    footprint="TinyTapeout:SolderJumper-2_Bridged_Throughole1_7",
    value="SolderJumper_2_Bridged",
)
jp8 = Part(
    "JP8",
    "TinyTapeout:SolderJumper-2_Bridged_Throughole1_8",
    footprint="TinyTapeout:SolderJumper-2_Bridged_Throughole1_8",
    value="SolderJumper_2_Bridged",
)
mt1 = Part(
    "MT1",
    "MountingHole:MountingHole_3.2mm_M3_Pad",
    footprint="MountingHole:MountingHole_3.2mm_M3_Pad",
    value="MountingHole_Pad",
    properties={"Characteristics": "", "MPN": "DNP", "Part number": ""},
)
mt2 = Part(
    "MT2",
    "MountingHole:MountingHole_3.2mm_M3_Pad_2",
    footprint="MountingHole:MountingHole_3.2mm_M3_Pad_2",
    value="MountingHole_Pad",
    properties={"Characteristics": "", "MPN": "DNP", "Part number": ""},
)
mt3 = Part(
    "MT3",
    "MountingHole:MountingHole_3.2mm_M3_Pad_3",
    footprint="MountingHole:MountingHole_3.2mm_M3_Pad_3",
    value="MountingHole_Pad",
    properties={"Characteristics": "", "MPN": "DNP", "Part number": ""},
)
mt4 = Part(
    "MT4",
    "MountingHole:MountingHole_3.2mm_M3_Pad_4",
    footprint="MountingHole:MountingHole_3.2mm_M3_Pad_4",
    value="MountingHole_Pad",
    properties={"Characteristics": "", "MPN": "DNP", "Part number": ""},
)
nt1 = Part("NT1", "NetTie:NetTie-2_SMD_Pad0.5mm", footprint="NetTie:NetTie-2_SMD_Pad0.5mm", value="NetTie_2")
r1 = Part(
    "R1",
    "Resistor_SMD:R_0402_1005Metric",
    footprint="Resistor_SMD:R_0402_1005Metric",
    value="1k",
    properties={
        "Characteristics": "1k 0402",
        "JLC": "",
        "MPN": "CR0402-FX-1001GLF",
        "MPN_ALT": "WR04X1001FTL",
        "Part number": "",
    },
)
r2 = Part(
    "R2",
    "Resistor_SMD:R_0402_1005Metric",
    footprint="Resistor_SMD:R_0402_1005Metric",
    value="1k",
    properties={
        "Characteristics": "1k 0402",
        "JLC": "",
        "MPN": "CR0402-FX-1001GLF",
        "MPN_ALT": "WR04X1001FTL",
        "Part number": "",
    },
)
r3 = Part(
    "R3",
    "Resistor_SMD:R_0402_1005Metric",
    footprint="Resistor_SMD:R_0402_1005Metric",
    value="1k",
    properties={
        "Characteristics": "1k 0402",
        "JLC": "",
        "MPN": "CR0402-FX-1001GLF",
        "MPN_ALT": "WR04X1001FTL",
        "Part number": "",
    },
)
r4 = Part(
    "R4",
    "Resistor_SMD:R_0402_1005Metric",
    footprint="Resistor_SMD:R_0402_1005Metric",
    value="1k",
    properties={
        "Characteristics": "1k 0402",
        "JLC": "",
        "MPN": "CR0402-FX-1001GLF",
        "MPN_ALT": "WR04X1001FTL",
        "Part number": "",
    },
)
r5 = Part(
    "R5",
    "Resistor_SMD:R_0402_1005Metric",
    footprint="Resistor_SMD:R_0402_1005Metric",
    value="1k",
    properties={
        "Characteristics": "1k 0402",
        "JLC": "",
        "MPN": "CR0402-FX-1001GLF",
        "MPN_ALT": "WR04X1001FTL",
        "Part number": "",
    },
)
r6 = Part(
    "R6",
    "Resistor_SMD:R_0402_1005Metric",
    footprint="Resistor_SMD:R_0402_1005Metric",
    value="1k",
    properties={
        "Characteristics": "1k 0402",
        "JLC": "",
        "MPN": "CR0402-FX-1001GLF",
        "MPN_ALT": "WR04X1001FTL",
        "Part number": "",
    },
)
r7 = Part(
    "R7",
    "Resistor_SMD:R_0603_1608Metric_2",
    footprint="Resistor_SMD:R_0603_1608Metric_2",
    value="47k",
    properties={"Characteristics": "47k 0603", "MPN": "CR0603-FX-4642ELF", "MPN_ALT": "WR06X473 JTL"},
)
r8 = Part(
    "R8",
    "Resistor_SMD:R_0402_1005Metric_25",
    footprint="Resistor_SMD:R_0402_1005Metric_25",
    value="10k",
    properties={
        "Characteristics": "10k 0402",
        "JLC": "",
        "MPN": "RC0402FR-0710KL",
        "MPN_ALT": "WR04X1002FTL",
        "Part number": "",
    },
)
r9 = Part(
    "R9",
    "Resistor_SMD:R_0402_1005Metric_26",
    footprint="Resistor_SMD:R_0402_1005Metric_26",
    value="10k",
    properties={
        "Characteristics": "10k 0402",
        "JLC": "",
        "MPN": "RC0402FR-0710KL",
        "MPN_ALT": "WR04X1002FTL",
        "Part number": "",
    },
)
r10 = Part(
    "R10",
    "Resistor_SMD:R_0402_1005Metric",
    footprint="Resistor_SMD:R_0402_1005Metric",
    value="1k",
    properties={
        "Characteristics": "1k 0402",
        "JLC": "",
        "MPN": "CR0402-FX-1001GLF",
        "MPN_ALT": "WR04X1001FTL",
        "Part number": "",
    },
)
r11 = Part(
    "R11",
    "Resistor_SMD:R_0402_1005Metric",
    footprint="Resistor_SMD:R_0402_1005Metric",
    value="1k",
    properties={
        "Characteristics": "1k 0402",
        "JLC": "",
        "MPN": "CR0402-FX-1001GLF",
        "MPN_ALT": "WR04X1001FTL",
        "Part number": "",
    },
)
r12 = Part(
    "R12",
    "Resistor_SMD:R_0402_1005Metric_2",
    footprint="Resistor_SMD:R_0402_1005Metric_2",
    value="10k",
    properties={"Characteristics": "10k 0402", "MPN": "RC0402FR-0710KL", "MPN_ALT": "WR04X1002FTL"},
)
r13 = Part(
    "R13",
    "Resistor_SMD:R_0402_1005Metric_3",
    footprint="Resistor_SMD:R_0402_1005Metric_3",
    value="1k",
    properties={
        "Characteristics": "1k 0402",
        "MPN": "CR0402-FX-1001GLF",
        "MPN_ALT": "WR04X1001FTL",
        "Part number": "",
    },
)
r14 = Part(
    "R14",
    "Resistor_SMD:R_0402_1005Metric_4",
    footprint="Resistor_SMD:R_0402_1005Metric_4",
    value="1k",
    properties={
        "Characteristics": "1k 0402",
        "MPN": "CR0402-FX-1001GLF",
        "MPN_ALT": "WR04X1001FTL",
        "Part number": "",
    },
)
r15 = Part(
    "R15",
    "Resistor_SMD:R_0402_1005Metric_5",
    footprint="Resistor_SMD:R_0402_1005Metric_5",
    value="1.2K",
    properties={
        "Characteristics": "1.2k 0402",
        "MPN": "RC0402FR-071K2L",
        "MPN_ALT": "CR0402-JW-122GLF",
        "Part number": "",
    },
)
r16 = Part(
    "R16",
    "Resistor_SMD:R_0603_1608Metric",
    footprint="Resistor_SMD:R_0603_1608Metric",
    value="1M",
    properties={"JLC": "", "MPN": "", "Part number": ""},
    dnp=True,
)
r17 = Part(
    "R17",
    "Resistor_SMD:R_0402_1005Metric_5",
    footprint="Resistor_SMD:R_0402_1005Metric_5",
    value="510",
    properties={
        "Characteristics": "510R 0402",
        "MPN": "RC0402FR-07510RL",
        "MPN_ALT": "CR0402-FX-5100GLF",
        "Part number": "",
    },
)
r18 = Part(
    "R18",
    "Resistor_SMD:R_0402_1005Metric_6",
    footprint="Resistor_SMD:R_0402_1005Metric_6",
    value="0R",
    properties={
        "Characteristics": "0R 0402",
        "MPN": "RC0402FR-070RL",
        "MPN_ALT": "WR04X000 PTL",
        "Part number": "",
    },
)
r19 = Part(
    "R19",
    "Resistor_SMD:R_0402_1005Metric_7",
    footprint="Resistor_SMD:R_0402_1005Metric_7",
    value="510",
    properties={
        "Characteristics": "510R 0402",
        "MPN": "RC0402FR-07510RL",
        "MPN_ALT": "CR0402-FX-5100GLF",
        "Part number": "",
    },
)
r20 = Part(
    "R20",
    "Resistor_SMD:R_0402_1005Metric_8",
    footprint="Resistor_SMD:R_0402_1005Metric_8",
    value="5.1k",
    properties={
        "Characteristics": "5.1k 0402",
        "JLC": "",
        "MPN": "AC0402FR-135K1L",
        "MPN_ALT": "CR0402-FX-5101GLF",
        "Part number": "",
    },
)
r21 = Part(
    "R21",
    "Resistor_SMD:R_0402_1005Metric_9",
    footprint="Resistor_SMD:R_0402_1005Metric_9",
    value="5.1k",
    properties={
        "Characteristics": "5.1k 0402",
        "JLC": "",
        "MPN": "AC0402FR-135K1L",
        "MPN_ALT": "CR0402-FX-5101GLF",
        "Part number": "",
    },
)
r22 = Part(
    "R22",
    "Resistor_SMD:R_0402_1005Metric_10",
    footprint="Resistor_SMD:R_0402_1005Metric_10",
    value="68R",
    properties={
        "Characteristics": "68R 0402",
        "MPN": "RC0402FR-0768RL",
        "MPN_ALT": "WR04X68R0FTL",
        "Part number": "",
    },
)
r23 = Part(
    "R23",
    "Resistor_SMD:R_0402_1005Metric_10",
    footprint="Resistor_SMD:R_0402_1005Metric_10",
    value="68R",
    properties={
        "Characteristics": "68R 0402",
        "MPN": "RC0402FR-0768RL",
        "MPN_ALT": "WR04X68R0FTL",
        "Part number": "",
    },
)
r24 = Part(
    "R24",
    "Resistor_SMD:R_0402_1005Metric_10",
    footprint="Resistor_SMD:R_0402_1005Metric_10",
    value="68R",
    properties={
        "Characteristics": "68R 0402",
        "MPN": "RC0402FR-0768RL",
        "MPN_ALT": "WR04X68R0FTL",
        "Part number": "",
    },
)
r25 = Part(
    "R25",
    "Resistor_SMD:R_0402_1005Metric_10",
    footprint="Resistor_SMD:R_0402_1005Metric_10",
    value="68R",
    properties={
        "Characteristics": "68R 0402",
        "MPN": "RC0402FR-0768RL",
        "MPN_ALT": "WR04X68R0FTL",
        "Part number": "",
    },
)
r26 = Part(
    "R26",
    "Resistor_SMD:R_0402_1005Metric_10",
    footprint="Resistor_SMD:R_0402_1005Metric_10",
    value="68R",
    properties={
        "Characteristics": "68R 0402",
        "MPN": "RC0402FR-0768RL",
        "MPN_ALT": "WR04X68R0FTL",
        "Part number": "",
    },
)
r27 = Part(
    "R27",
    "Resistor_SMD:R_0402_1005Metric_10",
    footprint="Resistor_SMD:R_0402_1005Metric_10",
    value="68R",
    properties={
        "Characteristics": "68R 0402",
        "MPN": "RC0402FR-0768RL",
        "MPN_ALT": "WR04X68R0FTL",
        "Part number": "",
    },
)
r28 = Part(
    "R28",
    "Resistor_SMD:R_0402_1005Metric_10",
    footprint="Resistor_SMD:R_0402_1005Metric_10",
    value="68R",
    properties={
        "Characteristics": "68R 0402",
        "MPN": "RC0402FR-0768RL",
        "MPN_ALT": "WR04X68R0FTL",
        "Part number": "",
    },
)
r29 = Part(
    "R29",
    "Resistor_SMD:R_0402_1005Metric_10",
    footprint="Resistor_SMD:R_0402_1005Metric_10",
    value="68R",
    properties={
        "Characteristics": "68R 0402",
        "MPN": "RC0402FR-0768RL",
        "MPN_ALT": "WR04X68R0FTL",
        "Part number": "",
    },
)
r30 = Part(
    "R30",
    "Resistor_SMD:R_0402_1005Metric_11",
    footprint="Resistor_SMD:R_0402_1005Metric_11",
    value="10k",
    properties={"Characteristics": "10k 0402", "MPN": "RC0402FR-0710KL", "MPN_ALT": "WR04X1002FTL"},
)
r31 = Part(
    "R31",
    "Resistor_SMD:R_0402_1005Metric_10",
    footprint="Resistor_SMD:R_0402_1005Metric_10",
    value="10k",
    properties={"Characteristics": "10k 0402", "MPN": "RC0402FR-0710KL", "MPN_ALT": "WR04X1002FTL"},
)
r32 = Part(
    "R32",
    "Resistor_SMD:R_0402_1005Metric_11",
    footprint="Resistor_SMD:R_0402_1005Metric_11",
    value="10k",
    properties={"Characteristics": "10k 0402", "MPN": "RC0402FR-0710KL", "MPN_ALT": "WR04X1002FTL"},
)
r33 = Part(
    "R33",
    "Resistor_SMD:R_0402_1005Metric_12",
    footprint="Resistor_SMD:R_0402_1005Metric_12",
    value="10k",
    properties={
        "Characteristics": "10k 0402",
        "JLC": "",
        "MPN": "RC0402FR-0710KL",
        "MPN_ALT": "WR04X1002FTL",
        "Part number": "",
    },
)
r41 = Part(
    "R41",
    "Resistor_SMD:R_0402_1005Metric_19",
    footprint="Resistor_SMD:R_0402_1005Metric_19",
    value="47R",
    properties={"Characteristics": "47 0402", "MPN": "RMCF0402JT47R0", "MPN_ALT": "WR04X470 JTL"},
)
r42 = Part(
    "R42",
    "Resistor_SMD:R_0402_1005Metric_20",
    footprint="Resistor_SMD:R_0402_1005Metric_20",
    value="10k",
    properties={
        "Characteristics": "10k 0402",
        "JLC": "",
        "MPN": "RC0402FR-0710KL",
        "MPN_ALT": "WR04X1002FTL",
        "Part number": "",
    },
    dnp=True,
)
r43 = Part(
    "R43",
    "Resistor_SMD:R_0402_1005Metric_21",
    footprint="Resistor_SMD:R_0402_1005Metric_21",
    value="10k",
    properties={
        "Characteristics": "10k 0402",
        "MPN": "RC0402FR-0710KL",
        "MPN_ALT": "WR04X1002FTL",
        "Part number": "",
    },
)
r44 = Part(
    "R44",
    "Resistor_SMD:R_0402_1005Metric_21",
    footprint="Resistor_SMD:R_0402_1005Metric_21",
    value="10k",
    properties={
        "Characteristics": "10k 0402",
        "MPN": "RC0402FR-0710KL",
        "MPN_ALT": "WR04X1002FTL",
        "Part number": "",
    },
)
r45 = Part(
    "R45",
    "Resistor_SMD:R_0402_1005Metric_22",
    footprint="Resistor_SMD:R_0402_1005Metric_22",
    value="10k",
    properties={
        "Characteristics": "10k 0402",
        "MPN": "RC0402FR-0710KL",
        "MPN_ALT": "WR04X1002FTL",
        "Part number": "",
    },
)
r46 = Part(
    "R46",
    "Resistor_SMD:R_0402_1005Metric_23",
    footprint="Resistor_SMD:R_0402_1005Metric_23",
    value="10k",
    properties={
        "Characteristics": "10k 0402",
        "MPN": "RC0402FR-0710KL",
        "MPN_ALT": "WR04X1002FTL",
        "Part number": "",
    },
)
r47 = Part(
    "R47",
    "Resistor_SMD:R_0402_1005Metric_24",
    footprint="Resistor_SMD:R_0402_1005Metric_24",
    value="10k",
    properties={
        "Characteristics": "10k 0402",
        "MPN": "RC0402FR-0710KL",
        "MPN_ALT": "WR04X1002FTL",
        "Part number": "",
    },
)
r48 = Part(
    "R48",
    "Resistor_SMD:R_0402_1005Metric_21",
    footprint="Resistor_SMD:R_0402_1005Metric_21",
    value="10k",
    properties={
        "Characteristics": "10k 0402",
        "MPN": "RC0402FR-0710KL",
        "MPN_ALT": "WR04X1002FTL",
        "Part number": "",
    },
)
sw1 = Part(
    "SW1",
    "TinyTapeout:434121025816",
    footprint="TinyTapeout:434121025816",
    value="434121025816",
    properties={
        "Characteristics": "MOM SPST NO",
        "MPN": "434121025816",
        "MPN_ALT": "TS09-63-25-R-260-SMT-TR",
    },
)
sw2 = Part(
    "SW2",
    "TinyTapeout:434121025816_2",
    footprint="TinyTapeout:434121025816_2",
    value="434121025816",
    properties={
        "Characteristics": "MOM SPST NO",
        "MPN": "434121025816",
        "MPN_ALT": "TS09-63-25-R-260-SMT-TR",
    },
)
sw3 = Part(
    "SW3",
    "TinyTapeout:434121025816_3",
    footprint="TinyTapeout:434121025816_3",
    value="434121025816",
    properties={
        "Characteristics": "MOM SPST NO",
        "MPN": "434121025816",
        "MPN_ALT": "TS09-63-25-R-260-SMT-TR",
    },
)
sw4 = Part(
    "SW4",
    "TinyTapeout:418121270808",
    footprint="TinyTapeout:418121270808",
    value="418121270808",
    properties={"Characteristics": "8 POS SPST DIP", "MPN": "418121270808", "MPN_ALT": "219-8MST"},
)
tp1 = Part(
    "TP1",
    "TestPoint:TestPoint_Pad_D1.5mm",
    footprint="TestPoint:TestPoint_Pad_D1.5mm",
    value="TestPoint",
)
u1 = Part(
    "U1",
    "TinyTapeout:WL_S7DS-157112V12700",
    footprint="TinyTapeout:WL_S7DS-157112V12700",
    value="157112V12700",
    properties={
        "Characteristics": " 7 SEGMENT COMMON CATHODE",
        "DigikeyPN": "732-157112V12700DKR-ND",
        "MPN": "157112V12700",
        "MPN_ALT": "GS3011CR-G",
    },
)
u2 = Part(
    "U2",
    "Package_TO_SOT_SMD:SOT-223-3_TabPin2",
    footprint="Package_TO_SOT_SMD:SOT-223-3_TabPin2",
    value="TLV1117LV33",
    properties={
        "Characteristics": "VREG 3.3V SOT-223-4",
        "MPN": "TLV1117LV33DCYR",
        "MPN_ALT": "AZ1117CH-3.3TRG1",
        "Part number": "",
    },
)
u3 = Part(
    "U3",
    "Package_TO_SOT_SMD:SOT-23-5",
    footprint="Package_TO_SOT_SMD:SOT-23-5",
    value="AP2112K-1.8",
    properties={
        "Characteristics": "VREG 1.7V SOT-25",
        "DigikeyPN": "AP2112K-1.8TRG1DICT-ND",
        "MPN": "AP2112K-1.8TRG1",
    },
)
u4 = Part(
    "U4",
    "Package_SO:TSSOP-16_4.4x5mm_P0.65mm",
    footprint="Package_SO:TSSOP-16_4.4x5mm_P0.65mm",
    value="74CBTLV3257",
    properties={"MPN": "74CBTLV3257PW,118"},
)
u7 = Part(
    "U7",
    "Package_SO:SOIC-8_5.23x5.23mm_P1.27mm_2",
    footprint="Package_SO:SOIC-8_5.23x5.23mm_P1.27mm_2",
    value="W25Q32JVSS",
    properties={"Characteristics": "", "DigikeyPN": "W25Q32JVSSIQ-ND", "MPN": "W25Q32JVSSIQ"},
    dnp=True,
)
x1 = Part(
    "X1",
    "Oscillator:Oscillator_SMD_ECS_2520MV-xxx-xx-4Pin_2.5x2.0mm",
    footprint="Oscillator:Oscillator_SMD_ECS_2520MV-xxx-xx-4Pin_2.5x2.0mm",
    value="20MHz",
    properties={"DigikeyPN": "1923-830208220401DKR-ND", "MPN": "830208220401", "Part number": "830208220401"},
)
c29 = Part(
    "C29",
    "Capacitor_SMD:C_0402_1005Metric_13",
    footprint="Capacitor_SMD:C_0402_1005Metric_13",
    value="6pF",
    properties={
        "Characteristics": "6pF 10% 50V XR 0402",
        "MPN": "CC0402BRNPO9BN6R0",
        "MPN_ALT": "0402N6R0D500CT",
    },
)
c30 = Part(
    "C30",
    "Capacitor_SMD:C_0402_1005Metric_14",
    footprint="Capacitor_SMD:C_0402_1005Metric_14",
    value="6pF",
    properties={"Characteristics": "6pF 10% 50V XR 0402", "MPN": "CC0402BRNPO9BN6R0"},
)
c31 = Part(
    "C31",
    "Capacitor_SMD:C_0402_1005Metric_15",
    footprint="Capacitor_SMD:C_0402_1005Metric_15",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "JLC": "",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
        "Part number": "",
    },
)
c32 = Part(
    "C32",
    "Capacitor_SMD:C_0603_1608Metric_9",
    footprint="Capacitor_SMD:C_0603_1608Metric_9",
    value="1uF",
    properties={
        "Characteristics": "1u 10V XR 0603",
        "MPN": "CL10A105KA8NNNC",
        "MPN_ALT": "C0603C105K4RAC7411",
    },
)
c33 = Part(
    "C33",
    "Capacitor_SMD:C_0402_1005Metric_16",
    footprint="Capacitor_SMD:C_0402_1005Metric_16",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
    },
)
c34 = Part(
    "C34",
    "Capacitor_SMD:C_0402_1005Metric_11",
    footprint="Capacitor_SMD:C_0402_1005Metric_11",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
    },
)
c35 = Part(
    "C35",
    "Capacitor_SMD:C_0402_1005Metric_11",
    footprint="Capacitor_SMD:C_0402_1005Metric_11",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
    },
)
c36 = Part(
    "C36",
    "Capacitor_SMD:C_0402_1005Metric_17",
    footprint="Capacitor_SMD:C_0402_1005Metric_17",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
    },
)
c37 = Part(
    "C37",
    "Capacitor_SMD:C_0603_1608Metric_10",
    footprint="Capacitor_SMD:C_0603_1608Metric_10",
    value="1uF",
    properties={
        "Characteristics": "1u 10V XR 0603",
        "MPN": "CL10A105KA8NNNC",
        "MPN_ALT": "C0603C105K4RAC7411",
    },
)
c38 = Part(
    "C38",
    "Capacitor_SMD:C_0402_1005Metric_12",
    footprint="Capacitor_SMD:C_0402_1005Metric_12",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
    },
)
c39 = Part(
    "C39",
    "Capacitor_SMD:C_0402_1005Metric_12",
    footprint="Capacitor_SMD:C_0402_1005Metric_12",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
    },
)
c40 = Part(
    "C40",
    "Capacitor_SMD:C_0402_1005Metric_18",
    footprint="Capacitor_SMD:C_0402_1005Metric_18",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
    },
)
c41 = Part(
    "C41",
    "Capacitor_SMD:C_0402_1005Metric_19",
    footprint="Capacitor_SMD:C_0402_1005Metric_19",
    value="100nF",
    properties={
        "Characteristics": "100n 10% 25V XR 0402",
        "MPN": "CL05A104KA5NNNC",
        "MPN_ALT": "GRM155R71E104KE14J",
    },
)
j10 = Part(
    "J10",
    "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical",
    footprint="Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical",
    value="Conn_01x02",
    dnp=True,
)
j11 = Part(
    "J11",
    "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical_SMD_Pin1Right",
    footprint="Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical_SMD_Pin1Right",
    value="Conn_01x06",
    properties={"MPN": "61300611121", "Part number": "", "Status": ""},
    dnp=True,
)
r34 = Part(
    "R34",
    "Resistor_SMD:R_0402_1005Metric_13",
    footprint="Resistor_SMD:R_0402_1005Metric_13",
    value="10k",
    properties={
        "Characteristics": "10k 0402",
        "JLC": "",
        "MPN": "RC0402FR-0710KL",
        "MPN_ALT": "WR04X1002FTL",
        "Part number": "",
    },
)
r35 = Part(
    "R35",
    "Resistor_SMD:R_0402_1005Metric_14",
    footprint="Resistor_SMD:R_0402_1005Metric_14",
    value="10k",
    properties={
        "Characteristics": "10k 0402",
        "JLC": "",
        "MPN": "RC0402FR-0710KL",
        "MPN_ALT": "WR04X1002FTL",
        "Part number": "",
    },
)
r36 = Part(
    "R36",
    "Resistor_SMD:R_0402_1005Metric_15",
    footprint="Resistor_SMD:R_0402_1005Metric_15",
    value="10k",
    properties={"Characteristics": "10k 0402", "MPN": "RC0402FR-0710KL", "MPN_ALT": "WR04X1002FTL"},
)
r37 = Part(
    "R37",
    "Resistor_SMD:R_0402_1005Metric_16",
    footprint="Resistor_SMD:R_0402_1005Metric_16",
    value="1k",
    properties={
        "Characteristics": "1k 0402",
        "MPN": "CR0402-FX-1001GLF",
        "MPN_ALT": "WR04X1001FTL",
        "Part number": "",
    },
)
r38 = Part(
    "R38",
    "Resistor_SMD:R_0402_1005Metric_17",
    footprint="Resistor_SMD:R_0402_1005Metric_17",
    value="10k",
    properties={
        "Characteristics": "10k 0402",
        "JLC": "",
        "MPN": "RC0402FR-0710KL",
        "MPN_ALT": "WR04X1002FTL",
        "Part number": "",
    },
)
r39 = Part(
    "R39",
    "Resistor_SMD:R_0402_1005Metric_10",
    footprint="Resistor_SMD:R_0402_1005Metric_10",
    value="10k",
    properties={
        "Characteristics": "10k 0402",
        "JLC": "",
        "MPN": "RC0402FR-0710KL",
        "MPN_ALT": "WR04X1002FTL",
        "Part number": "",
    },
)
r40 = Part(
    "R40",
    "Resistor_SMD:R_0402_1005Metric_18",
    footprint="Resistor_SMD:R_0402_1005Metric_18",
    value="10k",
    properties={
        "Characteristics": "10k 0402",
        "JLC": "",
        "MPN": "RC0402FR-0710KL",
        "MPN_ALT": "WR04X1002FTL",
        "Part number": "",
    },
)
u5 = Part(
    "U5",
    "Package_SO:SOIC-8_5.23x5.23mm_P1.27mm",
    footprint="Package_SO:SOIC-8_5.23x5.23mm_P1.27mm",
    value="W25Q32JVSS",
    properties={"Characteristics": "", "DigikeyPN": "W25Q32JVSSIQ-ND", "MPN": "W25Q32JVSSIQ"},
)
u6 = Part(
    "U6",
    "Package_DFN_QFN:QFN-56-1EP_7x7mm_P0.4mm_EP3.2x3.2mm",
    footprint="Package_DFN_QFN:QFN-56-1EP_7x7mm_P0.4mm_EP3.2x3.2mm",
    value="RP2040",
    properties={"DigikeyPN": "2648-SC0914(13)CT-ND", "MPN": "SC0914(13)"},
)
y1 = Part(
    "Y1",
    "Crystal:Crystal_SMD_3225-4Pin_3.2x2.5mm",
    footprint="Crystal:Crystal_SMD_3225-4Pin_3.2x2.5mm",
    value="12.0MHz",
    properties={"DigikeyPN": "1923-830108206909DKR-ND", "MPN": "830108206909"},
)

root = Module("root")
rp2040 = Module("rp2040")

root.add(
    c1,
    c2,
    c3,
    c4,
    c5,
    c6,
    c7,
    c8,
    c9,
    c10,
    c11,
    c12,
    c13,
    c14,
    c15,
    c16,
    c17,
    c18,
    c19,
    c20,
    c21,
    c22,
    c23,
    c24,
    c25,
    c26,
    c27,
    c28,
    c42,
    c43,
    c56,
    c57,
    c58,
    c59,
    c60,
    c61,
    d1,
    d2,
    d3,
    d4,
    f1,
    fid1,
    fid2,
    fid3,
    j1,
    j2,
    j3,
    j4,
    j5,
    j6,
    j7,
    j8,
    j9,
    j12,
    j13,
    j14,
    j15,
    j16,
    j17,
    j18,
    jp1,
    jp2,
    jp3,
    jp4,
    jp5,
    jp6,
    jp7,
    jp8,
    mt1,
    mt2,
    mt3,
    mt4,
    nt1,
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
    r22,
    r23,
    r24,
    r25,
    r26,
    r27,
    r28,
    r29,
    r30,
    r31,
    r32,
    r33,
    r41,
    r42,
    r43,
    r44,
    r45,
    r46,
    r47,
    r48,
    sw1,
    sw2,
    sw3,
    sw4,
    tp1,
    u1,
    u2,
    u3,
    u4,
    u7,
    x1,
)
rp2040.add(
    c29,
    c30,
    c31,
    c32,
    c33,
    c34,
    c35,
    c36,
    c37,
    c38,
    c39,
    c40,
    c41,
    j10,
    j11,
    r34,
    r35,
    r36,
    r37,
    r38,
    r39,
    r40,
    u5,
    u6,
    y1,
)
design.add(
    g_1,
    g_2,
    g_3,
    g_4,
    ref_1,
    ref_2,
    ref_3,
    stitch1_1,
    stitch1_2,
    stitch1_3,
    stitch1_4,
    stitch1_5,
    stitch1_6,
    stitch1_7,
    stitch1_8,
    stitch1_9,
    stitch1_10,
    stitch1_11,
    stitch1_12,
    stitch1_13,
    stitch1_14,
    stitch1_15,
    stitch1_16,
    stitch1_17,
    stitch1_18,
    stitch1_19,
    stitch1_20,
    stitch1_21,
    stitch1_22,
    stitch1_23,
    stitch1_24,
    stitch1_25,
    stitch1_26,
    stitch1_27,
    stitch1_28,
    stitch1_29,
    stitch1_30,
    stitch1_31,
    stitch1_32,
    stitch1_33,
    stitch1_34,
    stitch1_35,
    stitch1_36,
    stitch1_37,
    stitch1_38,
    stitch1_39,
    stitch1_40,
    stitch1_41,
    stitch1_42,
    stitch1_43,
    stitch1_44,
    stitch1_45,
    stitch1_46,
    stitch1_47,
    stitch1_48,
    stitch1_49,
    stitch1_50,
    stitch1_51,
    stitch1_52,
    stitch1_53,
    stitch1_54,
    stitch1_55,
    stitch1_56,
    stitch1_57,
    stitch1_58,
    stitch1_59,
    stitch1_60,
    stitch1_61,
    stitch1_62,
    stitch1_63,
    stitch1_64,
    stitch1_65,
    stitch1_66,
    stitch1_67,
    stitch1_68,
    stitch1_69,
    stitch1_70,
    stitch1_71,
    stitch1_72,
    stitch1_73,
    stitch1_74,
    stitch1_75,
    stitch1_76,
    stitch1_77,
    stitch1_78,
    stitch1_79,
    stitch1_80,
    stitch1_81,
    stitch1_82,
    stitch1_83,
    stitch1_84,
    stitch1_85,
    stitch1_86,
    stitch1_87,
    stitch1_88,
    stitch1_89,
    stitch1_90,
    stitch1_91,
    stitch1_92,
    stitch1_93,
    stitch1_94,
    stitch1_95,
    stitch1_96,
    stitch1_97,
    stitch1_98,
    stitch1_99,
    stitch1_100,
    stitch1_101,
    stitch1_102,
    stitch1_103,
    stitch1_104,
    stitch1_105,
    stitch1_106,
    stitch1_107,
    stitch1_108,
    stitch1_109,
    stitch1_110,
    stitch1_111,
    stitch1_112,
    stitch1_113,
    stitch1_114,
    stitch1_115,
    stitch1_116,
    stitch1_117,
    stitch1_118,
    stitch1_119,
    stitch1_120,
    stitch1_121,
    stitch1_122,
    stitch1_123,
    stitch1_124,
    stitch1_125,
    stitch1_126,
    stitch1_127,
    stitch1_128,
    stitch1_129,
    stitch1_130,
    stitch2,
    stitch3,
    stitch4,
    stitch5,
    stitch6_1,
    stitch6_2,
    stitch6_3,
    stitch7,
    stitch8,
    stitch9,
    stitch10,
    stitch11,
    stitch12,
    stitch13,
    stitch14,
    stitch15,
    stitch16,
    stitch17,
    stitch18,
    ttlogo,
    z2alogo,
    kibuzzard_63fe0d11,
    root,
    rp2040,
)

connect(
    net_1v8,
    c11["1"],
    c13["1"],
    c20["2"],
    c21["2"],
    c22["2"],
    c24["2"],
    c25["2"],
    j4["A7"],
    j4["B14"],
    j4["B16"],
    j4["B33"],
    j4["B35"],
    j9["2"],
    r18["1"],
    u3["5"],
)
connect(
    net_3v3,
    c1["1"],
    c4["1"],
    c5["2"],
    c7["1"],
    c8["1"],
    c9["2"],
    c10["1"],
    c12["1"],
    c14["1"],
    c15["2"],
    c16["2"],
    c17["2"],
    c18["1"],
    c19["2"],
    c23["2"],
    c26["2"],
    c27["1"],
    c28["2"],
    c31["2"],
    c33["1"],
    c34["1"],
    c35["1"],
    c36["1"],
    c37["1"],
    c38["1"],
    c39["1"],
    c43["2"],
    c56["1"],
    c57["2"],
    c58["1"],
    c59["2"],
    c60["1"],
    c61["2"],
    j3["6"],
    j3["12"],
    j4["A19"],
    j4["B1"],
    j4["B3"],
    j4["B15"],
    j4["B17"],
    j4["B37"],
    j4["B39"],
    j5["6"],
    j5["12"],
    j6["6"],
    j6["12"],
    j9["3"],
    j9["21"],
    j11["1"],
    j12["6"],
    j12["12"],
    j13["6"],
    j13["12"],
    j14["6"],
    j14["12"],
    r1["1"],
    r2["1"],
    r3["1"],
    r4["1"],
    r5["1"],
    r6["1"],
    r8["1"],
    r9["1"],
    r10["1"],
    r11["1"],
    r17["1"],
    r19["1"],
    r32["1"],
    r33["1"],
    r34["1"],
    r35["1"],
    r36["1"],
    r38["1"],
    r39["1"],
    r40["1"],
    r42["1"],
    r43["1"],
    r44["1"],
    r45["1"],
    r46["1"],
    r47["1"],
    r48["1"],
    sw1["2"],
    u2["2"],
    u3["1"],
    u3["3"],
    u4["16"],
    u5["8"],
    u6["1"],
    u6["10"],
    u6["22"],
    u6["33"],
    u6["42"],
    u6["43"],
    u6["44"],
    u6["48"],
    u6["49"],
    u7["8"],
    x1["4"],
)
connect(net_5v, c6["1"], f1["2"], j1["2"], j9["23"], r15["1"], u2["3"])
connect(cc1, j15["A5"], r21["1"])
connect(cc2, j15["B5"], r20["1"])
connect(rp2040_dvdd, c32["2"], c40["1"], c41["1"], u6["23"], u6["45"], u6["50"])
connect(rp2040_qspi_clk, j11["3"], r34["2"], u5["6"], u6["52"])
connect(rp2040_qspi_sd0, j11["4"], r39["2"], u5["5"], u6["53"])
connect(rp2040_qspi_sd1, j11["5"], r40["2"], u5["2"], u6["55"])
connect(rp2040_qspi_sd2, r35["2"], u5["3"], u6["54"])
connect(rp2040_qspi_sd3, r38["2"], u5["7"], u6["51"])
connect(rp2040_run, j10["2"], r36["2"], u6["26"])
connect(rp2040_swclk, j7["2"], u6["24"])
connect(rp2040_swdio, j7["1"], u6["25"])
connect(crvrst, c42["2"], j4["A12"], r42["2"], tp1["1"])
connect(caravel_csb, j4["A14"], r43["2"], u7["1"])
connect(caravel_d0, j4["A16"], r46["2"], u7["5"])
connect(caravel_d1, j4["A17"], r47["2"], u7["2"])
connect(caravel_sck, j4["A13"], r48["2"], u7["6"])
connect(
    gnd,
    c2["2"],
    c3["2"],
    c4["2"],
    c5["1"],
    c6["2"],
    c7["2"],
    c8["2"],
    c9["1"],
    c10["2"],
    c11["2"],
    c12["2"],
    c13["2"],
    c14["2"],
    c15["1"],
    c16["1"],
    c17["1"],
    c18["2"],
    c19["1"],
    c20["1"],
    c21["1"],
    c22["1"],
    c23["1"],
    c24["1"],
    c25["1"],
    c26["1"],
    c27["2"],
    c28["1"],
    c29["2"],
    c30["2"],
    c31["1"],
    c32["1"],
    c33["2"],
    c34["2"],
    c35["2"],
    c36["2"],
    c37["2"],
    c38["2"],
    c39["2"],
    c40["2"],
    c41["2"],
    c42["1"],
    c43["1"],
    c56["2"],
    c57["1"],
    c58["2"],
    c59["1"],
    c60["2"],
    c61["1"],
    d1["1"],
    d2["1"],
    d3["1"],
    j1["1"],
    j3["5"],
    j3["11"],
    j4["A2"],
    j4["A9"],
    j4["A10"],
    j4["A15"],
    j4["A20"],
    j4["A25"],
    j4["A29"],
    j4["A30"],
    j4["A40"],
    j4["B2"],
    j4["B4"],
    j4["B12"],
    j4["B13"],
    j4["B18"],
    j4["B19"],
    j4["B20"],
    j4["B24"],
    j4["B25"],
    j4["B31"],
    j4["B34"],
    j4["B36"],
    j4["B38"],
    j4["B40"],
    j5["5"],
    j5["11"],
    j6["5"],
    j6["11"],
    j9["1"],
    j9["4"],
    j9["8"],
    j9["15"],
    j9["19"],
    j9["22"],
    j9["24"],
    j10["1"],
    j11["6"],
    j12["5"],
    j12["11"],
    j13["5"],
    j13["11"],
    j14["5"],
    j14["11"],
    j15["A1_B12"],
    j15["B1_A12"],
    mt1["1"],
    mt2["1"],
    mt3["1"],
    mt4["1"],
    r7["2"],
    r14["2"],
    r16["2"],
    r20["2"],
    r21["2"],
    r30["2"],
    r31["2"],
    stitch1_1["1"],
    stitch1_2["1"],
    stitch1_3["1"],
    stitch1_4["1"],
    stitch1_5["1"],
    stitch1_6["1"],
    stitch1_7["1"],
    stitch1_8["1"],
    stitch1_9["1"],
    stitch1_10["1"],
    stitch1_11["1"],
    stitch1_12["1"],
    stitch1_13["1"],
    stitch1_14["1"],
    stitch1_15["1"],
    stitch1_16["1"],
    stitch1_17["1"],
    stitch1_18["1"],
    stitch1_19["1"],
    stitch1_20["1"],
    stitch1_21["1"],
    stitch1_22["1"],
    stitch1_23["1"],
    stitch1_24["1"],
    stitch1_25["1"],
    stitch1_26["1"],
    stitch1_27["1"],
    stitch1_28["1"],
    stitch1_29["1"],
    stitch1_30["1"],
    stitch1_31["1"],
    stitch1_32["1"],
    stitch1_33["1"],
    stitch1_34["1"],
    stitch1_35["1"],
    stitch1_36["1"],
    stitch1_37["1"],
    stitch1_38["1"],
    stitch1_39["1"],
    stitch1_40["1"],
    stitch1_41["1"],
    stitch1_42["1"],
    stitch1_43["1"],
    stitch1_44["1"],
    stitch1_45["1"],
    stitch1_46["1"],
    stitch1_47["1"],
    stitch1_48["1"],
    stitch1_49["1"],
    stitch1_50["1"],
    stitch1_51["1"],
    stitch1_52["1"],
    stitch1_53["1"],
    stitch1_54["1"],
    stitch1_55["1"],
    stitch1_56["1"],
    stitch1_57["1"],
    stitch1_58["1"],
    stitch1_59["1"],
    stitch1_60["1"],
    stitch1_61["1"],
    stitch1_62["1"],
    stitch1_63["1"],
    stitch1_64["1"],
    stitch1_65["1"],
    stitch1_66["1"],
    stitch1_67["1"],
    stitch1_68["1"],
    stitch1_69["1"],
    stitch1_70["1"],
    stitch1_71["1"],
    stitch1_72["1"],
    stitch1_73["1"],
    stitch1_74["1"],
    stitch1_75["1"],
    stitch1_76["1"],
    stitch1_77["1"],
    stitch1_78["1"],
    stitch1_79["1"],
    stitch1_80["1"],
    stitch1_81["1"],
    stitch1_82["1"],
    stitch1_83["1"],
    stitch1_84["1"],
    stitch1_85["1"],
    stitch1_86["1"],
    stitch1_87["1"],
    stitch1_88["1"],
    stitch1_89["1"],
    stitch1_90["1"],
    stitch1_91["1"],
    stitch1_92["1"],
    stitch1_93["1"],
    stitch1_94["1"],
    stitch1_95["1"],
    stitch1_96["1"],
    stitch1_97["1"],
    stitch1_98["1"],
    stitch1_99["1"],
    stitch1_100["1"],
    stitch1_101["1"],
    stitch1_102["1"],
    stitch1_103["1"],
    stitch1_104["1"],
    stitch1_105["1"],
    stitch1_106["1"],
    stitch1_107["1"],
    stitch1_108["1"],
    stitch1_109["1"],
    stitch1_110["1"],
    stitch1_111["1"],
    stitch1_112["1"],
    stitch1_113["1"],
    stitch1_114["1"],
    stitch1_115["1"],
    stitch1_116["1"],
    stitch1_117["1"],
    stitch1_118["1"],
    stitch1_119["1"],
    stitch1_120["1"],
    stitch1_121["1"],
    stitch1_122["1"],
    stitch1_123["1"],
    stitch1_124["1"],
    stitch1_125["1"],
    stitch1_126["1"],
    stitch1_127["1"],
    stitch1_128["1"],
    stitch1_129["1"],
    stitch1_130["1"],
    stitch2["1"],
    stitch3["1"],
    stitch4["1"],
    stitch5["1"],
    stitch6_1["1"],
    stitch6_2["1"],
    stitch6_3["1"],
    stitch7["1"],
    stitch8["1"],
    stitch9["1"],
    stitch10["1"],
    stitch11["1"],
    stitch12["1"],
    stitch13["1"],
    stitch14["1"],
    stitch15["1"],
    stitch16["1"],
    stitch17["1"],
    stitch18["1"],
    sw2["1"],
    u1["3"],
    u1["8"],
    u2["1"],
    u3["2"],
    u4["8"],
    u4["15"],
    u5["4"],
    u6["19"],
    u6["57"],
    u7["4"],
    x1["2"],
    y1["2"],
    y1["4"],
)
connect(hk_csb, j4["A23"], j9["7"], nt1["1"], r33["2"], u6["3"])
connect(hk_sck, j4["A26"], j9["6"], u6["4"])
connect(hk_sdi, j4["A24"], j9["9"], u4["5"])
connect(hk_sdo, j4["A21"], j9["10"], u4["14"])
connect(mux_sel, nt1["2"], u4["1"])
connect(net_c1_pad2, c1["2"], r7["1"], r12["2"], sw1["1"])
connect(net_c3_pad1, c3["1"], j15["S1"], j15["S2"], j15["S3"], j15["S4"], r16["1"])
connect(net_c30_pad1, c30["1"], r37["1"], y1["3"])
connect(net_d1_a, d1["2"], r15["2"])
connect(net_d2_a, d2["2"], r17["2"])
connect(net_d3_a, d3["2"], r18["2"])
connect(net_d4_a, d4["2"], r19["2"])
connect(net_jp1_b, jp1["2"], r22["1"])
connect(net_jp2_b, jp2["2"], r23["1"])
connect(net_jp3_b, jp3["2"], r24["1"])
connect(net_jp4_b, jp4["2"], r25["1"])
connect(net_jp5_b, jp5["2"], r26["1"])
connect(net_jp6_b, jp6["2"], r27["1"])
connect(net_jp7_b, jp7["2"], r28["1"])
connect(net_jp8_b, jp8["2"], r29["1"])
connect(net_r1_pad2, r1["2"], sw4["8"])
connect(net_r10_pad2, r10["2"], sw4["2"])
connect(net_r11_pad2, r11["2"], sw4["1"])
connect(net_r13_pad1, r8["2"], r13["1"], sw2["2"])
connect(net_r14_pad1, r14["1"], sw3["1"])
connect(net_r2_pad2, r2["2"], sw4["7"])
connect(net_r3_pad2, r3["2"], sw4["6"])
connect(net_r4_pad2, r4["2"], sw4["5"])
connect(net_r5_pad2, r5["2"], sw4["4"])
connect(net_r6_pad2, r6["2"], sw4["3"])
connect(net_u1_a, r22["2"], u1["7"])
connect(net_u1_b, r23["2"], u1["6"])
connect(net_u1_c, r24["2"], u1["4"])
connect(net_u1_d, r25["2"], u1["2"])
connect(net_u1_dp, r29["2"], u1["5"])
connect(net_u1_e, r26["2"], u1["1"])
connect(net_u1_f, r27["2"], u1["9"])
connect(net_u1_g, r28["2"], u1["10"])
connect(net_u6_xin, c29["1"], u6["20"], y1["1"])
connect(net_u6_xout, r37["2"], u6["21"])
connect(net_u7_io2, r44["2"], u7["3"])
connect(net_u7_io3, r45["2"], u7["7"])
connect(rpio29, j9["20"], u6["41"])
connect(rp_proj_clk, r41["1"], u6["2"])
connect(sdi_out0, u4["7"], u6["5"])
connect(sdo_out1, u4["12"], u6["6"])
connect(vbus, f1["1"], j15["A4_B9"], j15["B4_A9"])
connect(boot_mode, j11["2"], r9["2"], sw3["2"], u5["1"], u6["56"])
connect(cinc_out3, u4["9"], u6["11"])
connect(ctrl_ena, j4["A1"], j9["17"], r31["1"], u6["8"])
connect(ctrl_sel_inc, j4["A3"], j9["14"], r30["1"], u4["11"])
connect(gpio, d4["1"], j4["A18"])
connect(in0, j2["1"], j3["1"], j4["A32"], j13["1"], sw4["16"], u6["12"])
connect(in1, j2["2"], j3["2"], j4["A33"], j13["4"], sw4["15"], u6["13"])
connect(in2, j2["3"], j3["3"], j4["A34"], j12["3"], j13["2"], sw4["14"], u6["14"])
connect(in3, j2["4"], j3["4"], j4["A35"], j14["9"], sw4["13"], u6["15"])
connect(in4, j3["7"], j4["A36"], j13["7"], sw4["12"], u6["28"])
connect(in5, j3["8"], j4["A37"], j13["10"], j14["7"], sw4["11"], u6["29"])
connect(in6, j3["9"], j4["A38"], j13["8"], sw4["10"], u6["30"])
connect(in7, j3["10"], j4["A39"], sw4["9"], u6["31"])
connect(mio33, j4["A4"], j9["18"])
connect(mio35, j4["A6"], j9["16"])
connect(mio37, j4["A5"], j9["13"])
connect(mprj_io0, j4["A22"], j9["11"])
connect(out0, j1["3"], j4["B32"], j6["1"], jp1["1"], u4["6"])
connect(out1, j1["4"], j4["B29"], j6["2"], jp2["1"], u4["13"])
connect(out2, j1["5"], j4["B30"], j6["3"], jp3["1"], u4["3"])
connect(out3, j1["6"], j4["B27"], j6["4"], j12["2"], j13["3"], jp4["1"], u4["10"])
connect(out4, j4["B28"], j6["7"], j12["1"], j14["8"], jp5["1"], u6["16"])
connect(out5, j4["B23"], j6["8"], j12["4"], jp6["1"], u6["17"])
connect(out6, j4["B26"], j6["9"], j14["10"], jp7["1"], u6["18"])
connect(out7, j4["B21"], j6["10"], j12["8"], j13["9"], jp8["1"], u6["27"])
connect(project_clk, j4["A28"], j17["3"], r12["1"], r41["2"])
connect(uio0, j4["B22"], j5["1"], j8["1"], j12["7"], u6["32"])
connect(uio1, j4["B11"], j5["2"], j8["2"], j12["10"], u6["34"])
connect(uio2, j4["B9"], j5["3"], j8["3"], j12["9"], u6["35"])
connect(uio3, j4["B10"], j5["4"], j14["3"], j17["1"], u6["36"])
connect(uio4, j4["B7"], j5["7"], j14["1"], u6["37"])
connect(uio5, j4["B8"], j5["8"], j14["4"], u6["38"])
connect(uio6, j4["B5"], j5["9"], j14["2"], u6["39"])
connect(uio7, j4["B6"], j5["10"], u6["40"])
connect(usb_d, j15["A6"], j15["B6"], u6["47"])
connect(usb_d_2, j15["A7"], j15["B7"], u6["46"])
connect(usrclk2, j4["A27"], j9["5"])
connect(xclk, j4["A11"], x1["3"])
connect(crst_out2, u4["4"], u6["9"])
connect(ctrl_sel_rst, j4["A8"], j9["12"], r32["2"], u4["2"])
connect(project_rst, c2["1"], j4["A31"], j17["2"], r13["2"], u6["7"])

g_1.place(mm("6.6"), mm("-9.7"), rot=180, side="bottom")
g_2.place(mm("37.15"), mm("-14.08"), rot=180, side="bottom")
g_3.place(mm("37.2"), mm("-18.500375"), rot=180, side="bottom")
g_4.place(mm("46.55"), mm("25.9"))
ref_1.place(mm("37.0608"), mm("-3.234218"), rot=180, side="bottom")
ref_2.place(mm("37.163648"), mm("15.008261"), rot=180, side="bottom")
ref_3.place(mm("37.2"), mm("-33.6"), rot=180, side="bottom")
stitch1_1.place(mm("-42.8"), mm("-29.1"))
stitch1_2.place(mm("-42.8"), mm("-24.1"))
stitch1_3.place(mm("-42.8"), mm("21.6"))
stitch1_4.place(mm("-42.6"), mm("-37.8"))
stitch1_5.place(mm("-40.1"), mm("-15"))
stitch1_6.place(mm("-39.8"), mm("25.5"))
stitch1_7.place(mm("-36.3"), mm("-0.3"))
stitch1_8.place(mm("-35.4"), mm("-39.1"))
stitch1_9.place(mm("-35.4"), mm("-28.4"))
stitch1_10.place(mm("-35.05"), mm("-33.05"))
stitch1_11.place(mm("-35"), mm("15.4"))
stitch1_12.place(mm("-35"), mm("21.4"))
stitch1_13.place(mm("-34.9"), mm("-23.7"))
stitch1_14.place(mm("-34.9"), mm("-20.3"))
stitch1_15.place(mm("-34.8"), mm("-7.4"))
stitch1_16.place(mm("-33.2"), mm("-4.5"))
stitch1_17.place(mm("-33.2"), mm("5.2"))
stitch1_18.place(mm("-32.3"), mm("-20.2"))
stitch1_19.place(mm("-32.25"), mm("-45.7"))
stitch1_20.place(mm("-31.2"), mm("13.2"))
stitch1_21.place(mm("-31.1"), mm("-37.3"))
stitch1_22.place(mm("-31"), mm("-15.2"))
stitch1_23.place(mm("-31"), mm("-11.2"))
stitch1_24.place(mm("-31"), mm("-7.4"))
stitch1_25.place(mm("-31"), mm("21.4"))
stitch1_26.place(mm("-31"), mm("29.3"))
stitch1_27.place(mm("-25.9"), mm("20.6"))
stitch1_28.place(mm("-23.8"), mm("29.3"))
stitch1_29.place(mm("-23.5"), mm("-14.3"))
stitch1_30.place(mm("-23.3"), mm("-22.8"))
stitch1_31.place(mm("-20.5"), mm("-8.8"))
stitch1_32.place(mm("-19.9"), mm("26.4"))
stitch1_33.place(mm("-19.75"), mm("-36.5"))
stitch1_34.place(mm("-19.5"), mm("-38.8"))
stitch1_35.place(mm("-19.3"), mm("1.2"))
stitch1_36.place(mm("-19.1"), mm("15.6"))
stitch1_37.place(mm("-19"), mm("12.4"))
stitch1_38.place(mm("-17.5"), mm("-28.5"))
stitch1_39.place(mm("-17.5"), mm("14"))
stitch1_40.place(mm("-16.5"), mm("-33.7"))
stitch1_41.place(mm("-15.8"), mm("12.5"))
stitch1_42.place(mm("-15.8"), mm("15.7"))
stitch1_43.place(mm("-14.5"), mm("-35.9"))
stitch1_44.place(mm("-12.3"), mm("-22.3"))
stitch1_45.place(mm("-12.1"), mm("-10"))
stitch1_46.place(mm("-11.6"), mm("-32.7"))
stitch1_47.place(mm("-10.7"), mm("-38.8"))
stitch1_48.place(mm("-9.1"), mm("24.2"))
stitch1_49.place(mm("-9"), mm("19.7"))
stitch1_50.place(mm("-8.3"), mm("-37.7"))
stitch1_51.place(mm("-8"), mm("8.1"))
stitch1_52.place(mm("-8"), mm("15.5"))
stitch1_53.place(mm("-7.8"), mm("1.6"))
stitch1_54.place(mm("-7.8"), mm("28.9"))
stitch1_55.place(mm("-5.7"), mm("-7"))
stitch1_56.place(mm("-3.6"), mm("24.8"))
stitch1_57.place(mm("-3.3"), mm("15.4"))
stitch1_58.place(mm("-3.1"), mm("28.9"))
stitch1_59.place(mm("0.1"), mm("-6.8"))
stitch1_60.place(mm("0.4"), mm("-1.9"))
stitch1_61.place(mm("0.4"), mm("3"))
stitch1_62.place(mm("4.6"), mm("-41.1"))
stitch1_63.place(mm("5.3"), mm("-31.5"))
stitch1_64.place(mm("6.6"), mm("17.3"))
stitch1_65.place(mm("8.5"), mm("-28.3"))
stitch1_66.place(mm("9.5"), mm("-35"))
stitch1_67.place(mm("9.6"), mm("-41.1"))
stitch1_68.place(mm("11.4"), mm("-15.6"))
stitch1_69.place(mm("12.2"), mm("-41.1"))
stitch1_70.place(mm("13"), mm("4.2"))
stitch1_71.place(mm("13"), mm("25.3"))
stitch1_72.place(mm("13.1"), mm("-21"))
stitch1_73.place(mm("13.2"), mm("15.4"))
stitch1_74.place(mm("15.2"), mm("21.3"))
stitch1_75.place(mm("18.7"), mm("-30.8"))
stitch1_76.place(mm("18.7"), mm("-21.1"))
stitch1_77.place(mm("18.7"), mm("-15.8"))
stitch1_78.place(mm("18.7"), mm("-10.8"))
stitch1_79.place(mm("18.7"), mm("-6.6"))
stitch1_80.place(mm("18.7"), mm("0.5"))
stitch1_81.place(mm("18.7"), mm("7.4"))
stitch1_82.place(mm("18.7"), mm("15.4"))
stitch1_83.place(mm("19.7"), mm("28.2"))
stitch1_84.place(mm("19.8"), mm("-41.1"))
stitch1_85.place(mm("23.1"), mm("2.9"))
stitch1_86.place(mm("23.1"), mm("5.5"))
stitch1_87.place(mm("23.1"), mm("8"))
stitch1_88.place(mm("23.1"), mm("11"))
stitch1_89.place(mm("23.9"), mm("-41.1"))
stitch1_90.place(mm("27.4"), mm("-41.1"))
stitch1_91.place(mm("27.7"), mm("-30.7"))
stitch1_92.place(mm("27.7"), mm("-24.9"))
stitch1_93.place(mm("27.7"), mm("-16.4"))
stitch1_94.place(mm("27.8"), mm("-11.8"))
stitch1_95.place(mm("27.8"), mm("-4.3"))
stitch1_96.place(mm("27.8"), mm("1.9"))
stitch1_97.place(mm("27.8"), mm("7.1"))
stitch1_98.place(mm("27.8"), mm("12.4"))
stitch1_99.place(mm("28.1"), mm("22.5"))
stitch1_100.place(mm("30.1"), mm("-41.1"))
stitch1_101.place(mm("30.9"), mm("-39"))
stitch1_102.place(mm("35.4"), mm("-39"))
stitch1_103.place(mm("37.2"), mm("20.3"))
stitch1_104.place(mm("37.6"), mm("-41.1"))
stitch1_105.place(mm("40"), mm("27.7"))
stitch1_106.place(mm("40.1"), mm("-41.1"))
stitch1_107.place(mm("42.5"), mm("-8.6"))
stitch1_108.place(mm("42.5"), mm("-3"))
stitch1_109.place(mm("42.5"), mm("3.1"))
stitch1_110.place(mm("42.7"), mm("-41.1"))
stitch1_111.place(mm("43.35"), mm("20.3"))
stitch1_112.place(mm("43.6"), mm("11.5"))
stitch1_113.place(mm("45.2"), mm("-14.9"))
stitch1_114.place(mm("45.3"), mm("27.7"))
stitch1_115.place(mm("46.55"), mm("11.5"))
stitch1_116.place(mm("46.6"), mm("-24.7"))
stitch1_117.place(mm("48.3"), mm("-41.1"))
stitch1_118.place(mm("49.4"), mm("11.5"))
stitch1_119.place(mm("49.9"), mm("-20.6"))
stitch1_120.place(mm("51.8"), mm("-39.1"))
stitch1_121.place(mm("52.3"), mm("8.9"))
stitch1_122.place(mm("52.3"), mm("16.5"))
stitch1_123.place(mm("52.4"), mm("-24.9"))
stitch1_124.place(mm("52.7"), mm("-8.6"))
stitch1_125.place(mm("52.7"), mm("-3"))
stitch1_126.place(mm("54.2"), mm("-37.2"))
stitch1_127.place(mm("57.9"), mm("7.9"))
stitch1_128.place(mm("57.9"), mm("10.4"))
stitch1_129.place(mm("57.9"), mm("13"))
stitch1_130.place(mm("60.2"), mm("5.4"))
stitch2.place(mm("60.2"), mm("0.4"))
stitch3.place(mm("60.2"), mm("-4.6"))
stitch4.place(mm("60.2"), mm("-9.6"))
stitch5.place(mm("60.2"), mm("-14.6"))
stitch6_1.place(mm("-31"), mm("33.8"))
stitch6_2.place(mm("-0.6"), mm("33.7"))
stitch6_3.place(mm("60.2"), mm("-19.6"))
stitch7.place(mm("60.2"), mm("-24.6"))
stitch8.place(mm("60.2"), mm("-29.6"))
stitch9.place(mm("60.2"), mm("-34.6"))
stitch10.place(mm("4.48"), mm("33.7"))
stitch11.place(mm("9.56"), mm("33.7"))
stitch12.place(mm("14.64"), mm("33.7"))
stitch13.place(mm("19.72"), mm("33.7"))
stitch14.place(mm("24.8"), mm("33.7"))
stitch15.place(mm("29.88"), mm("33.7"))
stitch16.place(mm("34.96"), mm("33.7"))
stitch17.place(mm("40.04"), mm("33.7"))
stitch18.place(mm("45.12"), mm("33.7"))
ttlogo.place(mm("18.5"), mm("-28.92"))
z2alogo.place(mm("18.5"), mm("-7.491952"))
kibuzzard_63fe0d11.place(mm("55.5"), mm("-29"))
c1.place(mm("0.5"), mm("20.6"), rot=90)
c2.place(mm("20"), mm("19.6"))
c3.place(mm("-7.8"), mm("-41.2"), rot=90)
c4.place(mm("-26.48"), mm("27.855"), rot=90)
c5.place(mm("-25.1"), mm("27.6"), rot=-90)
c6.place(mm("-28.26"), mm("-32.79"), rot=180)
c7.place(mm("-23.65"), mm("-45.2"), rot=180)
c8.place(mm("4.575"), mm("23.4"))
c9.place(mm("4.875"), mm("24.6"), rot=180)
c10.place(mm("-27.55"), mm("-44.04"))
c11.place(mm("-23.35"), mm("-39.1"), rot=180)
c12.place(mm("-28"), mm("-45.7"))
c13.place(mm("-22.9"), mm("-37.6"), rot=180)
c14.place(mm("26.6"), mm("24.3"))
c15.place(mm("26.95"), mm("25.6"), rot=180)
c16.place(mm("22.675"), mm("21.24"))
c17.place(mm("22.675"), mm("19.74"))
c18.place(mm("25.175"), mm("8"), rot=180)
c19.place(mm("25.175"), mm("-35"))
c20.place(mm("25.175"), mm("-21"))
c21.place(mm("50.5"), mm("-40"), rot=180)
c22.place(mm("25.175"), mm("2.96"))
c23.place(mm("25.175"), mm("-37.5"))
c24.place(mm("25.175"), mm("5.5"))
c25.place(mm("50.5"), mm("-41.54"), rot=180)
c26.place(mm("25.175"), mm("11"))
c27.place(mm("-31.9"), mm("9.1"))
c28.place(mm("43.7"), mm("-31.3"), rot=180)
c42.place(mm("43.6"), mm("-36.7"), rot=90)
c43.place(mm("51.3"), mm("-14.3"), rot=180)
c56.place(mm("-34.8"), mm("11.1"), rot=-90)
c57.place(mm("-36.3"), mm("11.4"), rot=90)
c58.place(mm("-35"), mm("-34.9"), rot=-90)
c59.place(mm("-36.3"), mm("-34.6"), rot=90)
c60.place(mm("-35.1"), mm("-12.05"), rot=-90)
c61.place(mm("-36.35"), mm("-11.7"), rot=90)
d1.place(mm("57.3"), mm("-36.5"), rot=90)
d2.place(mm("52.3"), mm("-36.5"), rot=90)
d3.place(mm("48.2"), mm("-36.5"), rot=90)
d4.place(mm("49"), mm("-29"))
f1.place(mm("-24.81"), mm("-32.8025"), rot=180)
fid1.place(mm("-42"), mm("26"))
fid2.place(mm("-34.8"), mm("-44"))
fid3.place(mm("59.5"), mm("-38"))
j1.place(mm("51.5"), mm("31.5"), rot=-90)
j2.place(mm("-24.69"), mm("31.5"), rot=-90)
j3.place(mm("-22.155"), mm("28.955"), rot=90)
j4.place(mm("18.42"), mm("-13.4"))
j5.place(mm("0.705"), mm("28.955"), rot=90)
j6.place(mm("23.565"), mm("28.955"), rot=90)
j7.place(mm("18.42"), mm("11.6"), rot=-90)
j8.place(mm("21.045"), mm("31.5"), rot=-90)
j9.place(mm("51.5"), mm("-44.5"), rot=-90)
j12.place(mm("-39"), mm("10.22"))
j13.place(mm("-39"), mm("-12.64"))
j14.place(mm("-39"), mm("-35.5"))
j15.place(mm("-15.25"), mm("-44.5"), rot=180)
j16.place(mm("0.42"), mm("-13.4"))
j17.place(mm("-1.8"), mm("31.5"), rot=-90)
j18.place(mm("36.42"), mm("-13.4"))
jp1.place(mm("54.9"), mm("2.72"), rot=180)
jp2.place(mm("54.9"), mm("5.22"), rot=180)
jp3.place(mm("54.9"), mm("7.72"), rot=180)
jp4.place(mm("54.9"), mm("10.22"), rot=180)
jp5.place(mm("54.9"), mm("12.72"), rot=180)
jp6.place(mm("54.9"), mm("15.22"), rot=180)
jp7.place(mm("54.9"), mm("17.72"), rot=180)
jp8.place(mm("54.9"), mm("20.22"), rot=180)
mt1.place(mm("-39.75"), mm("30.75"), rot=90)
mt2.place(mm("57.25"), mm("30.75"))
mt3.place(mm("-39.75"), mm("-42.75"))
mt4.place(mm("57.25"), mm("-42.75"))
nt1.place(mm("-32.5"), mm("16.4"), rot=-90)
r1.place(mm("-28.6"), mm("-7.6"))
r2.place(mm("-28.6"), mm("-10.142858"))
r3.place(mm("-28.6"), mm("-12.685715"))
r4.place(mm("-28.6"), mm("-15.228572"))
r5.place(mm("-28.6"), mm("-17.771429"))
r6.place(mm("-28.6"), mm("-20.314286"))
r7.place(mm("-2"), mm("19.75"), rot=180)
r8.place(mm("17.6"), mm("21.1"), rot=90)
r9.place(mm("-36"), mm("-15"))
r10.place(mm("-28.6"), mm("-22.857143"))
r11.place(mm("-28.6"), mm("-25.4"))
r12.place(mm("-2"), mm("21.25"))
r13.place(mm("18.1"), mm("19.6"))
r14.place(mm("-41.9"), mm("-15"))
r15.place(mm("56"), mm("-36.8"), rot=90)
r16.place(mm("-6.3"), mm("-41.2"), rot=90)
r17.place(mm("51.05"), mm("-36.8"), rot=90)
r18.place(mm("46.9"), mm("-36.8"), rot=90)
r19.place(mm("51.75"), mm("-29"), rot=-90)
r20.place(mm("-16.6"), mm("-36.7"), rot=-90)
r21.place(mm("-13.3"), mm("-35.9"), rot=-90)
r22.place(mm("51.755"), mm("2.68"), rot=180)
r23.place(mm("51.755"), mm("5.185714"), rot=180)
r24.place(mm("51.755"), mm("7.691428"), rot=180)
r25.place(mm("51.755"), mm("10.197142"), rot=180)
r26.place(mm("51.755"), mm("12.702856"), rot=180)
r27.place(mm("51.755"), mm("15.20857"), rot=180)
r28.place(mm("51.755"), mm("17.714284"), rot=180)
r29.place(mm("51.755"), mm("20.22"), rot=180)
r30.place(mm("-6.5"), mm("-34.4"))
r31.place(mm("-6.5"), mm("-30.1"), rot=180)
r32.place(mm("-6.5"), mm("-28.8"))
r33.place(mm("-33"), mm("11.2"), rot=-90)
r41.place(mm("-4.25"), mm("20.4625"), rot=-90)
r42.place(mm("43.8"), mm("-38.7"))
r43.place(mm("49.8"), mm("-25"), rot=180)
r44.place(mm("49.8"), mm("-26.1"), rot=180)
r45.place(mm("49.8"), mm("-13.1"), rot=180)
r46.place(mm("47.8"), mm("-12.1"), rot=180)
r47.place(mm("49.8"), mm("-12.1"), rot=180)
r48.place(mm("47.8"), mm("-13.1"), rot=180)
sw1.place(mm("-2"), mm("24.5"), rot=180)
sw2.place(mm("20.5"), mm("24.5"), rot=180)
sw3.place(mm("-38.6"), mm("-18.4"))
sw4.place(mm("-21.5"), mm("-16.5"), rot=-90)
tp1.place(mm("41.8"), mm("-36.5"))
u1.place(mm("46.55"), mm("11.5"), rot=90)
u2.place(mm("-28.85"), mm("-38.5"), rot=90)
u3.place(mm("-23.4"), mm("-42"), rot=-90)
u4.place(mm("-29.5"), mm("13.5"), rot=90)
u7.place(mm("48.5"), mm("-19.5"), rot=-90)
x1.place(mm("43.9"), mm("-33.4"), rot=180)
c29.place(mm("-21.1"), mm("23.15"), rot=90)
c30.place(mm("-15.8"), mm("22.35"), rot=-90)
c31.place(mm("-21.95"), mm("1.1"))
c32.place(mm("-15.3"), mm("7.575"), rot=-90)
c33.place(mm("-12.4"), mm("8.1"), rot=90)
c34.place(mm("-11.45"), mm("10.6"))
c35.place(mm("-10.9"), mm("15.3"))
c36.place(mm("-16.1"), mm("20.25"))
c37.place(mm("-13.8"), mm("7.6"), rot=90)
c38.place(mm("-23.8"), mm("15.2"), rot=180)
c39.place(mm("-22.7"), mm("10.4"), rot=180)
c40.place(mm("-15.85"), mm("19.3"))
c41.place(mm("-17.7"), mm("7.95"), rot=90)
j10.place(mm("-41.81"), mm("5.24"), rot=90)
j11.place(mm("-26.9"), mm("5.38"), rot=90, side="bottom")
r34.place(mm("-19.6"), mm("5.05"), rot=180)
r35.place(mm("-31.25"), mm("5.465"))
r36.place(mm("-36.9"), mm("6.1"), rot=90)
r37.place(mm("-17.6"), mm("20"), rot=90)
r38.place(mm("-19.65"), mm("3.45"), rot=180)
r39.place(mm("-19.6"), mm("6.8"), rot=180)
r40.place(mm("-31.25"), mm("4.165"))
u5.place(mm("-25.5"), mm("4.5"))
u6.place(mm("-17.5"), mm("14"))
y1.place(mm("-18.5"), mm("22.75"))

design.zone(
    gnd,
    layers=("F.Cu", "B.Cu"),
    key="GND/1",
    outline=(
        (mm("-47.5"), mm("-49.5")),
        (mm("64.5"), mm("-49.5")),
        (mm("64.5"), mm("36.5")),
        (mm("-48"), mm("36.5")),
        (mm("-48"), mm("-49")),
    ),
    priority=1,
    clearance=mm("0.25"),
    thermal_spoke_width=mm("0.35"),
)
design.zone(
    gnd,
    layers=("In1.Cu", "In2.Cu"),
    name="INNERPLANES",
    outline=(
        (mm("-47.25"), mm("-49.75")),
        (mm("64.75"), mm("-49.75")),
        (mm("64.75"), mm("36.25")),
        (mm("-47.75"), mm("36.25")),
        (mm("-47.75"), mm("-49.25")),
    ),
    priority=1,
    clearance=mm("0.25"),
    thermal_spoke_width=mm("0.35"),
)

design.arc(
    "B.SilkS/arc/1",
    (mm("-35.8"), mm("-36.8")),
    (mm("-33.67868"), mm("-35.92132")),
    (mm("-32.8"), mm("-33.8")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.arc(
    "B.SilkS/arc/2",
    (mm("-35.8"), mm("-14")),
    (mm("-33.67868"), mm("-13.12132")),
    (mm("-32.8"), mm("-11")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.arc(
    "B.SilkS/arc/3",
    (mm("-35.8"), mm("8.9")),
    (mm("-33.67868"), mm("9.77868")),
    (mm("-32.8"), mm("11.9")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.arc(
    "B.SilkS/arc/4",
    (mm("-33.5"), mm("28.5")),
    (mm("-32.62132"), mm("26.37868")),
    (mm("-30.5"), mm("25.5")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.arc(
    "B.SilkS/arc/5",
    (mm("-32.8"), mm("-24.4")),
    (mm("-33.67868"), mm("-22.27868")),
    (mm("-35.8"), mm("-21.4")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.arc(
    "B.SilkS/arc/6",
    (mm("-32.8"), mm("-1.6")),
    (mm("-33.67868"), mm("0.52132")),
    (mm("-35.8"), mm("1.4")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.arc(
    "B.SilkS/arc/7",
    (mm("-32.8"), mm("21.3")),
    (mm("-33.67868"), mm("23.42132")),
    (mm("-35.8"), mm("24.3")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.arc(
    "B.SilkS/arc/8",
    (mm("-11.1"), mm("25.5")),
    (mm("-8.97868"), mm("26.37868")),
    (mm("-8.1"), mm("28.5")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.arc(
    "B.SilkS/arc/9",
    (mm("-3.1"), mm("28.5")),
    (mm("-2.22132"), mm("26.37868")),
    (mm("-0.1"), mm("25.5")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.arc(
    "B.SilkS/arc/10",
    (mm("19.3"), mm("25.5")),
    (mm("21.42132"), mm("26.37868")),
    (mm("22.3"), mm("28.5")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.arc(
    "B.SilkS/arc/11",
    (mm("22.3"), mm("28.5")),
    (mm("23.17868"), mm("26.37868")),
    (mm("25.3"), mm("25.5")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.arc(
    "B.SilkS/arc/12",
    (mm("44.7"), mm("25.5")),
    (mm("46.82132"), mm("26.37868")),
    (mm("47.7"), mm("28.5")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/1",
    (mm("-43"), mm("-36.8")),
    (mm("-35.8"), mm("-36.8")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/2",
    (mm("-43"), mm("-14")),
    (mm("-35.8"), mm("-14")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/3",
    (mm("-43"), mm("8.9")),
    (mm("-35.8"), mm("8.9")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/4",
    (mm("-42.895"), mm("-31.7")),
    (mm("-42.895"), mm("-34.35")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/5",
    (mm("-42.895"), mm("-8.8")),
    (mm("-42.895"), mm("-11.45")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/6",
    (mm("-42.895"), mm("14.125")),
    (mm("-42.895"), mm("11.475")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/7",
    (mm("-42.695"), mm("-31.7")),
    (mm("-42.695"), mm("-34.35")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/8",
    (mm("-42.695"), mm("-8.8")),
    (mm("-42.695"), mm("-11.45")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/9",
    (mm("-42.695"), mm("14.125")),
    (mm("-42.695"), mm("11.475")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/10",
    (mm("-40.395"), mm("-31.7")),
    (mm("-40.395"), mm("-34.35")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/11",
    (mm("-40.395"), mm("-8.8")),
    (mm("-40.395"), mm("-11.45")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/12",
    (mm("-40.395"), mm("14.125")),
    (mm("-40.395"), mm("11.475")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/13",
    (mm("-40.295"), mm("-31.7")),
    (mm("-40.295"), mm("-34.35")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/14",
    (mm("-40.295"), mm("-8.8")),
    (mm("-40.295"), mm("-11.45")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/15",
    (mm("-40.295"), mm("14.125")),
    (mm("-40.295"), mm("11.475")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/16",
    (mm("-40.195"), mm("-31.7")),
    (mm("-40.195"), mm("-34.35")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/17",
    (mm("-40.195"), mm("-8.8")),
    (mm("-40.195"), mm("-11.45")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/18",
    (mm("-40.195"), mm("14.125")),
    (mm("-40.195"), mm("11.475")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/19",
    (mm("-37.795"), mm("-31.7")),
    (mm("-37.795"), mm("-34.35")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/20",
    (mm("-37.795"), mm("-31.575")),
    (mm("-37.795"), mm("-34.225")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/21",
    (mm("-37.795"), mm("-8.875")),
    (mm("-37.795"), mm("-11.525")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/22",
    (mm("-37.795"), mm("-8.8")),
    (mm("-37.795"), mm("-11.45")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/23",
    (mm("-37.795"), mm("14.125")),
    (mm("-37.795"), mm("11.475")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/24",
    (mm("-36.5"), mm("-34.35")),
    (mm("-42.895"), mm("-34.35")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/25",
    (mm("-36.5"), mm("-34.2")),
    (mm("-42.895"), mm("-34.2")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/26",
    (mm("-36.5"), mm("-31.9")),
    (mm("-42.895"), mm("-31.9")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/27",
    (mm("-36.5"), mm("-31.7")),
    (mm("-42.895"), mm("-31.7")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/28",
    (mm("-36.5"), mm("-11.45")),
    (mm("-42.895"), mm("-11.45")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/29",
    (mm("-36.5"), mm("-11.3")),
    (mm("-42.895"), mm("-11.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/30",
    (mm("-36.5"), mm("-9")),
    (mm("-42.895"), mm("-9")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/31",
    (mm("-36.5"), mm("-8.8")),
    (mm("-42.895"), mm("-8.8")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/32",
    (mm("-36.5"), mm("11.475")),
    (mm("-42.895"), mm("11.475")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/33",
    (mm("-36.5"), mm("11.625")),
    (mm("-42.895"), mm("11.625")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/34",
    (mm("-36.5"), mm("13.925")),
    (mm("-42.895"), mm("13.925")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/35",
    (mm("-36.5"), mm("14.125")),
    (mm("-42.895"), mm("14.125")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/36",
    (mm("-36.495"), mm("-31.675")),
    (mm("-36.495"), mm("-34.325")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/37",
    (mm("-36.495"), mm("-31.55")),
    (mm("-36.495"), mm("-34.2")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/38",
    (mm("-36.495"), mm("-8.85")),
    (mm("-36.495"), mm("-11.5")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/39",
    (mm("-36.495"), mm("-8.775")),
    (mm("-36.495"), mm("-11.425")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/40",
    (mm("-36.495"), mm("14.15")),
    (mm("-36.495"), mm("11.5")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/41",
    (mm("-35.8"), mm("-21.4")),
    (mm("-43.3"), mm("-21.4")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/42",
    (mm("-35.8"), mm("1.4")),
    (mm("-43.3"), mm("1.4")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/43",
    (mm("-35.8"), mm("24.3")),
    (mm("-43.3"), mm("24.3")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/44",
    (mm("-33.7"), mm("32.8")),
    (mm("-23.535"), mm("32.8")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/45",
    (mm("-33.7"), mm("34.245")),
    (mm("-33.7"), mm("32.8")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/46",
    (mm("-33.6"), mm("34.245")),
    (mm("-33.6"), mm("32.8")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/47",
    (mm("-33.5"), mm("32.7")),
    (mm("-33.5"), mm("28.5")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/48",
    (mm("-32.8"), mm("-33.8")),
    (mm("-32.8"), mm("-24.4")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/49",
    (mm("-32.8"), mm("-11")),
    (mm("-32.8"), mm("-1.6")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/50",
    (mm("-32.8"), mm("11.9")),
    (mm("-32.8"), mm("21.3")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/51",
    (mm("-30.5"), mm("25.5")),
    (mm("-11.1"), mm("25.5")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/52",
    (mm("-23.6"), mm("34.245")),
    (mm("-23.6"), mm("32.8")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/53",
    (mm("-23.45"), mm("34.245")),
    (mm("-23.45"), mm("32.8")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/54",
    (mm("-21"), mm("27.6")),
    (mm("-18.35"), mm("27.6")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/55",
    (mm("-21"), mm("27.8")),
    (mm("-18.35"), mm("27.8")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/56",
    (mm("-21"), mm("30.1")),
    (mm("-18.35"), mm("30.1")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/57",
    (mm("-21"), mm("30.2")),
    (mm("-18.35"), mm("30.2")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/58",
    (mm("-21"), mm("30.3")),
    (mm("-18.35"), mm("30.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/59",
    (mm("-21"), mm("32.7")),
    (mm("-18.35"), mm("32.7")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/60",
    (mm("-21"), mm("34.295")),
    (mm("-21"), mm("27.6")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/61",
    (mm("-21"), mm("34.295")),
    (mm("-18.35"), mm("34.295")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/62",
    (mm("-20.8"), mm("34.295")),
    (mm("-20.8"), mm("27.6")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/63",
    (mm("-18.5"), mm("34.295")),
    (mm("-18.5"), mm("27.6")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/64",
    (mm("-18.35"), mm("34.295")),
    (mm("-18.35"), mm("27.6")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/65",
    (mm("-8.25"), mm("34.245")),
    (mm("-8.25"), mm("32.8")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/66",
    (mm("-8.2"), mm("-45.7")),
    (mm("-5.6"), mm("-45.7")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/67",
    (mm("-8.2"), mm("-45.5")),
    (mm("-5.6"), mm("-45.5")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/68",
    (mm("-8.2"), mm("-43.3")),
    (mm("-8.2"), mm("-45.7")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/69",
    (mm("-8.1"), mm("32.7")),
    (mm("-8.1"), mm("28.5")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/70",
    (mm("-8"), mm("-45.7")),
    (mm("-8"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/71",
    (mm("-7.9"), mm("-45.7")),
    (mm("-7.9"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/72",
    (mm("-5.9"), mm("-45.7")),
    (mm("-5.9"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/73",
    (mm("-5.8"), mm("-45.7")),
    (mm("-5.8"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/74",
    (mm("-5.6"), mm("-45.7")),
    (mm("-5.6"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/75",
    (mm("-5.6"), mm("-43.5")),
    (mm("-8.2"), mm("-43.5")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/76",
    (mm("-5.6"), mm("-43.3")),
    (mm("-8.2"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/77",
    (mm("-3.15"), mm("-45.7")),
    (mm("-0.55"), mm("-45.7")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/78",
    (mm("-3.15"), mm("-45.5")),
    (mm("-0.55"), mm("-45.5")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/79",
    (mm("-3.15"), mm("-43.3")),
    (mm("-3.15"), mm("-45.7")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/80",
    (mm("-3.1"), mm("32.7")),
    (mm("-3.1"), mm("28.5")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/81",
    (mm("-2.95"), mm("-45.7")),
    (mm("-2.95"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/82",
    (mm("-2.85"), mm("-45.7")),
    (mm("-2.85"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/83",
    (mm("-0.85"), mm("-45.7")),
    (mm("-0.85"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/84",
    (mm("-0.75"), mm("-45.7")),
    (mm("-0.75"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/85",
    (mm("-0.55"), mm("-45.7")),
    (mm("-0.55"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/86",
    (mm("-0.55"), mm("-43.5")),
    (mm("-3.15"), mm("-43.5")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/87",
    (mm("-0.55"), mm("-43.3")),
    (mm("-3.15"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/88",
    (mm("-0.1"), mm("25.5")),
    (mm("19.3"), mm("25.5")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/89",
    (mm("1.9"), mm("27.6")),
    (mm("4.55"), mm("27.6")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/90",
    (mm("1.9"), mm("27.8")),
    (mm("4.55"), mm("27.8")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/91",
    (mm("1.9"), mm("30.1")),
    (mm("4.55"), mm("30.1")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/92",
    (mm("1.9"), mm("30.2")),
    (mm("4.55"), mm("30.2")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/93",
    (mm("1.9"), mm("30.3")),
    (mm("4.55"), mm("30.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/94",
    (mm("1.9"), mm("32.7")),
    (mm("4.55"), mm("32.7")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/95",
    (mm("1.9"), mm("34.295")),
    (mm("1.9"), mm("27.6")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/96",
    (mm("1.9"), mm("34.295")),
    (mm("4.55"), mm("34.295")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/97",
    (mm("2.1"), mm("34.295")),
    (mm("2.1"), mm("27.6")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/98",
    (mm("4.4"), mm("34.295")),
    (mm("4.4"), mm("27.6")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/99",
    (mm("4.45"), mm("-45.7")),
    (mm("7.05"), mm("-45.7")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/100",
    (mm("4.45"), mm("-45.5")),
    (mm("7.05"), mm("-45.5")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/101",
    (mm("4.45"), mm("-43.3")),
    (mm("4.45"), mm("-45.7")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/102",
    (mm("4.55"), mm("34.295")),
    (mm("4.55"), mm("27.6")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/103",
    (mm("4.65"), mm("-45.7")),
    (mm("4.65"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/104",
    (mm("4.75"), mm("-45.7")),
    (mm("4.75"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/105",
    (mm("6.75"), mm("-45.7")),
    (mm("6.75"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/106",
    (mm("6.85"), mm("-45.7")),
    (mm("6.85"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/107",
    (mm("7.05"), mm("-45.7")),
    (mm("7.05"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/108",
    (mm("7.05"), mm("-43.5")),
    (mm("4.45"), mm("-43.5")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/109",
    (mm("7.05"), mm("-43.3")),
    (mm("4.45"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/110",
    (mm("14.6"), mm("-45.7")),
    (mm("17.2"), mm("-45.7")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/111",
    (mm("14.6"), mm("-45.5")),
    (mm("17.2"), mm("-45.5")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/112",
    (mm("14.6"), mm("-43.3")),
    (mm("14.6"), mm("-45.7")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/113",
    (mm("14.8"), mm("-45.7")),
    (mm("14.8"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/114",
    (mm("14.9"), mm("-45.7")),
    (mm("14.9"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/115",
    (mm("16.9"), mm("-45.7")),
    (mm("16.9"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/116",
    (mm("17"), mm("-45.7")),
    (mm("17"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/117",
    (mm("17.2"), mm("-45.7")),
    (mm("17.2"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/118",
    (mm("17.2"), mm("-43.5")),
    (mm("14.6"), mm("-43.5")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/119",
    (mm("17.2"), mm("-43.3")),
    (mm("14.6"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/120",
    (mm("22.185"), mm("32.8")),
    (mm("14.685"), mm("32.8")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/121",
    (mm("22.3"), mm("28.5")),
    (mm("22.3"), mm("32.7")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/122",
    (mm("22.3"), mm("32.7")),
    (mm("22.3"), mm("28.5")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/123",
    (mm("24.775"), mm("27.6")),
    (mm("27.425"), mm("27.6")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/124",
    (mm("24.775"), mm("27.8")),
    (mm("27.425"), mm("27.8")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/125",
    (mm("24.775"), mm("30.1")),
    (mm("27.425"), mm("30.1")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/126",
    (mm("24.775"), mm("30.2")),
    (mm("27.425"), mm("30.2")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/127",
    (mm("24.775"), mm("30.3")),
    (mm("27.425"), mm("30.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/128",
    (mm("24.775"), mm("32.7")),
    (mm("27.425"), mm("32.7")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/129",
    (mm("24.775"), mm("34.295")),
    (mm("24.775"), mm("27.6")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/130",
    (mm("24.775"), mm("34.295")),
    (mm("27.425"), mm("34.295")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/131",
    (mm("24.975"), mm("34.295")),
    (mm("24.975"), mm("27.6")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/132",
    (mm("25.3"), mm("25.5")),
    (mm("44.7"), mm("25.5")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/133",
    (mm("27.275"), mm("34.295")),
    (mm("27.275"), mm("27.6")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/134",
    (mm("27.425"), mm("34.295")),
    (mm("27.425"), mm("27.6")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/135",
    (mm("28.7"), mm("-40.1")),
    (mm("28.7"), mm("-38.1")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/136",
    (mm("28.7"), mm("-39.1")),
    (mm("31.1"), mm("-39.1")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/137",
    (mm("32.4"), mm("-45.7")),
    (mm("35"), mm("-45.7")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/138",
    (mm("32.4"), mm("-45.5")),
    (mm("35"), mm("-45.5")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/139",
    (mm("32.4"), mm("-43.3")),
    (mm("32.4"), mm("-45.7")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/140",
    (mm("32.6"), mm("-45.7")),
    (mm("32.6"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/141",
    (mm("32.7"), mm("-45.7")),
    (mm("32.7"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/142",
    (mm("34.7"), mm("-45.7")),
    (mm("34.7"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/143",
    (mm("34.8"), mm("-45.7")),
    (mm("34.8"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/144",
    (mm("35"), mm("-45.7")),
    (mm("35"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/145",
    (mm("35"), mm("-43.5")),
    (mm("32.4"), mm("-43.5")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/146",
    (mm("35"), mm("-43.3")),
    (mm("32.4"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/147",
    (mm("38.8"), mm("-40.1")),
    (mm("38.8"), mm("-38.1")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/148",
    (mm("38.8"), mm("-39.1")),
    (mm("36.7"), mm("-39.1")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/149",
    (mm("42.6"), mm("-45.7")),
    (mm("45.2"), mm("-45.7")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/150",
    (mm("42.6"), mm("-45.5")),
    (mm("45.2"), mm("-45.5")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/151",
    (mm("42.6"), mm("-43.3")),
    (mm("42.6"), mm("-45.7")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/152",
    (mm("42.8"), mm("-45.7")),
    (mm("42.8"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/153",
    (mm("42.9"), mm("-45.7")),
    (mm("42.9"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/154",
    (mm("44.9"), mm("-45.7")),
    (mm("44.9"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/155",
    (mm("45"), mm("-45.7")),
    (mm("45"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/156",
    (mm("45.2"), mm("-45.7")),
    (mm("45.2"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/157",
    (mm("45.2"), mm("-43.5")),
    (mm("42.6"), mm("-43.5")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/158",
    (mm("45.2"), mm("-43.3")),
    (mm("42.6"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/159",
    (mm("47.7"), mm("28.5")),
    (mm("47.7"), mm("32.7")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/160",
    (mm("50.1"), mm("-1.8")),
    (mm("50.1"), mm("-1.6")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/161",
    (mm("50.1"), mm("-1.6")),
    (mm("50.1"), mm("21.6")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/162",
    (mm("50.1"), mm("21.6")),
    (mm("58"), mm("21.6")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/163",
    (mm("50.2"), mm("-45.7")),
    (mm("52.8"), mm("-45.7")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/164",
    (mm("50.2"), mm("-45.5")),
    (mm("52.8"), mm("-45.5")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/165",
    (mm("50.2"), mm("-43.3")),
    (mm("50.2"), mm("-45.7")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/166",
    (mm("50.4"), mm("-45.7")),
    (mm("50.4"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/167",
    (mm("50.5"), mm("-45.7")),
    (mm("50.5"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/168",
    (mm("52.5"), mm("-45.7")),
    (mm("52.5"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/169",
    (mm("52.6"), mm("-45.7")),
    (mm("52.6"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/170",
    (mm("52.8"), mm("-45.7")),
    (mm("52.8"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/171",
    (mm("52.8"), mm("-43.5")),
    (mm("50.2"), mm("-43.5")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/172",
    (mm("52.8"), mm("-43.3")),
    (mm("50.2"), mm("-43.3")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/173",
    (mm("53.2"), mm("32.8")),
    (mm("37.545"), mm("32.8")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/174",
    (mm("54.05"), mm("3.9")),
    (mm("54.45"), mm("3.5")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/175",
    (mm("54.35"), mm("3.7")),
    (mm("54.35"), mm("4")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/176",
    (mm("54.45"), mm("3.5")),
    (mm("54.45"), mm("4.2")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/177",
    (mm("54.45"), mm("4.2")),
    (mm("54.45"), mm("4.3")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/178",
    (mm("54.45"), mm("4.3")),
    (mm("54.05"), mm("3.9")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/179",
    (mm("56.65"), mm("3.9")),
    (mm("54.05"), mm("3.9")),
    layer="B.SilkS",
    width=mm("0.2"),
)
design.line(
    "B.SilkS/line/180",
    (mm("58"), mm("-1.8")),
    (mm("50.1"), mm("-1.8")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.line(
    "B.SilkS/line/181",
    (mm("58"), mm("21.6")),
    (mm("58"), mm("-1.8")),
    layer="B.SilkS",
    width=mm("0.15"),
)
design.rect(
    "B.SilkS/rect/1",
    (mm("-37.795"), mm("-34.2")),
    (mm("-36.495"), mm("-31.8")),
    layer="B.SilkS",
    width=mm("0.15"),
    fill=True,
)
design.rect(
    "B.SilkS/rect/2",
    (mm("-37.795"), mm("-34.075")),
    (mm("-36.495"), mm("-31.675")),
    layer="B.SilkS",
    width=mm("0.15"),
    fill=True,
)
design.rect(
    "B.SilkS/rect/3",
    (mm("-37.795"), mm("-11.375")),
    (mm("-36.495"), mm("-8.975")),
    layer="B.SilkS",
    width=mm("0.15"),
    fill=True,
)
design.rect(
    "B.SilkS/rect/4",
    (mm("-37.795"), mm("-11.3")),
    (mm("-36.495"), mm("-8.9")),
    layer="B.SilkS",
    width=mm("0.15"),
    fill=True,
)
design.rect(
    "B.SilkS/rect/5",
    (mm("-37.795"), mm("11.625")),
    (mm("-36.495"), mm("14.025")),
    layer="B.SilkS",
    width=mm("0.15"),
    fill=True,
)
design.rect(
    "B.SilkS/rect/6",
    (mm("-20.9"), mm("32.7")),
    (mm("-18.5"), mm("34.2")),
    layer="B.SilkS",
    width=mm("0.15"),
    fill=True,
)
design.rect(
    "B.SilkS/rect/7",
    (mm("2"), mm("32.7")),
    (mm("4.4"), mm("34.2")),
    layer="B.SilkS",
    width=mm("0.15"),
    fill=True,
)
design.rect(
    "B.SilkS/rect/8",
    (mm("24.875"), mm("32.7")),
    (mm("27.275"), mm("34.2")),
    layer="B.SilkS",
    width=mm("0.15"),
    fill=True,
)
design.arc(
    "F.SilkS/arc/1",
    (mm("-13.65"), mm("-26.51")),
    (mm("-12.235786"), mm("-25.924214")),
    (mm("-11.65"), mm("-24.51")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.arc(
    "F.SilkS/arc/2",
    (mm("-11.65"), mm("-8.01")),
    (mm("-12.235786"), mm("-6.595786")),
    (mm("-13.65"), mm("-6.01")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.arc(
    "F.SilkS/arc/3",
    (mm("1.399999"), mm("18.000001")),
    (mm("2.107106"), mm("18.292894")),
    (mm("2.399999"), mm("19.000001")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.arc(
    "F.SilkS/arc/4",
    (mm("2.4"), mm("25.7")),
    (mm("2.107107"), mm("26.407107")),
    (mm("1.4"), mm("26.7")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.arc(
    "F.SilkS/arc/5",
    (mm("23.799999"), mm("18.000001")),
    (mm("24.507106"), mm("18.292894")),
    (mm("24.799999"), mm("19.000001")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.arc(
    "F.SilkS/arc/6",
    (mm("24.8"), mm("25.7")),
    (mm("24.507107"), mm("26.407107")),
    (mm("23.8"), mm("26.7")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.arc(
    "F.SilkS/arc/7",
    (mm("45.307107"), mm("-37.292893")),
    (mm("45.6"), mm("-38")),
    (mm("46.307107"), mm("-38.292893")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.arc(
    "F.SilkS/arc/8",
    (mm("47.8"), mm("-27.5")),
    (mm("46.3"), mm("-29")),
    (mm("47.8"), mm("-30.5")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.arc(
    "F.SilkS/arc/9",
    (mm("57.65"), mm("-38.3")),
    (mm("58.357107"), mm("-38.007107")),
    (mm("58.65"), mm("-37.3")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.circle(
    "F.SilkS/circle/1",
    (mm("46.05"), mm("-32.3")),
    (mm("46.8"), mm("-32.3")),
    layer="F.SilkS",
    width=mm("0.15"),
    fill=True,
)
design.circle(
    "F.SilkS/circle/2",
    (mm("57.9"), mm("-32.3")),
    (mm("58.65"), mm("-32.3")),
    layer="F.SilkS",
    width=mm("0.15"),
    fill=True,
)
design.line(
    "F.SilkS/line/1",
    (mm("-33.65"), mm("32.955")),
    (mm("-33.65"), mm("34.4")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/2",
    (mm("-33.55"), mm("32.955")),
    (mm("-33.55"), mm("34.4")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/3",
    (mm("-23.55"), mm("32.955")),
    (mm("-23.55"), mm("34.4")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/4",
    (mm("-23.485"), mm("32.955")),
    (mm("-33.65"), mm("32.955")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/5",
    (mm("-23.4"), mm("32.955")),
    (mm("-23.4"), mm("34.4")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/6",
    (mm("-23"), mm("-28.6")),
    (mm("-20"), mm("-28.6")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/7",
    (mm("-20.5"), mm("-29.1")),
    (mm("-20.5"), mm("-28.2")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/8",
    (mm("-20.5"), mm("-28.2")),
    (mm("-20.5"), mm("-28.1")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/9",
    (mm("-20.5"), mm("-28.1")),
    (mm("-20"), mm("-28.6")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/10",
    (mm("-20"), mm("-28.6")),
    (mm("-20.5"), mm("-29.1")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/11",
    (mm("-16.65"), mm("-6.01")),
    (mm("-13.65"), mm("-6.01")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/12",
    (mm("-13.65"), mm("-26.51")),
    (mm("-16.65"), mm("-26.51")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/13",
    (mm("-11.65"), mm("-24.51")),
    (mm("-11.65"), mm("-8.01")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/14",
    (mm("-8.2"), mm("-45.7")),
    (mm("-8.2"), mm("-43.3")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/15",
    (mm("-8.2"), mm("-43.5")),
    (mm("-5.6"), mm("-43.5")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/16",
    (mm("-8.2"), mm("-43.3")),
    (mm("-5.6"), mm("-43.3")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/17",
    (mm("-8.2"), mm("32.955")),
    (mm("-8.2"), mm("34.4")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/18",
    (mm("-8"), mm("-43.3")),
    (mm("-8"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/19",
    (mm("-7.9"), mm("-43.3")),
    (mm("-7.9"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/20",
    (mm("-7.6"), mm("18")),
    (mm("-7.6"), mm("23.4")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/21",
    (mm("-5.9"), mm("-43.3")),
    (mm("-5.9"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/22",
    (mm("-5.8"), mm("-43.3")),
    (mm("-5.8"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/23",
    (mm("-5.6"), mm("-45.7")),
    (mm("-8.2"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/24",
    (mm("-5.6"), mm("-45.5")),
    (mm("-8.2"), mm("-45.5")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/25",
    (mm("-5.6"), mm("-43.3")),
    (mm("-5.6"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/26",
    (mm("-5.6"), mm("18")),
    (mm("-5.6"), mm("23.4")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/27",
    (mm("-3.15"), mm("-45.7")),
    (mm("-3.15"), mm("-43.3")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/28",
    (mm("-3.15"), mm("-43.5")),
    (mm("-0.55"), mm("-43.5")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/29",
    (mm("-3.15"), mm("-43.3")),
    (mm("-0.55"), mm("-43.3")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/30",
    (mm("-2.95"), mm("-43.3")),
    (mm("-2.95"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/31",
    (mm("-2.85"), mm("-43.3")),
    (mm("-2.85"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/32",
    (mm("-0.85"), mm("-43.3")),
    (mm("-0.85"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/33",
    (mm("-0.75"), mm("-43.3")),
    (mm("-0.75"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/34",
    (mm("-0.55"), mm("-45.7")),
    (mm("-3.15"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/35",
    (mm("-0.55"), mm("-45.5")),
    (mm("-3.15"), mm("-45.5")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/36",
    (mm("-0.55"), mm("-43.3")),
    (mm("-0.55"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/37",
    (mm("1.399999"), mm("18.000001")),
    (mm("-5.6"), mm("18")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/38",
    (mm("2.4"), mm("19.000001")),
    (mm("2.4"), mm("25.7")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/39",
    (mm("4.45"), mm("-45.7")),
    (mm("4.45"), mm("-43.3")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/40",
    (mm("4.45"), mm("-43.5")),
    (mm("7.05"), mm("-43.5")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/41",
    (mm("4.45"), mm("-43.3")),
    (mm("7.05"), mm("-43.3")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/42",
    (mm("4.6"), mm("33.005")),
    (mm("4.6"), mm("34.45")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/43",
    (mm("4.65"), mm("-43.3")),
    (mm("4.65"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/44",
    (mm("4.75"), mm("-43.3")),
    (mm("4.75"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/45",
    (mm("6.75"), mm("-43.3")),
    (mm("6.75"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/46",
    (mm("6.85"), mm("-43.3")),
    (mm("6.85"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/47",
    (mm("7.05"), mm("-45.7")),
    (mm("4.45"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/48",
    (mm("7.05"), mm("-45.5")),
    (mm("4.45"), mm("-45.5")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/49",
    (mm("7.05"), mm("-43.3")),
    (mm("7.05"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/50",
    (mm("14.6"), mm("-45.7")),
    (mm("14.6"), mm("-43.3")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/51",
    (mm("14.6"), mm("-43.5")),
    (mm("17.2"), mm("-43.5")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/52",
    (mm("14.6"), mm("-43.3")),
    (mm("17.2"), mm("-43.3")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/53",
    (mm("14.735"), mm("32.955")),
    (mm("22.235"), mm("32.955")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/54",
    (mm("14.8"), mm("-43.3")),
    (mm("14.8"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/55",
    (mm("14.9"), mm("-43.3")),
    (mm("14.9"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/56",
    (mm("16.75"), mm("18")),
    (mm("16.75"), mm("23.4")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/57",
    (mm("16.9"), mm("-43.3")),
    (mm("16.9"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/58",
    (mm("17"), mm("-43.3")),
    (mm("17"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/59",
    (mm("17.2"), mm("-45.7")),
    (mm("14.6"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/60",
    (mm("17.2"), mm("-45.5")),
    (mm("14.6"), mm("-45.5")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/61",
    (mm("17.2"), mm("-43.3")),
    (mm("17.2"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/62",
    (mm("23.799999"), mm("18.000001")),
    (mm("16.8"), mm("18")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/63",
    (mm("23.8"), mm("26.7")),
    (mm("16.800001"), mm("26.700001")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/64",
    (mm("24.8"), mm("19.000001")),
    (mm("24.8"), mm("25.7")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/65",
    (mm("32.4"), mm("-45.7")),
    (mm("32.4"), mm("-43.3")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/66",
    (mm("32.4"), mm("-43.5")),
    (mm("35"), mm("-43.5")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/67",
    (mm("32.4"), mm("-43.3")),
    (mm("35"), mm("-43.3")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/68",
    (mm("32.6"), mm("-43.3")),
    (mm("32.6"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/69",
    (mm("32.7"), mm("-43.3")),
    (mm("32.7"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/70",
    (mm("34.7"), mm("-43.3")),
    (mm("34.7"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/71",
    (mm("34.8"), mm("-43.3")),
    (mm("34.8"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/72",
    (mm("35"), mm("-45.7")),
    (mm("32.4"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/73",
    (mm("35"), mm("-45.5")),
    (mm("32.4"), mm("-45.5")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/74",
    (mm("35"), mm("-43.3")),
    (mm("35"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/75",
    (mm("37.595"), mm("32.955")),
    (mm("53.25"), mm("32.955")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/76",
    (mm("42.6"), mm("-45.7")),
    (mm("42.6"), mm("-43.3")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/77",
    (mm("42.6"), mm("-43.5")),
    (mm("45.2"), mm("-43.5")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/78",
    (mm("42.6"), mm("-43.3")),
    (mm("45.2"), mm("-43.3")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/79",
    (mm("42.8"), mm("-43.3")),
    (mm("42.8"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/80",
    (mm("42.9"), mm("-43.3")),
    (mm("42.9"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/81",
    (mm("44.9"), mm("-43.3")),
    (mm("44.9"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/82",
    (mm("45"), mm("-43.3")),
    (mm("45"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/83",
    (mm("45.2"), mm("-45.7")),
    (mm("42.6"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/84",
    (mm("45.2"), mm("-45.5")),
    (mm("42.6"), mm("-45.5")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/85",
    (mm("45.2"), mm("-43.3")),
    (mm("45.2"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/86",
    (mm("45.307107"), mm("-37.392893")),
    (mm("45.307107"), mm("-33")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/87",
    (mm("47.8"), mm("-30.5")),
    (mm("58.3"), mm("-30.5")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/88",
    (mm("47.8"), mm("-27.5")),
    (mm("58.3"), mm("-27.5")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/89",
    (mm("49.55"), mm("-38.3")),
    (mm("46.3"), mm("-38.3")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/90",
    (mm("49.55"), mm("-38.3")),
    (mm("54.55"), mm("-38.3")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/91",
    (mm("49.55"), mm("-34.9")),
    (mm("49.55"), mm("-38.3")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/92",
    (mm("50.2"), mm("-45.7")),
    (mm("50.2"), mm("-43.3")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/93",
    (mm("50.2"), mm("-43.5")),
    (mm("52.8"), mm("-43.5")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/94",
    (mm("50.2"), mm("-43.3")),
    (mm("52.8"), mm("-43.3")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/95",
    (mm("50.4"), mm("-43.3")),
    (mm("50.4"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/96",
    (mm("50.5"), mm("-43.3")),
    (mm("50.5"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/97",
    (mm("52.5"), mm("-43.3")),
    (mm("52.5"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/98",
    (mm("52.6"), mm("-43.3")),
    (mm("52.6"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/99",
    (mm("52.8"), mm("-45.7")),
    (mm("50.2"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/100",
    (mm("52.8"), mm("-45.5")),
    (mm("50.2"), mm("-45.5")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/101",
    (mm("52.8"), mm("-43.3")),
    (mm("52.8"), mm("-45.7")),
    layer="F.SilkS",
    width=mm("0.2"),
)
design.line(
    "F.SilkS/line/102",
    (mm("54.5"), mm("-38.3")),
    (mm("57.65"), mm("-38.3")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/103",
    (mm("54.55"), mm("-38.3")),
    (mm("54.55"), mm("-33")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/104",
    (mm("58.4"), mm("-27.5")),
    (mm("58.4"), mm("-30.5")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.line(
    "F.SilkS/line/105",
    (mm("58.65"), mm("-37.3")),
    (mm("58.65"), mm("-32.9")),
    layer="F.SilkS",
    width=mm("0.15"),
)
design.polygon(
    "F.SilkS/polygon/1",
    (
        (mm("-20.5"), mm("-29.1")),
        (mm("-20.5"), mm("-28.2")),
        (mm("-20.4"), mm("-28.2")),
        (mm("-20"), mm("-28.6")),
    ),
    layer="F.SilkS",
    width=mm("0.15"),
    fill=True,
)
design.polygon(
    "F.SilkS/polygon/2",
    ((mm("-7.6"), mm("18.2")), (mm("-7.6"), mm("18")), (mm("-5.7"), mm("18")), (mm("-5.7"), mm("18.2"))),
    layer="F.SilkS",
    width=mm("0.15"),
    fill=True,
)
design.polygon(
    "F.SilkS/polygon/3",
    ((mm("-7.6"), mm("25.2")), (mm("-7.6"), mm("23.6")), (mm("-6.4"), mm("23.6")), (mm("-6.4"), mm("25.2"))),
    layer="F.SilkS",
    width=mm("0.15"),
    fill=True,
)
design.polygon(
    "F.SilkS/polygon/4",
    ((mm("-7.6"), mm("26.7")), (mm("-7.6"), mm("25.3")), (mm("-5.6"), mm("25.3")), (mm("-5.6"), mm("26.7"))),
    layer="F.SilkS",
    width=mm("0.15"),
    fill=True,
)
design.polygon(
    "F.SilkS/polygon/5",
    ((mm("14.85"), mm("18.2")), (mm("14.85"), mm("18")), (mm("16.7"), mm("18")), (mm("16.7"), mm("18.2"))),
    layer="F.SilkS",
    width=mm("0.15"),
    fill=True,
)
design.polygon(
    "F.SilkS/polygon/6",
    (
        (mm("14.85"), mm("23.5")),
        (mm("14.85"), mm("23.3")),
        (mm("16.75"), mm("23.3")),
        (mm("16.75"), mm("23.5")),
    ),
    layer="F.SilkS",
    width=mm("0.15"),
    fill=True,
)
design.polygon(
    "F.SilkS/polygon/7",
    ((mm("14.85"), mm("25.2")), (mm("14.85"), mm("23.6")), (mm("16"), mm("23.6")), (mm("16"), mm("25.2"))),
    layer="F.SilkS",
    width=mm("0.15"),
    fill=True,
)
design.polygon(
    "F.SilkS/polygon/8",
    (
        (mm("14.85"), mm("26.7")),
        (mm("14.85"), mm("25.3")),
        (mm("16.8"), mm("25.3")),
        (mm("16.8"), mm("26.7")),
    ),
    layer="F.SilkS",
    width=mm("0.15"),
    fill=True,
)
design.polygon(
    "F.SilkS/polygon/9",
    (
        (mm("47.05"), mm("-33.05")),
        (mm("47.05"), mm("-32.2")),
        (mm("45.25"), mm("-32.2")),
        (mm("45.25"), mm("-33.05")),
    ),
    layer="F.SilkS",
    width=mm("0.05"),
    fill=True,
)
design.polygon(
    "F.SilkS/polygon/10",
    (
        (mm("47.05"), mm("-31.5")),
        (mm("46.2"), mm("-31.5")),
        (mm("46.2"), mm("-32.8")),
        (mm("47.05"), mm("-32.8")),
    ),
    layer="F.SilkS",
    width=mm("0.05"),
    fill=True,
)
design.polygon(
    "F.SilkS/polygon/11",
    (
        (mm("49.95"), mm("-32.9")),
        (mm("49.5"), mm("-32.9")),
        (mm("49.5"), mm("-34.9")),
        (mm("49.95"), mm("-34.9")),
    ),
    layer="F.SilkS",
    width=mm("0.05"),
    fill=True,
)
design.polygon(
    "F.SilkS/polygon/12",
    (
        (mm("55"), mm("-32.9")),
        (mm("54.05"), mm("-32.9")),
        (mm("54.05"), mm("-34.9")),
        (mm("55"), mm("-34.9")),
    ),
    layer="F.SilkS",
    width=mm("0.05"),
    fill=True,
)
design.polygon(
    "F.SilkS/polygon/13",
    (
        (mm("57.85"), mm("-31.5")),
        (mm("57"), mm("-31.5")),
        (mm("57"), mm("-32.8")),
        (mm("57.85"), mm("-32.8")),
    ),
    layer="F.SilkS",
    width=mm("0.05"),
    fill=True,
)
design.polygon(
    "F.SilkS/polygon/14",
    (
        (mm("58.7"), mm("-33.05")),
        (mm("58.7"), mm("-32.2")),
        (mm("57.05"), mm("-32.2")),
        (mm("57.05"), mm("-33.05")),
    ),
    layer="F.SilkS",
    width=mm("0.05"),
    fill=True,
)
design.polygon(
    "F.SilkS/polygon/15",
    (
        (mm("58.7"), mm("-32.9")),
        (mm("58.2"), mm("-32.9")),
        (mm("58.2"), mm("-34.9")),
        (mm("58.7"), mm("-34.9")),
    ),
    layer="F.SilkS",
    width=mm("0.05"),
    fill=True,
)
design.text(
    "B.SilkS/text/1",
    "ot6",
    (mm("-43.4"), mm("-31.5")),
    layer="B.SilkS",
    size=(mm("1"), mm("0.7")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
)
design.text(
    "B.SilkS/text/2",
    "in3",
    (mm("-43.4"), mm("-29.1")),
    layer="B.SilkS",
    size=(mm("1"), mm("0.7")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/3",
    "ot4",
    (mm("-43.4"), mm("-26.5")),
    layer="B.SilkS",
    size=(mm("1"), mm("0.7")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
)
design.text(
    "B.SilkS/text/4",
    "in5",
    (mm("-43.4"), mm("-24")),
    layer="B.SilkS",
    size=(mm("1"), mm("0.7")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/5",
    "in5",
    (mm("-43.4"), mm("-8.8")),
    layer="B.SilkS",
    size=(mm("1"), mm("0.7")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
)
design.text(
    "B.SilkS/text/6",
    "ot7",
    (mm("-43.4"), mm("-6.4")),
    layer="B.SilkS",
    size=(mm("1"), mm("0.7")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/7",
    "in6",
    (mm("-43.4"), mm("-3.8")),
    layer="B.SilkS",
    size=(mm("1"), mm("0.7")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
)
design.text(
    "B.SilkS/text/8",
    "in4",
    (mm("-43.4"), mm("-1.3")),
    layer="B.SilkS",
    size=(mm("1"), mm("0.7")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/9",
    "bi1",
    (mm("-43.4"), mm("14.2")),
    layer="B.SilkS",
    size=(mm("1"), mm("0.7")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
)
design.text(
    "B.SilkS/text/10",
    "bi2",
    (mm("-43.4"), mm("16.6")),
    layer="B.SilkS",
    size=(mm("1"), mm("0.7")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/11",
    "ot7",
    (mm("-43.4"), mm("19.2")),
    layer="B.SilkS",
    size=(mm("1"), mm("0.7")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
)
design.text(
    "B.SilkS/text/12",
    "ot4",
    (mm("-43.4"), mm("21.7")),
    layer="B.SilkS",
    size=(mm("1"), mm("0.7")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/13",
    "3v3",
    (mm("-37.8"), mm("-36.8")),
    layer="B.SilkS",
    size=(mm("0.9"), mm("1")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
)
design.text(
    "B.SilkS/text/14",
    "bi3",
    (mm("-37.8"), mm("-29.1")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/15",
    "bi6",
    (mm("-37.8"), mm("-26.6")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
)
design.text(
    "B.SilkS/text/16",
    "bi4",
    (mm("-37.8"), mm("-24.1")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/17",
    "3v3",
    (mm("-37.8"), mm("-14.1")),
    layer="B.SilkS",
    size=(mm("0.9"), mm("1")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
)
design.text(
    "B.SilkS/text/18",
    "ot3",
    (mm("-37.8"), mm("-6.4")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/19",
    "in2",
    (mm("-37.8"), mm("-3.9")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
)
design.text(
    "B.SilkS/text/20",
    "in0",
    (mm("-37.8"), mm("-1.4")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/21",
    "3v3",
    (mm("-37.8"), mm("8.9")),
    layer="B.SilkS",
    size=(mm("0.9"), mm("1")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
)
design.text(
    "B.SilkS/text/22",
    "in2",
    (mm("-37.8"), mm("16.6")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/23",
    "ot3",
    (mm("-37.8"), mm("19.1")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
)
design.text(
    "B.SilkS/text/24",
    "ot4",
    (mm("-37.8"), mm("21.6")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/25",
    "bi5",
    (mm("-37.795"), mm("-31.575")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
)
design.text(
    "B.SilkS/text/26",
    "in1",
    (mm("-37.795"), mm("-8.875")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
)
design.text(
    "B.SilkS/text/27",
    "ot5",
    (mm("-37.795"), mm("14.125")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    rot=270,
    justify="right bottom",
)
design.text(
    "B.SilkS/text/28",
    "SPI SLAVE",
    (mm("-36.3"), mm("-2.8")),
    layer="B.SilkS",
    size=(mm("1.1"), mm("2")),
    thickness=mm("0.275"),
    rot=-90,
    justify="left bottom",
    knockout=True,
    bold=True,
)
design.text(
    "B.SilkS/text/29",
    "SPI MASTER",
    (mm("-36.3"), mm("21.5")),
    layer="B.SilkS",
    size=(mm("1.1"), mm("2")),
    thickness=mm("0.275"),
    rot=-90,
    justify="left bottom",
    knockout=True,
    bold=True,
)
design.text(
    "B.SilkS/text/30",
    "SPI BI/UART",
    (mm("-35.8"), mm("-23.6")),
    layer="B.SilkS",
    size=(mm("1.1"), mm("2")),
    thickness=mm("0.275"),
    rot=-90,
    justify="left bottom",
    knockout=True,
    bold=True,
)
design.text(
    "B.SilkS/text/31",
    "in3",
    (mm("-33.6"), mm("34.195")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
)
design.text(
    "B.SilkS/text/32",
    "Standard PMODs",
    (mm("-31.7"), mm("-36.4")),
    layer="B.SilkS",
    size=(mm("2.5"), mm("2.2")),
    thickness=mm("0.5"),
    rot=270,
    justify="right bottom",
    knockout=True,
    bold=True,
)
design.text(
    "B.SilkS/text/33",
    "SD1",
    (mm("-31.5"), mm("4")),
    layer="B.SilkS",
    size=mm("1.3"),
    thickness=mm("0.2"),
    rot=90,
    justify="right bottom",
)
design.text(
    "B.SilkS/text/34",
    "in2",
    (mm("-31.05"), mm("34.195")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/35",
    "GND",
    (mm("-31"), mm("6.71")),
    layer="B.SilkS",
    size=mm("1.3"),
    thickness=mm("0.2"),
    rot=90,
    justify="left bottom",
)
design.text(
    "B.SilkS/text/36",
    "in1",
    (mm("-28.5"), mm("34.195")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
)
design.text(
    "B.SilkS/text/37",
    "SCK",
    (mm("-26.5"), mm("4")),
    layer="B.SilkS",
    size=mm("1.3"),
    thickness=mm("0.2"),
    rot=90,
    justify="right bottom",
)
design.text(
    "B.SilkS/text/38",
    "INPUT",
    (mm("-26.3"), mm("28.9")),
    layer="B.SilkS",
    size=(mm("1.1"), mm("2")),
    thickness=mm("0.275"),
    justify="left bottom",
    knockout=True,
    bold=True,
)
design.text(
    "B.SilkS/text/39",
    "in0",
    (mm("-26.2"), mm("34.195")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/40",
    "SD0",
    (mm("-26"), mm("7")),
    layer="B.SilkS",
    size=mm("1.3"),
    thickness=mm("0.2"),
    rot=90,
    justify="left bottom",
)
design.text(
    "B.SilkS/text/41",
    "3v3",
    (mm("-23.45"), mm("34.195")),
    layer="B.SilkS",
    size=(mm("0.85"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
)
design.text(
    "B.SilkS/text/42",
    "3v3",
    (mm("-21.5"), mm("4")),
    layer="B.SilkS",
    size=mm("1.3"),
    thickness=mm("0.2"),
    rot=90,
    justify="right bottom",
)
design.text(
    "B.SilkS/text/43",
    "CS",
    (mm("-21"), mm("7")),
    layer="B.SilkS",
    size=mm("1.3"),
    thickness=mm("0.2"),
    rot=90,
    justify="left bottom",
)
design.text(
    "B.SilkS/text/44",
    "in3",
    (mm("-18.65"), mm("27.7")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/45",
    "in7",
    (mm("-18.3"), mm("34.195")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/46",
    "in2",
    (mm("-16.1"), mm("27.7")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
)
design.text(
    "B.SilkS/text/47",
    "in6",
    (mm("-15.85"), mm("34.195")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="right bottom",
)
design.text(
    "B.SilkS/text/48",
    "RP2040 FLASH",
    (mm("-15.6"), mm("13.2")),
    layer="B.SilkS",
    size=mm("1.5"),
    thickness=mm("0.2"),
    justify="left bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/49",
    "in1",
    (mm("-13.55"), mm("27.7")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/50",
    "in5",
    (mm("-13.3"), mm("34.195")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/51",
    "in0",
    (mm("-10.9"), mm("27.9")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="right bottom",
)
design.text(
    "B.SilkS/text/52",
    "in4",
    (mm("-10.8"), mm("34.195")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="right bottom",
)
design.text(
    "B.SilkS/text/53",
    "CLK",
    (mm("-8.15"), mm("34.195")),
    layer="B.SilkS",
    size=(mm("0.9"), mm("1.1")),
    thickness=mm("0.15"),
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/54",
    "GND",
    (mm("-7.9"), mm("-43")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/55",
    "ALPHA",
    (mm("-6.6"), mm("-14.8")),
    layer="B.SilkS",
    size=(mm("3"), mm("4")),
    thickness=mm("0.5"),
    rot=90,
    justify="bottom",
    knockout=True,
    bold=True,
    face="FreeMono",
)
design.text(
    "B.SilkS/text/56",
    "IN PWR",
    (mm("-5.8"), mm("-38.3")),
    layer="B.SilkS",
    size=(mm("0.9"), mm("1.2")),
    thickness=mm("0.2"),
    justify="bottom",
    bold=True,
)
design.text(
    "B.SilkS/text/57",
    "~{RST}",
    (mm("-5.55"), mm("34.195")),
    layer="B.SilkS",
    size=(mm("0.9"), mm("1.1")),
    thickness=mm("0.15"),
    justify="right bottom",
)
design.text(
    "B.SilkS/text/58",
    "+5V",
    (mm("-5.250786"), mm("-43")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/59",
    "v0.9",
    (mm("-4.3"), mm("-17")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    rot=90,
    justify="bottom",
)
design.text(
    "B.SilkS/text/60",
    "CTRL",
    (mm("-3.656423"), mm("25.9")),
    layer="B.SilkS",
    size=(mm("1.1"), mm("3")),
    thickness=mm("0.275"),
    rot=90,
    justify="left bottom",
    knockout=True,
    bold=True,
)
design.text(
    "B.SilkS/text/61",
    "bi3",
    (mm("-3.05"), mm("34.195")),
    layer="B.SilkS",
    size=(mm("1"), mm("1.1")),
    thickness=mm("0.15"),
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/62",
    "GND",
    (mm("-2.710786"), mm("-43")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/63",
    "3v3",
    (mm("-0.6"), mm("34.195")),
    layer="B.SilkS",
    size=(mm("0.85"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
)
design.text(
    "B.SilkS/text/64",
    "3v3",
    (mm("-0.200786"), mm("-43")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/65",
    "P29",
    (mm("2.399214"), mm("-43")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/66",
    "bi7",
    (mm("4.5"), mm("34.245")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/67",
    "bi3",
    (mm("4.6"), mm("27.595")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/68",
    "GND",
    (mm("4.909214"), mm("-43.1")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/69",
    "(C) 2023 Pat Deegan\nhttps://psychogenic.com",
    (mm("6.6"), mm("-0.4")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="bottom",
)
design.text(
    "B.SilkS/text/70",
    "TinyTapeout 4+\nDemo Board",
    (mm("6.7"), mm("-15.5")),
    layer="B.SilkS",
    size=mm("2.3"),
    thickness=mm("0.5"),
    justify="bottom",
    bold=True,
)
design.text(
    "B.SilkS/text/71",
    "bi6",
    (mm("7"), mm("34.245")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="right bottom",
)
design.text(
    "B.SilkS/text/72",
    "bi2",
    (mm("7.1"), mm("27.595")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
)
design.text(
    "B.SilkS/text/73",
    "m33",
    (mm("7.449214"), mm("-43.1")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/74",
    "bi5",
    (mm("9.5"), mm("34.245")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/75",
    "bi1",
    (mm("9.6"), mm("27.595")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/76",
    "cEN",
    (mm("9.999214"), mm("-43.1")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/77",
    "bi4",
    (mm("12.05"), mm("34.245")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="right bottom",
)
design.text(
    "B.SilkS/text/78",
    "bi0",
    (mm("12.15"), mm("27.595")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
)
design.text(
    "B.SilkS/text/79",
    "m35",
    (mm("12.529214"), mm("-43.1")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/80",
    "bi2",
    (mm("14.65"), mm("34.195")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/81",
    "GND",
    (mm("15.049214"), mm("-43")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/82",
    "bi1",
    (mm("17.1"), mm("34.195")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
)
design.text(
    "B.SilkS/text/83",
    "cINC",
    (mm("17.599214"), mm("-43.1")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/84",
    "bi0",
    (mm("19.6"), mm("34.195")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/85",
    "m37",
    (mm("20.149214"), mm("-42.95")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/86",
    "BIDIR",
    (mm("20.7"), mm("28.9")),
    layer="B.SilkS",
    size=(mm("1.1"), mm("2")),
    thickness=mm("0.275"),
    justify="left bottom",
    knockout=True,
    bold=True,
)
design.text(
    "B.SilkS/text/87",
    "3v3",
    (mm("22.25"), mm("34.195")),
    layer="B.SilkS",
    size=(mm("0.85"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
)
design.text(
    "B.SilkS/text/88",
    "cRST",
    (mm("22.689214"), mm("-43")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/89",
    "m00",
    (mm("25.249214"), mm("-43")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/90",
    "ot3",
    (mm("27.4"), mm("27.595")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/91",
    "ot7",
    (mm("27.5"), mm("34.245")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="right bottom",
)
design.text(
    "B.SilkS/text/92",
    "SDO",
    (mm("27.749214"), mm("-43")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/93",
    "ot6",
    (mm("29.85"), mm("34.245")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/94",
    "ot2",
    (mm("29.95"), mm("27.595")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
)
design.text(
    "B.SilkS/text/95",
    "SDI",
    (mm("30.299214"), mm("-43")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/96",
    "ot5",
    (mm("32.35"), mm("34.245")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="right bottom",
)
design.text(
    "B.SilkS/text/97",
    "ot1",
    (mm("32.5"), mm("27.595")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/98",
    "GND",
    (mm("32.849214"), mm("-43")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/99",
    "HK SPI",
    (mm("33.8"), mm("-38.3")),
    layer="B.SilkS",
    size=(mm("1"), mm("1.2")),
    thickness=mm("0.2"),
    justify="bottom",
    bold=True,
)
design.text(
    "B.SilkS/text/100",
    "ot4",
    (mm("34.9"), mm("34.245")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/101",
    "ot0",
    (mm("35.1"), mm("27.595")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
)
design.text(
    "B.SilkS/text/102",
    "CSB",
    (mm("35.389214"), mm("-43")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/103",
    "zerotoasic\ncourse.com",
    (mm("37"), mm("2.52")),
    layer="B.SilkS",
    size=(mm("1"), mm("1.1")),
    thickness=mm("0.2"),
)
design.text(
    "B.SilkS/text/104",
    "tinytapeout.com",
    (mm("37.1"), mm("-29.38")),
    layer="B.SilkS",
    size=(mm("1"), mm("1.2")),
    thickness=mm("0.17"),
)
design.text(
    "B.SilkS/text/105",
    "ot3",
    (mm("37.55"), mm("34.195")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
)
design.text(
    "B.SilkS/text/106",
    "SCK",
    (mm("37.929214"), mm("-43")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/107",
    "ot2",
    (mm("40.1"), mm("34.195")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/108",
    "UCK",
    (mm("40.469214"), mm("-43")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/109",
    "ot1",
    (mm("42.55"), mm("34.195")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
)
design.text(
    "B.SilkS/text/110",
    "GND",
    (mm("43.009214"), mm("-43")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/111",
    "ot0",
    (mm("45.15"), mm("34.195")),
    layer="B.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/112",
    "3v3",
    (mm("45.549214"), mm("-43")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/113",
    "OUTPUT",
    (mm("45.9"), mm("28.9")),
    layer="B.SilkS",
    size=(mm("1.1"), mm("2")),
    thickness=mm("0.275"),
    justify="left bottom",
    knockout=True,
    bold=True,
)
design.text(
    "B.SilkS/text/114",
    "5V ",
    (mm("46.9"), mm("34.195")),
    layer="B.SilkS",
    size=(mm("1.25"), mm("1")),
    thickness=mm("0.15"),
    justify="right bottom",
)
design.text(
    "B.SilkS/text/115",
    "Project I/O PMODs",
    (mm("47.1"), mm("24.2")),
    layer="B.SilkS",
    size=(mm("2.5"), mm("2.2")),
    thickness=mm("0.5"),
    justify="left bottom",
    knockout=True,
    bold=True,
)
design.text(
    "B.SilkS/text/116",
    "1v8",
    (mm("48.089214"), mm("-43")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/117",
    "GND",
    (mm("50.1"), mm("34.195")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/118",
    "GND",
    (mm("50.629214"), mm("-43")),
    layer="B.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=-90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "B.SilkS/text/119",
    "A",
    (mm("51.8"), mm("3.1")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "B.SilkS/text/120",
    "7",
    (mm("51.8"), mm("20.7")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "B.SilkS/text/121",
    "PWR",
    (mm("52.1"), mm("26.1")),
    layer="B.SilkS",
    size=(mm("1.1"), mm("3")),
    thickness=mm("0.275"),
    rot=90,
    justify="left bottom",
    knockout=True,
    bold=True,
)
design.text(
    "B.SilkS/text/122",
    "B",
    (mm("52.35"), mm("5.7")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "B.SilkS/text/123",
    "C",
    (mm("52.35"), mm("8.1")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "B.SilkS/text/124",
    "D",
    (mm("52.35"), mm("10.7")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "B.SilkS/text/125",
    "E",
    (mm("52.35"), mm("13.3")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "B.SilkS/text/126",
    "F",
    (mm("52.35"), mm("15.7")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "B.SilkS/text/127",
    "G",
    (mm("52.35"), mm("18.1")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "B.SilkS/text/128",
    "7-seg\nremap",
    (mm("56.9"), mm("1.4")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "B.SilkS/text/129",
    "0",
    (mm("57.9"), mm("3.1")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "B.SilkS/text/130",
    "1",
    (mm("57.9"), mm("5.7")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "B.SilkS/text/131",
    "2",
    (mm("57.9"), mm("8.1")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "B.SilkS/text/132",
    "3",
    (mm("57.9"), mm("10.7")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "B.SilkS/text/133",
    "4",
    (mm("57.9"), mm("13.3")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "B.SilkS/text/134",
    "5",
    (mm("57.9"), mm("15.7")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "B.SilkS/text/135",
    "6",
    (mm("57.9"), mm("18.1")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "B.SilkS/text/136",
    "7",
    (mm("57.9"), mm("20.7")),
    layer="B.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/1",
    "SPI MSTR",
    (mm("-36.8"), mm("20.1")),
    layer="F.SilkS",
    size=(mm("1.25"), mm("2")),
    thickness=mm("0.275"),
    rot=270,
    justify="bottom",
    knockout=True,
    bold=True,
)
design.text(
    "F.SilkS/text/2",
    "SPI BI/UART",
    (mm("-36.7"), mm("-27.1")),
    layer="F.SilkS",
    size=(mm("1.25"), mm("2")),
    thickness=mm("0.275"),
    rot=270,
    justify="bottom",
    knockout=True,
    bold=True,
)
design.text(
    "F.SilkS/text/3",
    "SPI SLV",
    (mm("-36.65"), mm("-2.55")),
    layer="F.SilkS",
    size=(mm("1.25"), mm("2")),
    thickness=mm("0.275"),
    rot=270,
    justify="bottom",
    knockout=True,
    bold=True,
)
design.text(
    "F.SilkS/text/4",
    "BOOT",
    (mm("-34.35"), mm("-18.4")),
    layer="F.SilkS",
    size=(mm("1.2"), mm("1.4")),
    thickness=mm("0.2"),
    rot=270,
    justify="bottom",
    bold=True,
)
design.text(
    "F.SilkS/text/5",
    "in3",
    (mm("-33.55"), mm("34.35")),
    layer="F.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/6",
    "in2",
    (mm("-31"), mm("34.35")),
    layer="F.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/7",
    "in1",
    (mm("-28.45"), mm("34.35")),
    layer="F.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/8",
    "OFF",
    (mm("-26.3"), mm("-27.8")),
    layer="F.SilkS",
    size=(mm("1"), mm("1.4")),
    thickness=mm("0.2"),
    justify="left bottom",
    bold=True,
)
design.text(
    "F.SilkS/text/9",
    "in0",
    (mm("-26.15"), mm("34.35")),
    layer="F.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/10",
    "3v3",
    (mm("-23.4"), mm("34.35")),
    layer="F.SilkS",
    size=(mm("0.85"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/11",
    "ON",
    (mm("-19.3"), mm("-27.8")),
    layer="F.SilkS",
    size=(mm("1"), mm("1.4")),
    thickness=mm("0.2"),
    justify="left bottom",
    bold=True,
)
design.text(
    "F.SilkS/text/12",
    "in7",
    (mm("-18.4"), mm("34.35")),
    layer="F.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/13",
    "in3",
    (mm("-18.25"), mm("27.7")),
    layer="F.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/14",
    "in6",
    (mm("-15.8"), mm("34.35")),
    layer="F.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/15",
    "in2",
    (mm("-15.7"), mm("27.7")),
    layer="F.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/16",
    "0",
    (mm("-14.95"), mm("-25.01")),
    layer="F.SilkS",
    size=mm("0.9"),
    thickness=mm("0.2"),
)
design.text(
    "F.SilkS/text/17",
    "1",
    (mm("-14.95"), mm("-22.51")),
    layer="F.SilkS",
    size=mm("0.9"),
    thickness=mm("0.2"),
)
design.text(
    "F.SilkS/text/18",
    "2",
    (mm("-14.95"), mm("-20.01")),
    layer="F.SilkS",
    size=mm("0.9"),
    thickness=mm("0.2"),
)
design.text(
    "F.SilkS/text/19",
    "3",
    (mm("-14.95"), mm("-17.51")),
    layer="F.SilkS",
    size=mm("0.9"),
    thickness=mm("0.2"),
)
design.text(
    "F.SilkS/text/20",
    "4",
    (mm("-14.95"), mm("-15.01")),
    layer="F.SilkS",
    size=mm("0.9"),
    thickness=mm("0.2"),
)
design.text(
    "F.SilkS/text/21",
    "5",
    (mm("-14.95"), mm("-12.51")),
    layer="F.SilkS",
    size=mm("0.9"),
    thickness=mm("0.2"),
)
design.text(
    "F.SilkS/text/22",
    "6",
    (mm("-14.95"), mm("-10.01")),
    layer="F.SilkS",
    size=mm("0.9"),
    thickness=mm("0.2"),
)
design.text(
    "F.SilkS/text/23",
    "7",
    (mm("-14.95"), mm("-7.01")),
    layer="F.SilkS",
    size=mm("0.9"),
    thickness=mm("0.2"),
)
design.text(
    "F.SilkS/text/24",
    "in5",
    (mm("-13.25"), mm("34.35")),
    layer="F.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/25",
    "in1",
    (mm("-13.15"), mm("27.7")),
    layer="F.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/26",
    "Input ",
    (mm("-12.85"), mm("-15.41")),
    layer="F.SilkS",
    size=mm("1.8"),
    thickness=mm("0.36"),
    rot=-90,
    bold=True,
)
design.text(
    "F.SilkS/text/27",
    "in4",
    (mm("-10.75"), mm("34.35")),
    layer="F.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/28",
    "in0",
    (mm("-10.7"), mm("27.7")),
    layer="F.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/29",
    "INPUT",
    (mm("-8.4"), mm("26.2")),
    layer="F.SilkS",
    size=(mm("1.3"), mm("2")),
    thickness=mm("0.275"),
    justify="right bottom",
    knockout=True,
    bold=True,
)
design.text(
    "F.SilkS/text/30",
    "CLK",
    (mm("-8.1"), mm("34.35")),
    layer="F.SilkS",
    size=(mm("0.9"), mm("1.1")),
    thickness=mm("0.15"),
    justify="left bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/31",
    "CLOCK",
    (mm("-5.8"), mm("20.85")),
    layer="F.SilkS",
    size=(mm("1.1"), mm("1.3")),
    thickness=mm("0.25"),
    rot=90,
    justify="bottom",
    knockout=True,
    bold=True,
)
design.text(
    "F.SilkS/text/32",
    "RST",
    (mm("-5.5"), mm("34.35")),
    layer="F.SilkS",
    size=(mm("0.9"), mm("1.1")),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/33",
    "+5V",
    (mm("-3.4"), mm("-43")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/34",
    "bi3",
    (mm("-3"), mm("34.35")),
    layer="F.SilkS",
    size=(mm("1"), mm("1.1")),
    thickness=mm("0.15"),
    justify="left bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/35",
    "GND",
    (mm("-0.86"), mm("-43")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/36",
    "3v3",
    (mm("-0.55"), mm("34.35")),
    layer="F.SilkS",
    size=(mm("0.85"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/37",
    "3v3",
    (mm("1.65"), mm("-43")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/38",
    "P29",
    (mm("4.25"), mm("-43")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/39",
    "bi7",
    (mm("4.55"), mm("34.4")),
    layer="F.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/40",
    "bi3",
    (mm("4.65"), mm("27.75")),
    layer="F.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/41",
    "cEN  GND\nc++  m33\nm37  m35\n1v8  cRS\nGND  GND\nxCK  xRS\ncCK  cCS\nGND  cD0\ncD1  GPIO\n3v3  GND\nhSO  m00\nhCS  hSI\nGND  hCK\nuCK  pCK\nGND  GND\npRS  in0\nin1  in2\nin3  in4\nin5  in6\nin7  GND\n",
    (mm("5"), mm("11.4")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.51")),
    thickness=mm("0.12"),
    justify="left bottom",
    bold=True,
    face="FreeMono",
)
design.text(
    "F.SilkS/text/42",
    "GND",
    (mm("6.76"), mm("-43.1")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/43",
    "bi6",
    (mm("7.05"), mm("34.4")),
    layer="F.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/44",
    "bi2",
    (mm("7.15"), mm("27.75")),
    layer="F.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/45",
    "m33",
    (mm("9.3"), mm("-43.1")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/46",
    "bi5",
    (mm("9.55"), mm("34.4")),
    layer="F.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/47",
    "bi1",
    (mm("9.65"), mm("27.75")),
    layer="F.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/48",
    "cEN",
    (mm("11.85"), mm("-43.1")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/49",
    "WayWayWay",
    (mm("12.1"), mm("10.6")),
    layer="F.SilkS",
    size=mm("0.8"),
    thickness=mm("0.15"),
    rot=90,
    justify="left bottom",
)
design.text(
    "F.SilkS/text/50",
    "bi4",
    (mm("12.1"), mm("34.4")),
    layer="F.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/51",
    "bi0",
    (mm("12.2"), mm("27.75")),
    layer="F.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/52",
    "m35",
    (mm("14.38"), mm("-43.1")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/53",
    "BIDIR",
    (mm("14.5"), mm("26.15")),
    layer="F.SilkS",
    size=(mm("1.3"), mm("2")),
    thickness=mm("0.275"),
    justify="right bottom",
    knockout=True,
    bold=True,
)
design.text(
    "F.SilkS/text/54",
    "bi2",
    (mm("14.7"), mm("34.35")),
    layer="F.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/55",
    "RESET",
    (mm("16.55"), mm("20.8")),
    layer="F.SilkS",
    size=(mm("1.1"), mm("1.3")),
    thickness=mm("0.25"),
    rot=90,
    justify="bottom",
    knockout=True,
    bold=True,
)
design.text(
    "F.SilkS/text/56",
    "bi1",
    (mm("17.15"), mm("34.35")),
    layer="F.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/57",
    "tinytapeout.com",
    (mm("18.5"), mm("-24.7")),
    layer="F.SilkS",
    size=(mm("1"), mm("1.2")),
    thickness=mm("0.17"),
)
design.text(
    "F.SilkS/text/58",
    "zerotoasic\ncourse.com",
    (mm("18.5"), mm("-1.937734")),
    layer="F.SilkS",
    size=(mm("1"), mm("1.1")),
    thickness=mm("0.2"),
)
design.text(
    "F.SilkS/text/59",
    "bi0",
    (mm("19.65"), mm("34.35")),
    layer="F.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/60",
    "cINC",
    (mm("19.8"), mm("-43.2")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/61",
    "m37",
    (mm("22"), mm("-42.95")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/62",
    "3v3",
    (mm("22.3"), mm("34.35")),
    layer="F.SilkS",
    size=(mm("0.85"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/63",
    "cRST",
    (mm("24.54"), mm("-43")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/64",
    "3v3  GND\n3v3  GND\nbi6  bi7\nbi4  bi5\nbi2  bi3\nbi1  GND\nGND  1v8\n3v3  1v8\n3v3  GND\nGND  GND\not7  bi0\not5  GND\nGND  ot6\not3  ot4\not1  ot2\nGND  ot0\n1v8  GND\n1v8  GND\n3v3  GND\n3v3  GND",
    (mm("26.6"), mm("11.7")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.51")),
    thickness=mm("0.12"),
    justify="left bottom",
    bold=True,
    face="FreeMono",
)
design.text(
    "F.SilkS/text/65",
    "m00",
    (mm("27.1"), mm("-43")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/66",
    "ot7",
    (mm("27.35"), mm("34.4")),
    layer="F.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/67",
    "ot3",
    (mm("27.45"), mm("27.75")),
    layer="F.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/68",
    "SDO",
    (mm("29.6"), mm("-43")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/69",
    "ot6",
    (mm("29.9"), mm("34.4")),
    layer="F.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/70",
    "ot2",
    (mm("30"), mm("27.75")),
    layer="F.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/71",
    "SDI",
    (mm("32.15"), mm("-43")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/72",
    "ot5",
    (mm("32.4"), mm("34.4")),
    layer="F.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/73",
    "ot1",
    (mm("32.55"), mm("27.75")),
    layer="F.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/74",
    "GND",
    (mm("34.7"), mm("-43")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/75",
    "ot4",
    (mm("34.95"), mm("34.4")),
    layer="F.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/76",
    "ot0",
    (mm("35.15"), mm("27.75")),
    layer="F.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/77",
    "CSB",
    (mm("37.24"), mm("-43")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/78",
    "ot3",
    (mm("37.6"), mm("34.35")),
    layer="F.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/79",
    "OUTPUT",
    (mm("37.75"), mm("26.15")),
    layer="F.SilkS",
    size=(mm("1.3"), mm("2")),
    thickness=mm("0.275"),
    justify="right bottom",
    knockout=True,
    bold=True,
)
design.text(
    "F.SilkS/text/80",
    "SCK",
    (mm("39.78"), mm("-43")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/81",
    "ot2",
    (mm("40.15"), mm("34.35")),
    layer="F.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/82",
    "Using TT4+ New BKOUT",
    (mm("41.2"), mm("-2")),
    layer="F.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/83",
    "(C) 2023 Pat Deegan",
    (mm("41.2"), mm("1")),
    layer="F.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/84",
    "UCK",
    (mm("42.32"), mm("-43")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/85",
    "ot1",
    (mm("42.6"), mm("34.35")),
    layer="F.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/86",
    "GND",
    (mm("44.86"), mm("-43")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/87",
    "ot0",
    (mm("45.2"), mm("34.35")),
    layer="F.SilkS",
    size=(mm("1.05"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/88",
    "3v3",
    (mm("47.4"), mm("-43")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/89",
    "1V8",
    (mm("47.5"), mm("-33.1")),
    layer="F.SilkS",
    size=(mm("1.5"), mm("1.3")),
    thickness=mm("0.3"),
    justify="bottom",
    knockout=True,
    bold=True,
)
design.text(
    "F.SilkS/text/90",
    "5V ",
    (mm("47.75"), mm("34.35")),
    layer="F.SilkS",
    size=(mm("1.25"), mm("1")),
    thickness=mm("0.15"),
    justify="left bottom",
)
design.text(
    "F.SilkS/text/91",
    "1v8",
    (mm("49.94"), mm("-43")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/92",
    "GND",
    (mm("50.15"), mm("34.35")),
    layer="F.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="left bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/93",
    "TinyTapeout 4+\nDemoboard Alpha",
    (mm("50.95"), mm("-3.9")),
    layer="F.SilkS",
    size=(mm("1.5"), mm("2.4")),
    thickness=mm("0.375"),
    justify="bottom",
    bold=True,
)
design.text(
    "F.SilkS/text/94",
    "POWER GOOD",
    (mm("52"), mm("-31.6")),
    layer="F.SilkS",
    size=mm("1"),
    thickness=mm("0.25"),
    justify="bottom",
    knockout=True,
    bold=True,
)
design.text(
    "F.SilkS/text/95",
    "3V3",
    (mm("52.1"), mm("-33.1")),
    layer="F.SilkS",
    size=(mm("1.5"), mm("1.3")),
    thickness=mm("0.3"),
    justify="bottom",
    knockout=True,
    bold=True,
)
design.text(
    "F.SilkS/text/96",
    "GND",
    (mm("52.48"), mm("-43")),
    layer="F.SilkS",
    size=(mm("0.8"), mm("1.5")),
    thickness=mm("0.15"),
    rot=90,
    justify="right bottom",
    knockout=True,
)
design.text(
    "F.SilkS/text/97",
    "5V",
    (mm("56.5"), mm("-33.1")),
    layer="F.SilkS",
    size=(mm("1.7"), mm("1.3")),
    thickness=mm("0.3"),
    justify="bottom",
    knockout=True,
    bold=True,
)
design.text(
    "F.SilkS/text/98",
    "v0.9.4",
    (mm("59.2"), mm("-10.9")),
    layer="F.SilkS",
    size=mm("1"),
    thickness=mm("0.15"),
    justify="right bottom",
)
design.text(
    "User.1/text/1",
    "4-layer, Aisler stackup\n0.3mm drill min\n>6mil traces\nbasic controlled Z",
    (mm("41.8"), mm("51.3")),
    layer="User.1",
    size=mm("2"),
    thickness=mm("0.4"),
    justify="left bottom",
    bold=True,
)
design.dimension(
    "User.2/dimension/1",
    (mm("-39.75"), mm("-42.75")),
    (mm("57.25"), mm("-42.75")),
    offset=mm("-8.5"),
    layer="User.2",
    units="auto",
    size=mm("1"),
    thickness=mm("0.15"),
    width=mm("0.15"),
)
design.dimension(
    "User.2/dimension/2",
    (mm("-39.75"), mm("30.75")),
    (mm("-43.5"), mm("30.75")),
    offset=mm("-8.45"),
    layer="User.2",
    units="auto",
    precision=2,
    size=mm("1"),
    thickness=mm("0.15"),
    width=mm("0.15"),
    text_at=(mm("-41.625"), mm("40.7")),
)
design.dimension(
    "User.2/dimension/3",
    (mm("-39.75"), mm("30.75")),
    (mm("-39.75"), mm("34.5")),
    offset=mm("9.55"),
    layer="User.2",
    units="auto",
    precision=2,
    size=mm("1"),
    thickness=mm("0.15"),
    width=mm("0.15"),
)
design.dimension(
    "User.2/dimension/4",
    (mm("57.25"), mm("-42.75")),
    (mm("57.25"), mm("30.75")),
    offset=mm("-10.95"),
    layer="User.2",
    units="auto",
    size=mm("1"),
    thickness=mm("0.15"),
    width=mm("0.15"),
)
design.dimension(
    "User.2/dimension/5",
    (mm("58"), mm("34.5")),
    (mm("58"), mm("-46.5")),
    offset=mm("14.85"),
    layer="User.2",
    units="auto",
    size=mm("1"),
    thickness=mm("0.15"),
    width=mm("0.15"),
)
design.dimension(
    "User.2/dimension/6",
    (mm("61"), mm("-43.5")),
    (mm("-43.5"), mm("-43.5")),
    offset=mm("10.65"),
    layer="User.2",
    units="auto",
    size=mm("1"),
    thickness=mm("0.15"),
    width=mm("0.15"),
)

design.group("", j12, j13, j14, key="group/1")
design.group("", j1, j17, j2, j3, j5, j6, j8, key="group/2")
design.group("", j4, j7, key="group/3")

copper.apply(
    design,
    {
        "+1V8": net_1v8,
        "+3V3": net_3v3,
        "+5V": net_5v,
        "/CC1": cc1,
        "/CC2": cc2,
        "/RP2040/DVDD": rp2040_dvdd,
        "/RP2040/QSPI_CLK": rp2040_qspi_clk,
        "/RP2040/QSPI_SD0": rp2040_qspi_sd0,
        "/RP2040/QSPI_SD1": rp2040_qspi_sd1,
        "/RP2040/QSPI_SD2": rp2040_qspi_sd2,
        "/RP2040/QSPI_SD3": rp2040_qspi_sd3,
        "/RP2040/RUN": rp2040_run,
        "/RP2040/SWCLK": rp2040_swclk,
        "/RP2040/SWDIO": rp2040_swdio,
        "/~{CRVRST}": crvrst,
        "Caravel_CSB": caravel_csb,
        "Caravel_D0": caravel_d0,
        "Caravel_D1": caravel_d1,
        "Caravel_SCK": caravel_sck,
        "GND": gnd,
        "HK_CSB": hk_csb,
        "HK_SCK": hk_sck,
        "HK_SDI": hk_sdi,
        "HK_SDO": hk_sdo,
        "MUX_SEL": mux_sel,
        "Net-(C1-Pad2)": net_c1_pad2,
        "Net-(C3-Pad1)": net_c3_pad1,
        "Net-(C30-Pad1)": net_c30_pad1,
        "Net-(D1-A)": net_d1_a,
        "Net-(D2-A)": net_d2_a,
        "Net-(D3-A)": net_d3_a,
        "Net-(D4-A)": net_d4_a,
        "Net-(JP1-B)": net_jp1_b,
        "Net-(JP2-B)": net_jp2_b,
        "Net-(JP3-B)": net_jp3_b,
        "Net-(JP4-B)": net_jp4_b,
        "Net-(JP5-B)": net_jp5_b,
        "Net-(JP6-B)": net_jp6_b,
        "Net-(JP7-B)": net_jp7_b,
        "Net-(JP8-B)": net_jp8_b,
        "Net-(R1-Pad2)": net_r1_pad2,
        "Net-(R10-Pad2)": net_r10_pad2,
        "Net-(R11-Pad2)": net_r11_pad2,
        "Net-(R13-Pad1)": net_r13_pad1,
        "Net-(R14-Pad1)": net_r14_pad1,
        "Net-(R2-Pad2)": net_r2_pad2,
        "Net-(R3-Pad2)": net_r3_pad2,
        "Net-(R4-Pad2)": net_r4_pad2,
        "Net-(R5-Pad2)": net_r5_pad2,
        "Net-(R6-Pad2)": net_r6_pad2,
        "Net-(U1-A)": net_u1_a,
        "Net-(U1-B)": net_u1_b,
        "Net-(U1-C)": net_u1_c,
        "Net-(U1-D)": net_u1_d,
        "Net-(U1-DP)": net_u1_dp,
        "Net-(U1-E)": net_u1_e,
        "Net-(U1-F)": net_u1_f,
        "Net-(U1-G)": net_u1_g,
        "Net-(U6-XIN)": net_u6_xin,
        "Net-(U6-XOUT)": net_u6_xout,
        "Net-(U7-IO2)": net_u7_io2,
        "Net-(U7-IO3)": net_u7_io3,
        "RPIO29": rpio29,
        "RP_proj_clk": rp_proj_clk,
        "SDI/out0": sdi_out0,
        "SDO/out1": sdo_out1,
        "VBUS": vbus,
        "boot_mode": boot_mode,
        "cinc/out3": cinc_out3,
        "ctrl_ena": ctrl_ena,
        "ctrl_sel_inc": ctrl_sel_inc,
        "gpio": gpio,
        "in0": in0,
        "in1": in1,
        "in2": in2,
        "in3": in3,
        "in4": in4,
        "in5": in5,
        "in6": in6,
        "in7": in7,
        "mio33": mio33,
        "mio35": mio35,
        "mio37": mio37,
        "mprj_io0": mprj_io0,
        "out0": out0,
        "out1": out1,
        "out2": out2,
        "out3": out3,
        "out4": out4,
        "out5": out5,
        "out6": out6,
        "out7": out7,
        "project_clk": project_clk,
        "uio0": uio0,
        "uio1": uio1,
        "uio2": uio2,
        "uio3": uio3,
        "uio4": uio4,
        "uio5": uio5,
        "uio6": uio6,
        "uio7": uio7,
        "usb_d+": usb_d,
        "usb_d-": usb_d_2,
        "usrclk2": usrclk2,
        "xclk": xclk,
        "~{crst}/out2": crst_out2,
        "~{ctrl_sel_rst}": ctrl_sel_rst,
        "~{project_rst}": project_rst,
    },
)
