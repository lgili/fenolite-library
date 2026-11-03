# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://github.com/Open-Air-Foundation/pcb-openair-max-main/tree/89aacf5013fc0ffe4b988a2e3c5a227bce3c4983/PCB/openair-max@89aacf5013fc0ffe4b988a2e3c5a227bce3c4983 by Fenolite 0.7.0.dev0 on 2026-11-03;
# modified: format conversion to the Fenolite DSL.

from fenolite.dsl import Module, Net, Part, connect, mm


def sheet(design, *, path, refs=None, **nets):
    module = Module(path.rsplit("/", 1)[-1])
    design.add(module)
    refs = refs or {}
    battery_holder_avdd = Net("/Battery_holder/AVDD")
    battery_holder_bat1 = Net("/Battery_holder/BAT1")
    battery_holder_bat2 = Net("/Battery_holder/BAT2")
    battery_holder_bat_th = Net("/Battery_holder/BAT_TH")
    battery_holder_chg = Net("/Battery_holder/CHG")
    battery_holder_ctrc = Net("/Battery_holder/CTRC")
    battery_holder_ctrd = Net("/Battery_holder/CTRD")
    battery_holder_dsg = Net("/Battery_holder/DSG")
    battery_holder_ld = Net("/Battery_holder/LD")
    battery_holder_srn = Net("/Battery_holder/SRN")
    battery_holder_srp = Net("/Battery_holder/SRP")
    battery_holder_vbat = Net("/Battery_holder/VBAT+")
    solar_module_vbat = nets["solar_module_vbat"]
    bat = Net("BAT-")
    net_c24_pad2 = Net("Net-(C24-Pad2)")
    net_d1_pad2 = Net("Net-(D1-Pad2)")
    net_d2_k = Net("Net-(D2-K)")
    net_f2_pad2 = Net("Net-(F2-Pad2)")
    net_q1_d = Net("Net-(Q1-D)")
    net_q1_g = Net("Net-(Q1-G)")
    net_u4_ccfg = Net("Net-(U4-CCFG)")
    net_u4_vc1 = Net("Net-(U4-VC1)")
    net_u4_vc2 = Net("Net-(U4-VC2)")
    net_u4_vc3 = Net("Net-(U4-VC3)")
    net_u4_vdd = Net("Net-(U4-VDD)")
    net_u4_vtb = Net("Net-(U4-VTB)")
    pgnd = nets["pgnd"]
    bat1 = Part(
        refs.get("BAT1", "BAT1"),
        "easyeda2kicad:BH-18650-B5BA016",
        footprint="easyeda2kicad:BAT-SMD_BH-18650-B5BA016",
        value="BH-18650-B5BA016",
        properties={"LCSC Part": "C19184086"},
        name="BAT1",
    )
    c15 = Part(
        refs.get("C15", "C15"),
        "easyeda2kicad:CC0603KRX7R9BB104",
        footprint="easyeda2kicad:C0603",
        value="0.1uF/50V",
        properties={"LCSC Part": "C14663"},
        name="C15",
    )
    c16 = Part(
        refs.get("C16", "C16"),
        "easyeda2kicad:CC0603KRX7R9BB104",
        footprint="easyeda2kicad:C0603",
        footprint_definition="easyeda2kicad:C0603_2",
        value="0.1uF/50V",
        properties={"LCSC Part": "C14663"},
        name="C16",
    )
    c17 = Part(
        refs.get("C17", "C17"),
        "easyeda2kicad:CC0603KRX7R9BB104",
        footprint="easyeda2kicad:C0603",
        footprint_definition="easyeda2kicad:C0603_3",
        value="0.1uF/50V",
        properties={"LCSC Part": "C14663"},
        name="C17",
    )
    c18 = Part(
        refs.get("C18", "C18"),
        "easyeda2kicad:CC0603KRX7R9BB104",
        footprint="easyeda2kicad:C0603",
        footprint_definition="easyeda2kicad:C0603_4",
        value="0.1uF/50V",
        properties={"LCSC Part": "C14663"},
        name="C18",
    )
    c19 = Part(
        refs.get("C19", "C19"),
        "easyeda2kicad:CC0603KRX7R9BB104",
        footprint="easyeda2kicad:C0603",
        footprint_definition="easyeda2kicad:C0603_5",
        value="0.1uF/50V",
        properties={"LCSC Part": "C14663"},
        name="C19",
    )
    c20 = Part(
        refs.get("C20", "C20"),
        "easyeda2kicad:CC0402KRX5R9BB105",
        footprint="easyeda2kicad:C0402",
        footprint_definition="easyeda2kicad:C0402_7",
        value="1uF/50V",
        properties={"LCSC Part": "C7500380"},
        name="C20",
    )
    c21 = Part(
        refs.get("C21", "C21"),
        "easyeda2kicad:CC0603KRX7R9BB104",
        footprint="easyeda2kicad:C0603",
        footprint_definition="easyeda2kicad:C0603_2",
        value="0.1uF/50V",
        properties={"LCSC Part": "C14663"},
        name="C21",
    )
    c22 = Part(
        refs.get("C22", "C22"),
        "easyeda2kicad:CC0402KRX5R9BB105",
        footprint="easyeda2kicad:C0402",
        footprint_definition="easyeda2kicad:C0402_8",
        value="1uF/50V",
        properties={"LCSC Part": "C7500380"},
        name="C22",
    )
    c24 = Part(
        refs.get("C24", "C24"),
        "easyeda2kicad:CC0603KRX7R9BB104",
        footprint="easyeda2kicad:C0603",
        footprint_definition="easyeda2kicad:C0603_6",
        value="0.1uF/50V",
        properties={"LCSC Part": "C14663"},
        name="C24",
    )
    c25 = Part(
        refs.get("C25", "C25"),
        "easyeda2kicad:CC0603KRX7R9BB104",
        footprint="easyeda2kicad:C0603",
        footprint_definition="easyeda2kicad:C0603_7",
        value="0.1uF/50V",
        properties={"LCSC Part": "C14663"},
        name="C25",
    )
    d1 = Part(
        refs.get("D1", "D1"),
        "BAS16J_135:BAS16J_135",
        footprint="BAS16J,135:SOD2512X80N",
        value="BAS16J_135",
        properties={
            "Availability": "In Stock",
            "Check_prices": "https://www.snapeda.com/parts/BAS16J,135/Nexperia/view-part/?ref=eda",
            "HEIGHT": "0.8mm",
            "MANUFACTURER_NAME": "Nexperia",
            "MANUFACTURER_PART_NUMBER": "BAS16J,135",
            "MF": "Nexperia USA",
            "MOUSER_PART_NUMBER": "771-BAS16J135",
            "MOUSER_PRICE-STOCK": "https://www.mouser.com/Search/Refine.aspx?Keyword=771-BAS16J135",
            "MP": "BAS16J,135",
            "Package": "SC-90-2 Nexperia USA Inc.",
            "Price": "None",
            "SnapEDA_Link": "https://www.snapeda.com/parts/BAS16J,135/Nexperia/view-part/?ref=snap",
        },
        name="D1",
    )
    d2 = Part(
        refs.get("D2", "D2"),
        "easyeda2kicad:MMSZ5246BS-7-F",
        footprint="easyeda2kicad:SOD-323_L1.8-W1.3-LS2.5-RD",
        value="MMSZ5246BS-7-F",
        properties={"LCSC Part": "C151819"},
        name="D2",
    )
    f2 = Part(
        refs.get("F2", "F2"),
        "Device:Fuse",
        footprint="easyeda2kicad:PCB_fuse",
        value="Fuse 5A",
        dnp=True,
        name="F2",
    )
    ntc1 = Part(
        refs.get("NTC1", "NTC1"),
        "easyeda2kicad:KNTC0805_10KF3950",
        footprint="easyeda2kicad:R0805",
        value="KNTC0805/10KF3950",
        properties={"LCSC Part": "C2892549"},
        name="NTC1",
    )
    pwr_sw1 = Part(
        refs.get("PWR_SW1", "PWR_SW1"),
        "easyeda2kicad:TK-6580A8-1",
        footprint="easyeda2kicad:SW-TH_TK-6580A8-1",
        value="TK-6580A8-1",
        properties={"LCSC Part": "C528772"},
        name="PWR_SW1",
    )
    q1 = Part(
        refs.get("Q1", "Q1"),
        "Transistor_FET:CSD18534Q5A",
        footprint="easyeda2kicad:PQFN-8_L5.8-W4.9-P1.27-LS6.0-BL",
        value="CSD18534Q5A",
        name="Q1",
    )
    q2 = Part(
        refs.get("Q2", "Q2"),
        "Transistor_FET:CSD18534Q5A",
        footprint="easyeda2kicad:PQFN-8_L5.8-W4.9-P1.27-LS6.0-BL",
        footprint_definition="easyeda2kicad:PQFN-8_L5.8-W4.9-P1.27-LS6.0-BL_2",
        value="CSD18534Q5A",
        name="Q2",
    )
    r10 = Part(
        refs.get("R10", "R10"),
        "easyeda2kicad:RC0402FR-7W100RL",
        footprint="easyeda2kicad:R0402",
        footprint_definition="easyeda2kicad:R0402_2",
        value="100",
        properties={"LCSC Part": "C606168"},
        name="R10",
    )
    r11 = Part(
        refs.get("R11", "R11"),
        "easyeda2kicad:RL2512FK-070R01L",
        footprint="easyeda2kicad:R2512",
        value="10m / 1W",
        properties={"LCSC Part": "C705061"},
        name="R11",
    )
    r12 = Part(
        refs.get("R12", "R12"),
        "easyeda2kicad:RC0402FR-7W1KL",
        footprint="easyeda2kicad:R0402",
        footprint_definition="easyeda2kicad:R0402_3",
        value="1K",
        properties={"LCSC Part": "C851849"},
        name="R12",
    )
    r13 = Part(
        refs.get("R13", "R13"),
        "easyeda2kicad:RC0402FR-7W100RL",
        footprint="easyeda2kicad:R0402",
        footprint_definition="easyeda2kicad:R0402_4",
        value="100",
        properties={"LCSC Part": "C606168"},
        name="R13",
    )
    r14 = Part(
        refs.get("R14", "R14"),
        "easyeda2kicad:RC0402FR-7W1KL",
        footprint="easyeda2kicad:R0402",
        footprint_definition="easyeda2kicad:R0402_5",
        value="1K",
        properties={"LCSC Part": "C851849"},
        name="R14",
    )
    r15 = Part(
        refs.get("R15", "R15"),
        "easyeda2kicad:RC0402FR-7W1KL",
        footprint="easyeda2kicad:R0402",
        footprint_definition="easyeda2kicad:R0402_6",
        value="1K",
        properties={"LCSC Part": "C851849"},
        name="R15",
    )
    r17 = Part(
        refs.get("R17", "R17"),
        "easyeda2kicad:RC0603FR-075K1L",
        footprint="easyeda2kicad:R0603",
        footprint_definition="easyeda2kicad:R0603_2",
        value="5.1K",
        properties={"LCSC Part": "C105580"},
        name="R17",
    )
    r18 = Part(
        refs.get("R18", "R18"),
        "easyeda2kicad:RC0603FR-0710ML",
        footprint="easyeda2kicad:R0603",
        footprint_definition="easyeda2kicad:R0603_3",
        value="10M",
        properties={"LCSC Part": "C114606"},
        name="R18",
    )
    r19 = Part(
        refs.get("R19", "R19"),
        "easyeda2kicad:RC0603FR-075K1L",
        footprint="easyeda2kicad:R0603",
        footprint_definition="easyeda2kicad:R0603_4",
        value="5.1K",
        properties={"LCSC Part": "C105580"},
        name="R19",
    )
    r20 = Part(
        refs.get("R20", "R20"),
        "easyeda2kicad:RC0603FR-071ML",
        footprint="easyeda2kicad:R0603",
        footprint_definition="easyeda2kicad:R0603_5",
        value="1M",
        properties={"LCSC Part": "C105578"},
        name="R20",
    )
    r21 = Part(
        refs.get("R21", "R21"),
        "easyeda2kicad:RC0603FR-073ML",
        footprint="easyeda2kicad:R0603",
        footprint_definition="easyeda2kicad:R0603_6",
        value="3M",
        properties={"LCSC Part": "C126361"},
        name="R21",
    )
    r22 = Part(
        refs.get("R22", "R22"),
        "easyeda2kicad:RC0603FR-0710KL",
        footprint="easyeda2kicad:R0603",
        footprint_definition="easyeda2kicad:R0603_7",
        value="10K",
        properties={"LCSC Part": "C98220"},
        name="R22",
    )
    r23 = Part(
        refs.get("R23", "R23"),
        "easyeda2kicad:RC0603FR-070RL",
        footprint="easyeda2kicad:R0603",
        footprint_definition="easyeda2kicad:R0603_8",
        value="0",
        properties={"LCSC Part": "C100044"},
        dnp=True,
        name="R23",
    )
    r24 = Part(
        refs.get("R24", "R24"),
        "easyeda2kicad:RC0603FR-07470KL",
        footprint="easyeda2kicad:R0603",
        footprint_definition="easyeda2kicad:R0603_9",
        value="470K",
        properties={"LCSC Part": "C114622"},
        name="R24",
    )
    r26 = Part(
        refs.get("R26", "R26"),
        "easyeda2kicad:RC0603FR-070RL",
        footprint="easyeda2kicad:R0603",
        footprint_definition="easyeda2kicad:R0603_11",
        value="0",
        properties={"LCSC Part": "C100044"},
        name="R26",
    )
    r27 = Part(
        refs.get("R27", "R27"),
        "easyeda2kicad:RC0603FR-070RL",
        footprint="easyeda2kicad:R0603",
        footprint_definition="easyeda2kicad:R0603_12",
        value="0",
        properties={"LCSC Part": "C100044"},
        name="R27",
    )
    r51 = Part(
        refs.get("R51", "R51"),
        "easyeda2kicad:RC0603FR-070RL",
        footprint="easyeda2kicad:R0603",
        footprint_definition="easyeda2kicad:R0603_21",
        value="0",
        properties={"LCSC Part": "C100044"},
        name="R51",
    )
    r9 = Part(
        refs.get("R9", "R9"),
        "easyeda2kicad:RC0402FR-7W1KL",
        footprint="easyeda2kicad:R0402",
        footprint_definition="easyeda2kicad:R0402_61",
        value="1K",
        properties={"LCSC Part": "C851849"},
        name="R9",
    )
    u4 = Part(
        refs.get("U4", "U4"),
        "easyeda2kicad:BQ7790512PWR",
        footprint="easyeda2kicad:TSSOP-20_L6.5-W4.4-P0.65-LS6.4-BL",
        value="BQ7790512PWR",
        properties={"LCSC Part": "C555146"},
        name="U4",
    )
    module.add(
        bat1,
        c15,
        c16,
        c17,
        c18,
        c19,
        c20,
        c21,
        c22,
        c24,
        c25,
        d1,
        d2,
        f2,
        ntc1,
        pwr_sw1,
        q1,
        q2,
        r9,
        r10,
        r11,
        r12,
        r13,
        r14,
        r15,
        r17,
        r18,
        r19,
        r20,
        r21,
        r22,
        r23,
        r24,
        r26,
        r27,
        r51,
        u4,
    )
    connect(battery_holder_avdd, c22["2"], r23["2"], u4["2"])
    connect(battery_holder_bat1, bat1["2"], bat1["4"], r9["1"])
    connect(battery_holder_bat2, bat1["3"], bat1["5"], r12["1"])
    connect(battery_holder_bat_th, ntc1["2"], r22["1"], u4["15"])
    connect(battery_holder_chg, r19["2"], u4["13"])
    connect(battery_holder_ctrc, r26["1"], u4["18"])
    connect(battery_holder_ctrd, r27["2"], u4["19"])
    connect(battery_holder_dsg, r17["2"], u4["11"])
    connect(battery_holder_ld, r24["2"], u4["14"])
    connect(battery_holder_srn, c17["1"], c19["2"], r13["2"], u4["10"])
    connect(battery_holder_srp, c15["2"], c17["2"], r10["2"], u4["9"])
    connect(battery_holder_vbat, bat1["6"], c25["2"], pwr_sw1["4"], pwr_sw1["6"], r14["1"], r15["1"])
    connect(solar_module_vbat, f2["1"])
    connect(
        bat,
        bat1["1"],
        c15["1"],
        c16["1"],
        c18["1"],
        c19["1"],
        c20["1"],
        c21["1"],
        c22["1"],
        ntc1["1"],
        r10["1"],
        r11["1"],
        r26["2"],
        r27["1"],
        r51["1"],
        u4["20"],
        u4["8"],
    )
    connect(net_c24_pad2, c24["2"], q1["1"], q1["2"], q1["3"], r11["2"], r13["1"], r18["1"])
    connect(net_d1_pad2, d1["2"], r19["1"], r20["2"])
    connect(net_d2_k, d1["1"], d2["1"], q2["4"], r20["1"], r21["2"])
    connect(net_f2_pad2, f2["2"], pwr_sw1["2"], pwr_sw1["5"])
    connect(net_q1_d, q1["5"], q1["6"], q1["7"], q1["8"], q2["5"], q2["6"], q2["7"], q2["8"])
    connect(net_q1_g, q1["4"], r17["1"], r18["2"])
    connect(net_u4_ccfg, r23["1"], r51["2"], u4["17"])
    connect(net_u4_vc1, c16["2"], r9["2"], u4["7"])
    connect(net_u4_vc2, c18["2"], r12["2"], u4["6"])
    connect(net_u4_vc3, c21["2"], r15["2"], u4["3"], u4["4"], u4["5"])
    connect(net_u4_vdd, c20["2"], r14["2"], u4["1"])
    connect(net_u4_vtb, r22["2"], u4["16"])
    connect(pgnd, c24["1"], c25["1"], d2["2"], q2["1"], q2["2"], q2["3"], r21["1"], r24["1"])
    bat1.place(mm("45.81"), mm("-14.18"), locked=True)
    c15.place(mm("75.61"), mm("2.275"), rot=90, side="bottom")
    c16.place(mm("75.11"), mm("10.84"), rot=90, side="bottom")
    c17.place(mm("81.285"), mm("2.3"), rot=-90, side="bottom")
    c18.place(mm("77.21"), mm("10.865"), rot=90, side="bottom")
    c19.place(mm("77.71"), mm("2.275"), rot=90, side="bottom")
    c20.place(mm("83.235"), mm("10.725"), side="bottom")
    c21.place(mm("79.31"), mm("10.84"), rot=90, side="bottom")
    c22.place(mm("81.085"), mm("10.65"), rot=90, side="bottom")
    c24.place(mm("74.76"), mm("-12.78"), rot=180, side="bottom")
    c25.place(mm("91.83"), mm("1.95"), rot=90, side="bottom")
    d1.place(mm("84.26"), mm("-1.875"), rot=180, side="bottom")
    d2.place(mm("88.33"), mm("-3.95"), side="bottom")
    f2.place(mm("69.11"), mm("-25.385"), rot=180, side="bottom")
    ntc1.place(mm("3.96"), mm("-26.68"), rot=-90)
    pwr_sw1.place(mm("73.07"), mm("16.42"))
    q1.place(mm("76.025"), mm("-8.48"), rot=90, side="bottom")
    q2.place(mm("84.585"), mm("-8.5"), rot=-90, side="bottom")
    r10.place(mm("74.56"), mm("-0.605"), rot=-90, side="bottom")
    r11.place(mm("69.955"), mm("-5.7"), rot=90, side="bottom")
    r12.place(mm("77.21"), mm("7.12"), rot=-90, side="bottom")
    r13.place(mm("76.11"), mm("-0.605"), rot=-90, side="bottom")
    r14.place(mm("83.355"), mm("12"), side="bottom")
    r15.place(mm("79.31"), mm("7.12"), rot=-90, side="bottom")
    r17.place(mm("81.36"), mm("-1.125"), rot=-90, side="bottom")
    r18.place(mm("77.71"), mm("-1.125"), rot=90, side="bottom")
    r19.place(mm("79.56"), mm("-1.15"), rot=-90, side="bottom")
    r20.place(mm("84.66"), mm("0.2"), rot=180, side="bottom")
    r21.place(mm("87.91"), mm("-1.875"), rot=180, side="bottom")
    r22.place(mm("91.385"), mm("5.47"), rot=-90, side="bottom")
    r23.place(mm("91.885"), mm("7.84"), side="bottom")
    r24.place(mm("87.91"), mm("0.175"), rot=180, side="bottom")
    r26.place(mm("72.795"), mm("1.35"), rot=90, side="bottom")
    r27.place(mm("90.48"), mm("10.7"), side="bottom")
    r51.place(mm("86.245"), mm("11.15"), side="bottom")
    r9.place(mm("75.11"), mm("7.12"), rot=-90, side="bottom")
    u4.place(mm("86.26"), mm("6.425"), rot=90, side="bottom")
    return module
