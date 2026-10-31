# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/video@97acc80c223d75520c03fc44cab63cd9a3202c42 by Fenolite 0.7.0.dev0 on 2026-10-31;
# modified: format conversion to the Fenolite DSL.

import copper
from fenolite.dsl import Design, Module, Net, Part, connect, mm, stack

design = Design("video")

design.board(
    outline=(
        (mm("-46.406"), mm("-43.485")),
        (mm("124.155"), mm("-43.485")),
        (mm("265.633"), mm("-43.485")),
        (mm("265.633"), mm("34.366")),
        (mm("260.553"), mm("34.366")),
        (mm("190.957"), mm("34.366")),
        (mm("116.027"), mm("34.366")),
        (mm("104.851"), mm("34.366")),
        (mm("104.851"), mm("45.542")),
        (mm("94.818"), mm("45.542")),
        (mm("85.42"), mm("54.94")),
        (mm("73.609"), mm("54.94")),
        (mm("73.609"), mm("63.195")),
        (mm("59.004"), mm("63.195")),
        (mm("59.004"), mm("54.94")),
        (mm("57.226"), mm("54.94")),
        (mm("57.226"), mm("63.195")),
        (mm("-5.639"), mm("63.195")),
        (mm("-5.639"), mm("54.94")),
        (mm("-31.42"), mm("54.94")),
        (mm("-31.42"), mm("63.195")),
        (mm("-46.406"), mm("63.195")),
    ),
    copper=4,
)
design.stackup(
    stack.silkscreen(color="White"),
    stack.mask(mm("0.01"), color="Green"),
    stack.copper(mm("0.035")),
    stack.core(mm("0.480066"), material="FR4", epsilon_r="4.5", loss_tangent="0.02"),
    stack.copper(mm("0.035")),
    stack.prepreg(mm("0.480066"), material="FR4", epsilon_r="4.5", loss_tangent="0.02"),
    stack.copper(mm("0.035")),
    stack.core(mm("0.480066"), material="FR4", epsilon_r="4.5", loss_tangent="0.02"),
    stack.copper(mm("0.035")),
    stack.mask(mm("0.01"), color="Green"),
    stack.silkscreen(color="White"),
    finish="HAL lead-free",
)
design.title_block(title="KiCad demo", date="2015-10-14", revision="1.A")

net_3_3v = Net("+3.3V")
net_5f = Net("+5F")
net_5v = Net("+5V")
pcrd = Net("//PCRD")
pcwr = Net("//PCWR")
acces_ram = Net("/ACCES_RAM-")
acq_on = Net("/ACQ_ON")
adr2 = Net("/ADR2")
adr3 = Net("/ADR3")
adr4 = Net("/ADR4")
adr5 = Net("/ADR5")
adr6 = Net("/ADR6")
be_0 = Net("/BE-0")
be_1 = Net("/BE-1")
be_2 = Net("/BE-2")
be_3 = Net("/BE-3")
blank = Net("/BLANK-")
blue_in = Net("/BLUE_IN")
blue_out = Net("/BLUE_OUT")
bpclk = Net("/BPCLK")
bt812_rd = Net("/BT812_RD-")
bt812_wr = Net("/BT812_WR-")
cas0 = Net("/CAS0-")
cas1 = Net("/CAS1-")
cas2 = Net("/CAS2-")
cas3 = Net("/CAS3-")
clamp = Net("/CLAMP")
clkcad = Net("/CLKCAD")
clkcda = Net("/CLKCDA")
csync_out = Net("/CSYNC-OUT")
csyncin = Net("/CSYNCIN-")
c_out = Net("/C_OUT")
dq0 = Net("/DQ0")
dq1 = Net("/DQ1")
dq10 = Net("/DQ10")
dq11 = Net("/DQ11")
dq12 = Net("/DQ12")
dq13 = Net("/DQ13")
dq14 = Net("/DQ14")
dq15 = Net("/DQ15")
dq16 = Net("/DQ16")
dq17 = Net("/DQ17")
dq18 = Net("/DQ18")
dq19 = Net("/DQ19")
dq2 = Net("/DQ2")
dq20 = Net("/DQ20")
dq21 = Net("/DQ21")
dq22 = Net("/DQ22")
dq23 = Net("/DQ23")
dq24 = Net("/DQ24")
dq25 = Net("/DQ25")
dq26 = Net("/DQ26")
dq27 = Net("/DQ27")
dq28 = Net("/DQ28")
dq29 = Net("/DQ29")
dq3 = Net("/DQ3")
dq30 = Net("/DQ30")
dq31 = Net("/DQ31")
dq4 = Net("/DQ4")
dq5 = Net("/DQ5")
dq6 = Net("/DQ6")
dq7 = Net("/DQ7")
dq8 = Net("/DQ8")
dq9 = Net("/DQ9")
esvideo_rvb_oe_rvb = Net("/ESVIDEO-RVB/OE_RVB-")
esvideo_rvb_ref = Net("/ESVIDEO-RVB/REF+")
esvideo_rvb_vaa = Net("/ESVIDEO-RVB/VAA")
f_palin = Net("/F_PALIN")
green_in = Net("/GREEN_IN")
green_out = Net("/GREEN_OUT")
hd_pal = Net("/HD_PAL-")
irq = Net("/IRQ-")
irq_srl = Net("/IRQ_SRL")
mxa0 = Net("/MXA0")
mxa1 = Net("/MXA1")
mxa10 = Net("/MXA10")
mxa2 = Net("/MXA2")
mxa3 = Net("/MXA3")
mxa4 = Net("/MXA4")
mxa5 = Net("/MXA5")
mxa6 = Net("/MXA6")
mxa7 = Net("/MXA7")
mxa8 = Net("/MXA8")
mxa9 = Net("/MXA9")
oe_pal = Net("/OE_PAL-")
pca0 = Net("/PCA0")
pca1 = Net("/PCA1")
pca2 = Net("/PCA2")
ptadr = Net("/PTADR-")
ptatn = Net("/PTATN-")
ptbe_0 = Net("/PTBE-0")
ptbe_1 = Net("/PTBE-1")
ptbe_2 = Net("/PTBE-2")
ptbe_3 = Net("/PTBE-3")
ptburst = Net("/PTBURST")
ptnum0 = Net("/PTNUM0")
ptnum1 = Net("/PTNUM1")
ptrdy = Net("/PTRDY-")
ptwr = Net("/PTWR")
ras0 = Net("/RAS0-")
ras1 = Net("/RAS1-")
ras2 = Net("/RAS2-")
ras3 = Net("/RAS3-")
ras4 = Net("/RAS4-")
ras5 = Net("/RAS5-")
ras6 = Net("/RAS6-")
ras7 = Net("/RAS7-")
rdcad = Net("/RDCAD-")
rdcda = Net("/RDCDA-")
rdempty = Net("/RDEMPTY")
rdfifo = Net("/RDFIFO-")
red_in = Net("/RED_IN")
red_out = Net("/RED_OUT")
select = Net("/SELECT-")
sysrst = Net("/SYSRST-")
tvb0 = Net("/TVB0")
tvb1 = Net("/TVB1")
tvb2 = Net("/TVB2")
tvb3 = Net("/TVB3")
tvb4 = Net("/TVB4")
tvb5 = Net("/TVB5")
tvb6 = Net("/TVB6")
tvb7 = Net("/TVB7")
tvg0 = Net("/TVG0")
tvg1 = Net("/TVG1")
tvg2 = Net("/TVG2")
tvg3 = Net("/TVG3")
tvg4 = Net("/TVG4")
tvg5 = Net("/TVG5")
tvg6 = Net("/TVG6")
tvg7 = Net("/TVG7")
tvi0 = Net("/TVI0")
tvi1 = Net("/TVI1")
tvr0 = Net("/TVR0")
tvr1 = Net("/TVR1")
tvr2 = Net("/TVR2")
tvr3 = Net("/TVR3")
tvr4 = Net("/TVR4")
tvr5 = Net("/TVR5")
tvr6 = Net("/TVR6")
tvr7 = Net("/TVR7")
tvram0 = Net("/TVRAM0")
tvram1 = Net("/TVRAM1")
tvram10 = Net("/TVRAM10")
tvram11 = Net("/TVRAM11")
tvram12 = Net("/TVRAM12")
tvram13 = Net("/TVRAM13")
tvram14 = Net("/TVRAM14")
tvram15 = Net("/TVRAM15")
tvram16 = Net("/TVRAM16")
tvram17 = Net("/TVRAM17")
tvram18 = Net("/TVRAM18")
tvram19 = Net("/TVRAM19")
tvram2 = Net("/TVRAM2")
tvram20 = Net("/TVRAM20")
tvram21 = Net("/TVRAM21")
tvram22 = Net("/TVRAM22")
tvram23 = Net("/TVRAM23")
tvram24 = Net("/TVRAM24")
tvram25 = Net("/TVRAM25")
tvram26 = Net("/TVRAM26")
tvram27 = Net("/TVRAM27")
tvram28 = Net("/TVRAM28")
tvram29 = Net("/TVRAM29")
tvram3 = Net("/TVRAM3")
tvram30 = Net("/TVRAM30")
tvram31 = Net("/TVRAM31")
tvram4 = Net("/TVRAM4")
tvram5 = Net("/TVRAM5")
tvram6 = Net("/TVRAM6")
tvram7 = Net("/TVRAM7")
tvram8 = Net("/TVRAM8")
tvram9 = Net("/TVRAM9")
vd_pal = Net("/VD_PAL-")
wram = Net("/WRAM-")
wrcad = Net("/WRCAD-")
wrcda = Net("/WRCDA-")
wrfifdo = Net("/WRFIFDO-")
wrfull = Net("/WRFULL")
write_ram = Net("/WRITE_RAM")
x_clk = Net("/X_CLK")
x_data = Net("/X_DATA")
x_done = Net("/X_DONE")
x_irq = Net("/X_IRQ")
x_prog = Net("/X_PROG-")
y_out = Net("/Y_OUT")
buspci_sch_ea1 = Net("/buspci.sch/EA1")
buspci_sch_ea10 = Net("/buspci.sch/EA10")
buspci_sch_ea11 = Net("/buspci.sch/EA11")
buspci_sch_ea12 = Net("/buspci.sch/EA12")
buspci_sch_ea13 = Net("/buspci.sch/EA13")
buspci_sch_ea14 = Net("/buspci.sch/EA14")
buspci_sch_ea15 = Net("/buspci.sch/EA15")
buspci_sch_ea2 = Net("/buspci.sch/EA2")
buspci_sch_ea3 = Net("/buspci.sch/EA3")
buspci_sch_ea4 = Net("/buspci.sch/EA4")
buspci_sch_ea5 = Net("/buspci.sch/EA5")
buspci_sch_ea6 = Net("/buspci.sch/EA6")
buspci_sch_ea7 = Net("/buspci.sch/EA7")
buspci_sch_ea9 = Net("/buspci.sch/EA9")
buspci_sch_eq0 = Net("/buspci.sch/EQ0")
buspci_sch_eq1 = Net("/buspci.sch/EQ1")
buspci_sch_eq2 = Net("/buspci.sch/EQ2")
buspci_sch_eq3 = Net("/buspci.sch/EQ3")
buspci_sch_eq4 = Net("/buspci.sch/EQ4")
buspci_sch_eq5 = Net("/buspci.sch/EQ5")
buspci_sch_eq6 = Net("/buspci.sch/EQ6")
buspci_sch_eq7 = Net("/buspci.sch/EQ7")
buspci_sch_p_ad0 = Net("/buspci.sch/P_AD0")
buspci_sch_p_ad1 = Net("/buspci.sch/P_AD1")
buspci_sch_p_ad10 = Net("/buspci.sch/P_AD10")
buspci_sch_p_ad11 = Net("/buspci.sch/P_AD11")
buspci_sch_p_ad12 = Net("/buspci.sch/P_AD12")
buspci_sch_p_ad13 = Net("/buspci.sch/P_AD13")
buspci_sch_p_ad14 = Net("/buspci.sch/P_AD14")
buspci_sch_p_ad15 = Net("/buspci.sch/P_AD15")
buspci_sch_p_ad16 = Net("/buspci.sch/P_AD16")
buspci_sch_p_ad17 = Net("/buspci.sch/P_AD17")
buspci_sch_p_ad18 = Net("/buspci.sch/P_AD18")
buspci_sch_p_ad19 = Net("/buspci.sch/P_AD19")
buspci_sch_p_ad2 = Net("/buspci.sch/P_AD2")
buspci_sch_p_ad20 = Net("/buspci.sch/P_AD20")
buspci_sch_p_ad21 = Net("/buspci.sch/P_AD21")
buspci_sch_p_ad22 = Net("/buspci.sch/P_AD22")
buspci_sch_p_ad23 = Net("/buspci.sch/P_AD23")
buspci_sch_p_ad24 = Net("/buspci.sch/P_AD24")
buspci_sch_p_ad25 = Net("/buspci.sch/P_AD25")
buspci_sch_p_ad26 = Net("/buspci.sch/P_AD26")
buspci_sch_p_ad27 = Net("/buspci.sch/P_AD27")
buspci_sch_p_ad28 = Net("/buspci.sch/P_AD28")
buspci_sch_p_ad29 = Net("/buspci.sch/P_AD29")
buspci_sch_p_ad3 = Net("/buspci.sch/P_AD3")
buspci_sch_p_ad30 = Net("/buspci.sch/P_AD30")
buspci_sch_p_ad31 = Net("/buspci.sch/P_AD31")
buspci_sch_p_ad4 = Net("/buspci.sch/P_AD4")
buspci_sch_p_ad5 = Net("/buspci.sch/P_AD5")
buspci_sch_p_ad6 = Net("/buspci.sch/P_AD6")
buspci_sch_p_ad7 = Net("/buspci.sch/P_AD7")
buspci_sch_p_ad8 = Net("/buspci.sch/P_AD8")
buspci_sch_p_ad9 = Net("/buspci.sch/P_AD9")
buspci_sch_p_c_be0 = Net("/buspci.sch/P_C/BE0#")
buspci_sch_p_c_be1 = Net("/buspci.sch/P_C/BE1#")
buspci_sch_p_c_be2 = Net("/buspci.sch/P_C/BE2#")
buspci_sch_p_c_be3 = Net("/buspci.sch/P_C/BE3#")
buspci_sch_p_clk = Net("/buspci.sch/P_CLK")
buspci_sch_p_devsel = Net("/buspci.sch/P_DEVSEL#")
buspci_sch_p_frame = Net("/buspci.sch/P_FRAME#")
buspci_sch_p_gnt = Net("/buspci.sch/P_GNT#")
buspci_sch_p_idsel = Net("/buspci.sch/P_IDSEL")
buspci_sch_p_inta = Net("/buspci.sch/P_INTA#")
buspci_sch_p_irdy = Net("/buspci.sch/P_IRDY#")
buspci_sch_p_lock = Net("/buspci.sch/P_LOCK#")
buspci_sch_p_par = Net("/buspci.sch/P_PAR")
buspci_sch_p_perr = Net("/buspci.sch/P_PERR#")
buspci_sch_p_req = Net("/buspci.sch/P_REQ#")
buspci_sch_p_rst = Net("/buspci.sch/P_RST#")
buspci_sch_p_serr = Net("/buspci.sch/P_SERR#")
buspci_sch_p_stop = Net("/buspci.sch/P_STOP#")
buspci_sch_p_trdy = Net("/buspci.sch/P_TRDY#")
graphic_14mhzout = Net("/graphic/14MHZOUT")
graphic_cclk = Net("/graphic/CCLK")
graphic_clk10mhz = Net("/graphic/CLK10MHz")
graphic_csio = Net("/graphic/CSIO-")
graphic_din = Net("/graphic/DIN")
graphic_done = Net("/graphic/DONE")
graphic_hdout = Net("/graphic/HDOUT")
graphic_hdrefout = Net("/graphic/HDREFOUT")
graphic_ia0 = Net("/graphic/IA0")
graphic_ia1 = Net("/graphic/IA1")
graphic_ia2 = Net("/graphic/IA2")
graphic_ia3 = Net("/graphic/IA3")
graphic_ia4 = Net("/graphic/IA4")
graphic_ia5 = Net("/graphic/IA5")
graphic_ia6 = Net("/graphic/IA6")
graphic_ia7 = Net("/graphic/IA7")
graphic_ia8 = Net("/graphic/IA8")
graphic_ia9 = Net("/graphic/IA9")
graphic_icas = Net("/graphic/ICAS-")
graphic_id0 = Net("/graphic/ID0")
graphic_id1 = Net("/graphic/ID1")
graphic_id2 = Net("/graphic/ID2")
graphic_id3 = Net("/graphic/ID3")
graphic_ioe = Net("/graphic/IOE-")
graphic_iras = Net("/graphic/IRAS-")
graphic_iwr = Net("/graphic/IWR-")
graphic_led = Net("/graphic/LED")
graphic_prog = Net("/graphic/PROG*")
graphic_reserv1 = Net("/graphic/RESERV1")
graphic_vosc = Net("/graphic/VOSC")
graphic_xtal_i = Net("/graphic/XTAL_I")
graphic_x_din = Net("/graphic/X_DIN")
modul_chrom = Net("/modul/CHROM")
modul_cvbs = Net("/modul/CVBS")
modul_cvbsout = Net("/modul/CVBSOUT")
modul_lum = Net("/modul/LUM")
pal_ntsc_sch_c_video = Net("/pal-ntsc.sch/C-VIDEO")
pal_ntsc_sch_vaf = Net("/pal-ntsc.sch/VAF")
pal_ntsc_sch_y_video = Net("/pal-ntsc.sch/Y-VIDEO")
pal_ntsc_sch_y_sync = Net("/pal-ntsc.sch/Y_SYNC")
gnd = Net("GND")
net_bus1_prsnt1 = Net("Net-(BUS1-PRSNT1#)")
net_bus1_prsnt2 = Net("Net-(BUS1-PRSNT2#)")
net_bus1_tdi = Net("Net-(BUS1-TDI)")
net_c1_pad1 = Net("Net-(C1-Pad1)")
net_c3_pad1 = Net("Net-(C3-Pad1)")
net_c36_pad2 = Net("Net-(C36-Pad2)")
net_c39_pad2 = Net("Net-(C39-Pad2)")
net_c4_pad1 = Net("Net-(C4-Pad1)")
net_c40_pad2 = Net("Net-(C40-Pad2)")
net_c41_pad2 = Net("Net-(C41-Pad2)")
net_c46_pad1 = Net("Net-(C46-Pad1)")
net_c49_pad1 = Net("Net-(C49-Pad1)")
net_c5_pad2 = Net("Net-(C5-Pad2)")
net_c61_pad1 = Net("Net-(C61-Pad1)")
net_c8_pad2 = Net("Net-(C8-Pad2)")
net_cv1_pad1 = Net("Net-(CV1-Pad1)")
net_d6_a = Net("Net-(D6-A)")
net_l6_pad1 = Net("Net-(L6-Pad1)")
net_p4_p1 = Net("Net-(P4-P1)")
net_pot1_pad3 = Net("Net-(POT1-Pad3)")
net_q1_b = Net("Net-(Q1-B)")
net_q1_e = Net("Net-(Q1-E)")
net_q2_b = Net("Net-(Q2-B)")
net_q2_e = Net("Net-(Q2-E)")
net_q3_b = Net("Net-(Q3-B)")
net_q3_e = Net("Net-(Q3-E)")
net_u1_scl = Net("Net-(U1-SCL)")
net_u1_sda = Net("Net-(U1-SDA)")
net_u10_clevel = Net("Net-(U10-CLEVEL)")
net_u10_cref = Net("Net-(U10-CREF+)")
net_u10_n_c = Net("Net-(U10-N/C)")
net_u10_out_c = Net("Net-(U10-OUT_C)")
net_u10_r_2 = Net("Net-(U10-R/2)")
net_u10_sync_det = Net("Net-(U10-SYNC_DET)")
net_u10_vin_c = Net("Net-(U10-VIN_C)")
net_u10_vin_y_comp = Net("Net-(U10-VIN_Y/COMP.)")
net_u10_xtal1_in = Net("Net-(U10-XTAL1_IN)")
net_u10_xtal1_out = Net("Net-(U10-XTAL1_OUT)")
net_u11_flt = Net("Net-(U11-FLT#)")
net_u11_mode_16_32 = Net("Net-(U11-MODE_16/32)")
net_u11_snv = Net("Net-(U11-SNV)")
net_u20_b = Net("Net-(U20-B)")
net_u20_b_adj = Net("Net-(U20-B/ADJ)")
net_u20_cs = Net("Net-(U20-CS)")
net_u20_flt = Net("Net-(U20-FLT)")
net_u20_g = Net("Net-(U20-G)")
net_u20_mctr = Net("Net-(U20-MCTR)")
net_u20_notch = Net("Net-(U20-NOTCH)")
net_u20_osc = Net("Net-(U20-OSC)")
net_u20_r = Net("Net-(U20-R)")
net_u20_uoff = Net("Net-(U20-UOFF)")
net_u20_vcc = Net("Net-(U20-VCC)")
net_u20_voff = Net("Net-(U20-VOFF)")
net_u20_vref = Net("Net-(U20-VREF)")
net_u20_y_sin = Net("Net-(U20-Y+SIN)")
net_u20_y_sout = Net("Net-(U20-Y+SOUT)")
net_u23_p87 = Net("Net-(U23-P87)")
net_u23_pgck4 = Net("Net-(U23-PGCK4)")
net_u23_sgck3 = Net("Net-(U23-SGCK3)")
net_u8_bin = Net("Net-(U8-BIN)")
net_u8_bvid0 = Net("Net-(U8-BVID0)")
net_u8_cext1 = Net("Net-(U8-CEXT1)")
net_u8_cext2 = Net("Net-(U8-CEXT2)")
net_u8_gin = Net("Net-(U8-GIN)")
net_u8_gvid0 = Net("Net-(U8-GVID0)")
net_u8_rin = Net("Net-(U8-RIN)")
net_u8_rset = Net("Net-(U8-RSET)")
net_u8_rvid0 = Net("Net-(U8-RVID0)")
net_u9_comp = Net("Net-(U9-COMP)")
net_u9_iref = Net("Net-(U9-IREF)")
net_u9_vref = Net("Net-(U9-VREF)")

