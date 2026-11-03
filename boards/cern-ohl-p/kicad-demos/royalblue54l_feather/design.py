# SPDX-License-Identifier: CERN-OHL-P-2.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/royalblue54L_feather@97acc80c223d75520c03fc44cab63cd9a3202c42 by Fenolite 0.7.0.dev0 on 2026-10-31;
# modified: format conversion to the Fenolite DSL.

import copper
from fenolite.dsl import Design, Module, Net, Part, arc_to, connect, mm, stack

design = Design("RoyalBlue54L-Feather")

design.board(
    outline=(
        (mm("19.1"), mm("-3.91")),
        arc_to((mm("19.843949"), mm("-5.706051")), (mm("21.64"), mm("-6.45"))),
        (mm("74.98"), mm("-6.45")),
        arc_to((mm("76.776051"), mm("-5.706051")), (mm("77.52"), mm("-3.91"))),
        (mm("77.52"), mm("13.87")),
        arc_to((mm("76.776051"), mm("15.666051")), (mm("74.98"), mm("16.41"))),
        (mm("21.64"), mm("16.41")),
        arc_to((mm("19.843949"), mm("15.666051")), (mm("19.1"), mm("13.87"))),
    ),
    copper=8,
)
design.stackup(
    stack.silkscreen(color="White"),
    stack.mask(mm("0.01"), color="Blue"),
    stack.copper(mm("0.035")),
    stack.prepreg(mm("0.1"), material="FR4", epsilon_r="4.5", loss_tangent="0.02"),
    stack.copper(mm("0.035")),
    stack.core(mm("0.3"), material="FR4", epsilon_r="4.5", loss_tangent="0.02"),
    stack.copper(mm("0.035")),
    stack.prepreg(mm("0.1"), material="FR4", epsilon_r="4.5", loss_tangent="0.02"),
    stack.copper(mm("0.035")),
    stack.core(mm("0.3"), material="FR4", epsilon_r="4.5", loss_tangent="0.02"),
    stack.copper(mm("0.035")),
    stack.prepreg(mm("0.1"), material="FR4", epsilon_r="4.5", loss_tangent="0.02"),
    stack.copper(mm("0.035")),
    stack.core(mm("0.3"), material="FR4", epsilon_r="4.5", loss_tangent="0.02"),
    stack.copper(mm("0.035")),
    stack.prepreg(mm("0.1"), material="FR4", epsilon_r="4.5", loss_tangent="0.02"),
    stack.copper(mm("0.035")),
    stack.mask(mm("0.01"), color="Blue"),
    stack.silkscreen(color="White"),
    finish="ENIG",
)
design.title_block(date="2025-02-12")
design.user_layers(9)

batt = Net("+BATT")
connectors_analog_a0 = Net("/Connectors/ANALOG.A0")
connectors_analog_a1 = Net("/Connectors/ANALOG.A1")
connectors_analog_a2 = Net("/Connectors/ANALOG.A2")
connectors_analog_a3 = Net("/Connectors/ANALOG.A3")
connectors_analog_a4 = Net("/Connectors/ANALOG.A4")
connectors_analog_a5 = Net("/Connectors/ANALOG.A5")
connectors_dig_d10 = Net("/Connectors/DIG.D10")
connectors_dig_d11 = Net("/Connectors/DIG.D11")
connectors_dig_d12 = Net("/Connectors/DIG.D12")
connectors_dig_d13 = Net("/Connectors/DIG.D13")
connectors_dig_d5 = Net("/Connectors/DIG.D5")
connectors_dig_d6 = Net("/Connectors/DIG.D6")
connectors_dig_d9 = Net("/Connectors/DIG.D9")
connectors_enable = Net("/Connectors/ENABLE")
connectors_i2c_scl = Net("/Connectors/I2C.SCL")
connectors_i2c_sda = Net("/Connectors/I2C.SDA")
connectors_shphld = Net("/Connectors/SHPHLD")
connectors_spi_miso = Net("/Connectors/SPI.MISO")
connectors_spi_mosi = Net("/Connectors/SPI.MOSI")
connectors_spi_sck = Net("/Connectors/SPI.SCK")
connectors_uart_rx = Net("/Connectors/UART.RX")
connectors_uart_tx = Net("/Connectors/UART.TX")
debugger_d = Net("/Debugger/D+")
debugger_d_2 = Net("/Debugger/D-")
debugger_swd_trg_swdclk = Net("/Debugger/SWD_TRG.SWDCLK")
debugger_swd_trg_swdio = Net("/Debugger/SWD_TRG.SWDIO")
debugger_swd_trg_reset = Net("/Debugger/SWD_TRG.~{RESET}")
debugger_trg_swdclk_nrf52 = Net("/Debugger/TRG_SWDCLK_NRF52")
debugger_trg_swdio_nrf52 = Net("/Debugger/TRG_SWDIO_NRF52")
debugger_trg__reset__nrf52 = Net("/Debugger/TRG_~{RESET}_NRF52")
debugger_uart_rx_nrf52 = Net("/Debugger/UART_RX_NRF52")
debugger_uart_tx_nrf52 = Net("/Debugger/UART_TX_NRF52")
debugger_usb_cc1 = Net("/Debugger/USB.CC1")
debugger_usb_cc2 = Net("/Debugger/USB.CC2")
debugger_usb_vbus = Net("/Debugger/USB.VBUS")
debugger_nrf52_vdd = Net("/Debugger/nRF52_VDD")
npm1300_npm1300_int = Net("/nPM1300/NPM1300.INT")
npm1300_npm1300_scl = Net("/nPM1300/NPM1300.SCL")
npm1300_npm1300_sda = Net("/nPM1300/NPM1300.SDA")
nrf54l15_d2_flash = Net("/nRF54L15/D2_FLASH")
nrf54l15_d3_flash = Net("/nRF54L15/D3_FLASH")
nrf54l15_cs__flash = Net("/nRF54L15/~{CS}_FLASH")
gnd = Net("GND")
net_d1_a = Net("Net-(D1-A)")
net_d1_k = Net("Net-(D1-K)")
net_d3_bk = Net("Net-(D3-BK)")
net_d3_gk = Net("Net-(D3-GK)")
net_d3_rk = Net("Net-(D3-RK)")
net_j6_pin_2 = Net("Net-(J6-Pin_2)")
net_j6_pin_4 = Net("Net-(J6-Pin_4)")
net_j8_swclk = Net("Net-(J8-SWCLK)")
net_j8_swdio = Net("Net-(J8-SWDIO)")
net_j8_reset = Net("Net-(J8-~{RESET})")
net_jp1_a = Net("Net-(JP1-A)")
net_u1_p1_00_xl1 = Net("Net-(U1-P1.00/XL1)")
net_u1_p1_01_xl2 = Net("Net-(U1-P1.01/XL2)")
net_u2_sw2 = Net("Net-(U2-SW2)")
net_u2_vset2 = Net("Net-(U2-VSET2)")
net_u5_dec1 = Net("Net-(U5-DEC1)")
net_u5_dec3 = Net("Net-(U5-DEC3)")
net_u5_dec4 = Net("Net-(U5-DEC4)")
net_u5_decusb = Net("Net-(U5-DECUSB)")
net_u5_xc1 = Net("Net-(U5-XC1)")
net_u5_xc2 = Net("Net-(U5-XC2)")
vbus = Net("VBUS")
vdd = Net("VDD")
vsys = Net("VSYS")

