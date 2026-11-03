# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/kit-dev-coldfire-xilinx_5213@97acc80c223d75520c03fc44cab63cd9a3202c42 by Fenolite 0.7.0.dev0 on 2026-11-03;
# modified: format conversion to the Fenolite DSL.

import copper
from sheets import in_out_conn as _sheet_in_out_conn
from sheets import xilinx as _sheet_xilinx
from fenolite.dsl import Design, Net, Part, connect, mm, stack

design = Design("kit-dev-coldfire-xilinx_5213")

design.board(
    outline=(
        (mm("-28.88"), mm("-44.12")),
        (mm("128.6"), mm("-44.12")),
        (mm("128.6"), mm("47.32")),
        (mm("-28.88"), mm("47.32")),
    ),
    copper=4,
    technical_layers=(
        "F.Adhes",
        "B.Adhes",
        "F.Paste",
        "B.Paste",
        "F.SilkS",
        "B.SilkS",
        "F.Mask",
        "B.Mask",
        "Dwgs.User",
        "Cmts.User",
        "Edge.Cuts",
        "Margin",
        "F.CrtYd",
        "B.CrtYd",
        "F.Fab",
        "B.Fab",
    ),
    outline_width=mm("0.381"),
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
gnd = Net("GND")
gnda = Net("GNDA")
net_abrt_sw101_pad1 = Net("Net-(ABRT_SW101-Pad1)")
net_bdm_port101_p22_pad26 = Net("Net-(BDM_PORT101-P22-Pad26)")
net_bdm_port101_p6 = Net("Net-(BDM_PORT101-P6)")
net_c104_pad1 = Net("Net-(C104-Pad1)")
net_d101_k = Net("Net-(D101-K)")
net_d102_k = Net("Net-(D102-K)")
net_l102_pad1 = Net("Net-(L102-Pad1)")
net_ledabrt101_k = Net("Net-(LEDABRT101-K)")
net_led_rst101_a = Net("Net-(LED_RST101-A)")
net_q101_b = Net("Net-(Q101-B)")
net_q101_c = Net("Net-(Q101-C)")
net_u102_tclk_pstclk_clkout = Net("Net-(U102-TCLK/PSTCLK/CLKOUT)")
net_u102_test = Net("Net-(U102-TEST)")

abrt_sw101 = Part(
    "ABRT_SW101",
    "kit-dev-coldfire-xilinx_5213:SW_PUSH",
    footprint="kit-dev-coldfire:SW_PUSH_SMALL",
    value="SW_PUSH",
)
allpst101 = Part(
    "ALLPST101",
    "kit-dev-coldfire-xilinx_5213:CONN_1",
    footprint="Connector_PinHeader_2.54mm:PinHeader_1x01_P2.54mm_Vertical",
    value="CONN_1",
)
bdm_port101 = Part(
    "BDM_PORT101",
    "kit-dev-coldfire-xilinx_5213:CONN_13X2",
    footprint="Connector_PinHeader_2.54mm:PinHeader_2x13_P2.54mm_Vertical",
    value="CONN_13X2",
)
c101 = Part(
    "C101",
    "kit-dev-coldfire-xilinx_5213:C",
    footprint="Capacitor_SMD:C_0805_2012Metric",
    value="100nF",
)
c102 = Part(
    "C102",
    "kit-dev-coldfire-xilinx_5213:C",
    footprint="Capacitor_SMD:C_0805_2012Metric",
    footprint_definition="Capacitor_SMD:C_0805_2012Metric_2",
    value="1nF",
)
c103 = Part(
    "C103",
    "kit-dev-coldfire-xilinx_5213:C",
    footprint="Capacitor_SMD:C_0805_2012Metric",
    footprint_definition="Capacitor_SMD:C_0805_2012Metric_3",
    value="100nF",
)
c104 = Part(
    "C104",
    "kit-dev-coldfire-xilinx_5213:C",
    footprint="Capacitor_SMD:C_0805_2012Metric",
    footprint_definition="Capacitor_SMD:C_0805_2012Metric_4",
    value="100nF",
)
c105 = Part(
    "C105",
    "kit-dev-coldfire-xilinx_5213:C",
    footprint="Capacitor_SMD:C_0805_2012Metric",
    footprint_definition="Capacitor_SMD:C_0805_2012Metric_5",
    value="1nF",
)
c106 = Part(
    "C106",
    "kit-dev-coldfire-xilinx_5213:C",
    footprint="Capacitor_SMD:C_0805_2012Metric",
    footprint_definition="Capacitor_SMD:C_0805_2012Metric_6",
    value="10pF",
)
c107 = Part(
    "C107",
    "kit-dev-coldfire-xilinx_5213:C",
    footprint="Capacitor_SMD:C_0805_2012Metric",
    footprint_definition="Capacitor_SMD:C_0805_2012Metric_3",
    value="10pF",
)
c108 = Part("C108", "kit-dev-coldfire-xilinx_5213:CP", footprint="kit-dev-coldfire:SM1206POL", value="10uF")
c109 = Part(
    "C109",
    "kit-dev-coldfire-xilinx_5213:C",
    footprint="Capacitor_SMD:C_0805_2012Metric",
    footprint_definition="Capacitor_SMD:C_0805_2012Metric_7",
    value="100nF",
)
c110 = Part(
    "C110",
    "kit-dev-coldfire-xilinx_5213:C",
    footprint="Capacitor_SMD:C_0805_2012Metric",
    footprint_definition="Capacitor_SMD:C_0805_2012Metric_8",
    value="100nF",
)
c111 = Part(
    "C111",
    "kit-dev-coldfire-xilinx_5213:C",
    footprint="Capacitor_SMD:C_0805_2012Metric",
    footprint_definition="Capacitor_SMD:C_0805_2012Metric_9",
    value="100nF",
)
c112 = Part(
    "C112",
    "kit-dev-coldfire-xilinx_5213:C",
    footprint="Capacitor_SMD:C_0805_2012Metric",
    footprint_definition="Capacitor_SMD:C_0805_2012Metric_10",
    value="100nF",
)
c113 = Part(
    "C113",
    "kit-dev-coldfire-xilinx_5213:C",
    footprint="Capacitor_SMD:C_0805_2012Metric",
    footprint_definition="Capacitor_SMD:C_0805_2012Metric_11",
    value="100nF",
)
c114 = Part(
    "C114",
    "kit-dev-coldfire-xilinx_5213:C",
    footprint="Capacitor_SMD:C_0805_2012Metric",
    footprint_definition="Capacitor_SMD:C_0805_2012Metric_12",
    value="100nF",
)
c115 = Part(
    "C115",
    "kit-dev-coldfire-xilinx_5213:C",
    footprint="Capacitor_SMD:C_0805_2012Metric",
    footprint_definition="Capacitor_SMD:C_0805_2012Metric_12",
    value="100nF",
)
c116 = Part(
    "C116",
    "kit-dev-coldfire-xilinx_5213:C",
    footprint="Capacitor_SMD:C_0805_2012Metric",
    footprint_definition="Capacitor_SMD:C_0805_2012Metric_12",
    value="100nF",
)
c117 = Part(
    "C117",
    "kit-dev-coldfire-xilinx_5213:C",
    footprint="Capacitor_SMD:C_0805_2012Metric",
    footprint_definition="Capacitor_SMD:C_0805_2012Metric_13",
    value="100nF",
)
c118 = Part(
    "C118",
    "kit-dev-coldfire-xilinx_5213:C",
    footprint="Capacitor_SMD:C_0805_2012Metric",
    footprint_definition="Capacitor_SMD:C_0805_2012Metric_14",
    value="100nF",
)
c119 = Part(
    "C119",
    "kit-dev-coldfire-xilinx_5213:CP",
    footprint="kit-dev-coldfire:SM1206POL",
    footprint_definition="kit-dev-coldfire:SM1206POL_2",
    value="100uF",
)
clkout101 = Part(
    "CLKOUT101",
    "kit-dev-coldfire-xilinx_5213:CONN_1",
    footprint="Connector_PinHeader_2.54mm:PinHeader_1x01_P2.54mm_Vertical",
    value="CONN_1",
)
ct101 = Part(
    "CT101",
    "kit-dev-coldfire-xilinx_5213:JUMPER",
    footprint="Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical",
    footprint_definition="Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical_2",
    value="JUMPER",
)
d101 = Part(
    "D101",
    "kit-dev-coldfire-xilinx_5213:DIODE",
    footprint="kit-dev-coldfire:D_SOT-23_ANK",
    value="BAT54",
)
d102 = Part(
    "D102",
    "kit-dev-coldfire-xilinx_5213:DIODE",
    footprint="kit-dev-coldfire:D_SOT-23_ANK",
    value="BAT54",
)
fb101 = Part(
    "FB101",
    "kit-dev-coldfire-xilinx_5213:INDUCTOR",
    footprint="Resistor_SMD:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
    value="BEAD",
)
gnd101 = Part(
    "GND101",
    "kit-dev-coldfire-xilinx_5213:CONN_1",
    footprint="Connector_PinHeader_2.54mm:PinHeader_1x01_P2.54mm_Vertical",
    value="CONN_1",
)
jp101 = Part(
    "JP101",
    "kit-dev-coldfire-xilinx_5213:JUMPER_TRIPLE",
    footprint="Connector_PinHeader_2.54mm:PinHeader_2x03_P2.54mm_Vertical",
    value="JUMPER_TRIPLE",
)
l101 = Part(
    "L101",
    "kit-dev-coldfire-xilinx_5213:INDUCTOR",
    footprint="Resistor_SMD:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
    footprint_definition="Resistor_SMD:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
    value="10uH",
)
l102 = Part(
    "L102",
    "kit-dev-coldfire-xilinx_5213:INDUCTOR",
    footprint="Resistor_SMD:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
    footprint_definition="Resistor_SMD:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
    value="10uH",
)
ledabrt101 = Part(
    "LEDABRT101",
    "kit-dev-coldfire-xilinx_5213:LED",
    footprint="LED_SMD:LED_1206_3216Metric",
    footprint_definition="LED_SMD:LED_1206_3216Metric_5",
    value="LED_RED",
)
led_rst101 = Part(
    "LED_RST101",
    "kit-dev-coldfire-xilinx_5213:LED",
    footprint="LED_SMD:LED_1206_3216Metric",
    footprint_definition="LED_SMD:LED_1206_3216Metric_6",
    value="LED_RED",
)
lv101 = Part(
    "LV101",
    "kit-dev-coldfire-xilinx_5213:MC34064P",
    footprint="Package_TO_SOT_THT:TO-92",
    value="DS1818",
)
q101 = Part("Q101", "kit-dev-coldfire-xilinx_5213:PNP", footprint="kit-dev-coldfire:SOT23EBC", value="3906")
r101 = Part(
    "R101",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    value="4,7K",
)
r102 = Part(
    "R102",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_2",
    value="4,7K",
)
r103 = Part(
    "R103",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_3",
    value="270",
)
r104 = Part(
    "R104",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_3",
    value="1K",
)
r105 = Part(
    "R105",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_4",
    value="20K",
)
r106 = Part(
    "R106",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_5",
    value="4,7K",
)
r107 = Part(
    "R107",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_6",
    value="4,7K",
)
r108 = Part(
    "R108",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_6",
    value="4,7K",
)
r109 = Part(
    "R109",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_7",
    value="4,7K",
)
r110 = Part(
    "R110",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_8",
    value="4,7K",
)
r111 = Part(
    "R111",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_9",
    value="4,7K",
)
r112 = Part(
    "R112",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_10",
    value="4,7K",
)
r113 = Part(
    "R113",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_11",
    value="0",
)
r114 = Part(
    "R114",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_12",
    value="22",
)
r115 = Part(
    "R115",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_10",
    value="4.7K",
)
r116 = Part(
    "R116",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_13",
    value="270",
)
r117 = Part(
    "R117",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_14",
    value="10K",
)
r118 = Part(
    "R118",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_15",
    value="10K",
)
r119 = Part(
    "R119",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_6",
    value="10K",
)
r120 = Part(
    "R120",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_13",
    value="10K",
)
r121 = Part(
    "R121",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_13",
    value="10K",
)
r122 = Part(
    "R122",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_16",
    value="10K",
)
r123 = Part(
    "R123",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_17",
    value="10K",
)
r124 = Part(
    "R124",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_18",
    value="10K",
)
r125 = Part(
    "R125",
    "kit-dev-coldfire-xilinx_5213:R",
    footprint="Resistor_SMD:R_0805_2012Metric",
    footprint_definition="Resistor_SMD:R_0805_2012Metric_10",
    value="1M",
)
rst_sw101 = Part(
    "RST_SW101",
    "kit-dev-coldfire-xilinx_5213:SW_PUSH",
    footprint="kit-dev-coldfire:SW_PUSH_SMALL",
    footprint_definition="kit-dev-coldfire:SW_PUSH_SMALL_2",
    value="SW_PUSH",
)
ta_101 = Part(
    "TA-101",
    "kit-dev-coldfire-xilinx_5213:CONN_1",
    footprint="Connector_PinHeader_2.54mm:PinHeader_1x01_P2.54mm_Vertical",
    value="CONN_1",
)
u101 = Part(
    "U101",
    "kit-dev-coldfire-xilinx_5213:74AHC1G14",
    footprint="kit-dev-coldfire:SOT353",
    value="74AHC1G14",
)
u102 = Part(
    "U102",
    "kit-dev-coldfire-xilinx_5213:MCF5213-LQFP100",
    footprint="Package_QFP:LQFP-100_14x14mm_P0.5mm",
    value="MCF5213-LQFP100",
)
vdda101 = Part(
    "VDDA101",
    "kit-dev-coldfire-xilinx_5213:JUMPER",
    footprint="Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical",
    footprint_definition="Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical_4",
    value="JUMPER",
)
y101 = Part(
    "Y101",
    "kit-dev-coldfire-xilinx_5213:CRYSTAL",
    footprint="Crystal:Crystal_HC18-U_Horizontal",
    value="8MHz",
)

design.add(
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
    d101,
    d102,
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
_sheet_in_out_conn.sheet(
    design,
    path="inout_user",
    refs={
        "C201": "C201",
        "C202": "C202",
        "C203": "C203",
        "C204": "C204",
        "C205": "C205",
        "C206": "C206",
        "C207": "C207",
        "C208": "C208",
        "C209": "C209",
        "C210": "C210",
        "C211": "C211",
        "C212": "C212",
        "C213": "C213",
        "C214": "C214",
        "C215": "C215",
        "C216": "C216",
        "C217": "C217",
        "C218": "C218",
        "C219": "C219",
        "C220": "C220",
        "C221": "C221",
        "CAN_EN201": "CAN_EN201",
        "CAN_TERM201": "CAN_TERM201",
        "COM_SEL201": "COM_SEL201",
        "COM_SEL202": "COM_SEL202",
        "COM_SEL203": "COM_SEL203",
        "D201": "D201",
        "F201": "F201",
        "J201": "J201",
        "JP201": "JP201",
        "LED201": "LED201",
        "LED202": "LED202",
        "LED203": "LED203",
        "LED204": "LED204",
        "LED205": "LED205",
        "MCU_PORT201": "MCU_PORT201",
        "PULUPEN201": "PULUPEN201",
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
        "R214": "R214",
        "R215": "R215",
        "RCAN201": "RCAN201",
        "RCAN202": "RCAN202",
        "RS201": "RS201",
        "SW201": "SW201",
        "SW202": "SW202",
        "SW_ONOFF201": "SW_ONOFF201",
        "TB201": "TB201",
        "U201": "U201",
        "U202": "U202",
        "U203": "U203",
        "U204": "U204",
        "U205": "U205",
        "UARTCAN201": "UARTCAN201",
        "UARTCAN202": "UARTCAN202",
        "UARTCAN203": "UARTCAN203",
        "UART_EN201": "UART_EN201",
        "UART_EN202": "UART_EN202",
        "UART_EN203": "UART_EN203",
        "VR201": "VR201",
        "VREF201": "VREF201",
        "VX_EN201": "VX_EN201",
    },
    net_3_3v=net_3_3v,
    an0=an0,
    an1=an1,
    an2=an2,
    an3=an3,
    an4=an4,
    an5=an5,
    an6=an6,
    an7=an7,
    canrx=canrx,
    cantx=cantx,
    dspi_dout=dspi_dout,
    dtin0=dtin0,
    dtin1=dtin1,
    dtin2=dtin2,
    dtin3=dtin3,
    gpt0=gpt0,
    gpt1=gpt1,
    gpt2=gpt2,
    gpt3=gpt3,
    irq_1=irq_1,
    irq_2=irq_2,
    irq_3=irq_3,
    irq_4=irq_4,
    irq_5=irq_5,
    irq_6=irq_6,
    irq_7=irq_7,
    pwm1=pwm1,
    pwm3=pwm3,
    pwm5=pwm5,
    pwm7=pwm7,
    qspi_clk=qspi_clk,
    qspi_cs0=qspi_cs0,
    qspi_cs1=qspi_cs1,
    qspi_cs2=qspi_cs2,
    qspi_cs3=qspi_cs3,
    qspi_din=qspi_din,
    rcon=rcon,
    rsti=rsti,
    rsto=rsto,
    ucts0=ucts0,
    ucts1=ucts1,
    ucts2=ucts2,
    urts0=urts0,
    urts1=urts1,
    urts2=urts2,
    urxd0=urxd0,
    urxd1=urxd1,
    urxd2=urxd2,
    utxd0=utxd0,
    utxd1=utxd1,
    utxd2=utxd2,
    vcca=vcca,
    gnd=gnd,
    gnda=gnda,
)
_sheet_xilinx.sheet(
    design,
    path="xilinx",
    refs={
        "C301": "C301",
        "C302": "C302",
        "C303": "C303",
        "C304": "C304",
        "C305": "C305",
        "C306": "C306",
        "C307": "C307",
        "C308": "C308",
        "C309": "C309",
        "C310": "C310",
        "C311": "C311",
        "D301": "D301",
        "D302": "D302",
        "P301": "P301",
        "P302": "P302",
        "P303": "P303",
        "R301": "R301",
        "R302": "R302",
        "R303": "R303",
        "R304": "R304",
        "U301": "U301",
    },
    net_3_3v=net_3_3v,
    dspi_dout=dspi_dout,
    irq_1=irq_1,
    irq_2=irq_2,
    irq_3=irq_3,
    qspi_clk=qspi_clk,
    qspi_cs1=qspi_cs1,
    qspi_cs2=qspi_cs2,
    qspi_din=qspi_din,
    ucts1=ucts1,
    urts1=urts1,
    xtal=xtal,
    gnd=gnd,
)

inout_user_can_h = design.nets["/inout_user/CAN_H"]
inout_user_can_l = design.nets["/inout_user/CAN_L"]
inout_user_cts0 = design.nets["/inout_user/CTS0"]
inout_user_cts1 = design.nets["/inout_user/CTS1"]
inout_user_cts2_canh = design.nets["/inout_user/CTS2/CANH"]
inout_user_rts0 = design.nets["/inout_user/RTS0"]
inout_user_rts1 = design.nets["/inout_user/RTS1"]
inout_user_rts2 = design.nets["/inout_user/RTS2"]
inout_user_rxd0 = design.nets["/inout_user/RXD0"]
inout_user_rxd1 = design.nets["/inout_user/RXD1"]
inout_user_rxd2 = design.nets["/inout_user/RXD2"]
inout_user_rxd_can = design.nets["/inout_user/RxD_CAN"]
inout_user_txd0 = design.nets["/inout_user/TXD0"]
inout_user_txd1 = design.nets["/inout_user/TXD1"]
inout_user_txd2_canl = design.nets["/inout_user/TXD2/CANL"]
inout_user_txd_can = design.nets["/inout_user/TxD_CAN"]
xilinx_3_3v_out = design.nets["/xilinx/+3,3V_OUT"]
xilinx_led_test1 = design.nets["/xilinx/LED_TEST1"]
xilinx_led_test2 = design.nets["/xilinx/LED_TEST2"]
xilinx_tck = design.nets["/xilinx/TCK"]
xilinx_tdi = design.nets["/xilinx/TDI"]
xilinx_tdo = design.nets["/xilinx/TDO"]
xilinx_tms = design.nets["/xilinx/TMS"]
xilinx_xil_d0 = design.nets["/xilinx/XIL_D0"]
xilinx_xil_d1 = design.nets["/xilinx/XIL_D1"]
xilinx_xil_d10 = design.nets["/xilinx/XIL_D10"]
xilinx_xil_d11 = design.nets["/xilinx/XIL_D11"]
xilinx_xil_d12 = design.nets["/xilinx/XIL_D12"]
xilinx_xil_d13 = design.nets["/xilinx/XIL_D13"]
xilinx_xil_d14 = design.nets["/xilinx/XIL_D14"]
xilinx_xil_d15 = design.nets["/xilinx/XIL_D15"]
xilinx_xil_d16 = design.nets["/xilinx/XIL_D16"]
xilinx_xil_d17 = design.nets["/xilinx/XIL_D17"]
xilinx_xil_d18 = design.nets["/xilinx/XIL_D18"]
xilinx_xil_d19 = design.nets["/xilinx/XIL_D19"]
xilinx_xil_d2 = design.nets["/xilinx/XIL_D2"]
xilinx_xil_d20 = design.nets["/xilinx/XIL_D20"]
xilinx_xil_d21 = design.nets["/xilinx/XIL_D21"]
xilinx_xil_d22 = design.nets["/xilinx/XIL_D22"]
xilinx_xil_d23 = design.nets["/xilinx/XIL_D23"]
xilinx_xil_d24 = design.nets["/xilinx/XIL_D24"]
xilinx_xil_d25 = design.nets["/xilinx/XIL_D25"]
xilinx_xil_d26 = design.nets["/xilinx/XIL_D26"]
xilinx_xil_d27 = design.nets["/xilinx/XIL_D27"]
xilinx_xil_d28 = design.nets["/xilinx/XIL_D28"]
xilinx_xil_d29 = design.nets["/xilinx/XIL_D29"]
xilinx_xil_d3 = design.nets["/xilinx/XIL_D3"]
xilinx_xil_d30 = design.nets["/xilinx/XIL_D30"]
xilinx_xil_d31 = design.nets["/xilinx/XIL_D31"]
xilinx_xil_d32 = design.nets["/xilinx/XIL_D32"]
xilinx_xil_d33 = design.nets["/xilinx/XIL_D33"]
xilinx_xil_d34 = design.nets["/xilinx/XIL_D34"]
xilinx_xil_d35 = design.nets["/xilinx/XIL_D35"]
xilinx_xil_d36 = design.nets["/xilinx/XIL_D36"]
xilinx_xil_d4 = design.nets["/xilinx/XIL_D4"]
xilinx_xil_d5 = design.nets["/xilinx/XIL_D5"]
xilinx_xil_d6 = design.nets["/xilinx/XIL_D6"]
xilinx_xil_d7 = design.nets["/xilinx/XIL_D7"]
xilinx_xil_d8 = design.nets["/xilinx/XIL_D8"]
xilinx_xil_d9 = design.nets["/xilinx/XIL_D9"]
net_can_term201_pad2 = design.nets["Net-(CAN_TERM201-Pad2)"]
net_com_sel201_p3 = design.nets["Net-(COM_SEL201-P3)"]
net_com_sel202_p3 = design.nets["Net-(COM_SEL202-P3)"]
net_com_sel203_p3 = design.nets["Net-(COM_SEL203-P3)"]
net_d201_k = design.nets["Net-(D201-K)"]
net_d301_a = design.nets["Net-(D301-A)"]
net_d302_a = design.nets["Net-(D302-A)"]
net_f201_pad1 = design.nets["Net-(F201-Pad1)"]
net_led201_a = design.nets["Net-(LED201-A)"]
net_led202_a = design.nets["Net-(LED202-A)"]
net_led203_a = design.nets["Net-(LED203-A)"]
net_led204_a = design.nets["Net-(LED204-A)"]
net_led205_a = design.nets["Net-(LED205-A)"]
net_mcu_port201_p1 = design.nets["Net-(MCU_PORT201-P1)"]
net_pulupen201_pad2 = design.nets["Net-(PULUPEN201-Pad2)"]
net_pulupen201_pad4 = design.nets["Net-(PULUPEN201-Pad4)"]
net_pulupen201_pad6 = design.nets["Net-(PULUPEN201-Pad6)"]
net_pulupen201_pad8 = design.nets["Net-(PULUPEN201-Pad8)"]
net_tb201_p1 = design.nets["Net-(TB201-P1)"]
net_u201a_e = design.nets["Net-(U201A-E)"]
net_u201a_o = design.nets["Net-(U201A-O)"]
net_u201b_o = design.nets["Net-(U201B-O)"]
net_u201c_o = design.nets["Net-(U201C-O)"]
net_u201d_o = design.nets["Net-(U201D-O)"]
net_u202_c1 = design.nets["Net-(U202-C1+)"]
net_u202_c1_2 = design.nets["Net-(U202-C1-)"]
net_u202_c2 = design.nets["Net-(U202-C2+)"]
net_u202_c2_2 = design.nets["Net-(U202-C2-)"]
net_u202_r1out = design.nets["Net-(U202-R1OUT)"]
net_u202_r2out = design.nets["Net-(U202-R2OUT)"]
net_u202_t1in = design.nets["Net-(U202-T1IN)"]
net_u202_t2in = design.nets["Net-(U202-T2IN)"]
net_u202_v = design.nets["Net-(U202-V+)"]
net_u202_v_2 = design.nets["Net-(U202-V-)"]
net_u203_c1 = design.nets["Net-(U203-C1+)"]
net_u203_c1_2 = design.nets["Net-(U203-C1-)"]
net_u203_c2 = design.nets["Net-(U203-C2+)"]
net_u203_c2_2 = design.nets["Net-(U203-C2-)"]
net_u203_r1out = design.nets["Net-(U203-R1OUT)"]
net_u203_r2out = design.nets["Net-(U203-R2OUT)"]
net_u203_t1in = design.nets["Net-(U203-T1IN)"]
net_u203_t2in = design.nets["Net-(U203-T2IN)"]
net_u203_v = design.nets["Net-(U203-V+)"]
net_u203_v_2 = design.nets["Net-(U203-V-)"]
net_u204_c1 = design.nets["Net-(U204-C1+)"]
net_u204_c1_2 = design.nets["Net-(U204-C1-)"]
net_u204_c2 = design.nets["Net-(U204-C2+)"]
net_u204_c2_2 = design.nets["Net-(U204-C2-)"]
net_u204_r1out = design.nets["Net-(U204-R1OUT)"]
net_u204_r2out = design.nets["Net-(U204-R2OUT)"]
net_u204_t1in = design.nets["Net-(U204-T1IN)"]
net_u204_t2in = design.nets["Net-(U204-T2IN)"]
net_u204_v = design.nets["Net-(U204-V+)"]
net_u204_v_2 = design.nets["Net-(U204-V-)"]
net_u205_rsl = design.nets["Net-(U205-Rsl)"]
net_u205_vref = design.nets["Net-(U205-Vref)"]
net_u301_p11 = design.nets["Net-(U301-P11)"]
net_u301_p4 = design.nets["Net-(U301-P4)"]
net_uartcan201_p6 = design.nets["Net-(UARTCAN201-P6)"]
net_uartcan202_p6 = design.nets["Net-(UARTCAN202-P6)"]
net_uartcan203_p6 = design.nets["Net-(UARTCAN203-P6)"]

design.rules.netclass(
    "Default",
    clearance=mm("0.15"),
    track_width=mm("0.2"),
    via_diameter=mm("0.6"),
    via_drill=mm("0.4"),
    diff_pair_width=mm("0.2"),
    diff_pair_gap=mm("0.25"),
    diff_pair_via_gap=mm("0.25"),
    nets=(),
)
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

connect(
    net_3_3v,
    abrt_sw101["2"],
    bdm_port101["25"],
    bdm_port101["9"],
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
    l101["1"],
    ledabrt101["2"],
    lv101["2"],
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
    u101["5"],
    u102["1"],
    u102["14"],
    u102["2"],
    u102["22"],
    u102["23"],
    u102["34"],
    u102["41"],
    u102["55"],
    u102["57"],
    u102["68"],
    u102["81"],
    u102["93"],
    vdda101["1"],
)
connect(allpst, allpst101["1"], u102["86"])
connect(an0, u102["43"])
connect(an1, u102["44"])
connect(an2, u102["45"])
connect(an3, u102["46"])
connect(an4, u102["54"])
connect(an5, u102["53"])
connect(an6, u102["52"])
connect(an7, u102["51"])
connect(bkpt, bdm_port101["2"], r107["2"], u102["76"])
connect(canrx, u102["11"])
connect(cantx, u102["10"])
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
connect(dspi_dout, u102["17"])
connect(dtin0, u102["36"])
connect(dtin1, u102["37"])
connect(dtin2, u102["31"])
connect(dtin3, u102["32"])
connect(gpt0, u102["58"])
connect(gpt1, u102["59"])
connect(gpt2, u102["61"])
connect(gpt3, u102["62"])
connect(irq_1, r118["1"], u102["87"])
connect(irq_2, r119["1"], u102["88"])
connect(irq_3, r120["1"], u102["89"])
connect(irq_4, r121["1"], u102["90"])
connect(irq_5, r122["1"], u102["91"])
connect(irq_6, r123["1"], u102["94"])
connect(irq_7, d101["2"], r124["1"], u102["95"])
connect(jtag_en, jp101["2"], r111["2"], u102["26"])
connect(pst0, bdm_port101["15"], u102["65"])
connect(pst1, bdm_port101["14"], u102["66"])
connect(pst2, bdm_port101["13"], u102["69"])
connect(pst3, bdm_port101["12"], u102["70"])
connect(pwm1, u102["38"])
connect(pwm3, u102["33"])
connect(pwm5, u102["60"])
connect(pwm7, u102["63"])
connect(qspi_clk, u102["18"])
connect(qspi_cs0, u102["20"])
connect(qspi_cs1, u102["19"])
connect(qspi_cs2, u102["13"])
connect(qspi_cs3, u102["12"])
connect(qspi_din, u102["16"])
connect(rcon, r112["1"], u102["21"])
connect(rsti, bdm_port101["7"], d102["2"], r106["2"], u102["96"])
connect(rsto, r115["1"], u102["97"])
connect(tclk, bdm_port101["24"], clkout101["1"], ct101["2"], r114["2"], r117["1"])
connect(ucts0, u102["6"])
connect(ucts1, u102["98"])
connect(ucts2, u102["27"])
connect(urts0, u102["9"])
connect(urts1, u102["4"])
connect(urts2, u102["30"])
connect(urxd0, u102["7"])
connect(urxd1, u102["100"])
connect(urxd2, u102["28"])
connect(utxd0, u102["8"])
connect(utxd1, u102["99"])
connect(utxd2, u102["29"])
connect(vcca, c108["1"], c109["1"], l102["2"], u102["49"], u102["50"])
connect(vddpll, c102["1"], c103["1"], l101["2"], u102["74"])
connect(xtal, c106["1"], r125["1"], u102["72"], y101["2"])
connect(
    gnd,
    bdm_port101["11"],
    bdm_port101["20"],
    bdm_port101["23"],
    bdm_port101["3"],
    bdm_port101["5"],
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
    fb101["1"],
    gnd101["1"],
    jp101["1"],
    jp101["3"],
    jp101["5"],
    led_rst101["1"],
    lv101["3"],
    r105["2"],
    r113["2"],
    r117["2"],
    rst_sw101["2"],
    u101["3"],
    u102["15"],
    u102["24"],
    u102["25"],
    u102["3"],
    u102["35"],
    u102["42"],
    u102["56"],
    u102["67"],
    u102["71"],
    u102["75"],
    u102["82"],
    u102["92"],
)
connect(gnda, c108["2"], c109["2"], fb101["2"], u102["47"], u102["48"])
connect(net_abrt_sw101_pad1, abrt_sw101["1"], r104["1"])
connect(net_bdm_port101_p22_pad26, bdm_port101["26"], ta_101["1"])
connect(net_bdm_port101_p6, bdm_port101["6"], ct101["1"])
connect(net_c104_pad1, c104["1"], r104["2"], r105["1"], u101["2"])
connect(net_d101_k, d101["1"], r103["2"], u101["4"])
connect(net_d102_k, c105["1"], d102["1"], lv101["1"], rst_sw101["1"])
connect(net_l102_pad1, l102["1"], vdda101["2"])
connect(net_ledabrt101_k, ledabrt101["1"], r103["1"])
connect(net_led_rst101_a, led_rst101["2"], r116["2"])
connect(net_q101_b, q101["2"], r115["2"])
connect(net_q101_c, q101["3"], r116["1"])
connect(net_u102_tclk_pstclk_clkout, r114["1"], u102["64"])
connect(net_u102_test, r113["1"], u102["5"])

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
d101.place(mm("60.401"), mm("2.489"))
d102.place(mm("61.798"), mm("-4.369"))
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

design.load_schematic("schematic.toml")

design.kicad_project(
    "native/project.kicad_pro",
    sha256="d6ca906944730a3eae31ba3d9240c6966424b0d80ba76e80710e39d7b23c4637",
    preserve_minimums=True,
)
