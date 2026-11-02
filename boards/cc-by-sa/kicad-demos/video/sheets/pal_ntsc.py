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
    bt812_rd = nets["bt812_rd"]
    bt812_wr = nets["bt812_wr"]
    dq0 = nets["dq0"]
    dq1 = nets["dq1"]
    dq2 = nets["dq2"]
    dq3 = nets["dq3"]
    dq4 = nets["dq4"]
    dq5 = nets["dq5"]
    dq6 = nets["dq6"]
    dq7 = nets["dq7"]
    f_palin = nets["f_palin"]
    green_in = nets["green_in"]
    hd_pal = nets["hd_pal"]
    oe_pal = nets["oe_pal"]
    pca0 = nets["pca0"]
    pca1 = nets["pca1"]
    red_in = nets["red_in"]
    sysrst = nets["sysrst"]
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
    tvr0 = nets["tvr0"]
    tvr1 = nets["tvr1"]
    tvr2 = nets["tvr2"]
    tvr3 = nets["tvr3"]
    tvr4 = nets["tvr4"]
    tvr5 = nets["tvr5"]
    tvr6 = nets["tvr6"]
    tvr7 = nets["tvr7"]
    vd_pal = nets["vd_pal"]
    pal_ntsc_sch_c_video = Net("/pal-ntsc.sch/C-VIDEO")
    pal_ntsc_sch_vaf = Net("/pal-ntsc.sch/VAF")
    pal_ntsc_sch_y_video = Net("/pal-ntsc.sch/Y-VIDEO")
    pal_ntsc_sch_y_sync = Net("/pal-ntsc.sch/Y_SYNC")
    gnd = nets["gnd"]
    net_c1_pad1 = Net("Net-(C1-Pad1)")
    net_c3_pad1 = Net("Net-(C3-Pad1)")
    net_c4_pad1 = Net("Net-(C4-Pad1)")
    net_c5_pad2 = Net("Net-(C5-Pad2)")
    net_c8_pad2 = Net("Net-(C8-Pad2)")
    net_u10_clevel = Net("Net-(U10-CLEVEL)")
    net_u10_cref = Net("Net-(U10-CREF+)")
    net_u10_n_c = Net("Net-(U10-N/C)")
    net_u10_out_c = Net("Net-(U10-OUT_C)")
    net_u10_r_2 = Net("Net-(U10-R/2)")
    net_u10_sync_det = Net("Net-(U10-SYNC_DET)")
    net_u10_vin_c = Net("Net-(U10-VIN_C)")
    net_u10_vin_y_comp = Net("Net-(U10-VIN_Y/COMP.)")
    net_u10_xtal1_in = Net("Net-(U10-XTAL1_IN)")
    net_u10_xtal1_out = Net("Net-(U10-XTAL1_OUT)")
    c1 = Part(
        refs.get("C1", "C1"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        value="100nF",
        name="C1",
    )
    c10 = Part(
        refs.get("C10", "C10"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="100nF",
        name="C10",
    )
    c11 = Part(
        refs.get("C11", "C11"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
        value="100nF",
        name="C11",
    )
    c12 = Part(
        refs.get("C12", "C12"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
        value="100nF",
        name="C12",
    )
    c13 = Part(
        refs.get("C13", "C13"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="100nF",
        name="C13",
    )
    c14 = Part(
        refs.get("C14", "C14"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
        value="100nF",
        name="C14",
    )
    c15 = Part(
        refs.get("C15", "C15"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="100nF",
        name="C15",
    )
    c16 = Part(
        refs.get("C16", "C16"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
        value="100nF",
        name="C16",
    )
    c2 = Part(
        refs.get("C2", "C2"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
        value="100nF",
        name="C2",
    )
    c3 = Part(
        refs.get("C3", "C3"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_6",
        value="100nF",
        name="C3",
    )
    c4 = Part(
        refs.get("C4", "C4"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_10",
        value="100nF",
        name="C4",
    )
    c47 = Part(
        refs.get("C47", "C47"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_13",
        value="220pF",
        name="C47",
    )
    c5 = Part(
        refs.get("C5", "C5"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_15",
        value="100nF",
        name="C5",
    )
    c6 = Part(
        refs.get("C6", "C6"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
        value="100nF",
        name="C6",
    )
    c62 = Part(
        refs.get("C62", "C62"),
        "video_schlib:CP",
        footprint="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder",
        footprint_definition="footprints:R_1210_3225Metric_Pad1.30x2.65mm_HandSolder_4",
        value="47uF",
        name="C62",
    )
    c65 = Part(
        refs.get("C65", "C65"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_19",
        value="22pF",
        name="C65",
    )
    c66 = Part(
        refs.get("C66", "C66"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="22pF",
        name="C66",
    )
    c7 = Part(
        refs.get("C7", "C7"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_20",
        value="100nF",
        name="C7",
    )
    c8 = Part(
        refs.get("C8", "C8"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_4",
        value="100nF",
        name="C8",
    )
    c9 = Part(
        refs.get("C9", "C9"),
        "video_schlib:C",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="100nF",
        name="C9",
    )
    d1 = Part(
        refs.get("D1", "D1"),
        "video_schlib:DIODESCH",
        footprint="footprints:D_DO-34_SOD68_P7.62mm_Horizontal",
        value="BAT46",
        name="D1",
    )
    d2 = Part(
        refs.get("D2", "D2"),
        "video_schlib:DIODESCH",
        footprint="footprints:D_DO-34_SOD68_P7.62mm_Horizontal",
        value="BAT46",
        name="D2",
    )
    d3 = Part(
        refs.get("D3", "D3"),
        "video_schlib:DIODESCH",
        footprint="footprints:D_DO-34_SOD68_P7.62mm_Horizontal",
        value="BAT46",
        name="D3",
    )
    d4 = Part(
        refs.get("D4", "D4"),
        "video_schlib:DIODESCH",
        footprint="footprints:D_DO-34_SOD68_P7.62mm_Horizontal",
        value="BAT46",
        name="D4",
    )
    l4 = Part(
        refs.get("L4", "L4"),
        "video_schlib:INDUCTOR",
        footprint="footprints:R_1812_4532Metric_Pad1.30x3.40mm_HandSolder",
        value="22uF",
        name="L4",
    )
    r12 = Part(
        refs.get("R12", "R12"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_23",
        value="1K",
        name="R12",
    )
    r14 = Part(
        refs.get("R14", "R14"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_18",
        value="1M",
        name="R14",
    )
    r19 = Part(
        refs.get("R19", "R19"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_26",
        value="220",
        name="R19",
    )
    r2 = Part(
        refs.get("R2", "R2"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_27",
        value="100",
        name="R2",
    )
    r20 = Part(
        refs.get("R20", "R20"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_2",
        value="220",
        name="R20",
    )
    r25 = Part(
        refs.get("R25", "R25"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_3",
        value="220K",
        name="R25",
    )
    r27 = Part(
        refs.get("R27", "R27"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_29",
        value="27K",
        name="R27",
    )
    r3 = Part(
        refs.get("R3", "R3"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_30",
        value="100",
        name="R3",
    )
    r35 = Part(
        refs.get("R35", "R35"),
        "video_schlib:R",
        footprint="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder",
        footprint_definition="footprints:R_1206_3216Metric_Pad1.30x1.75mm_HandSolder_35",
        value="470",
        name="R35",
    )
    u10 = Part(
        refs.get("U10", "U10"),
        "video_schlib:BT812",
        footprint="footprints:PQFP-160_28x28mm_P0.65mm",
        value="BT812",
        name="U10",
    )
    x2 = Part(
        refs.get("X2", "X2"),
        "video_schlib:CRYSTAL",
        footprint="footprints:Crystal_HC18-U_Vertical",
        footprint_definition="footprints:Crystal_HC18-U_Vertical_2",
        value="30MHz",
        name="X2",
    )
    module.add(
        c1,
        c2,
        c3,
        c4,
        c5,
        c6,
        c7,
        c8,
        c9,
        c10,
        c11,
        c12,
        c13,
        c14,
        c15,
        c16,
        c47,
        c62,
        c65,
        c66,
        d1,
        d2,
        d3,
        d4,
        l4,
        r2,
        r3,
        r12,
        r14,
        r19,
        r20,
        r25,
        r27,
        r35,
        u10,
        x2,
    )
    connect(
        net_5v,
        c10["1"],
        c11["1"],
        c15["1"],
        c9["1"],
        d2["2"],
        d4["2"],
        l4["1"],
        u10["102"],
        u10["112"],
        u10["31"],
        u10["45"],
        u10["57"],
        u10["76"],
        u10["91"],
    )
    connect(bt812_rd, u10["86"])
    connect(bt812_wr, u10["83"])
    connect(dq0, u10["92"])
    connect(dq1, u10["93"])
    connect(dq2, u10["94"])
    connect(dq3, u10["95"])
    connect(dq4, u10["96"])
    connect(dq5, u10["97"])
    connect(dq6, u10["99"])
    connect(dq7, u10["100"])
    connect(f_palin, u10["104"])
    connect(green_in, c3["2"])
    connect(hd_pal, u10["36"])
    connect(oe_pal, u10["46"], u10["47"])
    connect(pca0, u10["84"])
    connect(pca1, u10["85"])
    connect(red_in, c4["2"])
    connect(sysrst, u10["87"])
    connect(tvb0, u10["55"])
    connect(tvb1, u10["54"])
    connect(tvb2, u10["53"])
    connect(tvb3, u10["52"])
    connect(tvb4, u10["51"])
    connect(tvb5, u10["50"])
    connect(tvb6, u10["49"])
    connect(tvb7, u10["48"])
    connect(tvg0, u10["74"])
    connect(tvg1, u10["73"])
    connect(tvg2, u10["72"])
    connect(tvg3, u10["71"])
    connect(tvg4, u10["70"])
    connect(tvg5, u10["69"])
    connect(tvg6, u10["68"])
    connect(tvg7, u10["67"])
    connect(tvr0, u10["65"])
    connect(tvr1, u10["64"])
    connect(tvr2, u10["63"])
    connect(tvr3, u10["62"])
    connect(tvr4, u10["61"])
    connect(tvr5, u10["60"])
    connect(tvr6, u10["59"])
    connect(tvr7, u10["58"])
    connect(vd_pal, u10["34"])
    connect(pal_ntsc_sch_c_video, d3["2"], d4["1"], r2["1"], u10["125"])
    connect(
        pal_ntsc_sch_vaf,
        c12["1"],
        c13["1"],
        c14["1"],
        c2["1"],
        c62["1"],
        l4["2"],
        r12["2"],
        u10["1"],
        u10["119"],
        u10["120"],
        u10["121"],
        u10["122"],
        u10["123"],
        u10["132"],
        u10["141"],
        u10["142"],
        u10["149"],
        u10["158"],
        u10["159"],
        u10["160"],
        u10["2"],
        u10["39"],
        u10["40"],
        u10["41"],
        u10["42"],
        u10["43"],
        u10["78"],
        u10["79"],
        u10["80"],
        u10["81"],
        u10["82"],
    )
    connect(pal_ntsc_sch_y_video, d1["2"], d2["1"], r3["1"], u10["156"])
    connect(pal_ntsc_sch_y_sync, r20["2"], r35["2"], u10["6"])
    connect(
        gnd,
        c10["2"],
        c11["2"],
        c12["2"],
        c13["2"],
        c14["2"],
        c15["2"],
        c16["2"],
        c2["2"],
        c47["2"],
        c6["2"],
        c62["2"],
        c65["1"],
        c66["1"],
        c7["2"],
        c9["2"],
        d1["1"],
        d3["1"],
        r14["2"],
        u10["103"],
        u10["111"],
        u10["116"],
        u10["118"],
        u10["124"],
        u10["126"],
        u10["128"],
        u10["130"],
        u10["134"],
        u10["136"],
        u10["138"],
        u10["139"],
        u10["143"],
        u10["145"],
        u10["147"],
        u10["151"],
        u10["153"],
        u10["155"],
        u10["157"],
        u10["16"],
        u10["3"],
        u10["30"],
        u10["44"],
        u10["5"],
        u10["56"],
        u10["66"],
        u10["7"],
        u10["75"],
        u10["88"],
        u10["89"],
        u10["90"],
        u10["98"],
    )
    connect(net_c1_pad1, c1["1"], c47["1"], r35["1"])
    connect(net_c3_pad1, c3["1"], r3["2"])
    connect(net_c4_pad1, c4["1"], r2["2"])
    connect(net_c5_pad2, c5["2"], r19["1"])
    connect(net_c8_pad2, c8["2"], r20["1"])
    connect(net_u10_clevel, c7["1"], r27["2"], u10["114"])
    connect(net_u10_cref, c6["1"], r12["1"], u10["113"], u10["137"], u10["144"])
    connect(net_u10_n_c, c16["1"], u10["110"])
    connect(net_u10_out_c, r19["2"], u10["115"])
    connect(net_u10_r_2, r27["1"], u10["135"])
    connect(net_u10_sync_det, c1["2"], r14["1"], u10["140"])
    connect(net_u10_vin_c, c5["1"], u10["117"])
    connect(net_u10_vin_y_comp, c8["1"], u10["4"])
    connect(net_u10_xtal1_in, c66["2"], r25["1"], u10["108"], x2["2"])
    connect(net_u10_xtal1_out, c65["2"], r25["2"], u10["109"], x2["1"])
    c1.place(mm("258.521"), mm("-41.707"))
    c10.place(mm("244.297"), mm("-12.243"), side="bottom")
    c11.place(mm("219.278"), mm("-30.023"), rot=90, side="bottom")
    c12.place(mm("245.567"), mm("-19.609"), rot=90, side="bottom")
    c13.place(mm("226.009"), mm("-35.357"), side="bottom")
    c14.place(mm("224.231"), mm("-18.085"), rot=90, side="bottom")
    c15.place(mm("225.755"), mm("-12.751"), side="bottom")
    c16.place(mm("238.201"), mm("-15.291"), rot=180, side="bottom")
    c2.place(mm("245.567"), mm("-32.563"), rot=90, side="bottom")
    c3.place(mm("258.14"), mm("-26.213"), rot=-90)
    c4.place(mm("255.981"), mm("-21.895"), side="bottom")
    c47.place(mm("258.521"), mm("-39.167"))
    c5.place(mm("246.202"), mm("-2.718"), rot=-90, side="bottom")
    c6.place(mm("245.567"), mm("-26.721"), rot=90, side="bottom")
    c62.place(mm("256.235"), mm("-33.833"), side="bottom")
    c65.place(mm("251.409"), mm("-6.909"), side="bottom")
    c66.place(mm("251.409"), mm("-4.115"), side="bottom")
    c7.place(mm("238.201"), mm("-12.243"), rot=180, side="bottom")
    c8.place(mm("249.123"), mm("-41.961"), rot=180, side="bottom")
    c9.place(mm("233.883"), mm("-35.103"), side="bottom")
    d1.place(mm("210.300142"), mm("-38.960639"))
    d2.place(mm("211.023"), mm("-41.199"))
    d3.place(mm("253.949"), mm("-15.545"))
    d4.place(mm("253.949"), mm("-13.280835"))
    l4.place(mm("245.313"), mm("-2.845"))
    r12.place(mm("255.727"), mm("-27.737"), rot=90, side="bottom")
    r14.place(mm("258.521"), mm("-36.373"), rot=180)
    r19.place(mm("243.408"), mm("-2.718"), rot=90, side="bottom")
    r2.place(mm("255.981"), mm("-18.847"), side="bottom")
    r20.place(mm("243.027"), mm("-41.961"), side="bottom")
    r25.place(mm("255.346"), mm("-5.385"), rot=90, side="bottom")
    r27.place(mm("244.297"), mm("-15.291"), side="bottom")
    r3.place(mm("258.14"), mm("-27.737"), rot=-90, side="bottom")
    r35.place(mm("253.5"), mm("-40.7075"), rot=90)
    u10.place(mm("235.407"), mm("-23.673"), rot=-90)
    x2.place(mm("257.632"), mm("-8.052"), rot=-90)
    return module
