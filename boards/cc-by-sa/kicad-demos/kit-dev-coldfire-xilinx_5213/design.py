# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/kit-dev-coldfire-xilinx_5213@97acc80c223d75520c03fc44cab63cd9a3202c42 by Fenolite 0.7.0.dev0 on 2026-10-31;
# modified: format conversion to the Fenolite DSL.

import copper
from fenolite.dsl import Design, Module, Net, Part, connect, mm, stack

design = Design("kit-dev-coldfire-xilinx_5213")

design.board(
    outline=(
        (mm("-28.88"), mm("-44.12")),
        (mm("128.6"), mm("-44.12")),
        (mm("128.6"), mm("47.32")),
        (mm("-28.88"), mm("47.32")),
    ),
    copper=4,
)
design.stackup(
    stack.silkscreen(material="Liquid Photo", color="White"),
    stack.mask(mm("0.01"), material="Dry Film", epsilon_r="3.3", loss_tangent="0", color="Green"),
    stack.copper(mm("0.035")),
    stack.prepreg(mm("0.48"), material="FR4", epsilon_r="4.5", loss_tangent="0.02"),
    stack.copper(mm("0.035")),
    stack.core(mm("0.48"), material="FR4", epsilon_r="4.5", loss_tangent="0.02"),
    stack.copper(mm("0.035")),
    stack.prepreg(mm("0.48"), material="FR4", epsilon_r="4.5", loss_tangent="0.02"),
    stack.copper(mm("0.035")),
    stack.mask(mm("0.01"), material="Dry Film", epsilon_r="3.3", loss_tangent="0", color="Green"),
    stack.silkscreen(material="Liquid Photo", color="White"),
    finish="ENIG",
)
design.title_block(title="Demo Kicad", date="2015-10-09", revision="2")

net_3_3v = Net("+3.3V")
allpst = Net("/ALLPST")
an0 = Net("/AN0")
an1 = Net("/AN1")
an2 = Net("/AN2")
an3 = Net("/AN3")
an4 = Net("/AN4")
an5 = Net("/AN5")
an6 = Net("/AN6")
an7 = Net("/AN7")
bkpt = Net("/BKPT-")
canrx = Net("/CANRX")
cantx = Net("/CANTX")
clkin_extal = Net("/CLKIN/EXTAL")
clkmod0 = Net("/CLKMOD0")
clkmod1 = Net("/CLKMOD1")
ddat0 = Net("/DDAT0")
ddat1 = Net("/DDAT1")
ddat2 = Net("/DDAT2")
ddat3 = Net("/DDAT3")
dsclk = Net("/DSCLK")
dsi = Net("/DSI")
dso = Net("/DSO")
dspi_dout = Net("/DSPI_DOUT")
dtin0 = Net("/DTIN0")
dtin1 = Net("/DTIN1")
dtin2 = Net("/DTIN2")
dtin3 = Net("/DTIN3")
gpt0 = Net("/GPT0")
gpt1 = Net("/GPT1")
gpt2 = Net("/GPT2")
gpt3 = Net("/GPT3")
irq_1 = Net("/IRQ-1")
irq_2 = Net("/IRQ-2")
irq_3 = Net("/IRQ-3")
irq_4 = Net("/IRQ-4")
irq_5 = Net("/IRQ-5")
irq_6 = Net("/IRQ-6")
irq_7 = Net("/IRQ-7")
jtag_en = Net("/JTAG_EN")
pst0 = Net("/PST0")
pst1 = Net("/PST1")
pst2 = Net("/PST2")
pst3 = Net("/PST3")
pwm1 = Net("/PWM1")
pwm3 = Net("/PWM3")
pwm5 = Net("/PWM5")
pwm7 = Net("/PWM7")
qspi_clk = Net("/QSPI_CLK")
qspi_cs0 = Net("/QSPI_CS0")
qspi_cs1 = Net("/QSPI_CS1")
qspi_cs2 = Net("/QSPI_CS2")
qspi_cs3 = Net("/QSPI_CS3")
qspi_din = Net("/QSPI_DIN")
rcon = Net("/RCON-")
rsti = Net("/RSTI-")
rsto = Net("/RSTO-")
tclk = Net("/TCLK")
ucts0 = Net("/UCTS0")
ucts1 = Net("/UCTS1")
ucts2 = Net("/UCTS2")
urts0 = Net("/URTS0")
urts1 = Net("/URTS1")
urts2 = Net("/URTS2")
urxd0 = Net("/URXD0")
urxd1 = Net("/URXD1")
urxd2 = Net("/URXD2")
utxd0 = Net("/UTXD0")
utxd1 = Net("/UTXD1")
utxd2 = Net("/UTXD2")
vcca = Net("/VCCA")
vddpll = Net("/VDDPLL")
xtal = Net("/XTAL")
inout_user_can_h = Net("/inout_user/CAN_H")
inout_user_can_l = Net("/inout_user/CAN_L")
inout_user_cts0 = Net("/inout_user/CTS0")
inout_user_cts1 = Net("/inout_user/CTS1")
inout_user_cts2_canh = Net("/inout_user/CTS2/CANH")
inout_user_rts0 = Net("/inout_user/RTS0")
inout_user_rts1 = Net("/inout_user/RTS1")
inout_user_rts2 = Net("/inout_user/RTS2")
inout_user_rxd0 = Net("/inout_user/RXD0")
inout_user_rxd1 = Net("/inout_user/RXD1")
inout_user_rxd2 = Net("/inout_user/RXD2")
inout_user_rxd_can = Net("/inout_user/RxD_CAN")
inout_user_txd0 = Net("/inout_user/TXD0")
inout_user_txd1 = Net("/inout_user/TXD1")
inout_user_txd2_canl = Net("/inout_user/TXD2/CANL")
inout_user_txd_can = Net("/inout_user/TxD_CAN")
xilinx_3_3v_out = Net("/xilinx/+3,3V_OUT")
xilinx_led_test1 = Net("/xilinx/LED_TEST1")
xilinx_led_test2 = Net("/xilinx/LED_TEST2")
xilinx_tck = Net("/xilinx/TCK")
xilinx_tdi = Net("/xilinx/TDI")
xilinx_tdo = Net("/xilinx/TDO")
xilinx_tms = Net("/xilinx/TMS")
xilinx_xil_d0 = Net("/xilinx/XIL_D0")
xilinx_xil_d1 = Net("/xilinx/XIL_D1")
xilinx_xil_d10 = Net("/xilinx/XIL_D10")
xilinx_xil_d11 = Net("/xilinx/XIL_D11")
xilinx_xil_d12 = Net("/xilinx/XIL_D12")
xilinx_xil_d13 = Net("/xilinx/XIL_D13")
xilinx_xil_d14 = Net("/xilinx/XIL_D14")
xilinx_xil_d15 = Net("/xilinx/XIL_D15")
xilinx_xil_d16 = Net("/xilinx/XIL_D16")
xilinx_xil_d17 = Net("/xilinx/XIL_D17")
xilinx_xil_d18 = Net("/xilinx/XIL_D18")
xilinx_xil_d19 = Net("/xilinx/XIL_D19")
xilinx_xil_d2 = Net("/xilinx/XIL_D2")
xilinx_xil_d20 = Net("/xilinx/XIL_D20")
xilinx_xil_d21 = Net("/xilinx/XIL_D21")
xilinx_xil_d22 = Net("/xilinx/XIL_D22")
xilinx_xil_d23 = Net("/xilinx/XIL_D23")
xilinx_xil_d24 = Net("/xilinx/XIL_D24")
xilinx_xil_d25 = Net("/xilinx/XIL_D25")
xilinx_xil_d26 = Net("/xilinx/XIL_D26")
xilinx_xil_d27 = Net("/xilinx/XIL_D27")
xilinx_xil_d28 = Net("/xilinx/XIL_D28")
xilinx_xil_d29 = Net("/xilinx/XIL_D29")
xilinx_xil_d3 = Net("/xilinx/XIL_D3")
xilinx_xil_d30 = Net("/xilinx/XIL_D30")
xilinx_xil_d31 = Net("/xilinx/XIL_D31")
xilinx_xil_d32 = Net("/xilinx/XIL_D32")
xilinx_xil_d33 = Net("/xilinx/XIL_D33")
xilinx_xil_d34 = Net("/xilinx/XIL_D34")
xilinx_xil_d35 = Net("/xilinx/XIL_D35")
xilinx_xil_d36 = Net("/xilinx/XIL_D36")
xilinx_xil_d4 = Net("/xilinx/XIL_D4")
xilinx_xil_d5 = Net("/xilinx/XIL_D5")
xilinx_xil_d6 = Net("/xilinx/XIL_D6")
xilinx_xil_d7 = Net("/xilinx/XIL_D7")
xilinx_xil_d8 = Net("/xilinx/XIL_D8")
xilinx_xil_d9 = Net("/xilinx/XIL_D9")
gnd = Net("GND")
gnda = Net("GNDA")
net_abrt_sw101_pad1 = Net("Net-(ABRT_SW101-Pad1)")
net_bdm_port101_p22_pad26 = Net("Net-(BDM_PORT101-P22-Pad26)")
net_bdm_port101_p6 = Net("Net-(BDM_PORT101-P6)")
net_c104_pad1 = Net("Net-(C104-Pad1)")
net_can_term201_pad2 = Net("Net-(CAN_TERM201-Pad2)")
net_com_sel201_p3 = Net("Net-(COM_SEL201-P3)")
net_com_sel202_p3 = Net("Net-(COM_SEL202-P3)")
net_com_sel203_p3 = Net("Net-(COM_SEL203-P3)")
net_d101_k = Net("Net-(D101-K)")
net_d102_k = Net("Net-(D102-K)")
net_d201_k = Net("Net-(D201-K)")
net_d301_a = Net("Net-(D301-A)")
net_d302_a = Net("Net-(D302-A)")
net_f201_pad1 = Net("Net-(F201-Pad1)")
net_l102_pad1 = Net("Net-(L102-Pad1)")
net_led201_a = Net("Net-(LED201-A)")
net_led202_a = Net("Net-(LED202-A)")
net_led203_a = Net("Net-(LED203-A)")
net_led204_a = Net("Net-(LED204-A)")
net_led205_a = Net("Net-(LED205-A)")
net_ledabrt101_k = Net("Net-(LEDABRT101-K)")
net_led_rst101_a = Net("Net-(LED_RST101-A)")
net_mcu_port201_p1 = Net("Net-(MCU_PORT201-P1)")
net_pulupen201_pad2 = Net("Net-(PULUPEN201-Pad2)")
net_pulupen201_pad4 = Net("Net-(PULUPEN201-Pad4)")
net_pulupen201_pad6 = Net("Net-(PULUPEN201-Pad6)")
net_pulupen201_pad8 = Net("Net-(PULUPEN201-Pad8)")
net_q101_b = Net("Net-(Q101-B)")
net_q101_c = Net("Net-(Q101-C)")
net_tb201_p1 = Net("Net-(TB201-P1)")
net_u102_tclk_pstclk_clkout = Net("Net-(U102-TCLK/PSTCLK/CLKOUT)")
net_u102_test = Net("Net-(U102-TEST)")
net_u201a_e = Net("Net-(U201A-E)")
net_u201a_o = Net("Net-(U201A-O)")
net_u201b_o = Net("Net-(U201B-O)")
net_u201c_o = Net("Net-(U201C-O)")
net_u201d_o = Net("Net-(U201D-O)")
net_u202_c1 = Net("Net-(U202-C1+)")
net_u202_c1_2 = Net("Net-(U202-C1-)")
net_u202_c2 = Net("Net-(U202-C2+)")
net_u202_c2_2 = Net("Net-(U202-C2-)")
net_u202_r1out = Net("Net-(U202-R1OUT)")
net_u202_r2out = Net("Net-(U202-R2OUT)")
net_u202_t1in = Net("Net-(U202-T1IN)")
net_u202_t2in = Net("Net-(U202-T2IN)")
net_u202_v = Net("Net-(U202-V+)")
net_u202_v_2 = Net("Net-(U202-V-)")
net_u203_c1 = Net("Net-(U203-C1+)")
net_u203_c1_2 = Net("Net-(U203-C1-)")
net_u203_c2 = Net("Net-(U203-C2+)")
net_u203_c2_2 = Net("Net-(U203-C2-)")
net_u203_r1out = Net("Net-(U203-R1OUT)")
net_u203_r2out = Net("Net-(U203-R2OUT)")
net_u203_t1in = Net("Net-(U203-T1IN)")
net_u203_t2in = Net("Net-(U203-T2IN)")
net_u203_v = Net("Net-(U203-V+)")
net_u203_v_2 = Net("Net-(U203-V-)")
net_u204_c1 = Net("Net-(U204-C1+)")
net_u204_c1_2 = Net("Net-(U204-C1-)")
net_u204_c2 = Net("Net-(U204-C2+)")
net_u204_c2_2 = Net("Net-(U204-C2-)")
net_u204_r1out = Net("Net-(U204-R1OUT)")
net_u204_r2out = Net("Net-(U204-R2OUT)")
net_u204_t1in = Net("Net-(U204-T1IN)")
net_u204_t2in = Net("Net-(U204-T2IN)")
net_u204_v = Net("Net-(U204-V+)")
net_u204_v_2 = Net("Net-(U204-V-)")
net_u205_rsl = Net("Net-(U205-Rsl)")
net_u205_vref = Net("Net-(U205-Vref)")
net_u301_p11 = Net("Net-(U301-P11)")
net_u301_p4 = Net("Net-(U301-P4)")
net_uartcan201_p6 = Net("Net-(UARTCAN201-P6)")
net_uartcan202_p6 = Net("Net-(UARTCAN202-P6)")
net_uartcan203_p6 = Net("Net-(UARTCAN203-P6)")

