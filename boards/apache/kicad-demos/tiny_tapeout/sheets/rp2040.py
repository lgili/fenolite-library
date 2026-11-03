# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/tiny_tapeout@97acc80c223d75520c03fc44cab63cd9a3202c42 by Fenolite 0.7.0.dev0 on 2026-11-03;
# modified: format conversion to the Fenolite DSL.

from fenolite.dsl import Module, Net, Part, connect, mm


def sheet(design, *, path, refs=None, **nets):
    module = Module(path.rsplit("/", 1)[-1])
    design.add(module)
    refs = refs or {}
    net_3v3 = nets["net_3v3"]
    rp2040_dvdd = Net("/RP2040/DVDD")
    rp2040_qspi_clk = Net("/RP2040/QSPI_CLK")
    rp2040_qspi_sd0 = Net("/RP2040/QSPI_SD0")
    rp2040_qspi_sd1 = Net("/RP2040/QSPI_SD1")
    rp2040_qspi_sd2 = Net("/RP2040/QSPI_SD2")
    rp2040_qspi_sd3 = Net("/RP2040/QSPI_SD3")
    rp2040_run = Net("/RP2040/RUN")
    rp2040_swclk = nets["rp2040_swclk"]
    rp2040_swdio = nets["rp2040_swdio"]
    gnd = nets["gnd"]
    hk_csb = nets["hk_csb"]
    hk_sck = nets["hk_sck"]
    net_c30_pad1 = Net("Net-(C30-Pad1)")
    net_u6_xin = Net("Net-(U6-XIN)")
    net_u6_xout = Net("Net-(U6-XOUT)")
    rpio29 = nets["rpio29"]
    rp_proj_clk = nets["rp_proj_clk"]
    sdi_out0 = nets["sdi_out0"]
    sdo_out1 = nets["sdo_out1"]
    boot_mode = nets["boot_mode"]
    cinc_out3 = nets["cinc_out3"]
    ctrl_ena = nets["ctrl_ena"]
    in0 = nets["in0"]
    in1 = nets["in1"]
    in2 = nets["in2"]
    in3 = nets["in3"]
    in4 = nets["in4"]
    in5 = nets["in5"]
    in6 = nets["in6"]
    in7 = nets["in7"]
    out4 = nets["out4"]
    out5 = nets["out5"]
    out6 = nets["out6"]
    out7 = nets["out7"]
    uio0 = nets["uio0"]
    uio1 = nets["uio1"]
    uio2 = nets["uio2"]
    uio3 = nets["uio3"]
    uio4 = nets["uio4"]
    uio5 = nets["uio5"]
    uio6 = nets["uio6"]
    uio7 = nets["uio7"]
    usb_d = nets["usb_d"]
    usb_d_2 = nets["usb_d_2"]
    crst_out2 = nets["crst_out2"]
    project_rst = nets["project_rst"]
    c29 = Part(
        refs.get("C29", "C29"),
        "TinyTapeout:C_Small",
        footprint="Capacitor_SMD:C_0402_1005Metric",
        footprint_definition="Capacitor_SMD:C_0402_1005Metric_13",
        value="6pF",
        properties={
            "Characteristics": "6pF 10% 50V XR 0402",
            "MPN": "CC0402BRNPO9BN6R0",
            "MPN_ALT": "0402N6R0D500CT",
        },
        name="C29",
    )
    c30 = Part(
        refs.get("C30", "C30"),
        "TinyTapeout:C_Small",
        footprint="Capacitor_SMD:C_0402_1005Metric",
        footprint_definition="Capacitor_SMD:C_0402_1005Metric_14",
        value="6pF",
        properties={"Characteristics": "6pF 10% 50V XR 0402", "MPN": "CC0402BRNPO9BN6R0"},
        name="C30",
    )
    c31 = Part(
        refs.get("C31", "C31"),
        "TinyTapeout:C_Small",
        footprint="Capacitor_SMD:C_0402_1005Metric",
        footprint_definition="Capacitor_SMD:C_0402_1005Metric_15",
        value="100nF",
        properties={
            "Characteristics": "100n 10% 25V XR 0402",
            "JLC": "",
            "MPN": "CL05A104KA5NNNC",
            "MPN_ALT": "GRM155R71E104KE14J",
            "Part number": "",
        },
        name="C31",
    )
    c32 = Part(
        refs.get("C32", "C32"),
        "TinyTapeout:C_Small",
        footprint="Capacitor_SMD:C_0603_1608Metric",
        footprint_definition="Capacitor_SMD:C_0603_1608Metric_9",
        value="1uF",
        properties={
            "Characteristics": "1u 10V XR 0603",
            "MPN": "CL10A105KA8NNNC",
            "MPN_ALT": "C0603C105K4RAC7411",
        },
        name="C32",
    )
    c33 = Part(
        refs.get("C33", "C33"),
        "TinyTapeout:C_Small",
        footprint="Capacitor_SMD:C_0402_1005Metric",
        footprint_definition="Capacitor_SMD:C_0402_1005Metric_16",
        value="100nF",
        properties={
            "Characteristics": "100n 10% 25V XR 0402",
            "MPN": "CL05A104KA5NNNC",
            "MPN_ALT": "GRM155R71E104KE14J",
        },
        name="C33",
    )
    c34 = Part(
        refs.get("C34", "C34"),
        "TinyTapeout:C_Small",
        footprint="Capacitor_SMD:C_0402_1005Metric",
        footprint_definition="Capacitor_SMD:C_0402_1005Metric_11",
        value="100nF",
        properties={
            "Characteristics": "100n 10% 25V XR 0402",
            "MPN": "CL05A104KA5NNNC",
            "MPN_ALT": "GRM155R71E104KE14J",
        },
        name="C34",
    )
    c35 = Part(
        refs.get("C35", "C35"),
        "TinyTapeout:C_Small",
        footprint="Capacitor_SMD:C_0402_1005Metric",
        footprint_definition="Capacitor_SMD:C_0402_1005Metric_11",
        value="100nF",
        properties={
            "Characteristics": "100n 10% 25V XR 0402",
            "MPN": "CL05A104KA5NNNC",
            "MPN_ALT": "GRM155R71E104KE14J",
        },
        name="C35",
    )
    c36 = Part(
        refs.get("C36", "C36"),
        "TinyTapeout:C_Small",
        footprint="Capacitor_SMD:C_0402_1005Metric",
        footprint_definition="Capacitor_SMD:C_0402_1005Metric_17",
        value="100nF",
        properties={
            "Characteristics": "100n 10% 25V XR 0402",
            "MPN": "CL05A104KA5NNNC",
            "MPN_ALT": "GRM155R71E104KE14J",
        },
        name="C36",
    )
    c37 = Part(
        refs.get("C37", "C37"),
        "TinyTapeout:C_Small",
        footprint="Capacitor_SMD:C_0603_1608Metric",
        footprint_definition="Capacitor_SMD:C_0603_1608Metric_10",
        value="1uF",
        properties={
            "Characteristics": "1u 10V XR 0603",
            "MPN": "CL10A105KA8NNNC",
            "MPN_ALT": "C0603C105K4RAC7411",
        },
        name="C37",
    )
    c38 = Part(
        refs.get("C38", "C38"),
        "TinyTapeout:C_Small",
        footprint="Capacitor_SMD:C_0402_1005Metric",
        footprint_definition="Capacitor_SMD:C_0402_1005Metric_12",
        value="100nF",
        properties={
            "Characteristics": "100n 10% 25V XR 0402",
            "MPN": "CL05A104KA5NNNC",
            "MPN_ALT": "GRM155R71E104KE14J",
        },
        name="C38",
    )
    c39 = Part(
        refs.get("C39", "C39"),
        "TinyTapeout:C_Small",
        footprint="Capacitor_SMD:C_0402_1005Metric",
        footprint_definition="Capacitor_SMD:C_0402_1005Metric_12",
        value="100nF",
        properties={
            "Characteristics": "100n 10% 25V XR 0402",
            "MPN": "CL05A104KA5NNNC",
            "MPN_ALT": "GRM155R71E104KE14J",
        },
        name="C39",
    )
    c40 = Part(
        refs.get("C40", "C40"),
        "TinyTapeout:C_Small",
        footprint="Capacitor_SMD:C_0402_1005Metric",
        footprint_definition="Capacitor_SMD:C_0402_1005Metric_18",
        value="100nF",
        properties={
            "Characteristics": "100n 10% 25V XR 0402",
            "MPN": "CL05A104KA5NNNC",
            "MPN_ALT": "GRM155R71E104KE14J",
        },
        name="C40",
    )
    c41 = Part(
        refs.get("C41", "C41"),
        "TinyTapeout:C_Small",
        footprint="Capacitor_SMD:C_0402_1005Metric",
        footprint_definition="Capacitor_SMD:C_0402_1005Metric_19",
        value="100nF",
        properties={
            "Characteristics": "100n 10% 25V XR 0402",
            "MPN": "CL05A104KA5NNNC",
            "MPN_ALT": "GRM155R71E104KE14J",
        },
        name="C41",
    )
    j10 = Part(
        refs.get("J10", "J10"),
        "TinyTapeout:Conn_01x02",
        footprint="Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical",
        value="Conn_01x02",
        dnp=True,
        name="J10",
    )
    j11 = Part(
        refs.get("J11", "J11"),
        "TinyTapeout:Conn_01x06",
        footprint="Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical_SMD_Pin1Right",
        value="Conn_01x06",
        properties={"MPN": "61300611121", "Part number": "", "Status": ""},
        dnp=True,
        name="J11",
    )
    r34 = Part(
        refs.get("R34", "R34"),
        "TinyTapeout:R_Small",
        footprint="Resistor_SMD:R_0402_1005Metric",
        footprint_definition="Resistor_SMD:R_0402_1005Metric_13",
        value="10k",
        properties={
            "Characteristics": "10k 0402",
            "JLC": "",
            "MPN": "RC0402FR-0710KL",
            "MPN_ALT": "WR04X1002FTL",
            "Part number": "",
        },
        name="R34",
    )
    r35 = Part(
        refs.get("R35", "R35"),
        "TinyTapeout:R_Small",
        footprint="Resistor_SMD:R_0402_1005Metric",
        footprint_definition="Resistor_SMD:R_0402_1005Metric_14",
        value="10k",
        properties={
            "Characteristics": "10k 0402",
            "JLC": "",
            "MPN": "RC0402FR-0710KL",
            "MPN_ALT": "WR04X1002FTL",
            "Part number": "",
        },
        name="R35",
    )
    r36 = Part(
        refs.get("R36", "R36"),
        "TinyTapeout:R_Small",
        footprint="Resistor_SMD:R_0402_1005Metric",
        footprint_definition="Resistor_SMD:R_0402_1005Metric_15",
        value="10k",
        properties={"Characteristics": "10k 0402", "MPN": "RC0402FR-0710KL", "MPN_ALT": "WR04X1002FTL"},
        name="R36",
    )
    r37 = Part(
        refs.get("R37", "R37"),
        "TinyTapeout:R_Small",
        footprint="Resistor_SMD:R_0402_1005Metric",
        footprint_definition="Resistor_SMD:R_0402_1005Metric_16",
        value="1k",
        properties={
            "Characteristics": "1k 0402",
            "MPN": "CR0402-FX-1001GLF",
            "MPN_ALT": "WR04X1001FTL",
            "Part number": "",
        },
        name="R37",
    )
    r38 = Part(
        refs.get("R38", "R38"),
        "TinyTapeout:R_Small",
        footprint="Resistor_SMD:R_0402_1005Metric",
        footprint_definition="Resistor_SMD:R_0402_1005Metric_17",
        value="10k",
        properties={
            "Characteristics": "10k 0402",
            "JLC": "",
            "MPN": "RC0402FR-0710KL",
            "MPN_ALT": "WR04X1002FTL",
            "Part number": "",
        },
        name="R38",
    )
    r39 = Part(
        refs.get("R39", "R39"),
        "TinyTapeout:R_Small",
        footprint="Resistor_SMD:R_0402_1005Metric",
        footprint_definition="Resistor_SMD:R_0402_1005Metric_10",
        value="10k",
        properties={
            "Characteristics": "10k 0402",
            "JLC": "",
            "MPN": "RC0402FR-0710KL",
            "MPN_ALT": "WR04X1002FTL",
            "Part number": "",
        },
        name="R39",
    )
    r40 = Part(
        refs.get("R40", "R40"),
        "TinyTapeout:R_Small",
        footprint="Resistor_SMD:R_0402_1005Metric",
        footprint_definition="Resistor_SMD:R_0402_1005Metric_18",
        value="10k",
        properties={
            "Characteristics": "10k 0402",
            "JLC": "",
            "MPN": "RC0402FR-0710KL",
            "MPN_ALT": "WR04X1002FTL",
            "Part number": "",
        },
        name="R40",
    )
    u5 = Part(
        refs.get("U5", "U5"),
        "TinyTapeout:W25Q32JVSS",
        footprint="Package_SO:SOIC-8_5.23x5.23mm_P1.27mm",
        value="W25Q32JVSS",
        properties={"Characteristics": "", "DigikeyPN": "W25Q32JVSSIQ-ND", "MPN": "W25Q32JVSSIQ"},
        name="U5",
    )
    u6 = Part(
        refs.get("U6", "U6"),
        "TinyTapeout:RP2040",
        footprint="Package_DFN_QFN:QFN-56-1EP_7x7mm_P0.4mm_EP3.2x3.2mm",
        value="RP2040",
        properties={"DigikeyPN": "2648-SC0914(13)CT-ND", "MPN": "SC0914(13)"},
        name="U6",
    )
    y1 = Part(
        refs.get("Y1", "Y1"),
        "TinyTapeout:Crystal_GND24",
        footprint="Crystal:Crystal_SMD_3225-4Pin_3.2x2.5mm",
        value="12.0MHz",
        properties={"DigikeyPN": "1923-830108206909DKR-ND", "MPN": "830108206909"},
        name="Y1",
    )
    module.add(
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
    connect(
        net_3v3,
        c31["2"],
        c33["1"],
        c34["1"],
        c35["1"],
        c36["1"],
        c37["1"],
        c38["1"],
        c39["1"],
        j11["1"],
        r34["1"],
        r35["1"],
        r36["1"],
        r38["1"],
        r39["1"],
        r40["1"],
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
    )
    connect(rp2040_dvdd, c32["2"], c40["1"], c41["1"], u6["23"], u6["45"], u6["50"])
    connect(rp2040_qspi_clk, j11["3"], r34["2"], u5["6"], u6["52"])
    connect(rp2040_qspi_sd0, j11["4"], r39["2"], u5["5"], u6["53"])
    connect(rp2040_qspi_sd1, j11["5"], r40["2"], u5["2"], u6["55"])
    connect(rp2040_qspi_sd2, r35["2"], u5["3"], u6["54"])
    connect(rp2040_qspi_sd3, r38["2"], u5["7"], u6["51"])
    connect(rp2040_run, j10["2"], r36["2"], u6["26"])
    connect(rp2040_swclk, u6["24"])
    connect(rp2040_swdio, u6["25"])
    connect(
        gnd,
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
        j10["1"],
        j11["6"],
        u5["4"],
        u6["19"],
        u6["57"],
        y1["2"],
        y1["4"],
    )
    connect(hk_csb, u6["3"])
    connect(hk_sck, u6["4"])
    connect(net_c30_pad1, c30["1"], r37["1"], y1["3"])
    connect(net_u6_xin, c29["1"], u6["20"], y1["1"])
    connect(net_u6_xout, r37["2"], u6["21"])
    connect(rpio29, u6["41"])
    connect(rp_proj_clk, u6["2"])
    connect(sdi_out0, u6["5"])
    connect(sdo_out1, u6["6"])
    connect(boot_mode, j11["2"], u5["1"], u6["56"])
    connect(cinc_out3, u6["11"])
    connect(ctrl_ena, u6["8"])
    connect(in0, u6["12"])
    connect(in1, u6["13"])
    connect(in2, u6["14"])
    connect(in3, u6["15"])
    connect(in4, u6["28"])
    connect(in5, u6["29"])
    connect(in6, u6["30"])
    connect(in7, u6["31"])
    connect(out4, u6["16"])
    connect(out5, u6["17"])
    connect(out6, u6["18"])
    connect(out7, u6["27"])
    connect(uio0, u6["32"])
    connect(uio1, u6["34"])
    connect(uio2, u6["35"])
    connect(uio3, u6["36"])
    connect(uio4, u6["37"])
    connect(uio5, u6["38"])
    connect(uio6, u6["39"])
    connect(uio7, u6["40"])
    connect(usb_d, u6["47"])
    connect(usb_d_2, u6["46"])
    connect(crst_out2, u6["9"])
    connect(project_rst, u6["7"])
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
    return module
