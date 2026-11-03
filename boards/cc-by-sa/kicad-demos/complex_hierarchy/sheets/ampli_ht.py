# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/complex_hierarchy@97acc80c223d75520c03fc44cab63cd9a3202c42 by Fenolite 0.7.0.dev0 on 2026-11-03;
# modified: format conversion to the Fenolite DSL.

from fenolite.dsl import Module, Net, Part, connect, mm


def sheet(design, *, path, refs=None, **nets):
    module = Module(path.rsplit("/", 1)[-1])
    design.add(module)
    refs = refs or {}
    if path == "ampli_ht_vertical":
        net_12v = nets["net_12v"]
        vaa = nets["vaa"]
        ampli_ht_vertical_piezo_in = Net("/ampli_ht_vertical/PIEZO_IN")
        ampli_ht_vertical_piezo_out = Net("/ampli_ht_vertical/PIEZO_OUT")
        ampli_ht_vertical_s_out = Net("/ampli_ht_vertical/S_OUT+")
        ampli_ht_vertical_vpil_0_3_3v = Net("/ampli_ht_vertical/Vpil_0_3,3V")
        gnd = nets["gnd"]
        ht = nets["ht"]
        net_c201_pad2 = Net("Net-(C201-Pad2)")
        net_c202_pad1 = Net("Net-(C202-Pad1)")
        net_c204_pad1 = Net("Net-(C204-Pad1)")
        net_d201_k = Net("Net-(D201-K)")
        net_d202_k = Net("Net-(D202-K)")
        net_d203_a = Net("Net-(D203-A)")
        net_d203_k = Net("Net-(D203-K)")
        net_d204_k = Net("Net-(D204-K)")
        net_q201_e = Net("Net-(Q201-E)")
        net_q202_e = Net("Net-(Q202-E)")
        net_q203_e = Net("Net-(Q203-E)")
        net_q204_b = Net("Net-(Q204-B)")
        net_q204_e = Net("Net-(Q204-E)")
        net_r212_pad2 = Net("Net-(R212-Pad2)")
        net_r213_pad1 = Net("Net-(R213-Pad1)")
        net_u201a = Net("Net-(U201A--)")
        net_u201b = Net("Net-(U201B-+)")
        c201 = Part(
            refs.get("C201", "C201"),
            "complex_hierarchy:C",
            footprint="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm",
            value="15nF",
            name="C201",
        )
        c202 = Part(
            refs.get("C202", "C202"),
            "complex_hierarchy:C",
            footprint="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm",
            footprint_definition="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm_2",
            value="150nF",
            name="C202",
        )
        c203 = Part(
            refs.get("C203", "C203"),
            "complex_hierarchy:C",
            footprint="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm",
            footprint_definition="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm_3",
            value="4.7nF",
            name="C203",
        )
        c204 = Part(
            refs.get("C204", "C204"),
            "complex_hierarchy:C",
            footprint="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm",
            footprint_definition="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm_4",
            value="820pF",
            name="C204",
        )
        d201 = Part(
            refs.get("D201", "D201"),
            "complex_hierarchy:D_Small",
            footprint="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal",
            value="1N4148",
            name="D201",
        )
        d202 = Part(
            refs.get("D202", "D202"),
            "complex_hierarchy:D_Small",
            footprint="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal",
            footprint_definition="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal_2",
            value="1N4148",
            name="D202",
        )
        d203 = Part(
            refs.get("D203", "D203"),
            "complex_hierarchy:D_Small",
            footprint="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal",
            footprint_definition="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal_3",
            value="1N4148",
            name="D203",
        )
        d204 = Part(
            refs.get("D204", "D204"),
            "complex_hierarchy:D_Small",
            footprint="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal",
            footprint_definition="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal_4",
            value="1N4148",
            name="D204",
        )
        p201 = Part(
            refs.get("P201", "P201"),
            "complex_hierarchy:CONN_2",
            footprint="TerminalBlock_Altech:Altech_AK300_1x02_P5.00mm_45-Degree",
            footprint_definition="TerminalBlock_Altech:Altech_AK300_1x02_P5.00mm_45-Degree_3",
            value="CONN_2",
            name="P201",
        )
        p202 = Part(
            refs.get("P202", "P202"),
            "complex_hierarchy:CONN_2",
            footprint="TerminalBlock_Altech:Altech_AK300_1x02_P5.00mm_45-Degree",
            footprint_definition="TerminalBlock_Altech:Altech_AK300_1x02_P5.00mm_45-Degree_4",
            value="CONN_2",
            name="P202",
        )
        q201 = Part(
            refs.get("Q201", "Q201"),
            "complex_hierarchy:MPSA92",
            footprint="Package_TO_SOT_THT:TO-92_HandSolder",
            value="MPSA92",
            name="Q201",
        )
        q202 = Part(
            refs.get("Q202", "Q202"),
            "complex_hierarchy:MPSA42",
            footprint="Package_TO_SOT_THT:TO-92_HandSolder",
            footprint_definition="Package_TO_SOT_THT:TO-92_HandSolder_2",
            value="MPSA42",
            name="Q202",
        )
        q203 = Part(
            refs.get("Q203", "Q203"),
            "complex_hierarchy:MPSA92",
            footprint="Package_TO_SOT_THT:TO-92_HandSolder",
            footprint_definition="Package_TO_SOT_THT:TO-92_HandSolder_3",
            value="MPSA92",
            name="Q203",
        )
        q204 = Part(
            refs.get("Q204", "Q204"),
            "complex_hierarchy:MPSA42",
            footprint="Package_TO_SOT_THT:TO-92_HandSolder",
            footprint_definition="Package_TO_SOT_THT:TO-92_HandSolder_4",
            value="MPSA42",
            name="Q204",
        )
        r201 = Part(
            refs.get("R201", "R201"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            value="1K",
            name="R201",
        )
        r202 = Part(
            refs.get("R202", "R202"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_2",
            value="22K",
            name="R202",
        )
        r203 = Part(
            refs.get("R203", "R203"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_3",
            value="22K",
            name="R203",
        )
        r204 = Part(
            refs.get("R204", "R204"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
            value="470",
            name="R204",
        )
        r205 = Part(
            refs.get("R205", "R205"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_5",
            value="220K",
            name="R205",
        )
        r206 = Part(
            refs.get("R206", "R206"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
            value="47",
            name="R206",
        )
        r207 = Part(
            refs.get("R207", "R207"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
            value="47",
            name="R207",
        )
        r208 = Part(
            refs.get("R208", "R208"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
            value="1K",
            name="R208",
        )
        r209 = Part(
            refs.get("R209", "R209"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_5",
            value="220K",
            name="R209",
        )
        r210 = Part(
            refs.get("R210", "R210"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_5",
            value="220K",
            name="R210",
        )
        r211 = Part(
            refs.get("R211", "R211"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_6",
            value="5,6K",
            name="R211",
        )
        r212 = Part(
            refs.get("R212", "R212"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
            value="1K",
            name="R212",
        )
        r213 = Part(
            refs.get("R213", "R213"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_7",
            value="4,7K",
            name="R213",
        )
        rv201 = Part(
            refs.get("RV201", "RV201"),
            "complex_hierarchy:POT",
            footprint="Potentiometer_THT:Potentiometer_Bourns_3266W_Vertical",
            value="4,7K",
            name="RV201",
        )
        u201 = Part(
            refs.get("U201", "U201"),
            "complex_hierarchy:LM358N",
            footprint="Package_DIP:DIP-8_W7.62mm_LongPads",
            footprint_definition="Package_DIP:DIP-8_W7.62mm_LongPads_2",
            value="LM358N",
            name="U201",
        )
        module.add(
            c201,
            c202,
            c203,
            c204,
            d201,
            d202,
            d203,
            d204,
            p201,
            p202,
            q201,
            q202,
            q203,
            q204,
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
            rv201,
            u201,
        )
        connect(net_12v, u201["8"])
        connect(vaa, u201["4"])
        connect(ampli_ht_vertical_piezo_in, p201["1"], r201["2"])
        connect(ampli_ht_vertical_piezo_out, p202["1"], r206["1"], r207["1"])
        connect(ampli_ht_vertical_s_out, r209["1"], r210["1"], rv201["3"])
        connect(ampli_ht_vertical_vpil_0_3_3v, c201["1"], u201["3"], u201["6"], u201["7"])
        connect(
            gnd,
            c202["2"],
            c203["2"],
            c204["2"],
            p201["2"],
            p202["2"],
            q203["3"],
            r205["2"],
            r208["2"],
            r213["2"],
        )
        connect(ht, d201["2"], q202["3"], r204["1"])
        connect(net_c201_pad2, c201["2"], r202["1"], r203["2"])
        connect(net_c202_pad1, c202["1"], r201["1"], r202["2"])
        connect(net_c204_pad1, c204["1"], r211["2"])
        connect(net_d201_k, d201["1"], d202["2"])
        connect(net_d202_k, d202["1"], q201["2"], r205["1"])
        connect(net_d203_a, d203["2"], q201["3"], q202["2"])
        connect(net_d203_k, d203["1"], d204["2"])
        connect(net_d204_k, d204["1"], q203["2"], q204["3"], r211["1"])
        connect(net_q201_e, q201["1"], r204["2"])
        connect(net_q202_e, q202["1"], r206["2"], r210["2"])
        connect(net_q203_e, q203["1"], r207["2"], r209["2"])
        connect(net_q204_b, q204["2"], r208["1"])
        connect(net_q204_e, q204["1"], r212["1"])
        connect(net_r212_pad2, r212["2"], u201["1"])
        connect(net_r213_pad1, r213["1"], rv201["1"])
        connect(net_u201a, rv201["2"], u201["2"])
        connect(net_u201b, c203["1"], r203["1"], u201["5"])
        c201.place(mm("18.618"), mm("9.474"), rot=180)
        c202.place(mm("13.665"), mm("6.045"))
        c203.place(mm("13.665"), mm("12.776"))
        c204.place(mm("38.176"), mm("30.048"))
        d201.place(mm("27.635"), mm("5.918"))
        d202.place(mm("27.635"), mm("8.966"))
        d203.place(mm("44.78"), mm("23.571"), rot=90)
        d204.place(mm("40.97"), mm("23.571"), rot=90)
        p201.place(mm("-5.385"), mm("11.633"), rot=-90)
        p202.place(mm("81.1925"), mm("12.4575"), rot=90)
        q201.place(mm("31.445"), mm("15.316"))
        q202.place(mm("49.225"), mm("15.062"))
        q203.place(mm("51.765"), mm("23.825"), rot=180)
        q204.place(mm("30.556"), mm("25.73"))
        r201.place(mm("9.855"), mm("7.061"), rot=180)
        r202.place(mm("9.855"), mm("10.236"), rot=180)
        r203.place(mm("9.855"), mm("12.776"), rot=180)
        r204.place(mm("46.685"), mm("8.966"), rot=180)
        r205.place(mm("22.555"), mm("15.316"), rot=-90)
        r206.place(mm("73.355"), mm("19.126"), rot=180)
        r207.place(mm("73.355"), mm("22.936"), rot=180)
        r208.place(mm("26.365"), mm("28.016"), rot=180)
        r209.place(mm("56.21"), mm("16.713"), rot=-90)
        r210.place(mm("60.02"), mm("16.586"), rot=-90)
        r211.place(mm("44.399"), mm("26.873"), rot=180)
        r212.place(mm("34.493"), mm("20.142"), rot=180)
        r213.place(mm("2.87"), mm("26.746"), rot=90)
        rv201.place(mm("-6.655"), mm("25.476"), rot=180)
        u201.place(mm("7.315"), mm("24.206"), rot=90)
    elif path == "ampli_ht_horizontal":
        net_12v = nets["net_12v"]
        vaa = nets["vaa"]
        ampli_ht_horizontal_piezo_in = Net("/ampli_ht_horizontal/PIEZO_IN")
        ampli_ht_horizontal_piezo_out = Net("/ampli_ht_horizontal/PIEZO_OUT")
        ampli_ht_horizontal_s_out = Net("/ampli_ht_horizontal/S_OUT+")
        ampli_ht_horizontal_vpil_0_3_3v = Net("/ampli_ht_horizontal/Vpil_0_3,3V")
        gnd = nets["gnd"]
        ht = nets["ht"]
        net_c301_pad2 = Net("Net-(C301-Pad2)")
        net_c302_pad1 = Net("Net-(C302-Pad1)")
        net_c304_pad1 = Net("Net-(C304-Pad1)")
        net_d301_k = Net("Net-(D301-K)")
        net_d302_k = Net("Net-(D302-K)")
        net_d303_a = Net("Net-(D303-A)")
        net_d303_k = Net("Net-(D303-K)")
        net_d304_k = Net("Net-(D304-K)")
        net_q301_e = Net("Net-(Q301-E)")
        net_q302_e = Net("Net-(Q302-E)")
        net_q303_e = Net("Net-(Q303-E)")
        net_q304_b = Net("Net-(Q304-B)")
        net_q304_e = Net("Net-(Q304-E)")
        net_r312_pad2 = Net("Net-(R312-Pad2)")
        net_r313_pad1 = Net("Net-(R313-Pad1)")
        net_u301a = Net("Net-(U301A--)")
        net_u301b = Net("Net-(U301B-+)")
        c301 = Part(
            refs.get("C201", "C301"),
            "complex_hierarchy:C",
            footprint="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm",
            footprint_definition="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm_5",
            value="15nF",
            name="C201",
        )
        c302 = Part(
            refs.get("C202", "C302"),
            "complex_hierarchy:C",
            footprint="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm",
            footprint_definition="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm_6",
            value="150nF",
            name="C202",
        )
        c303 = Part(
            refs.get("C203", "C303"),
            "complex_hierarchy:C",
            footprint="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm",
            footprint_definition="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm_7",
            value="4.7nF",
            name="C203",
        )
        c304 = Part(
            refs.get("C204", "C304"),
            "complex_hierarchy:C",
            footprint="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm",
            footprint_definition="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm_8",
            value="820pF",
            name="C204",
        )
        d301 = Part(
            refs.get("D201", "D301"),
            "complex_hierarchy:D_Small",
            footprint="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal",
            footprint_definition="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal_5",
            value="1N4148",
            name="D201",
        )
        d302 = Part(
            refs.get("D202", "D302"),
            "complex_hierarchy:D_Small",
            footprint="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal",
            footprint_definition="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal_6",
            value="1N4148",
            name="D202",
        )
        d303 = Part(
            refs.get("D203", "D303"),
            "complex_hierarchy:D_Small",
            footprint="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal",
            footprint_definition="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal_7",
            value="1N4148",
            name="D203",
        )
        d304 = Part(
            refs.get("D204", "D304"),
            "complex_hierarchy:D_Small",
            footprint="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal",
            footprint_definition="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal_8",
            value="1N4148",
            name="D204",
        )
        p301 = Part(
            refs.get("P201", "P301"),
            "complex_hierarchy:CONN_2",
            footprint="TerminalBlock_Altech:Altech_AK300_1x02_P5.00mm_45-Degree",
            footprint_definition="TerminalBlock_Altech:Altech_AK300_1x02_P5.00mm_45-Degree_5",
            value="CONN_2",
            name="P201",
        )
        p302 = Part(
            refs.get("P202", "P302"),
            "complex_hierarchy:CONN_2",
            footprint="TerminalBlock_Altech:Altech_AK300_1x02_P5.00mm_45-Degree",
            footprint_definition="TerminalBlock_Altech:Altech_AK300_1x02_P5.00mm_45-Degree_6",
            value="CONN_2",
            name="P202",
        )
        q301 = Part(
            refs.get("Q201", "Q301"),
            "complex_hierarchy:MPSA92",
            footprint="Package_TO_SOT_THT:TO-92_HandSolder",
            footprint_definition="Package_TO_SOT_THT:TO-92_HandSolder_5",
            value="MPSA92",
            name="Q201",
        )
        q302 = Part(
            refs.get("Q202", "Q302"),
            "complex_hierarchy:MPSA42",
            footprint="Package_TO_SOT_THT:TO-92_HandSolder",
            footprint_definition="Package_TO_SOT_THT:TO-92_HandSolder_2",
            value="MPSA42",
            name="Q202",
        )
        q303 = Part(
            refs.get("Q203", "Q303"),
            "complex_hierarchy:MPSA92",
            footprint="Package_TO_SOT_THT:TO-92_HandSolder",
            footprint_definition="Package_TO_SOT_THT:TO-92_HandSolder_6",
            value="MPSA92",
            name="Q203",
        )
        q304 = Part(
            refs.get("Q204", "Q304"),
            "complex_hierarchy:MPSA42",
            footprint="Package_TO_SOT_THT:TO-92_HandSolder",
            footprint_definition="Package_TO_SOT_THT:TO-92_HandSolder_2",
            value="MPSA42",
            name="Q204",
        )
        r301 = Part(
            refs.get("R201", "R301"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
            value="1K",
            name="R201",
        )
        r302 = Part(
            refs.get("R202", "R302"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_8",
            value="22K",
            name="R202",
        )
        r303 = Part(
            refs.get("R203", "R303"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_9",
            value="22K",
            name="R203",
        )
        r304 = Part(
            refs.get("R204", "R304"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
            value="470",
            name="R204",
        )
        r305 = Part(
            refs.get("R205", "R305"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_10",
            value="220K",
            name="R205",
        )
        r306 = Part(
            refs.get("R206", "R306"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
            value="47",
            name="R206",
        )
        r307 = Part(
            refs.get("R207", "R307"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
            value="47",
            name="R207",
        )
        r308 = Part(
            refs.get("R208", "R308"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
            value="1K",
            name="R208",
        )
        r309 = Part(
            refs.get("R209", "R309"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_5",
            value="220K",
            name="R209",
        )
        r310 = Part(
            refs.get("R210", "R310"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_5",
            value="220K",
            name="R210",
        )
        r311 = Part(
            refs.get("R211", "R311"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_11",
            value="5,6K",
            name="R211",
        )
        r312 = Part(
            refs.get("R212", "R312"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_4",
            value="1K",
            name="R212",
        )
        r313 = Part(
            refs.get("R213", "R313"),
            "complex_hierarchy:R",
            footprint="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal",
            footprint_definition="Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal_7",
            value="4,7K",
            name="R213",
        )
        rv301 = Part(
            refs.get("RV201", "RV301"),
            "complex_hierarchy:POT",
            footprint="Potentiometer_THT:Potentiometer_Bourns_3266W_Vertical",
            value="4,7K",
            name="RV201",
        )
        u301 = Part(
            refs.get("U201", "U301"),
            "complex_hierarchy:LM358N",
            footprint="Package_DIP:DIP-8_W7.62mm_LongPads",
            footprint_definition="Package_DIP:DIP-8_W7.62mm_LongPads_2",
            value="LM358N",
            name="U201",
        )
        module.add(
            c301,
            c302,
            c303,
            c304,
            d301,
            d302,
            d303,
            d304,
            p301,
            p302,
            q301,
            q302,
            q303,
            q304,
            r301,
            r302,
            r303,
            r304,
            r305,
            r306,
            r307,
            r308,
            r309,
            r310,
            r311,
            r312,
            r313,
            rv301,
            u301,
        )
        connect(net_12v, u301["8"])
        connect(vaa, u301["4"])
        connect(ampli_ht_horizontal_piezo_in, p301["1"], r301["2"])
        connect(ampli_ht_horizontal_piezo_out, p302["1"], r306["1"], r307["1"])
        connect(ampli_ht_horizontal_s_out, r309["1"], r310["1"], rv301["3"])
        connect(ampli_ht_horizontal_vpil_0_3_3v, c301["1"], u301["3"], u301["6"], u301["7"])
        connect(
            gnd,
            c302["2"],
            c303["2"],
            c304["2"],
            p301["2"],
            p302["2"],
            q303["3"],
            r305["2"],
            r308["2"],
            r313["2"],
        )
        connect(ht, d301["2"], q302["3"], r304["1"])
        connect(net_c301_pad2, c301["2"], r302["1"], r303["2"])
        connect(net_c302_pad1, c302["1"], r301["1"], r302["2"])
        connect(net_c304_pad1, c304["1"], r311["2"])
        connect(net_d301_k, d301["1"], d302["2"])
        connect(net_d302_k, d302["1"], q301["2"], r305["1"])
        connect(net_d303_a, d303["2"], q301["3"], q302["2"])
        connect(net_d303_k, d303["1"], d304["2"])
        connect(net_d304_k, d304["1"], q303["2"], q304["3"], r311["1"])
        connect(net_q301_e, q301["1"], r304["2"])
        connect(net_q302_e, q302["1"], r306["2"], r310["2"])
        connect(net_q303_e, q303["1"], r307["2"], r309["2"])
        connect(net_q304_b, q304["2"], r308["1"])
        connect(net_q304_e, q304["1"], r312["1"])
        connect(net_r312_pad2, r312["2"], u301["1"])
        connect(net_r313_pad1, r313["1"], rv301["1"])
        connect(net_u301a, rv301["2"], u301["2"])
        connect(net_u301b, c303["1"], r303["1"], u301["5"])
        c301.place(mm("18.745"), mm("-18.593"), rot=180)
        c302.place(mm("13.792"), mm("-22.022"))
        c303.place(mm("13.792"), mm("-15.164"))
        c304.place(mm("38.049"), mm("4.14"))
        d301.place(mm("25.095"), mm("-21.133"))
        d302.place(mm("32.715"), mm("-17.704"), rot=180)
        d303.place(mm("45.415"), mm("-2.464"), rot=90)
        d304.place(mm("41.605"), mm("-2.464"), rot=90)
        p301.place(mm("-5.1"), mm("-15"), rot=-90)
        p302.place(mm("81.2"), mm("-13.7"), rot=90)
        q301.place(mm("31.445"), mm("-11.354"))
        q302.place(mm("50.495"), mm("-10.084"))
        q303.place(mm("51.003"), mm("0.965"), rot=180)
        q304.place(mm("29.794"), mm("-3.48"), locked=True)
        r301.place(mm("10.363"), mm("-21.26"), rot=180)
        r302.place(mm("10.617"), mm("-17.704"), rot=180)
        r303.place(mm("2.997"), mm("-15.037"))
        r304.place(mm("45.415"), mm("-13.894"), rot=180)
        r305.place(mm("37.795"), mm("-18.974"))
        r306.place(mm("73.355"), mm("-8.814"), rot=180)
        r307.place(mm("73.355"), mm("-2.464"), rot=180)
        r308.place(mm("25.603"), mm("1.346"), rot=180)
        r309.place(mm("56.845"), mm("-10.084"), rot=-90)
        r310.place(mm("61.29"), mm("-10.084"), rot=-90)
        r311.place(mm("41.605"), mm("1.346"), rot=180)
        r312.place(mm("26.111"), mm("-5.004"), rot=180)
        r313.place(mm("2.235"), mm("2.616"), rot=90)
        rv301.place(mm("-6.655"), mm("0.076"), rot=180)
        u301.place(mm("7.315"), mm("-3.734"), rot=90)
    else:
        raise ValueError(f"unknown source sheet instance: {path}")
    return module
