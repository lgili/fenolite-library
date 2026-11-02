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
    cas0 = nets["cas0"]
    cas1 = nets["cas1"]
    cas2 = nets["cas2"]
    cas3 = nets["cas3"]
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
    ras0 = nets["ras0"]
    ras1 = nets["ras1"]
    ras2 = nets["ras2"]
    ras3 = nets["ras3"]
    ras4 = nets["ras4"]
    ras5 = nets["ras5"]
    ras6 = nets["ras6"]
    ras7 = nets["ras7"]
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
    wram = nets["wram"]
    gnd = nets["gnd"]
    u12 = Part(
        refs.get("U12", "U12"),
        "video_schlib:SIM4X32_4",
        footprint="footprints:sim72",
        value="SIM4X32",
        name="U12",
    )
    u13 = Part(
        refs.get("U13", "U13"),
        "video_schlib:SIM4X32_1",
        footprint="footprints:sim72",
        footprint_definition="footprints:sim72_2",
        value="SIM4X32",
        name="U13",
    )
    u14 = Part(
        refs.get("U14", "U14"),
        "video_schlib:SIM4X32_2",
        footprint="footprints:sim72",
        footprint_definition="footprints:sim72_3",
        value="SIM4X32",
        name="U14",
    )
    u15 = Part(
        refs.get("U15", "U15"),
        "video_schlib:SIM4X32",
        footprint="footprints:sim72",
        value="SIM4X32",
        name="U15",
    )
    u16 = Part(
        refs.get("U16", "U16"),
        "video_schlib:SIM4X32_3",
        footprint="footprints:sim72",
        value="SIM4X32",
        name="U16",
    )
    u17 = Part(
        refs.get("U17", "U17"),
        "video_schlib:SIM4X32_7",
        footprint="footprints:sim72",
        value="SIM4X32",
        name="U17",
    )
    u18 = Part(
        refs.get("U18", "U18"),
        "video_schlib:SIM4X32_5",
        footprint="footprints:sim72",
        value="SIM4X32",
        name="U18",
    )
    u19 = Part(
        refs.get("U19", "U19"),
        "video_schlib:SIM4X32_6",
        footprint="footprints:sim72",
        value="SIM4X32",
        name="U19",
    )
    module.add(u12, u13, u14, u15, u16, u17, u18, u19)
    connect(
        net_5v,
        u12["10"],
        u12["30"],
        u12["59"],
        u13["10"],
        u13["30"],
        u13["59"],
        u14["10"],
        u14["30"],
        u14["59"],
        u15["10"],
        u15["30"],
        u15["59"],
        u16["10"],
        u16["30"],
        u16["59"],
        u17["10"],
        u17["30"],
        u17["59"],
        u18["10"],
        u18["30"],
        u18["59"],
        u19["10"],
        u19["30"],
        u19["59"],
    )
    connect(cas0, u12["40"], u13["40"], u14["40"], u15["40"], u16["40"], u17["40"], u18["40"], u19["40"])
    connect(cas1, u12["41"], u13["41"], u14["41"], u15["41"], u16["41"], u17["41"], u18["41"], u19["41"])
    connect(cas2, u12["42"], u13["42"], u14["42"], u15["42"], u16["42"], u17["42"], u18["42"], u19["42"])
    connect(cas3, u12["43"], u13["43"], u14["43"], u15["43"], u16["43"], u17["43"], u18["43"], u19["43"])
    connect(mxa0, u12["12"], u13["12"], u14["12"], u15["12"], u16["12"], u17["12"], u18["12"], u19["12"])
    connect(mxa1, u12["13"], u13["13"], u14["13"], u15["13"], u16["13"], u17["13"], u18["13"], u19["13"])
    connect(mxa10, u12["19"], u13["19"], u14["19"], u15["19"], u16["19"], u17["19"], u18["19"], u19["19"])
    connect(mxa2, u12["14"], u13["14"], u14["14"], u15["14"], u16["14"], u17["14"], u18["14"], u19["14"])
    connect(mxa3, u12["15"], u13["15"], u14["15"], u15["15"], u16["15"], u17["15"], u18["15"], u19["15"])
    connect(mxa4, u12["16"], u13["16"], u14["16"], u15["16"], u16["16"], u17["16"], u18["16"], u19["16"])
    connect(mxa5, u12["17"], u13["17"], u14["17"], u15["17"], u16["17"], u17["17"], u18["17"], u19["17"])
    connect(mxa6, u12["18"], u13["18"], u14["18"], u15["18"], u16["18"], u17["18"], u18["18"], u19["18"])
    connect(mxa7, u12["28"], u13["28"], u14["28"], u15["28"], u16["28"], u17["28"], u18["28"], u19["28"])
    connect(mxa8, u12["31"], u13["31"], u14["31"], u15["31"], u16["31"], u17["31"], u18["31"], u19["31"])
    connect(mxa9, u12["32"], u13["32"], u14["32"], u15["32"], u16["32"], u17["32"], u18["32"], u19["32"])
    connect(ras0, u19["34"], u19["44"])
    connect(ras1, u18["34"], u18["44"])
    connect(ras2, u17["34"], u17["44"])
    connect(ras3, u15["34"], u15["44"])
    connect(ras4, u16["34"], u16["44"])
    connect(ras5, u12["34"], u12["44"])
    connect(ras6, u14["34"], u14["44"])
    connect(ras7, u13["34"], u13["44"])
    connect(tvram0, u12["2"], u13["2"], u14["2"], u15["2"], u16["2"], u17["2"], u18["2"], u19["2"])
    connect(tvram1, u12["4"], u13["4"], u14["4"], u15["4"], u16["4"], u17["4"], u18["4"], u19["4"])
    connect(tvram10, u12["53"], u13["53"], u14["53"], u15["53"], u16["53"], u17["53"], u18["53"], u19["53"])
    connect(tvram11, u12["55"], u13["55"], u14["55"], u15["55"], u16["55"], u17["55"], u18["55"], u19["55"])
    connect(tvram12, u12["57"], u13["57"], u14["57"], u15["57"], u16["57"], u17["57"], u18["57"], u19["57"])
    connect(tvram13, u12["61"], u13["61"], u14["61"], u15["61"], u16["61"], u17["61"], u18["61"], u19["61"])
    connect(tvram14, u12["63"], u13["63"], u14["63"], u15["63"], u16["63"], u17["63"], u18["63"], u19["63"])
    connect(tvram15, u12["65"], u13["65"], u14["65"], u15["65"], u16["65"], u17["65"], u18["65"], u19["65"])
    connect(tvram16, u12["3"], u13["3"], u14["3"], u15["3"], u16["3"], u17["3"], u18["3"], u19["3"])
    connect(tvram17, u12["5"], u13["5"], u14["5"], u15["5"], u16["5"], u17["5"], u18["5"], u19["5"])
    connect(tvram18, u12["7"], u13["7"], u14["7"], u15["7"], u16["7"], u17["7"], u18["7"], u19["7"])
    connect(tvram19, u12["9"], u13["9"], u14["9"], u15["9"], u16["9"], u17["9"], u18["9"], u19["9"])
    connect(tvram2, u12["6"], u13["6"], u14["6"], u15["6"], u16["6"], u17["6"], u18["6"], u19["6"])
    connect(tvram20, u12["21"], u13["21"], u14["21"], u15["21"], u16["21"], u17["21"], u18["21"], u19["21"])
    connect(tvram21, u12["23"], u13["23"], u14["23"], u15["23"], u16["23"], u17["23"], u18["23"], u19["23"])
    connect(tvram22, u12["25"], u13["25"], u14["25"], u15["25"], u16["25"], u17["25"], u18["25"], u19["25"])
    connect(tvram23, u12["27"], u13["27"], u14["27"], u15["27"], u16["27"], u17["27"], u18["27"], u19["27"])
    connect(tvram24, u12["50"], u13["50"], u14["50"], u15["50"], u16["50"], u17["50"], u18["50"], u19["50"])
    connect(tvram25, u12["52"], u13["52"], u14["52"], u15["52"], u16["52"], u17["52"], u18["52"], u19["52"])
    connect(tvram26, u12["54"], u13["54"], u14["54"], u15["54"], u16["54"], u17["54"], u18["54"], u19["54"])
    connect(tvram27, u12["56"], u13["56"], u14["56"], u15["56"], u16["56"], u17["56"], u18["56"], u19["56"])
    connect(tvram28, u12["58"], u13["58"], u14["58"], u15["58"], u16["58"], u17["58"], u18["58"], u19["58"])
    connect(tvram29, u12["60"], u13["60"], u14["60"], u15["60"], u16["60"], u17["60"], u18["60"], u19["60"])
    connect(tvram3, u12["8"], u13["8"], u14["8"], u15["8"], u16["8"], u17["8"], u18["8"], u19["8"])
    connect(tvram30, u12["62"], u13["62"], u14["62"], u15["62"], u16["62"], u17["62"], u18["62"], u19["62"])
    connect(tvram31, u12["64"], u13["64"], u14["64"], u15["64"], u16["64"], u17["64"], u18["64"], u19["64"])
    connect(tvram4, u12["20"], u13["20"], u14["20"], u15["20"], u16["20"], u17["20"], u18["20"], u19["20"])
    connect(tvram5, u12["22"], u13["22"], u14["22"], u15["22"], u16["22"], u17["22"], u18["22"], u19["22"])
    connect(tvram6, u12["24"], u13["24"], u14["24"], u15["24"], u16["24"], u17["24"], u18["24"], u19["24"])
    connect(tvram7, u12["26"], u13["26"], u14["26"], u15["26"], u16["26"], u17["26"], u18["26"], u19["26"])
    connect(tvram8, u12["49"], u13["49"], u14["49"], u15["49"], u16["49"], u17["49"], u18["49"], u19["49"])
    connect(tvram9, u12["51"], u13["51"], u14["51"], u15["51"], u16["51"], u17["51"], u18["51"], u19["51"])
    connect(wram, u12["47"], u13["47"], u14["47"], u15["47"], u16["47"], u17["47"], u18["47"], u19["47"])
    connect(
        gnd,
        u12["1"],
        u12["39"],
        u12["72"],
        u13["1"],
        u13["39"],
        u13["72"],
        u14["1"],
        u14["39"],
        u14["72"],
        u15["1"],
        u15["39"],
        u15["72"],
        u16["1"],
        u16["39"],
        u16["72"],
        u17["1"],
        u17["39"],
        u17["72"],
        u18["1"],
        u18["39"],
        u18["72"],
        u19["1"],
        u19["39"],
        u19["72"],
    )
    u12.place(mm("134.315"), mm("8.585"))
    u13.place(mm("134.315"), mm("26.365"))
    u14.place(mm("134.315"), mm("17.475"))
    u15.place(mm("134.315"), mm("-9.195"))
    u16.place(mm("134.315"), mm("-0.305"))
    u17.place(mm("134.315"), mm("-18.085"))
    u18.place(mm("134.315"), mm("-26.975"))
    u19.place(mm("134.315"), mm("-35.865"))
    return module
