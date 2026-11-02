# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/video@97acc80c223d75520c03fc44cab63cd9a3202c42 by Fenolite 0.7.0.dev0 on 2026-10-31;
# modified: format conversion to the Fenolite DSL.

from fenolite.dsl import Module, Net, Part, connect, mm


def sheet(design, *, path, refs=None, **nets):
    module = Module(path.rsplit("/", 1)[-1])
    design.add(module)
    refs = refs or {}
    net_5v = nets["net_5v"]
    pcrd = nets["pcrd"]
    pcwr = nets["pcwr"]
    acces_ram = nets["acces_ram"]
    acq_on = nets["acq_on"]
    adr2 = nets["adr2"]
    adr3 = nets["adr3"]
    adr4 = nets["adr4"]
    adr5 = nets["adr5"]
    adr6 = nets["adr6"]
    be_0 = nets["be_0"]
    be_1 = nets["be_1"]
    be_2 = nets["be_2"]
    be_3 = nets["be_3"]
    blank = nets["blank"]
    bpclk = nets["bpclk"]
    bt812_rd = nets["bt812_rd"]
    bt812_wr = nets["bt812_wr"]
    cas0 = nets["cas0"]
    cas1 = nets["cas1"]
    cas2 = nets["cas2"]
    cas3 = nets["cas3"]
    clamp = nets["clamp"]
    clkcad = nets["clkcad"]
    clkcda = nets["clkcda"]
    csync_out = nets["csync_out"]
    csyncin = nets["csyncin"]
    dq0 = nets["dq0"]
    dq1 = nets["dq1"]
    dq10 = nets["dq10"]
    dq11 = nets["dq11"]
    dq12 = nets["dq12"]
    dq13 = nets["dq13"]
    dq14 = nets["dq14"]
    dq15 = nets["dq15"]
    dq2 = nets["dq2"]
    dq3 = nets["dq3"]
    dq4 = nets["dq4"]
    dq5 = nets["dq5"]
    dq6 = nets["dq6"]
    dq7 = nets["dq7"]
    dq8 = nets["dq8"]
    dq9 = nets["dq9"]
    f_palin = nets["f_palin"]
    hd_pal = nets["hd_pal"]
    irq = nets["irq"]
    irq_srl = nets["irq_srl"]
    mxa0 = nets["mxa0"]
    mxa1 = nets["mxa1"]
    mxa10 = nets["mxa10"]
    mxa2 = nets["mxa2"]
    mxa3 = nets["mxa3"]
    mxa4 = nets["mxa4"]
    mxa5 = nets["mxa5"]
    mxa6 = nets["mxa6"]
    mxa7 = nets["mxa7"]
    mxa8 = nets["mxa8"]
    mxa9 = nets["mxa9"]
    pca0 = nets["pca0"]
    pca1 = nets["pca1"]
    pca2 = nets["pca2"]
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
    ras0 = nets["ras0"]
    ras1 = nets["ras1"]
    ras2 = nets["ras2"]
    ras3 = nets["ras3"]
    ras4 = nets["ras4"]
    ras5 = nets["ras5"]
    ras6 = nets["ras6"]
    ras7 = nets["ras7"]
    rdcad = nets["rdcad"]
    rdcda = nets["rdcda"]
    rdempty = nets["rdempty"]
    rdfifo = nets["rdfifo"]
    select = nets["select"]
    sysrst = nets["sysrst"]
    tvi0 = nets["tvi0"]
    tvi1 = nets["tvi1"]
    vd_pal = nets["vd_pal"]
    wram = nets["wram"]
    wrcad = nets["wrcad"]
    wrcda = nets["wrcda"]
    wrfifdo = nets["wrfifdo"]
    wrfull = nets["wrfull"]
    write_ram = nets["write_ram"]
    x_clk = nets["x_clk"]
    x_data = nets["x_data"]
    x_done = nets["x_done"]
    x_irq = nets["x_irq"]
    x_prog = nets["x_prog"]
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
    gnd = nets["gnd"]
    net_c49_pad1 = Net("Net-(C49-Pad1)")
    net_d6_a = Net("Net-(D6-A)")
    net_p4_p1 = Net("Net-(P4-P1)")
    net_u23_p87 = Net("Net-(U23-P87)")
    net_u23_pgck4 = Net("Net-(U23-PGCK4)")
    net_u23_sgck3 = Net("Net-(U23-SGCK3)")
    c17 = Part(
        refs.get("C17", "C17"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
        value="100nF",
        name="C17",
    )
    c18 = Part(
        refs.get("C18", "C18"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_5",
        value="100nF",
        name="C18",
    )
    c19 = Part(
        refs.get("C19", "C19"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
        value="100nF",
        name="C19",
    )
    c20 = Part(
        refs.get("C20", "C20"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="100nF",
        name="C20",
    )
    c21 = Part(
        refs.get("C21", "C21"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="100nF",
        name="C21",
    )
    c22 = Part(
        refs.get("C22", "C22"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="100nF",
        name="C22",
    )
    c23 = Part(
        refs.get("C23", "C23"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="100nF",
        name="C23",
    )
    c49 = Part(
        refs.get("C49", "C49"),
        "video_schlib:C",
        footprint="footprints:C_Disc_D3.0mm_W2.0mm_P2.50mm",
        value="22pF",
        name="C49",
    )
    c50 = Part(
        refs.get("C50", "C50"),
        "video_schlib:C",
        footprint="footprints:C_Disc_D3.0mm_W2.0mm_P2.50mm",
        footprint_definition="footprints:C_Disc_D3.0mm_W2.0mm_P2.50mm_2",
        value="22pF",
        name="C50",
    )
    c56 = Part(
        refs.get("C56", "C56"),
        "video_schlib:CP",
        footprint="footprints:CP_EIA-3528-21_Kemet-B_Pad1.50x2.35mm_HandSolder",
        value="4.7uF",
        name="C56",
    )
    c57 = Part(
        refs.get("C57", "C57"),
        "video_schlib:CP",
        footprint="footprints:CP_EIA-3528-21_Kemet-B_Pad1.50x2.35mm_HandSolder",
        value="4.7uF",
        name="C57",
    )
    c63 = Part(
        refs.get("C63", "C63"),
        "video_schlib:CP",
        footprint="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder",
        footprint_definition="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_7",
        value="47uF",
        name="C63",
    )
    c70 = Part(
        refs.get("C70", "C70"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
        value="100nF",
        name="C70",
    )
    c71 = Part(
        refs.get("C71", "C71"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
        value="100nF",
        name="C71",
    )
    c72 = Part(
        refs.get("C72", "C72"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_21",
        value="100nF",
        name="C72",
    )
    c73 = Part(
        refs.get("C73", "C73"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="100nF",
        name="C73",
    )
    d6 = Part(
        refs.get("D6", "D6"),
        "video_schlib:LED",
        footprint="footprints:LED_D3.0mm",
        value="LED",
        name="D6",
    )
    p10 = Part(
        refs.get("P10", "P10"),
        "video_schlib:CONN_1",
        footprint="footprints:PinHeader_1x01_P2.54mm_Vertical",
        value="CONN_1",
        name="P10",
    )
    p11 = Part(
        refs.get("P11", "P11"),
        "video_schlib:CONN_1",
        footprint="footprints:PinHeader_1x01_P2.54mm_Vertical",
        footprint_definition="footprints:PinHeader_1x01_P2.54mm_Vertical_2",
        value="CONN_1",
        name="P11",
    )
    p12 = Part(
        refs.get("P12", "P12"),
        "video_schlib:CONN_1",
        footprint="footprints:PinHeader_1x01_P2.54mm_Vertical",
        footprint_definition="footprints:PinHeader_1x01_P2.54mm_Vertical_3",
        value="CONN_1",
        name="P12",
    )
    p4 = Part(
        refs.get("P4", "P4"),
        "video_schlib:CONN_2",
        footprint="footprints:PinHeader_1x02_P2.54mm_Vertical",
        value="CONN_2",
        name="P4",
    )
    p5 = Part(
        refs.get("P5", "P5"),
        "video_schlib:CONN_5",
        footprint="footprints:PinHeader_1x05_P2.54mm_Vertical",
        value="CONN_5",
        name="P5",
    )
    p9 = Part(
        refs.get("P9", "P9"),
        "video_schlib:CONN_1",
        footprint="footprints:PinHeader_1x01_P2.54mm_Vertical",
        footprint_definition="footprints:PinHeader_1x01_P2.54mm_Vertical_2",
        value="CONN_1",
        name="P9",
    )
    r1 = Part(
        refs.get("R1", "R1"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_22",
        value="10",
        properties={"Champ7": ""},
        name="R1",
    )
    r13 = Part(
        refs.get("R13", "R13"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="1K",
        name="R13",
    )
    r21 = Part(
        refs.get("R21", "R21"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
        value="220",
        name="R21",
    )
    r26 = Part(
        refs.get("R26", "R26"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="220K",
        name="R26",
    )
    r48 = Part(
        refs.get("R48", "R48"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="10K",
        properties={"Champ7": ""},
        name="R48",
    )
    u2 = Part(
        refs.get("U2", "U2"),
        "video_schlib:4C4001",
        footprint="footprints:SOIC-28W_7.5x17.9mm_P1.27mm",
        value="4C4001",
        name="U2",
    )
    u21 = Part(
        refs.get("U21", "U21"),
        "video_schlib:XC1736APD8",
        footprint="footprints:DIP-8_W7.62mm",
        value="XC1736APD8",
        name="U21",
    )
    u23 = Part(
        refs.get("U23", "U23"),
        "video_schlib:XC4005-PQ100",
        footprint="footprints:PQFP-100_14x20mm_P0.65mm",
        value="XC4003/PQ100",
        name="U23",
    )
    u24 = Part(
        refs.get("U24", "U24"),
        "video_schlib:XC4005-PQ160",
        footprint="footprints:PQFP-160_28x28mm_P0.65mm",
        footprint_definition="footprints:PQFP-160_28x28mm_P0.65mm_2",
        value="XC4005-PQ160",
        name="U24",
    )
    u7 = Part(
        refs.get("U7", "U7"),
        "video_schlib:AV9173",
        footprint="footprints:SSOP-8_3.95x5.21x3.27mm_P1.27mm",
        value="AV9173",
        name="U7",
    )
    x1 = Part(
        refs.get("X1", "X1"),
        "video_schlib:CRYSTAL",
        footprint="footprints:Crystal_HC18-U_Vertical",
        value="10MHz",
        name="X1",
    )
    module.add(
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
    connect(
        net_5v,
        c17["1"],
        c18["1"],
        c19["1"],
        c20["1"],
        c21["1"],
        c22["1"],
        c56["1"],
        c57["1"],
        c70["1"],
        c71["1"],
        c72["1"],
        c73["1"],
        r1["2"],
        r13["1"],
        r48["1"],
        u2["10"],
        u21["7"],
        u21["8"],
        u23["15"],
        u23["28"],
        u23["3"],
        u23["40"],
        u23["54"],
        u23["66"],
        u23["78"],
        u23["92"],
        u24["100"],
        u24["120"],
        u24["142"],
        u24["160"],
        u24["20"],
        u24["38"],
        u24["40"],
        u24["41"],
        u24["42"],
        u24["60"],
        u24["81"],
    )
    connect(pcrd, u23["46"], u24["133"])
    connect(pcwr, u23["47"], u24["132"])
    connect(acces_ram, u24["56"])
    connect(acq_on, u24["48"])
    connect(adr2, u23["48"], u24["137"])
    connect(adr3, u23["44"], u24["138"])
    connect(adr4, u23["43"], u24["139"])
    connect(adr5, u23["42"], u24["140"])
    connect(adr6, u23["39"], u24["143"])
    connect(be_0, u23["38"], u24["144"])
    connect(be_1, u23["37"], u24["145"])
    connect(be_2, u23["36"], u24["146"])
    connect(be_3, u23["35"], u24["147"])
    connect(blank, u24["53"])
    connect(bpclk, u23["30"])
    connect(bt812_rd, u23["71"])
    connect(bt812_wr, u23["70"])
    connect(cas0, u24["57"])
    connect(cas1, u24["58"])
    connect(cas2, u24["59"])
    connect(cas3, u24["62"])
    connect(clamp, u24["75"])
    connect(clkcad, u24["77"])
    connect(clkcda, u24["76"])
    connect(csync_out, u24["13"])
    connect(csyncin, u24["54"])
    connect(dq0, u23["13"], u24["21"])
    connect(dq1, u23["12"], u24["22"])
    connect(dq10, u23["95"], u24["34"])
    connect(dq11, u23["94"], u24["35"])
    connect(dq12, u23["93"], u24["36"])
    connect(dq13, u23["90"], u24["45"])
    connect(dq14, u23["88"], u24["46"])
    connect(dq15, u23["89"], u24["47"])
    connect(dq2, u23["11"], u24["23"])
    connect(dq3, u23["7"], u24["24"])
    connect(dq4, u23["9"], u24["25"])
    connect(dq5, u23["8"], u24["26"])
    connect(dq6, u23["6"], u24["27"])
    connect(dq7, u23["5"], u24["28"])
    connect(dq8, u23["97"], u24["32"])
    connect(dq9, u23["96"], u24["33"])
    connect(f_palin, u24["43"])
    connect(hd_pal, u24["52"])
    connect(irq, u24["149"])
    connect(irq_srl, u24["134"])
    connect(mxa0, u24["128"])
    connect(mxa1, u24["127"])
    connect(mxa10, u24["109"])
    connect(mxa2, u24["126"])
    connect(mxa3, u24["125"])
    connect(mxa4, u24["124"])
    connect(mxa5, u24["123"])
    connect(mxa6, u24["116"])
    connect(mxa7, u24["115"])
    connect(mxa8, u24["114"])
    connect(mxa9, u24["113"])
    connect(pca0, u23["65"])
    connect(pca1, u23["64"])
    connect(pca2, u23["63"])
    connect(ptadr, u23["24"], u24["14"])
    connect(ptatn, u23["18"], u24["4"])
    connect(ptbe_0, u23["20"], u24["158"])
    connect(ptbe_1, u23["21"], u24["157"])
    connect(ptbe_2, u23["22"], u24["156"])
    connect(ptbe_3, u23["23"], u24["155"])
    connect(ptburst, u23["17"], u24["5"])
    connect(ptnum0, u23["34"], u24["150"])
    connect(ptnum1, u23["32"], u24["154"])
    connect(ptrdy, u23["19"], u24["3"])
    connect(ptwr, u23["16"], u24["12"])
    connect(ras0, u24["74"])
    connect(ras1, u24["73"])
    connect(ras2, u24["69"])
    connect(ras3, u24["68"])
    connect(ras4, u24["67"])
    connect(ras5, u24["66"])
    connect(ras6, u24["65"])
    connect(ras7, u24["64"])
    connect(rdcad, u23["74"])
    connect(rdcda, u23["72"])
    connect(rdempty, u24["15"])
    connect(rdfifo, u24["16"])
    connect(select, u23["45"], u24["135"])
    connect(sysrst, u23["1"], u24["148"])
    connect(tvi0, u24["108"])
    connect(tvi1, u24["107"])
    connect(vd_pal, u24["37"])
    connect(wram, u24["63"])
    connect(wrcad, u23["69"])
    connect(wrcda, u23["73"])
    connect(wrfifdo, u24["18"])
    connect(wrfull, u24["17"])
    connect(write_ram, u24["55"])
    connect(x_clk, u23["86"], u24["119"])
    connect(x_data, u24["118"])
    connect(x_done, u23["83"], u24["80"])
    connect(x_irq, u24["11"])
    connect(x_prog, u23["84"], u24["82"])
    connect(graphic_14mhzout, u24["95"], u7["6"])
    connect(graphic_cclk, p5["2"], u21["2"], u23["77"])
    connect(graphic_clk10mhz, r21["2"], u23["57"], u24["2"])
    connect(graphic_csio, u23["61"], u24["159"])
    connect(graphic_din, p5["3"], u21["1"], u23["75"])
    connect(graphic_done, p5["4"], u23["53"])
    connect(graphic_hdout, u24["7"], u7["1"])
    connect(graphic_hdrefout, u24["6"], u7["2"])
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
    connect(
        gnd,
        c17["2"],
        c18["2"],
        c19["2"],
        c20["2"],
        c21["2"],
        c22["2"],
        c23["2"],
        c49["2"],
        c50["2"],
        c56["2"],
        c57["2"],
        c63["2"],
        c70["2"],
        c71["2"],
        c72["2"],
        c73["2"],
        p12["1"],
        p4["2"],
        p5["1"],
        u2["20"],
        u21["5"],
        u23["14"],
        u23["26"],
        u23["4"],
        u23["41"],
        u23["52"],
        u23["67"],
        u23["80"],
        u23["91"],
        u24["1"],
        u24["10"],
        u24["101"],
        u24["110"],
        u24["122"],
        u24["131"],
        u24["141"],
        u24["151"],
        u24["19"],
        u24["29"],
        u24["39"],
        u24["51"],
        u24["61"],
        u24["70"],
        u24["79"],
        u24["91"],
        u7["3"],
    )
    connect(net_c49_pad1, c49["1"], r21["1"], r26["2"], x1["1"])
    connect(net_d6_a, d6["1"], r13["2"])
    connect(net_p4_p1, p4["1"], r48["2"], u23["25"], u23["27"], u23["29"])
    connect(net_u23_p87, p10["1"], u23["87"])
    connect(net_u23_pgck4, p11["1"], u23["82"])
    connect(net_u23_sgck3, p9["1"], u23["51"])
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
    p10.place(mm("-10.465"), mm("-40.945"))
    p11.place(mm("-10.465"), mm("-36.5"))
    p12.place(mm("-17.577"), mm("-42.088"))
    p4.place(mm("5.664"), mm("-29.642"), rot=180)
    p5.place(mm("-6.655"), mm("-38.405"), rot=90)
    p9.place(mm("14.3"), mm("-25.07"))
    r1.place(mm("23.825"), mm("-36.881"))
    r13.place(mm("-14.104745"), mm("-24.458838"), side="bottom")
    r21.place(mm("9.855"), mm("-32.436"), rot=180, side="bottom")
    r26.place(mm("11.887"), mm("-37.897"), side="bottom")
    r48.place(mm("8.331"), mm("-13.259"), side="bottom")
    u2.place(mm("48.717"), mm("-36.754"), rot=90)
    u21.place(mm("-5.385"), mm("-26.975"), rot=90)
    u23.place(mm("3.505"), mm("-13.132"), rot=90)
    u24.place(mm("41.605"), mm("-11.835"), rot=90)
    u7.place(mm("30.175"), mm("-38.405"), rot=90)
    x1.place(mm("14.427"), mm("-40.31"), rot=180)
    return module