design.rules.netclass(
    "USB_DIFF",
    clearance=mm("0.2032"),
    track_width=mm("0.125"),
    via_diameter=mm("0.8"),
    via_drill=mm("0.4"),
    diff_pair_width=mm("0.125"),
    diff_pair_gap=mm("0.2032"),
    nets=(debugger_d, debugger_d_2),
)
design.rules.minimum(
    clearance=mm("0.0762"),
    track_width=mm("0.0762"),
    via_diameter=mm("0.35"),
    hole_size=mm("0.2"),
    edge_clearance=mm("0.127"),
)

h1 = Part(
    "H1",
    "MountingHole:MountingHole_2.5mm",
    footprint="MountingHole:MountingHole_2.5mm",
    value="MountingHole",
    dnp=True,
)
h2 = Part(
    "H2",
    "MountingHole:MountingHole_2.5mm",
    footprint="MountingHole:MountingHole_2.5mm",
    value="MountingHole",
    dnp=True,
)
h3 = Part(
    "H3",
    "MountingHole:MountingHole_2.5mm",
    footprint="MountingHole:MountingHole_2.5mm",
    value="MountingHole",
    dnp=True,
)
h4 = Part(
    "H4",
    "MountingHole:MountingHole_2.5mm",
    footprint="MountingHole:MountingHole_2.5mm",
    value="MountingHole",
    dnp=True,
)
logo1 = Part(
    "LOGO1",
    "LordsBoards-Symbol:LordsBoardsLogo_Small_Silk",
    footprint="LordsBoards-Symbol:LordsBoardsLogo_Small_Silk",
    value="~",
    dnp=True,
)
j1 = Part(
    "J1",
    "RoyalBlue54L-Feather-Connector_PinHeader_2.54mm:PinHeader_1x16_P2.54mm_Vertical",
    footprint="RoyalBlue54L-Feather-Connector_PinHeader_2.54mm:PinHeader_1x16_P2.54mm_Vertical",
    value="Conn_01x16_Pin",
    dnp=True,
)
j2 = Part(
    "J2",
    "RoyalBlue54L-Feather-Connector_PinHeader_2.54mm:PinHeader_1x12_P2.54mm_Vertical",
    footprint="RoyalBlue54L-Feather-Connector_PinHeader_2.54mm:PinHeader_1x12_P2.54mm_Vertical",
    value="Conn_01x12_Pin",
    dnp=True,
)
j4 = Part(
    "J4",
    "Connector_JST:JST_PH_S2B-PH-SM4-TB_1x02-1MP_P2.00mm_Horizontal",
    footprint="Connector_JST:JST_PH_S2B-PH-SM4-TB_1x02-1MP_P2.00mm_Horizontal",
    value="Conn_01x02_MountingPin",
    properties={"LCSC": "C295747"},
)
j5 = Part(
    "J5",
    "Connector_JST:JST_SH_SM04B-SRSS-TB_1x04-1MP_P1.00mm_Horizontal",
    footprint="Connector_JST:JST_SH_SM04B-SRSS-TB_1x04-1MP_P1.00mm_Horizontal",
    value="Conn_01x04_MountingPin",
    properties={"LCSC": "C3029343"},
)
c7 = Part(
    "C7",
    "Capacitor_SMD:C_0402_1005Metric_6",
    footprint="Capacitor_SMD:C_0402_1005Metric_6",
    value="4.7uF",
    properties={"LCSC": "C23733"},
)
c10 = Part(
    "C10",
    "Capacitor_SMD:C_0402_1005Metric_2",
    footprint="Capacitor_SMD:C_0402_1005Metric_2",
    value="4.7uF",
    properties={"LCSC": "C23733"},
)
c15 = Part(
    "C15",
    "Capacitor_SMD:C_0402_1005Metric_3",
    footprint="Capacitor_SMD:C_0402_1005Metric_3",
    value="1uF",
    properties={"LCSC": "C52923"},
)
c16 = Part(
    "C16",
    "Capacitor_SMD:C_0402_1005Metric_4",
    footprint="Capacitor_SMD:C_0402_1005Metric_4",
    value="100nF",
    properties={"LCSC": "C307331"},
)
c17 = Part(
    "C17",
    "Capacitor_SMD:C_0402_1005Metric_4",
    footprint="Capacitor_SMD:C_0402_1005Metric_4",
    value="100nF",
    properties={"LCSC": "C307331"},
)
c18 = Part(
    "C18",
    "Capacitor_SMD:C_0402_1005Metric",
    footprint="Capacitor_SMD:C_0402_1005Metric",
    value="12pF",
    properties={"LCSC": "C1547"},
)
c19 = Part(
    "C19",
    "Capacitor_SMD:C_0402_1005Metric",
    footprint="Capacitor_SMD:C_0402_1005Metric",
    value="100nF",
    properties={"LCSC": "C307331"},
)
c20 = Part(
    "C20",
    "Capacitor_SMD:C_0402_1005Metric_3",
    footprint="Capacitor_SMD:C_0402_1005Metric_3",
    value="12pF",
    properties={"LCSC": "C1547"},
)
c21 = Part(
    "C21",
    "Capacitor_SMD:C_0402_1005Metric_4",
    footprint="Capacitor_SMD:C_0402_1005Metric_4",
    value="100pF",
    properties={"LCSC": "C1546"},
)
c22 = Part(
    "C22",
    "Capacitor_SMD:C_0402_1005Metric_4",
    footprint="Capacitor_SMD:C_0402_1005Metric_4",
    value="1uF",
    properties={"LCSC": "C52923"},
)
c23 = Part(
    "C23",
    "Capacitor_SMD:C_0402_1005Metric_3",
    footprint="Capacitor_SMD:C_0402_1005Metric_3",
    value="4.7uF",
    properties={"LCSC": "C23733"},
)
c24 = Part(
    "C24",
    "Capacitor_SMD:C_0402_1005Metric_5",
    footprint="Capacitor_SMD:C_0402_1005Metric_5",
    value="100nF",
    properties={"LCSC": "C307331"},
)
c25 = Part(
    "C25",
    "Capacitor_SMD:C_0402_1005Metric_3",
    footprint="Capacitor_SMD:C_0402_1005Metric_3",
    value="100nF",
    properties={"LCSC": "C307331"},
)
j3 = Part(
    "J3",
    "marbastlib-various:USB_C_Receptacle_HRO_TYPE-C-31-M-12",
    footprint="marbastlib-various:USB_C_Receptacle_HRO_TYPE-C-31-M-12",
    value="USB_C_Receptacle_USB2.0_16P",
    properties={"LCSC": "C165948"},
)
j8 = Part(
    "J8",
    "Connector:Tag-Connect_TC2030-IDC-NL_2x03_P1.27mm_Vertical",
    footprint="Connector:Tag-Connect_TC2030-IDC-NL_2x03_P1.27mm_Vertical",
    value="Conn_ARM_SWD_TagConnect_TC2030-NL",
    dnp=True,
)
r1 = Part(
    "R1",
    "Resistor_SMD:R_0402_1005Metric",
    footprint="Resistor_SMD:R_0402_1005Metric",
    value="100kR",
    properties={"LCSC": "C25741"},
)
r8 = Part(
    "R8",
    "Resistor_SMD:R_0402_1005Metric_5",
    footprint="Resistor_SMD:R_0402_1005Metric_5",
    value="100kR",
    properties={"LCSC": "C25741"},
)
tp5 = Part(
    "TP5",
    "TestPoint:TestPoint_Pad_D1.5mm_2",
    footprint="TestPoint:TestPoint_Pad_D1.5mm_2",
    value="TestPoint",
    dnp=True,
)
tp6 = Part(
    "TP6",
    "TestPoint:TestPoint_Pad_D1.5mm_2",
    footprint="TestPoint:TestPoint_Pad_D1.5mm_2",
    value="TestPoint",
    dnp=True,
)
tp7 = Part(
    "TP7",
    "TestPoint:TestPoint_Pad_D1.5mm_3",
    footprint="TestPoint:TestPoint_Pad_D1.5mm_3",
    value="TestPoint",
    dnp=True,
)
tp8 = Part(
    "TP8",
    "TestPoint:TestPoint_Pad_D1.5mm_3",
    footprint="TestPoint:TestPoint_Pad_D1.5mm_3",
    value="TestPoint",
    dnp=True,
)
tp9 = Part(
    "TP9",
    "TestPoint:TestPoint_Pad_D1.5mm",
    footprint="TestPoint:TestPoint_Pad_D1.5mm",
    value="TestPoint",
    dnp=True,
)
tp10 = Part(
    "TP10",
    "TestPoint:TestPoint_Pad_D1.5mm",
    footprint="TestPoint:TestPoint_Pad_D1.5mm",
    value="TestPoint",
    dnp=True,
)
tp11 = Part(
    "TP11",
    "TestPoint:TestPoint_Pad_D1.5mm",
    footprint="TestPoint:TestPoint_Pad_D1.5mm",
    value="TestPoint",
    dnp=True,
)
tp12 = Part(
    "TP12",
    "TestPoint:TestPoint_Pad_D1.5mm",
    footprint="TestPoint:TestPoint_Pad_D1.5mm",
    value="TestPoint",
    dnp=True,
)
u3 = Part(
    "U3",
    "Package_TO_SOT_SMD:SOT-553",
    footprint="Package_TO_SOT_SMD:SOT-553",
    value="TPD3E001DRLR",
    properties={"LCSC": "C2999113"},
)
u5 = Part(
    "U5",
    "Package_DFN_QFN:QFN-40-1EP_5x5mm_P0.4mm_EP3.6x3.6mm_ThermalVias",
    footprint="Package_DFN_QFN:QFN-40-1EP_5x5mm_P0.4mm_EP3.6x3.6mm_ThermalVias",
    value="nRF52833-QDXX",
    properties={"LCSC": "C2895249"},
)
u6 = Part(
    "U6",
    "Package_DFN_QFN:Texas_RGY_R-PVQFN-N16_EP2.05x2.55mm",
    footprint="Package_DFN_QFN:Texas_RGY_R-PVQFN-N16_EP2.05x2.55mm",
    value="TXB0106RGY",
    properties={"LCSC": "C2652978"},
)
y2 = Part(
    "Y2",
    "Crystal:Crystal_SMD_2016-4Pin_2.0x1.6mm",
    footprint="Crystal:Crystal_SMD_2016-4Pin_2.0x1.6mm",
    value="32MHz",
    properties={"LCSC": "C2682773"},
)
c1 = Part(
    "C1",
    "Capacitor_SMD:C_0402_1005Metric",
    footprint="Capacitor_SMD:C_0402_1005Metric",
    value="100nF",
    properties={"LCSC": "C307331"},
)
c2 = Part(
    "C2",
    "Capacitor_SMD:C_0603_1608Metric_2",
    footprint="Capacitor_SMD:C_0603_1608Metric_2",
    value="10uF",
    properties={"LCSC": "C96446"},
)
c3 = Part(
    "C3",
    "Capacitor_SMD:C_0603_1608Metric_3",
    footprint="Capacitor_SMD:C_0603_1608Metric_3",
    value="10uF",
    properties={"LCSC": "C96446"},
)
c4 = Part(
    "C4",
    "Capacitor_SMD:C_0603_1608Metric_4",
    footprint="Capacitor_SMD:C_0603_1608Metric_4",
    value="10uF",
    properties={"LCSC": "C96446"},
)
c5 = Part(
    "C5",
    "Capacitor_SMD:C_0603_1608Metric_4",
    footprint="Capacitor_SMD:C_0603_1608Metric_4",
    value="1uF",
    properties={"LCSC": "C15849"},
)
c6 = Part(
    "C6",
    "Capacitor_SMD:C_0603_1608Metric_4",
    footprint="Capacitor_SMD:C_0603_1608Metric_4",
    value="1uF",
    properties={"LCSC": "C15849"},
)
c8 = Part(
    "C8",
    "Capacitor_SMD:C_0603_1608Metric_4",
    footprint="Capacitor_SMD:C_0603_1608Metric_4",
    value="10uF",
    properties={"LCSC": "C96446"},
)
c11 = Part(
    "C11",
    "Capacitor_SMD:C_0603_1608Metric",
    footprint="Capacitor_SMD:C_0603_1608Metric",
    value="2.2uF",
    properties={"LCSC": "C23630"},
)
d3 = Part(
    "D3",
    "LED_SMD:LED_Wurth_150044M155260",
    footprint="LED_SMD:LED_Wurth_150044M155260",
    value="LED_ARGB",
    properties={"LCSC": "C404280"},
)
jp1 = Part(
    "JP1",
    "Jumper:SolderJumper-2_P1.3mm_Bridged_RoundedPad1.0x1.5mm",
    footprint="Jumper:SolderJumper-2_P1.3mm_Bridged_RoundedPad1.0x1.5mm",
    value="SolderJumper_2_Bridged",
)
l1 = Part(
    "L1",
    "Inductor_SMD:L_0603_1608Metric",
    footprint="Inductor_SMD:L_0603_1608Metric",
    value="2.2uH",
    properties={"LCSC": "C337910"},
)
r4 = Part(
    "R4",
    "Resistor_SMD:R_0402_1005Metric_3",
    footprint="Resistor_SMD:R_0402_1005Metric_3",
    value="330kR",
    properties={"LCSC": "C25778"},
)
u2 = Part(
    "U2",
    "Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.6x3.6mm_ThermalVias",
    footprint="Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.6x3.6mm_ThermalVias",
    value="nPM1300-QEXX",
    properties={"LCSC": "C7466043"},
)
c9 = Part(
    "C9",
    "Capacitor_SMD:C_0402_1005Metric_5",
    footprint="Capacitor_SMD:C_0402_1005Metric_5",
    value="4.7uF",
    properties={"LCSC": "C23733"},
)
c12 = Part(
    "C12",
    "Capacitor_SMD:C_0402_1005Metric",
    footprint="Capacitor_SMD:C_0402_1005Metric",
    value="100nF",
    properties={"LCSC": "C307331"},
)
c13 = Part(
    "C13",
    "Capacitor_SMD:C_0402_1005Metric_3",
    footprint="Capacitor_SMD:C_0402_1005Metric_3",
    value="300pF",
    properties={"LCSC": "C126505"},
)
c14 = Part(
    "C14",
    "Capacitor_SMD:C_0402_1005Metric_4",
    footprint="Capacitor_SMD:C_0402_1005Metric_4",
    value="300pF",
    properties={"LCSC": "C126505"},
)
d1 = Part(
    "D1",
    "LED_SMD:LED_0603_1608Metric",
    footprint="LED_SMD:LED_0603_1608Metric",
    value="LED_Small",
    properties={"LCSC": "C125103", "Sim.Pin": "1=K 2=A"},
)
j6 = Part(
    "J6",
    "RoyalBlue54L-Feather-Connector_FFC-FPC:CONN-SMD_5P-P0.50_HCTL_HC-FPC-05-09-5RLTAG",
    footprint="RoyalBlue54L-Feather-Connector_FFC-FPC:CONN-SMD_5P-P0.50_HCTL_HC-FPC-05-09-5RLTAG",
    value="Conn_01x05_MountingPin",
    properties={"LCSC": "C5213747"},
)
r2 = Part(
    "R2",
    "Resistor_SMD:R_0402_1005Metric_2",
    footprint="Resistor_SMD:R_0402_1005Metric_2",
    value="10kR",
    properties={"LCSC": "C25744"},
    dnp=True,
)
r3 = Part(
    "R3",
    "Resistor_SMD:R_0402_1005Metric_2",
    footprint="Resistor_SMD:R_0402_1005Metric_2",
    value="10kR",
    properties={"LCSC": "C25744"},
    dnp=True,
)
r5 = Part(
    "R5",
    "Resistor_SMD:R_0402_1005Metric_4",
    footprint="Resistor_SMD:R_0402_1005Metric_4",
    value="10kR",
    properties={"LCSC": "C25744"},
)
r6 = Part(
    "R6",
    "Resistor_SMD:R_0402_1005Metric",
    footprint="Resistor_SMD:R_0402_1005Metric",
    value="470R",
    properties={"LCSC": "C25117"},
)
r7 = Part(
    "R7",
    "Resistor_SMD:R_0402_1005Metric_4",
    footprint="Resistor_SMD:R_0402_1005Metric_4",
    value="10kR",
    properties={"LCSC": "C25744"},
)
sw1 = Part(
    "SW1",
    "Button_Switch_SMD:SW_Push_1P1T_NO_Vertical_Wuerth_434133025816",
    footprint="Button_Switch_SMD:SW_Push_1P1T_NO_Vertical_Wuerth_434133025816",
    value="SW_Push",
    properties={"LCSC": "C139797"},
)
sw2 = Part(
    "SW2",
    "Button_Switch_SMD:SW_Push_1P1T_NO_Vertical_Wuerth_434133025816_2",
    footprint="Button_Switch_SMD:SW_Push_1P1T_NO_Vertical_Wuerth_434133025816_2",
    value="SW_Push",
    properties={"LCSC": "C139797"},
)
tp1 = Part(
    "TP1",
    "TestPoint:TestPoint_Pad_D2.0mm",
    footprint="TestPoint:TestPoint_Pad_D2.0mm",
    value="TestPoint",
    dnp=True,
)
tp2 = Part(
    "TP2",
    "TestPoint:TestPoint_Pad_D2.0mm",
    footprint="TestPoint:TestPoint_Pad_D2.0mm",
    value="TestPoint",
    dnp=True,
)
tp3 = Part(
    "TP3",
    "TestPoint:TestPoint_Pad_D2.0mm",
    footprint="TestPoint:TestPoint_Pad_D2.0mm",
    value="TestPoint",
    dnp=True,
)
tp4 = Part(
    "TP4",
    "TestPoint:TestPoint_Pad_D2.0mm_2",
    footprint="TestPoint:TestPoint_Pad_D2.0mm_2",
    value="TestPoint",
    dnp=True,
)
u1 = Part(
    "U1",
    "nordic-lib-kicad-nrf54-modules:BM15x-LGA-45_15.8x10mm",
    footprint="nordic-lib-kicad-nrf54-modules:BM15x-LGA-45_15.8x10mm",
    value="BM15x",
    properties={"LCSC": "C9900148376"},
)
u4 = Part(
    "U4",
    "Package_SON:Winbond_USON-8-1EP_3x2mm_P0.5mm_EP0.2x1.6mm",
    footprint="Package_SON:Winbond_USON-8-1EP_3x2mm_P0.5mm_EP0.2x1.6mm",
    value="W25Q16JVUXIQ",
    properties={"LCSC": "C2843335"},
)
y1 = Part(
    "Y1",
    "Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm",
    footprint="Crystal:Crystal_SMD_3215-2Pin_3.2x1.5mm",
    value="32.768KHz",
    properties={"LCSC": "C32346"},
)

