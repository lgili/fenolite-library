# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/video@97acc80c223d75520c03fc44cab63cd9a3202c42 by Fenolite 0.7.0.dev0 on 2026-10-31;
# modified: format conversion to the Fenolite DSL.

from fenolite.dsl import Module, Net, Part, connect, mm


def sheet(design, *, path, refs=None, **nets):
    module = Module(path.rsplit("/", 1)[-1])
    design.add(module)
    refs = refs or {}
    net_3_3v = Net("+3.3V")
    net_5v = nets["net_5v"]
    pcrd = nets["pcrd"]
    pcwr = nets["pcwr"]
    adr2 = nets["adr2"]
    adr3 = nets["adr3"]
    adr4 = nets["adr4"]
    adr5 = nets["adr5"]
    adr6 = nets["adr6"]
    be_0 = nets["be_0"]
    be_1 = nets["be_1"]
    be_2 = nets["be_2"]
    be_3 = nets["be_3"]
    bpclk = nets["bpclk"]
    dq0 = nets["dq0"]
    dq1 = nets["dq1"]
    dq10 = nets["dq10"]
    dq11 = nets["dq11"]
    dq12 = nets["dq12"]
    dq13 = nets["dq13"]
    dq14 = nets["dq14"]
    dq15 = nets["dq15"]
    dq16 = nets["dq16"]
    dq17 = nets["dq17"]
    dq18 = nets["dq18"]
    dq19 = nets["dq19"]
    dq2 = nets["dq2"]
    dq20 = nets["dq20"]
    dq21 = nets["dq21"]
    dq22 = nets["dq22"]
    dq23 = nets["dq23"]
    dq24 = nets["dq24"]
    dq25 = nets["dq25"]
    dq26 = nets["dq26"]
    dq27 = nets["dq27"]
    dq28 = nets["dq28"]
    dq29 = nets["dq29"]
    dq3 = nets["dq3"]
    dq30 = nets["dq30"]
    dq31 = nets["dq31"]
    dq4 = nets["dq4"]
    dq5 = nets["dq5"]
    dq6 = nets["dq6"]
    dq7 = nets["dq7"]
    dq8 = nets["dq8"]
    dq9 = nets["dq9"]
    irq = nets["irq"]
    irq_srl = nets["irq_srl"]
    ptadr = nets["ptadr"]
    ptatn = nets["ptatn"]
    ptbe_0 = nets["ptbe_0"]
    ptbe_1 = nets["ptbe_1"]
    ptbe_2 = nets["ptbe_2"]
    ptbe_3 = nets["ptbe_3"]
    ptburst = nets["ptburst"]
    ptnum0 = nets["ptnum0"]
    ptnum1 = nets["ptnum1"]
    ptrdy = nets["ptrdy"]
    ptwr = nets["ptwr"]
    rdempty = nets["rdempty"]
    rdfifo = nets["rdfifo"]
    select = nets["select"]
    sysrst = nets["sysrst"]
    wrfifdo = nets["wrfifdo"]
    wrfull = nets["wrfull"]
    x_irq = nets["x_irq"]
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
    gnd = nets["gnd"]
    net_bus1_prsnt1 = Net("Net-(BUS1-PRSNT1#)")
    net_bus1_prsnt2 = Net("Net-(BUS1-PRSNT2#)")
    net_bus1_tdi = Net("Net-(BUS1-TDI)")
    net_u1_scl = Net("Net-(U1-SCL)")
    net_u1_sda = Net("Net-(U1-SDA)")
    net_u11_flt = Net("Net-(U11-FLT#)")
    net_u11_mode_16_32 = Net("Net-(U11-MODE_16/32)")
    net_u11_snv = Net("Net-(U11-SNV)")
    bus1 = Part(
        refs.get("BUS1", "BUS1"),
        "video_schlib:BUSPCI-5V",
        footprint="footprints:BUSPCI",
        value="BUSPCI_5V",
        name="BUS1",
    )
    c24 = Part(
        refs.get("C24", "C24"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="100nF",
        name="C24",
    )
    c25 = Part(
        refs.get("C25", "C25"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
        value="100nF",
        name="C25",
    )
    c26 = Part(
        refs.get("C26", "C26"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
        value="100nF",
        name="C26",
    )
    c27 = Part(
        refs.get("C27", "C27"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="100nF",
        name="C27",
    )
    c28 = Part(
        refs.get("C28", "C28"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
        value="100nF",
        name="C28",
    )
    c29 = Part(
        refs.get("C29", "C29"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
        value="100nF",
        name="C29",
    )
    c30 = Part(
        refs.get("C30", "C30"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="100nF",
        name="C30",
    )
    c31 = Part(
        refs.get("C31", "C31"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="100nF",
        name="C31",
    )
    c38 = Part(
        refs.get("C38", "C38"),
        "video_schlib:CP",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
        value="4,7uF",
        name="C38",
    )
    c67 = Part(
        refs.get("C67", "C67"),
        "video_schlib:CP",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
        value="4,7uF",
        name="C67",
    )
    c68 = Part(
        refs.get("C68", "C68"),
        "video_schlib:CP",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
        value="4,7uF",
        name="C68",
    )
    c69 = Part(
        refs.get("C69", "C69"),
        "video_schlib:CP",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="4,7uF",
        name="C69",
    )
    r28 = Part(
        refs.get("R28", "R28"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        value="2,2K",
        name="R28",
    )
    r29 = Part(
        refs.get("R29", "R29"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        value="2,2K",
        name="R29",
    )
    r5 = Part(
        refs.get("R5", "R5"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="10K",
        name="R5",
    )
    r6 = Part(
        refs.get("R6", "R6"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
        value="10K",
        name="R6",
    )
    r7 = Part(
        refs.get("R7", "R7"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
        value="10K",
        name="R7",
    )
    rr1 = Part(
        refs.get("RR1", "RR1"),
        "video_schlib:RR8",
        footprint="footprints:R_Array_SIP9",
        value="8x10K",
        name="RR1",
    )
    rr2 = Part(
        refs.get("RR2", "RR2"),
        "video_schlib:RR8",
        footprint="footprints:R_Array_SIP9",
        value="8x10K",
        name="RR2",
    )
    rr3 = Part(
        refs.get("RR3", "RR3"),
        "video_schlib:RR8",
        footprint="footprints:R_Array_SIP9",
        footprint_definition="footprints:R_Array_SIP9_2",
        value="8x10K",
        name="RR3",
    )
    rr4 = Part(
        refs.get("RR4", "RR4"),
        "video_schlib:RR8",
        footprint="footprints:R_Array_SIP9",
        footprint_definition="footprints:R_Array_SIP9_3",
        value="8x10K",
        name="RR4",
    )
    rr5 = Part(
        refs.get("RR5", "RR5"),
        "video_schlib:RR8",
        footprint="footprints:R_Array_SIP9",
        footprint_definition="footprints:R_Array_SIP9_3",
        value="8x10K",
        name="RR5",
    )
    rr6 = Part(
        refs.get("RR6", "RR6"),
        "video_schlib:RR8",
        footprint="footprints:R_Array_SIP9",
        footprint_definition="footprints:R_Array_SIP9_3",
        value="8x10K",
        name="RR6",
    )
    rr7 = Part(
        refs.get("RR7", "RR7"),
        "video_schlib:RR8",
        footprint="footprints:R_Array_SIP9",
        footprint_definition="footprints:R_Array_SIP9_4",
        value="8x10K",
        name="RR7",
    )
    rr8 = Part(
        refs.get("RR8", "RR8"),
        "video_schlib:RR8",
        footprint="footprints:R_Array_SIP9",
        footprint_definition="footprints:R_Array_SIP9_5",
        value="8x10K",
        name="RR8",
    )
    u1 = Part(
        refs.get("U1", "U1"),
        "video_schlib:24C16",
        footprint="footprints:DIP-8_W7.62mm",
        value="24C16",
        name="U1",
    )
    u11 = Part(
        refs.get("U11", "U11"),
        "video_schlib:S5933_PQ160",
        footprint="footprints:PQFP-160_28x28mm_P0.65mm",
        footprint_definition="footprints:PQFP-160_28x28mm_P0.65mm_2",
        value="S5933_PQ160",
        name="U11",
    )
    w1 = Part(
        refs.get("W1", "W1"),
        "video_schlib:TEST",
        footprint="footprints:SolderJumper-2_P1.3mm_Open_Pad1.0x1.5mm",
        value="16/32",
        name="W1",
    )
    w2 = Part(
        refs.get("W2", "W2"),
        "video_schlib:TEST",
        footprint="footprints:SolderJumper-2_P1.3mm_Open_Pad1.0x1.5mm",
        footprint_definition="footprints:SolderJumper-2_P1.3mm_Open_Pad1.0x1.5mm_2",
        value="FLOAT#",
        name="W2",
    )
    w3 = Part(
        refs.get("W3", "W3"),
        "video_schlib:TEST",
        footprint="footprints:SolderJumper-2_P1.3mm_Open_Pad1.0x1.5mm",
        footprint_definition="footprints:SolderJumper-2_P1.3mm_Open_Pad1.0x1.5mm_3",
        value="SERNV",
        name="W3",
    )
    w4 = Part(
        refs.get("W4", "W4"),
        "video_schlib:TEST",
        footprint="footprints:PinHeader_1x02_P2.54mm_Vertical",
        footprint_definition="footprints:PinHeader_1x02_P2.54mm_Vertical_2",
        value="TEST",
        name="W4",
    )
    w5 = Part(
        refs.get("W5", "W5"),
        "video_schlib:TEST",
        footprint="footprints:PinHeader_1x02_P2.54mm_Vertical",
        footprint_definition="footprints:PinHeader_1x02_P2.54mm_Vertical_3",
        value="TEST",
        name="W5",
    )
    module.add(
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
    connect(
        net_5v,
        bus1["A10"],
        bus1["A16"],
        bus1["A5"],
        bus1["A59"],
        bus1["A61"],
        bus1["A62"],
        bus1["A8"],
        bus1["B19"],
        bus1["B5"],
        bus1["B59"],
        bus1["B6"],
        bus1["B61"],
        bus1["B62"],
        c24["1"],
        c25["1"],
        c26["1"],
        c27["1"],
        c28["1"],
        c29["1"],
        c30["1"],
        c31["1"],
        c38["1"],
        c67["1"],
        r28["1"],
        r29["1"],
        r5["2"],
        r6["2"],
        r7["2"],
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
        u11["11"],
        u11["111"],
        u11["131"],
        u11["151"],
        u11["31"],
        u11["51"],
        u11["71"],
        u11["91"],
    )
    connect(pcrd, rr3["7"], u11["72"])
    connect(pcwr, rr3["5"], u11["74"])
    connect(adr2, u11["68"])
    connect(adr3, u11["67"])
    connect(adr4, u11["66"])
    connect(adr5, u11["64"])
    connect(adr6, u11["132"])
    connect(be_0, u11["87"])
    connect(be_1, u11["63"])
    connect(be_2, u11["62"])
    connect(be_3, u11["60"])
    connect(bpclk, u11["140"])
    connect(dq0, rr7["2"], u11["100"])
    connect(dq1, rr7["3"], u11["99"])
    connect(dq10, rr8["7"], u11["83"])
    connect(dq11, rr8["6"], u11["82"])
    connect(dq12, rr8["5"], u11["80"])
    connect(dq13, rr8["4"], u11["79"])
    connect(dq14, rr8["3"], u11["78"])
    connect(dq15, rr8["2"], u11["76"])
    connect(dq16, rr4["7"], u11["157"])
    connect(dq17, rr4["9"], u11["145"])
    connect(dq18, rr6["6"], u11["133"])
    connect(dq19, rr6["8"], u11["125"])
    connect(dq2, rr7["4"], u11["98"])
    connect(dq20, rr6["3"], u11["117"])
    connect(dq21, rr5["6"], u11["105"])
    connect(dq22, rr4["3"], u11["93"])
    connect(dq23, rr4["5"], u11["85"])
    connect(dq24, rr3["3"], u11["77"])
    connect(dq25, rr3["9"], u11["65"])
    connect(dq26, rr2["8"], u11["53"])
    connect(dq27, rr2["5"], u11["45"])
    connect(dq28, rr2["3"], u11["37"])
    connect(dq29, rr1["8"], u11["25"])
    connect(dq3, rr7["5"], u11["96"])
    connect(dq30, rr1["5"], u11["13"])
    connect(dq31, rr1["3"], u11["5"])
    connect(dq4, rr7["6"], u11["95"])
    connect(dq5, rr7["7"], u11["94"])
    connect(dq6, rr7["8"], u11["92"])
    connect(dq7, rr7["9"], u11["88"])
    connect(dq8, rr8["9"], u11["86"])
    connect(dq9, rr8["8"], u11["84"])
    connect(irq, u11["124"])
    connect(irq_srl, rr2["7"], u11["57"])
    connect(ptadr, rr5["5"], u11["107"])
    connect(ptatn, rr5["2"], u11["114"])
    connect(ptbe_0, u11["116"])
    connect(ptbe_1, u11["118"])
    connect(ptbe_2, u11["119"])
    connect(ptbe_3, u11["120"])
    connect(ptburst, u11["112"])
    connect(ptnum0, u11["123"])
    connect(ptnum1, u11["122"])
    connect(ptrdy, rr6["2"], u11["115"])
    connect(ptwr, u11["108"])
    connect(rdempty, u11["106"])
    connect(rdfifo, rr5["7"], u11["104"])
    connect(select, rr3["4"], u11["75"])
    connect(sysrst, u11["126"])
    connect(wrfifdo, rr5["8"], u11["102"])
    connect(wrfull, u11["103"])
    connect(x_irq, rr5["4"], u11["109"])
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
        bus1["B15"],
        bus1["B17"],
        bus1["B22"],
        bus1["B28"],
        bus1["B3"],
        bus1["B34"],
        bus1["B38"],
        bus1["B46"],
        bus1["B49"],
        bus1["B57"],
        c24["2"],
        c25["2"],
        c26["2"],
        c27["2"],
        c28["2"],
        c29["2"],
        c30["2"],
        c31["2"],
        c38["2"],
        c67["2"],
        c68["2"],
        c69["2"],
        u1["1"],
        u1["2"],
        u1["3"],
        u1["4"],
        u11["10"],
        u11["110"],
        u11["130"],
        u11["150"],
        u11["30"],
        u11["50"],
        u11["70"],
        u11["90"],
        w1["1"],
        w2["1"],
        w3["1"],
        w4["1"],
        w5["1"],
    )
    connect(net_bus1_prsnt1, bus1["B9"], w5["2"])
    connect(net_bus1_prsnt2, bus1["B11"], w4["2"])
    connect(net_bus1_tdi, bus1["A4"], bus1["B4"])
    connect(net_u1_scl, r28["2"], u1["6"], u11["128"])
    connect(net_u1_sda, r29["2"], u1["5"], u11["127"])
    connect(net_u11_flt, r6["1"], u11["138"], w2["2"])
    connect(net_u11_mode_16_32, r5["1"], u11["59"], w1["2"])
    connect(net_u11_snv, r7["1"], u11["135"], w3["2"])
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
    r28.place(mm("11.76"), mm("14.935"))
    r29.place(mm("14.3"), mm("11.76"))
    r5.place(mm("63.449"), mm("34.62"), side="bottom")
    r6.place(mm("14.935"), mm("23.19"), rot=180, side="bottom")
    r7.place(mm("18.745"), mm("20.65"), rot=180, side="bottom")
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
    return module