design.rules.netclass(
    "POWER",
    clearance=mm("0.15"),
    track_width=mm("0.4"),
    via_diameter=mm("0.8"),
    via_drill=mm("0.4"),
    diff_pair_width=mm("0.2"),
    diff_pair_gap=mm("0.25"),
    diff_pair_via_gap=mm("0.25"),
    nets=(net_3_3v, gnd, gnda),
)
design.rules.minimum(
    clearance=mm("0.1"),
    track_width=mm("0.19812"),
    hole_size=mm("0.4"),
    edge_clearance=mm("0.01"),
)

d101 = Part("D101", "kit-dev-coldfire:D_SOT-23_ANK", footprint="kit-dev-coldfire:D_SOT-23_ANK", value="BAT54")
d102 = Part("D102", "kit-dev-coldfire:D_SOT-23_ANK", footprint="kit-dev-coldfire:D_SOT-23_ANK", value="BAT54")
j201 = Part("J201", "kit-dev-coldfire:JACK_ALIM", footprint="kit-dev-coldfire:JACK_ALIM", value="JACK_2P")
c201 = Part(
    "C201",
    "kit-dev-coldfire:C_0805_2012Metric_15",
    footprint="kit-dev-coldfire:C_0805_2012Metric_15",
    value="100nF",
)
c202 = Part(
    "C202",
    "kit-dev-coldfire:C_0805_2012Metric_7",
    footprint="kit-dev-coldfire:C_0805_2012Metric_7",
    value="100nF",
)
c203 = Part(
    "C203",
    "kit-dev-coldfire:C_0805_2012Metric_3",
    footprint="kit-dev-coldfire:C_0805_2012Metric_3",
    value="100nF",
)
c204 = Part(
    "C204",
    "kit-dev-coldfire:C_0805_2012Metric_16",
    footprint="kit-dev-coldfire:C_0805_2012Metric_16",
    value="100nF",
)
c205 = Part(
    "C205",
    "kit-dev-coldfire:C_0805_2012Metric_3",
    footprint="kit-dev-coldfire:C_0805_2012Metric_3",
    value="100nF",
)
c206 = Part(
    "C206",
    "kit-dev-coldfire:C_0805_2012Metric_3",
    footprint="kit-dev-coldfire:C_0805_2012Metric_3",
    value="100nF",
)
c207 = Part(
    "C207",
    "kit-dev-coldfire:C_0805_2012Metric_6",
    footprint="kit-dev-coldfire:C_0805_2012Metric_6",
    value="100nF",
)
c208 = Part(
    "C208",
    "kit-dev-coldfire:C_0805_2012Metric_3",
    footprint="kit-dev-coldfire:C_0805_2012Metric_3",
    value="100nF",
)
c209 = Part(
    "C209",
    "kit-dev-coldfire:C_0805_2012Metric_17",
    footprint="kit-dev-coldfire:C_0805_2012Metric_17",
    value="100nF",
)
c210 = Part(
    "C210",
    "kit-dev-coldfire:C_0805_2012Metric_3",
    footprint="kit-dev-coldfire:C_0805_2012Metric_3",
    value="100nF",
)
c211 = Part(
    "C211",
    "kit-dev-coldfire:C_0805_2012Metric_3",
    footprint="kit-dev-coldfire:C_0805_2012Metric_3",
    value="100nF",
)
c212 = Part(
    "C212",
    "kit-dev-coldfire:CP_Radial_D8.0mm_P5.00mm",
    footprint="kit-dev-coldfire:CP_Radial_D8.0mm_P5.00mm",
    value="10uF",
)
c213 = Part(
    "C213",
    "kit-dev-coldfire:C_0805_2012Metric_18",
    footprint="kit-dev-coldfire:C_0805_2012Metric_18",
    value="100nF",
)
c214 = Part(
    "C214",
    "kit-dev-coldfire:C_0805_2012Metric_6",
    footprint="kit-dev-coldfire:C_0805_2012Metric_6",
    value="100nF",
)
c215 = Part(
    "C215",
    "kit-dev-coldfire:CP_Radial_D8.0mm_P5.00mm_2",
    footprint="kit-dev-coldfire:CP_Radial_D8.0mm_P5.00mm_2",
    value="220uF",
)
c216 = Part(
    "C216",
    "kit-dev-coldfire:C_0805_2012Metric_3",
    footprint="kit-dev-coldfire:C_0805_2012Metric_3",
    value="100nF",
)
c217 = Part(
    "C217",
    "kit-dev-coldfire:C_0805_2012Metric_19",
    footprint="kit-dev-coldfire:C_0805_2012Metric_19",
    value="100nF",
)
c218 = Part(
    "C218",
    "kit-dev-coldfire:C_0805_2012Metric_3",
    footprint="kit-dev-coldfire:C_0805_2012Metric_3",
    value="100nF",
)
c219 = Part(
    "C219",
    "kit-dev-coldfire:C_0805_2012Metric_7",
    footprint="kit-dev-coldfire:C_0805_2012Metric_7",
    value="100nF",
)
c220 = Part(
    "C220",
    "kit-dev-coldfire:C_0805_2012Metric_20",
    footprint="kit-dev-coldfire:C_0805_2012Metric_20",
    value="100nF",
)
c221 = Part(
    "C221",
    "kit-dev-coldfire:C_0805_2012Metric_21",
    footprint="kit-dev-coldfire:C_0805_2012Metric_21",
    value="100nF",
)
can_en201 = Part(
    "CAN_EN201",
    "kit-dev-coldfire:PinHeader_2x02_P2.54mm_Vertical",
    footprint="kit-dev-coldfire:PinHeader_2x02_P2.54mm_Vertical",
    value="CONN_2X2",
)
can_term201 = Part(
    "CAN_TERM201",
    "kit-dev-coldfire:PinHeader_1x02_P2.54mm_Vertical",
    footprint="kit-dev-coldfire:PinHeader_1x02_P2.54mm_Vertical",
    value="JUMPER",
)
com_sel201 = Part(
    "COM_SEL201",
    "kit-dev-coldfire:PinHeader_1x03_P2.54mm_Vertical",
    footprint="kit-dev-coldfire:PinHeader_1x03_P2.54mm_Vertical",
    value="CONN_3",
)
com_sel202 = Part(
    "COM_SEL202",
    "kit-dev-coldfire:PinHeader_1x03_P2.54mm_Vertical_2",
    footprint="kit-dev-coldfire:PinHeader_1x03_P2.54mm_Vertical_2",
    value="CONN_3",
)
com_sel203 = Part(
    "COM_SEL203",
    "kit-dev-coldfire:PinHeader_1x03_P2.54mm_Vertical",
    footprint="kit-dev-coldfire:PinHeader_1x03_P2.54mm_Vertical",
    value="CONN_3",
)
d201 = Part(
    "D201",
    "kit-dev-coldfire:D_DO-15_P12.70mm_Horizontal",
    footprint="kit-dev-coldfire:D_DO-15_P12.70mm_Horizontal",
    value="1N4004",
)
f201 = Part("F201", "kit-dev-coldfire:FSUPCMS", footprint="kit-dev-coldfire:FSUPCMS", value="FUSE")
jp201 = Part(
    "JP201",
    "kit-dev-coldfire:PinHeader_1x02_P2.54mm_Vertical_3",
    footprint="kit-dev-coldfire:PinHeader_1x02_P2.54mm_Vertical_3",
    value="JUMPER",
)
led201 = Part(
    "LED201",
    "kit-dev-coldfire:LED_1206_3216Metric_2",
    footprint="kit-dev-coldfire:LED_1206_3216Metric_2",
    value="LED",
)
led202 = Part(
    "LED202",
    "kit-dev-coldfire:LED_1206_3216Metric_3",
    footprint="kit-dev-coldfire:LED_1206_3216Metric_3",
    value="LED",
)
led203 = Part(
    "LED203",
    "kit-dev-coldfire:LED_1206_3216Metric_3",
    footprint="kit-dev-coldfire:LED_1206_3216Metric_3",
    value="LED",
)
led204 = Part(
    "LED204",
    "kit-dev-coldfire:LED_1206_3216Metric_3",
    footprint="kit-dev-coldfire:LED_1206_3216Metric_3",
    value="LED",
)
led205 = Part(
    "LED205",
    "kit-dev-coldfire:LED_1206_3216Metric_4",
    footprint="kit-dev-coldfire:LED_1206_3216Metric_4",
    value="LED",
)
mcu_port201 = Part(
    "MCU_PORT201",
    "kit-dev-coldfire:PinHeader_2x30_P2.54mm_Vertical",
    footprint="kit-dev-coldfire:PinHeader_2x30_P2.54mm_Vertical",
    value="CONN_30X2",
)
pulupen201 = Part(
    "PULUPEN201",
    "kit-dev-coldfire:PinHeader_2x04_P2.54mm_Vertical",
    footprint="kit-dev-coldfire:PinHeader_2x04_P2.54mm_Vertical",
    value="CONN_4X2",
)
r201 = Part(
    "R201",
    "kit-dev-coldfire:R_0805_2012Metric_9",
    footprint="kit-dev-coldfire:R_0805_2012Metric_9",
    value="10K",
)
r202 = Part(
    "R202",
    "kit-dev-coldfire:R_0805_2012Metric_13",
    footprint="kit-dev-coldfire:R_0805_2012Metric_13",
    value="270",
)
r203 = Part(
    "R203",
    "kit-dev-coldfire:R_0805_2012Metric_13",
    footprint="kit-dev-coldfire:R_0805_2012Metric_13",
    value="270",
)
r204 = Part(
    "R204",
    "kit-dev-coldfire:R_0805_2012Metric_13",
    footprint="kit-dev-coldfire:R_0805_2012Metric_13",
    value="270",
)
r205 = Part(
    "R205",
    "kit-dev-coldfire:R_0805_2012Metric_10",
    footprint="kit-dev-coldfire:R_0805_2012Metric_10",
    value="10K",
)
r206 = Part(
    "R206",
    "kit-dev-coldfire:R_0805_2012Metric_13",
    footprint="kit-dev-coldfire:R_0805_2012Metric_13",
    value="270",
)
r207 = Part(
    "R207",
    "kit-dev-coldfire:R_0805_2012Metric_13",
    footprint="kit-dev-coldfire:R_0805_2012Metric_13",
    value="270",
)
r208 = Part(
    "R208",
    "kit-dev-coldfire:R_0805_2012Metric_10",
    footprint="kit-dev-coldfire:R_0805_2012Metric_10",
    value="10K",
)
r209 = Part(
    "R209",
    "kit-dev-coldfire:R_0805_2012Metric_19",
    footprint="kit-dev-coldfire:R_0805_2012Metric_19",
    value="62",
)
r210 = Part(
    "R210",
    "kit-dev-coldfire:R_0805_2012Metric_20",
    footprint="kit-dev-coldfire:R_0805_2012Metric_20",
    value="1K",
)
r211 = Part(
    "R211",
    "kit-dev-coldfire:R_0805_2012Metric_21",
    footprint="kit-dev-coldfire:R_0805_2012Metric_21",
    value="4,7K",
)
r212 = Part(
    "R212",
    "kit-dev-coldfire:R_0805_2012Metric_22",
    footprint="kit-dev-coldfire:R_0805_2012Metric_22",
    value="4,7K",
)
r213 = Part(
    "R213",
    "kit-dev-coldfire:R_0805_2012Metric_23",
    footprint="kit-dev-coldfire:R_0805_2012Metric_23",
    value="4,7K",
)
r214 = Part(
    "R214",
    "kit-dev-coldfire:R_0805_2012Metric_10",
    footprint="kit-dev-coldfire:R_0805_2012Metric_10",
    value="4,7K",
)
r215 = Part(
    "R215",
    "kit-dev-coldfire:R_0805_2012Metric_9",
    footprint="kit-dev-coldfire:R_0805_2012Metric_9",
    value="10K",
)
rcan201 = Part(
    "RCAN201",
    "kit-dev-coldfire:R_0805_2012Metric_24",
    footprint="kit-dev-coldfire:R_0805_2012Metric_24",
    value="R",
)
rcan202 = Part(
    "RCAN202",
    "kit-dev-coldfire:R_0805_2012Metric_25",
    footprint="kit-dev-coldfire:R_0805_2012Metric_25",
    value="R",
)
rs201 = Part(
    "RS201",
    "kit-dev-coldfire:PinHeader_1x01_P2.54mm_Vertical_2",
    footprint="kit-dev-coldfire:PinHeader_1x01_P2.54mm_Vertical_2",
    value="CONN_1",
)
sw201 = Part(
    "SW201",
    "kit-dev-coldfire:SW_PUSH_SMALL_3",
    footprint="kit-dev-coldfire:SW_PUSH_SMALL_3",
    value="SW_PUSH",
)
sw202 = Part(
    "SW202",
    "kit-dev-coldfire:SW_PUSH_SMALL_4",
    footprint="kit-dev-coldfire:SW_PUSH_SMALL_4",
    value="SW_PUSH",
)
sw_onoff201 = Part(
    "SW_ONOFF201",
    "kit-dev-coldfire:SW_SPDT",
    footprint="kit-dev-coldfire:SW_SPDT",
    value="SWITCH_INV",
)
tb201 = Part(
    "TB201",
    "kit-dev-coldfire:Altech_AK300_1x02_P5.00mm_45-Degree",
    footprint="kit-dev-coldfire:Altech_AK300_1x02_P5.00mm_45-Degree",
    value="CONN_2",
)
u201 = Part(
    "U201",
    "kit-dev-coldfire:SOIC-14_3.9x8.7mm_P1.27mm",
    footprint="kit-dev-coldfire:SOIC-14_3.9x8.7mm_P1.27mm",
    value="74HC125",
)
u202 = Part(
    "U202",
    "kit-dev-coldfire:SOIC-16_3.9x9.9mm_P1.27mm",
    footprint="kit-dev-coldfire:SOIC-16_3.9x9.9mm_P1.27mm",
    value="MAX202",
)
u203 = Part(
    "U203",
    "kit-dev-coldfire:SOIC-16_3.9x9.9mm_P1.27mm_2",
    footprint="kit-dev-coldfire:SOIC-16_3.9x9.9mm_P1.27mm_2",
    value="MAX202",
)
u204 = Part(
    "U204",
    "kit-dev-coldfire:SOIC-16_3.9x9.9mm_P1.27mm_3",
    footprint="kit-dev-coldfire:SOIC-16_3.9x9.9mm_P1.27mm_3",
    value="MAX202",
)
u205 = Part(
    "U205",
    "kit-dev-coldfire:SOIC-8_3.9x4.9mm_P1.27mm",
    footprint="kit-dev-coldfire:SOIC-8_3.9x4.9mm_P1.27mm",
    value="PCA82C251",
)
uartcan201 = Part(
    "UARTCAN201",
    "kit-dev-coldfire:DSUB-9_Female_Horizontal_P2.77x2.84mm_EdgePinOffset7.70mm_Housed_MountingHolesOffset9.12mm",
    footprint="kit-dev-coldfire:DSUB-9_Female_Horizontal_P2.77x2.84mm_EdgePinOffset7.70mm_Housed_MountingHolesOffset9.12mm",
    value="DB9",
)
uartcan202 = Part(
    "UARTCAN202",
    "kit-dev-coldfire:DSUB-9_Female_Horizontal_P2.77x2.84mm_EdgePinOffset7.70mm_Housed_MountingHolesOffset9.12mm_2",
    footprint="kit-dev-coldfire:DSUB-9_Female_Horizontal_P2.77x2.84mm_EdgePinOffset7.70mm_Housed_MountingHolesOffset9.12mm_2",
    value="DB9",
)
uartcan203 = Part(
    "UARTCAN203",
    "kit-dev-coldfire:DSUB-9_Female_Horizontal_P2.77x2.84mm_EdgePinOffset7.70mm_Housed_MountingHolesOffset9.12mm_3",
    footprint="kit-dev-coldfire:DSUB-9_Female_Horizontal_P2.77x2.84mm_EdgePinOffset7.70mm_Housed_MountingHolesOffset9.12mm_3",
    value="DB9",
)
uart_en201 = Part(
    "UART_EN201",
    "kit-dev-coldfire:PinHeader_2x04_P2.54mm_Vertical_2",
    footprint="kit-dev-coldfire:PinHeader_2x04_P2.54mm_Vertical_2",
    value="CONN_4X2",
)
uart_en202 = Part(
    "UART_EN202",
    "kit-dev-coldfire:PinHeader_2x04_P2.54mm_Vertical_2",
    footprint="kit-dev-coldfire:PinHeader_2x04_P2.54mm_Vertical_2",
    value="CONN_4X2",
)
uart_en203 = Part(
    "UART_EN203",
    "kit-dev-coldfire:PinHeader_2x04_P2.54mm_Vertical_2",
    footprint="kit-dev-coldfire:PinHeader_2x04_P2.54mm_Vertical_2",
    value="CONN_4X2",
)
vr201 = Part(
    "VR201",
    "kit-dev-coldfire:TO-263-5_TabPin3",
    footprint="kit-dev-coldfire:TO-263-5_TabPin3",
    value="LT1129_QPACK",
)
vref201 = Part(
    "VREF201",
    "kit-dev-coldfire:PinHeader_1x01_P2.54mm_Vertical_3",
    footprint="kit-dev-coldfire:PinHeader_1x01_P2.54mm_Vertical_3",
    value="CONN_1",
)
vx_en201 = Part(
    "VX_EN201",
    "kit-dev-coldfire:PinHeader_1x02_P2.54mm_Vertical_4",
    footprint="kit-dev-coldfire:PinHeader_1x02_P2.54mm_Vertical_4",
    value="JUMPER",
)
abrt_sw101 = Part(
    "ABRT_SW101",
    "kit-dev-coldfire:SW_PUSH_SMALL",
    footprint="kit-dev-coldfire:SW_PUSH_SMALL",
    value="SW_PUSH",
)
allpst101 = Part(
    "ALLPST101",
    "kit-dev-coldfire:PinHeader_1x01_P2.54mm_Vertical",
    footprint="kit-dev-coldfire:PinHeader_1x01_P2.54mm_Vertical",
    value="CONN_1",
)
bdm_port101 = Part(
    "BDM_PORT101",
    "kit-dev-coldfire:PinHeader_2x13_P2.54mm_Vertical",
    footprint="kit-dev-coldfire:PinHeader_2x13_P2.54mm_Vertical",
    value="CONN_13X2",
)
c101 = Part(
    "C101",
    "kit-dev-coldfire:C_0805_2012Metric",
    footprint="kit-dev-coldfire:C_0805_2012Metric",
    value="100nF",
)
c102 = Part(
    "C102",
    "kit-dev-coldfire:C_0805_2012Metric_2",
    footprint="kit-dev-coldfire:C_0805_2012Metric_2",
    value="1nF",
)
c103 = Part(
    "C103",
    "kit-dev-coldfire:C_0805_2012Metric_3",
    footprint="kit-dev-coldfire:C_0805_2012Metric_3",
    value="100nF",
)
c104 = Part(
    "C104",
    "kit-dev-coldfire:C_0805_2012Metric_4",
    footprint="kit-dev-coldfire:C_0805_2012Metric_4",
    value="100nF",
)
c105 = Part(
    "C105",
    "kit-dev-coldfire:C_0805_2012Metric_5",
    footprint="kit-dev-coldfire:C_0805_2012Metric_5",
    value="1nF",
)
c106 = Part(
    "C106",
    "kit-dev-coldfire:C_0805_2012Metric_6",
    footprint="kit-dev-coldfire:C_0805_2012Metric_6",
    value="10pF",
)
c107 = Part(
    "C107",
    "kit-dev-coldfire:C_0805_2012Metric_3",
    footprint="kit-dev-coldfire:C_0805_2012Metric_3",
    value="10pF",
)
c108 = Part("C108", "kit-dev-coldfire:SM1206POL", footprint="kit-dev-coldfire:SM1206POL", value="10uF")
c109 = Part(
    "C109",
    "kit-dev-coldfire:C_0805_2012Metric_7",
    footprint="kit-dev-coldfire:C_0805_2012Metric_7",
    value="100nF",
)
c110 = Part(
    "C110",
    "kit-dev-coldfire:C_0805_2012Metric_8",
    footprint="kit-dev-coldfire:C_0805_2012Metric_8",
    value="100nF",
)
c111 = Part(
    "C111",
    "kit-dev-coldfire:C_0805_2012Metric_9",
    footprint="kit-dev-coldfire:C_0805_2012Metric_9",
    value="100nF",
)
c112 = Part(
    "C112",
    "kit-dev-coldfire:C_0805_2012Metric_10",
    footprint="kit-dev-coldfire:C_0805_2012Metric_10",
    value="100nF",
)
c113 = Part(
    "C113",
    "kit-dev-coldfire:C_0805_2012Metric_11",
    footprint="kit-dev-coldfire:C_0805_2012Metric_11",
    value="100nF",
)
c114 = Part(
    "C114",
    "kit-dev-coldfire:C_0805_2012Metric_12",
    footprint="kit-dev-coldfire:C_0805_2012Metric_12",
    value="100nF",
)
c115 = Part(
    "C115",
    "kit-dev-coldfire:C_0805_2012Metric_12",
    footprint="kit-dev-coldfire:C_0805_2012Metric_12",
    value="100nF",
)
c116 = Part(
    "C116",
    "kit-dev-coldfire:C_0805_2012Metric_12",
    footprint="kit-dev-coldfire:C_0805_2012Metric_12",
    value="100nF",
)
c117 = Part(
    "C117",
    "kit-dev-coldfire:C_0805_2012Metric_13",
    footprint="kit-dev-coldfire:C_0805_2012Metric_13",
    value="100nF",
)
c118 = Part(
    "C118",
    "kit-dev-coldfire:C_0805_2012Metric_14",
    footprint="kit-dev-coldfire:C_0805_2012Metric_14",
    value="100nF",
)
c119 = Part("C119", "kit-dev-coldfire:SM1206POL_2", footprint="kit-dev-coldfire:SM1206POL_2", value="100uF")
clkout101 = Part(
    "CLKOUT101",
    "kit-dev-coldfire:PinHeader_1x01_P2.54mm_Vertical",
    footprint="kit-dev-coldfire:PinHeader_1x01_P2.54mm_Vertical",
    value="CONN_1",
)
ct101 = Part(
    "CT101",
    "kit-dev-coldfire:PinHeader_1x02_P2.54mm_Vertical_2",
    footprint="kit-dev-coldfire:PinHeader_1x02_P2.54mm_Vertical_2",
    value="JUMPER",
)
fb101 = Part(
    "FB101",
    "kit-dev-coldfire:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
    footprint="kit-dev-coldfire:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
    value="BEAD",
)
gnd101 = Part(
    "GND101",
    "kit-dev-coldfire:PinHeader_1x01_P2.54mm_Vertical",
    footprint="kit-dev-coldfire:PinHeader_1x01_P2.54mm_Vertical",
    value="CONN_1",
)
jp101 = Part(
    "JP101",
    "kit-dev-coldfire:PinHeader_2x03_P2.54mm_Vertical",
    footprint="kit-dev-coldfire:PinHeader_2x03_P2.54mm_Vertical",
    value="JUMPER_TRIPLE",
)
l101 = Part(
    "L101",
    "kit-dev-coldfire:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    footprint="kit-dev-coldfire:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="10uH",
)
l102 = Part(
    "L102",
    "kit-dev-coldfire:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    footprint="kit-dev-coldfire:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    value="10uH",
)
ledabrt101 = Part(
    "LEDABRT101",
    "kit-dev-coldfire:LED_1206_3216Metric_5",
    footprint="kit-dev-coldfire:LED_1206_3216Metric_5",
    value="LED_RED",
)
led_rst101 = Part(
    "LED_RST101",
    "kit-dev-coldfire:LED_1206_3216Metric_6",
    footprint="kit-dev-coldfire:LED_1206_3216Metric_6",
    value="LED_RED",
)
lv101 = Part("LV101", "kit-dev-coldfire:TO-92", footprint="kit-dev-coldfire:TO-92", value="DS1818")
q101 = Part("Q101", "kit-dev-coldfire:SOT23EBC", footprint="kit-dev-coldfire:SOT23EBC", value="3906")
r101 = Part(
    "R101",
    "kit-dev-coldfire:R_0805_2012Metric",
    footprint="kit-dev-coldfire:R_0805_2012Metric",
    value="4,7K",
)
r102 = Part(
    "R102",
    "kit-dev-coldfire:R_0805_2012Metric_2",
    footprint="kit-dev-coldfire:R_0805_2012Metric_2",
    value="4,7K",
)
r103 = Part(
    "R103",
    "kit-dev-coldfire:R_0805_2012Metric_3",
    footprint="kit-dev-coldfire:R_0805_2012Metric_3",
    value="270",
)
r104 = Part(
    "R104",
    "kit-dev-coldfire:R_0805_2012Metric_3",
    footprint="kit-dev-coldfire:R_0805_2012Metric_3",
    value="1K",
)
r105 = Part(
    "R105",
    "kit-dev-coldfire:R_0805_2012Metric_4",
    footprint="kit-dev-coldfire:R_0805_2012Metric_4",
    value="20K",
)
r106 = Part(
    "R106",
    "kit-dev-coldfire:R_0805_2012Metric_5",
    footprint="kit-dev-coldfire:R_0805_2012Metric_5",
    value="4,7K",
)
r107 = Part(
    "R107",
    "kit-dev-coldfire:R_0805_2012Metric_6",
    footprint="kit-dev-coldfire:R_0805_2012Metric_6",
    value="4,7K",
)
r108 = Part(
    "R108",
    "kit-dev-coldfire:R_0805_2012Metric_6",
    footprint="kit-dev-coldfire:R_0805_2012Metric_6",
    value="4,7K",
)
r109 = Part(
    "R109",
    "kit-dev-coldfire:R_0805_2012Metric_7",
    footprint="kit-dev-coldfire:R_0805_2012Metric_7",
    value="4,7K",
)
r110 = Part(
    "R110",
    "kit-dev-coldfire:R_0805_2012Metric_8",
    footprint="kit-dev-coldfire:R_0805_2012Metric_8",
    value="4,7K",
)
r111 = Part(
    "R111",
    "kit-dev-coldfire:R_0805_2012Metric_9",
    footprint="kit-dev-coldfire:R_0805_2012Metric_9",
    value="4,7K",
)
r112 = Part(
    "R112",
    "kit-dev-coldfire:R_0805_2012Metric_10",
    footprint="kit-dev-coldfire:R_0805_2012Metric_10",
    value="4,7K",
)
r113 = Part(
    "R113",
    "kit-dev-coldfire:R_0805_2012Metric_11",
    footprint="kit-dev-coldfire:R_0805_2012Metric_11",
    value="0",
)
r114 = Part(
    "R114",
    "kit-dev-coldfire:R_0805_2012Metric_12",
    footprint="kit-dev-coldfire:R_0805_2012Metric_12",
    value="22",
)
r115 = Part(
    "R115",
    "kit-dev-coldfire:R_0805_2012Metric_10",
    footprint="kit-dev-coldfire:R_0805_2012Metric_10",
    value="4.7K",
)
r116 = Part(
    "R116",
    "kit-dev-coldfire:R_0805_2012Metric_13",
    footprint="kit-dev-coldfire:R_0805_2012Metric_13",
    value="270",
)
r117 = Part(
    "R117",
    "kit-dev-coldfire:R_0805_2012Metric_14",
    footprint="kit-dev-coldfire:R_0805_2012Metric_14",
    value="10K",
)
r118 = Part(
    "R118",
    "kit-dev-coldfire:R_0805_2012Metric_15",
    footprint="kit-dev-coldfire:R_0805_2012Metric_15",
    value="10K",
)
r119 = Part(
    "R119",
    "kit-dev-coldfire:R_0805_2012Metric_6",
    footprint="kit-dev-coldfire:R_0805_2012Metric_6",
    value="10K",
)
r120 = Part(
    "R120",
    "kit-dev-coldfire:R_0805_2012Metric_13",
    footprint="kit-dev-coldfire:R_0805_2012Metric_13",
    value="10K",
)
r121 = Part(
    "R121",
    "kit-dev-coldfire:R_0805_2012Metric_13",
    footprint="kit-dev-coldfire:R_0805_2012Metric_13",
    value="10K",
)
r122 = Part(
    "R122",
    "kit-dev-coldfire:R_0805_2012Metric_16",
    footprint="kit-dev-coldfire:R_0805_2012Metric_16",
    value="10K",
)
r123 = Part(
    "R123",
    "kit-dev-coldfire:R_0805_2012Metric_17",
    footprint="kit-dev-coldfire:R_0805_2012Metric_17",
    value="10K",
)
r124 = Part(
    "R124",
    "kit-dev-coldfire:R_0805_2012Metric_18",
    footprint="kit-dev-coldfire:R_0805_2012Metric_18",
    value="10K",
)
r125 = Part(
    "R125",
    "kit-dev-coldfire:R_0805_2012Metric_10",
    footprint="kit-dev-coldfire:R_0805_2012Metric_10",
    value="1M",
)
rst_sw101 = Part(
    "RST_SW101",
    "kit-dev-coldfire:SW_PUSH_SMALL_2",
    footprint="kit-dev-coldfire:SW_PUSH_SMALL_2",
    value="SW_PUSH",
)
ta_101 = Part(
    "TA-101",
    "kit-dev-coldfire:PinHeader_1x01_P2.54mm_Vertical",
    footprint="kit-dev-coldfire:PinHeader_1x01_P2.54mm_Vertical",
    value="CONN_1",
)
u101 = Part("U101", "kit-dev-coldfire:SOT353", footprint="kit-dev-coldfire:SOT353", value="74AHC1G14")
u102 = Part(
    "U102",
    "kit-dev-coldfire:LQFP-100_14x14mm_P0.5mm",
    footprint="kit-dev-coldfire:LQFP-100_14x14mm_P0.5mm",
    value="MCF5213-LQFP100",
)
vdda101 = Part(
    "VDDA101",
    "kit-dev-coldfire:PinHeader_1x02_P2.54mm_Vertical_4",
    footprint="kit-dev-coldfire:PinHeader_1x02_P2.54mm_Vertical_4",
    value="JUMPER",
)
y101 = Part(
    "Y101",
    "kit-dev-coldfire:Crystal_HC18-U_Horizontal",
    footprint="kit-dev-coldfire:Crystal_HC18-U_Horizontal",
    value="8MHz",
)
c301 = Part(
    "C301",
    "kit-dev-coldfire:C_0805_2012Metric_13",
    footprint="kit-dev-coldfire:C_0805_2012Metric_13",
    value="100nF",
)
c302 = Part(
    "C302",
    "kit-dev-coldfire:C_0805_2012Metric_10",
    footprint="kit-dev-coldfire:C_0805_2012Metric_10",
    value="100nF",
)
c303 = Part(
    "C303",
    "kit-dev-coldfire:C_0805_2012Metric_13",
    footprint="kit-dev-coldfire:C_0805_2012Metric_13",
    value="100nF",
)
c304 = Part(
    "C304",
    "kit-dev-coldfire:C_0805_2012Metric_14",
    footprint="kit-dev-coldfire:C_0805_2012Metric_14",
    value="100nF",
)
c305 = Part(
    "C305",
    "kit-dev-coldfire:C_0805_2012Metric_14",
    footprint="kit-dev-coldfire:C_0805_2012Metric_14",
    value="100nF",
)
c306 = Part(
    "C306",
    "kit-dev-coldfire:C_0805_2012Metric_14",
    footprint="kit-dev-coldfire:C_0805_2012Metric_14",
    value="100nF",
)
c307 = Part(
    "C307",
    "kit-dev-coldfire:C_0805_2012Metric_14",
    footprint="kit-dev-coldfire:C_0805_2012Metric_14",
    value="100nF",
)
c308 = Part(
    "C308",
    "kit-dev-coldfire:C_0805_2012Metric_13",
    footprint="kit-dev-coldfire:C_0805_2012Metric_13",
    value="100nF",
)
c309 = Part(
    "C309",
    "kit-dev-coldfire:C_0805_2012Metric_14",
    footprint="kit-dev-coldfire:C_0805_2012Metric_14",
    value="100nF",
)
c310 = Part(
    "C310",
    "kit-dev-coldfire:C_0805_2012Metric_14",
    footprint="kit-dev-coldfire:C_0805_2012Metric_14",
    value="100nF",
)
c311 = Part(
    "C311",
    "kit-dev-coldfire:C_0805_2012Metric_10",
    footprint="kit-dev-coldfire:C_0805_2012Metric_10",
    value="100nF",
)
d301 = Part(
    "D301",
    "kit-dev-coldfire:LED_1206_3216Metric",
    footprint="kit-dev-coldfire:LED_1206_3216Metric",
    value="LED",
)
d302 = Part(
    "D302",
    "kit-dev-coldfire:LED_1206_3216Metric",
    footprint="kit-dev-coldfire:LED_1206_3216Metric",
    value="LED",
)
p301 = Part(
    "P301",
    "kit-dev-coldfire:PinHeader_1x06_P2.54mm_Vertical",
    footprint="kit-dev-coldfire:PinHeader_1x06_P2.54mm_Vertical",
    value="CONN_6",
)
p302 = Part(
    "P302",
    "kit-dev-coldfire:PinHeader_2x02_P2.54mm_Vertical",
    footprint="kit-dev-coldfire:PinHeader_2x02_P2.54mm_Vertical",
    value="CONN_2X2",
)
p303 = Part(
    "P303",
    "kit-dev-coldfire:PinHeader_2x20_P2.54mm_Vertical",
    footprint="kit-dev-coldfire:PinHeader_2x20_P2.54mm_Vertical",
    value="CONN_20X2",
)
r301 = Part(
    "R301",
    "kit-dev-coldfire:R_0805_2012Metric_3",
    footprint="kit-dev-coldfire:R_0805_2012Metric_3",
    value="4K7",
)
r302 = Part(
    "R302",
    "kit-dev-coldfire:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
    footprint="kit-dev-coldfire:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
    value="3,3",
)
r303 = Part(
    "R303",
    "kit-dev-coldfire:R_0805_2012Metric_13",
    footprint="kit-dev-coldfire:R_0805_2012Metric_13",
    value="1K",
)
r304 = Part(
    "R304",
    "kit-dev-coldfire:R_0805_2012Metric_13",
    footprint="kit-dev-coldfire:R_0805_2012Metric_13",
    value="1K",
)
u301 = Part(
    "U301",
    "kit-dev-coldfire:TQFP-144_20x20mm_P0.5mm",
    footprint="kit-dev-coldfire:TQFP-144_20x20mm_P0.5mm",
    value="XCR3256-TQ144",
)