design.rules.netclass(
    "pwr",
    clearance=mm("0.2"),
    track_width=mm("0.25"),
    via_diameter=mm("0.8"),
    via_drill=mm("0.4"),
    diff_pair_width=mm("0.2"),
    diff_pair_gap=mm("0.25"),
    diff_pair_via_gap=mm("0.25"),
    nets=(net_3_3v, net_5f),
)
design.rules.minimum(
    clearance=mm("0.1"),
    via_diameter=mm("0.8"),
    hole_size=mm("0.4"),
    edge_clearance=mm("0.01"),
)

bus1 = Part("BUS1", "footprints:BUSPCI", footprint="footprints:BUSPCI", value="BUSPCI_5V")
c24 = Part(
    "C24",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="100nF",
)
c25 = Part(
    "C25",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    value="100nF",
)
c26 = Part(
    "C26",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    value="100nF",
)
c27 = Part(
    "C27",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="100nF",
)
c28 = Part(
    "C28",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    value="100nF",
)
c29 = Part(
    "C29",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    value="100nF",
)
c30 = Part(
    "C30",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="100nF",
)
c31 = Part(
    "C31",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="100nF",
)
c38 = Part(
    "C38",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    value="4,7uF",
)
c67 = Part(
    "C67",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    value="4,7uF",
)
c68 = Part(
    "C68",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    value="4,7uF",
)
c69 = Part(
    "C69",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="4,7uF",
)
r5 = Part(
    "R5",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="10K",
)
r6 = Part(
    "R6",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    value="10K",
)
r7 = Part(
    "R7",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    value="10K",
)
r28 = Part(
    "R28",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
    value="2,2K",
)
r29 = Part(
    "R29",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
    value="2,2K",
)
rr1 = Part("RR1", "footprints:R_Array_SIP9", footprint="footprints:R_Array_SIP9", value="8x10K")
rr2 = Part("RR2", "footprints:R_Array_SIP9", footprint="footprints:R_Array_SIP9", value="8x10K")
rr3 = Part("RR3", "footprints:R_Array_SIP9_2", footprint="footprints:R_Array_SIP9_2", value="8x10K")
rr4 = Part("RR4", "footprints:R_Array_SIP9_3", footprint="footprints:R_Array_SIP9_3", value="8x10K")
rr5 = Part("RR5", "footprints:R_Array_SIP9_3", footprint="footprints:R_Array_SIP9_3", value="8x10K")
rr6 = Part("RR6", "footprints:R_Array_SIP9_3", footprint="footprints:R_Array_SIP9_3", value="8x10K")
rr7 = Part("RR7", "footprints:R_Array_SIP9_4", footprint="footprints:R_Array_SIP9_4", value="8x10K")
rr8 = Part("RR8", "footprints:R_Array_SIP9_5", footprint="footprints:R_Array_SIP9_5", value="8x10K")
u1 = Part("U1", "footprints:DIP-8_W7.62mm", footprint="footprints:DIP-8_W7.62mm", value="24C16")
u11 = Part(
    "U11",
    "footprints:PQFP-160_28x28mm_P0.65mm_2",
    footprint="footprints:PQFP-160_28x28mm_P0.65mm_2",
    value="S5933_PQ160",
)
w1 = Part(
    "W1",
    "footprints:SolderJumper-2_P1.3mm_Open_Pad1.0x1.5mm",
    footprint="footprints:SolderJumper-2_P1.3mm_Open_Pad1.0x1.5mm",
    value="16/32",
)
w2 = Part(
    "W2",
    "footprints:SolderJumper-2_P1.3mm_Open_Pad1.0x1.5mm_2",
    footprint="footprints:SolderJumper-2_P1.3mm_Open_Pad1.0x1.5mm_2",
    value="FLOAT#",
)
w3 = Part(
    "W3",
    "footprints:SolderJumper-2_P1.3mm_Open_Pad1.0x1.5mm_3",
    footprint="footprints:SolderJumper-2_P1.3mm_Open_Pad1.0x1.5mm_3",
    value="SERNV",
)
w4 = Part(
    "W4",
    "footprints:PinHeader_1x02_P2.54mm_Vertical_2",
    footprint="footprints:PinHeader_1x02_P2.54mm_Vertical_2",
    value="TEST",
)
w5 = Part(
    "W5",
    "footprints:PinHeader_1x02_P2.54mm_Vertical_3",
    footprint="footprints:PinHeader_1x02_P2.54mm_Vertical_3",
    value="TEST",
)
c32 = Part(
    "C32",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    value="100nF",
)
c33 = Part(
    "C33",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="100nF",
)
c34 = Part(
    "C34",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_7",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_7",
    value="100nF",
)
c35 = Part(
    "C35",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="100nF",
)
c36 = Part(
    "C36",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_8",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_8",
    value="100nF",
)
c37 = Part(
    "C37",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_9",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_9",
    value="100pF",
)
c39 = Part(
    "C39",
    "footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder",
    footprint="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder",
    value="1uF",
)
c40 = Part(
    "C40",
    "footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_2",
    footprint="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_2",
    value="1uF",
)
c41 = Part(
    "C41",
    "footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_3",
    footprint="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_3",
    value="1uF",
)
c42 = Part(
    "C42",
    "footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_4",
    footprint="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_4",
    value="2.2uF",
)
c51 = Part(
    "C51",
    "footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_5",
    footprint="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_5",
    value="22uF",
)
c52 = Part(
    "C52",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="22uF",
)
l5 = Part(
    "L5",
    "footprints:R_1812_4532Metric_Pad1.30x3.40mm_HandSolder_2",
    footprint="footprints:R_1812_4532Metric_Pad1.30x3.40mm_HandSolder_2",
    value="22uH",
)
r8 = Part(
    "R8",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_18",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_18",
    value="150",
)
r15 = Part(
    "R15",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_24",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_24",
    value="1M",
)
r22 = Part(
    "R22",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_28",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_28",
    value="220",
)
r23 = Part(
    "R23",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_18",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_18",
    value="220",
)
r24 = Part(
    "R24",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_18",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_18",
    value="220",
)
r36 = Part(
    "R36",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_36",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_36",
    value="470",
)
r37 = Part(
    "R37",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_37",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_37",
    value="510",
)
r38 = Part(
    "R38",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="510",
)
r42 = Part(
    "R42",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_40",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_40",
    value="75",
)
r43 = Part(
    "R43",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_41",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_41",
    value="75",
)
r44 = Part(
    "R44",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_42",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_42",
    value="75",
)
r45 = Part(
    "R45",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
    value="75",
)
r46 = Part(
    "R46",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_5",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_5",
    value="75",
)
r47 = Part(
    "R47",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="75",
)
u8 = Part("U8", "footprints:PLCC84", footprint="footprints:PLCC84", value="BT253")
u9 = Part("U9", "footprints:PLCC68", footprint="footprints:PLCC68", value="BT473")
c17 = Part(
    "C17",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    value="100nF",
)
c18 = Part(
    "C18",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_5",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_5",
    value="100nF",
)
c19 = Part(
    "C19",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    value="100nF",
)
c20 = Part(
    "C20",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="100nF",
)
c21 = Part(
    "C21",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="100nF",
)
c22 = Part(
    "C22",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="100nF",
)
c23 = Part(
    "C23",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="100nF",
)
c49 = Part(
    "C49",
    "footprints:C_Disc_D3.0mm_W2.0mm_P2.50mm",
    footprint="footprints:C_Disc_D3.0mm_W2.0mm_P2.50mm",
    value="22pF",
)
c50 = Part(
    "C50",
    "footprints:C_Disc_D3.0mm_W2.0mm_P2.50mm_2",
    footprint="footprints:C_Disc_D3.0mm_W2.0mm_P2.50mm_2",
    value="22pF",
)
c56 = Part(
    "C56",
    "footprints:CP_EIA-3528-21_Kemet-B_Pad1.50x2.35mm_HandSolder",
    footprint="footprints:CP_EIA-3528-21_Kemet-B_Pad1.50x2.35mm_HandSolder",
    value="4.7uF",
)
c57 = Part(
    "C57",
    "footprints:CP_EIA-3528-21_Kemet-B_Pad1.50x2.35mm_HandSolder",
    footprint="footprints:CP_EIA-3528-21_Kemet-B_Pad1.50x2.35mm_HandSolder",
    value="4.7uF",
)
c63 = Part(
    "C63",
    "footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_7",
    footprint="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_7",
    value="47uF",
)
c70 = Part(
    "C70",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    value="100nF",
)
c71 = Part(
    "C71",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    value="100nF",
)
c72 = Part(
    "C72",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_21",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_21",
    value="100nF",
)
c73 = Part(
    "C73",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="100nF",
)
d6 = Part("D6", "footprints:LED_D3.0mm", footprint="footprints:LED_D3.0mm", value="LED")
p4 = Part(
    "P4",
    "footprints:PinHeader_1x02_P2.54mm_Vertical",
    footprint="footprints:PinHeader_1x02_P2.54mm_Vertical",
    value="CONN_2",
)
p5 = Part(
    "P5",
    "footprints:PinHeader_1x05_P2.54mm_Vertical",
    footprint="footprints:PinHeader_1x05_P2.54mm_Vertical",
    value="CONN_5",
)
p9 = Part(
    "P9",
    "footprints:PinHeader_1x01_P2.54mm_Vertical_2",
    footprint="footprints:PinHeader_1x01_P2.54mm_Vertical_2",
    value="CONN_1",
)
p10 = Part(
    "P10",
    "footprints:PinHeader_1x01_P2.54mm_Vertical",
    footprint="footprints:PinHeader_1x01_P2.54mm_Vertical",
    value="CONN_1",
)
p11 = Part(
    "P11",
    "footprints:PinHeader_1x01_P2.54mm_Vertical_2",
    footprint="footprints:PinHeader_1x01_P2.54mm_Vertical_2",
    value="CONN_1",
)
p12 = Part(
    "P12",
    "footprints:PinHeader_1x01_P2.54mm_Vertical_3",
    footprint="footprints:PinHeader_1x01_P2.54mm_Vertical_3",
    value="CONN_1",
)
r1 = Part(
    "R1",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_22",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_22",
    value="10",
    properties={"Champ7": ""},
)
r13 = Part(
    "R13",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="1K",
)
r21 = Part(
    "R21",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    value="220",
)
r26 = Part(
    "R26",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="220K",
)
r48 = Part(
    "R48",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="10K",
    properties={"Champ7": ""},
)
u2 = Part(
    "U2",
    "footprints:SOIC-28W_7.5x17.9mm_P1.27mm",
    footprint="footprints:SOIC-28W_7.5x17.9mm_P1.27mm",
    value="4C4001",
)
u7 = Part(
    "U7",
    "footprints:SSOP-8_3.95x5.21x3.27mm_P1.27mm",
    footprint="footprints:SSOP-8_3.95x5.21x3.27mm_P1.27mm",
    value="AV9173",
)
u21 = Part("U21", "footprints:DIP-8_W7.62mm", footprint="footprints:DIP-8_W7.62mm", value="XC1736APD8")
u23 = Part(
    "U23",
    "footprints:PQFP-100_14x20mm_P0.65mm",
    footprint="footprints:PQFP-100_14x20mm_P0.65mm",
    value="XC4003/PQ100",
)
u24 = Part(
    "U24",
    "footprints:PQFP-160_28x28mm_P0.65mm_2",
    footprint="footprints:PQFP-160_28x28mm_P0.65mm_2",
    value="XC4005-PQ160",
)
x1 = Part(
    "X1",
    "footprints:Crystal_HC18-U_Vertical",
    footprint="footprints:Crystal_HC18-U_Vertical",
    value="10MHz",
)
c43 = Part(
    "C43",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="220nF",
)
c44 = Part(
    "C44",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    value="220nF",
)
c45 = Part(
    "C45",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_11",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_11",
    value="220nF",
)
c46 = Part(
    "C46",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_12",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_12",
    value="220pF",
)
c48 = Part(
    "C48",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_14",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_14",
    value="22nF",
)
c53 = Part(
    "C53",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_16",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_16",
    value="330pF",
)
c54 = Part(
    "C54",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_5",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_5",
    value="4.7uF",
)
c55 = Part(
    "C55",
    "footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_6",
    footprint="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_6",
    value="4.7uF",
)
c58 = Part(
    "C58",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
    value="47nF",
)
c59 = Part(
    "C59",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_17",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_17",
    value="47nF",
)
c60 = Part(
    "C60",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
    value="47nF",
)
c61 = Part(
    "C61",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_18",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_18",
    value="47nF",
)
c64 = Part(
    "C64",
    "footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_6",
    footprint="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_6",
    value="6,8uF",
)
cv1 = Part("CV1", "footprints:CV3-30PF", footprint="footprints:CV3-30PF", value="5/30pF")
l1 = Part(
    "L1",
    "footprints:R_1812_4532Metric_Pad1.30x3.40mm_HandSolder",
    footprint="footprints:R_1812_4532Metric_Pad1.30x3.40mm_HandSolder",
    value="2,2uH",
)
l2 = Part(
    "L2",
    "footprints:R_1812_4532Metric_Pad1.30x3.40mm_HandSolder_2",
    footprint="footprints:R_1812_4532Metric_Pad1.30x3.40mm_HandSolder_2",
    value="22uH",
)
l3 = Part(
    "L3",
    "footprints:R_1812_4532Metric_Pad1.30x3.40mm_HandSolder",
    footprint="footprints:R_1812_4532Metric_Pad1.30x3.40mm_HandSolder",
    value="22uH",
)
l6 = Part("L6", "footprints:LRTDK", footprint="footprints:LRTDK", value="470ns")
pot1 = Part(
    "POT1",
    "footprints:Potentiometer_Bourns_3314G_Vertical",
    footprint="footprints:Potentiometer_Bourns_3314G_Vertical",
    value="100K",
)
q1 = Part("Q1", "footprints:SOT23EBC", footprint="footprints:SOT23EBC", value="BC848")
q2 = Part("Q2", "footprints:SOT23EBC", footprint="footprints:SOT23EBC", value="BC848")
q3 = Part("Q3", "footprints:SOT23EBC", footprint="footprints:SOT23EBC", value="BC848")
r4 = Part(
    "R4",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
    value="10K",
    properties={"Champ7": ""},
)
r9 = Part(
    "R9",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_5",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_5",
    value="150K",
)
r10 = Part(
    "R10",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_18",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_18",
    value="1K",
)
r11 = Part(
    "R11",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
    value="1K",
)
r16 = Part(
    "R16",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    value="220",
)
r17 = Part(
    "R17",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    value="220",
)
r18 = Part(
    "R18",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_25",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_25",
    value="220",
)
r30 = Part(
    "R30",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_31",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_31",
    value="3,3K",
)
r31 = Part(
    "R31",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_32",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_32",
    value="470",
)
r32 = Part(
    "R32",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="470",
)
r33 = Part(
    "R33",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_33",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_33",
    value="470",
)
r34 = Part(
    "R34",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_34",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_34",
    value="470",
)
r39 = Part(
    "R39",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_38",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_38",
    value="68",
)
r40 = Part(
    "R40",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    value="68",
)
r41 = Part(
    "R41",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_39",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_39",
    value="68",
)
u20 = Part(
    "U20",
    "footprints:SOIC-24W_7.5x15.4mm_P1.27mm",
    footprint="footprints:SOIC-24W_7.5x15.4mm_P1.27mm",
    value="TDA8501",
)
x3 = Part(
    "X3",
    "footprints:Crystal_HC18-U_Horizontal",
    footprint="footprints:Crystal_HC18-U_Horizontal",
    value="4.433618MHz",
)
u3 = Part(
    "U3",
    "footprints:SOIC-20W_7.5x12.8mm_P1.27mm",
    footprint="footprints:SOIC-20W_7.5x12.8mm_P1.27mm",
    value="74LS245",
)
u4 = Part(
    "U4",
    "footprints:SOIC-20W_7.5x12.8mm_P1.27mm_2",
    footprint="footprints:SOIC-20W_7.5x12.8mm_P1.27mm_2",
    value="74LS245",
)
u5 = Part(
    "U5",
    "footprints:SOIC-20W_7.5x12.8mm_P1.27mm_2",
    footprint="footprints:SOIC-20W_7.5x12.8mm_P1.27mm_2",
    value="74LS245",
)
u6 = Part(
    "U6",
    "footprints:SOIC-20W_7.5x12.8mm_P1.27mm_3",
    footprint="footprints:SOIC-20W_7.5x12.8mm_P1.27mm_3",
    value="74LS245",
)
u22 = Part(
    "U22",
    "footprints:TQFP-100_14x14mm_P0.5mm",
    footprint="footprints:TQFP-100_14x14mm_P0.5mm",
    value="XC4003-VQ100",
)
c1 = Part(
    "C1",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
    value="100nF",
)
c2 = Part(
    "C2",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    value="100nF",
)
c3 = Part(
    "C3",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_6",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_6",
    value="100nF",
)
c4 = Part(
    "C4",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_10",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_10",
    value="100nF",
)
c5 = Part(
    "C5",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_15",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_15",
    value="100nF",
)
c6 = Part(
    "C6",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    value="100nF",
)
c7 = Part(
    "C7",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_20",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_20",
    value="100nF",
)
c8 = Part(
    "C8",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    value="100nF",
)
c9 = Part(
    "C9",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="100nF",
)
c10 = Part(
    "C10",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="100nF",
)
c11 = Part(
    "C11",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    value="100nF",
)
c12 = Part(
    "C12",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    value="100nF",
)
c13 = Part(
    "C13",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="100nF",
)
c14 = Part(
    "C14",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    value="100nF",
)
c15 = Part(
    "C15",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="100nF",
)
c16 = Part(
    "C16",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
    value="100nF",
)
c47 = Part(
    "C47",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_13",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_13",
    value="220pF",
)
c62 = Part(
    "C62",
    "footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_4",
    footprint="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_4",
    value="47uF",
)
c65 = Part(
    "C65",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_19",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_19",
    value="22pF",
)
c66 = Part(
    "C66",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="22pF",
)
d1 = Part(
    "D1",
    "footprints:D_DO-34_SOD68_P7.62mm_Horizontal",
    footprint="footprints:D_DO-34_SOD68_P7.62mm_Horizontal",
    value="BAT46",
)
d2 = Part(
    "D2",
    "footprints:D_DO-34_SOD68_P7.62mm_Horizontal",
    footprint="footprints:D_DO-34_SOD68_P7.62mm_Horizontal",
    value="BAT46",
)
d3 = Part(
    "D3",
    "footprints:D_DO-34_SOD68_P7.62mm_Horizontal",
    footprint="footprints:D_DO-34_SOD68_P7.62mm_Horizontal",
    value="BAT46",
)
d4 = Part(
    "D4",
    "footprints:D_DO-34_SOD68_P7.62mm_Horizontal",
    footprint="footprints:D_DO-34_SOD68_P7.62mm_Horizontal",
    value="BAT46",
)
l4 = Part(
    "L4",
    "footprints:R_1812_4532Metric_Pad1.30x3.40mm_HandSolder",
    footprint="footprints:R_1812_4532Metric_Pad1.30x3.40mm_HandSolder",
    value="22uF",
)
r2 = Part(
    "R2",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_27",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_27",
    value="100",
)
r3 = Part(
    "R3",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_30",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_30",
    value="100",
)
r12 = Part(
    "R12",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_23",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_23",
    value="1K",
)
r14 = Part(
    "R14",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_18",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_18",
    value="1M",
)
r19 = Part(
    "R19",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_26",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_26",
    value="220",
)
r20 = Part(
    "R20",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="220",
)
r25 = Part(
    "R25",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    value="220K",
)
r27 = Part(
    "R27",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_29",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_29",
    value="27K",
)
r35 = Part(
    "R35",
    "footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_35",
    footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_35",
    value="470",
)
u10 = Part(
    "U10",
    "footprints:PQFP-160_28x28mm_P0.65mm",
    footprint="footprints:PQFP-160_28x28mm_P0.65mm",
    value="BT812",
)
x2 = Part(
    "X2",
    "footprints:Crystal_HC18-U_Vertical_2",
    footprint="footprints:Crystal_HC18-U_Vertical_2",
    value="30MHz",
)
j4 = Part(
    "J4",
    "footprints:DSUB-9_Female_Horizontal_P2.77x2.84mm_EdgePinOffset14.56mm_Housed_MountingHolesOffset15.98mm",
    footprint="footprints:DSUB-9_Female_Horizontal_P2.77x2.84mm_EdgePinOffset14.56mm_Housed_MountingHolesOffset15.98mm",
    value="DB9FEM",
)
p1 = Part("P1", "footprints:subclick", footprint="footprints:subclick", value="BNC")
p2 = Part("P2", "footprints:subclick_2", footprint="footprints:subclick_2", value="BNC")
p3 = Part("P3", "footprints:subclick_3", footprint="footprints:subclick_3", value="BNC")
p8 = Part("P8", "footprints:subclick_4", footprint="footprints:subclick_4", value="BNC")
u12 = Part("U12", "footprints:sim72", footprint="footprints:sim72", value="SIM4X32")
u13 = Part("U13", "footprints:sim72_2", footprint="footprints:sim72_2", value="SIM4X32")
u14 = Part("U14", "footprints:sim72_3", footprint="footprints:sim72_3", value="SIM4X32")
u15 = Part("U15", "footprints:sim72", footprint="footprints:sim72", value="SIM4X32")
u16 = Part("U16", "footprints:sim72", footprint="footprints:sim72", value="SIM4X32")
u17 = Part("U17", "footprints:sim72", footprint="footprints:sim72", value="SIM4X32")
u18 = Part("U18", "footprints:sim72", footprint="footprints:sim72", value="SIM4X32")
u19 = Part("U19", "footprints:sim72", footprint="footprints:sim72", value="SIM4X32")

