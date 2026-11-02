# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/video@97acc80c223d75520c03fc44cab63cd9a3202c42 by Fenolite 0.7.0.dev0 on 2026-10-31;
# modified: format conversion to the Fenolite DSL.

from fenolite.dsl import Module, Net, Part, connect, mm


def sheet(design, *, path, refs=None, **nets):
    module = Module(path.rsplit("/", 1)[-1])
    design.add(module)
    refs = refs or {}
    net_5f = Net("+5F")
    net_5v = nets["net_5v"]
    blue_out = nets["blue_out"]
    csync_out = nets["csync_out"]
    c_out = nets["c_out"]
    green_out = nets["green_out"]
    red_out = nets["red_out"]
    y_out = nets["y_out"]
    modul_chrom = Net("/modul/CHROM")
    modul_cvbs = Net("/modul/CVBS")
    modul_cvbsout = nets["modul_cvbsout"]
    modul_lum = Net("/modul/LUM")
    gnd = nets["gnd"]
    net_c46_pad1 = Net("Net-(C46-Pad1)")
    net_c61_pad1 = Net("Net-(C61-Pad1)")
    net_cv1_pad1 = Net("Net-(CV1-Pad1)")
    net_l6_pad1 = Net("Net-(L6-Pad1)")
    net_pot1_pad3 = Net("Net-(POT1-Pad3)")
    net_q1_b = Net("Net-(Q1-B)")
    net_q1_e = Net("Net-(Q1-E)")
    net_q2_b = Net("Net-(Q2-B)")
    net_q2_e = Net("Net-(Q2-E)")
    net_q3_b = Net("Net-(Q3-B)")
    net_q3_e = Net("Net-(Q3-E)")
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
    c43 = Part(
        refs.get("C43", "C43"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="220nF",
        name="C43",
    )
    c44 = Part(
        refs.get("C44", "C44"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
        value="220nF",
        name="C44",
    )
    c45 = Part(
        refs.get("C45", "C45"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_11",
        value="220nF",
        name="C45",
    )
    c46 = Part(
        refs.get("C46", "C46"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_12",
        value="220pF",
        name="C46",
    )
    c48 = Part(
        refs.get("C48", "C48"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_14",
        value="22nF",
        name="C48",
    )
    c53 = Part(
        refs.get("C53", "C53"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_16",
        value="330pF",
        name="C53",
    )
    c54 = Part(
        refs.get("C54", "C54"),
        "video_schlib:CP",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_5",
        value="4.7uF",
        name="C54",
    )
    c55 = Part(
        refs.get("C55", "C55"),
        "video_schlib:CP",
        footprint="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder",
        footprint_definition="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_6",
        value="4.7uF",
        name="C55",
    )
    c58 = Part(
        refs.get("C58", "C58"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        value="47nF",
        name="C58",
    )
    c59 = Part(
        refs.get("C59", "C59"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_17",
        value="47nF",
        name="C59",
    )
    c60 = Part(
        refs.get("C60", "C60"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        value="47nF",
        name="C60",
    )
    c61 = Part(
        refs.get("C61", "C61"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_18",
        value="47nF",
        name="C61",
    )
    c64 = Part(
        refs.get("C64", "C64"),
        "video_schlib:CP",
        footprint="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder",
        footprint_definition="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_6",
        value="6,8uF",
        name="C64",
    )
    cv1 = Part(
        refs.get("CV1", "CV1"),
        "video_schlib:CTRIM",
        footprint="footprints:CV3-30PF",
        value="5/30pF",
        name="CV1",
    )
    l1 = Part(
        refs.get("L1", "L1"),
        "video_schlib:INDUCTOR",
        footprint="footprints:R_1812_4532Metric_Pad1.30x3.40mm_HandSolder",
        value="2,2uH",
        name="L1",
    )
    l2 = Part(
        refs.get("L2", "L2"),
        "video_schlib:INDUCTOR",
        footprint="footprints:R_1812_4532Metric_Pad1.30x3.40mm_HandSolder",
        footprint_definition="footprints:R_1812_4532Metric_Pad1.30x3.40mm_HandSolder_2",
        value="22uH",
        name="L2",
    )
    l3 = Part(
        refs.get("L3", "L3"),
        "video_schlib:INDUCTOR",
        footprint="footprints:R_1812_4532Metric_Pad1.30x3.40mm_HandSolder",
        value="22uH",
        name="L3",
    )
    l6 = Part(
        refs.get("L6", "L6"),
        "video_schlib:LIGNE_A_RETARD",
        footprint="footprints:LRTDK",
        value="470ns",
        name="L6",
    )
    pot1 = Part(
        refs.get("POT1", "POT1"),
        "video_schlib:POT",
        footprint="footprints:Potentiometer_Bourns_3314G_Vertical",
        value="100K",
        name="POT1",
    )
    q1 = Part(
        refs.get("Q1", "Q1"),
        "video_schlib:NPN",
        footprint="footprints:SOT23EBC",
        value="BC848",
        name="Q1",
    )
    q2 = Part(
        refs.get("Q2", "Q2"),
        "video_schlib:NPN",
        footprint="footprints:SOT23EBC",
        value="BC848",
        name="Q2",
    )
    q3 = Part(
        refs.get("Q3", "Q3"),
        "video_schlib:NPN",
        footprint="footprints:SOT23EBC",
        value="BC848",
        name="Q3",
    )
    r10 = Part(
        refs.get("R10", "R10"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_18",
        value="1K",
        name="R10",
    )
    r11 = Part(
        refs.get("R11", "R11"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        value="1K",
        name="R11",
    )
    r16 = Part(
        refs.get("R16", "R16"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
        value="220",
        name="R16",
    )
    r17 = Part(
        refs.get("R17", "R17"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
        value="220",
        name="R17",
    )
    r18 = Part(
        refs.get("R18", "R18"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_25",
        value="220",
        name="R18",
    )
    r30 = Part(
        refs.get("R30", "R30"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_31",
        value="3,3K",
        name="R30",
    )
    r31 = Part(
        refs.get("R31", "R31"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_32",
        value="470",
        name="R31",
    )
    r32 = Part(
        refs.get("R32", "R32"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="470",
        name="R32",
    )
    r33 = Part(
        refs.get("R33", "R33"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_33",
        value="470",
        name="R33",
    )
    r34 = Part(
        refs.get("R34", "R34"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_34",
        value="470",
        name="R34",
    )
    r39 = Part(
        refs.get("R39", "R39"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_38",
        value="68",
        name="R39",
    )
    r4 = Part(
        refs.get("R4", "R4"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        value="10K",
        properties={"Champ7": ""},
        name="R4",
    )
    r40 = Part(
        refs.get("R40", "R40"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
        value="68",
        name="R40",
    )
    r41 = Part(
        refs.get("R41", "R41"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_39",
        value="68",
        name="R41",
    )
    r9 = Part(
        refs.get("R9", "R9"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_5",
        value="150K",
        name="R9",
    )
    u20 = Part(
        refs.get("U20", "U20"),
        "video_schlib:TDA8501",
        footprint="footprints:SOIC-24W_7.5x15.4mm_P1.27mm",
        value="TDA8501",
        name="U20",
    )
    x3 = Part(
        refs.get("X3", "X3"),
        "video_schlib:CRYSTAL",
        footprint="footprints:Crystal_HC18-U_Horizontal",
        value="4.433618MHz",
        name="X3",
    )
    module.add(
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
    connect(net_5f, c55["1"], l3["2"], q1["3"], q2["3"], q3["3"])
    connect(net_5v, l2["1"], l3["1"], r4["2"])
    connect(blue_out, c60["2"])
    connect(csync_out, r30["2"])
    connect(c_out, r39["1"])
    connect(green_out, c59["2"])
    connect(red_out, c58["2"])
    connect(y_out, r40["2"])
    connect(modul_chrom, r16["2"], u20["14"])
    connect(modul_cvbs, r18["2"], u20["16"])
    connect(modul_cvbsout, r41["1"])
    connect(modul_lum, r17["2"], u20["19"])
    connect(
        gnd,
        c43["2"],
        c44["2"],
        c45["2"],
        c46["2"],
        c48["1"],
        c53["2"],
        c54["2"],
        c55["2"],
        c64["2"],
        cv1["2"],
        l6["3"],
        pot1["1"],
        pot1["2"],
        r31["1"],
        r32["2"],
        r33["2"],
        r34["2"],
        u20["10"],
        u20["17"],
    )
    connect(net_c46_pad1, c46["1"], c53["1"], l1["2"])
    connect(net_c61_pad1, c61["1"], r30["1"], r31["2"])
    connect(net_cv1_pad1, cv1["1"], x3["1"])
    connect(net_l6_pad1, l6["1"], r10["1"])
    connect(net_pot1_pad3, pot1["3"], r9["1"])
    connect(net_q1_b, q1["2"], r16["1"])
    connect(net_q1_e, q1["1"], r32["1"], r39["2"])
    connect(net_q2_b, q2["2"], r17["1"])
    connect(net_q2_e, q2["1"], r33["1"], r40["1"])
    connect(net_q3_b, q3["2"], r18["1"])
    connect(net_q3_e, q3["1"], r34["1"], r41["2"])
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
    r4.place(mm("-32.055"), mm("11.887"))
    r40.place(mm("-24.943"), mm("33.731"), rot=180, side="bottom")
    r41.place(mm("-31.293"), mm("-4.369"), side="bottom")
    r9.place(mm("-32.055"), mm("-14.783"), rot=-90, side="bottom")
    u20.place(mm("-26.086"), mm("-14.91"), rot=90)
    x3.place(mm("-24.435"), mm("-26.975"), rot=180)
    return module