inout_user = Module("inout_user")
racine = Module("racine")
xilinx = Module("xilinx")

inout_user.add(
    c201,
    c202,
    c203,
    c204,
    c205,
    c206,
    c207,
    c208,
    c209,
    c210,
    c211,
    c212,
    c213,
    c214,
    c215,
    c216,
    c217,
    c218,
    c219,
    c220,
    c221,
    can_en201,
    can_term201,
    com_sel201,
    com_sel202,
    com_sel203,
    d201,
    f201,
    jp201,
    led201,
    led202,
    led203,
    led204,
    led205,
    mcu_port201,
    pulupen201,
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
    r214,
    r215,
    rcan201,
    rcan202,
    rs201,
    sw201,
    sw202,
    sw_onoff201,
    tb201,
    u201,
    u202,
    u203,
    u204,
    u205,
    uartcan201,
    uartcan202,
    uartcan203,
    uart_en201,
    uart_en202,
    uart_en203,
    vr201,
    vref201,
    vx_en201,
)
racine.add(
    abrt_sw101,
    allpst101,
    bdm_port101,
    c101,
    c102,
    c103,
    c104,
    c105,
    c106,
    c107,
    c108,
    c109,
    c110,
    c111,
    c112,
    c113,
    c114,
    c115,
    c116,
    c117,
    c118,
    c119,
    clkout101,
    ct101,
    fb101,
    gnd101,
    jp101,
    l101,
    l102,
    ledabrt101,
    led_rst101,
    lv101,
    q101,
    r101,
    r102,
    r103,
    r104,
    r105,
    r106,
    r107,
    r108,
    r109,
    r110,
    r111,
    r112,
    r113,
    r114,
    r115,
    r116,
    r117,
    r118,
    r119,
    r120,
    r121,
    r122,
    r123,
    r124,
    r125,
    rst_sw101,
    ta_101,
    u101,
    u102,
    vdda101,
    y101,
)
xilinx.add(
    c301,
    c302,
    c303,
    c304,
    c305,
    c306,
    c307,
    c308,
    c309,
    c310,
    c311,
    d301,
    d302,
    p301,
    p302,
    p303,
    r301,
    r302,
    r303,
    r304,
    u301,
)
design.add(d101, d102, j201, inout_user, racine, xilinx)