connectors = Module("connectors")
debugger = Module("debugger")
npm1300 = Module("npm1300")
nrf54l15 = Module("nrf54l15")

connectors.add(j1, j2, j4, j5)
debugger.add(
    c7,
    c10,
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
    j3,
    j8,
    r1,
    r8,
    tp5,
    tp6,
    tp7,
    tp8,
    tp9,
    tp10,
    tp11,
    tp12,
    u3,
    u5,
    u6,
    y2,
)
npm1300.add(c1, c2, c3, c4, c5, c6, c8, c11, d3, jp1, l1, r4, u2)
nrf54l15.add(c9, c12, c13, c14, d1, j6, r2, r3, r5, r6, r7, sw1, sw2, tp1, tp2, tp3, tp4, u1, u4, y1)
design.add(h1, h2, h3, h4, logo1, connectors, debugger, npm1300, nrf54l15)

connect(batt, c11["1"], j2["1"], j4["1"], u2["19"])
connect(connectors_analog_a0, j1["5"], u1["E9"])
connect(connectors_analog_a1, j1["6"], u1["F8"])
connect(connectors_analog_a2, j1["7"], u1["F9"])
connect(connectors_analog_a3, j1["8"], u1["G9"])
connect(connectors_analog_a4, j1["9"], u1["B4"])
connect(connectors_analog_a5, j1["10"], u1["B5"])
connect(connectors_dig_d10, j2["7"], u1["K6"])
connect(connectors_dig_d11, j2["6"], sw2["1"], u1["J4"])
connect(connectors_dig_d12, j2["5"], u1["J5"])
connect(connectors_dig_d13, j2["4"], u1["J6"])
connect(connectors_dig_d5, j2["10"], u1["B6"])
connect(connectors_dig_d6, j2["9"], u1["K4"])
connect(connectors_dig_d9, j2["8"], u1["K5"])
connect(connectors_enable, j2["2"], u2["8"])
connect(connectors_i2c_scl, j2["11"], j5["4"], r2["2"], u1["G8"])
connect(connectors_i2c_sda, j2["12"], j5["3"], r3["2"], u1["B3"])
connect(connectors_shphld, j1["16"], u2["15"])
connect(connectors_spi_miso, j1["13"], u1["K9"], u4["2"])
connect(connectors_spi_mosi, j1["12"], u1["J8"], u4["5"])
connect(connectors_spi_sck, j1["11"], u1["J9"], u4["6"])
connect(connectors_uart_rx, j1["14"], u1["A3"], u6["14"])
connect(connectors_uart_tx, j1["15"], u1["B2"], u6["13"])
connect(debugger_d, j3["A6"], j3["B6"], tp7["1"], u3["4"], u5["13"])
connect(debugger_d_2, j3["A7"], j3["B7"], tp8["1"], u3["2"], u5["12"])
connect(debugger_swd_trg_swdclk, tp3["1"], u1["K3"], u6["10"])
connect(debugger_swd_trg_swdio, tp1["1"], u1["J3"], u6["11"])
connect(debugger_swd_trg_reset, j1["1"], sw1["2"], tp2["1"], u1["G2"], u6["12"])
connect(debugger_trg_swdclk_nrf52, u5["32"], u6["7"])
connect(debugger_trg_swdio_nrf52, u5["33"], u6["6"])
connect(debugger_trg__reset__nrf52, r8["2"], u5["34"], u6["5"])
connect(debugger_uart_rx_nrf52, u5["36"], u6["3"])
connect(debugger_uart_tx_nrf52, u5["35"], u6["4"])
connect(debugger_usb_cc1, j3["A5"], u2["23"])
connect(debugger_usb_cc2, j3["B5"], tp6["1"], u2["24"])
connect(debugger_usb_vbus, c5["1"], j3["A4"], j3["A9"], j3["B4"], j3["B9"], tp5["1"], u2["21"], u3["5"])
connect(
    debugger_nrf52_vdd,
    c10["1"],
    c15["1"],
    c16["1"],
    c17["1"],
    c25["1"],
    j8["1"],
    r1["1"],
    r8["1"],
    tp9["1"],
    u5["8"],
    u5["18"],
    u5["30"],
    u5["40"],
    u6["2"],
    u6["8"],
)
connect(npm1300_npm1300_int, u1["K2"], u2["7"])
connect(npm1300_npm1300_scl, r5["2"], u1["J2"], u2["14"])
connect(npm1300_npm1300_sda, r7["2"], u1["H2"], u2["13"])
connect(nrf54l15_d2_flash, u1["J7"], u4["3"])
connect(nrf54l15_d3_flash, u1["H9"], u4["7"])
connect(nrf54l15_cs__flash, u1["K8"], u4["1"])
connect(
    gnd,
    c1["2"],
    c2["2"],
    c3["2"],
    c4["2"],
    c5["2"],
    c6["2"],
    c7["2"],
    c8["2"],
    c9["2"],
    c10["2"],
    c11["2"],
    c12["2"],
    c13["2"],
    c14["2"],
    c15["2"],
    c16["2"],
    c17["2"],
    c18["1"],
    c19["2"],
    c20["1"],
    c21["2"],
    c22["2"],
    c23["2"],
    c24["2"],
    c25["2"],
    j1["4"],
    j3["A1"],
    j3["A12"],
    j3["B1"],
    j3["B12"],
    j3["S1"],
    j4["2"],
    j4["MP"],
    j5["1"],
    j5["MP"],
    j6["MP"],
    j8["5"],
    r1["2"],
    r4["2"],
    r6["2"],
    sw1["1"],
    sw2["2"],
    tp4["1"],
    u1["A1"],
    u1["A9"],
    u1["B1"],
    u1["B7"],
    u1["B9"],
    u1["D1"],
    u1["E1"],
    u1["F1"],
    u1["H8"],
    u2["2"],
    u2["6"],
    u2["17"],
    u2["18"],
    u2["28"],
    u2["29"],
    u2["30"],
    u2["31"],
    u2["33"],
    u3["3"],
    u4["4"],
    u4["9"],
    u5["25"],
    u5["37"],
    u5["41"],
    u6["1"],
    u6["9"],
    u6["16"],
    u6["17"],
    y2["2"],
    y2["4"],
)
connect(net_d1_a, d1["2"], u1["K7"])
connect(net_d1_k, d1["1"], r6["1"])
connect(net_d3_bk, d3["4"], u2["27"])
connect(net_d3_gk, d3["3"], u2["26"])
connect(net_d3_rk, d3["2"], u2["25"])
connect(net_j6_pin_2, c14["1"], j6["2"], u1["D9"])
connect(net_j6_pin_4, c13["1"], j6["4"], u1["E8"])
connect(net_j8_swclk, j8["4"], tp11["1"], u5["20"])
connect(net_j8_swdio, j8["2"], tp12["1"], u5["19"])
connect(net_j8_reset, j8["3"], tp10["1"], u5["16"])
connect(net_jp1_a, c8["1"], jp1["1"], l1["1"], u2["32"])
connect(net_u1_p1_00_xl1, u1["D8"], y1["2"])
connect(net_u1_p1_01_xl2, u1["C9"], y1["1"])
connect(net_u2_sw2, l1["2"], u2["5"])
connect(net_u2_vset2, r4["1"], u2["16"])
connect(net_u5_dec1, c19["1"], u5["1"])
connect(net_u5_dec3, c21["1"], u5["27"])
connect(net_u5_dec4, c22["1"], u5["26"], u5["38"])
connect(net_u5_decusb, c23["1"], u5["11"])
connect(net_u5_xc1, c18["2"], u5["28"], y2["1"])
connect(net_u5_xc2, c20["2"], u5["29"], y2["3"])
connect(vbus, c6["1"], c7["1"], u2["22"], u5["9"], u5["10"])
connect(
    vdd,
    c1["1"],
    c9["1"],
    c12["1"],
    c24["1"],
    j1["2"],
    j5["2"],
    jp1["2"],
    r2["1"],
    r3["1"],
    r5["1"],
    r7["1"],
    u1["B8"],
    u1["C8"],
    u2["12"],
    u4["8"],
    u6["15"],
)
connect(vsys, c2["1"], c3["1"], c4["1"], d3["1"], j2["3"], u2["1"], u2["4"], u2["20"])