buspci_sch = Module("buspci_sch")
esvideo_rvb = Module("esvideo_rvb")
graphic = Module("graphic")
modul = Module("modul")
muxdata = Module("muxdata")
pal_ntsc_sch = Module("pal_ntsc_sch")
racine = Module("racine")
rams = Module("rams")

buspci_sch.add(
    bus1,
    c24,
    c25,
    c26,
    c27,
    c28,
    c29,
    c30,
    c31,
    c38,
    c67,
    c68,
    c69,
    r5,
    r6,
    r7,
    r28,
    r29,
    rr1,
    rr2,
    rr3,
    rr4,
    rr5,
    rr6,
    rr7,
    rr8,
    u1,
    u11,
    w1,
    w2,
    w3,
    w4,
    w5,
)
esvideo_rvb.add(
    c32,
    c33,
    c34,
    c35,
    c36,
    c37,
    c39,
    c40,
    c41,
    c42,
    c51,
    c52,
    l5,
    r8,
    r15,
    r22,
    r23,
    r24,
    r36,
    r37,
    r38,
    r42,
    r43,
    r44,
    r45,
    r46,
    r47,
    u8,
    u9,
)
graphic.add(
    c17,
    c18,
    c19,
    c20,
    c21,
    c22,
    c23,
    c49,
    c50,
    c56,
    c57,
    c63,
    c70,
    c71,
    c72,
    c73,
    d6,
    p4,
    p5,
    p9,
    p10,
    p11,
    p12,
    r1,
    r13,
    r21,
    r26,
    r48,
    u2,
    u7,
    u21,
    u23,
    u24,
    x1,
)
modul.add(
    c43,
    c44,
    c45,
    c46,
    c48,
    c53,
    c54,
    c55,
    c58,
    c59,
    c60,
    c61,
    c64,
    cv1,
    l1,
    l2,
    l3,
    l6,
    pot1,
    q1,
    q2,
    q3,
    r4,
    r9,
    r10,
    r11,
    r16,
    r17,
    r18,
    r30,
    r31,
    r32,
    r33,
    r34,
    r39,
    r40,
    r41,
    u20,
    x3,
)
muxdata.add(u3, u4, u5, u6, u22)
pal_ntsc_sch.add(
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
    c47,
    c62,
    c65,
    c66,
    d1,
    d2,
    d3,
    d4,
    l4,
    r2,
    r3,
    r12,
    r14,
    r19,
    r20,
    r25,
    r27,
    r35,
    u10,
    x2,
)
racine.add(j4, p1, p2, p3, p8)
rams.add(u12, u13, u14, u15, u16, u17, u18, u19)
design.add(buspci_sch, esvideo_rvb, graphic, modul, muxdata, pal_ntsc_sch, racine, rams)