connect(
    net_3_3v,
    abrt_sw101["2"],
    bdm_port101["9"],
    bdm_port101["25"],
    c101["2"],
    c110["1"],
    c111["1"],
    c112["1"],
    c113["1"],
    c114["1"],
    c115["1"],
    c116["1"],
    c117["1"],
    c118["1"],
    c119["1"],
    c202["1"],
    c203["1"],
    c204["1"],
    c208["1"],
    c209["1"],
    c215["1"],
    c216["1"],
    c217["1"],
    c219["1"],
    c301["1"],
    c302["1"],
    c303["1"],
    c304["1"],
    c305["1"],
    c306["1"],
    c307["1"],
    c308["1"],
    c309["1"],
    c310["1"],
    c311["1"],
    l101["1"],
    ledabrt101["2"],
    lv101["2"],
    mcu_port201["59"],
    p301["1"],
    q101["1"],
    r101["1"],
    r102["1"],
    r106["1"],
    r107["1"],
    r108["1"],
    r109["1"],
    r110["1"],
    r111["1"],
    r112["2"],
    r118["2"],
    r119["2"],
    r120["2"],
    r121["2"],
    r122["2"],
    r123["2"],
    r124["2"],
    r201["1"],
    r207["2"],
    r211["1"],
    r212["1"],
    r213["1"],
    r214["1"],
    r301["1"],
    r302["1"],
    rcan202["1"],
    u101["5"],
    u102["1"],
    u102["2"],
    u102["14"],
    u102["22"],
    u102["23"],
    u102["34"],
    u102["41"],
    u102["55"],
    u102["57"],
    u102["68"],
    u102["81"],
    u102["93"],
    u201["14"],
    u202["16"],
    u203["16"],
    u204["16"],
    u205["3"],
    u301["24"],
    u301["50"],
    u301["51"],
    u301["58"],
    u301["73"],
    u301["76"],
    u301["95"],
    u301["115"],
    u301["123"],
    u301["130"],
    u301["144"],
    vdda101["1"],
    vr201["1"],
    vr201["2"],
    vx_en201["1"],
)
connect(allpst, allpst101["1"], u102["86"])
connect(an0, mcu_port201["10"], u102["43"])
connect(an1, mcu_port201["12"], u102["44"])
connect(an2, mcu_port201["14"], u102["45"])
connect(an3, mcu_port201["16"], u102["46"])
connect(an4, mcu_port201["18"], u102["54"])
connect(an5, mcu_port201["20"], u102["53"])
connect(an6, mcu_port201["22"], u102["52"])
connect(an7, mcu_port201["24"], u102["51"])
connect(bkpt, bdm_port101["2"], r107["2"], u102["76"])
connect(canrx, can_en201["4"], mcu_port201["28"], pulupen201["7"], u102["11"])
connect(cantx, can_en201["1"], mcu_port201["26"], pulupen201["5"], u102["10"])
connect(clkin_extal, c107["1"], r125["2"], u102["73"], y101["1"])
connect(clkmod0, jp101["6"], r101["2"], u102["40"])
connect(clkmod1, jp101["4"], r102["2"], u102["39"])
connect(ddat0, bdm_port101["19"], u102["77"])
connect(ddat1, bdm_port101["18"], u102["78"])
connect(ddat2, bdm_port101["17"], u102["83"])
connect(ddat3, bdm_port101["16"], u102["84"])
connect(dsclk, bdm_port101["4"], r108["2"], u102["85"])
connect(dsi, bdm_port101["8"], r109["2"], u102["79"])
connect(dso, bdm_port101["10"], r110["2"], u102["80"])
connect(dspi_dout, mcu_port201["17"], u102["17"], u301["47"])
connect(dtin0, mcu_port201["34"], u102["36"], u201["2"])
connect(dtin1, mcu_port201["36"], u102["37"], u201["5"])
connect(dtin2, mcu_port201["38"], u102["31"], u201["12"])
connect(dtin3, mcu_port201["40"], u102["32"], u201["9"])
connect(gpt0, mcu_port201["49"], u102["58"])
connect(gpt1, mcu_port201["50"], u102["59"])
connect(gpt2, mcu_port201["51"], u102["61"])
connect(gpt3, mcu_port201["52"], u102["62"])
connect(irq_1, mcu_port201["2"], r118["1"], u102["87"], u301["42"])
connect(irq_2, mcu_port201["8"], r119["1"], u102["88"], u301["43"])
connect(irq_3, mcu_port201["31"], r120["1"], u102["89"], u301["44"])
connect(irq_4, mcu_port201["33"], r121["1"], sw201["1"], u102["90"])
connect(irq_5, mcu_port201["35"], r122["1"], sw202["1"], u102["91"])
connect(irq_6, mcu_port201["37"], r123["1"], u102["94"])
connect(irq_7, d101["2"], mcu_port201["39"], r124["1"], u102["95"])
connect(jtag_en, jp101["2"], r111["2"], u102["26"])
connect(pst0, bdm_port101["15"], u102["65"])
connect(pst1, bdm_port101["14"], u102["66"])
connect(pst2, bdm_port101["13"], u102["69"])
connect(pst3, bdm_port101["12"], u102["70"])
connect(pwm1, mcu_port201["13"], u102["38"])
connect(pwm3, mcu_port201["15"], u102["33"])
connect(pwm5, mcu_port201["30"], u102["60"])
connect(pwm7, mcu_port201["32"], u102["63"])
connect(qspi_clk, mcu_port201["21"], pulupen201["1"], u102["18"], u301["48"])
connect(qspi_cs0, mcu_port201["23"], pulupen201["3"], u102["20"])
connect(qspi_cs1, mcu_port201["25"], u102["19"], u301["54"])
connect(qspi_cs2, mcu_port201["27"], u102["13"], u301["45"])
connect(qspi_cs3, mcu_port201["29"], u102["12"])
connect(qspi_din, mcu_port201["19"], u102["16"], u301["46"])
connect(rcon, mcu_port201["53"], r112["1"], u102["21"])
connect(rsti, bdm_port101["7"], d102["2"], mcu_port201["6"], r106["2"], u102["96"])
connect(rsto, mcu_port201["4"], r115["1"], u102["97"])
connect(tclk, bdm_port101["24"], clkout101["1"], ct101["2"], r114["2"], r117["1"])
connect(ucts0, mcu_port201["44"], u102["6"], uart_en201["8"])
connect(ucts1, mcu_port201["11"], p302["1"], u102["98"], u301["49"], uart_en202["8"])
connect(ucts2, mcu_port201["48"], u102["27"], uart_en203["8"])
connect(urts0, mcu_port201["42"], u102["9"], uart_en201["6"])
connect(urts1, mcu_port201["9"], p302["3"], u102["4"], u301["53"], uart_en202["6"])
connect(urts2, mcu_port201["46"], u102["30"], uart_en203["6"])
connect(urxd0, mcu_port201["43"], u102["7"], uart_en201["4"])
connect(urxd1, mcu_port201["7"], u102["100"], uart_en202["4"])
connect(urxd2, mcu_port201["47"], u102["28"], uart_en203["4"])
connect(utxd0, mcu_port201["41"], u102["8"], uart_en201["2"])
connect(utxd1, mcu_port201["5"], u102["99"], uart_en202["2"])
connect(utxd2, mcu_port201["45"], u102["29"], uart_en203["2"])
connect(vcca, c108["1"], c109["1"], l102["2"], mcu_port201["55"], mcu_port201["57"], u102["49"], u102["50"])
connect(vddpll, c102["1"], c103["1"], l101["2"], u102["74"])
connect(xtal, c106["1"], r125["1"], u102["72"], u301["128"], y101["2"])
connect(inout_user_can_h, can_term201["1"], com_sel203["1"], rcan201["2"], u205["7"])
connect(inout_user_can_l, com_sel201["1"], r209["1"], rcan202["2"], u205["6"])
connect(inout_user_cts0, u202["8"], uartcan201["7"])
connect(inout_user_cts1, u203["8"], uartcan202["7"])
connect(inout_user_cts2_canh, com_sel203["2"], uartcan203["7"])
connect(inout_user_rts0, u202["7"], uartcan201["8"])
connect(inout_user_rts1, u203["7"], uartcan202["8"])
connect(inout_user_rts2, u204["14"], uartcan203["8"])
connect(inout_user_rxd0, u202["13"], uartcan201["3"])
connect(inout_user_rxd1, u203["13"], uartcan202["3"])
connect(inout_user_rxd2, com_sel202["2"], uartcan203["3"])
connect(inout_user_rxd_can, can_en201["2"], u205["4"])
connect(inout_user_txd0, u202["14"], uartcan201["2"])
connect(inout_user_txd1, u203["14"], uartcan202["2"])
connect(inout_user_txd2_canl, com_sel201["2"], uartcan203["2"])
connect(inout_user_txd_can, can_en201["3"], u205["1"])
connect(xilinx_3_3v_out, p303["38"], r302["2"])
connect(xilinx_led_test1, r303["1"], u301["28"])
connect(xilinx_led_test2, r304["1"], u301["27"])
connect(xilinx_tck, p301["5"], r301["2"], u301["89"])
connect(xilinx_tdi, p301["4"], u301["4"])
connect(xilinx_tdo, p301["6"], u301["104"])
connect(xilinx_tms, p301["3"], u301["20"])
connect(xilinx_xil_d0, p303["1"], u301["12"])
connect(xilinx_xil_d1, p303["3"], u301["11"])
connect(xilinx_xil_d10, p303["21"], u301["122"])
connect(xilinx_xil_d11, p303["23"], u301["119"])
connect(xilinx_xil_d12, p303["25"], u301["114"])
connect(xilinx_xil_d13, p303["27"], u301["111"])
connect(xilinx_xil_d14, p303["29"], u301["109"])
connect(xilinx_xil_d15, p303["31"], u301["108"])
connect(xilinx_xil_d16, p303["33"], u301["100"])
connect(xilinx_xil_d17, p303["35"], u301["101"])
connect(xilinx_xil_d18, p303["37"], u301["97"])
connect(xilinx_xil_d19, p303["39"], u301["96"])
connect(xilinx_xil_d2, p303["5"], u301["7"])
connect(xilinx_xil_d20, p303["4"], u301["6"])
connect(xilinx_xil_d21, p303["6"], u301["10"])
connect(xilinx_xil_d22, p303["8"], u301["5"])
connect(xilinx_xil_d23, p303["10"], u301["1"])
connect(xilinx_xil_d24, p303["12"], u301["142"])
connect(xilinx_xil_d25, p303["14"], u301["139"])
connect(xilinx_xil_d26, p303["16"], u301["137"])
connect(xilinx_xil_d27, p303["18"], u301["134"])
connect(xilinx_xil_d28, p303["20"], u301["132"])
connect(xilinx_xil_d29, p303["22"], u301["117"])
connect(xilinx_xil_d3, p303["7"], u301["8"])
connect(xilinx_xil_d30, p303["24"], u301["118"])
connect(xilinx_xil_d31, p303["26"], u301["116"])
connect(xilinx_xil_d32, p303["28"], u301["98"])
connect(xilinx_xil_d33, p303["30"], u301["112"])
connect(xilinx_xil_d34, p303["32"], u301["113"])
connect(xilinx_xil_d35, p303["34"], u301["107"])
connect(xilinx_xil_d36, p303["36"], u301["99"])
connect(xilinx_xil_d4, p303["9"], u301["2"])
connect(xilinx_xil_d5, p303["11"], u301["143"])
connect(xilinx_xil_d6, p303["13"], u301["140"])
connect(xilinx_xil_d7, p303["15"], u301["138"])
connect(xilinx_xil_d8, p303["17"], u301["136"])
connect(xilinx_xil_d9, p303["19"], u301["131"])
connect(
    gnd,
    bdm_port101["3"],
    bdm_port101["5"],
    bdm_port101["11"],
    bdm_port101["20"],
    bdm_port101["23"],
    c101["1"],
    c102["2"],
    c103["2"],
    c104["2"],
    c105["2"],
    c106["2"],
    c107["2"],
    c110["2"],
    c111["2"],
    c112["2"],
    c113["2"],
    c114["2"],
    c115["2"],
    c116["2"],
    c117["2"],
    c118["2"],
    c119["2"],
    c201["1"],
    c202["2"],
    c203["2"],
    c207["2"],
    c208["2"],
    c212["2"],
    c213["2"],
    c214["2"],
    c215["2"],
    c216["2"],
    c219["2"],
    c221["2"],
    c301["2"],
    c302["2"],
    c303["2"],
    c304["2"],
    c305["2"],
    c306["2"],
    c307["2"],
    c308["2"],
    c309["2"],
    c310["2"],
    c311["2"],
    com_sel202["1"],
    d201["2"],
    d301["1"],
    d302["1"],
    fb101["1"],
    gnd101["1"],
    j201["1"],
    j201["2"],
    jp101["1"],
    jp101["3"],
    jp101["5"],
    jp201["1"],
    led201["1"],
    led202["1"],
    led203["1"],
    led204["1"],
    led205["1"],
    led_rst101["1"],
    lv101["3"],
    mcu_port201["3"],
    mcu_port201["54"],
    mcu_port201["60"],
    p301["2"],
    p303["2"],
    p303["40"],
    r105["2"],
    r113["2"],
    r117["2"],
    r205["1"],
    r208["1"],
    r210["2"],
    r215["1"],
    rcan201["1"],
    rst_sw101["2"],
    sw201["2"],
    sw202["2"],
    tb201["2"],
    u101["3"],
    u102["3"],
    u102["15"],
    u102["24"],
    u102["25"],
    u102["35"],
    u102["42"],
    u102["56"],
    u102["67"],
    u102["71"],
    u102["75"],
    u102["82"],
    u102["92"],
    u201["7"],
    u202["15"],
    u203["15"],
    u204["15"],
    u205["2"],
    u301["3"],
    u301["13"],
    u301["17"],
    u301["33"],
    u301["52"],
    u301["57"],
    u301["59"],
    u301["64"],
    u301["85"],
    u301["105"],
    u301["124"],
    u301["125"],
    u301["126"],
    u301["127"],
    u301["129"],
    u301["135"],
    uartcan201["5"],
    uartcan202["5"],
    uartcan203["5"],
    vr201["3"],
)
connect(gnda, c108["2"], c109["2"], fb101["2"], mcu_port201["56"], mcu_port201["58"], u102["47"], u102["48"])
connect(net_abrt_sw101_pad1, abrt_sw101["1"], r104["1"])
connect(net_bdm_port101_p22_pad26, bdm_port101["26"], ta_101["1"])
connect(net_bdm_port101_p6, bdm_port101["6"], ct101["1"])
connect(net_c104_pad1, c104["1"], r104["2"], r105["1"], u101["2"])
connect(net_can_term201_pad2, can_term201["2"], r209["2"])
connect(net_com_sel201_p3, com_sel201["3"], u204["7"])
connect(net_com_sel202_p3, com_sel202["3"], u204["8"])
connect(net_com_sel203_p3, com_sel203["3"], u204["13"])
connect(net_d101_k, d101["1"], r103["2"], u101["4"])
connect(net_d102_k, c105["1"], d102["1"], lv101["1"], rst_sw101["1"])
connect(net_d201_k, c212["1"], c213["1"], d201["1"], f201["2"], vr201["5"])
connect(net_d301_a, d301["2"], r303["2"])
connect(net_d302_a, d302["2"], r304["2"])
connect(net_f201_pad1, f201["1"], sw_onoff201["2"])
connect(net_l102_pad1, l102["1"], vdda101["2"])
connect(net_led201_a, led201["2"], r202["1"])
connect(net_led202_a, led202["2"], r203["1"])
connect(net_led203_a, led203["2"], r204["1"])
connect(net_led204_a, led204["2"], r206["1"])
connect(net_led205_a, led205["2"], r207["1"])
connect(net_ledabrt101_k, ledabrt101["1"], r103["1"])
connect(net_led_rst101_a, led_rst101["2"], r116["2"])
connect(net_mcu_port201_p1, c201["2"], mcu_port201["1"], vx_en201["2"])
connect(net_pulupen201_pad2, pulupen201["2"], r211["2"])
connect(net_pulupen201_pad4, pulupen201["4"], r212["2"])
connect(net_pulupen201_pad6, pulupen201["6"], r213["2"])
connect(net_pulupen201_pad8, pulupen201["8"], r214["2"])
connect(net_q101_b, q101["2"], r115["2"])
connect(net_q101_c, q101["3"], r116["1"])
connect(net_tb201_p1, j201["3"], sw_onoff201["3"], tb201["1"])
connect(net_u102_tclk_pstclk_clkout, r114["1"], u102["64"])
connect(net_u102_test, r113["1"], u102["5"])
connect(net_u201a_e, jp201["2"], r201["2"], u201["1"], u201["4"], u201["10"], u201["13"])
connect(net_u201a_o, r202["2"], u201["3"])
connect(net_u201b_o, r203["2"], u201["6"])
connect(net_u201c_o, r206["2"], u201["8"])
connect(net_u201d_o, r204["2"], u201["11"])
connect(net_u202_c1, c205["1"], u202["1"])
connect(net_u202_c1_2, c205["2"], u202["3"])
connect(net_u202_c2, c206["1"], u202["4"])
connect(net_u202_c2_2, c206["2"], u202["5"])
connect(net_u202_r1out, u202["12"], uart_en201["3"])
connect(net_u202_r2out, u202["9"], uart_en201["7"])
connect(net_u202_t1in, u202["11"], uart_en201["1"])
connect(net_u202_t2in, r205["2"], u202["10"], uart_en201["5"])
connect(net_u202_v, c204["2"], u202["2"])
connect(net_u202_v_2, c207["1"], u202["6"])
connect(net_u203_c1, c210["1"], u203["1"])
connect(net_u203_c1_2, c210["2"], u203["3"])
connect(net_u203_c2, c211["1"], u203["4"])
connect(net_u203_c2_2, c211["2"], u203["5"])
connect(net_u203_r1out, u203["12"], uart_en202["3"])
connect(net_u203_r2out, u203["9"], uart_en202["7"])
connect(net_u203_t1in, u203["11"], uart_en202["1"])
connect(net_u203_t2in, r208["2"], u203["10"], uart_en202["5"])
connect(net_u203_v, c209["2"], u203["2"])
connect(net_u203_v_2, c214["1"], u203["6"])
connect(net_u204_c1, c218["1"], u204["1"])
connect(net_u204_c1_2, c218["2"], u204["3"])
connect(net_u204_c2, c220["1"], u204["4"])
connect(net_u204_c2_2, c220["2"], u204["5"])
connect(net_u204_r1out, u204["12"], uart_en203["7"])
connect(net_u204_r2out, u204["9"], uart_en203["3"])
connect(net_u204_t1in, r215["2"], u204["11"], uart_en203["5"])
connect(net_u204_t2in, u204["10"], uart_en203["1"])
connect(net_u204_v, c217["2"], u204["2"])
connect(net_u204_v_2, c221["1"], u204["6"])
connect(net_u205_rsl, r210["1"], rs201["1"], u205["8"])
connect(net_u205_vref, u205["5"], vref201["1"])
connect(net_u301_p11, p302["2"], u301["32"])
connect(net_u301_p4, p302["4"], u301["31"])
connect(net_uartcan201_p6, uartcan201["1"], uartcan201["4"], uartcan201["6"])
connect(net_uartcan202_p6, uartcan202["1"], uartcan202["4"], uartcan202["6"])
connect(net_uartcan203_p6, uartcan203["1"], uartcan203["4"], uartcan203["6"])

