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
    blank = nets["blank"]
    blue_in = nets["blue_in"]
    blue_out = nets["blue_out"]
    clamp = nets["clamp"]
    clkcad = nets["clkcad"]
    clkcda = nets["clkcda"]
    csync_out = nets["csync_out"]
    csyncin = nets["csyncin"]
    dq0 = nets["dq0"]
    dq1 = nets["dq1"]
    dq2 = nets["dq2"]
    dq3 = nets["dq3"]
    dq4 = nets["dq4"]
    dq5 = nets["dq5"]
    dq6 = nets["dq6"]
    dq7 = nets["dq7"]
    esvideo_rvb_oe_rvb = Net("/ESVIDEO-RVB/OE_RVB-")
    esvideo_rvb_ref = Net("/ESVIDEO-RVB/REF+")
    esvideo_rvb_vaa = Net("/ESVIDEO-RVB/VAA")
    green_in = nets["green_in"]
    green_out = nets["green_out"]
    oe_pal = nets["oe_pal"]
    pca0 = nets["pca0"]
    pca1 = nets["pca1"]
    pca2 = nets["pca2"]
    rdcad = nets["rdcad"]
    rdcda = nets["rdcda"]
    red_in = nets["red_in"]
    red_out = nets["red_out"]
    tvb0 = nets["tvb0"]
    tvb1 = nets["tvb1"]
    tvb2 = nets["tvb2"]
    tvb3 = nets["tvb3"]
    tvb4 = nets["tvb4"]
    tvb5 = nets["tvb5"]
    tvb6 = nets["tvb6"]
    tvb7 = nets["tvb7"]
    tvg0 = nets["tvg0"]
    tvg1 = nets["tvg1"]
    tvg2 = nets["tvg2"]
    tvg3 = nets["tvg3"]
    tvg4 = nets["tvg4"]
    tvg5 = nets["tvg5"]
    tvg6 = nets["tvg6"]
    tvg7 = nets["tvg7"]
    tvi0 = nets["tvi0"]
    tvi1 = nets["tvi1"]
    tvr0 = nets["tvr0"]
    tvr1 = nets["tvr1"]
    tvr2 = nets["tvr2"]
    tvr3 = nets["tvr3"]
    tvr4 = nets["tvr4"]
    tvr5 = nets["tvr5"]
    tvr6 = nets["tvr6"]
    tvr7 = nets["tvr7"]
    wrcad = nets["wrcad"]
    wrcda = nets["wrcda"]
    gnd = nets["gnd"]
    net_c36_pad2 = Net("Net-(C36-Pad2)")
    net_c39_pad2 = Net("Net-(C39-Pad2)")
    net_c40_pad2 = Net("Net-(C40-Pad2)")
    net_c41_pad2 = Net("Net-(C41-Pad2)")
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
    c32 = Part(
        refs.get("C32", "C32"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
        value="100nF",
        name="C32",
    )
    c33 = Part(
        refs.get("C33", "C33"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="100nF",
        name="C33",
    )
    c34 = Part(
        refs.get("C34", "C34"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_7",
        value="100nF",
        name="C34",
    )
    c35 = Part(
        refs.get("C35", "C35"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="100nF",
        name="C35",
    )
    c36 = Part(
        refs.get("C36", "C36"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_8",
        value="100nF",
        name="C36",
    )
    c37 = Part(
        refs.get("C37", "C37"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_9",
        value="100pF",
        name="C37",
    )
    c39 = Part(
        refs.get("C39", "C39"),
        "video_schlib:C",
        footprint="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder",
        value="1uF",
        name="C39",
    )
    c40 = Part(
        refs.get("C40", "C40"),
        "video_schlib:C",
        footprint="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder",
        footprint_definition="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_2",
        value="1uF",
        name="C40",
    )
    c41 = Part(
        refs.get("C41", "C41"),
        "video_schlib:C",
        footprint="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder",
        footprint_definition="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_3",
        value="1uF",
        name="C41",
    )
    c42 = Part(
        refs.get("C42", "C42"),
        "video_schlib:CP",
        footprint="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder",
        footprint_definition="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_4",
        value="2.2uF",
        name="C42",
    )
    c51 = Part(
        refs.get("C51", "C51"),
        "video_schlib:CP",
        footprint="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder",
        footprint_definition="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_5",
        value="22uF",
        name="C51",
    )
    c52 = Part(
        refs.get("C52", "C52"),
        "video_schlib:CP",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="22uF",
        name="C52",
    )
    l5 = Part(
        refs.get("L5", "L5"),
        "video_schlib:INDUCTOR",
        footprint="footprints:R_1812_4532Metric_Pad1.30x3.40mm_HandSolder",
        footprint_definition="footprints:R_1812_4532Metric_Pad1.30x3.40mm_HandSolder_2",
        value="22uH",
        name="L5",
    )
    r15 = Part(
        refs.get("R15", "R15"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_24",
        value="1M",
        name="R15",
    )
    r22 = Part(
        refs.get("R22", "R22"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_28",
        value="220",
        name="R22",
    )
    r23 = Part(
        refs.get("R23", "R23"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_18",
        value="220",
        name="R23",
    )
    r24 = Part(
        refs.get("R24", "R24"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_18",
        value="220",
        name="R24",
    )
    r36 = Part(
        refs.get("R36", "R36"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_36",
        value="470",
        name="R36",
    )
    r37 = Part(
        refs.get("R37", "R37"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_37",
        value="510",
        name="R37",
    )
    r38 = Part(
        refs.get("R38", "R38"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="510",
        name="R38",
    )
    r42 = Part(
        refs.get("R42", "R42"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_40",
        value="75",
        name="R42",
    )
    r43 = Part(
        refs.get("R43", "R43"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_41",
        value="75",
        name="R43",
    )
    r44 = Part(
        refs.get("R44", "R44"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_42",
        value="75",
        name="R44",
    )
    r45 = Part(
        refs.get("R45", "R45"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        value="75",
        name="R45",
    )
    r46 = Part(
        refs.get("R46", "R46"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_5",
        value="75",
        name="R46",
    )
    r47 = Part(
        refs.get("R47", "R47"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="75",
        name="R47",
    )
    r8 = Part(
        refs.get("R8", "R8"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_18",
        value="150",
        name="R8",
    )
    u8 = Part(
        refs.get("U8", "U8"),
        "video_schlib:BT253",
        footprint="footprints:PLCC84",
        value="BT253",
        name="U8",
    )
    u9 = Part(
        refs.get("U9", "U9"),
        "video_schlib:BT473",
        footprint="footprints:PLCC68",
        value="BT473",
        name="U9",
    )
    module.add(
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
    connect(net_5v, l5["1"])
    connect(blank, u9["7"])
    connect(blue_in, r22["1"], r46["1"])
    connect(blue_out, r44["2"], u9["39"])
    connect(clamp, u8["37"], u8["59"])
    connect(clkcad, u8["38"], u8["39"], u8["40"])
    connect(clkcda, u9["9"])
    connect(csync_out, u9["8"])
    connect(csyncin, u8["8"])
    connect(dq0, u8["16"], u9["14"])
    connect(dq1, u8["15"], u9["15"])
    connect(dq2, u8["14"], u9["16"])
    connect(dq3, u8["13"], u9["17"])
    connect(dq4, u8["12"], u9["18"])
    connect(dq5, u8["11"], u9["19"])
    connect(dq6, u8["10"], u9["20"])
    connect(dq7, u8["9"], u9["21"])
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
    connect(green_in, r23["1"], r45["1"])
    connect(green_out, r43["2"], u9["38"])
    connect(oe_pal, u9["28"])
    connect(pca0, u8["17"], u9["24"])
    connect(pca1, u8["18"], u9["25"])
    connect(pca2, u8["19"], u9["26"])
    connect(rdcad, u8["20"])
    connect(rdcda, u9["22"])
    connect(red_in, r24["1"], r47["1"])
    connect(red_out, r42["2"], u9["37"])
    connect(tvb0, u8["32"], u9["61"])
    connect(tvb1, u8["31"], u9["62"])
    connect(tvb2, u8["30"], u9["63"])
    connect(tvb3, u8["29"], u9["64"])
    connect(tvb4, u8["28"], u9["65"])
    connect(tvb5, u8["27"], u9["66"])
    connect(tvb6, u8["26"], u9["67"])
    connect(tvb7, u8["25"], u9["68"])
    connect(tvg0, u8["48"], u9["53"])
    connect(tvg1, u8["47"], u9["54"])
    connect(tvg2, u8["46"], u9["55"])
    connect(tvg3, u8["45"], u9["56"])
    connect(tvg4, u8["36"], u9["57"])
    connect(tvg5, u8["35"], u9["58"])
    connect(tvg6, u8["34"], u9["59"])
    connect(tvg7, u8["33"], u9["60"])
    connect(tvi0, u9["10"])
    connect(tvi1, u9["11"])
    connect(tvr0, u8["56"], u9["45"])
    connect(tvr1, u8["55"], u9["46"])
    connect(tvr2, u8["54"], u9["47"])
    connect(tvr3, u8["53"], u9["48"])
    connect(tvr4, u8["52"], u9["49"])
    connect(tvr5, u8["51"], u9["50"])
    connect(tvr6, u8["50"], u9["51"])
    connect(tvr7, u8["49"], u9["52"])
    connect(wrcad, u8["24"])
    connect(wrcda, u9["23"])
    connect(
        gnd,
        c32["1"],
        c33["2"],
        c37["1"],
        c51["2"],
        c52["2"],
        r15["1"],
        r37["1"],
        r38["2"],
        r42["1"],
        r43["1"],
        r44["1"],
        r45["2"],
        r46["2"],
        r47["2"],
        r8["2"],
        u8["2"],
        u8["21"],
        u8["22"],
        u8["23"],
        u8["3"],
        u8["41"],
        u8["42"],
        u8["61"],
        u8["63"],
        u8["67"],
        u9["12"],
        u9["13"],
        u9["3"],
        u9["31"],
        u9["32"],
        u9["4"],
    )
    connect(net_c36_pad2, c36["2"], c37["2"], r36["1"])
    connect(net_c39_pad2, c39["2"], r24["2"])
    connect(net_c40_pad2, c40["2"], r23["2"])
    connect(net_c41_pad2, c41["2"], r22["2"])
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
    r8.place(mm("248.234"), mm("31.699"), rot=180)
    u8.place(mm("211.277"), mm("12.649"), rot=90)
    u9.place(mm("243.535"), mm("14.935"), rot=-90)
    return module
