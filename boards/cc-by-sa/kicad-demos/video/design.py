# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileCopyrightText: NOASSERTION
# Converted from https://gitlab.com/kicad/code/kicad/-/tree/97acc80c223d75520c03fc44cab63cd9a3202c42/demos/video@97acc80c223d75520c03fc44cab63cd9a3202c42 by Fenolite 0.7.0.dev0 on 2026-10-31;
# modified: format conversion to the Fenolite DSL.

import copper
from sheets import bus_pci as _sheet_bus_pci
from sheets import esvideo as _sheet_esvideo
from sheets import graphic as _sheet_graphic
from sheets import modul as _sheet_modul
from sheets import muxdata as _sheet_muxdata
from sheets import pal_ntsc as _sheet_pal_ntsc
from sheets import rams as _sheet_rams
from fenolite.dsl import Design, Net, Part, connect, mm, stack

design = Design("video")

design.board(
    outline=(
        (mm("-46.406"), mm("-43.485")),
        (mm("124.155"), mm("-43.485")),
        (mm("265.633"), mm("-43.485")),
        (mm("265.633"), mm("34.366")),
        (mm("260.553"), mm("34.366")),
        (mm("190.957"), mm("34.366")),
        (mm("116.027"), mm("34.366")),
        (mm("104.851"), mm("34.366")),
        (mm("104.851"), mm("45.542")),
        (mm("94.818"), mm("45.542")),
        (mm("85.42"), mm("54.94")),
        (mm("73.609"), mm("54.94")),
        (mm("73.609"), mm("63.195")),
        (mm("59.004"), mm("63.195")),
        (mm("59.004"), mm("54.94")),
        (mm("57.226"), mm("54.94")),
        (mm("57.226"), mm("63.195")),
        (mm("-5.639"), mm("63.195")),
        (mm("-5.639"), mm("54.94")),
        (mm("-31.42"), mm("54.94")),
        (mm("-31.42"), mm("63.195")),
        (mm("-46.406"), mm("63.195")),
    ),
    copper=4,
    outline_width=mm("0.2032"),
)
design.stackup(
    stack.silkscreen(color="White"),
    stack.mask(mm("0.01"), color="Green"),
    stack.copper(mm("0.035")),
    stack.core(mm("0.480066"), material="FR4", epsilon_r="4.5", loss_tangent="0.02"),
    stack.copper(mm("0.035")),
    stack.prepreg(mm("0.480066"), material="FR4", epsilon_r="4.5", loss_tangent="0.02"),
    stack.copper(mm("0.035")),
    stack.core(mm("0.480066"), material="FR4", epsilon_r="4.5", loss_tangent="0.02"),
    stack.copper(mm("0.035")),
    stack.mask(mm("0.01"), color="Green"),
    stack.silkscreen(color="White"),
    finish="HAL lead-free",
)
design.title_block(title="KiCad demo", date="2015-10-14", revision="1.A")

net_5v = Net("+5V")
pcrd = Net("//PCRD")
pcwr = Net("//PCWR")
acces_ram = Net("/ACCES_RAM-")
acq_on = Net("/ACQ_ON")
adr2 = Net("/ADR2")
adr3 = Net("/ADR3")
adr4 = Net("/ADR4")
adr5 = Net("/ADR5")
adr6 = Net("/ADR6")
be_0 = Net("/BE-0")
be_1 = Net("/BE-1")
be_2 = Net("/BE-2")
be_3 = Net("/BE-3")
blank = Net("/BLANK-")
blue_in = Net("/BLUE_IN")
blue_out = Net("/BLUE_OUT")
bpclk = Net("/BPCLK")
bt812_rd = Net("/BT812_RD-")
bt812_wr = Net("/BT812_WR-")
cas0 = Net("/CAS0-")
cas1 = Net("/CAS1-")
cas2 = Net("/CAS2-")
cas3 = Net("/CAS3-")
clamp = Net("/CLAMP")
clkcad = Net("/CLKCAD")
clkcda = Net("/CLKCDA")
csync_out = Net("/CSYNC-OUT")
csyncin = Net("/CSYNCIN-")
c_out = Net("/C_OUT")
dq0 = Net("/DQ0")
dq1 = Net("/DQ1")
dq10 = Net("/DQ10")
dq11 = Net("/DQ11")
dq12 = Net("/DQ12")
dq13 = Net("/DQ13")
dq14 = Net("/DQ14")
dq15 = Net("/DQ15")
dq16 = Net("/DQ16")
dq17 = Net("/DQ17")
dq18 = Net("/DQ18")
dq19 = Net("/DQ19")
dq2 = Net("/DQ2")
dq20 = Net("/DQ20")
dq21 = Net("/DQ21")
dq22 = Net("/DQ22")
dq23 = Net("/DQ23")
dq24 = Net("/DQ24")
dq25 = Net("/DQ25")
dq26 = Net("/DQ26")
dq27 = Net("/DQ27")
dq28 = Net("/DQ28")
dq29 = Net("/DQ29")
dq3 = Net("/DQ3")
dq30 = Net("/DQ30")
dq31 = Net("/DQ31")
dq4 = Net("/DQ4")
dq5 = Net("/DQ5")
dq6 = Net("/DQ6")
dq7 = Net("/DQ7")
dq8 = Net("/DQ8")
dq9 = Net("/DQ9")
f_palin = Net("/F_PALIN")
green_in = Net("/GREEN_IN")
green_out = Net("/GREEN_OUT")
hd_pal = Net("/HD_PAL-")
irq = Net("/IRQ-")
irq_srl = Net("/IRQ_SRL")
mxa0 = Net("/MXA0")
mxa1 = Net("/MXA1")
mxa10 = Net("/MXA10")
mxa2 = Net("/MXA2")
mxa3 = Net("/MXA3")
mxa4 = Net("/MXA4")
mxa5 = Net("/MXA5")
mxa6 = Net("/MXA6")
mxa7 = Net("/MXA7")
mxa8 = Net("/MXA8")
mxa9 = Net("/MXA9")
oe_pal = Net("/OE_PAL-")
pca0 = Net("/PCA0")
pca1 = Net("/PCA1")
pca2 = Net("/PCA2")
ptadr = Net("/PTADR-")
ptatn = Net("/PTATN-")
ptbe_0 = Net("/PTBE-0")
ptbe_1 = Net("/PTBE-1")
ptbe_2 = Net("/PTBE-2")
ptbe_3 = Net("/PTBE-3")
ptburst = Net("/PTBURST")
ptnum0 = Net("/PTNUM0")
ptnum1 = Net("/PTNUM1")
ptrdy = Net("/PTRDY-")
ptwr = Net("/PTWR")
ras0 = Net("/RAS0-")
ras1 = Net("/RAS1-")
ras2 = Net("/RAS2-")
ras3 = Net("/RAS3-")
ras4 = Net("/RAS4-")
ras5 = Net("/RAS5-")
ras6 = Net("/RAS6-")
ras7 = Net("/RAS7-")
rdcad = Net("/RDCAD-")
rdcda = Net("/RDCDA-")
rdempty = Net("/RDEMPTY")
rdfifo = Net("/RDFIFO-")
red_in = Net("/RED_IN")
red_out = Net("/RED_OUT")
select = Net("/SELECT-")
sysrst = Net("/SYSRST-")
tvb0 = Net("/TVB0")
tvb1 = Net("/TVB1")
tvb2 = Net("/TVB2")
tvb3 = Net("/TVB3")
tvb4 = Net("/TVB4")
tvb5 = Net("/TVB5")
tvb6 = Net("/TVB6")
tvb7 = Net("/TVB7")
tvg0 = Net("/TVG0")
tvg1 = Net("/TVG1")
tvg2 = Net("/TVG2")
tvg3 = Net("/TVG3")
tvg4 = Net("/TVG4")
tvg5 = Net("/TVG5")
tvg6 = Net("/TVG6")
tvg7 = Net("/TVG7")
tvi0 = Net("/TVI0")
tvi1 = Net("/TVI1")
tvr0 = Net("/TVR0")
tvr1 = Net("/TVR1")
tvr2 = Net("/TVR2")
tvr3 = Net("/TVR3")
tvr4 = Net("/TVR4")
tvr5 = Net("/TVR5")
tvr6 = Net("/TVR6")
tvr7 = Net("/TVR7")
tvram0 = Net("/TVRAM0")
tvram1 = Net("/TVRAM1")
tvram10 = Net("/TVRAM10")
tvram11 = Net("/TVRAM11")
tvram12 = Net("/TVRAM12")
tvram13 = Net("/TVRAM13")
tvram14 = Net("/TVRAM14")
tvram15 = Net("/TVRAM15")
tvram16 = Net("/TVRAM16")
tvram17 = Net("/TVRAM17")
tvram18 = Net("/TVRAM18")
tvram19 = Net("/TVRAM19")
tvram2 = Net("/TVRAM2")
tvram20 = Net("/TVRAM20")
tvram21 = Net("/TVRAM21")
tvram22 = Net("/TVRAM22")
tvram23 = Net("/TVRAM23")
tvram24 = Net("/TVRAM24")
tvram25 = Net("/TVRAM25")
tvram26 = Net("/TVRAM26")
tvram27 = Net("/TVRAM27")
tvram28 = Net("/TVRAM28")
tvram29 = Net("/TVRAM29")
tvram3 = Net("/TVRAM3")
tvram30 = Net("/TVRAM30")
tvram31 = Net("/TVRAM31")
tvram4 = Net("/TVRAM4")
tvram5 = Net("/TVRAM5")
tvram6 = Net("/TVRAM6")
tvram7 = Net("/TVRAM7")
tvram8 = Net("/TVRAM8")
tvram9 = Net("/TVRAM9")
vd_pal = Net("/VD_PAL-")
wram = Net("/WRAM-")
wrcad = Net("/WRCAD-")
wrcda = Net("/WRCDA-")
wrfifdo = Net("/WRFIFDO-")
wrfull = Net("/WRFULL")
write_ram = Net("/WRITE_RAM")
x_clk = Net("/X_CLK")
x_data = Net("/X_DATA")
x_done = Net("/X_DONE")
x_irq = Net("/X_IRQ")
x_prog = Net("/X_PROG-")
y_out = Net("/Y_OUT")
modul_cvbsout = Net("/modul/CVBSOUT")
gnd = Net("GND")