d101.place(mm("60.401"), mm("2.489"))
d102.place(mm("61.798"), mm("-4.369"))
j201.place(mm("4.5"), mm("-40"), rot=-90)
c201.place(mm("83.769"), mm("25.73"))
c202.place(mm("2.616"), mm("11.252"))
c203.place(mm("92.532"), mm("-25.832"), rot=-90)
c204.place(mm("89.23"), mm("-28.753"), rot=180)
c205.place(mm("81.102"), mm("-26.086"), rot=-90)
c206.place(mm("81.102"), mm("-21.768"), rot=-90)
c207.place(mm("78.562"), mm("-21.895"), rot=90)
c208.place(mm("64.592"), mm("-25.832"), rot=-90)
c209.place(mm("61.29"), mm("-28.753"), rot=180)
c210.place(mm("53.162"), mm("-26.213"), rot=-90)
c211.place(mm("53.035"), mm("-21.895"), rot=-90)
c212.place(mm("-11.1"), mm("-12.37"), rot=90)
c213.place(mm("4"), mm("-22.5"), rot=90)
c214.place(mm("50.876"), mm("-21.895"), rot=90)
c215.place(mm("-11.1"), mm("0.33"), rot=90)
c216.place(mm("30.937"), mm("-25.451"), rot=-90)
c217.place(mm("28.27"), mm("-28.753"), rot=180)
c218.place(mm("20.142"), mm("-26.213"), rot=-90)
c219.place(mm("8.458"), mm("-15.672"))
c220.place(mm("20.142"), mm("-21.895"), rot=-90)
c221.place(mm("17.602"), mm("-21.895"), rot=90)
can_en201.place(mm("12.522"), mm("-13.767"))
can_term201.place(mm("-3.353"), mm("-4.242"), rot=180)
com_sel201.place(mm("7"), mm("-21.387"), rot=180)
com_sel202.place(mm("10.744"), mm("-21.387"), rot=180)
com_sel203.place(mm("14.5"), mm("-21.387"), rot=180)
d201.place(mm("-5"), mm("-23"), rot=180)
f201.place(mm("-0.2"), mm("-22.4"), rot=-90)
jp201.place(mm("-9.5"), mm("13"), rot=90)
led201.place(mm("-11.608"), mm("17.094"))
led202.place(mm("-11.608"), mm("21.158"))
led203.place(mm("-11.608"), mm("25.349"))
led204.place(mm("-11.608"), mm("29.54"))
led205.place(mm("4.14"), mm("38.176"), rot=90)
mcu_port201.place(mm("84.404"), mm("36.906"), rot=-90)
pulupen201.place(mm("65.227"), mm("17.983"), rot=-90)
r201.place(mm("-3.48"), mm("9.728"), rot=180)
r202.place(mm("-6.782"), mm("17.094"))
r203.place(mm("-6.782"), mm("21.158"))
r204.place(mm("-6.782"), mm("25.349"))
r205.place(mm("92.532"), mm("-17.704"), rot=90)
r206.place(mm("-6.782"), mm("29.413"))
r207.place(mm("5.41"), mm("33.858"))
r208.place(mm("64.592"), mm("-17.704"), rot=90)
r209.place(mm("-0.305"), mm("-14.529"), rot=180)
r210.place(mm("1.854"), mm("-7.163"))
r211.place(mm("65.354"), mm("25.476"), rot=90)
r212.place(mm("62.814"), mm("25.476"), rot=90)
r213.place(mm("60.274"), mm("25.476"), rot=90)
r214.place(mm("57.734"), mm("25.476"), rot=90)
r215.place(mm("27.889"), mm("-15.545"), rot=180)
rcan201.place(mm("-0.305"), mm("-9.957"))
rcan202.place(mm("-0.305"), mm("-12.243"))
rs201.place(mm("0.457"), mm("-4.242"), rot=-90)
sw201.place(mm("72.339"), mm("10.617"))
sw202.place(mm("72.466"), mm("22.301"))
sw_onoff201.place(mm("-10.5"), mm("-28.626"), rot=90)
tb201.place(mm("-24"), mm("-34.5"), rot=-90)
u201.place(mm("0.203"), mm("17.602"))
u202.place(mm("86.69"), mm("-22.149"))
u203.place(mm("58.75"), mm("-22.149"))
u204.place(mm("25.73"), mm("-22.149"))
u205.place(mm("5.918"), mm("-11.608"), rot=180)
uartcan201.place(mm("92.5"), mm("-33.5"), rot=180)
uartcan202.place(mm("56.5"), mm("-33.5"), rot=180)
uartcan203.place(mm("21.5"), mm("-33.5"), rot=180)
uart_en201.place(mm("97.485"), mm("-25.451"))
uart_en202.place(mm("69.545"), mm("-25.451"))
uart_en203.place(mm("35.763"), mm("-25.451"))
vr201.place(mm("-21.895"), mm("-11.735"), rot=90)
vref201.place(mm("-5"), mm("-13.5"), rot=-90)
vx_en201.place(mm("81.864"), mm("30.302"), rot=90)
abrt_sw101.place(mm("72.339"), mm("0.33"))
allpst101.place(mm("52.019"), mm("2.489"), rot=-90)
bdm_port101.place(mm("-23.673"), mm("6.299"))
c101.place(mm("60.401"), mm("5.537"))
c102.place(mm("41.732"), mm("12.395"), rot=-90)
c103.place(mm("43.891"), mm("12.395"), rot=-90)
c104.place(mm("60.401"), mm("11.252"), rot=180)
c105.place(mm("64.846"), mm("-5.639"), rot=90)
c106.place(mm("36.652"), mm("23.063"), rot=90)
c107.place(mm("36.652"), mm("17.729"), rot=-90)
c108.place(mm("20.777"), mm("6.045"), rot=90)
c109.place(mm("23.825"), mm("8.712"))
c110.place(mm("41.605"), mm("-8.941"), rot=180)
c111.place(mm("34.493"), mm("-8.56"), rot=180)
c112.place(mm("29.921"), mm("-8.56"), rot=180, side="bottom")
c113.place(mm("25.349"), mm("-0.178"), rot=-90)
c114.place(mm("24.587"), mm("3.505"), rot=180)
c115.place(mm("31.953"), mm("12.268"), rot=180)
c116.place(mm("37.668"), mm("11.76"), rot=180)
c117.place(mm("45.288"), mm("4.775"), rot=90, side="bottom")
c118.place(mm("45.415"), mm("-0.686"), rot=-90, side="bottom")
c119.place(mm("50.241"), mm("20.015"))
clkout101.place(mm("-16.561"), mm("34.239"), rot=-90)
ct101.place(mm("-8.56"), mm("34.62"), rot=-90)
fb101.place(mm("19.634"), mm("1.346"), rot=180)
gnd101.place(mm("-10.465"), mm("40.97"), rot=-90)
jp101.place(mm("12.522"), mm("-6.655"))
l101.place(mm("51.892"), mm("9.22"), rot=180)
l102.place(mm("18.999"), mm("10.236"))
ledabrt101.place(mm("64.846"), mm("0.457"), rot=90)
led_rst101.place(mm("64.846"), mm("-10.719"), rot=90)
lv101.place(mm("86.69"), mm("-10.592"))
q101.place(mm("61.798"), mm("-9.957"), rot=90)
r101.place(mm("4.267"), mm("-1.067"))
r102.place(mm("4.267"), mm("-3.353"))
r103.place(mm("64.846"), mm("5.41"), rot=-90)
r104.place(mm("63.957"), mm("12.268"), rot=-90)
r105.place(mm("60.401"), mm("14.046"), rot=180)
r106.place(mm("58.623"), mm("-5.131"), rot=90)
r107.place(mm("-16.688"), mm("4.267"), rot=180)
r108.place(mm("-16.688"), mm("6.553"), rot=180)
r109.place(mm("-16.688"), mm("19.126"), rot=180)
r110.place(mm("-16.688"), mm("21.412"), rot=180)
r111.place(mm("20.142"), mm("-2.718"), rot=180)
r112.place(mm("0.584"), mm("1.473"), rot=90)
r113.place(mm("41.478"), mm("-14.148"), rot=90)
r114.place(mm("34.874"), mm("13.411"), rot=-90)
r115.place(mm("58.623"), mm("-9.703"), rot=90)
r116.place(mm("61.544"), mm("-13.005"))
r117.place(mm("-15.164"), mm("13.792"), rot=-90)
r118.place(mm("83.769"), mm("21.158"), rot=180)
r119.place(mm("83.769"), mm("23.444"), rot=180)
r120.place(mm("53.035"), mm("-6.147"))
r121.place(mm("69.672"), mm("17.094"))
r122.place(mm("73.863"), mm("17.094"), rot=180)
r123.place(mm("53.035"), mm("-1.702"))
r124.place(mm("53.035"), mm("-3.988"))
r125.place(mm("28.27"), mm("21.285"), rot=90)
rst_sw101.place(mm("72.339"), mm("-10.211"), rot=180)
ta_101.place(mm("-16.561"), mm("38.557"), rot=-90)
u101.place(mm("60.528"), mm("8.331"))
u102.place(mm("35.382"), mm("1.473"), rot=-90)
vdda101.place(mm("12.014"), mm("8.458"), rot=90)
y101.place(mm("23.444"), mm("20.777"), rot=-90)
c301.place(mm("109.296"), mm("0.838"), rot=90, side="bottom")
c302.place(mm("91.008"), mm("7.315"), rot=180, side="bottom")
c303.place(mm("103.454"), mm("0.838"), rot=90, side="bottom")
c304.place(mm("108.28"), mm("10.49"), rot=-90, side="bottom")
c305.place(mm("101.422"), mm("23.444"), rot=-90, side="bottom")
c306.place(mm("108.28"), mm("19.38"), rot=-90, side="bottom")
c307.place(mm("90.5"), mm("-0.94"), rot=-90, side="bottom")
c308.place(mm("99.009"), mm("0.838"), rot=90, side="bottom")
c309.place(mm("105.359"), mm("23.444"), rot=-90, side="bottom")
c310.place(mm("97.485"), mm("23.444"), rot=-90, side="bottom")
c311.place(mm("91.008"), mm("15.189"), rot=180, side="bottom")
d301.place(mm("112.09"), mm("-23.165"), rot=180)
d302.place(mm("112.09"), mm("-19.355"), rot=180)
p301.place(mm("123.52"), mm("-36.5"))
p302.place(mm("97.5"), mm("-13"))
p303.place(mm("122.25"), mm("-11.1"))
r301.place(mm("118.25"), mm("-27"), rot=-90)
r302.place(mm("107.01"), mm("34.62"))
r303.place(mm("106.375"), mm("-23.165"))
r304.place(mm("106.375"), mm("-19.355"))
u301.place(mm("101.93"), mm("11.76"), rot=-90)