h1.place(mm("21.64"), mm("-3.91"), locked=True)
h2.place(mm("74.98"), mm("-3.91"), locked=True)
h3.place(mm("21.64"), mm("13.87"), locked=True)
h4.place(mm("74.98"), mm("13.87"), locked=True)
logo1.place(mm("30.223897"), mm("1.8175"), rot=90)
j1.place(mm("33.07"), mm("15.14"), rot=-90, side="bottom", locked=True)
j2.place(mm("43.23"), mm("-5.18"), rot=90)
j4.place(mm("36.88"), mm("-1.542"), rot=180, locked=True)
j5.place(mm("27.99"), mm("-3.367"), rot=180, locked=True)
c7.place(mm("40.44"), mm("5.94"), rot=90)
c10.place(mm("40.44"), mm("7.76"), rot=-90)
c15.place(mm("39.07"), mm("11.69"))
c16.place(mm("33.96"), mm("11.71"), rot=180)
c17.place(mm("35.39"), mm("4.4"), rot=180)
c18.place(mm("29.93"), mm("9.3"), rot=-90)
c19.place(mm("40.44"), mm("10.53"), rot=-90)
c20.place(mm("31.69"), mm("12.06"))
c21.place(mm("32.3"), mm("7.74"), rot=180)
c22.place(mm("32.78"), mm("6.78"), rot=180)
c23.place(mm("39.4"), mm("4.57"))
c24.place(mm("58.06"), mm("2.94"), rot=90)
c25.place(mm("53.71"), mm("1.81"))
j3.place(mm("21.36"), mm("4.98"), rot=-90)
j8.place(mm("28.61"), mm("4.9725"), rot=90, side="bottom")
r1.place(mm("55.76"), mm("8.04"))
r8.place(mm("43.11"), mm("7.52"), rot=-90)
tp5.place(mm("22.3"), mm("1.38"), rot=-90, side="bottom")
tp6.place(mm("22.3"), mm("8.58"), rot=-90, side="bottom")
tp7.place(mm("22.4"), mm("6.18"), rot=90, side="bottom")
tp8.place(mm("22.4"), mm("3.78"), rot=90, side="bottom")
tp9.place(mm("39.1"), mm("-0.02"), rot=180, side="bottom")
tp10.place(mm("36.7"), mm("-0.02"), rot=180, side="bottom")
tp11.place(mm("39.1"), mm("2.38"), rot=180, side="bottom")
tp12.place(mm("36.7"), mm("2.38"), rot=180, side="bottom")
u3.place(mm("28.61"), mm("4.9725"))
u5.place(mm("36.88"), mm("8.13"), rot=180)
u6.place(mm("55.2"), mm("4.92"))
y2.place(mm("31.69"), mm("10.2"), rot=-90)
c1.place(mm("51.14"), mm("5.69"), rot=-90)
c2.place(mm("48.86"), mm("8.67"))
c3.place(mm("45.84"), mm("8.67"), rot=180)
c4.place(mm("48.58"), mm("-1.18"), rot=90)
c5.place(mm("47.01"), mm("-1.18"), rot=90)
c6.place(mm("44.88"), mm("-1.18"), rot=90)
c8.place(mm("50.37"), mm("10.93"), rot=90)
c11.place(mm("50.82"), mm("0.59"))
d3.place(mm("42.88"), mm("4.98"))
jp1.place(mm("52.86"), mm("6.33"), rot=90, side="bottom")
l1.place(mm("48.86"), mm("10.93"), rot=90)
r4.place(mm("51.2"), mm("2.29"), rot=90)
u2.place(mm("47.58"), mm("4.46"), rot=90)
c9.place(mm("60.26"), mm("0.39"), rot=90)
c12.place(mm("60.21"), mm("9.62"), rot=-90)
c13.place(mm("28.79"), mm("11.855"))
c14.place(mm("26.83"), mm("11.855"), rot=180)
d1.place(mm("64.85"), mm("11.65"), rot=180)
j6.place(mm("27.81"), mm("14.53"))
r2.place(mm("27.103416"), mm("0.845058"), rot=90)
r3.place(mm("28.043416"), mm("0.845058"), rot=90)
r5.place(mm("69.7"), mm("12.07"), rot=180)
r6.place(mm("67.45"), mm("11.65"))
r7.place(mm("69.7"), mm("11.13"), rot=180)
sw1.place(mm("55.76"), mm("10.53"), rot=180)
sw2.place(mm("55.76"), mm("-0.57"), rot=180)
tp1.place(mm("70.36"), mm("2.48"), rot=90, side="bottom")
tp2.place(mm("65.36"), mm("2.48"), rot=90, side="bottom")
tp3.place(mm("70.36"), mm("7.48"), rot=90, side="bottom")
tp4.place(mm("65.51"), mm("7.48"), rot=90, side="bottom")
u1.place(mm("69.12"), mm("4.98"), rot=-90)
u4.place(mm("59.46"), mm("6.53"), rot=-90)
y1.place(mm("61.09"), mm("-1.77"), rot=180)