connect(
    net_3_3v,
    bus1["A21"],
    bus1["A27"],
    bus1["A33"],
    bus1["A39"],
    bus1["A45"],
    bus1["A53"],
    bus1["B25"],
    bus1["B31"],
    bus1["B36"],
    bus1["B41"],
    bus1["B43"],
    bus1["B54"],
    c68["1"],
    c69["1"],
)
connect(net_5f, c55["1"], l3["2"], q1["3"], q2["3"], q3["3"])
connect(
    net_5v,
    bus1["A5"],
    bus1["A8"],
    bus1["A10"],
    bus1["A16"],
    bus1["A59"],
    bus1["A61"],
    bus1["A62"],
    bus1["B5"],
    bus1["B6"],
    bus1["B19"],
    bus1["B59"],
    bus1["B61"],
    bus1["B62"],
    c9["1"],
    c10["1"],
    c11["1"],
    c15["1"],
    c17["1"],
    c18["1"],
    c19["1"],
    c20["1"],
    c21["1"],
    c22["1"],
    c24["1"],
    c25["1"],
    c26["1"],
    c27["1"],
    c28["1"],
    c29["1"],
    c30["1"],
    c31["1"],
    c38["1"],
    c56["1"],
    c57["1"],
    c67["1"],
    c70["1"],
    c71["1"],
    c72["1"],
    c73["1"],
    d2["2"],
    d4["2"],
    l2["1"],
    l3["1"],
    l4["1"],
    l5["1"],
    r1["2"],
    r4["2"],
    r5["2"],
    r6["2"],
    r7["2"],
    r13["1"],
    r28["1"],
    r29["1"],
    r48["1"],
    rr1["1"],
    rr2["1"],
    rr3["1"],
    rr4["1"],
    rr5["1"],
    rr6["1"],
    rr7["1"],
    rr8["1"],
    u1["7"],
    u1["8"],
    u2["10"],
    u3["20"],
    u4["20"],
    u5["20"],
    u6["20"],
    u10["31"],
    u10["45"],
    u10["57"],
    u10["76"],
    u10["91"],
    u10["102"],
    u10["112"],
    u11["11"],
    u11["31"],
    u11["51"],
    u11["71"],
    u11["91"],
    u11["111"],
    u11["131"],
    u11["151"],
    u12["10"],
    u12["30"],
    u12["59"],
    u13["10"],
    u13["30"],
    u13["59"],
    u14["10"],
    u14["30"],
    u14["59"],
    u15["10"],
    u15["30"],
    u15["59"],
    u16["10"],
    u16["30"],
    u16["59"],
    u17["10"],
    u17["30"],
    u17["59"],
    u18["10"],
    u18["30"],
    u18["59"],
    u19["10"],
    u19["30"],
    u19["59"],
    u21["7"],
    u21["8"],
    u22["12"],
    u22["22"],
    u22["24"],
    u22["25"],
    u22["26"],
    u22["37"],
    u22["51"],
    u22["63"],
    u22["75"],
    u22["89"],
    u22["100"],
    u23["3"],
    u23["15"],
    u23["28"],
    u23["40"],
    u23["54"],
    u23["66"],
    u23["78"],
    u23["92"],
    u24["20"],
    u24["38"],
    u24["40"],
    u24["41"],
    u24["42"],
    u24["60"],
    u24["81"],
    u24["100"],
    u24["120"],
    u24["142"],
    u24["160"],
)
connect(pcrd, rr3["7"], u11["72"], u23["46"], u24["133"])
connect(pcwr, rr3["5"], u11["74"], u23["47"], u24["132"])
connect(acces_ram, u3["19"], u4["19"], u5["19"], u6["19"], u22["21"], u24["56"])
connect(acq_on, u22["13"], u24["48"])
connect(adr2, u11["68"], u23["48"], u24["137"])
connect(adr3, u11["67"], u23["44"], u24["138"])
connect(adr4, u11["66"], u23["43"], u24["139"])
connect(adr5, u11["64"], u23["42"], u24["140"])
connect(adr6, u11["132"], u23["39"], u24["143"])
connect(be_0, u11["87"], u23["38"], u24["144"])
connect(be_1, u11["63"], u23["37"], u24["145"])
connect(be_2, u11["62"], u23["36"], u24["146"])
connect(be_3, u11["60"], u23["35"], u24["147"])
connect(blank, u9["7"], u22["8"], u24["53"])
connect(blue_in, p3["1"], r22["1"], r46["1"])
connect(blue_out, c60["2"], j4["3"], r44["2"], u9["39"])
connect(bpclk, u11["140"], u23["30"])
connect(bt812_rd, u10["86"], u23["71"])
connect(bt812_wr, u10["83"], u23["70"])
connect(
    cas0,
    u12["40"],
    u13["40"],
    u14["40"],
    u15["40"],
    u16["40"],
    u17["40"],
    u18["40"],
    u19["40"],
    u24["57"],
)
connect(
    cas1,
    u12["41"],
    u13["41"],
    u14["41"],
    u15["41"],
    u16["41"],
    u17["41"],
    u18["41"],
    u19["41"],
    u24["58"],
)
connect(
    cas2,
    u12["42"],
    u13["42"],
    u14["42"],
    u15["42"],
    u16["42"],
    u17["42"],
    u18["42"],
    u19["42"],
    u24["59"],
)
connect(
    cas3,
    u12["43"],
    u13["43"],
    u14["43"],
    u15["43"],
    u16["43"],
    u17["43"],
    u18["43"],
    u19["43"],
    u24["62"],
)
connect(clamp, u8["37"], u8["59"], u22["7"], u24["75"])
connect(clkcad, u8["38"], u8["39"], u8["40"], u22["2"], u24["77"])
connect(clkcda, u9["9"], u22["79"], u24["76"])
connect(csync_out, r30["2"], u9["8"], u22["9"], u24["13"])
connect(csyncin, u8["8"], u24["54"])
connect(c_out, j4["8"], r39["1"])
connect(dq0, rr7["2"], u3["2"], u8["16"], u9["14"], u10["92"], u11["100"], u23["13"], u24["21"])
connect(dq1, rr7["3"], u3["3"], u8["15"], u9["15"], u10["93"], u11["99"], u23["12"], u24["22"])
connect(dq10, rr8["7"], u4["4"], u11["83"], u23["95"], u24["34"])
connect(dq11, rr8["6"], u4["5"], u11["82"], u23["94"], u24["35"])
connect(dq12, rr8["5"], u4["6"], u11["80"], u23["93"], u24["36"])
connect(dq13, rr8["4"], u4["7"], u11["79"], u23["90"], u24["45"])
connect(dq14, rr8["3"], u4["8"], u11["78"], u23["88"], u24["46"])
connect(dq15, rr8["2"], u4["9"], u11["76"], u23["89"], u24["47"])
connect(dq16, rr4["7"], u5["2"], u11["157"])
connect(dq17, rr4["9"], u5["3"], u11["145"])
connect(dq18, rr6["6"], u5["4"], u11["133"])
connect(dq19, rr6["8"], u5["5"], u11["125"])
connect(dq2, rr7["4"], u3["4"], u8["14"], u9["16"], u10["94"], u11["98"], u23["11"], u24["23"])
connect(dq20, rr6["3"], u5["6"], u11["117"])
connect(dq21, rr5["6"], u5["7"], u11["105"])
connect(dq22, rr4["3"], u5["8"], u11["93"])
connect(dq23, rr4["5"], u5["9"], u11["85"])
connect(dq24, rr3["3"], u6["2"], u11["77"])
connect(dq25, rr3["9"], u6["3"], u11["65"])
connect(dq26, rr2["8"], u6["4"], u11["53"])
connect(dq27, rr2["5"], u6["5"], u11["45"])
connect(dq28, rr2["3"], u6["6"], u11["37"])
connect(dq29, rr1["8"], u6["7"], u11["25"])
connect(dq3, rr7["5"], u3["5"], u8["13"], u9["17"], u10["95"], u11["96"], u23["7"], u24["24"])
connect(dq30, rr1["5"], u6["8"], u11["13"])
connect(dq31, rr1["3"], u6["9"], u11["5"])
connect(dq4, rr7["6"], u3["6"], u8["12"], u9["18"], u10["96"], u11["95"], u23["9"], u24["25"])
connect(dq5, rr7["7"], u3["7"], u8["11"], u9["19"], u10["97"], u11["94"], u23["8"], u24["26"])
connect(dq6, rr7["8"], u3["8"], u8["10"], u9["20"], u10["99"], u11["92"], u23["6"], u24["27"])
connect(dq7, rr7["9"], u3["9"], u8["9"], u9["21"], u10["100"], u11["88"], u23["5"], u24["28"])
connect(dq8, rr8["9"], u4["2"], u11["86"], u23["97"], u24["32"])
connect(dq9, rr8["8"], u4["3"], u11["84"], u23["96"], u24["33"])
connect(esvideo_rvb_oe_rvb, u8["57"], u9["29"])
connect(
    esvideo_rvb_ref,
    r37["2"],
    u8["64"],
    u8["65"],
    u8["66"],
    u8["71"],
    u8["73"],
    u8["76"],
    u8["78"],
    u8["80"],
    u8["82"],
)
connect(
    esvideo_rvb_vaa,
    c33["1"],
    c34["1"],
    c35["1"],
    c42["1"],
    c51["1"],
    c52["1"],
    l5["2"],
    u8["1"],
    u8["43"],
    u8["44"],
    u8["84"],
    u9["1"],
    u9["2"],
    u9["33"],
    u9["34"],
    u9["35"],
    u9["36"],
)
connect(f_palin, u10["104"], u24["43"])
connect(green_in, c3["2"], p2["1"], r23["1"], r45["1"])
connect(green_out, c59["2"], j4["2"], r43["2"], u9["38"])
connect(hd_pal, u10["36"], u24["52"])
connect(irq, u11["124"], u24["149"])
connect(irq_srl, rr2["7"], u11["57"], u24["134"])
connect(
    mxa0,
    u12["12"],
    u13["12"],
    u14["12"],
    u15["12"],
    u16["12"],
    u17["12"],
    u18["12"],
    u19["12"],
    u24["128"],
)
connect(
    mxa1,
    u12["13"],
    u13["13"],
    u14["13"],
    u15["13"],
    u16["13"],
    u17["13"],
    u18["13"],
    u19["13"],
    u24["127"],
)
connect(
    mxa10,
    u12["19"],
    u13["19"],
    u14["19"],
    u15["19"],
    u16["19"],
    u17["19"],
    u18["19"],
    u19["19"],
    u24["109"],
)
connect(
    mxa2,
    u12["14"],
    u13["14"],
    u14["14"],
    u15["14"],
    u16["14"],
    u17["14"],
    u18["14"],
    u19["14"],
    u24["126"],
)
connect(
    mxa3,
    u12["15"],
    u13["15"],
    u14["15"],
    u15["15"],
    u16["15"],
    u17["15"],
    u18["15"],
    u19["15"],
    u24["125"],
)
connect(
    mxa4,
    u12["16"],
    u13["16"],
    u14["16"],
    u15["16"],
    u16["16"],
    u17["16"],
    u18["16"],
    u19["16"],
    u24["124"],
)
connect(
    mxa5,
    u12["17"],
    u13["17"],
    u14["17"],
    u15["17"],
    u16["17"],
    u17["17"],
    u18["17"],
    u19["17"],
    u24["123"],
)
connect(
    mxa6,
    u12["18"],
    u13["18"],
    u14["18"],
    u15["18"],
    u16["18"],
    u17["18"],
    u18["18"],
    u19["18"],
    u24["116"],
)
connect(
    mxa7,
    u12["28"],
    u13["28"],
    u14["28"],
    u15["28"],
    u16["28"],
    u17["28"],
    u18["28"],
    u19["28"],
    u24["115"],
)
connect(
    mxa8,
    u12["31"],
    u13["31"],
    u14["31"],
    u15["31"],
    u16["31"],
    u17["31"],
    u18["31"],
    u19["31"],
    u24["114"],
)
connect(
    mxa9,
    u12["32"],
    u13["32"],
    u14["32"],
    u15["32"],
    u16["32"],
    u17["32"],
    u18["32"],
    u19["32"],
    u24["113"],
)
connect(oe_pal, u9["28"], u10["46"], u10["47"])
connect(pca0, u8["17"], u9["24"], u10["84"], u23["65"])
connect(pca1, u8["18"], u9["25"], u10["85"], u23["64"])
connect(pca2, u8["19"], u9["26"], u23["63"])
connect(ptadr, rr5["5"], u11["107"], u23["24"], u24["14"])
connect(ptatn, rr5["2"], u11["114"], u23["18"], u24["4"])
connect(ptbe_0, u11["116"], u23["20"], u24["158"])
connect(ptbe_1, u11["118"], u23["21"], u24["157"])
connect(ptbe_2, u11["119"], u23["22"], u24["156"])
connect(ptbe_3, u11["120"], u23["23"], u24["155"])
connect(ptburst, u11["112"], u23["17"], u24["5"])
connect(ptnum0, u11["123"], u23["34"], u24["150"])
connect(ptnum1, u11["122"], u23["32"], u24["154"])
connect(ptrdy, rr6["2"], u11["115"], u23["19"], u24["3"])
connect(ptwr, u11["108"], u23["16"], u24["12"])
connect(ras0, u19["34"], u19["44"], u24["74"])
connect(ras1, u18["34"], u18["44"], u24["73"])
connect(ras2, u17["34"], u17["44"], u24["69"])
connect(ras3, u15["34"], u15["44"], u24["68"])
connect(ras4, u16["34"], u16["44"], u24["67"])
connect(ras5, u12["34"], u12["44"], u24["66"])
connect(ras6, u14["34"], u14["44"], u24["65"])
connect(ras7, u13["34"], u13["44"], u24["64"])
connect(rdcad, u8["20"], u23["74"])
connect(rdcda, u9["22"], u23["72"])
connect(rdempty, u11["106"], u24["15"])
connect(rdfifo, rr5["7"], u11["104"], u24["16"])
connect(red_in, c4["2"], p1["1"], r24["1"], r47["1"])
connect(red_out, c58["2"], j4["1"], r42["2"], u9["37"])
connect(select, rr3["4"], u11["75"], u23["45"], u24["135"])
connect(sysrst, u10["87"], u11["126"], u23["1"], u24["148"])
connect(tvb0, u8["32"], u9["61"], u10["55"], u22["92"])
connect(tvb1, u8["31"], u9["62"], u10["54"], u22["93"])
connect(tvb2, u8["30"], u9["63"], u10["53"], u22["94"])
connect(tvb3, u8["29"], u9["64"], u10["52"], u22["95"])
connect(tvb4, u8["28"], u9["65"], u10["51"], u22["96"])
connect(tvb5, u8["27"], u9["66"], u10["50"], u22["97"])
connect(tvb6, u8["26"], u9["67"], u10["49"], u22["98"])
connect(tvb7, u8["25"], u9["68"], u10["48"], u22["99"])
connect(tvg0, u8["48"], u9["53"], u10["74"], u22["67"])
connect(tvg1, u8["47"], u9["54"], u10["73"], u22["68"])
connect(tvg2, u8["46"], u9["55"], u10["72"], u22["69"])
connect(tvg3, u8["45"], u9["56"], u10["71"], u22["70"])
connect(tvg4, u8["36"], u9["57"], u10["70"], u22["71"])
connect(tvg5, u8["35"], u9["58"], u10["69"], u22["78"])
connect(tvg6, u8["34"], u9["59"], u10["68"], u22["80"])
connect(tvg7, u8["33"], u9["60"], u10["67"], u22["81"])
connect(tvi0, u9["10"], u24["108"])
connect(tvi1, u9["11"], u24["107"])
connect(tvr0, u8["56"], u9["45"], u10["65"], u22["82"])
connect(tvr1, u8["55"], u9["46"], u10["64"], u22["83"])
connect(tvr2, u8["54"], u9["47"], u10["63"], u22["84"])
connect(tvr3, u8["53"], u9["48"], u10["62"], u22["85"])
connect(tvr4, u8["52"], u9["49"], u10["61"], u22["86"])
connect(tvr5, u8["51"], u9["50"], u10["60"], u22["87"])
connect(tvr6, u8["50"], u9["51"], u10["59"], u22["90"])
connect(tvr7, u8["49"], u9["52"], u10["58"], u22["91"])
connect(
    tvram0,
    u3["18"],
    u12["2"],
    u13["2"],
    u14["2"],
    u15["2"],
    u16["2"],
    u17["2"],
    u18["2"],
    u19["2"],
    u22["17"],
)
connect(
    tvram1,
    u3["17"],
    u12["4"],
    u13["4"],
    u14["4"],
    u15["4"],
    u16["4"],
    u17["4"],
    u18["4"],
    u19["4"],
    u22["19"],
)
connect(
    tvram10,
    u4["16"],
    u12["53"],
    u13["53"],
    u14["53"],
    u15["53"],
    u16["53"],
    u17["53"],
    u18["53"],
    u19["53"],
    u22["35"],
)
connect(
    tvram11,
    u4["15"],
    u12["55"],
    u13["55"],
    u14["55"],
    u15["55"],
    u16["55"],
    u17["55"],
    u18["55"],
    u19["55"],
    u22["36"],
)
connect(
    tvram12,
    u4["14"],
    u12["57"],
    u13["57"],
    u14["57"],
    u15["57"],
    u16["57"],
    u17["57"],
    u18["57"],
    u19["57"],
    u22["39"],
)
connect(
    tvram13,
    u4["13"],
    u12["61"],
    u13["61"],
    u14["61"],
    u15["61"],
    u16["61"],
    u17["61"],
    u18["61"],
    u19["61"],
    u22["40"],
)
connect(
    tvram14,
    u4["12"],
    u12["63"],
    u13["63"],
    u14["63"],
    u15["63"],
    u16["63"],
    u17["63"],
    u18["63"],
    u19["63"],
    u22["41"],
)
connect(
    tvram15,
    u4["11"],
    u12["65"],
    u13["65"],
    u14["65"],
    u15["65"],
    u16["65"],
    u17["65"],
    u18["65"],
    u19["65"],
    u22["42"],
)
connect(
    tvram16,
    u5["18"],
    u12["3"],
    u13["3"],
    u14["3"],
    u15["3"],
    u16["3"],
    u17["3"],
    u18["3"],
    u19["3"],
    u22["43"],
)
connect(
    tvram17,
    u5["17"],
    u12["5"],
    u13["5"],
    u14["5"],
    u15["5"],
    u16["5"],
    u17["5"],
    u18["5"],
    u19["5"],
    u22["44"],
)
connect(
    tvram18,
    u5["16"],
    u12["7"],
    u13["7"],
    u14["7"],
    u15["7"],
    u16["7"],
    u17["7"],
    u18["7"],
    u19["7"],
    u22["45"],
)
connect(
    tvram19,
    u5["15"],
    u12["9"],
    u13["9"],
    u14["9"],
    u15["9"],
    u16["9"],
    u17["9"],
    u18["9"],
    u19["9"],
    u22["46"],
)
connect(
    tvram2,
    u3["16"],
    u12["6"],
    u13["6"],
    u14["6"],
    u15["6"],
    u16["6"],
    u17["6"],
    u18["6"],
    u19["6"],
    u22["20"],
)
connect(
    tvram20,
    u5["14"],
    u12["21"],
    u13["21"],
    u14["21"],
    u15["21"],
    u16["21"],
    u17["21"],
    u18["21"],
    u19["21"],
    u22["47"],
)
connect(
    tvram21,
    u5["13"],
    u12["23"],
    u13["23"],
    u14["23"],
    u15["23"],
    u16["23"],
    u17["23"],
    u18["23"],
    u19["23"],
    u22["48"],
)
connect(
    tvram22,
    u5["12"],
    u12["25"],
    u13["25"],
    u14["25"],
    u15["25"],
    u16["25"],
    u17["25"],
    u18["25"],
    u19["25"],
    u22["53"],
)
connect(
    tvram23,
    u5["11"],
    u12["27"],
    u13["27"],
    u14["27"],
    u15["27"],
    u16["27"],
    u17["27"],
    u18["27"],
    u19["27"],
    u22["54"],
)
connect(
    tvram24,
    u6["18"],
    u12["50"],
    u13["50"],
    u14["50"],
    u15["50"],
    u16["50"],
    u17["50"],
    u18["50"],
    u19["50"],
    u22["55"],
)
connect(
    tvram25,
    u6["17"],
    u12["52"],
    u13["52"],
    u14["52"],
    u15["52"],
    u16["52"],
    u17["52"],
    u18["52"],
    u19["52"],
    u22["56"],
)
connect(
    tvram26,
    u6["16"],
    u12["54"],
    u13["54"],
    u14["54"],
    u15["54"],
    u16["54"],
    u17["54"],
    u18["54"],
    u19["54"],
    u22["57"],
)
connect(
    tvram27,
    u6["15"],
    u12["56"],
    u13["56"],
    u14["56"],
    u15["56"],
    u16["56"],
    u17["56"],
    u18["56"],
    u19["56"],
    u22["58"],
)
connect(
    tvram28,
    u6["14"],
    u12["58"],
    u13["58"],
    u14["58"],
    u15["58"],
    u16["58"],
    u17["58"],
    u18["58"],
    u19["58"],
    u22["59"],
)
connect(
    tvram29,
    u6["13"],
    u12["60"],
    u13["60"],
    u14["60"],
    u15["60"],
    u16["60"],
    u17["60"],
    u18["60"],
    u19["60"],
    u22["60"],
)
connect(
    tvram3,
    u3["15"],
    u12["8"],
    u13["8"],
    u14["8"],
    u15["8"],
    u16["8"],
    u17["8"],
    u18["8"],
    u19["8"],
    u22["18"],
)
connect(
    tvram30,
    u6["12"],
    u12["62"],
    u13["62"],
    u14["62"],
    u15["62"],
    u16["62"],
    u17["62"],
    u18["62"],
    u19["62"],
    u22["61"],
)
connect(
    tvram31,
    u6["11"],
    u12["64"],
    u13["64"],
    u14["64"],
    u15["64"],
    u16["64"],
    u17["64"],
    u18["64"],
    u19["64"],
    u22["62"],
)
connect(
    tvram4,
    u3["14"],
    u12["20"],
    u13["20"],
    u14["20"],
    u15["20"],
    u16["20"],
    u17["20"],
    u18["20"],
    u19["20"],
    u22["28"],
)
connect(
    tvram5,
    u3["13"],
    u12["22"],
    u13["22"],
    u14["22"],
    u15["22"],
    u16["22"],
    u17["22"],
    u18["22"],
    u19["22"],
    u22["29"],
)
connect(
    tvram6,
    u3["12"],
    u12["24"],
    u13["24"],
    u14["24"],
    u15["24"],
    u16["24"],
    u17["24"],
    u18["24"],
    u19["24"],
    u22["31"],
)
connect(
    tvram7,
    u3["11"],
    u12["26"],
    u13["26"],
    u14["26"],
    u15["26"],
    u16["26"],
    u17["26"],
    u18["26"],
    u19["26"],
    u22["32"],
)
connect(
    tvram8,
    u4["18"],
    u12["49"],
    u13["49"],
    u14["49"],
    u15["49"],
    u16["49"],
    u17["49"],
    u18["49"],
    u19["49"],
    u22["33"],
)
connect(
    tvram9,
    u4["17"],
    u12["51"],
    u13["51"],
    u14["51"],
    u15["51"],
    u16["51"],
    u17["51"],
    u18["51"],
    u19["51"],
    u22["34"],
)
connect(vd_pal, u10["34"], u24["37"])
connect(
    wram,
    u12["47"],
    u13["47"],
    u14["47"],
    u15["47"],
    u16["47"],
    u17["47"],
    u18["47"],
    u19["47"],
    u24["63"],
)
connect(wrcad, u8["24"], u23["69"])
connect(wrcda, u9["23"], u23["73"])
connect(wrfifdo, rr5["8"], u11["102"], u24["18"])
connect(wrfull, u11["103"], u24["17"])
connect(write_ram, u3["1"], u4["1"], u5["1"], u6["1"], u24["55"])
connect(x_clk, u22["74"], u23["86"], u24["119"])
connect(x_data, u22["72"], u24["118"])
connect(x_done, u22["50"], u23["83"], u24["80"])
connect(x_irq, rr5["4"], u11["109"], u24["11"])
connect(x_prog, u22["52"], u23["84"], u24["82"])
connect(y_out, j4["9"], r40["2"])
connect(buspci_sch_ea1, rr2["6"], u11["61"])
connect(buspci_sch_ea10, rr6["9"], u11["121"])
connect(buspci_sch_ea11, rr6["7"], u11["129"])
connect(buspci_sch_ea12, rr6["5"], u11["137"])
connect(buspci_sch_ea13, rr6["4"], u11["141"])
connect(buspci_sch_ea14, rr4["8"], u11["149"])
connect(buspci_sch_ea15, rr4["6"], u11["153"])
connect(buspci_sch_ea2, rr3["8"], u11["69"])
connect(buspci_sch_ea3, rr3["6"], u11["73"])
connect(buspci_sch_ea4, rr3["2"], u11["81"])
connect(buspci_sch_ea5, rr4["4"], u11["89"])
connect(buspci_sch_ea6, rr4["2"], u11["97"])
connect(buspci_sch_ea7, rr5["9"], u11["101"])
connect(buspci_sch_ea9, rr5["3"], u11["113"])
connect(buspci_sch_eq0, rr1["2"], u11["1"])
connect(buspci_sch_eq1, rr1["4"], u11["9"])
connect(buspci_sch_eq2, rr1["6"], u11["17"])
connect(buspci_sch_eq3, rr1["7"], u11["21"])
connect(buspci_sch_eq4, rr1["9"], u11["29"])
connect(buspci_sch_eq5, rr2["4"], u11["33"])
connect(buspci_sch_eq6, rr2["2"], u11["41"])
connect(buspci_sch_eq7, rr2["9"], u11["49"])
connect(buspci_sch_p_ad0, bus1["A58"], u11["56"])
connect(buspci_sch_p_ad1, bus1["B58"], u11["55"])
connect(buspci_sch_p_ad10, bus1["B48"], u11["39"])
connect(buspci_sch_p_ad11, bus1["A47"], u11["38"])
connect(buspci_sch_p_ad12, bus1["B47"], u11["36"])
connect(buspci_sch_p_ad13, bus1["A46"], u11["35"])
connect(buspci_sch_p_ad14, bus1["B45"], u11["34"])
connect(buspci_sch_p_ad15, bus1["A44"], u11["32"])
connect(buspci_sch_p_ad16, bus1["A32"], u11["14"])
connect(buspci_sch_p_ad17, bus1["B32"], u11["12"])
connect(buspci_sch_p_ad18, bus1["A31"], u11["8"])
connect(buspci_sch_p_ad19, bus1["B30"], u11["7"])
connect(buspci_sch_p_ad2, bus1["A57"], u11["54"])
connect(buspci_sch_p_ad20, bus1["A29"], u11["6"])
connect(buspci_sch_p_ad21, bus1["B29"], u11["4"])
connect(buspci_sch_p_ad22, bus1["A28"], u11["3"])
connect(buspci_sch_p_ad23, bus1["B27"], u11["2"])
connect(buspci_sch_p_ad24, bus1["A25"], u11["158"])
connect(buspci_sch_p_ad25, bus1["B24"], u11["156"])
connect(buspci_sch_p_ad26, bus1["A23"], u11["155"])
connect(buspci_sch_p_ad27, bus1["B23"], u11["154"])
connect(buspci_sch_p_ad28, bus1["A22"], u11["152"])
connect(buspci_sch_p_ad29, bus1["B21"], u11["148"])
connect(buspci_sch_p_ad3, bus1["B56"], u11["52"])
connect(buspci_sch_p_ad30, bus1["A20"], u11["147"])
connect(buspci_sch_p_ad31, bus1["B20"], u11["146"])
connect(buspci_sch_p_ad4, bus1["A55"], u11["48"])
connect(buspci_sch_p_ad5, bus1["B55"], u11["47"])
connect(buspci_sch_p_ad6, bus1["A54"], u11["46"])
connect(buspci_sch_p_ad7, bus1["B53"], u11["44"])
connect(buspci_sch_p_ad8, bus1["B52"], u11["42"])
connect(buspci_sch_p_ad9, bus1["A49"], u11["40"])
connect(buspci_sch_p_c_be0, bus1["A52"], u11["43"])
connect(buspci_sch_p_c_be1, bus1["B44"], u11["28"])
connect(buspci_sch_p_c_be2, bus1["B33"], u11["15"])
connect(buspci_sch_p_c_be3, bus1["B26"], u11["159"])
connect(buspci_sch_p_clk, bus1["B16"], u11["142"])
connect(buspci_sch_p_devsel, bus1["B37"], u11["20"])
connect(buspci_sch_p_frame, bus1["A34"], u11["16"])
connect(buspci_sch_p_gnt, bus1["A17"], u11["143"])
connect(buspci_sch_p_idsel, bus1["A26"], u11["160"])
connect(buspci_sch_p_inta, bus1["A6"], u11["58"])
connect(buspci_sch_p_irdy, bus1["B35"], u11["18"])
connect(buspci_sch_p_lock, bus1["B39"], u11["23"])
connect(buspci_sch_p_par, bus1["A43"], u11["27"])
connect(buspci_sch_p_perr, bus1["B40"], u11["24"])
connect(buspci_sch_p_req, bus1["B18"], u11["144"])
connect(buspci_sch_p_rst, bus1["A15"], u11["139"])
connect(buspci_sch_p_serr, bus1["B42"], u11["26"])
connect(buspci_sch_p_stop, bus1["A38"], u11["22"])
connect(buspci_sch_p_trdy, bus1["A36"], u11["19"])
connect(graphic_14mhzout, u7["6"], u24["95"])
connect(graphic_cclk, p5["2"], u21["2"], u23["77"])
connect(graphic_clk10mhz, r21["2"], u23["57"], u24["2"])
connect(graphic_csio, u23["61"], u24["159"])
connect(graphic_din, p5["3"], u21["1"], u23["75"])
connect(graphic_done, p5["4"], u23["53"])
connect(graphic_hdout, u7["1"], u24["7"])
connect(graphic_hdrefout, u7["2"], u24["6"])
connect(graphic_ia0, u2["6"], u24["94"])
connect(graphic_ia1, u2["7"], u24["92"])
connect(graphic_ia2, u2["8"], u24["88"])
connect(graphic_ia3, u2["9"], u24["87"])
connect(graphic_ia4, u2["11"], u24["86"])
connect(graphic_ia5, u2["12"], u24["85"])
connect(graphic_ia6, u2["13"], u24["83"])
connect(graphic_ia7, u2["14"], u24["78"])
connect(graphic_ia8, u2["15"], u24["93"])
connect(graphic_ia9, u2["5"], u24["96"])
connect(graphic_icas, u2["17"], u24["104"])
connect(graphic_id0, u2["1"], u24["102"])
connect(graphic_id1, u2["2"], u24["99"])
connect(graphic_id2, u2["18"], u24["105"])
connect(graphic_id3, u2["19"], u24["106"])
connect(graphic_ioe, u2["16"], u24["103"])
connect(graphic_iras, u2["4"], u24["97"])
connect(graphic_iwr, u2["3"], u24["98"])
connect(graphic_led, d6["2"], u23["81"])
connect(graphic_prog, p5["5"], u21["3"], u21["4"], u23["55"])
connect(graphic_reserv1, u23["59"], u24["44"])
connect(graphic_vosc, c23["1"], c63["1"], r1["1"], u7["4"], u7["5"], u7["7"])
connect(graphic_xtal_i, c50["1"], r26["1"], u23["56"], x1["2"])
connect(graphic_x_din, u23["85"], u24["117"])
connect(modul_chrom, r16["2"], u20["14"])
connect(modul_cvbs, r18["2"], u20["16"])
connect(modul_cvbsout, p8["1"], r41["1"])
connect(modul_lum, r17["2"], u20["19"])
connect(pal_ntsc_sch_c_video, d3["2"], d4["1"], r2["1"], u10["125"])
connect(
    pal_ntsc_sch_vaf,
    c2["1"],
    c12["1"],
    c13["1"],
    c14["1"],
    c62["1"],
    l4["2"],
    r12["2"],
    u10["1"],
    u10["2"],
    u10["39"],
    u10["40"],
    u10["41"],
    u10["42"],
    u10["43"],
    u10["78"],
    u10["79"],
    u10["80"],
    u10["81"],
    u10["82"],
    u10["119"],
    u10["120"],
    u10["121"],
    u10["122"],
    u10["123"],
    u10["132"],
    u10["141"],
    u10["142"],
    u10["149"],
    u10["158"],
    u10["159"],
    u10["160"],
)
connect(pal_ntsc_sch_y_video, d1["2"], d2["1"], r3["1"], u10["156"])
connect(pal_ntsc_sch_y_sync, r20["2"], r35["2"], u10["6"])
connect(
    gnd,
    bus1["A18"],
    bus1["A24"],
    bus1["A30"],
    bus1["A35"],
    bus1["A37"],
    bus1["A42"],
    bus1["A48"],
    bus1["A56"],
    bus1["B3"],
    bus1["B15"],
    bus1["B17"],
    bus1["B22"],
    bus1["B28"],
    bus1["B34"],
    bus1["B38"],
    bus1["B46"],
    bus1["B49"],
    bus1["B57"],
    c2["2"],
    c6["2"],
    c7["2"],
    c9["2"],
    c10["2"],
    c11["2"],
    c12["2"],
    c13["2"],
    c14["2"],
    c15["2"],
    c16["2"],
    c17["2"],
    c18["2"],
    c19["2"],
    c20["2"],
    c21["2"],
    c22["2"],
    c23["2"],
    c24["2"],
    c25["2"],
    c26["2"],
    c27["2"],
    c28["2"],
    c29["2"],
    c30["2"],
    c31["2"],
    c32["1"],
    c33["2"],
    c37["1"],
    c38["2"],
    c43["2"],
    c44["2"],
    c45["2"],
    c46["2"],
    c47["2"],
    c48["1"],
    c49["2"],
    c50["2"],
    c51["2"],
    c52["2"],
    c53["2"],
    c54["2"],
    c55["2"],
    c56["2"],
    c57["2"],
    c62["2"],
    c63["2"],
    c64["2"],
    c65["1"],
    c66["1"],
    c67["2"],
    c68["2"],
    c69["2"],
    c70["2"],
    c71["2"],
    c72["2"],
    c73["2"],
    cv1["2"],
    d1["1"],
    d3["1"],
    j4["4"],
    j4["5"],
    j4["6"],
    j4["7"],
    l6["3"],
    p1["2"],
    p2["2"],
    p3["2"],
    p4["2"],
    p5["1"],
    p8["2"],
    p12["1"],
    pot1["1"],
    pot1["2"],
    r8["2"],
    r14["2"],
    r15["1"],
    r31["1"],
    r32["2"],
    r33["2"],
    r34["2"],
    r37["1"],
    r38["2"],
    r42["1"],
    r43["1"],
    r44["1"],
    r45["2"],
    r46["2"],
    r47["2"],
    u1["1"],
    u1["2"],
    u1["3"],
    u1["4"],
    u2["20"],
    u3["10"],
    u4["10"],
    u5["10"],
    u6["10"],
    u7["3"],
    u8["2"],
    u8["3"],
    u8["21"],
    u8["22"],
    u8["23"],
    u8["41"],
    u8["42"],
    u8["61"],
    u8["63"],
    u8["67"],
    u9["3"],
    u9["4"],
    u9["12"],
    u9["13"],
    u9["31"],
    u9["32"],
    u10["3"],
    u10["5"],
    u10["7"],
    u10["16"],
    u10["30"],
    u10["44"],
    u10["56"],
    u10["66"],
    u10["75"],
    u10["88"],
    u10["89"],
    u10["90"],
    u10["98"],
    u10["103"],
    u10["111"],
    u10["116"],
    u10["118"],
    u10["124"],
    u10["126"],
    u10["128"],
    u10["130"],
    u10["134"],
    u10["136"],
    u10["138"],
    u10["139"],
    u10["143"],
    u10["145"],
    u10["147"],
    u10["151"],
    u10["153"],
    u10["155"],
    u10["157"],
    u11["10"],
    u11["30"],
    u11["50"],
    u11["70"],
    u11["90"],
    u11["110"],
    u11["130"],
    u11["150"],
    u12["1"],
    u12["39"],
    u12["72"],
    u13["1"],
    u13["39"],
    u13["72"],
    u14["1"],
    u14["39"],
    u14["72"],
    u15["1"],
    u15["39"],
    u15["72"],
    u16["1"],
    u16["39"],
    u16["72"],
    u17["1"],
    u17["39"],
    u17["72"],
    u18["1"],
    u18["39"],
    u18["72"],
    u19["1"],
    u19["39"],
    u19["72"],
    u20["10"],
    u20["17"],
    u21["5"],
    u22["1"],
    u22["11"],
    u22["23"],
    u22["38"],
    u22["49"],
    u22["64"],
    u22["77"],
    u22["88"],
    u23["4"],
    u23["14"],
    u23["26"],
    u23["41"],
    u23["52"],
    u23["67"],
    u23["80"],
    u23["91"],
    u24["1"],
    u24["10"],
    u24["19"],
    u24["29"],
    u24["39"],
    u24["51"],
    u24["61"],
    u24["70"],
    u24["79"],
    u24["91"],
    u24["101"],
    u24["110"],
    u24["122"],
    u24["131"],
    u24["141"],
    u24["151"],
    w1["1"],
    w2["1"],
    w3["1"],
    w4["1"],
    w5["1"],
)
connect(net_bus1_prsnt1, bus1["B9"], w5["2"])
connect(net_bus1_prsnt2, bus1["B11"], w4["2"])
connect(net_bus1_tdi, bus1["A4"], bus1["B4"])
connect(net_c1_pad1, c1["1"], c47["1"], r35["1"])
connect(net_c3_pad1, c3["1"], r3["2"])
connect(net_c36_pad2, c36["2"], c37["2"], r36["1"])
connect(net_c39_pad2, c39["2"], r24["2"])
connect(net_c4_pad1, c4["1"], r2["2"])
connect(net_c40_pad2, c40["2"], r23["2"])
connect(net_c41_pad2, c41["2"], r22["2"])
connect(net_c46_pad1, c46["1"], c53["1"], l1["2"])
connect(net_c49_pad1, c49["1"], r21["1"], r26["2"], x1["1"])
connect(net_c5_pad2, c5["2"], r19["1"])
connect(net_c61_pad1, c61["1"], r30["1"], r31["2"])
connect(net_c8_pad2, c8["2"], r20["1"])
connect(net_cv1_pad1, cv1["1"], x3["1"])
connect(net_d6_a, d6["1"], r13["2"])
connect(net_l6_pad1, l6["1"], r10["1"])
connect(net_p4_p1, p4["1"], r48["2"], u23["25"], u23["27"], u23["29"])
connect(net_pot1_pad3, pot1["3"], r9["1"])
connect(net_q1_b, q1["2"], r16["1"])
connect(net_q1_e, q1["1"], r32["1"], r39["2"])
connect(net_q2_b, q2["2"], r17["1"])
connect(net_q2_e, q2["1"], r33["1"], r40["1"])
connect(net_q3_b, q3["2"], r18["1"])
connect(net_q3_e, q3["1"], r34["1"], r41["2"])
connect(net_u1_scl, r28["2"], u1["6"], u11["128"])
connect(net_u1_sda, r29["2"], u1["5"], u11["127"])
connect(net_u10_clevel, c7["1"], r27["2"], u10["114"])
connect(net_u10_cref, c6["1"], r12["1"], u10["113"], u10["137"], u10["144"])
connect(net_u10_n_c, c16["1"], u10["110"])
connect(net_u10_out_c, r19["2"], u10["115"])
connect(net_u10_r_2, r27["1"], u10["135"])
connect(net_u10_sync_det, c1["2"], r14["1"], u10["140"])
connect(net_u10_vin_c, c5["1"], u10["117"])
connect(net_u10_vin_y_comp, c8["1"], u10["4"])
connect(net_u10_xtal1_in, c66["2"], r25["1"], u10["108"], x2["2"])
connect(net_u10_xtal1_out, c65["2"], r25["2"], u10["109"], x2["1"])
connect(net_u11_flt, r6["1"], u11["138"], w2["2"])
connect(net_u11_mode_16_32, r5["1"], u11["59"], w1["2"])
connect(net_u11_snv, r7["1"], u11["135"], w3["2"])
connect(net_u20_b, c58["1"], u20["11"])
connect(net_u20_b_adj, r9["2"], u20["21"])
connect(net_u20_cs, c61["2"], u20["24"])
connect(net_u20_flt, c45["1"], u20["15"])
connect(net_u20_g, c59["1"], u20["9"])
connect(net_u20_mctr, r4["1"], u20["2"])
connect(net_u20_notch, l1["1"], u20["18"])
connect(net_u20_osc, u20["23"], x3["2"])
connect(net_u20_r, c60["1"], u20["7"])
connect(net_u20_uoff, c44["1"], u20["6"])
connect(net_u20_vcc, c54["1"], l2["2"], u20["8"])
connect(net_u20_voff, c43["1"], u20["12"])
connect(net_u20_vref, c48["2"], c64["1"], r11["2"], u20["13"])
connect(net_u20_y_sin, l6["2"], r11["1"], u20["20"])
connect(net_u20_y_sout, r10["2"], u20["22"])
connect(net_u23_p87, p10["1"], u23["87"])
connect(net_u23_pgck4, p11["1"], u23["82"])
connect(net_u23_sgck3, p9["1"], u23["51"])
connect(net_u8_bin, u8["58"], u8["68"])
connect(net_u8_bvid0, c41["1"], u8["75"])
connect(net_u8_cext1, r36["2"], u8["6"])
connect(net_u8_cext2, c36["1"], r15["2"], u8["7"])
connect(net_u8_gin, u8["60"], u8["70"])
connect(net_u8_gvid0, c40["1"], u8["79"])
connect(net_u8_rin, u8["62"], u8["72"])
connect(net_u8_rset, r38["1"], u8["69"])
connect(net_u8_rvid0, c39["1"], u8["83"])
connect(net_u9_comp, c35["2"], u9["41"], u9["42"])
connect(net_u9_iref, c34["2"], c42["2"], r8["1"], u9["40"])
connect(net_u9_vref, c32["2"], u9["43"], u9["44"])

