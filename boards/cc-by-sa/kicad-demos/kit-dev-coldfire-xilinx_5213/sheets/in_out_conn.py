# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/kit-dev-coldfire-xilinx_5213@97acc80c223d75520c03fc44cab63cd9a3202c42 by Fenolite 0.7.0.dev0 on 2026-11-03;
# modified: format conversion to the Fenolite DSL.

from fenolite.dsl import Module, Net, Part, connect, mm


def sheet(design, *, path, refs=None, **nets):
    module = Module(path.rsplit("/", 1)[-1])
    design.add(module)
    refs = refs or {}
    net_3_3v = nets["net_3_3v"]
    an0 = nets["an0"]
    an1 = nets["an1"]
    an2 = nets["an2"]
    an3 = nets["an3"]
    an4 = nets["an4"]
    an5 = nets["an5"]
    an6 = nets["an6"]
    an7 = nets["an7"]
    canrx = nets["canrx"]
    cantx = nets["cantx"]
    dspi_dout = nets["dspi_dout"]
    dtin0 = nets["dtin0"]
    dtin1 = nets["dtin1"]
    dtin2 = nets["dtin2"]
    dtin3 = nets["dtin3"]
    gpt0 = nets["gpt0"]
    gpt1 = nets["gpt1"]
    gpt2 = nets["gpt2"]
    gpt3 = nets["gpt3"]
    irq_1 = nets["irq_1"]
    irq_2 = nets["irq_2"]
    irq_3 = nets["irq_3"]
    irq_4 = nets["irq_4"]
    irq_5 = nets["irq_5"]
    irq_6 = nets["irq_6"]
    irq_7 = nets["irq_7"]
    pwm1 = nets["pwm1"]
    pwm3 = nets["pwm3"]
    pwm5 = nets["pwm5"]
    pwm7 = nets["pwm7"]
    qspi_clk = nets["qspi_clk"]
    qspi_cs0 = nets["qspi_cs0"]
    qspi_cs1 = nets["qspi_cs1"]
    qspi_cs2 = nets["qspi_cs2"]
    qspi_cs3 = nets["qspi_cs3"]
    qspi_din = nets["qspi_din"]
    rcon = nets["rcon"]
    rsti = nets["rsti"]
    rsto = nets["rsto"]
    ucts0 = nets["ucts0"]
    ucts1 = nets["ucts1"]
    ucts2 = nets["ucts2"]
    urts0 = nets["urts0"]
    urts1 = nets["urts1"]
    urts2 = nets["urts2"]
    urxd0 = nets["urxd0"]
    urxd1 = nets["urxd1"]
    urxd2 = nets["urxd2"]
    utxd0 = nets["utxd0"]
    utxd1 = nets["utxd1"]
    utxd2 = nets["utxd2"]
    vcca = nets["vcca"]
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
    gnd = nets["gnd"]
    gnda = nets["gnda"]
    net_can_term201_pad2 = Net("Net-(CAN_TERM201-Pad2)")
    net_com_sel201_p3 = Net("Net-(COM_SEL201-P3)")
    net_com_sel202_p3 = Net("Net-(COM_SEL202-P3)")
    net_com_sel203_p3 = Net("Net-(COM_SEL203-P3)")
    net_d201_k = Net("Net-(D201-K)")
    net_f201_pad1 = Net("Net-(F201-Pad1)")
    net_led201_a = Net("Net-(LED201-A)")
    net_led202_a = Net("Net-(LED202-A)")
    net_led203_a = Net("Net-(LED203-A)")
    net_led204_a = Net("Net-(LED204-A)")
    net_led205_a = Net("Net-(LED205-A)")
    net_mcu_port201_p1 = Net("Net-(MCU_PORT201-P1)")
    net_pulupen201_pad2 = Net("Net-(PULUPEN201-Pad2)")
    net_pulupen201_pad4 = Net("Net-(PULUPEN201-Pad4)")
    net_pulupen201_pad6 = Net("Net-(PULUPEN201-Pad6)")
    net_pulupen201_pad8 = Net("Net-(PULUPEN201-Pad8)")
    net_tb201_p1 = Net("Net-(TB201-P1)")
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
    net_uartcan201_p6 = Net("Net-(UARTCAN201-P6)")
    net_uartcan202_p6 = Net("Net-(UARTCAN202-P6)")
    net_uartcan203_p6 = Net("Net-(UARTCAN203-P6)")
    c201 = Part(
        refs.get("C201", "C201"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_15",
        value="100nF",
        name="C201",
    )
    c202 = Part(
        refs.get("C202", "C202"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_7",
        value="100nF",
        name="C202",
    )
    c203 = Part(
        refs.get("C203", "C203"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_3",
        value="100nF",
        name="C203",
    )
    c204 = Part(
        refs.get("C204", "C204"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_16",
        value="100nF",
        name="C204",
    )
    c205 = Part(
        refs.get("C205", "C205"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_3",
        value="100nF",
        name="C205",
    )
    c206 = Part(
        refs.get("C206", "C206"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_3",
        value="100nF",
        name="C206",
    )
    c207 = Part(
        refs.get("C207", "C207"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_6",
        value="100nF",
        name="C207",
    )
    c208 = Part(
        refs.get("C208", "C208"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_3",
        value="100nF",
        name="C208",
    )
    c209 = Part(
        refs.get("C209", "C209"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_17",
        value="100nF",
        name="C209",
    )
    c210 = Part(
        refs.get("C210", "C210"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_3",
        value="100nF",
        name="C210",
    )
    c211 = Part(
        refs.get("C211", "C211"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_3",
        value="100nF",
        name="C211",
    )
    c212 = Part(
        refs.get("C212", "C212"),
        "kit-dev-coldfire-xilinx_5213:CP",
        footprint="Capacitor_THT:CP_Radial_D8.0mm_P5.00mm",
        value="10uF",
        name="C212",
    )
    c213 = Part(
        refs.get("C213", "C213"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_18",
        value="100nF",
        name="C213",
    )
    c214 = Part(
        refs.get("C214", "C214"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_6",
        value="100nF",
        name="C214",
    )
    c215 = Part(
        refs.get("C215", "C215"),
        "kit-dev-coldfire-xilinx_5213:CP",
        footprint="Capacitor_THT:CP_Radial_D8.0mm_P5.00mm",
        footprint_definition="Capacitor_THT:CP_Radial_D8.0mm_P5.00mm_2",
        value="220uF",
        name="C215",
    )
    c216 = Part(
        refs.get("C216", "C216"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_3",
        value="100nF",
        name="C216",
    )
    c217 = Part(
        refs.get("C217", "C217"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_19",
        value="100nF",
        name="C217",
    )
    c218 = Part(
        refs.get("C218", "C218"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_3",
        value="100nF",
        name="C218",
    )
    c219 = Part(
        refs.get("C219", "C219"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_7",
        value="100nF",
        name="C219",
    )
    c220 = Part(
        refs.get("C220", "C220"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_20",
        value="100nF",
        name="C220",
    )
    c221 = Part(
        refs.get("C221", "C221"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_21",
        value="100nF",
        name="C221",
    )
    can_en201 = Part(
        refs.get("CAN_EN201", "CAN_EN201"),
        "kit-dev-coldfire-xilinx_5213:CONN_2X2",
        footprint="Connector_PinHeader_2.54mm:PinHeader_2x02_P2.54mm_Vertical",
        value="CONN_2X2",
        name="CAN_EN201",
    )
    can_term201 = Part(
        refs.get("CAN_TERM201", "CAN_TERM201"),
        "kit-dev-coldfire-xilinx_5213:JUMPER",
        footprint="Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical",
        value="JUMPER",
        name="CAN_TERM201",
    )
    com_sel201 = Part(
        refs.get("COM_SEL201", "COM_SEL201"),
        "kit-dev-coldfire-xilinx_5213:CONN_3",
        footprint="Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical",
        value="CONN_3",
        name="COM_SEL201",
    )
    com_sel202 = Part(
        refs.get("COM_SEL202", "COM_SEL202"),
        "kit-dev-coldfire-xilinx_5213:CONN_3",
        footprint="Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical",
        footprint_definition="Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical_2",
        value="CONN_3",
        name="COM_SEL202",
    )
    com_sel203 = Part(
        refs.get("COM_SEL203", "COM_SEL203"),
        "kit-dev-coldfire-xilinx_5213:CONN_3",
        footprint="Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical",
        value="CONN_3",
        name="COM_SEL203",
    )
    d201 = Part(
        refs.get("D201", "D201"),
        "kit-dev-coldfire-xilinx_5213:DIODE",
        footprint="Diode_THT:D_DO-15_P12.70mm_Horizontal",
        value="1N4004",
        name="D201",
    )
    f201 = Part(
        refs.get("F201", "F201"),
        "kit-dev-coldfire-xilinx_5213:FUSE",
        footprint="kit-dev-coldfire:FSUPCMS",
        value="FUSE",
        name="F201",
    )
    j201 = Part(
        refs.get("J201", "J201"),
        "kit-dev-coldfire-xilinx_5213:JACK_2P",
        footprint="kit-dev-coldfire:JACK_ALIM",
        value="JACK_2P",
        name="J201",
    )
    jp201 = Part(
        refs.get("JP201", "JP201"),
        "kit-dev-coldfire-xilinx_5213:JUMPER",
        footprint="Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical",
        footprint_definition="Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical_3",
        value="JUMPER",
        name="JP201",
    )
    led201 = Part(
        refs.get("LED201", "LED201"),
        "kit-dev-coldfire-xilinx_5213:LED",
        footprint="LED_SMD:LED_1206_3216Metric",
        footprint_definition="LED_SMD:LED_1206_3216Metric_2",
        value="LED",
        name="LED201",
    )
    led202 = Part(
        refs.get("LED202", "LED202"),
        "kit-dev-coldfire-xilinx_5213:LED",
        footprint="LED_SMD:LED_1206_3216Metric",
        footprint_definition="LED_SMD:LED_1206_3216Metric_3",
        value="LED",
        name="LED202",
    )
    led203 = Part(
        refs.get("LED203", "LED203"),
        "kit-dev-coldfire-xilinx_5213:LED",
        footprint="LED_SMD:LED_1206_3216Metric",
        footprint_definition="LED_SMD:LED_1206_3216Metric_3",
        value="LED",
        name="LED203",
    )
    led204 = Part(
        refs.get("LED204", "LED204"),
        "kit-dev-coldfire-xilinx_5213:LED",
        footprint="LED_SMD:LED_1206_3216Metric",
        footprint_definition="LED_SMD:LED_1206_3216Metric_3",
        value="LED",
        name="LED204",
    )
    led205 = Part(
        refs.get("LED205", "LED205"),
        "kit-dev-coldfire-xilinx_5213:LED",
        footprint="LED_SMD:LED_1206_3216Metric",
        footprint_definition="LED_SMD:LED_1206_3216Metric_4",
        value="LED",
        name="LED205",
    )
    mcu_port201 = Part(
        refs.get("MCU_PORT201", "MCU_PORT201"),
        "kit-dev-coldfire-xilinx_5213:CONN_30X2",
        footprint="Connector_PinHeader_2.54mm:PinHeader_2x30_P2.54mm_Vertical",
        value="CONN_30X2",
        name="MCU_PORT201",
    )
    pulupen201 = Part(
        refs.get("PULUPEN201", "PULUPEN201"),
        "kit-dev-coldfire-xilinx_5213:CONN_4X2",
        footprint="Connector_PinHeader_2.54mm:PinHeader_2x04_P2.54mm_Vertical",
        value="CONN_4X2",
        name="PULUPEN201",
    )
    r201 = Part(
        refs.get("R201", "R201"),
        "kit-dev-coldfire-xilinx_5213:R",
        footprint="Resistor_SMD:R_0805_2012Metric",
        footprint_definition="Resistor_SMD:R_0805_2012Metric_9",
        value="10K",
        name="R201",
    )
    r202 = Part(
        refs.get("R202", "R202"),
        "kit-dev-coldfire-xilinx_5213:R",
        footprint="Resistor_SMD:R_0805_2012Metric",
        footprint_definition="Resistor_SMD:R_0805_2012Metric_13",
        value="270",
        name="R202",
    )
    r203 = Part(
        refs.get("R203", "R203"),
        "kit-dev-coldfire-xilinx_5213:R",
        footprint="Resistor_SMD:R_0805_2012Metric",
        footprint_definition="Resistor_SMD:R_0805_2012Metric_13",
        value="270",
        name="R203",
    )
    r204 = Part(
        refs.get("R204", "R204"),
        "kit-dev-coldfire-xilinx_5213:R",
        footprint="Resistor_SMD:R_0805_2012Metric",
        footprint_definition="Resistor_SMD:R_0805_2012Metric_13",
        value="270",
        name="R204",
    )
    r205 = Part(
        refs.get("R205", "R205"),
        "kit-dev-coldfire-xilinx_5213:R",
        footprint="Resistor_SMD:R_0805_2012Metric",
        footprint_definition="Resistor_SMD:R_0805_2012Metric_10",
        value="10K",
        name="R205",
    )
    r206 = Part(
        refs.get("R206", "R206"),
        "kit-dev-coldfire-xilinx_5213:R",
        footprint="Resistor_SMD:R_0805_2012Metric",
        footprint_definition="Resistor_SMD:R_0805_2012Metric_13",
        value="270",
        name="R206",
    )
    r207 = Part(
        refs.get("R207", "R207"),
        "kit-dev-coldfire-xilinx_5213:R",
        footprint="Resistor_SMD:R_0805_2012Metric",
        footprint_definition="Resistor_SMD:R_0805_2012Metric_13",
        value="270",
        name="R207",
    )
    r208 = Part(
        refs.get("R208", "R208"),
        "kit-dev-coldfire-xilinx_5213:R",
        footprint="Resistor_SMD:R_0805_2012Metric",
        footprint_definition="Resistor_SMD:R_0805_2012Metric_10",
        value="10K",
        name="R208",
    )
    r209 = Part(
        refs.get("R209", "R209"),
        "kit-dev-coldfire-xilinx_5213:R",
        footprint="Resistor_SMD:R_0805_2012Metric",
        footprint_definition="Resistor_SMD:R_0805_2012Metric_19",
        value="62",
        name="R209",
    )
    r210 = Part(
        refs.get("R210", "R210"),
        "kit-dev-coldfire-xilinx_5213:R",
        footprint="Resistor_SMD:R_0805_2012Metric",
        footprint_definition="Resistor_SMD:R_0805_2012Metric_20",
        value="1K",
        name="R210",
    )
    r211 = Part(
        refs.get("R211", "R211"),
        "kit-dev-coldfire-xilinx_5213:R",
        footprint="Resistor_SMD:R_0805_2012Metric",
        footprint_definition="Resistor_SMD:R_0805_2012Metric_21",
        value="4,7K",
        name="R211",
    )
    r212 = Part(
        refs.get("R212", "R212"),
        "kit-dev-coldfire-xilinx_5213:R",
        footprint="Resistor_SMD:R_0805_2012Metric",
        footprint_definition="Resistor_SMD:R_0805_2012Metric_22",
        value="4,7K",
        name="R212",
    )
    r213 = Part(
        refs.get("R213", "R213"),
        "kit-dev-coldfire-xilinx_5213:R",
        footprint="Resistor_SMD:R_0805_2012Metric",
        footprint_definition="Resistor_SMD:R_0805_2012Metric_23",
        value="4,7K",
        name="R213",
    )
    r214 = Part(
        refs.get("R214", "R214"),
        "kit-dev-coldfire-xilinx_5213:R",
        footprint="Resistor_SMD:R_0805_2012Metric",
        footprint_definition="Resistor_SMD:R_0805_2012Metric_10",
        value="4,7K",
        name="R214",
    )
    r215 = Part(
        refs.get("R215", "R215"),
        "kit-dev-coldfire-xilinx_5213:R",
        footprint="Resistor_SMD:R_0805_2012Metric",
        footprint_definition="Resistor_SMD:R_0805_2012Metric_9",
        value="10K",
        name="R215",
    )
    rcan201 = Part(
        refs.get("RCAN201", "RCAN201"),
        "kit-dev-coldfire-xilinx_5213:R",
        footprint="Resistor_SMD:R_0805_2012Metric",
        footprint_definition="Resistor_SMD:R_0805_2012Metric_24",
        value="R",
        name="RCAN201",
    )
    rcan202 = Part(
        refs.get("RCAN202", "RCAN202"),
        "kit-dev-coldfire-xilinx_5213:R",
        footprint="Resistor_SMD:R_0805_2012Metric",
        footprint_definition="Resistor_SMD:R_0805_2012Metric_25",
        value="R",
        name="RCAN202",
    )
    rs201 = Part(
        refs.get("RS201", "RS201"),
        "kit-dev-coldfire-xilinx_5213:CONN_1",
        footprint="Connector_PinHeader_2.54mm:PinHeader_1x01_P2.54mm_Vertical",
        footprint_definition="Connector_PinHeader_2.54mm:PinHeader_1x01_P2.54mm_Vertical_2",
        value="CONN_1",
        name="RS201",
    )
    sw201 = Part(
        refs.get("SW201", "SW201"),
        "kit-dev-coldfire-xilinx_5213:SW_PUSH",
        footprint="kit-dev-coldfire:SW_PUSH_SMALL",
        footprint_definition="kit-dev-coldfire:SW_PUSH_SMALL_3",
        value="SW_PUSH",
        name="SW201",
    )
    sw202 = Part(
        refs.get("SW202", "SW202"),
        "kit-dev-coldfire-xilinx_5213:SW_PUSH",
        footprint="kit-dev-coldfire:SW_PUSH_SMALL",
        footprint_definition="kit-dev-coldfire:SW_PUSH_SMALL_4",
        value="SW_PUSH",
        name="SW202",
    )
    sw_onoff201 = Part(
        refs.get("SW_ONOFF201", "SW_ONOFF201"),
        "kit-dev-coldfire-xilinx_5213:SWITCH_INV",
        footprint="kit-dev-coldfire:SW_SPDT",
        value="SWITCH_INV",
        name="SW_ONOFF201",
    )
    tb201 = Part(
        refs.get("TB201", "TB201"),
        "kit-dev-coldfire-xilinx_5213:CONN_2",
        footprint="TerminalBlock_Altech:Altech_AK300_1x02_P5.00mm_45-Degree",
        value="CONN_2",
        name="TB201",
    )
    u201 = Part(
        refs.get("U201", "U201"),
        "kit-dev-coldfire-xilinx_5213:74LS125",
        footprint="Package_SO:SOIC-14_3.9x8.7mm_P1.27mm",
        value="74HC125",
        name="U201",
    )
    u202 = Part(
        refs.get("U202", "U202"),
        "kit-dev-coldfire-xilinx_5213:MAX202",
        footprint="Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
        value="MAX202",
        name="U202",
    )
    u203 = Part(
        refs.get("U203", "U203"),
        "kit-dev-coldfire-xilinx_5213:MAX202",
        footprint="Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
        footprint_definition="Package_SO:SOIC-16_3.9x9.9mm_P1.27mm_2",
        value="MAX202",
        name="U203",
    )
    u204 = Part(
        refs.get("U204", "U204"),
        "kit-dev-coldfire-xilinx_5213:MAX202",
        footprint="Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
        footprint_definition="Package_SO:SOIC-16_3.9x9.9mm_P1.27mm_3",
        value="MAX202",
        name="U204",
    )
    u205 = Part(
        refs.get("U205", "U205"),
        "kit-dev-coldfire-xilinx_5213:PCA82C251",
        footprint="Package_SO:SOIC-8_3.9x4.9mm_P1.27mm",
        value="PCA82C251",
        name="U205",
    )
    uartcan201 = Part(
        refs.get("UARTCAN201", "UARTCAN201"),
        "kit-dev-coldfire-xilinx_5213:DB9",
        footprint="Connector_Dsub:DSUB-9_Female_Horizontal_P2.77x2.84mm_EdgePinOffset7.70mm_Housed_MountingHolesOffset9.12mm",
        value="DB9",
        name="UARTCAN201",
    )
    uartcan202 = Part(
        refs.get("UARTCAN202", "UARTCAN202"),
        "kit-dev-coldfire-xilinx_5213:DB9",
        footprint="Connector_Dsub:DSUB-9_Female_Horizontal_P2.77x2.84mm_EdgePinOffset7.70mm_Housed_MountingHolesOffset9.12mm",
        footprint_definition="Connector_Dsub:DSUB-9_Female_Horizontal_P2.77x2.84mm_EdgePinOffset7.70mm_Housed_MountingHolesOffset9.12mm_2",
        value="DB9",
        name="UARTCAN202",
    )
    uartcan203 = Part(
        refs.get("UARTCAN203", "UARTCAN203"),
        "kit-dev-coldfire-xilinx_5213:DB9",
        footprint="Connector_Dsub:DSUB-9_Female_Horizontal_P2.77x2.84mm_EdgePinOffset7.70mm_Housed_MountingHolesOffset9.12mm",
        footprint_definition="Connector_Dsub:DSUB-9_Female_Horizontal_P2.77x2.84mm_EdgePinOffset7.70mm_Housed_MountingHolesOffset9.12mm_3",
        value="DB9",
        name="UARTCAN203",
    )
    uart_en201 = Part(
        refs.get("UART_EN201", "UART_EN201"),
        "kit-dev-coldfire-xilinx_5213:CONN_4X2",
        footprint="Connector_PinHeader_2.54mm:PinHeader_2x04_P2.54mm_Vertical",
        footprint_definition="Connector_PinHeader_2.54mm:PinHeader_2x04_P2.54mm_Vertical_2",
        value="CONN_4X2",
        name="UART_EN201",
    )
    uart_en202 = Part(
        refs.get("UART_EN202", "UART_EN202"),
        "kit-dev-coldfire-xilinx_5213:CONN_4X2",
        footprint="Connector_PinHeader_2.54mm:PinHeader_2x04_P2.54mm_Vertical",
        footprint_definition="Connector_PinHeader_2.54mm:PinHeader_2x04_P2.54mm_Vertical_2",
        value="CONN_4X2",
        name="UART_EN202",
    )
    uart_en203 = Part(
        refs.get("UART_EN203", "UART_EN203"),
        "kit-dev-coldfire-xilinx_5213:CONN_4X2",
        footprint="Connector_PinHeader_2.54mm:PinHeader_2x04_P2.54mm_Vertical",
        footprint_definition="Connector_PinHeader_2.54mm:PinHeader_2x04_P2.54mm_Vertical_2",
        value="CONN_4X2",
        name="UART_EN203",
    )
    vr201 = Part(
        refs.get("VR201", "VR201"),
        "kit-dev-coldfire-xilinx_5213:LT1129_QPACK",
        footprint="Package_TO_SOT_SMD:TO-263-5_TabPin3",
        value="LT1129_QPACK",
        name="VR201",
    )
    vref201 = Part(
        refs.get("VREF201", "VREF201"),
        "kit-dev-coldfire-xilinx_5213:CONN_1",
        footprint="Connector_PinHeader_2.54mm:PinHeader_1x01_P2.54mm_Vertical",
        footprint_definition="Connector_PinHeader_2.54mm:PinHeader_1x01_P2.54mm_Vertical_3",
        value="CONN_1",
        name="VREF201",
    )
    vx_en201 = Part(
        refs.get("VX_EN201", "VX_EN201"),
        "kit-dev-coldfire-xilinx_5213:JUMPER",
        footprint="Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical",
        footprint_definition="Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical_4",
        value="JUMPER",
        name="VX_EN201",
    )
    module.add(
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
        j201,
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
    connect(
        net_3_3v,
        c202["1"],
        c203["1"],
        c204["1"],
        c208["1"],
        c209["1"],
        c215["1"],
        c216["1"],
        c217["1"],
        c219["1"],
        mcu_port201["59"],
        r201["1"],
        r207["2"],
        r211["1"],
        r212["1"],
        r213["1"],
        r214["1"],
        rcan202["1"],
        u201["14"],
        u202["16"],
        u203["16"],
        u204["16"],
        u205["3"],
        vr201["1"],
        vr201["2"],
        vx_en201["1"],
    )
    connect(an0, mcu_port201["10"])
    connect(an1, mcu_port201["12"])
    connect(an2, mcu_port201["14"])
    connect(an3, mcu_port201["16"])
    connect(an4, mcu_port201["18"])
    connect(an5, mcu_port201["20"])
    connect(an6, mcu_port201["22"])
    connect(an7, mcu_port201["24"])
    connect(canrx, can_en201["4"], mcu_port201["28"], pulupen201["7"])
    connect(cantx, can_en201["1"], mcu_port201["26"], pulupen201["5"])
    connect(dspi_dout, mcu_port201["17"])
    connect(dtin0, mcu_port201["34"], u201["2"])
    connect(dtin1, mcu_port201["36"], u201["5"])
    connect(dtin2, mcu_port201["38"], u201["12"])
    connect(dtin3, mcu_port201["40"], u201["9"])
    connect(gpt0, mcu_port201["49"])
    connect(gpt1, mcu_port201["50"])
    connect(gpt2, mcu_port201["51"])
    connect(gpt3, mcu_port201["52"])
    connect(irq_1, mcu_port201["2"])
    connect(irq_2, mcu_port201["8"])
    connect(irq_3, mcu_port201["31"])
    connect(irq_4, mcu_port201["33"], sw201["1"])
    connect(irq_5, mcu_port201["35"], sw202["1"])
    connect(irq_6, mcu_port201["37"])
    connect(irq_7, mcu_port201["39"])
    connect(pwm1, mcu_port201["13"])
    connect(pwm3, mcu_port201["15"])
    connect(pwm5, mcu_port201["30"])
    connect(pwm7, mcu_port201["32"])
    connect(qspi_clk, mcu_port201["21"], pulupen201["1"])
    connect(qspi_cs0, mcu_port201["23"], pulupen201["3"])
    connect(qspi_cs1, mcu_port201["25"])
    connect(qspi_cs2, mcu_port201["27"])
    connect(qspi_cs3, mcu_port201["29"])
    connect(qspi_din, mcu_port201["19"])
    connect(rcon, mcu_port201["53"])
    connect(rsti, mcu_port201["6"])
    connect(rsto, mcu_port201["4"])
    connect(ucts0, mcu_port201["44"], uart_en201["8"])
    connect(ucts1, mcu_port201["11"], uart_en202["8"])
    connect(ucts2, mcu_port201["48"], uart_en203["8"])
    connect(urts0, mcu_port201["42"], uart_en201["6"])
    connect(urts1, mcu_port201["9"], uart_en202["6"])
    connect(urts2, mcu_port201["46"], uart_en203["6"])
    connect(urxd0, mcu_port201["43"], uart_en201["4"])
    connect(urxd1, mcu_port201["7"], uart_en202["4"])
    connect(urxd2, mcu_port201["47"], uart_en203["4"])
    connect(utxd0, mcu_port201["41"], uart_en201["2"])
    connect(utxd1, mcu_port201["5"], uart_en202["2"])
    connect(utxd2, mcu_port201["45"], uart_en203["2"])
    connect(vcca, mcu_port201["55"], mcu_port201["57"])
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
    connect(
        gnd,
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
        com_sel202["1"],
        d201["2"],
        j201["1"],
        j201["2"],
        jp201["1"],
        led201["1"],
        led202["1"],
        led203["1"],
        led204["1"],
        led205["1"],
        mcu_port201["3"],
        mcu_port201["54"],
        mcu_port201["60"],
        r205["1"],
        r208["1"],
        r210["2"],
        r215["1"],
        rcan201["1"],
        sw201["2"],
        sw202["2"],
        tb201["2"],
        u201["7"],
        u202["15"],
        u203["15"],
        u204["15"],
        u205["2"],
        uartcan201["5"],
        uartcan202["5"],
        uartcan203["5"],
        vr201["3"],
    )
    connect(gnda, mcu_port201["56"], mcu_port201["58"])
    connect(net_can_term201_pad2, can_term201["2"], r209["2"])
    connect(net_com_sel201_p3, com_sel201["3"], u204["7"])
    connect(net_com_sel202_p3, com_sel202["3"], u204["8"])
    connect(net_com_sel203_p3, com_sel203["3"], u204["13"])
    connect(net_d201_k, c212["1"], c213["1"], d201["1"], f201["2"], vr201["5"])
    connect(net_f201_pad1, f201["1"], sw_onoff201["2"])
    connect(net_led201_a, led201["2"], r202["1"])
    connect(net_led202_a, led202["2"], r203["1"])
    connect(net_led203_a, led203["2"], r204["1"])
    connect(net_led204_a, led204["2"], r206["1"])
    connect(net_led205_a, led205["2"], r207["1"])
    connect(net_mcu_port201_p1, c201["2"], mcu_port201["1"], vx_en201["2"])
    connect(net_pulupen201_pad2, pulupen201["2"], r211["2"])
    connect(net_pulupen201_pad4, pulupen201["4"], r212["2"])
    connect(net_pulupen201_pad6, pulupen201["6"], r213["2"])
    connect(net_pulupen201_pad8, pulupen201["8"], r214["2"])
    connect(net_tb201_p1, j201["3"], sw_onoff201["3"], tb201["1"])
    connect(net_u201a_e, jp201["2"], r201["2"], u201["1"], u201["10"], u201["13"], u201["4"])
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
    connect(net_uartcan201_p6, uartcan201["1"], uartcan201["4"], uartcan201["6"])
    connect(net_uartcan202_p6, uartcan202["1"], uartcan202["4"], uartcan202["6"])
    connect(net_uartcan203_p6, uartcan203["1"], uartcan203["4"], uartcan203["6"])
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
    j201.place(mm("4.5"), mm("-40"), rot=-90)
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
    return module