design.zone(
    batt,
    layers=("In2.Cu",),
    key="+BATT/1",
    outline=(
        (mm("44.26"), mm("-4.77")),
        arc_to((mm("44.552893"), mm("-4.062893")), (mm("45.26"), mm("-3.77"))),
        (mm("48.545786"), mm("-3.77")),
        arc_to((mm("48.928469"), mm("-3.69388")), (mm("49.252893"), mm("-3.477107"))),
        (mm("50.167107"), mm("-2.562893")),
        arc_to((mm("50.38388"), mm("-2.23847")), (mm("50.46"), mm("-1.855786"))),
        (mm("50.46"), mm("2.13")),
        arc_to((mm("50.167107"), mm("2.837107")), (mm("49.46"), mm("3.13"))),
        (mm("38.36"), mm("3.13")),
        arc_to((mm("37.652893"), mm("2.837107")), (mm("37.36"), mm("2.13"))),
        (mm("37.36"), mm("-5.27")),
        arc_to((mm("37.652893"), mm("-5.977107")), (mm("38.36"), mm("-6.27"))),
        (mm("43.26"), mm("-6.27")),
        arc_to((mm("43.967107"), mm("-5.977107")), (mm("44.26"), mm("-5.27"))),
    ),
    priority=2,
    clearance=mm("0.127"),
    min_thickness=mm("0.127"),
)
design.zone(
    gnd,
    layers=("F.Cu", "B.Cu", "In1.Cu", "In3.Cu", "In5.Cu", "In6.Cu"),
    key="GND/1",
    outline=(
        (mm("18.06"), mm("-8.47")),
        (mm("71.42"), mm("-8.47")),
        (mm("71.42"), mm("18.53")),
        (mm("18.06"), mm("18.53")),
    ),
    priority=1,
    clearance=mm("0.12"),
    min_thickness=mm("0.127"),
)
design.zone(
    vdd,
    layers=("In2.Cu", "In4.Cu"),
    key="VDD/1",
    outline=(
        (mm("18.06"), mm("-8.47")),
        (mm("71.42"), mm("-8.47")),
        (mm("71.42"), mm("19.91")),
        (mm("18.06"), mm("19.91")),
    ),
    priority=1,
    clearance=mm("0.127"),
    min_thickness=mm("0.127"),
)
design.zone(
    vsys,
    layers=("B.Cu",),
    key="VSYS/1",
    outline=(
        (mm("49.28"), mm("5.91")),
        arc_to((mm("49.206777"), mm("6.086777")), (mm("49.03"), mm("6.16"))),
        (mm("47.13"), mm("6.16")),
        arc_to((mm("46.953223"), mm("6.233223")), (mm("46.88"), mm("6.41"))),
        (mm("46.88"), mm("8.81")),
        arc_to((mm("46.953223"), mm("8.986777")), (mm("47.13"), mm("9.06"))),
        (mm("49.93"), mm("9.06")),
        arc_to((mm("50.106777"), mm("8.986777")), (mm("50.18"), mm("8.81"))),
        (mm("50.18"), mm("-0.59")),
        arc_to((mm("50.106777"), mm("-0.766777")), (mm("49.93"), mm("-0.84"))),
        (mm("47.83"), mm("-0.84")),
        arc_to((mm("47.653223"), mm("-0.766777")), (mm("47.58"), mm("-0.59"))),
        (mm("47.58"), mm("2.61")),
        arc_to((mm("47.653223"), mm("2.786777")), (mm("47.83"), mm("2.86"))),
        (mm("49.03"), mm("2.86")),
        arc_to((mm("49.206777"), mm("2.933223")), (mm("49.28"), mm("3.11"))),
    ),
    priority=2,
    clearance=mm("0.127"),
    min_thickness=mm("0.127"),
)