bus1.place(mm("58.115"), mm("58.75"), locked=True)
c24.place(mm("38.049"), mm("16.84"), side="bottom")
c25.place(mm("46.431"), mm("14.935"), rot=180, side="bottom")
c26.place(mm("50.622"), mm("22.936"), rot=180, side="bottom")
c27.place(mm("32.334"), mm("23.19"), side="bottom")
c28.place(mm("50.241"), mm("35.89"), rot=180, side="bottom")
c29.place(mm("47.066"), mm("39.7"), rot=180, side="bottom")
c30.place(mm("36.779"), mm("39.7"), side="bottom")
c31.place(mm("32.334"), mm("36.525"), side="bottom")
c38.place(mm("50.241"), mm("32.08"), rot=180, side="bottom")
c67.place(mm("-0.559"), mm("49.733"), rot=180, side="bottom")
c68.place(mm("17.983"), mm("48.463"), rot=180, side="bottom")
c69.place(mm("51.638"), mm("48.463"), side="bottom")
r5.place(mm("63.449"), mm("34.62"), side="bottom")
r6.place(mm("14.935"), mm("23.19"), rot=180, side="bottom")
r7.place(mm("18.745"), mm("20.65"), rot=180, side="bottom")
r28.place(mm("11.76"), mm("14.935"))
r29.place(mm("14.3"), mm("11.76"))
rr1.place(mm("88.595"), mm("42.621"), rot=180)
rr2.place(mm("88.595"), mm("37.795"), rot=180)
rr3.place(mm("88.595"), mm("34.112"), rot=180)
rr4.place(mm("-14.91"), mm("42.875"))
rr5.place(mm("-14.91"), mm("35.89"))
rr6.place(mm("-15.2"), mm("27"))
rr7.place(mm("-7.925"), mm("20.015"), rot=90)
rr8.place(mm("-11.227"), mm("-20.625"), rot=-90)
u1.place(mm("8.585"), mm("25.73"), rot=90)
u11.place(mm("41.605"), mm("29.44"), rot=90)
w1.place(mm("62.687"), mm("32.08"), rot=180, side="bottom")
w2.place(mm("19.4"), mm("25.2"), rot=-90)
w3.place(mm("22.3"), mm("25.2"), rot=-90)
w4.place(mm("9.22"), mm("42.875"))
w5.place(mm("-11.1"), mm("47.955"), rot=90)
c32.place(mm("257.759"), mm("27.635"), rot=180, side="bottom")
c33.place(mm("245.313"), mm("11.76"), side="bottom")
c34.place(mm("243.789"), mm("17.602"), side="bottom")
c35.place(mm("253.949"), mm("31.699"), side="bottom")
c36.place(mm("213.944"), mm("20.015"), rot=-90, side="bottom")
c37.place(mm("218.9"), mm("20.015"), rot=-90, side="bottom")
c39.place(mm("233.248"), mm("31.699"))
c40.place(mm("207.086"), mm("31.699"))
c41.place(mm("200.355"), mm("31.572"), rot=180)
c42.place(mm("243.916"), mm("20.396"), side="bottom")
c51.place(mm("245.44"), mm("8.585"), side="bottom")
c52.place(mm("210.261"), mm("17.729"), side="bottom")
l5.place(mm("226.009"), mm("31.572"), rot=180)
r8.place(mm("248.234"), mm("31.699"), rot=180)
r15.place(mm("221.437"), mm("20.015"), rot=-90, side="bottom")
r22.place(mm("194.767"), mm("31.572"))
r23.place(mm("213.69"), mm("32.08"), rot=180)
r24.place(mm("239.598"), mm("31.318"), rot=180)
r36.place(mm("216.357"), mm("20.015"), rot=90, side="bottom")
r37.place(mm("209.372"), mm("21.285"), rot=180, side="bottom")
r38.place(mm("204.165"), mm("17.729"), side="bottom")
r42.place(mm("-24.943"), mm("45.923"), rot=180, side="bottom")
r43.place(mm("-24.943"), mm("42.875"), rot=180, side="bottom")
r44.place(mm("-24.943"), mm("39.827"), rot=180, side="bottom")
r45.place(mm("-32.055"), mm("16.205"))
r46.place(mm("-33.452"), mm("7.696"), rot=-90, side="bottom")
r47.place(mm("-32.055"), mm("14.046"), side="bottom")
u8.place(mm("211.277"), mm("12.649"), rot=90)
u9.place(mm("243.535"), mm("14.935"), rot=-90)
c17.place(mm("55.194"), mm("-14.656"), rot=90, side="bottom")
c18.place(mm("57.48"), mm("-25.705"), rot=-90, side="bottom")
c19.place(mm("40.97"), mm("-26.34"), rot=180, side="bottom")
c20.place(mm("30.81"), mm("-26.975"), side="bottom")
c21.place(mm("24.714"), mm("-9.195"), side="bottom")
c22.place(mm("27"), mm("4.14"), side="bottom")
c23.place(mm("30.175"), mm("-38.405"), side="bottom")
c49.place(mm("16.459"), mm("-35.357"), rot=180)
c50.place(mm("7.569"), mm("-35.357"))
c56.place(mm("25.73"), mm("-14.91"), side="bottom")
c57.place(mm("48.59"), mm("-38.659"), side="bottom")
c63.place(mm("23.825"), mm("-39.907372"))
c70.place(mm("-2.464"), mm("-14.91"), rot=90, side="bottom")
c71.place(mm("6.426"), mm("-16.815"), rot=180, side="bottom")
c72.place(mm("10.236"), mm("-9.195"), rot=180, side="bottom")
c73.place(mm("-5.385"), mm("-5.385"), side="bottom")
d6.place(mm("-10.465"), mm("-24.435"))
p4.place(mm("5.664"), mm("-29.642"), rot=180)
p5.place(mm("-6.655"), mm("-38.405"), rot=90)
p9.place(mm("14.3"), mm("-25.07"))
p10.place(mm("-10.465"), mm("-40.945"))
p11.place(mm("-10.465"), mm("-36.5"))
p12.place(mm("-17.577"), mm("-42.088"))
r1.place(mm("23.825"), mm("-36.881"))
r13.place(mm("-14.104745"), mm("-24.458838"), side="bottom")
r21.place(mm("9.855"), mm("-32.436"), rot=180, side="bottom")
r26.place(mm("11.887"), mm("-37.897"), side="bottom")
r48.place(mm("8.331"), mm("-13.259"), side="bottom")
u2.place(mm("48.717"), mm("-36.754"), rot=90)
u7.place(mm("30.175"), mm("-38.405"), rot=90)
u21.place(mm("-5.385"), mm("-26.975"), rot=90)
u23.place(mm("3.505"), mm("-13.132"), rot=90)
u24.place(mm("41.605"), mm("-11.835"), rot=90)
x1.place(mm("14.427"), mm("-40.31"), rot=180)
c43.place(mm("-20.879"), mm("-11.989"), side="bottom")
c44.place(mm("-25.959"), mm("-14.656"), rot=90, side="bottom")
c45.place(mm("-20.879"), mm("-14.529"), side="bottom")
c46.place(mm("-19.609"), mm("14.935"), side="bottom")
c48.place(mm("-20.879"), mm("-17.069"), side="bottom")
c53.place(mm("-19.609"), mm("11.887"), side="bottom")
c54.place(mm("-21.387"), mm("-33.96"), rot=-90, side="bottom")
c55.place(mm("-24.054"), mm("0.457"), rot=-90, side="bottom")
c58.place(mm("-17.831"), mm("-7.29"))
c59.place(mm("-17.831"), mm("-3.353"), side="bottom")
c60.place(mm("-18.567997"), mm("0.609389"))
c61.place(mm("-31.293"), mm("2.235"), rot=180)
c64.place(mm("-15.799"), mm("-11.481"), rot=-90, side="bottom")
cv1.place(mm("-15.545"), mm("-30.785"), rot=180)
l1.place(mm("-19.863"), mm("7.061"))
l2.place(mm("-15.545"), mm("-38.024"), rot=180)
l3.place(mm("-29.134"), mm("6.934"))
l6.place(mm("-27.126232"), mm("9.506012"), rot=-90)
pot1.place(mm("-15.460043"), mm("-17.958"), rot=180)
q1.place(mm("-20.371"), mm("28.397"), side="bottom")
q2.place(mm("-24.943"), mm("28.397"), side="bottom")
q3.place(mm("-24.943"), mm("-5.385"), side="bottom")
r4.place(mm("-32.055"), mm("11.887"))
r9.place(mm("-32.055"), mm("-14.783"), rot=-90, side="bottom")
r10.place(mm("-29.261"), mm("-23.165"), rot=180)
r11.place(mm("-22.657"), mm("-23.165"))
r16.place(mm("-20.117"), mm("22.555"), rot=90, side="bottom")
r17.place(mm("-24.435"), mm("22.555"), rot=90, side="bottom")
r18.place(mm("-29.261"), mm("-14.783"), rot=-90, side="bottom")
r30.place(mm("-18.593"), mm("-0.559"), side="bottom")
r31.place(mm("-18.593"), mm("2.743"), rot=180, side="bottom")
r32.place(mm("-19.609"), mm("36.779"), side="bottom")
r33.place(mm("-19.609"), mm("33.731"), side="bottom")
r34.place(mm("-31.293"), mm("-1.067"), rot=180, side="bottom")
r39.place(mm("-24.943"), mm("36.779"), side="bottom")
r40.place(mm("-24.943"), mm("33.731"), rot=180, side="bottom")
r41.place(mm("-31.293"), mm("-4.369"), side="bottom")
u20.place(mm("-26.086"), mm("-14.91"), rot=90)
x3.place(mm("-24.435"), mm("-26.975"), rot=180)
u3.place(mm("68.783"), mm("6.553"), side="bottom")
u4.place(mm("68.783"), mm("-8.433"), side="bottom")
u5.place(mm("68.783"), mm("21.031"), side="bottom")
u6.place(mm("97.739"), mm("38.811"))
u22.place(mm("204.927"), mm("-25.578"), rot=-90)
c1.place(mm("258.521"), mm("-41.707"))
c2.place(mm("245.567"), mm("-32.563"), rot=90, side="bottom")
c3.place(mm("258.14"), mm("-26.213"), rot=-90)
c4.place(mm("255.981"), mm("-21.895"), side="bottom")
c5.place(mm("246.202"), mm("-2.718"), rot=-90, side="bottom")
c6.place(mm("245.567"), mm("-26.721"), rot=90, side="bottom")
c7.place(mm("238.201"), mm("-12.243"), rot=180, side="bottom")
c8.place(mm("249.123"), mm("-41.961"), rot=180, side="bottom")
c9.place(mm("233.883"), mm("-35.103"), side="bottom")
c10.place(mm("244.297"), mm("-12.243"), side="bottom")
c11.place(mm("219.278"), mm("-30.023"), rot=90, side="bottom")
c12.place(mm("245.567"), mm("-19.609"), rot=90, side="bottom")
c13.place(mm("226.009"), mm("-35.357"), side="bottom")
c14.place(mm("224.231"), mm("-18.085"), rot=90, side="bottom")
c15.place(mm("225.755"), mm("-12.751"), side="bottom")
c16.place(mm("238.201"), mm("-15.291"), rot=180, side="bottom")
c47.place(mm("258.521"), mm("-39.167"))
c62.place(mm("256.235"), mm("-33.833"), side="bottom")
c65.place(mm("251.409"), mm("-6.909"), side="bottom")
c66.place(mm("251.409"), mm("-4.115"), side="bottom")
d1.place(mm("210.300142"), mm("-38.960639"))
d2.place(mm("211.023"), mm("-41.199"))
d3.place(mm("253.949"), mm("-15.545"))
d4.place(mm("253.949"), mm("-13.280835"))
l4.place(mm("245.313"), mm("-2.845"))
r2.place(mm("255.981"), mm("-18.847"), side="bottom")
r3.place(mm("258.14"), mm("-27.737"), rot=-90, side="bottom")
r12.place(mm("255.727"), mm("-27.737"), rot=90, side="bottom")
r14.place(mm("258.521"), mm("-36.373"), rot=180)
r19.place(mm("243.408"), mm("-2.718"), rot=90, side="bottom")
r20.place(mm("243.027"), mm("-41.961"), side="bottom")
r25.place(mm("255.346"), mm("-5.385"), rot=90, side="bottom")
r27.place(mm("244.297"), mm("-15.291"), side="bottom")
r35.place(mm("253.5"), mm("-40.7075"), rot=90)
u10.place(mm("235.407"), mm("-23.673"), rot=-90)
x2.place(mm("257.632"), mm("-8.052"), rot=-90)
j4.place(mm("-29.261"), mm("44.145"), rot=-90, locked=True)
p1.place(mm("-40.945"), mm("4.775"), rot=180, locked=True)
p2.place(mm("-40.945"), mm("16.205"), rot=180, locked=True)
p3.place(mm("-40.945"), mm("-6.655"), rot=180, locked=True)
p8.place(mm("-40.945"), mm("-18.085"), rot=180, locked=True)
u12.place(mm("134.315"), mm("8.585"))
u13.place(mm("134.315"), mm("26.365"))
u14.place(mm("134.315"), mm("17.475"))
u15.place(mm("134.315"), mm("-9.195"))
u16.place(mm("134.315"), mm("-0.305"))
u17.place(mm("134.315"), mm("-18.085"))
u18.place(mm("134.315"), mm("-26.975"))
u19.place(mm("134.315"), mm("-35.865"))