j4 = Part(
    "J4",
    "video_schlib:DB9",
    footprint="footprints:DSUB-9_Female_Horizontal_P2.77x2.84mm_EdgePinOffset14.56mm_Housed_MountingHolesOffset15.98mm",
    value="DB9FEM",
)
p1 = Part("P1", "video_schlib:BNC", footprint="footprints:subclick", value="BNC")
p2 = Part(
    "P2",
    "video_schlib:BNC",
    footprint="footprints:subclick",
    footprint_definition="footprints:subclick_2",
    value="BNC",
)
p3 = Part(
    "P3",
    "video_schlib:BNC",
    footprint="footprints:subclick",
    footprint_definition="footprints:subclick_3",
    value="BNC",
)
p8 = Part(
    "P8",
    "video_schlib:BNC",
    footprint="footprints:subclick",
    footprint_definition="footprints:subclick_4",
    value="BNC",
)

design.add(j4, p1, p2, p3, p8)
_sheet_bus_pci.sheet(
    design,
    path="buspci_sch",
    refs={
        "BUS1": "BUS1",
        "C24": "C24",
        "C25": "C25",
        "C26": "C26",
        "C27": "C27",
        "C28": "C28",
        "C29": "C29",
        "C30": "C30",
        "C31": "C31",
        "C38": "C38",
        "C67": "C67",
        "C68": "C68",
        "C69": "C69",
        "R28": "R28",
        "R29": "R29",
        "R5": "R5",
        "R6": "R6",
        "R7": "R7",
        "RR1": "RR1",
        "RR2": "RR2",
        "RR3": "RR3",
        "RR4": "RR4",
        "RR5": "RR5",
        "RR6": "RR6",
        "RR7": "RR7",
        "RR8": "RR8",
        "U1": "U1",
        "U11": "U11",
        "W1": "W1",
        "W2": "W2",
        "W3": "W3",
        "W4": "W4",
        "W5": "W5",
    },
    net_5v=net_5v,
    pcrd=pcrd,
    pcwr=pcwr,
    adr2=adr2,
    adr3=adr3,
    adr4=adr4,
    adr5=adr5,
    adr6=adr6,
    be_0=be_0,
    be_1=be_1,
    be_2=be_2,
    be_3=be_3,
    bpclk=bpclk,
    dq0=dq0,
    dq1=dq1,
    dq10=dq10,
    dq11=dq11,
    dq12=dq12,
    dq13=dq13,
    dq14=dq14,
    dq15=dq15,
    dq16=dq16,
    dq17=dq17,
    dq18=dq18,
    dq19=dq19,
    dq2=dq2,
    dq20=dq20,
    dq21=dq21,
    dq22=dq22,
    dq23=dq23,
    dq24=dq24,
    dq25=dq25,
    dq26=dq26,
    dq27=dq27,
    dq28=dq28,
    dq29=dq29,
    dq3=dq3,
    dq30=dq30,
    dq31=dq31,
    dq4=dq4,
    dq5=dq5,
    dq6=dq6,
    dq7=dq7,
    dq8=dq8,
    dq9=dq9,
    irq=irq,
    irq_srl=irq_srl,
    ptadr=ptadr,
    ptatn=ptatn,
    ptbe_0=ptbe_0,
    ptbe_1=ptbe_1,
    ptbe_2=ptbe_2,
    ptbe_3=ptbe_3,
    ptburst=ptburst,
    ptnum0=ptnum0,
    ptnum1=ptnum1,
    ptrdy=ptrdy,
    ptwr=ptwr,
    rdempty=rdempty,
    rdfifo=rdfifo,
    select=select,
    sysrst=sysrst,
    wrfifdo=wrfifdo,
    wrfull=wrfull,
    x_irq=x_irq,
    gnd=gnd,
)
_sheet_esvideo.sheet(
    design,
    path="esvideo_rvb",
    refs={
        "C32": "C32",
        "C33": "C33",
        "C34": "C34",
        "C35": "C35",
        "C36": "C36",
        "C37": "C37",
        "C39": "C39",
        "C40": "C40",
        "C41": "C41",
        "C42": "C42",
        "C51": "C51",
        "C52": "C52",
        "L5": "L5",
        "R15": "R15",
        "R22": "R22",
        "R23": "R23",
        "R24": "R24",
        "R36": "R36",
        "R37": "R37",
        "R38": "R38",
        "R42": "R42",
        "R43": "R43",
        "R44": "R44",
        "R45": "R45",
        "R46": "R46",
        "R47": "R47",
        "R8": "R8",
        "U8": "U8",
        "U9": "U9",
    },
    net_5v=net_5v,
    blank=blank,
    blue_in=blue_in,
    blue_out=blue_out,
    clamp=clamp,
    clkcad=clkcad,
    clkcda=clkcda,
    csync_out=csync_out,
    csyncin=csyncin,
    dq0=dq0,
    dq1=dq1,
    dq2=dq2,
    dq3=dq3,
    dq4=dq4,
    dq5=dq5,
    dq6=dq6,
    dq7=dq7,
    green_in=green_in,
    green_out=green_out,
    oe_pal=oe_pal,
    pca0=pca0,
    pca1=pca1,
    pca2=pca2,
    rdcad=rdcad,
    rdcda=rdcda,
    red_in=red_in,
    red_out=red_out,
    tvb0=tvb0,
    tvb1=tvb1,
    tvb2=tvb2,
    tvb3=tvb3,
    tvb4=tvb4,
    tvb5=tvb5,
    tvb6=tvb6,
    tvb7=tvb7,
    tvg0=tvg0,
    tvg1=tvg1,
    tvg2=tvg2,
    tvg3=tvg3,
    tvg4=tvg4,
    tvg5=tvg5,
    tvg6=tvg6,
    tvg7=tvg7,
    tvi0=tvi0,
    tvi1=tvi1,
    tvr0=tvr0,
    tvr1=tvr1,
    tvr2=tvr2,
    tvr3=tvr3,
    tvr4=tvr4,
    tvr5=tvr5,
    tvr6=tvr6,
    tvr7=tvr7,
    wrcad=wrcad,
    wrcda=wrcda,
    gnd=gnd,
)
_sheet_graphic.sheet(
    design,
    path="graphic",
    refs={
        "C17": "C17",
        "C18": "C18",
        "C19": "C19",
        "C20": "C20",
        "C21": "C21",
        "C22": "C22",
        "C23": "C23",
        "C49": "C49",
        "C50": "C50",
        "C56": "C56",
        "C57": "C57",
        "C63": "C63",
        "C70": "C70",
        "C71": "C71",
        "C72": "C72",
        "C73": "C73",
        "D6": "D6",
        "P10": "P10",
        "P11": "P11",
        "P12": "P12",
        "P4": "P4",
        "P5": "P5",
        "P9": "P9",
        "R1": "R1",
        "R13": "R13",
        "R21": "R21",
        "R26": "R26",
        "R48": "R48",
        "U2": "U2",
        "U21": "U21",
        "U23": "U23",
        "U24": "U24",
        "U7": "U7",
        "X1": "X1",
    },
    net_5v=net_5v,
    pcrd=pcrd,
    pcwr=pcwr,
    acces_ram=acces_ram,
    acq_on=acq_on,
    adr2=adr2,
    adr3=adr3,
    adr4=adr4,
    adr5=adr5,
    adr6=adr6,
    be_0=be_0,
    be_1=be_1,
    be_2=be_2,
    be_3=be_3,
    blank=blank,
    bpclk=bpclk,
    bt812_rd=bt812_rd,
    bt812_wr=bt812_wr,
    cas0=cas0,
    cas1=cas1,
    cas2=cas2,
    cas3=cas3,
    clamp=clamp,
    clkcad=clkcad,
    clkcda=clkcda,
    csync_out=csync_out,
    csyncin=csyncin,
    dq0=dq0,
    dq1=dq1,
    dq10=dq10,
    dq11=dq11,
    dq12=dq12,
    dq13=dq13,
    dq14=dq14,
    dq15=dq15,
    dq2=dq2,
    dq3=dq3,
    dq4=dq4,
    dq5=dq5,
    dq6=dq6,
    dq7=dq7,
    dq8=dq8,
    dq9=dq9,
    f_palin=f_palin,
    hd_pal=hd_pal,
    irq=irq,
    irq_srl=irq_srl,
    mxa0=mxa0,
    mxa1=mxa1,
    mxa10=mxa10,
    mxa2=mxa2,
    mxa3=mxa3,
    mxa4=mxa4,
    mxa5=mxa5,
    mxa6=mxa6,
    mxa7=mxa7,
    mxa8=mxa8,
    mxa9=mxa9,
    pca0=pca0,
    pca1=pca1,
    pca2=pca2,
    ptadr=ptadr,
    ptatn=ptatn,
    ptbe_0=ptbe_0,
    ptbe_1=ptbe_1,
    ptbe_2=ptbe_2,
    ptbe_3=ptbe_3,
    ptburst=ptburst,
    ptnum0=ptnum0,
    ptnum1=ptnum1,
    ptrdy=ptrdy,
    ptwr=ptwr,
    ras0=ras0,
    ras1=ras1,
    ras2=ras2,
    ras3=ras3,
    ras4=ras4,
    ras5=ras5,
    ras6=ras6,
    ras7=ras7,
    rdcad=rdcad,
    rdcda=rdcda,
    rdempty=rdempty,
    rdfifo=rdfifo,
    select=select,
    sysrst=sysrst,
    tvi0=tvi0,
    tvi1=tvi1,
    vd_pal=vd_pal,
    wram=wram,
    wrcad=wrcad,
    wrcda=wrcda,
    wrfifdo=wrfifdo,
    wrfull=wrfull,
    write_ram=write_ram,
    x_clk=x_clk,
    x_data=x_data,
    x_done=x_done,
    x_irq=x_irq,
    x_prog=x_prog,
    gnd=gnd,
)
_sheet_modul.sheet(
    design,
    path="modul",
    refs={
        "C43": "C43",
        "C44": "C44",
        "C45": "C45",
        "C46": "C46",
        "C48": "C48",
        "C53": "C53",
        "C54": "C54",
        "C55": "C55",
        "C58": "C58",
        "C59": "C59",
        "C60": "C60",
        "C61": "C61",
        "C64": "C64",
        "CV1": "CV1",
        "L1": "L1",
        "L2": "L2",
        "L3": "L3",
        "L6": "L6",
        "POT1": "POT1",
        "Q1": "Q1",
        "Q2": "Q2",
        "Q3": "Q3",
        "R10": "R10",
        "R11": "R11",
        "R16": "R16",
        "R17": "R17",
        "R18": "R18",
        "R30": "R30",
        "R31": "R31",
        "R32": "R32",
        "R33": "R33",
        "R34": "R34",
        "R39": "R39",
        "R4": "R4",
        "R40": "R40",
        "R41": "R41",
        "R9": "R9",
        "U20": "U20",
        "X3": "X3",
    },
    net_5v=net_5v,
    blue_out=blue_out,
    csync_out=csync_out,
    c_out=c_out,
    green_out=green_out,
    red_out=red_out,
    y_out=y_out,
    modul_cvbsout=modul_cvbsout,
    gnd=gnd,
)
_sheet_muxdata.sheet(
    design,
    path="muxdata",
    refs={"U22": "U22", "U3": "U3", "U4": "U4", "U5": "U5", "U6": "U6"},
    net_5v=net_5v,
    acces_ram=acces_ram,
    acq_on=acq_on,
    blank=blank,
    clamp=clamp,
    clkcad=clkcad,
    clkcda=clkcda,
    csync_out=csync_out,
    dq0=dq0,
    dq1=dq1,
    dq10=dq10,
    dq11=dq11,
    dq12=dq12,
    dq13=dq13,
    dq14=dq14,
    dq15=dq15,
    dq16=dq16,
    dq17=dq17,
    dq18=dq18,
    dq19=dq19,
    dq2=dq2,
    dq20=dq20,
    dq21=dq21,
    dq22=dq22,
    dq23=dq23,
    dq24=dq24,
    dq25=dq25,
    dq26=dq26,
    dq27=dq27,
    dq28=dq28,
    dq29=dq29,
    dq3=dq3,
    dq30=dq30,
    dq31=dq31,
    dq4=dq4,
    dq5=dq5,
    dq6=dq6,
    dq7=dq7,
    dq8=dq8,
    dq9=dq9,
    tvb0=tvb0,
    tvb1=tvb1,
    tvb2=tvb2,
    tvb3=tvb3,
    tvb4=tvb4,
    tvb5=tvb5,
    tvb6=tvb6,
    tvb7=tvb7,
    tvg0=tvg0,
    tvg1=tvg1,
    tvg2=tvg2,
    tvg3=tvg3,
    tvg4=tvg4,
    tvg5=tvg5,
    tvg6=tvg6,
    tvg7=tvg7,
    tvr0=tvr0,
    tvr1=tvr1,
    tvr2=tvr2,
    tvr3=tvr3,
    tvr4=tvr4,
    tvr5=tvr5,
    tvr6=tvr6,
    tvr7=tvr7,
    tvram0=tvram0,
    tvram1=tvram1,
    tvram10=tvram10,
    tvram11=tvram11,
    tvram12=tvram12,
    tvram13=tvram13,
    tvram14=tvram14,
    tvram15=tvram15,
    tvram16=tvram16,
    tvram17=tvram17,
    tvram18=tvram18,
    tvram19=tvram19,
    tvram2=tvram2,
    tvram20=tvram20,
    tvram21=tvram21,
    tvram22=tvram22,
    tvram23=tvram23,
    tvram24=tvram24,
    tvram25=tvram25,
    tvram26=tvram26,
    tvram27=tvram27,
    tvram28=tvram28,
    tvram29=tvram29,
    tvram3=tvram3,
    tvram30=tvram30,
    tvram31=tvram31,
    tvram4=tvram4,
    tvram5=tvram5,
    tvram6=tvram6,
    tvram7=tvram7,
    tvram8=tvram8,
    tvram9=tvram9,
    write_ram=write_ram,
    x_clk=x_clk,
    x_data=x_data,
    x_done=x_done,
    x_prog=x_prog,
    gnd=gnd,
)
_sheet_pal_ntsc.sheet(
    design,
    path="pal_ntsc_sch",
    refs={
        "C1": "C1",
        "C10": "C10",
        "C11": "C11",
        "C12": "C12",
        "C13": "C13",
        "C14": "C14",
        "C15": "C15",
        "C16": "C16",
        "C2": "C2",
        "C3": "C3",
        "C4": "C4",
        "C47": "C47",
        "C5": "C5",
        "C6": "C6",
        "C62": "C62",
        "C65": "C65",
        "C66": "C66",
        "C7": "C7",
        "C8": "C8",
        "C9": "C9",
        "D1": "D1",
        "D2": "D2",
        "D3": "D3",
        "D4": "D4",
        "L4": "L4",
        "R12": "R12",
        "R14": "R14",
        "R19": "R19",
        "R2": "R2",
        "R20": "R20",
        "R25": "R25",
        "R27": "R27",
        "R3": "R3",
        "R35": "R35",
        "U10": "U10",
        "X2": "X2",
    },
    net_5v=net_5v,
    bt812_rd=bt812_rd,
    bt812_wr=bt812_wr,
    dq0=dq0,
    dq1=dq1,
    dq2=dq2,
    dq3=dq3,
    dq4=dq4,
    dq5=dq5,
    dq6=dq6,
    dq7=dq7,
    f_palin=f_palin,
    green_in=green_in,
    hd_pal=hd_pal,
    oe_pal=oe_pal,
    pca0=pca0,
    pca1=pca1,
    red_in=red_in,
    sysrst=sysrst,
    tvb0=tvb0,
    tvb1=tvb1,
    tvb2=tvb2,
    tvb3=tvb3,
    tvb4=tvb4,
    tvb5=tvb5,
    tvb6=tvb6,
    tvb7=tvb7,
    tvg0=tvg0,
    tvg1=tvg1,
    tvg2=tvg2,
    tvg3=tvg3,
    tvg4=tvg4,
    tvg5=tvg5,
    tvg6=tvg6,
    tvg7=tvg7,
    tvr0=tvr0,
    tvr1=tvr1,
    tvr2=tvr2,
    tvr3=tvr3,
    tvr4=tvr4,
    tvr5=tvr5,
    tvr6=tvr6,
    tvr7=tvr7,
    vd_pal=vd_pal,
    gnd=gnd,
)
_sheet_rams.sheet(
    design,
    path="rams",
    refs={
        "U12": "U12",
        "U13": "U13",
        "U14": "U14",
        "U15": "U15",
        "U16": "U16",
        "U17": "U17",
        "U18": "U18",
        "U19": "U19",
    },
    net_5v=net_5v,
    cas0=cas0,
    cas1=cas1,
    cas2=cas2,
    cas3=cas3,
    mxa0=mxa0,
    mxa1=mxa1,
    mxa10=mxa10,
    mxa2=mxa2,
    mxa3=mxa3,
    mxa4=mxa4,
    mxa5=mxa5,
    mxa6=mxa6,
    mxa7=mxa7,
    mxa8=mxa8,
    mxa9=mxa9,
    ras0=ras0,
    ras1=ras1,
    ras2=ras2,
    ras3=ras3,
    ras4=ras4,
    ras5=ras5,
    ras6=ras6,
    ras7=ras7,
    tvram0=tvram0,
    tvram1=tvram1,
    tvram10=tvram10,
    tvram11=tvram11,
    tvram12=tvram12,
    tvram13=tvram13,
    tvram14=tvram14,
    tvram15=tvram15,
    tvram16=tvram16,
    tvram17=tvram17,
    tvram18=tvram18,
    tvram19=tvram19,
    tvram2=tvram2,
    tvram20=tvram20,
    tvram21=tvram21,
    tvram22=tvram22,
    tvram23=tvram23,
    tvram24=tvram24,
    tvram25=tvram25,
    tvram26=tvram26,
    tvram27=tvram27,
    tvram28=tvram28,
    tvram29=tvram29,
    tvram3=tvram3,
    tvram30=tvram30,
    tvram31=tvram31,
    tvram4=tvram4,
    tvram5=tvram5,
    tvram6=tvram6,
    tvram7=tvram7,
    tvram8=tvram8,
    tvram9=tvram9,
    wram=wram,
    gnd=gnd,
)

