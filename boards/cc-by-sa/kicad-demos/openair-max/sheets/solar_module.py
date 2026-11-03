# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://github.com/Open-Air-Foundation/pcb-openair-max-main/tree/89aacf5013fc0ffe4b988a2e3c5a227bce3c4983/PCB/openair-max@89aacf5013fc0ffe4b988a2e3c5a227bce3c4983 by Fenolite 0.7.0.dev0 on 2026-11-03;
# modified: format conversion to the Fenolite DSL.

from fenolite.dsl import Module, Net, Part, connect, mm


def sheet(design, *, path, refs=None, **nets):
    module = Module(path.rsplit("/", 1)[-1])
    design.add(module)
    refs = refs or {}
    net_3v3 = nets["net_3v3"]
    net_5vbat = nets["net_5vbat"]
    net_5vusb = nets["net_5vusb"]
    scl = nets["scl"]
    sda = nets["sda"]
    solar_module_acdrv1 = Net("/Solar_module/ACDRV1")
    solar_module_acdrv2 = Net("/Solar_module/ACDRV2")
    solar_module_btst1 = Net("/Solar_module/BTST1")
    solar_module_btst2 = Net("/Solar_module/BTST2")
    solar_module_fb_vset = Net("/Solar_module/FB/VSET")
    solar_module_ilim_hiz = Net("/Solar_module/ILIM_HIZ")
    solar_module_prog = Net("/Solar_module/PROG")
    solar_module_regn = Net("/Solar_module/REGN")
    solar_module_sw1 = Net("/Solar_module/SW1")
    solar_module_sw2 = Net("/Solar_module/SW2")
    solar_module_sys = Net("/Solar_module/SYS")
    solar_module_solar = Net("/Solar_module/Solar+")
    solar_module_vbat = nets["solar_module_vbat"]
    solar_module_vbus = Net("/Solar_module/VBUS")
    gnd = nets["gnd"]
    net_c91_pad2 = Net("Net-(C91-Pad2)")
    net_c94_pad2 = Net("Net-(C94-Pad2)")
    net_d8_a = Net("Net-(D8-A)")
    net_d8_k = Net("Net-(D8-K)")
    net_d9_a = Net("Net-(D9-A)")
    net_d9_k = Net("Net-(D9-K)")
    net_led3_a = Net("Net-(LED3-A)")
    net_led3_k = Net("Net-(LED3-K)")
    net_r16_pad1 = Net("Net-(R16-Pad1)")
    net_u5_batp = Net("Net-(U5-BATP)")
    net_u5_pmid = Net("Net-(U5-PMID)")
    net_u5_sdrv = Net("Net-(U5-SDRV)")
    net_u5_ts = Net("Net-(U5-TS)")
    net_u5_ce = Net("Net-(U5-~{CE})")
    net_u6_en = Net("Net-(U6-EN)")
    net_u6_mode_s_conf = Net("Net-(U6-MODE/S-CONF)")
    net_u6_pg = Net("Net-(U6-PG)")
    net_u6_ss_tr = Net("Net-(U6-SS/TR)")
    net_u6_sw = Net("Net-(U6-SW)")
    pgnd = nets["pgnd"]
    battery1 = Part(
        refs.get("Battery1", "Battery1"),
        "Library:ZX-PM2.54-1-2PY",
        footprint="easyeda2kicad:HDR-TH_2P-P2.54-V-F",
        value="ZX-PM2.54-1-2PY",
        properties={"LCSC Part": "C7499322"},
        dnp=True,
        name="Battery1",
    )
    c23 = Part(
        refs.get("C23", "C23"),
        "easyeda2kicad:CL31A106KAHNNNE",
        footprint="easyeda2kicad:C1206",
        value="10uF/25V",
        properties={"LCSC Part": "C9807"},
        name="C23",
    )
    c26 = Part(
        refs.get("C26", "C26"),
        "easyeda2kicad:CL05A104KA5NNNC",
        footprint="easyeda2kicad:C0402",
        footprint_definition="easyeda2kicad:C0402_9",
        value="0.1uF/25V",
        properties={"LCSC Part": "C100072"},
        name="C26",
    )
    c27 = Part(
        refs.get("C27", "C27"),
        "easyeda2kicad:CL31A106KAHNNNE",
        footprint="easyeda2kicad:C1206",
        footprint_definition="easyeda2kicad:C1206_2",
        value="10uF/25V",
        properties={"LCSC Part": "C9807"},
        name="C27",
    )
    c28 = Part(
        refs.get("C28", "C28"),
        "easyeda2kicad:CC0402KRX7R9BB473",
        footprint="easyeda2kicad:C0402",
        footprint_definition="easyeda2kicad:C0402_10",
        value="47nF/50V",
        properties={"LCSC Part": "C272875"},
        name="C28",
    )
    c29 = Part(
        refs.get("C29", "C29"),
        "easyeda2kicad:CC0402KRX7R9BB473",
        footprint="easyeda2kicad:C0402",
        footprint_definition="easyeda2kicad:C0402_11",
        value="47nF/50V",
        properties={"LCSC Part": "C272875"},
        name="C29",
    )
    c30 = Part(
        refs.get("C30", "C30"),
        "easyeda2kicad:CL31A106KAHNNNE",
        footprint="easyeda2kicad:C1206",
        footprint_definition="easyeda2kicad:C1206_4",
        value="10uF/25V",
        properties={"LCSC Part": "C9807"},
        name="C30",
    )
    c31 = Part(
        refs.get("C31", "C31"),
        "easyeda2kicad:GRM155R71H104KE14D",
        footprint="easyeda2kicad:C0402",
        footprint_definition="easyeda2kicad:C0402_12",
        value="0.1uF/50V",
        properties={"LCSC Part": "C77020"},
        name="C31",
    )
    c33 = Part(
        refs.get("C33", "C33"),
        "easyeda2kicad:CL31A106KBHNNNE",
        footprint="easyeda2kicad:C1206",
        footprint_definition="easyeda2kicad:C1206_5",
        value="10uF/50V",
        properties={"LCSC Part": "C13585"},
        name="C33",
    )
    c34 = Part(
        refs.get("C34", "C34"),
        "easyeda2kicad:GRM155R71H104KE14D",
        footprint="easyeda2kicad:C0402",
        footprint_definition="easyeda2kicad:C0402_14",
        value="0.1uF/50V",
        properties={"LCSC Part": "C77020"},
        name="C34",
    )
    c35 = Part(
        refs.get("C35", "C35"),
        "easyeda2kicad:CL31A106KBHNNNE",
        footprint="easyeda2kicad:C1206",
        footprint_definition="easyeda2kicad:C1206_6",
        value="10uF/50V",
        properties={"LCSC Part": "C13585"},
        name="C35",
    )
    c36 = Part(
        refs.get("C36", "C36"),
        "easyeda2kicad:CGA0603X7R475K160JT",
        footprint="easyeda2kicad:C0603",
        footprint_definition="easyeda2kicad:C0603_8",
        value="4.7uF/16V",
        properties={"LCSC Part": "C22399629"},
        name="C36",
    )
    c37 = Part(
        refs.get("C37", "C37"),
        "easyeda2kicad:GRM155R71H104KE14D",
        footprint="easyeda2kicad:C0402",
        footprint_definition="easyeda2kicad:C0402_15",
        value="0.1uF/50V",
        properties={"LCSC Part": "C77020"},
        name="C37",
    )
    c38 = Part(
        refs.get("C38", "C38"),
        "easyeda2kicad:CL31A106KBHNNNE",
        footprint="easyeda2kicad:C1206",
        footprint_definition="easyeda2kicad:C1206_7",
        value="10uF/50V",
        properties={"LCSC Part": "C13585"},
        name="C38",
    )
    c39 = Part(
        refs.get("C39", "C39"),
        "easyeda2kicad:GRM155R71H104KE14D",
        footprint="easyeda2kicad:C0402",
        footprint_definition="easyeda2kicad:C0402_16",
        value="0.1uF/50V",
        properties={"LCSC Part": "C77020"},
        name="C39",
    )
    c40 = Part(
        refs.get("C40", "C40"),
        "easyeda2kicad:CL31A106KBHNNNE",
        footprint="easyeda2kicad:C1206",
        footprint_definition="easyeda2kicad:C1206_8",
        value="10uF/50V",
        properties={"LCSC Part": "C13585"},
        name="C40",
    )
    c41 = Part(
        refs.get("C41", "C41"),
        "easyeda2kicad:GRM155R71H102KA01D",
        footprint="easyeda2kicad:C0402",
        footprint_definition="easyeda2kicad:C0402_18",
        value="1nF/50V",
        properties={"LCSC Part": "C77018"},
        name="C41",
    )
    c42 = Part(
        refs.get("C42", "C42"),
        "easyeda2kicad:CL05B104KO5NNNC",
        footprint="easyeda2kicad:C0402",
        footprint_definition="easyeda2kicad:C0402_19",
        value="0.1uF/16V",
        properties={"LCSC Part": "C1525"},
        name="C42",
    )
    c43 = Part(
        refs.get("C43", "C43"),
        "easyeda2kicad:CC1206KKX7R7BB106",
        footprint="easyeda2kicad:C1206",
        footprint_definition="easyeda2kicad:C1206_9",
        value="10uF/16V",
        properties={"LCSC Part": "C109464"},
        name="C43",
    )
    c44 = Part(
        refs.get("C44", "C44"),
        "easyeda2kicad:CL05B104KO5NNNC",
        footprint="easyeda2kicad:C0402",
        footprint_definition="easyeda2kicad:C0402_20",
        value="0.1uF/16V",
        properties={"LCSC Part": "C1525"},
        name="C44",
    )
    c45 = Part(
        refs.get("C45", "C45"),
        "easyeda2kicad:CC1206KKX7R7BB106",
        footprint="easyeda2kicad:C1206",
        footprint_definition="easyeda2kicad:C1206_10",
        value="10uF/16V",
        properties={"LCSC Part": "C109464"},
        name="C45",
    )
    c46 = Part(
        refs.get("C46", "C46"),
        "easyeda2kicad:CL21A226MAYNNNE",
        footprint="easyeda2kicad:C0805",
        footprint_definition="easyeda2kicad:C0805_2",
        value="22uF/25V",
        properties={"LCSC Part": "C602037"},
        name="C46",
    )
    c47 = Part(
        refs.get("C47", "C47"),
        "easyeda2kicad:CL05A104KA5NNNC",
        footprint="easyeda2kicad:C0402",
        footprint_definition="easyeda2kicad:C0402_21",
        value="0.1uF/25V",
        properties={"LCSC Part": "C100072"},
        name="C47",
    )
    c48 = Part(
        refs.get("C48", "C48"),
        "easyeda2kicad:CL21A226MAYNNNE",
        footprint="easyeda2kicad:C0805",
        footprint_definition="easyeda2kicad:C0805_3",
        value="22uF/25V",
        properties={"LCSC Part": "C602037"},
        name="C48",
    )
    c49 = Part(
        refs.get("C49", "C49"),
        "easyeda2kicad:CC0402KRX7R7BB332",
        footprint="easyeda2kicad:C0402",
        footprint_definition="easyeda2kicad:C0402_22",
        value="3.3nF/16V",
        properties={"LCSC Part": "C541378"},
        name="C49",
    )
    c87 = Part(
        refs.get("C87", "C87"),
        "easyeda2kicad:GRM155R71H102KA01D",
        footprint="easyeda2kicad:C0402",
        footprint_definition="easyeda2kicad:C0402_59",
        value="1nF/50V",
        properties={"LCSC Part": "C77018"},
        name="C87",
    )
    c88 = Part(
        refs.get("C88", "C88"),
        "easyeda2kicad:GRM155R71H102KA01D",
        footprint="easyeda2kicad:C0402",
        footprint_definition="easyeda2kicad:C0402_60",
        value="1nF/50V",
        properties={"LCSC Part": "C77018"},
        name="C88",
    )
    c89 = Part(
        refs.get("C89", "C89"),
        "easyeda2kicad:GRM155R71H104KE14D",
        footprint="easyeda2kicad:C0402",
        footprint_definition="easyeda2kicad:C0402_61",
        value="0.1uF/50V",
        properties={"LCSC Part": "C77020"},
        name="C89",
    )
    c90 = Part(
        refs.get("C90", "C90"),
        "easyeda2kicad:GRM155R71H104KE14D",
        footprint="easyeda2kicad:C0402",
        footprint_definition="easyeda2kicad:C0402_63",
        value="0.1uF/50V",
        properties={"LCSC Part": "C77020"},
        name="C90",
    )
    c91 = Part(
        refs.get("C91", "C91"),
        "easyeda2kicad:CGA0402X5R225K350GT",
        footprint="easyeda2kicad:C0402",
        footprint_definition="easyeda2kicad:C0402_64",
        value="2.2uF/35V",
        properties={"LCSC Part": "C6119793"},
        name="C91",
    )
    c94 = Part(
        refs.get("C94", "C94"),
        "easyeda2kicad:CGA0402X5R225K350GT",
        footprint="easyeda2kicad:C0402",
        footprint_definition="easyeda2kicad:C0402_65",
        value="2.2uF/35V",
        properties={"LCSC Part": "C6119793"},
        name="C94",
    )
    d3 = Part(
        refs.get("D3", "D3"),
        "easyeda2kicad:SMBJ24A_C908801",
        footprint="easyeda2kicad:SMB_L4.4-W3.6-LS5.3-RD",
        value="SMBJ24A_C908801",
        properties={"LCSC Part": "C908801"},
        name="D3",
    )
    d8 = Part(
        refs.get("D8", "D8"),
        "easyeda2kicad:BZT52C12T-7",
        footprint="easyeda2kicad:SOD-523_L1.2-W0.8-LS1.6-RD",
        value="BZT52C12T-7",
        properties={"LCSC Part": "C507911"},
        name="D8",
    )
    d9 = Part(
        refs.get("D9", "D9"),
        "easyeda2kicad:BZT52C12T-7",
        footprint="easyeda2kicad:SOD-523_L1.2-W0.8-LS1.6-RD",
        footprint_definition="easyeda2kicad:SOD-523_L1.2-W0.8-LS1.6-RD_2",
        value="BZT52C12T-7",
        properties={"LCSC Part": "C507911"},
        name="D9",
    )
    dc1 = Part(
        refs.get("DC1", "DC1"),
        "easyeda2kicad:DC-045A-13A",
        footprint="easyeda2kicad:DC-IN-SMD_DC-045A-13A",
        value="DC-045A-13A",
        properties={"LCSC Part": "C707277"},
        name="DC1",
    )
    fb1 = Part(
        refs.get("FB1", "FB1"),
        "easyeda2kicad:PBY201209T-601Y-N",
        footprint="easyeda2kicad:L0805",
        value="PBY201209T-601Y-N",
        properties={"LCSC Part": "C108304"},
        name="FB1",
    )
    l1 = Part(
        refs.get("L1", "L1"),
        "easyeda2kicad:SPM6530T-1R0M120",
        footprint="easyeda2kicad:IND-SMD_L7.1-W6.5-P5.60",
        value="SPM6530T-1R0M120",
        properties={"LCSC Part": "C87572"},
        name="L1",
    )
    l2 = Part(
        refs.get("L2", "L2"),
        "easyeda2kicad:XGL4020-102MEC",
        footprint="easyeda2kicad:IND-SMD_L4.0-W4.0_XAL4030-332MEC",
        value="XGL4020-102MEC",
        properties={"LCSC Part": "C5357696"},
        name="L2",
    )
    led3 = Part(
        refs.get("LED3", "LED3"),
        "easyeda2kicad-old:FC-DA1608HRK-620D",
        footprint="easyeda2kicad:LED0603-RD_RED",
        value="FC-DA1608HRK-620D",
        properties={"LCSC Part": "C84263"},
        name="LED3",
    )
    q3 = Part(
        refs.get("Q3", "Q3"),
        "Transistor_FET:CSD17577Q3A",
        footprint="Package_SON:VSON-8_3.3x3.3mm_P0.65mm_NexFET",
        value="CSD17577Q3A",
        properties={"LCSC Part": "C201632"},
        name="Q3",
    )
    q4 = Part(
        refs.get("Q4", "Q4"),
        "Transistor_FET:CSD17577Q3A",
        footprint="Package_SON:VSON-8_3.3x3.3mm_P0.65mm_NexFET",
        footprint_definition="Package_SON:VSON-8_3.3x3.3mm_P0.65mm_NexFET_2",
        value="CSD17577Q3A",
        properties={"LCSC Part": "C201632"},
        name="Q4",
    )
    q5 = Part(
        refs.get("Q5", "Q5"),
        "Transistor_FET:CSD17577Q3A",
        footprint="Package_SON:VSON-8_3.3x3.3mm_P0.65mm_NexFET",
        footprint_definition="Package_SON:VSON-8_3.3x3.3mm_P0.65mm_NexFET_3",
        value="CSD17577Q3A",
        properties={"LCSC Part": "C201632"},
        name="Q5",
    )
    q6 = Part(
        refs.get("Q6", "Q6"),
        "Transistor_FET:CSD17577Q3A",
        footprint="Package_SON:VSON-8_3.3x3.3mm_P0.65mm_NexFET",
        footprint_definition="Package_SON:VSON-8_3.3x3.3mm_P0.65mm_NexFET_4",
        value="CSD17577Q3A",
        properties={"LCSC Part": "C201632"},
        name="Q6",
    )
    r16 = Part(
        refs.get("R16", "R16"),
        "easyeda2kicad:RC0603FR-0710K5L",
        footprint="easyeda2kicad:R0603",
        value="10.5K",
        properties={"LCSC Part": "C137808"},
        name="R16",
    )
    r28 = Part(
        refs.get("R28", "R28"),
        "easyeda2kicad:RC0402FR-0710KL",
        footprint="easyeda2kicad:R0402",
        footprint_definition="easyeda2kicad:R0402_8",
        value="10K",
        properties={"LCSC Part": "C60490"},
        name="R28",
    )
    r29 = Part(
        refs.get("R29", "R29"),
        "easyeda2kicad:RC0402FR-0710KL",
        footprint="easyeda2kicad:R0402",
        footprint_definition="easyeda2kicad:R0402_9",
        value="10K",
        properties={"LCSC Part": "C60490"},
        name="R29",
    )
    r30 = Part(
        refs.get("R30", "R30"),
        "easyeda2kicad:RC0402FR-0710KL",
        footprint="easyeda2kicad:R0402",
        footprint_definition="easyeda2kicad:R0402_11",
        value="10K",
        properties={"LCSC Part": "C60490"},
        name="R30",
    )
    r31 = Part(
        refs.get("R31", "R31"),
        "easyeda2kicad:RC0402FR-07100KL",
        footprint="easyeda2kicad:R0402",
        footprint_definition="easyeda2kicad:R0402_12",
        value="100K",
        properties={"LCSC Part": "C60491"},
        name="R31",
    )
    r33 = Part(
        refs.get("R33", "R33"),
        "easyeda2kicad:RC0603FR-070RL",
        footprint="easyeda2kicad:R0603",
        footprint_definition="easyeda2kicad:R0603_13",
        value="0",
        properties={"LCSC Part": "C100044"},
        name="R33",
    )
    r34 = Part(
        refs.get("R34", "R34"),
        "easyeda2kicad:RC0603FR-075K23L",
        footprint="easyeda2kicad:R0603",
        footprint_definition="easyeda2kicad:R0603_14",
        value="5.23K",
        properties={"LCSC Part": "C185317"},
        name="R34",
    )
    r35 = Part(
        refs.get("R35", "R35"),
        "easyeda2kicad:RC0603FR-07255KL_C295887",
        footprint="easyeda2kicad:R0603",
        footprint_definition="easyeda2kicad:R0603_15",
        value="255K",
        properties={"LCSC Part": "C295887"},
        name="R35",
    )
    r36 = Part(
        refs.get("R36", "R36"),
        "easyeda2kicad:RC0402FR-7W100RL",
        footprint="easyeda2kicad:R0402",
        footprint_definition="easyeda2kicad:R0402_14",
        value="100",
        properties={"LCSC Part": "C606168"},
        name="R36",
    )
    r37 = Part(
        refs.get("R37", "R37"),
        "easyeda2kicad:RC0402FR-07100KL",
        footprint="easyeda2kicad:R0402",
        footprint_definition="easyeda2kicad:R0402_15",
        value="100K",
        properties={"LCSC Part": "C60491"},
        name="R37",
    )
    r38 = Part(
        refs.get("R38", "R38"),
        "easyeda2kicad:RC0603FR-0730K1L",
        footprint="easyeda2kicad:R0603",
        footprint_definition="easyeda2kicad:R0603_16",
        value="30.1K",
        properties={"LCSC Part": "C137745"},
        name="R38",
    )
    r39 = Part(
        refs.get("R39", "R39"),
        "easyeda2kicad:RC0402FR-7W200KL",
        footprint="easyeda2kicad:R0402",
        footprint_definition="easyeda2kicad:R0402_16",
        value="200K",
        properties={"LCSC Part": "C606170"},
        name="R39",
    )
    r40 = Part(
        refs.get("R40", "R40"),
        "easyeda2kicad:RC0603FR-0727KL",
        footprint="easyeda2kicad:R0603",
        footprint_definition="easyeda2kicad:R0603_17",
        value="27K",
        properties={"LCSC Part": "C114614"},
        name="R40",
    )
    r42 = Part(
        refs.get("R42", "R42"),
        "easyeda2kicad:RT0603BRD077K15L",
        footprint="easyeda2kicad:R0603",
        footprint_definition="easyeda2kicad:R0603_19",
        value="7.15K",
        properties={"LCSC Part": "C861562"},
        name="R42",
    )
    r50 = Part(
        refs.get("R50", "R50"),
        "easyeda2kicad:RC0402FR-0710KL",
        footprint="easyeda2kicad:R0402",
        footprint_definition="easyeda2kicad:R0402_25",
        value="10K",
        properties={"LCSC Part": "C60490"},
        name="R50",
    )
    r72 = Part(
        refs.get("R72", "R72"),
        "easyeda2kicad:RC0603FR-070RL",
        footprint="easyeda2kicad:R0603",
        footprint_definition="easyeda2kicad:R0603_23",
        value="0",
        properties={"LCSC Part": "C100044"},
        name="R72",
    )
    r73 = Part(
        refs.get("R73", "R73"),
        "easyeda2kicad:RC0603FR-070RL",
        footprint="easyeda2kicad:R0603",
        footprint_definition="easyeda2kicad:R0603_24",
        value="0",
        properties={"LCSC Part": "C100044"},
        dnp=True,
        name="R73",
    )
    r83 = Part(
        refs.get("R83", "R83"),
        "easyeda2kicad:HPCR0402F2R00G9",
        footprint="easyeda2kicad:R0402",
        footprint_definition="easyeda2kicad:R0402_57",
        value="2",
        properties={"LCSC Part": "C514778"},
        name="R83",
    )
    r84 = Part(
        refs.get("R84", "R84"),
        "easyeda2kicad:RC0402FR-07294RL",
        footprint="easyeda2kicad:R0402",
        footprint_definition="easyeda2kicad:R0402_58",
        value="294",
        properties={"LCSC Part": "C477682"},
        name="R84",
    )
    r85 = Part(
        refs.get("R85", "R85"),
        "easyeda2kicad:RC0402FR-07294RL",
        footprint="easyeda2kicad:R0402",
        footprint_definition="easyeda2kicad:R0402_59",
        value="294",
        properties={"LCSC Part": "C477682"},
        name="R85",
    )
    r86 = Part(
        refs.get("R86", "R86"),
        "easyeda2kicad:HPCR0402F2R00G9",
        footprint="easyeda2kicad:R0402",
        footprint_definition="easyeda2kicad:R0402_60",
        value="2",
        properties={"LCSC Part": "C514778"},
        name="R86",
    )
    solarpower1 = Part(
        refs.get("Solarpower1", "Solarpower1"),
        "Library:ZX-PM2.54-1-2PY",
        footprint="easyeda2kicad:HDR-TH_2P-P2.54-V-F",
        footprint_definition="easyeda2kicad:HDR-TH_2P-P2.54-V-F_2",
        value="ZX-PM2.54-1-2PY",
        properties={"LCSC Part": "C7499322"},
        dnp=True,
        name="Solarpower1",
    )
    tp1 = Part(
        refs.get("TP1", "TP1"),
        "Connector:TestPoint",
        footprint="TestPoint:TestPoint_Pad_D1.5mm",
        value="T_PG",
        dnp=True,
        name="TP1",
    )
    tp2 = Part(
        refs.get("TP2", "TP2"),
        "Connector:TestPoint",
        footprint="TestPoint:TestPoint_Pad_D1.5mm",
        footprint_definition="TestPoint:TestPoint_Pad_D1.5mm_2",
        value="T_PG",
        dnp=True,
        name="TP2",
    )
    tp7 = Part(
        refs.get("TP7", "TP7"),
        "Connector:TestPoint",
        footprint="TestPoint:TestPoint_Pad_D1.5mm",
        footprint_definition="TestPoint:TestPoint_Pad_D1.5mm_3",
        value="T_PG",
        dnp=True,
        name="TP7",
    )
    tp8 = Part(
        refs.get("TP8", "TP8"),
        "Connector:TestPoint",
        footprint="TestPoint:TestPoint_Pad_D1.5mm",
        footprint_definition="TestPoint:TestPoint_Pad_D1.5mm_4",
        value="T_PG",
        dnp=True,
        name="TP8",
    )
    u5 = Part(
        refs.get("U5", "U5"),
        "easyeda2kicad:BQ25798RQMR",
        footprint="easyeda2kicad:QFN-29_L4.0-W4.0-P0.40-TL-BQ25792RQMR",
        value="BQ25798RQMR",
        properties={"LCSC Part": "C2876593"},
        name="U5",
    )
    u6 = Part(
        refs.get("U6", "U6"),
        "easyeda2kicad:TPS62903QRYTRQ1_C20345985",
        footprint="easyeda2kicad:VQFNHR-9_L2.2-W2.0_TPS62993QRYTRQ1",
        value="TPS62903QRYTRQ1_C20345985",
        properties={"LCSC Part": "C20345985"},
        name="U6",
    )
    module.add(
        battery1,
        c23,
        c26,
        c27,
        c28,
        c29,
        c30,
        c31,
        c33,
        c34,
        c35,
        c36,
        c37,
        c38,
        c39,
        c40,
        c41,
        c42,
        c43,
        c44,
        c45,
        c46,
        c47,
        c48,
        c49,
        c87,
        c88,
        c89,
        c90,
        c91,
        c94,
        d3,
        d8,
        d9,
        dc1,
        fb1,
        l1,
        l2,
        led3,
        q3,
        q4,
        q5,
        q6,
        r16,
        r28,
        r29,
        r30,
        r31,
        r33,
        r34,
        r35,
        r36,
        r37,
        r38,
        r39,
        r40,
        r42,
        r50,
        r72,
        r73,
        r83,
        r84,
        r85,
        r86,
        solarpower1,
        tp1,
        tp2,
        tp7,
        tp8,
        u5,
        u6,
    )
    connect(net_3v3, r28["2"], r29["2"])
    connect(net_5vbat, c42["2"], c43["2"], c44["2"], c45["2"], l2["1"], r39["2"], u6["3"])
    connect(net_5vusb, c89["2"], q5["5"], r83["2"], u5["8"])
    connect(scl, r28["1"], u5["14"])
    connect(sda, r29["1"], u5["15"])
    connect(solar_module_acdrv1, r85["2"], u5["11"])
    connect(solar_module_acdrv2, r84["2"], u5["10"])
    connect(solar_module_btst1, c28["1"], u5["4"])
    connect(solar_module_btst2, c29["1"], u5["19"])
    connect(solar_module_fb_vset, r39["1"], r40["2"], tp2["1"], u6["9"])
    connect(solar_module_ilim_hiz, r35["2"], r37["2"], u5["17"])
    connect(solar_module_prog, r16["2"], u5["20"])
    connect(solar_module_regn, c36["2"], r34["1"], r35["1"], u5["5"])
    connect(solar_module_sw1, c28["2"], l1["1"], u5["28"])
    connect(solar_module_sw2, c29["2"], l1["2"], u5["26"])
    connect(solar_module_sys, c26["2"], c27["2"], r72["1"], tp7["1"], u5["25"])
    connect(solar_module_solar, c90["2"], d3["1"], dc1["1"], q3["5"], r86["2"], solarpower1["1"], u5["9"])
    connect(
        solar_module_vbat,
        battery1["1"],
        c23["2"],
        c30["2"],
        r36["2"],
        r73["1"],
        tp8["1"],
        u5["22"],
        u5["23"],
    )
    connect(
        solar_module_vbus,
        c31["2"],
        c33["2"],
        c34["2"],
        c35["2"],
        q4["5"],
        q6["5"],
        r30["1"],
        u5["2"],
        u5["3"],
    )
    connect(gnd, fb1["1"])
    connect(net_c91_pad2, c91["2"], r83["1"])
    connect(net_c94_pad2, c94["2"], r86["1"])
    connect(net_d8_a, c87["2"], d8["2"], q3["1"], q3["2"], q3["3"], q4["1"], q4["2"], q4["3"])
    connect(net_d8_k, c87["1"], d8["1"], q3["4"], q4["4"], r85["1"])
    connect(net_d9_a, c88["2"], d9["2"], q5["1"], q5["2"], q5["3"], q6["1"], q6["2"], q6["3"])
    connect(net_d9_k, c88["1"], d9["1"], q5["4"], q6["4"], r84["1"])
    connect(net_led3_a, led3["2"], r30["2"])
    connect(net_led3_k, led3["1"], u5["1"])
    connect(net_r16_pad1, r16["1"], r33["1"])
    connect(net_u5_batp, r36["1"], u5["18"])
    connect(net_u5_pmid, c37["2"], c38["2"], c39["2"], c40["2"], u5["29"])
    connect(net_u5_sdrv, c41["2"], u5["24"])
    connect(net_u5_ts, r34["2"], r38["1"], r50["2"], u5["16"])
    connect(net_u5_ce, r31["1"], u5["13"])
    connect(net_u6_en, c46["2"], c47["2"], c48["2"], r72["2"], r73["2"], u6["5"], u6["6"])
    connect(net_u6_mode_s_conf, r42["2"], u6["7"])
    connect(net_u6_pg, tp1["1"], u6["1"])
    connect(net_u6_ss_tr, c49["2"], u6["8"])
    connect(net_u6_sw, l2["2"], u6["2"])
    connect(
        pgnd,
        battery1["2"],
        c23["1"],
        c26["1"],
        c27["1"],
        c30["1"],
        c31["1"],
        c33["1"],
        c34["1"],
        c35["1"],
        c36["1"],
        c37["1"],
        c38["1"],
        c39["1"],
        c40["1"],
        c41["1"],
        c42["1"],
        c43["1"],
        c44["1"],
        c45["1"],
        c46["1"],
        c47["1"],
        c48["1"],
        c49["1"],
        c89["1"],
        c90["1"],
        c91["1"],
        c94["1"],
        d3["2"],
        dc1["2"],
        dc1["3"],
        dc1["4"],
        fb1["2"],
        r31["2"],
        r33["2"],
        r37["1"],
        r38["2"],
        r40["1"],
        r42["1"],
        r50["1"],
        solarpower1["2"],
        u5["27"],
        u6["4"],
    )
    battery1.place(mm("91.56"), mm("-38.21"), rot=-90, side="bottom")
    c23.place(mm("68.845"), mm("-37.68"), side="bottom")
    c26.place(mm("75.785"), mm("-39.38"), rot=180, side="bottom")
    c27.place(mm("69.77"), mm("-44.98"), side="bottom")
    c28.place(mm("81.21"), mm("-35.805"), rot=90, side="bottom")
    c29.place(mm("72.935"), mm("-34.48"), rot=90, side="bottom")
    c30.place(mm("70.31"), mm("-33.365"), rot=90, side="bottom")
    c31.place(mm("78.73"), mm("-31.69"), side="bottom")
    c33.place(mm("79.395"), mm("-29.38"), side="bottom")
    c34.place(mm("83.71"), mm("-32.18"), rot=-90, side="bottom")
    c35.place(mm("86.06"), mm("-31.17"), rot=-90, side="bottom")
    c36.place(mm("86.1"), mm("-35.65"), rot=-90, side="bottom")
    c37.place(mm("78.41"), mm("-39.405"), side="bottom")
    c38.place(mm("86.135"), mm("-43.72"), rot=-90, side="bottom")
    c39.place(mm("83.01"), mm("-38.78"), rot=90, side="bottom")
    c40.place(mm("83.11"), mm("-43.72"), rot=-90, side="bottom")
    c41.place(mm("73.56"), mm("-37.805"), rot=-90, side="bottom")
    c42.place(mm("82.6"), mm("-16.08"), side="bottom")
    c43.place(mm("87.225"), mm("-13.855"), rot=180, side="bottom")
    c44.place(mm("82.6"), mm("-17.53"), side="bottom")
    c45.place(mm("81.56"), mm("-13.83"), side="bottom")
    c46.place(mm("77.185"), mm("-16.78"), side="bottom")
    c47.place(mm("80.035"), mm("-18.905"), rot=90, side="bottom")
    c48.place(mm("77.21"), mm("-19.305"), side="bottom")
    c49.place(mm("83.95"), mm("-23.43"), rot=-90, side="bottom")
    c87.place(mm("66.79"), mm("-3.59"), rot=90, side="bottom")
    c88.place(mm("61.2625"), mm("-0.855"), rot=90, side="bottom")
    c89.place(mm("81.41"), mm("-33.68"), rot=180, side="bottom")
    c90.place(mm("81.435"), mm("-32.305"), rot=180, side="bottom")
    c91.place(mm("61.65"), mm("4.43"), rot=90, side="bottom")
    c94.place(mm("67.93"), mm("5.01"), rot=90, side="bottom")
    d3.place(mm("81.46"), mm("20.52"), side="bottom")
    d8.place(mm("66.8"), mm("-0.76"), rot=90, side="bottom")
    d9.place(mm("59.7625"), mm("-0.755"), rot=90, side="bottom")
    dc1.place(mm("89.26"), mm("16.42"), rot=90)
    fb1.place(mm("74.83"), mm("-21.68"), side="bottom")
    l1.place(mm("77.04"), mm("-43.964998"), rot=180, side="bottom")
    l2.place(mm("87.35"), mm("-18.81"), rot=90, side="bottom")
    led3.place(mm("85.41"), mm("-38.68"), rot=180, side="bottom")
    q3.place(mm("64.17"), mm("1.55"), rot=-90, side="bottom")
    q4.place(mm("64.18"), mm("-2.99"), rot=90, side="bottom")
    q5.place(mm("56.9675"), mm("1.495"), rot=-90, side="bottom")
    q6.place(mm("56.9825"), mm("-2.89"), rot=90, side="bottom")
    r16.place(mm("69.61"), mm("-40.88"), side="bottom")
    r28.place(mm("59.84"), mm("-45.62"), rot=-90, side="bottom")
    r29.place(mm("58.24"), mm("-45.62"), rot=-90, side="bottom")
    r30.place(mm("85.04"), mm("-40.23"), rot=180, side="bottom")
    r31.place(mm("74.66"), mm("-31.68"), rot=180, side="bottom")
    r33.place(mm("69.61"), mm("-42.68"), rot=180, side="bottom")
    r34.place(mm("76.8"), mm("-25.81"), rot=180, side="bottom")
    r35.place(mm("76.81"), mm("-24.18"), rot=180, side="bottom")
    r36.place(mm("67.99"), mm("-31.5"), rot=90, side="bottom")
    r37.place(mm("73.46"), mm("-24.04"), side="bottom")
    r38.place(mm("73.26"), mm("-25.82"), rot=180, side="bottom")
    r39.place(mm("84.66"), mm("-26.01"), rot=90, side="bottom")
    r40.place(mm("83.16"), mm("-26.53"), rot=-90, side="bottom")
    r42.place(mm("81.8"), mm("-23.53"), rot=-90, side="bottom")
    r50.place(mm("72.43"), mm("-31.93"), rot=90, side="bottom")
    r72.place(mm("80"), mm("-23.43"), rot=-90, side="bottom")
    r73.place(mm("78.36"), mm("-21.93"), rot=-90, side="bottom")
    r83.place(mm("59.96"), mm("3.78"), rot=180, side="bottom")
    r84.place(mm("61.2875"), mm("-3.53"), rot=90, side="bottom")
    r85.place(mm("66.2"), mm("-7.1"), rot=90, side="bottom")
    r86.place(mm("67.25"), mm("2.81"), rot=180, side="bottom")
    solarpower1.place(mm("81.28"), mm("16.62"))
    tp1.place(mm("88.05"), mm("-23.08"), rot=-90, side="bottom")
    tp2.place(mm("86.65"), mm("-25.48"), rot=-90, side="bottom")
    tp7.place(mm("65.76"), mm("-44.68"), rot=180, side="bottom")
    tp8.place(mm("69.56"), mm("-20.88"), rot=180, side="bottom")
    u5.place(mm("77.08"), mm("-35.235"), rot=180, side="bottom")
    u6.place(mm("82.64"), mm("-19.83"), rot=180, side="bottom")
    return module
