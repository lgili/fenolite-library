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
    dspi_dout = nets["dspi_dout"]
    irq_1 = nets["irq_1"]
    irq_2 = nets["irq_2"]
    irq_3 = nets["irq_3"]
    qspi_clk = nets["qspi_clk"]
    qspi_cs1 = nets["qspi_cs1"]
    qspi_cs2 = nets["qspi_cs2"]
    qspi_din = nets["qspi_din"]
    ucts1 = nets["ucts1"]
    urts1 = nets["urts1"]
    xtal = nets["xtal"]
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
    gnd = nets["gnd"]
    net_d301_a = Net("Net-(D301-A)")
    net_d302_a = Net("Net-(D302-A)")
    net_u301_p11 = Net("Net-(U301-P11)")
    net_u301_p4 = Net("Net-(U301-P4)")
    c301 = Part(
        refs.get("C301", "C301"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_13",
        value="100nF",
        name="C301",
    )
    c302 = Part(
        refs.get("C302", "C302"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_10",
        value="100nF",
        name="C302",
    )
    c303 = Part(
        refs.get("C303", "C303"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_13",
        value="100nF",
        name="C303",
    )
    c304 = Part(
        refs.get("C304", "C304"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_14",
        value="100nF",
        name="C304",
    )
    c305 = Part(
        refs.get("C305", "C305"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_14",
        value="100nF",
        name="C305",
    )
    c306 = Part(
        refs.get("C306", "C306"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_14",
        value="100nF",
        name="C306",
    )
    c307 = Part(
        refs.get("C307", "C307"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_14",
        value="100nF",
        name="C307",
    )
    c308 = Part(
        refs.get("C308", "C308"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_13",
        value="100nF",
        name="C308",
    )
    c309 = Part(
        refs.get("C309", "C309"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_14",
        value="100nF",
        name="C309",
    )
    c310 = Part(
        refs.get("C310", "C310"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_14",
        value="100nF",
        name="C310",
    )
    c311 = Part(
        refs.get("C311", "C311"),
        "kit-dev-coldfire-xilinx_5213:C",
        footprint="Capacitor_SMD:C_0805_2012Metric",
        footprint_definition="Capacitor_SMD:C_0805_2012Metric_10",
        value="100nF",
        name="C311",
    )
    d301 = Part(
        refs.get("D301", "D301"),
        "kit-dev-coldfire-xilinx_5213:LED",
        footprint="LED_SMD:LED_1206_3216Metric",
        value="LED",
        name="D301",
    )
    d302 = Part(
        refs.get("D302", "D302"),
        "kit-dev-coldfire-xilinx_5213:LED",
        footprint="LED_SMD:LED_1206_3216Metric",
        value="LED",
        name="D302",
    )
    p301 = Part(
        refs.get("P301", "P301"),
        "kit-dev-coldfire-xilinx_5213:CONN_6",
        footprint="Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical",
        value="CONN_6",
        name="P301",
    )
    p302 = Part(
        refs.get("P302", "P302"),
        "kit-dev-coldfire-xilinx_5213:CONN_2X2",
        footprint="Connector_PinHeader_2.54mm:PinHeader_2x02_P2.54mm_Vertical",
        value="CONN_2X2",
        name="P302",
    )
    p303 = Part(
        refs.get("P303", "P303"),
        "kit-dev-coldfire-xilinx_5213:CONN_20X2",
        footprint="Connector_PinHeader_2.54mm:PinHeader_2x20_P2.54mm_Vertical",
        value="CONN_20X2",
        name="P303",
    )
    r301 = Part(
        refs.get("R301", "R301"),
        "kit-dev-coldfire-xilinx_5213:R",
        footprint="Resistor_SMD:R_0805_2012Metric",
        footprint_definition="Resistor_SMD:R_0805_2012Metric_3",
        value="4K7",
        name="R301",
    )
    r302 = Part(
        refs.get("R302", "R302"),
        "kit-dev-coldfire-xilinx_5213:R",
        footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
        value="3,3",
        name="R302",
    )
    r303 = Part(
        refs.get("R303", "R303"),
        "kit-dev-coldfire-xilinx_5213:R",
        footprint="Resistor_SMD:R_0805_2012Metric",
        footprint_definition="Resistor_SMD:R_0805_2012Metric_13",
        value="1K",
        name="R303",
    )
    r304 = Part(
        refs.get("R304", "R304"),
        "kit-dev-coldfire-xilinx_5213:R",
        footprint="Resistor_SMD:R_0805_2012Metric",
        footprint_definition="Resistor_SMD:R_0805_2012Metric_13",
        value="1K",
        name="R304",
    )
    u301 = Part(
        refs.get("U301", "U301"),
        "kit-dev-coldfire-xilinx_5213:XCR3256-TQ144",
        footprint="Package_QFP:TQFP-144_20x20mm_P0.5mm",
        value="XCR3256-TQ144",
        name="U301",
    )
    module.add(
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
    connect(
        net_3_3v,
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
        p301["1"],
        r301["1"],
        r302["1"],
        u301["115"],
        u301["123"],
        u301["130"],
        u301["144"],
        u301["24"],
        u301["50"],
        u301["51"],
        u301["58"],
        u301["73"],
        u301["76"],
        u301["95"],
    )
    connect(dspi_dout, u301["47"])
    connect(irq_1, u301["42"])
    connect(irq_2, u301["43"])
    connect(irq_3, u301["44"])
    connect(qspi_clk, u301["48"])
    connect(qspi_cs1, u301["54"])
    connect(qspi_cs2, u301["45"])
    connect(qspi_din, u301["46"])
    connect(ucts1, p302["1"], u301["49"])
    connect(urts1, p302["3"], u301["53"])
    connect(xtal, u301["128"])
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
        d301["1"],
        d302["1"],
        p301["2"],
        p303["2"],
        p303["40"],
        u301["105"],
        u301["124"],
        u301["125"],
        u301["126"],
        u301["127"],
        u301["129"],
        u301["13"],
        u301["135"],
        u301["17"],
        u301["3"],
        u301["33"],
        u301["52"],
        u301["57"],
        u301["59"],
        u301["64"],
        u301["85"],
    )
    connect(net_d301_a, d301["2"], r303["2"])
    connect(net_d302_a, d302["2"], r304["2"])
    connect(net_u301_p11, p302["2"], u301["32"])
    connect(net_u301_p4, p302["4"], u301["31"])
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
    return module