net_3_3v = design.nets["+3.3V"]
net_5f = design.nets["+5F"]
esvideo_rvb_oe_rvb = design.nets["/ESVIDEO-RVB/OE_RVB-"]
esvideo_rvb_ref = design.nets["/ESVIDEO-RVB/REF+"]
esvideo_rvb_vaa = design.nets["/ESVIDEO-RVB/VAA"]
buspci_sch_ea1 = design.nets["/buspci.sch/EA1"]
buspci_sch_ea10 = design.nets["/buspci.sch/EA10"]
buspci_sch_ea11 = design.nets["/buspci.sch/EA11"]
buspci_sch_ea12 = design.nets["/buspci.sch/EA12"]
buspci_sch_ea13 = design.nets["/buspci.sch/EA13"]
buspci_sch_ea14 = design.nets["/buspci.sch/EA14"]
buspci_sch_ea15 = design.nets["/buspci.sch/EA15"]
buspci_sch_ea2 = design.nets["/buspci.sch/EA2"]
buspci_sch_ea3 = design.nets["/buspci.sch/EA3"]
buspci_sch_ea4 = design.nets["/buspci.sch/EA4"]
buspci_sch_ea5 = design.nets["/buspci.sch/EA5"]
buspci_sch_ea6 = design.nets["/buspci.sch/EA6"]
buspci_sch_ea7 = design.nets["/buspci.sch/EA7"]
buspci_sch_ea9 = design.nets["/buspci.sch/EA9"]
buspci_sch_eq0 = design.nets["/buspci.sch/EQ0"]
buspci_sch_eq1 = design.nets["/buspci.sch/EQ1"]
buspci_sch_eq2 = design.nets["/buspci.sch/EQ2"]
buspci_sch_eq3 = design.nets["/buspci.sch/EQ3"]
buspci_sch_eq4 = design.nets["/buspci.sch/EQ4"]
buspci_sch_eq5 = design.nets["/buspci.sch/EQ5"]
buspci_sch_eq6 = design.nets["/buspci.sch/EQ6"]
buspci_sch_eq7 = design.nets["/buspci.sch/EQ7"]
buspci_sch_p_ad0 = design.nets["/buspci.sch/P_AD0"]
buspci_sch_p_ad1 = design.nets["/buspci.sch/P_AD1"]
buspci_sch_p_ad10 = design.nets["/buspci.sch/P_AD10"]
buspci_sch_p_ad11 = design.nets["/buspci.sch/P_AD11"]
buspci_sch_p_ad12 = design.nets["/buspci.sch/P_AD12"]
buspci_sch_p_ad13 = design.nets["/buspci.sch/P_AD13"]
buspci_sch_p_ad14 = design.nets["/buspci.sch/P_AD14"]
buspci_sch_p_ad15 = design.nets["/buspci.sch/P_AD15"]
buspci_sch_p_ad16 = design.nets["/buspci.sch/P_AD16"]
buspci_sch_p_ad17 = design.nets["/buspci.sch/P_AD17"]
buspci_sch_p_ad18 = design.nets["/buspci.sch/P_AD18"]
buspci_sch_p_ad19 = design.nets["/buspci.sch/P_AD19"]
buspci_sch_p_ad2 = design.nets["/buspci.sch/P_AD2"]
buspci_sch_p_ad20 = design.nets["/buspci.sch/P_AD20"]
buspci_sch_p_ad21 = design.nets["/buspci.sch/P_AD21"]
buspci_sch_p_ad22 = design.nets["/buspci.sch/P_AD22"]
buspci_sch_p_ad23 = design.nets["/buspci.sch/P_AD23"]
buspci_sch_p_ad24 = design.nets["/buspci.sch/P_AD24"]
buspci_sch_p_ad25 = design.nets["/buspci.sch/P_AD25"]
buspci_sch_p_ad26 = design.nets["/buspci.sch/P_AD26"]
buspci_sch_p_ad27 = design.nets["/buspci.sch/P_AD27"]
buspci_sch_p_ad28 = design.nets["/buspci.sch/P_AD28"]
buspci_sch_p_ad29 = design.nets["/buspci.sch/P_AD29"]
buspci_sch_p_ad3 = design.nets["/buspci.sch/P_AD3"]
buspci_sch_p_ad30 = design.nets["/buspci.sch/P_AD30"]
buspci_sch_p_ad31 = design.nets["/buspci.sch/P_AD31"]
buspci_sch_p_ad4 = design.nets["/buspci.sch/P_AD4"]
buspci_sch_p_ad5 = design.nets["/buspci.sch/P_AD5"]
buspci_sch_p_ad6 = design.nets["/buspci.sch/P_AD6"]
buspci_sch_p_ad7 = design.nets["/buspci.sch/P_AD7"]
buspci_sch_p_ad8 = design.nets["/buspci.sch/P_AD8"]
buspci_sch_p_ad9 = design.nets["/buspci.sch/P_AD9"]
buspci_sch_p_c_be0 = design.nets["/buspci.sch/P_C/BE0#"]
buspci_sch_p_c_be1 = design.nets["/buspci.sch/P_C/BE1#"]
buspci_sch_p_c_be2 = design.nets["/buspci.sch/P_C/BE2#"]
buspci_sch_p_c_be3 = design.nets["/buspci.sch/P_C/BE3#"]
buspci_sch_p_clk = design.nets["/buspci.sch/P_CLK"]
buspci_sch_p_devsel = design.nets["/buspci.sch/P_DEVSEL#"]
buspci_sch_p_frame = design.nets["/buspci.sch/P_FRAME#"]
buspci_sch_p_gnt = design.nets["/buspci.sch/P_GNT#"]
buspci_sch_p_idsel = design.nets["/buspci.sch/P_IDSEL"]
buspci_sch_p_inta = design.nets["/buspci.sch/P_INTA#"]
buspci_sch_p_irdy = design.nets["/buspci.sch/P_IRDY#"]
buspci_sch_p_lock = design.nets["/buspci.sch/P_LOCK#"]
buspci_sch_p_par = design.nets["/buspci.sch/P_PAR"]
buspci_sch_p_perr = design.nets["/buspci.sch/P_PERR#"]
buspci_sch_p_req = design.nets["/buspci.sch/P_REQ#"]
buspci_sch_p_rst = design.nets["/buspci.sch/P_RST#"]
buspci_sch_p_serr = design.nets["/buspci.sch/P_SERR#"]
buspci_sch_p_stop = design.nets["/buspci.sch/P_STOP#"]
buspci_sch_p_trdy = design.nets["/buspci.sch/P_TRDY#"]
graphic_14mhzout = design.nets["/graphic/14MHZOUT"]
graphic_cclk = design.nets["/graphic/CCLK"]
graphic_clk10mhz = design.nets["/graphic/CLK10MHz"]
graphic_csio = design.nets["/graphic/CSIO-"]
graphic_din = design.nets["/graphic/DIN"]
graphic_done = design.nets["/graphic/DONE"]
graphic_hdout = design.nets["/graphic/HDOUT"]
graphic_hdrefout = design.nets["/graphic/HDREFOUT"]
graphic_ia0 = design.nets["/graphic/IA0"]
graphic_ia1 = design.nets["/graphic/IA1"]
graphic_ia2 = design.nets["/graphic/IA2"]
graphic_ia3 = design.nets["/graphic/IA3"]
graphic_ia4 = design.nets["/graphic/IA4"]
graphic_ia5 = design.nets["/graphic/IA5"]
graphic_ia6 = design.nets["/graphic/IA6"]
graphic_ia7 = design.nets["/graphic/IA7"]
graphic_ia8 = design.nets["/graphic/IA8"]
graphic_ia9 = design.nets["/graphic/IA9"]
graphic_icas = design.nets["/graphic/ICAS-"]
graphic_id0 = design.nets["/graphic/ID0"]
graphic_id1 = design.nets["/graphic/ID1"]
graphic_id2 = design.nets["/graphic/ID2"]
graphic_id3 = design.nets["/graphic/ID3"]
graphic_ioe = design.nets["/graphic/IOE-"]
graphic_iras = design.nets["/graphic/IRAS-"]
graphic_iwr = design.nets["/graphic/IWR-"]
graphic_led = design.nets["/graphic/LED"]
graphic_prog = design.nets["/graphic/PROG*"]
graphic_reserv1 = design.nets["/graphic/RESERV1"]
graphic_vosc = design.nets["/graphic/VOSC"]
graphic_xtal_i = design.nets["/graphic/XTAL_I"]
graphic_x_din = design.nets["/graphic/X_DIN"]
modul_chrom = design.nets["/modul/CHROM"]
modul_cvbs = design.nets["/modul/CVBS"]
modul_lum = design.nets["/modul/LUM"]
pal_ntsc_sch_c_video = design.nets["/pal-ntsc.sch/C-VIDEO"]
pal_ntsc_sch_vaf = design.nets["/pal-ntsc.sch/VAF"]
pal_ntsc_sch_y_video = design.nets["/pal-ntsc.sch/Y-VIDEO"]
pal_ntsc_sch_y_sync = design.nets["/pal-ntsc.sch/Y_SYNC"]
net_bus1_prsnt1 = design.nets["Net-(BUS1-PRSNT1#)"]
net_bus1_prsnt2 = design.nets["Net-(BUS1-PRSNT2#)"]
net_bus1_tdi = design.nets["Net-(BUS1-TDI)"]
net_c1_pad1 = design.nets["Net-(C1-Pad1)"]
net_c3_pad1 = design.nets["Net-(C3-Pad1)"]
net_c36_pad2 = design.nets["Net-(C36-Pad2)"]
net_c39_pad2 = design.nets["Net-(C39-Pad2)"]
net_c4_pad1 = design.nets["Net-(C4-Pad1)"]
net_c40_pad2 = design.nets["Net-(C40-Pad2)"]
net_c41_pad2 = design.nets["Net-(C41-Pad2)"]
net_c46_pad1 = design.nets["Net-(C46-Pad1)"]
net_c49_pad1 = design.nets["Net-(C49-Pad1)"]
net_c5_pad2 = design.nets["Net-(C5-Pad2)"]
net_c61_pad1 = design.nets["Net-(C61-Pad1)"]
net_c8_pad2 = design.nets["Net-(C8-Pad2)"]
net_cv1_pad1 = design.nets["Net-(CV1-Pad1)"]
net_d6_a = design.nets["Net-(D6-A)"]
net_l6_pad1 = design.nets["Net-(L6-Pad1)"]
net_p4_p1 = design.nets["Net-(P4-P1)"]
net_pot1_pad3 = design.nets["Net-(POT1-Pad3)"]
net_q1_b = design.nets["Net-(Q1-B)"]
net_q1_e = design.nets["Net-(Q1-E)"]
net_q2_b = design.nets["Net-(Q2-B)"]
net_q2_e = design.nets["Net-(Q2-E)"]
net_q3_b = design.nets["Net-(Q3-B)"]
net_q3_e = design.nets["Net-(Q3-E)"]
net_u1_scl = design.nets["Net-(U1-SCL)"]
net_u1_sda = design.nets["Net-(U1-SDA)"]
net_u10_clevel = design.nets["Net-(U10-CLEVEL)"]
net_u10_cref = design.nets["Net-(U10-CREF+)"]
net_u10_n_c = design.nets["Net-(U10-N/C)"]
net_u10_out_c = design.nets["Net-(U10-OUT_C)"]
net_u10_r_2 = design.nets["Net-(U10-R/2)"]
net_u10_sync_det = design.nets["Net-(U10-SYNC_DET)"]
net_u10_vin_c = design.nets["Net-(U10-VIN_C)"]
net_u10_vin_y_comp = design.nets["Net-(U10-VIN_Y/COMP.)"]
net_u10_xtal1_in = design.nets["Net-(U10-XTAL1_IN)"]
net_u10_xtal1_out = design.nets["Net-(U10-XTAL1_OUT)"]
net_u11_flt = design.nets["Net-(U11-FLT#)"]
net_u11_mode_16_32 = design.nets["Net-(U11-MODE_16/32)"]
net_u11_snv = design.nets["Net-(U11-SNV)"]
net_u20_b = design.nets["Net-(U20-B)"]
net_u20_b_adj = design.nets["Net-(U20-B/ADJ)"]
net_u20_cs = design.nets["Net-(U20-CS)"]
net_u20_flt = design.nets["Net-(U20-FLT)"]
net_u20_g = design.nets["Net-(U20-G)"]
net_u20_mctr = design.nets["Net-(U20-MCTR)"]
net_u20_notch = design.nets["Net-(U20-NOTCH)"]
net_u20_osc = design.nets["Net-(U20-OSC)"]
net_u20_r = design.nets["Net-(U20-R)"]
net_u20_uoff = design.nets["Net-(U20-UOFF)"]
net_u20_vcc = design.nets["Net-(U20-VCC)"]
net_u20_voff = design.nets["Net-(U20-VOFF)"]
net_u20_vref = design.nets["Net-(U20-VREF)"]
net_u20_y_sin = design.nets["Net-(U20-Y+SIN)"]
net_u20_y_sout = design.nets["Net-(U20-Y+SOUT)"]
net_u23_p87 = design.nets["Net-(U23-P87)"]
net_u23_pgck4 = design.nets["Net-(U23-PGCK4)"]
net_u23_sgck3 = design.nets["Net-(U23-SGCK3)"]
net_u8_bin = design.nets["Net-(U8-BIN)"]
net_u8_bvid0 = design.nets["Net-(U8-BVID0)"]
net_u8_cext1 = design.nets["Net-(U8-CEXT1)"]
net_u8_cext2 = design.nets["Net-(U8-CEXT2)"]
net_u8_gin = design.nets["Net-(U8-GIN)"]
net_u8_gvid0 = design.nets["Net-(U8-GVID0)"]
net_u8_rin = design.nets["Net-(U8-RIN)"]
net_u8_rset = design.nets["Net-(U8-RSET)"]
net_u8_rvid0 = design.nets["Net-(U8-RVID0)"]
net_u9_comp = design.nets["Net-(U9-COMP)"]
net_u9_iref = design.nets["Net-(U9-IREF)"]
net_u9_vref = design.nets["Net-(U9-VREF)"]