design.zone(
    net_3_3v,
    layers=("In2.Cu",),
    key="+3.3V/1",
    outline=(
        (mm("-27.5"), mm("45.5")),
        (mm("-28"), mm("-43")),
        (mm("127.5"), mm("-43")),
        (mm("127"), mm("45.5")),
    ),
    min_thickness=mm("0.3"),
    thermal_gap=mm("0.508"),
    thermal_spoke_width=mm("0.508"),
)
design.zone(
    gnd,
    layers=("B.Cu",),
    key="GND/1",
    outline=(
        (mm("-28.3"), mm("-43.7")),
        (mm("128.2"), mm("-43.7")),
        (mm("128.2"), mm("46.7")),
        (mm("-28.3"), mm("46.7")),
        (mm("-28.3"), mm("46.4")),
    ),
    clearance=mm("0.3"),
    thermal_gap=mm("0.381"),
    thermal_spoke_width=mm("0.381"),
)
design.zone(
    gnd,
    layers=("In1.Cu",),
    key="GND/2",
    outline=(
        (mm("-28.245"), mm("46.685")),
        (mm("127.33"), mm("46.05")),
        (mm("127.33"), mm("-43.485")),
        (mm("-2.845"), mm("-43.485")),
        (mm("-2.845"), mm("-25.07")),
        (mm("-20.625"), mm("-25.07")),
        (mm("-20.625"), mm("-28.88")),
        (mm("-28.245"), mm("-28.88")),
    ),
    min_thickness=mm("0.3"),
    thermal_gap=mm("0.508"),
    thermal_spoke_width=mm("0.508"),
)