design.text(
    "B.SilkS/text/1",
    "~{RST}",
    (mm("33.06"), mm("13.33")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/2",
    "VDD",
    (mm("35.6"), mm("13.33")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/3",
    "VDD",
    (mm("38.14"), mm("13.33")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/4",
    "Guide at:\nlordsboards.com/royalblue54l",
    (mm("40.1"), mm("-3.98")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    justify="left",
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/5",
    "GND",
    (mm("40.68"), mm("13.33")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/6",
    "A0",
    (mm("43.22"), mm("13.33")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/7",
    "BAT",
    (mm("43.26"), mm("-3.37")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/8",
    "A1",
    (mm("45.76"), mm("13.33")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/9",
    "EN",
    (mm("45.8"), mm("-3.37")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/10",
    "A2",
    (mm("48.3"), mm("13.33")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/11",
    "USB",
    (mm("48.34"), mm("-3.37")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/12",
    "A3",
    (mm("50.84"), mm("13.33")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/13",
    "13",
    (mm("50.88"), mm("-3.37")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/14",
    "A4",
    (mm("53.38"), mm("13.33")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/15",
    "12",
    (mm("53.42"), mm("-3.37")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/16",
    "VDD",
    (mm("54.46"), mm("6.33")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    rot=270,
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/17",
    "A5",
    (mm("55.92"), mm("13.33")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/18",
    "11",
    (mm("55.96"), mm("-3.37")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/19",
    "SCK",
    (mm("58.46"), mm("13.33")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/20",
    "10",
    (mm("58.5"), mm("-3.37")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/21",
    "SDO",
    (mm("61"), mm("13.33")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/22",
    "9",
    (mm("61.04"), mm("-3.37")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/23",
    "~{RST}",
    (mm("63.16"), mm("2.479293")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    rot=270,
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/24",
    "GND",
    (mm("63.16"), mm("7.48")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    rot=270,
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/25",
    "SDI",
    (mm("63.54"), mm("13.33")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/26",
    "6",
    (mm("63.58"), mm("-3.37")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/27",
    "RX",
    (mm("66.08"), mm("13.33")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/28",
    "5",
    (mm("66.12"), mm("-3.37")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/29",
    "DIO",
    (mm("68.16"), mm("2.479293")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    rot=270,
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/30",
    "CLK",
    (mm("68.16"), mm("7.48")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    rot=270,
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/31",
    "TX",
    (mm("68.62"), mm("13.33")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/32",
    "SCL",
    (mm("68.66"), mm("-3.37")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/33",
    "SHP",
    (mm("71.16"), mm("13.33")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "B.SilkS/text/34",
    "SDA",
    (mm("71.2"), mm("-3.37")),
    layer="B.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/1",
    "I^{2}C",
    (mm("25.235"), mm("-0.82")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/2",
    "NFC",
    (mm("27.81"), mm("10.83")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/3",
    "Lord's",
    (mm("32.26"), mm("-3.27")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    rot=90,
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/4",
    "~{RST}",
    (mm("33.06"), mm("13.33")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/5",
    "VDD",
    (mm("35.6"), mm("13.33")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/6",
    "NC",
    (mm("38.14"), mm("13.33")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/7",
    "+",
    (mm("39.71"), mm("2.855")),
    layer="F.SilkS",
    size=mm("2"),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/8",
    "GND",
    (mm("40.68"), mm("13.33")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/9",
    "Debugger",
    (mm("41.56"), mm("8.13")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    rot=90,
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/10",
    "A0",
    (mm("43.22"), mm("13.33")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/11",
    "BAT",
    (mm("43.26"), mm("-3.37")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/12",
    "A1",
    (mm("45.76"), mm("13.33")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/13",
    "EN",
    (mm("45.8"), mm("-3.37")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/14",
    "nPM1300",
    (mm("46.685"), mm("0.905")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/15",
    "A2",
    (mm("48.3"), mm("13.33")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/16",
    "USB",
    (mm("48.34"), mm("-3.37")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/17",
    "A3",
    (mm("50.84"), mm("13.33")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/18",
    "13",
    (mm("50.88"), mm("-3.37")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/19",
    "BTN",
    (mm("52.06"), mm("-0.57")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/20",
    "~{RST}",
    (mm("52.06"), mm("10.73")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/21",
    "A4",
    (mm("53.38"), mm("13.33")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/22",
    "12",
    (mm("53.42"), mm("-3.37")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/23",
    "A5",
    (mm("55.92"), mm("13.33")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/24",
    "11",
    (mm("55.96"), mm("-3.37")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/25",
    "SCK",
    (mm("58.46"), mm("13.33")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/26",
    "10",
    (mm("58.5"), mm("-3.37")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/27",
    "2M",
    (mm("59.46"), mm("3.73")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/28",
    "SDO",
    (mm("61"), mm("13.33")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/29",
    "9",
    (mm("61.04"), mm("-3.37")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/30",
    "SDI",
    (mm("63.54"), mm("13.33")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/31",
    "6",
    (mm("63.58"), mm("-3.37")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/32",
    "RX",
    (mm("66.08"), mm("13.33")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/33",
    "5",
    (mm("66.12"), mm("-3.37")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/34",
    "RoyalBlue54L",
    (mm("67.36"), mm("-1.67")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/35",
    "TX",
    (mm("68.62"), mm("13.33")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/36",
    "SCL",
    (mm("68.66"), mm("-3.37")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/37",
    "SHP",
    (mm("71.16"), mm("13.33")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)
design.text(
    "F.SilkS/text/38",
    "SDA",
    (mm("71.2"), mm("-3.37")),
    layer="F.SilkS",
    size=(mm("0.7"), mm("0.8")),
    thickness=mm("0.16"),
    bold=True,
    face="Ubuntu Sans",
)

copper.apply(
    design,
    {
        "+BATT": batt,
        "/Connectors/ANALOG.A0": connectors_analog_a0,
        "/Connectors/ANALOG.A1": connectors_analog_a1,
        "/Connectors/ANALOG.A2": connectors_analog_a2,
        "/Connectors/ANALOG.A3": connectors_analog_a3,
        "/Connectors/ANALOG.A4": connectors_analog_a4,
        "/Connectors/ANALOG.A5": connectors_analog_a5,
        "/Connectors/DIG.D10": connectors_dig_d10,
        "/Connectors/DIG.D11": connectors_dig_d11,
        "/Connectors/DIG.D12": connectors_dig_d12,
        "/Connectors/DIG.D13": connectors_dig_d13,
        "/Connectors/DIG.D5": connectors_dig_d5,
        "/Connectors/DIG.D6": connectors_dig_d6,
        "/Connectors/DIG.D9": connectors_dig_d9,
        "/Connectors/ENABLE": connectors_enable,
        "/Connectors/I2C.SCL": connectors_i2c_scl,
        "/Connectors/I2C.SDA": connectors_i2c_sda,
        "/Connectors/SHPHLD": connectors_shphld,
        "/Connectors/SPI.MISO": connectors_spi_miso,
        "/Connectors/SPI.MOSI": connectors_spi_mosi,
        "/Connectors/SPI.SCK": connectors_spi_sck,
        "/Connectors/UART.RX": connectors_uart_rx,
        "/Connectors/UART.TX": connectors_uart_tx,
        "/Debugger/D+": debugger_d,
        "/Debugger/D-": debugger_d_2,
        "/Debugger/SWD_TRG.SWDCLK": debugger_swd_trg_swdclk,
        "/Debugger/SWD_TRG.SWDIO": debugger_swd_trg_swdio,
        "/Debugger/SWD_TRG.~{RESET}": debugger_swd_trg_reset,
        "/Debugger/TRG_SWDCLK_NRF52": debugger_trg_swdclk_nrf52,
        "/Debugger/TRG_SWDIO_NRF52": debugger_trg_swdio_nrf52,
        "/Debugger/TRG_~{RESET}_NRF52": debugger_trg__reset__nrf52,
        "/Debugger/UART_RX_NRF52": debugger_uart_rx_nrf52,
        "/Debugger/UART_TX_NRF52": debugger_uart_tx_nrf52,
        "/Debugger/USB.CC1": debugger_usb_cc1,
        "/Debugger/USB.CC2": debugger_usb_cc2,
        "/Debugger/USB.VBUS": debugger_usb_vbus,
        "/Debugger/nRF52_VDD": debugger_nrf52_vdd,
        "/nPM1300/NPM1300.INT": npm1300_npm1300_int,
        "/nPM1300/NPM1300.SCL": npm1300_npm1300_scl,
        "/nPM1300/NPM1300.SDA": npm1300_npm1300_sda,
        "/nRF54L15/D2_FLASH": nrf54l15_d2_flash,
        "/nRF54L15/D3_FLASH": nrf54l15_d3_flash,
        "/nRF54L15/~{CS}_FLASH": nrf54l15_cs__flash,
        "GND": gnd,
        "Net-(D1-A)": net_d1_a,
        "Net-(D1-K)": net_d1_k,
        "Net-(D3-BK)": net_d3_bk,
        "Net-(D3-GK)": net_d3_gk,
        "Net-(D3-RK)": net_d3_rk,
        "Net-(J6-Pin_2)": net_j6_pin_2,
        "Net-(J6-Pin_4)": net_j6_pin_4,
        "Net-(J8-SWCLK)": net_j8_swclk,
        "Net-(J8-SWDIO)": net_j8_swdio,
        "Net-(J8-~{RESET})": net_j8_reset,
        "Net-(JP1-A)": net_jp1_a,
        "Net-(U1-P1.00/XL1)": net_u1_p1_00_xl1,
        "Net-(U1-P1.01/XL2)": net_u1_p1_01_xl2,
        "Net-(U2-SW2)": net_u2_sw2,
        "Net-(U2-VSET2)": net_u2_vset2,
        "Net-(U5-DEC1)": net_u5_dec1,
        "Net-(U5-DEC3)": net_u5_dec3,
        "Net-(U5-DEC4)": net_u5_dec4,
        "Net-(U5-DECUSB)": net_u5_decusb,
        "Net-(U5-XC1)": net_u5_xc1,
        "Net-(U5-XC2)": net_u5_xc2,
        "VBUS": vbus,
        "VDD": vdd,
        "VSYS": vsys,
    },
)
