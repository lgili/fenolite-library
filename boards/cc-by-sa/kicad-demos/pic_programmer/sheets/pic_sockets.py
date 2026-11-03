# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/pic_programmer@97acc80c223d75520c03fc44cab63cd9a3202c42 by Fenolite 0.7.0.dev0 on 2026-11-03;
# modified: format conversion to the Fenolite DSL.

from fenolite.dsl import Module, Part, connect, mm


def sheet(design, *, path, refs=None, **nets):
    module = Module(path.rsplit("/", 1)[-1])
    design.add(module)
    refs = refs or {}
    clock_rb6 = nets["clock_rb6"]
    data_rb7 = nets["data_rb7"]
    vpp_mclr = nets["vpp_mclr"]
    pic_sockets_vcc_pic = nets["pic_sockets_vcc_pic"]
    gnd = nets["gnd"]
    c6 = Part(
        refs.get("C6", "C6"),
        "pic_programmer:C",
        footprint="Capacitor_THT:C_Disc_D5.1mm_W3.2mm_P5.00mm",
        footprint_definition="Capacitor_THT:C_Disc_D5.1mm_W3.2mm_P5.00mm_3",
        value="100nF",
        name="C6",
    )
    c7 = Part(
        refs.get("C7", "C7"),
        "pic_programmer:C",
        footprint="Capacitor_THT:C_Disc_D5.1mm_W3.2mm_P5.00mm",
        footprint_definition="Capacitor_THT:C_Disc_D5.1mm_W3.2mm_P5.00mm_3",
        value="100nF",
        name="C7",
    )
    p2 = Part(
        refs.get("P2", "P2"),
        "pic_programmer:SUPP28",
        footprint="Package_DIP:DIP-28_W7.62mm_Socket_LongPads",
        value="SUPP28",
        name="P2",
    )
    p3 = Part(
        refs.get("P3", "P3"),
        "pic_programmer:SUPP40",
        footprint="footprints:40tex-Ell600",
        value="SUPP40",
        name="P3",
    )
    u1 = Part(
        refs.get("U1", "U1"),
        "pic_programmer:24C16",
        footprint="Package_DIP:DIP-8_W7.62mm_Socket_LongPads",
        value="24Cxx",
        name="U1",
    )
    u5 = Part(
        refs.get("U5", "U5"),
        "pic_programmer:PIC16F54",
        footprint="Package_DIP:DIP-18_W7.62mm_Socket_LongPads",
        value="PIC_18_PINS",
        name="U5",
    )
    u6 = Part(
        refs.get("U6", "U6"),
        "pic_programmer:PIC12C508A",
        footprint="Package_DIP:DIP-8_W7.62mm_Socket_LongPads",
        footprint_definition="Package_DIP:DIP-8_W7.62mm_Socket_LongPads_2",
        value="PIC_8_PINS",
        name="U6",
    )
    module.add(c6, c7, p2, p3, u1, u5, u6)
    connect(clock_rb6, p2["27"], p3["39"], u1["6"], u5["12"], u6["6"])
    connect(data_rb7, p2["28"], p3["40"], u1["5"], u5["13"], u6["7"])
    connect(vpp_mclr, p2["1"], p3["1"], u5["4"], u6["4"])
    connect(pic_sockets_vcc_pic, c6["1"], c7["1"], p2["20"], p3["11"], p3["32"], u1["8"], u5["14"], u6["1"])
    connect(
        gnd,
        c6["2"],
        c7["2"],
        p2["19"],
        p2["8"],
        p3["12"],
        p3["31"],
        p3["8"],
        u1["1"],
        u1["2"],
        u1["3"],
        u1["4"],
        u5["5"],
        u6["8"],
    )
    c6.place(mm("96.85"), mm("12.395"), rot=-90)
    c7.place(mm("98.755"), mm("-28.88"), rot=-90)
    p2.place(mm("107.645"), mm("-49.2"))
    p3.place(mm("75.26"), mm("-49.2"))
    u1.place(mm("79.07"), mm("9.22"))
    u5.place(mm("107.899"), mm("7.95"))
    u6.place(mm("79.07"), mm("20.65"))
    return module
