# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/video@97acc80c223d75520c03fc44cab63cd9a3202c42 by Fenolite 0.7.0.dev0 on 2026-10-31;
# modified: format conversion to the Fenolite DSL.

from fenolite.dsl import Module, Part, connect, mm


def sheet(design, *, path, refs=None, **nets):
    module = Module(path.rsplit("/", 1)[-1])
    design.add(module)
    refs = refs or {}
    net_5v = nets["net_5v"]
    acces_ram = nets["acces_ram"]
    acq_on = nets["acq_on"]
    blank = nets["blank"]
    clamp = nets["clamp"]
    clkcad = nets["clkcad"]
    clkcda = nets["clkcda"]
    csync_out = nets["csync_out"]
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
    tvram0 = nets["tvram0"]
    tvram1 = nets["tvram1"]
    tvram10 = nets["tvram10"]
    tvram11 = nets["tvram11"]
    tvram12 = nets["tvram12"]
    tvram13 = nets["tvram13"]
    tvram14 = nets["tvram14"]
    tvram15 = nets["tvram15"]
    tvram16 = nets["tvram16"]
    tvram17 = nets["tvram17"]
    tvram18 = nets["tvram18"]
    tvram19 = nets["tvram19"]
    tvram2 = nets["tvram2"]
    tvram20 = nets["tvram20"]
    tvram21 = nets["tvram21"]
    tvram22 = nets["tvram22"]
    tvram23 = nets["tvram23"]
    tvram24 = nets["tvram24"]
    tvram25 = nets["tvram25"]
    tvram26 = nets["tvram26"]
    tvram27 = nets["tvram27"]
    tvram28 = nets["tvram28"]
    tvram29 = nets["tvram29"]
    tvram3 = nets["tvram3"]
    tvram30 = nets["tvram30"]
    tvram31 = nets["tvram31"]
    tvram4 = nets["tvram4"]
    tvram5 = nets["tvram5"]
    tvram6 = nets["tvram6"]
    tvram7 = nets["tvram7"]
    tvram8 = nets["tvram8"]
    tvram9 = nets["tvram9"]
    write_ram = nets["write_ram"]
    x_clk = nets["x_clk"]
    x_data = nets["x_data"]
    x_done = nets["x_done"]
    x_prog = nets["x_prog"]
    gnd = nets["gnd"]
    u22 = Part(
        refs.get("U22", "U22"),
        "video_schlib:XC4003-VQ100",
        footprint="footprints:TQFP-100_14x14mm_P0.5mm",
        value="XC4003-VQ100",
        name="U22",
    )
    u3 = Part(
        refs.get("U3", "U3"),
        "video_schlib:74LS245_1",
        footprint="footprints:SOIC-20W_7.5x12.8mm_P1.27mm",
        value="74LS245",
        name="U3",
    )
    u4 = Part(
        refs.get("U4", "U4"),
        "video_schlib:74LS245_2",
        footprint="footprints:SOIC-20W_7.5x12.8mm_P1.27mm",
        footprint_definition="footprints:SOIC-20W_7.5x12.8mm_P1.27mm_2",
        value="74LS245",
        name="U4",
    )
    u5 = Part(
        refs.get("U5", "U5"),
        "video_schlib:74LS245",
        footprint="footprints:SOIC-20W_7.5x12.8mm_P1.27mm",
        footprint_definition="footprints:SOIC-20W_7.5x12.8mm_P1.27mm_2",
        value="74LS245",
        name="U5",
    )
    u6 = Part(
        refs.get("U6", "U6"),
        "video_schlib:74LS245_3",
        footprint="footprints:SOIC-20W_7.5x12.8mm_P1.27mm",
        footprint_definition="footprints:SOIC-20W_7.5x12.8mm_P1.27mm_3",
        value="74LS245",
        name="U6",
    )
    module.add(u3, u4, u5, u6, u22)
    connect(
        net_5v,
        u22["100"],
        u22["12"],
        u22["22"],
        u22["24"],
        u22["25"],
        u22["26"],
        u22["37"],
        u22["51"],
        u22["63"],
        u22["75"],
        u22["89"],
        u3["20"],
        u4["20"],
        u5["20"],
        u6["20"],
    )
    connect(acces_ram, u22["21"], u3["19"], u4["19"], u5["19"], u6["19"])
    connect(acq_on, u22["13"])
    connect(blank, u22["8"])
    connect(clamp, u22["7"])
    connect(clkcad, u22["2"])
    connect(clkcda, u22["79"])
    connect(csync_out, u22["9"])
    connect(dq0, u3["2"])
    connect(dq1, u3["3"])
    connect(dq10, u4["4"])
    connect(dq11, u4["5"])
    connect(dq12, u4["6"])
    connect(dq13, u4["7"])
    connect(dq14, u4["8"])
    connect(dq15, u4["9"])
    connect(dq16, u5["2"])
    connect(dq17, u5["3"])
    connect(dq18, u5["4"])
    connect(dq19, u5["5"])
    connect(dq2, u3["4"])
    connect(dq20, u5["6"])
    connect(dq21, u5["7"])
    connect(dq22, u5["8"])
    connect(dq23, u5["9"])
    connect(dq24, u6["2"])
    connect(dq25, u6["3"])
    connect(dq26, u6["4"])
    connect(dq27, u6["5"])
    connect(dq28, u6["6"])
    connect(dq29, u6["7"])
    connect(dq3, u3["5"])
    connect(dq30, u6["8"])
    connect(dq31, u6["9"])
    connect(dq4, u3["6"])
    connect(dq5, u3["7"])
    connect(dq6, u3["8"])
    connect(dq7, u3["9"])
    connect(dq8, u4["2"])
    connect(dq9, u4["3"])
    connect(tvb0, u22["92"])
    connect(tvb1, u22["93"])
    connect(tvb2, u22["94"])
    connect(tvb3, u22["95"])
    connect(tvb4, u22["96"])
    connect(tvb5, u22["97"])
    connect(tvb6, u22["98"])
    connect(tvb7, u22["99"])
    connect(tvg0, u22["67"])
    connect(tvg1, u22["68"])
    connect(tvg2, u22["69"])
    connect(tvg3, u22["70"])
    connect(tvg4, u22["71"])
    connect(tvg5, u22["78"])
    connect(tvg6, u22["80"])
    connect(tvg7, u22["81"])
    connect(tvr0, u22["82"])
    connect(tvr1, u22["83"])
    connect(tvr2, u22["84"])
    connect(tvr3, u22["85"])
    connect(tvr4, u22["86"])
    connect(tvr5, u22["87"])
    connect(tvr6, u22["90"])
    connect(tvr7, u22["91"])
    connect(tvram0, u22["17"], u3["18"])
    connect(tvram1, u22["19"], u3["17"])
    connect(tvram10, u22["35"], u4["16"])
    connect(tvram11, u22["36"], u4["15"])
    connect(tvram12, u22["39"], u4["14"])
    connect(tvram13, u22["40"], u4["13"])
    connect(tvram14, u22["41"], u4["12"])
    connect(tvram15, u22["42"], u4["11"])
    connect(tvram16, u22["43"], u5["18"])
    connect(tvram17, u22["44"], u5["17"])
    connect(tvram18, u22["45"], u5["16"])
    connect(tvram19, u22["46"], u5["15"])
    connect(tvram2, u22["20"], u3["16"])
    connect(tvram20, u22["47"], u5["14"])
    connect(tvram21, u22["48"], u5["13"])
    connect(tvram22, u22["53"], u5["12"])
    connect(tvram23, u22["54"], u5["11"])
    connect(tvram24, u22["55"], u6["18"])
    connect(tvram25, u22["56"], u6["17"])
    connect(tvram26, u22["57"], u6["16"])
    connect(tvram27, u22["58"], u6["15"])
    connect(tvram28, u22["59"], u6["14"])
    connect(tvram29, u22["60"], u6["13"])
    connect(tvram3, u22["18"], u3["15"])
    connect(tvram30, u22["61"], u6["12"])
    connect(tvram31, u22["62"], u6["11"])
    connect(tvram4, u22["28"], u3["14"])
    connect(tvram5, u22["29"], u3["13"])
    connect(tvram6, u22["31"], u3["12"])
    connect(tvram7, u22["32"], u3["11"])
    connect(tvram8, u22["33"], u4["18"])
    connect(tvram9, u22["34"], u4["17"])
    connect(write_ram, u3["1"], u4["1"], u5["1"], u6["1"])
    connect(x_clk, u22["74"])
    connect(x_data, u22["72"])
    connect(x_done, u22["50"])
    connect(x_prog, u22["52"])
    connect(
        gnd,
        u22["1"],
        u22["11"],
        u22["23"],
        u22["38"],
        u22["49"],
        u22["64"],
        u22["77"],
        u22["88"],
        u3["10"],
        u4["10"],
        u5["10"],
        u6["10"],
    )
    u22.place(mm("204.927"), mm("-25.578"), rot=-90)
    u3.place(mm("68.783"), mm("6.553"), side="bottom")
    u4.place(mm("68.783"), mm("-8.433"), side="bottom")
    u5.place(mm("68.783"), mm("21.031"), side="bottom")
    u6.place(mm("97.739"), mm("38.811"))
    return module