design.rules.netclass(
    "pwr",
    clearance=mm("0.2"),
    track_width=mm("0.25"),
    via_diameter=mm("0.8"),
    via_drill=mm("0.4"),
    diff_pair_width=mm("0.2"),
    diff_pair_gap=mm("0.25"),
    diff_pair_via_gap=mm("0.25"),
    nets=(net_3_3v, net_5f),
)
design.rules.minimum(
    clearance=mm("0.1"),
    via_diameter=mm("0.8"),
    hole_size=mm("0.4"),
    edge_clearance=mm("0.01"),
)

connect(blue_in, p3["1"])
connect(blue_out, j4["3"])
connect(c_out, j4["8"])
connect(green_in, p2["1"])
connect(green_out, j4["2"])
connect(red_in, p1["1"])
connect(red_out, j4["1"])
connect(y_out, j4["9"])
connect(modul_cvbsout, p8["1"])
connect(gnd, j4["4"], j4["5"], j4["6"], j4["7"], p1["2"], p2["2"], p3["2"], p8["2"])

j4.place(mm("-29.261"), mm("44.145"), rot=-90, locked=True)
p1.place(mm("-40.945"), mm("4.775"), rot=180, locked=True)
p2.place(mm("-40.945"), mm("16.205"), rot=180, locked=True)
p3.place(mm("-40.945"), mm("-6.655"), rot=180, locked=True)
p8.place(mm("-40.945"), mm("-18.085"), rot=180, locked=True)