design.zone(
    net_5v,
    layers=("In2.Cu",),
    key="+5V/1",
    outline=(
        (mm("85.674"), mm("54.305")),
        (mm("94.818"), mm("45.542")),
        (mm("104.851"), mm("45.542")),
        (mm("104.851"), mm("34.493")),
        (mm("264.236"), mm("34.366")),
        (mm("264.236"), mm("-43.485")),
        (mm("-8.687"), mm("-43.485")),
        (mm("-8.687"), mm("-26.594")),
        (mm("-18.79874"), mm("-26.594")),
        (mm("-20.244"), mm("-25.1589")),
        (mm("-20.244"), mm("-23.927")),
        (mm("-46.30694"), mm("-23.927")),
        (mm("-46.406"), mm("53.797")),
    ),
    clearance=mm("0.4"),
    thermal_gap=mm("0.4"),
    thermal_spoke_width=mm("0.3"),
)
design.zone(
    gnd,
    layers=("In1.Cu",),
    key="GND/1",
    outline=(
        (mm("-45"), mm("-42.8")),
        (mm("265"), mm("-43.1")),
        (mm("265"), mm("34")),
        (mm("104.5"), mm("34")),
        (mm("104.5"), mm("45")),
        (mm("95"), mm("45")),
        (mm("85.5"), mm("54.5")),
        (mm("-5"), mm("55")),
        (mm("-5"), mm("54.5")),
        (mm("-45"), mm("54")),
    ),
    clearance=mm("0.4"),
    thermal_gap=mm("0.4"),
    thermal_spoke_width=mm("0.3"),
)