design.text(
    "B.Cu/text/1",
    "CARTE COLDFIRE",
    (mm("113.995"), mm("-41.58")),
    layer="B.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)
design.text(
    "F.Cu/text/1",
    "JTAG_EN\n",
    (mm("8"), mm("-6.5")),
    layer="F.Cu",
    size=mm("1"),
    thickness=mm("0.2"),
)
design.text("F.Cu/text/2", "MOD1", (mm("9"), mm("-4")), layer="F.Cu", size=mm("1"), thickness=mm("0.2"))
design.text("F.Cu/text/3", "MOD0", (mm("9"), mm("-0.5")), layer="F.Cu", size=mm("1"), thickness=mm("0.2"))
design.text(
    "F.Cu/text/4",
    "CARTE COLDFIRE",
    (mm("113.995"), mm("-41.58")),
    layer="F.Cu",
    size=(mm("1.524"), mm("2.032")),
    thickness=mm("0.3048"),
)

copper.apply(
    design,
    {
        "+3.3V": net_3_3v,
        "/ALLPST": allpst,
        "/AN0": an0,
        "/AN1": an1,
        "/AN2": an2,
        "/AN3": an3,
        "/AN4": an4,
        "/AN5": an5,
        "/AN6": an6,
        "/AN7": an7,
        "/BKPT-": bkpt,
        "/CANRX": canrx,
        "/CANTX": cantx,
        "/CLKIN/EXTAL": clkin_extal,
        "/CLKMOD0": clkmod0,
        "/CLKMOD1": clkmod1,
        "/DDAT0": ddat0,
        "/DDAT1": ddat1,
        "/DDAT2": ddat2,
        "/DDAT3": ddat3,
        "/DSCLK": dsclk,
        "/DSI": dsi,
        "/DSO": dso,
        "/DSPI_DOUT": dspi_dout,
        "/DTIN0": dtin0,
        "/DTIN1": dtin1,
        "/DTIN2": dtin2,
        "/DTIN3": dtin3,
        "/GPT0": gpt0,
        "/GPT1": gpt1,
        "/GPT2": gpt2,
        "/GPT3": gpt3,
        "/IRQ-1": irq_1,
        "/IRQ-2": irq_2,
        "/IRQ-3": irq_3,
        "/IRQ-4": irq_4,
        "/IRQ-5": irq_5,
        "/IRQ-6": irq_6,
        "/IRQ-7": irq_7,
        "/JTAG_EN": jtag_en,
        "/PST0": pst0,
        "/PST1": pst1,
        "/PST2": pst2,
        "/PST3": pst3,
        "/PWM1": pwm1,
        "/PWM3": pwm3,
        "/PWM5": pwm5,
        "/PWM7": pwm7,
        "/QSPI_CLK": qspi_clk,
        "/QSPI_CS0": qspi_cs0,
        "/QSPI_CS1": qspi_cs1,
        "/QSPI_CS2": qspi_cs2,
        "/QSPI_CS3": qspi_cs3,
        "/QSPI_DIN": qspi_din,
        "/RCON-": rcon,
        "/RSTI-": rsti,
        "/RSTO-": rsto,
        "/TCLK": tclk,
        "/UCTS0": ucts0,
        "/UCTS1": ucts1,
        "/UCTS2": ucts2,
        "/URTS0": urts0,
        "/URTS1": urts1,
        "/URTS2": urts2,
        "/URXD0": urxd0,
        "/URXD1": urxd1,
        "/URXD2": urxd2,
        "/UTXD0": utxd0,
        "/UTXD1": utxd1,
        "/UTXD2": utxd2,
        "/VCCA": vcca,
        "/VDDPLL": vddpll,
        "/XTAL": xtal,
        "/inout_user/CAN_H": inout_user_can_h,
        "/inout_user/CAN_L": inout_user_can_l,
        "/inout_user/CTS0": inout_user_cts0,
        "/inout_user/CTS1": inout_user_cts1,
        "/inout_user/CTS2/CANH": inout_user_cts2_canh,
        "/inout_user/RTS0": inout_user_rts0,
        "/inout_user/RTS1": inout_user_rts1,
        "/inout_user/RTS2": inout_user_rts2,
        "/inout_user/RXD0": inout_user_rxd0,
        "/inout_user/RXD1": inout_user_rxd1,
        "/inout_user/RXD2": inout_user_rxd2,
        "/inout_user/RxD_CAN": inout_user_rxd_can,
        "/inout_user/TXD0": inout_user_txd0,
        "/inout_user/TXD1": inout_user_txd1,
        "/inout_user/TXD2/CANL": inout_user_txd2_canl,
        "/inout_user/TxD_CAN": inout_user_txd_can,
        "/xilinx/+3,3V_OUT": xilinx_3_3v_out,
        "/xilinx/LED_TEST1": xilinx_led_test1,
        "/xilinx/LED_TEST2": xilinx_led_test2,
        "/xilinx/TCK": xilinx_tck,
        "/xilinx/TDI": xilinx_tdi,
        "/xilinx/TDO": xilinx_tdo,
        "/xilinx/TMS": xilinx_tms,
        "/xilinx/XIL_D0": xilinx_xil_d0,
        "/xilinx/XIL_D1": xilinx_xil_d1,
        "/xilinx/XIL_D10": xilinx_xil_d10,
        "/xilinx/XIL_D11": xilinx_xil_d11,
        "/xilinx/XIL_D12": xilinx_xil_d12,
        "/xilinx/XIL_D13": xilinx_xil_d13,
        "/xilinx/XIL_D14": xilinx_xil_d14,
        "/xilinx/XIL_D15": xilinx_xil_d15,
        "/xilinx/XIL_D16": xilinx_xil_d16,
        "/xilinx/XIL_D17": xilinx_xil_d17,
        "/xilinx/XIL_D18": xilinx_xil_d18,
        "/xilinx/XIL_D19": xilinx_xil_d19,
        "/xilinx/XIL_D2": xilinx_xil_d2,
        "/xilinx/XIL_D20": xilinx_xil_d20,
        "/xilinx/XIL_D21": xilinx_xil_d21,
        "/xilinx/XIL_D22": xilinx_xil_d22,
        "/xilinx/XIL_D23": xilinx_xil_d23,
        "/xilinx/XIL_D24": xilinx_xil_d24,
        "/xilinx/XIL_D25": xilinx_xil_d25,
        "/xilinx/XIL_D26": xilinx_xil_d26,
        "/xilinx/XIL_D27": xilinx_xil_d27,
        "/xilinx/XIL_D28": xilinx_xil_d28,
        "/xilinx/XIL_D29": xilinx_xil_d29,
        "/xilinx/XIL_D3": xilinx_xil_d3,
        "/xilinx/XIL_D30": xilinx_xil_d30,
        "/xilinx/XIL_D31": xilinx_xil_d31,
        "/xilinx/XIL_D32": xilinx_xil_d32,
        "/xilinx/XIL_D33": xilinx_xil_d33,
        "/xilinx/XIL_D34": xilinx_xil_d34,
        "/xilinx/XIL_D35": xilinx_xil_d35,
        "/xilinx/XIL_D36": xilinx_xil_d36,
        "/xilinx/XIL_D4": xilinx_xil_d4,
        "/xilinx/XIL_D5": xilinx_xil_d5,
        "/xilinx/XIL_D6": xilinx_xil_d6,
        "/xilinx/XIL_D7": xilinx_xil_d7,
        "/xilinx/XIL_D8": xilinx_xil_d8,
        "/xilinx/XIL_D9": xilinx_xil_d9,
        "GND": gnd,
        "GNDA": gnda,
        "Net-(ABRT_SW101-Pad1)": net_abrt_sw101_pad1,
        "Net-(BDM_PORT101-P22-Pad26)": net_bdm_port101_p22_pad26,
        "Net-(BDM_PORT101-P6)": net_bdm_port101_p6,
        "Net-(C104-Pad1)": net_c104_pad1,
        "Net-(CAN_TERM201-Pad2)": net_can_term201_pad2,
        "Net-(COM_SEL201-P3)": net_com_sel201_p3,
        "Net-(COM_SEL202-P3)": net_com_sel202_p3,
        "Net-(COM_SEL203-P3)": net_com_sel203_p3,
        "Net-(D101-K)": net_d101_k,
        "Net-(D102-K)": net_d102_k,
        "Net-(D201-K)": net_d201_k,
        "Net-(D301-A)": net_d301_a,
        "Net-(D302-A)": net_d302_a,
        "Net-(F201-Pad1)": net_f201_pad1,
        "Net-(L102-Pad1)": net_l102_pad1,
        "Net-(LED201-A)": net_led201_a,
        "Net-(LED202-A)": net_led202_a,
        "Net-(LED203-A)": net_led203_a,
        "Net-(LED204-A)": net_led204_a,
        "Net-(LED205-A)": net_led205_a,
        "Net-(LEDABRT101-K)": net_ledabrt101_k,
        "Net-(LED_RST101-A)": net_led_rst101_a,
        "Net-(MCU_PORT201-P1)": net_mcu_port201_p1,
        "Net-(PULUPEN201-Pad2)": net_pulupen201_pad2,
        "Net-(PULUPEN201-Pad4)": net_pulupen201_pad4,
        "Net-(PULUPEN201-Pad6)": net_pulupen201_pad6,
        "Net-(PULUPEN201-Pad8)": net_pulupen201_pad8,
        "Net-(Q101-B)": net_q101_b,
        "Net-(Q101-C)": net_q101_c,
        "Net-(TB201-P1)": net_tb201_p1,
        "Net-(U102-TCLK/PSTCLK/CLKOUT)": net_u102_tclk_pstclk_clkout,
        "Net-(U102-TEST)": net_u102_test,
        "Net-(U201A-E)": net_u201a_e,
        "Net-(U201A-O)": net_u201a_o,
        "Net-(U201B-O)": net_u201b_o,
        "Net-(U201C-O)": net_u201c_o,
        "Net-(U201D-O)": net_u201d_o,
        "Net-(U202-C1+)": net_u202_c1,
        "Net-(U202-C1-)": net_u202_c1_2,
        "Net-(U202-C2+)": net_u202_c2,
        "Net-(U202-C2-)": net_u202_c2_2,
        "Net-(U202-R1OUT)": net_u202_r1out,
        "Net-(U202-R2OUT)": net_u202_r2out,
        "Net-(U202-T1IN)": net_u202_t1in,
        "Net-(U202-T2IN)": net_u202_t2in,
        "Net-(U202-V+)": net_u202_v,
        "Net-(U202-V-)": net_u202_v_2,
        "Net-(U203-C1+)": net_u203_c1,
        "Net-(U203-C1-)": net_u203_c1_2,
        "Net-(U203-C2+)": net_u203_c2,
        "Net-(U203-C2-)": net_u203_c2_2,
        "Net-(U203-R1OUT)": net_u203_r1out,
        "Net-(U203-R2OUT)": net_u203_r2out,
        "Net-(U203-T1IN)": net_u203_t1in,
        "Net-(U203-T2IN)": net_u203_t2in,
        "Net-(U203-V+)": net_u203_v,
        "Net-(U203-V-)": net_u203_v_2,
        "Net-(U204-C1+)": net_u204_c1,
        "Net-(U204-C1-)": net_u204_c1_2,
        "Net-(U204-C2+)": net_u204_c2,
        "Net-(U204-C2-)": net_u204_c2_2,
        "Net-(U204-R1OUT)": net_u204_r1out,
        "Net-(U204-R2OUT)": net_u204_r2out,
        "Net-(U204-T1IN)": net_u204_t1in,
        "Net-(U204-T2IN)": net_u204_t2in,
        "Net-(U204-V+)": net_u204_v,
        "Net-(U204-V-)": net_u204_v_2,
        "Net-(U205-Rsl)": net_u205_rsl,
        "Net-(U205-Vref)": net_u205_vref,
        "Net-(U301-P11)": net_u301_p11,
        "Net-(U301-P4)": net_u301_p4,
        "Net-(UARTCAN201-P6)": net_uartcan201_p6,
        "Net-(UARTCAN202-P6)": net_uartcan202_p6,
        "Net-(UARTCAN203-P6)": net_uartcan203_p6,
    },
)