design.zone(
    net_5v,
    layers=("In2.Cu",),
    key="+5V/1",
    outline=(
        (mm("85.674"), mm("54.305")),
        (mm("94.818"), mm("45.542")),
        (mm("104.851"), mm("45.542")),
        (mm("104.851"), mm("34.493")),
        (mm("264.236"), mm("34.366")),
        (mm("264.236"), mm("-43.485")),
        (mm("-8.687"), mm("-43.485")),
        (mm("-8.687"), mm("-26.594")),
        (mm("-18.79874"), mm("-26.594")),
        (mm("-20.244"), mm("-25.1589")),
        (mm("-20.244"), mm("-23.927")),
        (mm("-46.30694"), mm("-23.927")),
        (mm("-46.406"), mm("53.797")),
    ),
    clearance=mm("0.4"),
    thermal_gap=mm("0.4"),
    thermal_spoke_width=mm("0.3"),
)
design.zone(
    gnd,
    layers=("In1.Cu",),
    key="GND/1",
    outline=(
        (mm("-45"), mm("-42.8")),
        (mm("265"), mm("-43.1")),
        (mm("265"), mm("34")),
        (mm("104.5"), mm("34")),
        (mm("104.5"), mm("45")),
        (mm("95"), mm("45")),
        (mm("85.5"), mm("54.5")),
        (mm("-5"), mm("55")),
        (mm("-5"), mm("54.5")),
        (mm("-45"), mm("54")),
    ),
    clearance=mm("0.4"),
    thermal_gap=mm("0.4"),
    thermal_spoke_width=mm("0.3"),
)