design.line(
    "Dwgs.User/line/1",
    (mm("-41.453"), mm("-26.975")),
    (mm("-36.373"), mm("-26.975")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/2",
    (mm("-41.453"), mm("58.369")),
    (mm("-36.373"), mm("58.369")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/3",
    (mm("-41.326"), mm("-23.038")),
    (mm("-41.326"), mm("54.432")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/4",
    (mm("-38.913"), mm("60.909")),
    (mm("-38.913"), mm("-29.515")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/5",
    (mm("-33.706"), mm("-43.485")),
    (mm("-33.706"), mm("-23.038")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/6",
    (mm("-33.706"), mm("-23.038")),
    (mm("-46.406"), mm("-23.038")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/7",
    (mm("-33.706"), mm("54.432")),
    (mm("-46.406"), mm("54.432")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/8",
    (mm("-33.706"), mm("54.432")),
    (mm("-33.706"), mm("63.195")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/9",
    (mm("92.659"), mm("54.94")),
    (mm("124.028"), mm("54.94")),
    layer="Dwgs.User",
    width=mm("0.2"),
)
design.line(
    "Dwgs.User/line/10",
    (mm("255.473"), mm("-33.325")),
    (mm("255.473"), mm("-43.485")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/11",
    (mm("255.473"), mm("-33.325")),
    (mm("260.553"), mm("-33.325")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/12",
    (mm("258.013"), mm("-38.405")),
    (mm("263.093"), mm("-38.405")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/13",
    (mm("260.553"), mm("-40.945")),
    (mm("260.553"), mm("-35.865")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/14",
    (mm("260.553"), mm("-33.325")),
    (mm("260.553"), mm("34.366")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.text(
    "B.Cu/text/1",
    "TEXTE",
    (mm("-40.4624"), mm("50.9776")),
    layer="B.Cu",
    size=mm("1.524"),
    thickness=mm("0.2032"),
)
design.dimension(
    "Dwgs.User/dimension/1",
    (mm("73.609"), mm("54.94")),
    (mm("73.609"), mm("63.195")),
    offset=mm("-16.002"),
    size=mm("1.524"),
    thickness=mm("0.2"),
    width=mm("0.2"),
    extension_offset=mm("0"),
)
design.dimension(
    "Dwgs.User/dimension/2",
    (mm("124.028"), mm("34.366")),
    (mm("124.028"), mm("54.94")),
    offset=mm("-3.175"),
    size=mm("1.524"),
    thickness=mm("0.2"),
    width=mm("0.2"),
    extension_offset=mm("0"),
)

copper.apply(
    design,
    {
        "+3.3V": net_3_3v,
        "+5F": net_5f,
        "+5V": net_5v,
        "//PCRD": pcrd,
        "//PCWR": pcwr,
        "/ACCES_RAM-": acces_ram,
        "/ACQ_ON": acq_on,
        "/ADR2": adr2,
        "/ADR3": adr3,
        "/ADR4": adr4,
        "/ADR5": adr5,
        "/ADR6": adr6,
        "/BE-0": be_0,
        "/BE-1": be_1,
        "/BE-2": be_2,
        "/BE-3": be_3,
        "/BLANK-": blank,
        "/BLUE_IN": blue_in,
        "/BLUE_OUT": blue_out,
        "/BPCLK": bpclk,
        "/BT812_RD-": bt812_rd,
        "/BT812_WR-": bt812_wr,
        "/CAS0-": cas0,
        "/CAS1-": cas1,
        "/CAS2-": cas2,
        "/CAS3-": cas3,
        "/CLAMP": clamp,
        "/CLKCAD": clkcad,
        "/CLKCDA": clkcda,
        "/CSYNC-OUT": csync_out,
        "/CSYNCIN-": csyncin,
        "/C_OUT": c_out,
        "/DQ0": dq0,
        "/DQ1": dq1,
        "/DQ10": dq10,
        "/DQ11": dq11,
        "/DQ12": dq12,
        "/DQ13": dq13,
        "/DQ14": dq14,
        "/DQ15": dq15,
        "/DQ16": dq16,
        "/DQ17": dq17,
        "/DQ18": dq18,
        "/DQ19": dq19,
        "/DQ2": dq2,
        "/DQ20": dq20,
        "/DQ21": dq21,
        "/DQ22": dq22,
        "/DQ23": dq23,
        "/DQ24": dq24,
        "/DQ25": dq25,
        "/DQ26": dq26,
        "/DQ27": dq27,
        "/DQ28": dq28,
        "/DQ29": dq29,
        "/DQ3": dq3,
        "/DQ30": dq30,
        "/DQ31": dq31,
        "/DQ4": dq4,
        "/DQ5": dq5,
        "/DQ6": dq6,
        "/DQ7": dq7,
        "/DQ8": dq8,
        "/DQ9": dq9,
        "/ESVIDEO-RVB/OE_RVB-": esvideo_rvb_oe_rvb,
        "/ESVIDEO-RVB/REF+": esvideo_rvb_ref,
        "/ESVIDEO-RVB/VAA": esvideo_rvb_vaa,
        "/F_PALIN": f_palin,
        "/GREEN_IN": green_in,
        "/GREEN_OUT": green_out,
        "/HD_PAL-": hd_pal,
        "/IRQ-": irq,
        "/IRQ_SRL": irq_srl,
        "/MXA0": mxa0,
        "/MXA1": mxa1,
        "/MXA10": mxa10,
        "/MXA2": mxa2,
        "/MXA3": mxa3,
        "/MXA4": mxa4,
        "/MXA5": mxa5,
        "/MXA6": mxa6,
        "/MXA7": mxa7,
        "/MXA8": mxa8,
        "/MXA9": mxa9,
        "/OE_PAL-": oe_pal,
        "/PCA0": pca0,
        "/PCA1": pca1,
        "/PCA2": pca2,
        "/PTADR-": ptadr,
        "/PTATN-": ptatn,
        "/PTBE-0": ptbe_0,
        "/PTBE-1": ptbe_1,
        "/PTBE-2": ptbe_2,
        "/PTBE-3": ptbe_3,
        "/PTBURST": ptburst,
        "/PTNUM0": ptnum0,
        "/PTNUM1": ptnum1,
        "/PTRDY-": ptrdy,
        "/PTWR": ptwr,
        "/RAS0-": ras0,
        "/RAS1-": ras1,
        "/RAS2-": ras2,
        "/RAS3-": ras3,
        "/RAS4-": ras4,
        "/RAS5-": ras5,
        "/RAS6-": ras6,
        "/RAS7-": ras7,
        "/RDCAD-": rdcad,
        "/RDCDA-": rdcda,
        "/RDEMPTY": rdempty,
        "/RDFIFO-": rdfifo,
        "/RED_IN": red_in,
        "/RED_OUT": red_out,
        "/SELECT-": select,
        "/SYSRST-": sysrst,
        "/TVB0": tvb0,
        "/TVB1": tvb1,
        "/TVB2": tvb2,
        "/TVB3": tvb3,
        "/TVB4": tvb4,
        "/TVB5": tvb5,
        "/TVB6": tvb6,
        "/TVB7": tvb7,
        "/TVG0": tvg0,
        "/TVG1": tvg1,
        "/TVG2": tvg2,
        "/TVG3": tvg3,
        "/TVG4": tvg4,
        "/TVG5": tvg5,
        "/TVG6": tvg6,
        "/TVG7": tvg7,
        "/TVI0": tvi0,
        "/TVI1": tvi1,
        "/TVR0": tvr0,
        "/TVR1": tvr1,
        "/TVR2": tvr2,
        "/TVR3": tvr3,
        "/TVR4": tvr4,
        "/TVR5": tvr5,
        "/TVR6": tvr6,
        "/TVR7": tvr7,
        "/TVRAM0": tvram0,
        "/TVRAM1": tvram1,
        "/TVRAM10": tvram10,
        "/TVRAM11": tvram11,
        "/TVRAM12": tvram12,
        "/TVRAM13": tvram13,
        "/TVRAM14": tvram14,
        "/TVRAM15": tvram15,
        "/TVRAM16": tvram16,
        "/TVRAM17": tvram17,
        "/TVRAM18": tvram18,
        "/TVRAM19": tvram19,
        "/TVRAM2": tvram2,
        "/TVRAM20": tvram20,
        "/TVRAM21": tvram21,
        "/TVRAM22": tvram22,
        "/TVRAM23": tvram23,
        "/TVRAM24": tvram24,
        "/TVRAM25": tvram25,
        "/TVRAM26": tvram26,
        "/TVRAM27": tvram27,
        "/TVRAM28": tvram28,
        "/TVRAM29": tvram29,
        "/TVRAM3": tvram3,
        "/TVRAM30": tvram30,
        "/TVRAM31": tvram31,
        "/TVRAM4": tvram4,
        "/TVRAM5": tvram5,
        "/TVRAM6": tvram6,
        "/TVRAM7": tvram7,
        "/TVRAM8": tvram8,
        "/TVRAM9": tvram9,
        "/VD_PAL-": vd_pal,
        "/WRAM-": wram,
        "/WRCAD-": wrcad,
        "/WRCDA-": wrcda,
        "/WRFIFDO-": wrfifdo,
        "/WRFULL": wrfull,
        "/WRITE_RAM": write_ram,
        "/X_CLK": x_clk,
        "/X_DATA": x_data,
        "/X_DONE": x_done,
        "/X_IRQ": x_irq,
        "/X_PROG-": x_prog,
        "/Y_OUT": y_out,
        "/buspci.sch/EA1": buspci_sch_ea1,
        "/buspci.sch/EA10": buspci_sch_ea10,
        "/buspci.sch/EA11": buspci_sch_ea11,
        "/buspci.sch/EA12": buspci_sch_ea12,
        "/buspci.sch/EA13": buspci_sch_ea13,
        "/buspci.sch/EA14": buspci_sch_ea14,
        "/buspci.sch/EA15": buspci_sch_ea15,
        "/buspci.sch/EA2": buspci_sch_ea2,
        "/buspci.sch/EA3": buspci_sch_ea3,
        "/buspci.sch/EA4": buspci_sch_ea4,
        "/buspci.sch/EA5": buspci_sch_ea5,
        "/buspci.sch/EA6": buspci_sch_ea6,
        "/buspci.sch/EA7": buspci_sch_ea7,
        "/buspci.sch/EA9": buspci_sch_ea9,
        "/buspci.sch/EQ0": buspci_sch_eq0,
        "/buspci.sch/EQ1": buspci_sch_eq1,
        "/buspci.sch/EQ2": buspci_sch_eq2,
        "/buspci.sch/EQ3": buspci_sch_eq3,
        "/buspci.sch/EQ4": buspci_sch_eq4,
        "/buspci.sch/EQ5": buspci_sch_eq5,
        "/buspci.sch/EQ6": buspci_sch_eq6,
        "/buspci.sch/EQ7": buspci_sch_eq7,
        "/buspci.sch/P_AD0": buspci_sch_p_ad0,
        "/buspci.sch/P_AD1": buspci_sch_p_ad1,
        "/buspci.sch/P_AD10": buspci_sch_p_ad10,
        "/buspci.sch/P_AD11": buspci_sch_p_ad11,
        "/buspci.sch/P_AD12": buspci_sch_p_ad12,
        "/buspci.sch/P_AD13": buspci_sch_p_ad13,
        "/buspci.sch/P_AD14": buspci_sch_p_ad14,
        "/buspci.sch/P_AD15": buspci_sch_p_ad15,
        "/buspci.sch/P_AD16": buspci_sch_p_ad16,
        "/buspci.sch/P_AD17": buspci_sch_p_ad17,
        "/buspci.sch/P_AD18": buspci_sch_p_ad18,
        "/buspci.sch/P_AD19": buspci_sch_p_ad19,
        "/buspci.sch/P_AD2": buspci_sch_p_ad2,
        "/buspci.sch/P_AD20": buspci_sch_p_ad20,
        "/buspci.sch/P_AD21": buspci_sch_p_ad21,
        "/buspci.sch/P_AD22": buspci_sch_p_ad22,
        "/buspci.sch/P_AD23": buspci_sch_p_ad23,
        "/buspci.sch/P_AD24": buspci_sch_p_ad24,
        "/buspci.sch/P_AD25": buspci_sch_p_ad25,
        "/buspci.sch/P_AD26": buspci_sch_p_ad26,
        "/buspci.sch/P_AD27": buspci_sch_p_ad27,
        "/buspci.sch/P_AD28": buspci_sch_p_ad28,
        "/buspci.sch/P_AD29": buspci_sch_p_ad29,
        "/buspci.sch/P_AD3": buspci_sch_p_ad3,
        "/buspci.sch/P_AD30": buspci_sch_p_ad30,
        "/buspci.sch/P_AD31": buspci_sch_p_ad31,
        "/buspci.sch/P_AD4": buspci_sch_p_ad4,
        "/buspci.sch/P_AD5": buspci_sch_p_ad5,
        "/buspci.sch/P_AD6": buspci_sch_p_ad6,
        "/buspci.sch/P_AD7": buspci_sch_p_ad7,
        "/buspci.sch/P_AD8": buspci_sch_p_ad8,
        "/buspci.sch/P_AD9": buspci_sch_p_ad9,
        "/buspci.sch/P_C/BE0#": buspci_sch_p_c_be0,
        "/buspci.sch/P_C/BE1#": buspci_sch_p_c_be1,
        "/buspci.sch/P_C/BE2#": buspci_sch_p_c_be2,
        "/buspci.sch/P_C/BE3#": buspci_sch_p_c_be3,
        "/buspci.sch/P_CLK": buspci_sch_p_clk,
        "/buspci.sch/P_DEVSEL#": buspci_sch_p_devsel,
        "/buspci.sch/P_FRAME#": buspci_sch_p_frame,
        "/buspci.sch/P_GNT#": buspci_sch_p_gnt,
        "/buspci.sch/P_IDSEL": buspci_sch_p_idsel,
        "/buspci.sch/P_INTA#": buspci_sch_p_inta,
        "/buspci.sch/P_IRDY#": buspci_sch_p_irdy,
        "/buspci.sch/P_LOCK#": buspci_sch_p_lock,
        "/buspci.sch/P_PAR": buspci_sch_p_par,
        "/buspci.sch/P_PERR#": buspci_sch_p_perr,
        "/buspci.sch/P_REQ#": buspci_sch_p_req,
        "/buspci.sch/P_RST#": buspci_sch_p_rst,
        "/buspci.sch/P_SERR#": buspci_sch_p_serr,
        "/buspci.sch/P_STOP#": buspci_sch_p_stop,
        "/buspci.sch/P_TRDY#": buspci_sch_p_trdy,
        "/graphic/14MHZOUT": graphic_14mhzout,
        "/graphic/CCLK": graphic_cclk,
        "/graphic/CLK10MHz": graphic_clk10mhz,
        "/graphic/CSIO-": graphic_csio,
        "/graphic/DIN": graphic_din,
        "/graphic/DONE": graphic_done,
        "/graphic/HDOUT": graphic_hdout,
        "/graphic/HDREFOUT": graphic_hdrefout,
        "/graphic/IA0": graphic_ia0,
        "/graphic/IA1": graphic_ia1,
        "/graphic/IA2": graphic_ia2,
        "/graphic/IA3": graphic_ia3,
        "/graphic/IA4": graphic_ia4,
        "/graphic/IA5": graphic_ia5,
        "/graphic/IA6": graphic_ia6,
        "/graphic/IA7": graphic_ia7,
        "/graphic/IA8": graphic_ia8,
        "/graphic/IA9": graphic_ia9,
        "/graphic/ICAS-": graphic_icas,
        "/graphic/ID0": graphic_id0,
        "/graphic/ID1": graphic_id1,
        "/graphic/ID2": graphic_id2,
        "/graphic/ID3": graphic_id3,
        "/graphic/IOE-": graphic_ioe,
        "/graphic/IRAS-": graphic_iras,
        "/graphic/IWR-": graphic_iwr,
        "/graphic/LED": graphic_led,
        "/graphic/PROG*": graphic_prog,
        "/graphic/RESERV1": graphic_reserv1,
        "/graphic/VOSC": graphic_vosc,
        "/graphic/XTAL_I": graphic_xtal_i,
        "/graphic/X_DIN": graphic_x_din,
        "/modul/CHROM": modul_chrom,
        "/modul/CVBS": modul_cvbs,
        "/modul/CVBSOUT": modul_cvbsout,
        "/modul/LUM": modul_lum,
        "/pal-ntsc.sch/C-VIDEO": pal_ntsc_sch_c_video,
        "/pal-ntsc.sch/VAF": pal_ntsc_sch_vaf,
        "/pal-ntsc.sch/Y-VIDEO": pal_ntsc_sch_y_video,
        "/pal-ntsc.sch/Y_SYNC": pal_ntsc_sch_y_sync,
        "GND": gnd,
        "Net-(BUS1-PRSNT1#)": net_bus1_prsnt1,
        "Net-(BUS1-PRSNT2#)": net_bus1_prsnt2,
        "Net-(BUS1-TDI)": net_bus1_tdi,
        "Net-(C1-Pad1)": net_c1_pad1,
        "Net-(C3-Pad1)": net_c3_pad1,
        "Net-(C36-Pad2)": net_c36_pad2,
        "Net-(C39-Pad2)": net_c39_pad2,
        "Net-(C4-Pad1)": net_c4_pad1,
        "Net-(C40-Pad2)": net_c40_pad2,
        "Net-(C41-Pad2)": net_c41_pad2,
        "Net-(C46-Pad1)": net_c46_pad1,
        "Net-(C49-Pad1)": net_c49_pad1,
        "Net-(C5-Pad2)": net_c5_pad2,
        "Net-(C61-Pad1)": net_c61_pad1,
        "Net-(C8-Pad2)": net_c8_pad2,
        "Net-(CV1-Pad1)": net_cv1_pad1,
        "Net-(D6-A)": net_d6_a,
        "Net-(L6-Pad1)": net_l6_pad1,
        "Net-(P4-P1)": net_p4_p1,
        "Net-(POT1-Pad3)": net_pot1_pad3,
        "Net-(Q1-B)": net_q1_b,
        "Net-(Q1-E)": net_q1_e,
        "Net-(Q2-B)": net_q2_b,
        "Net-(Q2-E)": net_q2_e,
        "Net-(Q3-B)": net_q3_b,
        "Net-(Q3-E)": net_q3_e,
        "Net-(U1-SCL)": net_u1_scl,
        "Net-(U1-SDA)": net_u1_sda,
        "Net-(U10-CLEVEL)": net_u10_clevel,
        "Net-(U10-CREF+)": net_u10_cref,
        "Net-(U10-N/C)": net_u10_n_c,
        "Net-(U10-OUT_C)": net_u10_out_c,
        "Net-(U10-R/2)": net_u10_r_2,
        "Net-(U10-SYNC_DET)": net_u10_sync_det,
        "Net-(U10-VIN_C)": net_u10_vin_c,
        "Net-(U10-VIN_Y/COMP.)": net_u10_vin_y_comp,
        "Net-(U10-XTAL1_IN)": net_u10_xtal1_in,
        "Net-(U10-XTAL1_OUT)": net_u10_xtal1_out,
        "Net-(U11-FLT#)": net_u11_flt,
        "Net-(U11-MODE_16/32)": net_u11_mode_16_32,
        "Net-(U11-SNV)": net_u11_snv,
        "Net-(U20-B)": net_u20_b,
        "Net-(U20-B/ADJ)": net_u20_b_adj,
        "Net-(U20-CS)": net_u20_cs,
        "Net-(U20-FLT)": net_u20_flt,
        "Net-(U20-G)": net_u20_g,
        "Net-(U20-MCTR)": net_u20_mctr,
        "Net-(U20-NOTCH)": net_u20_notch,
        "Net-(U20-OSC)": net_u20_osc,
        "Net-(U20-R)": net_u20_r,
        "Net-(U20-UOFF)": net_u20_uoff,
        "Net-(U20-VCC)": net_u20_vcc,
        "Net-(U20-VOFF)": net_u20_voff,
        "Net-(U20-VREF)": net_u20_vref,
        "Net-(U20-Y+SIN)": net_u20_y_sin,
        "Net-(U20-Y+SOUT)": net_u20_y_sout,
        "Net-(U23-P87)": net_u23_p87,
        "Net-(U23-PGCK4)": net_u23_pgck4,
        "Net-(U23-SGCK3)": net_u23_sgck3,
        "Net-(U8-BIN)": net_u8_bin,
        "Net-(U8-BVID0)": net_u8_bvid0,
        "Net-(U8-CEXT1)": net_u8_cext1,
        "Net-(U8-CEXT2)": net_u8_cext2,
        "Net-(U8-GIN)": net_u8_gin,
        "Net-(U8-GVID0)": net_u8_gvid0,
        "Net-(U8-RIN)": net_u8_rin,
        "Net-(U8-RSET)": net_u8_rset,
        "Net-(U8-RVID0)": net_u8_rvid0,
        "Net-(U9-COMP)": net_u9_comp,
        "Net-(U9-IREF)": net_u9_iref,
        "Net-(U9-VREF)": net_u9_vref,
    },
)