design.line(
    "Dwgs.User/line/1",
    (mm("-41.453"), mm("-26.975")),
    (mm("-36.373"), mm("-26.975")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/2",
    (mm("-41.453"), mm("58.369")),
    (mm("-36.373"), mm("58.369")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/3",
    (mm("-41.326"), mm("-23.038")),
    (mm("-41.326"), mm("54.432")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/4",
    (mm("-38.913"), mm("60.909")),
    (mm("-38.913"), mm("-29.515")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/5",
    (mm("-33.706"), mm("-43.485")),
    (mm("-33.706"), mm("-23.038")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/6",
    (mm("-33.706"), mm("-23.038")),
    (mm("-46.406"), mm("-23.038")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/7",
    (mm("-33.706"), mm("54.432")),
    (mm("-46.406"), mm("54.432")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/8",
    (mm("-33.706"), mm("54.432")),
    (mm("-33.706"), mm("63.195")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/9",
    (mm("92.659"), mm("54.94")),
    (mm("124.028"), mm("54.94")),
    layer="Dwgs.User",
    width=mm("0.2"),
)
design.line(
    "Dwgs.User/line/10",
    (mm("255.473"), mm("-33.325")),
    (mm("255.473"), mm("-43.485")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/11",
    (mm("255.473"), mm("-33.325")),
    (mm("260.553"), mm("-33.325")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/12",
    (mm("258.013"), mm("-38.405")),
    (mm("263.093"), mm("-38.405")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/13",
    (mm("260.553"), mm("-40.945")),
    (mm("260.553"), mm("-35.865")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.line(
    "Dwgs.User/line/14",
    (mm("260.553"), mm("-33.325")),
    (mm("260.553"), mm("34.366")),
    layer="Dwgs.User",
    width=mm("0.2032"),
)
design.text(
    "B.Cu/text/1",
    "TEXTE",
    (mm("-40.4624"), mm("50.9776")),
    layer="B.Cu",
    size=mm("1.524"),
    thickness=mm("0.2032"),
)
design.dimension(
    "Dwgs.User/dimension/1",
    (mm("73.609"), mm("54.94")),
    (mm("73.609"), mm("63.195")),
    offset=mm("-16.002"),
    size=mm("1.524"),
    thickness=mm("0.2"),
    width=mm("0.2"),
    extension_offset=mm("0"),
)
design.dimension(
    "Dwgs.User/dimension/2",
    (mm("124.028"), mm("34.366")),
    (mm("124.028"), mm("54.94")),
    offset=mm("-3.175"),
    size=mm("1.524"),
    thickness=mm("0.2"),
    width=mm("0.2"),
    extension_offset=mm("0"),
)

copper.apply(
    design,
    {
        "+3.3V": net_3_3v,
        "+5F": net_5f,
        "+5V": net_5v,
        "//PCRD": pcrd,
        "//PCWR": pcwr,
        "/ACCES_RAM-": acces_ram,
        "/ACQ_ON": acq_on,
        "/ADR2": adr2,
        "/ADR3": adr3,
        "/ADR4": adr4,
        "/ADR5": adr5,
        "/ADR6": adr6,
        "/BE-0": be_0,
        "/BE-1": be_1,
        "/BE-2": be_2,
        "/BE-3": be_3,
        "/BLANK-": blank,
        "/BLUE_IN": blue_in,
        "/BLUE_OUT": blue_out,
        "/BPCLK": bpclk,
        "/BT812_RD-": bt812_rd,
        "/BT812_WR-": bt812_wr,
        "/CAS0-": cas0,
        "/CAS1-": cas1,
        "/CAS2-": cas2,
        "/CAS3-": cas3,
        "/CLAMP": clamp,
        "/CLKCAD": clkcad,
        "/CLKCDA": clkcda,
        "/CSYNC-OUT": csync_out,
        "/CSYNCIN-": csyncin,
        "/C_OUT": c_out,
        "/DQ0": dq0,
        "/DQ1": dq1,
        "/DQ10": dq10,
        "/DQ11": dq11,
        "/DQ12": dq12,
        "/DQ13": dq13,
        "/DQ14": dq14,
        "/DQ15": dq15,
        "/DQ16": dq16,
        "/DQ17": dq17,
        "/DQ18": dq18,
        "/DQ19": dq19,
        "/DQ2": dq2,
        "/DQ20": dq20,
        "/DQ21": dq21,
        "/DQ22": dq22,
        "/DQ23": dq23,
        "/DQ24": dq24,
        "/DQ25": dq25,
        "/DQ26": dq26,
        "/DQ27": dq27,
        "/DQ28": dq28,
        "/DQ29": dq29,
        "/DQ3": dq3,
        "/DQ30": dq30,
        "/DQ31": dq31,
        "/DQ4": dq4,
        "/DQ5": dq5,
        "/DQ6": dq6,
        "/DQ7": dq7,
        "/DQ8": dq8,
        "/DQ9": dq9,
        "/ESVIDEO-RVB/OE_RVB-": esvideo_rvb_oe_rvb,
        "/ESVIDEO-RVB/REF+": esvideo_rvb_ref,
        "/ESVIDEO-RVB/VAA": esvideo_rvb_vaa,
        "/F_PALIN": f_palin,
        "/GREEN_IN": green_in,
        "/GREEN_OUT": green_out,
        "/HD_PAL-": hd_pal,
        "/IRQ-": irq,
        "/IRQ_SRL": irq_srl,
        "/MXA0": mxa0,
        "/MXA1": mxa1,
        "/MXA10": mxa10,
        "/MXA2": mxa2,
        "/MXA3": mxa3,
        "/MXA4": mxa4,
        "/MXA5": mxa5,
        "/MXA6": mxa6,
        "/MXA7": mxa7,
        "/MXA8": mxa8,
        "/MXA9": mxa9,
        "/OE_PAL-": oe_pal,
        "/PCA0": pca0,
        "/PCA1": pca1,
        "/PCA2": pca2,
        "/PTADR-": ptadr,
        "/PTATN-": ptatn,
        "/PTBE-0": ptbe_0,
        "/PTBE-1": ptbe_1,
        "/PTBE-2": ptbe_2,
        "/PTBE-3": ptbe_3,
        "/PTBURST": ptburst,
        "/PTNUM0": ptnum0,
        "/PTNUM1": ptnum1,
        "/PTRDY-": ptrdy,
        "/PTWR": ptwr,
        "/RAS0-": ras0,
        "/RAS1-": ras1,
        "/RAS2-": ras2,
        "/RAS3-": ras3,
        "/RAS4-": ras4,
        "/RAS5-": ras5,
        "/RAS6-": ras6,
        "/RAS7-": ras7,
        "/RDCAD-": rdcad,
        "/RDCDA-": rdcda,
        "/RDEMPTY": rdempty,
        "/RDFIFO-": rdfifo,
        "/RED_IN": red_in,
        "/RED_OUT": red_out,
        "/SELECT-": select,
        "/SYSRST-": sysrst,
        "/TVB0": tvb0,
        "/TVB1": tvb1,
        "/TVB2": tvb2,
        "/TVB3": tvb3,
        "/TVB4": tvb4,
        "/TVB5": tvb5,
        "/TVB6": tvb6,
        "/TVB7": tvb7,
        "/TVG0": tvg0,
        "/TVG1": tvg1,
        "/TVG2": tvg2,
        "/TVG3": tvg3,
        "/TVG4": tvg4,
        "/TVG5": tvg5,
        "/TVG6": tvg6,
        "/TVG7": tvg7,
        "/TVI0": tvi0,
        "/TVI1": tvi1,
        "/TVR0": tvr0,
        "/TVR1": tvr1,
        "/TVR2": tvr2,
        "/TVR3": tvr3,
        "/TVR4": tvr4,
        "/TVR5": tvr5,
        "/TVR6": tvr6,
        "/TVR7": tvr7,
        "/TVRAM0": tvram0,
        "/TVRAM1": tvram1,
        "/TVRAM10": tvram10,
        "/TVRAM11": tvram11,
        "/TVRAM12": tvram12,
        "/TVRAM13": tvram13,
        "/TVRAM14": tvram14,
        "/TVRAM15": tvram15,
        "/TVRAM16": tvram16,
        "/TVRAM17": tvram17,
        "/TVRAM18": tvram18,
        "/TVRAM19": tvram19,
        "/TVRAM2": tvram2,
        "/TVRAM20": tvram20,
        "/TVRAM21": tvram21,
        "/TVRAM22": tvram22,
        "/TVRAM23": tvram23,
        "/TVRAM24": tvram24,
        "/TVRAM25": tvram25,
        "/TVRAM26": tvram26,
        "/TVRAM27": tvram27,
        "/TVRAM28": tvram28,
        "/TVRAM29": tvram29,
        "/TVRAM3": tvram3,
        "/TVRAM30": tvram30,
        "/TVRAM31": tvram31,
        "/TVRAM4": tvram4,
        "/TVRAM5": tvram5,
        "/TVRAM6": tvram6,
        "/TVRAM7": tvram7,
        "/TVRAM8": tvram8,
        "/TVRAM9": tvram9,
        "/VD_PAL-": vd_pal,
        "/WRAM-": wram,
        "/WRCAD-": wrcad,
        "/WRCDA-": wrcda,
        "/WRFIFDO-": wrfifdo,
        "/WRFULL": wrfull,
        "/WRITE_RAM": write_ram,
        "/X_CLK": x_clk,
        "/X_DATA": x_data,
        "/X_DONE": x_done,
        "/X_IRQ": x_irq,
        "/X_PROG-": x_prog,
        "/Y_OUT": y_out,
        "/buspci.sch/EA1": buspci_sch_ea1,
        "/buspci.sch/EA10": buspci_sch_ea10,
        "/buspci.sch/EA11": buspci_sch_ea11,
        "/buspci.sch/EA12": buspci_sch_ea12,
        "/buspci.sch/EA13": buspci_sch_ea13,
        "/buspci.sch/EA14": buspci_sch_ea14,
        "/buspci.sch/EA15": buspci_sch_ea15,
        "/buspci.sch/EA2": buspci_sch_ea2,
        "/buspci.sch/EA3": buspci_sch_ea3,
        "/buspci.sch/EA4": buspci_sch_ea4,
        "/buspci.sch/EA5": buspci_sch_ea5,
        "/buspci.sch/EA6": buspci_sch_ea6,
        "/buspci.sch/EA7": buspci_sch_ea7,
        "/buspci.sch/EA9": buspci_sch_ea9,
        "/buspci.sch/EQ0": buspci_sch_eq0,
        "/buspci.sch/EQ1": buspci_sch_eq1,
        "/buspci.sch/EQ2": buspci_sch_eq2,
        "/buspci.sch/EQ3": buspci_sch_eq3,
        "/buspci.sch/EQ4": buspci_sch_eq4,
        "/buspci.sch/EQ5": buspci_sch_eq5,
        "/buspci.sch/EQ6": buspci_sch_eq6,
        "/buspci.sch/EQ7": buspci_sch_eq7,
        "/buspci.sch/P_AD0": buspci_sch_p_ad0,
        "/buspci.sch/P_AD1": buspci_sch_p_ad1,
        "/buspci.sch/P_AD10": buspci_sch_p_ad10,
        "/buspci.sch/P_AD11": buspci_sch_p_ad11,
        "/buspci.sch/P_AD12": buspci_sch_p_ad12,
        "/buspci.sch/P_AD13": buspci_sch_p_ad13,
        "/buspci.sch/P_AD14": buspci_sch_p_ad14,
        "/buspci.sch/P_AD15": buspci_sch_p_ad15,
        "/buspci.sch/P_AD16": buspci_sch_p_ad16,
        "/buspci.sch/P_AD17": buspci_sch_p_ad17,
        "/buspci.sch/P_AD18": buspci_sch_p_ad18,
        "/buspci.sch/P_AD19": buspci_sch_p_ad19,
        "/buspci.sch/P_AD2": buspci_sch_p_ad2,
        "/buspci.sch/P_AD20": buspci_sch_p_ad20,
        "/buspci.sch/P_AD21": buspci_sch_p_ad21,
        "/buspci.sch/P_AD22": buspci_sch_p_ad22,
        "/buspci.sch/P_AD23": buspci_sch_p_ad23,
        "/buspci.sch/P_AD24": buspci_sch_p_ad24,
        "/buspci.sch/P_AD25": buspci_sch_p_ad25,
        "/buspci.sch/P_AD26": buspci_sch_p_ad26,
        "/buspci.sch/P_AD27": buspci_sch_p_ad27,
        "/buspci.sch/P_AD28": buspci_sch_p_ad28,
        "/buspci.sch/P_AD29": buspci_sch_p_ad29,
        "/buspci.sch/P_AD3": buspci_sch_p_ad3,
        "/buspci.sch/P_AD30": buspci_sch_p_ad30,
        "/buspci.sch/P_AD31": buspci_sch_p_ad31,
        "/buspci.sch/P_AD4": buspci_sch_p_ad4,
        "/buspci.sch/P_AD5": buspci_sch_p_ad5,
        "/buspci.sch/P_AD6": buspci_sch_p_ad6,
        "/buspci.sch/P_AD7": buspci_sch_p_ad7,
        "/buspci.sch/P_AD8": buspci_sch_p_ad8,
        "/buspci.sch/P_AD9": buspci_sch_p_ad9,
        "/buspci.sch/P_C/BE0#": buspci_sch_p_c_be0,
        "/buspci.sch/P_C/BE1#": buspci_sch_p_c_be1,
        "/buspci.sch/P_C/BE2#": buspci_sch_p_c_be2,
        "/buspci.sch/P_C/BE3#": buspci_sch_p_c_be3,
        "/buspci.sch/P_CLK": buspci_sch_p_clk,
        "/buspci.sch/P_DEVSEL#": buspci_sch_p_devsel,
        "/buspci.sch/P_FRAME#": buspci_sch_p_frame,
        "/buspci.sch/P_GNT#": buspci_sch_p_gnt,
        "/buspci.sch/P_IDSEL": buspci_sch_p_idsel,
        "/buspci.sch/P_INTA#": buspci_sch_p_inta,
        "/buspci.sch/P_IRDY#": buspci_sch_p_irdy,
        "/buspci.sch/P_LOCK#": buspci_sch_p_lock,
        "/buspci.sch/P_PAR": buspci_sch_p_par,
        "/buspci.sch/P_PERR#": buspci_sch_p_perr,
        "/buspci.sch/P_REQ#": buspci_sch_p_req,
        "/buspci.sch/P_RST#": buspci_sch_p_rst,
        "/buspci.sch/P_SERR#": buspci_sch_p_serr,
        "/buspci.sch/P_STOP#": buspci_sch_p_stop,
        "/buspci.sch/P_TRDY#": buspci_sch_p_trdy,
        "/graphic/14MHZOUT": graphic_14mhzout,
        "/graphic/CCLK": graphic_cclk,
        "/graphic/CLK10MHz": graphic_clk10mhz,
        "/graphic/CSIO-": graphic_csio,
        "/graphic/DIN": graphic_din,
        "/graphic/DONE": graphic_done,
        "/graphic/HDOUT": graphic_hdout,
        "/graphic/HDREFOUT": graphic_hdrefout,
        "/graphic/IA0": graphic_ia0,
        "/graphic/IA1": graphic_ia1,
        "/graphic/IA2": graphic_ia2,
        "/graphic/IA3": graphic_ia3,
        "/graphic/IA4": graphic_ia4,
        "/graphic/IA5": graphic_ia5,
        "/graphic/IA6": graphic_ia6,
        "/graphic/IA7": graphic_ia7,
        "/graphic/IA8": graphic_ia8,
        "/graphic/IA9": graphic_ia9,
        "/graphic/ICAS-": graphic_icas,
        "/graphic/ID0": graphic_id0,
        "/graphic/ID1": graphic_id1,
        "/graphic/ID2": graphic_id2,
        "/graphic/ID3": graphic_id3,
        "/graphic/IOE-": graphic_ioe,
        "/graphic/IRAS-": graphic_iras,
        "/graphic/IWR-": graphic_iwr,
        "/graphic/LED": graphic_led,
        "/graphic/PROG*": graphic_prog,
        "/graphic/RESERV1": graphic_reserv1,
        "/graphic/VOSC": graphic_vosc,
        "/graphic/XTAL_I": graphic_xtal_i,
        "/graphic/X_DIN": graphic_x_din,
        "/modul/CHROM": modul_chrom,
        "/modul/CVBS": modul_cvbs,
        "/modul/CVBSOUT": modul_cvbsout,
        "/modul/LUM": modul_lum,
        "/pal-ntsc.sch/C-VIDEO": pal_ntsc_sch_c_video,
        "/pal-ntsc.sch/VAF": pal_ntsc_sch_vaf,
        "/pal-ntsc.sch/Y-VIDEO": pal_ntsc_sch_y_video,
        "/pal-ntsc.sch/Y_SYNC": pal_ntsc_sch_y_sync,
        "GND": gnd,
        "Net-(BUS1-PRSNT1#)": net_bus1_prsnt1,
        "Net-(BUS1-PRSNT2#)": net_bus1_prsnt2,
        "Net-(BUS1-TDI)": net_bus1_tdi,
        "Net-(C1-Pad1)": net_c1_pad1,
        "Net-(C3-Pad1)": net_c3_pad1,
        "Net-(C36-Pad2)": net_c36_pad2,
        "Net-(C39-Pad2)": net_c39_pad2,
        "Net-(C4-Pad1)": net_c4_pad1,
        "Net-(C40-Pad2)": net_c40_pad2,
        "Net-(C41-Pad2)": net_c41_pad2,
        "Net-(C46-Pad1)": net_c46_pad1,
        "Net-(C49-Pad1)": net_c49_pad1,
        "Net-(C5-Pad2)": net_c5_pad2,
        "Net-(C61-Pad1)": net_c61_pad1,
        "Net-(C8-Pad2)": net_c8_pad2,
        "Net-(CV1-Pad1)": net_cv1_pad1,
        "Net-(D6-A)": net_d6_a,
        "Net-(L6-Pad1)": net_l6_pad1,
        "Net-(P4-P1)": net_p4_p1,
        "Net-(POT1-Pad3)": net_pot1_pad3,
        "Net-(Q1-B)": net_q1_b,
        "Net-(Q1-E)": net_q1_e,
        "Net-(Q2-B)": net_q2_b,
        "Net-(Q2-E)": net_q2_e,
        "Net-(Q3-B)": net_q3_b,
        "Net-(Q3-E)": net_q3_e,
        "Net-(U1-SCL)": net_u1_scl,
        "Net-(U1-SDA)": net_u1_sda,
        "Net-(U10-CLEVEL)": net_u10_clevel,
        "Net-(U10-CREF+)": net_u10_cref,
        "Net-(U10-N/C)": net_u10_n_c,
        "Net-(U10-OUT_C)": net_u10_out_c,
        "Net-(U10-R/2)": net_u10_r_2,
        "Net-(U10-SYNC_DET)": net_u10_sync_det,
        "Net-(U10-VIN_C)": net_u10_vin_c,
        "Net-(U10-VIN_Y/COMP.)": net_u10_vin_y_comp,
        "Net-(U10-XTAL1_IN)": net_u10_xtal1_in,
        "Net-(U10-XTAL1_OUT)": net_u10_xtal1_out,
        "Net-(U11-FLT#)": net_u11_flt,
        "Net-(U11-MODE_16/32)": net_u11_mode_16_32,
        "Net-(U11-SNV)": net_u11_snv,
        "Net-(U20-B)": net_u20_b,
        "Net-(U20-B/ADJ)": net_u20_b_adj,
        "Net-(U20-CS)": net_u20_cs,
        "Net-(U20-FLT)": net_u20_flt,
        "Net-(U20-G)": net_u20_g,
        "Net-(U20-MCTR)": net_u20_mctr,
        "Net-(U20-NOTCH)": net_u20_notch,
        "Net-(U20-OSC)": net_u20_osc,
        "Net-(U20-R)": net_u20_r,
        "Net-(U20-UOFF)": net_u20_uoff,
        "Net-(U20-VCC)": net_u20_vcc,
        "Net-(U20-VOFF)": net_u20_voff,
        "Net-(U20-VREF)": net_u20_vref,
        "Net-(U20-Y+SIN)": net_u20_y_sin,
        "Net-(U20-Y+SOUT)": net_u20_y_sout,
        "Net-(U23-P87)": net_u23_p87,
        "Net-(U23-PGCK4)": net_u23_pgck4,
        "Net-(U23-SGCK3)": net_u23_sgck3,
        "Net-(U8-BIN)": net_u8_bin,
        "Net-(U8-BVID0)": net_u8_bvid0,
        "Net-(U8-CEXT1)": net_u8_cext1,
        "Net-(U8-CEXT2)": net_u8_cext2,
        "Net-(U8-GIN)": net_u8_gin,
        "Net-(U8-GVID0)": net_u8_gvid0,
        "Net-(U8-RIN)": net_u8_rin,
        "Net-(U8-RSET)": net_u8_rset,
        "Net-(U8-RVID0)": net_u8_rvid0,
        "Net-(U9-COMP)": net_u9_comp,
        "Net-(U9-IREF)": net_u9_iref,
        "Net-(U9-VREF)": net_u9_vref,
    },
)

design.load_schematic("schematic.toml")
