#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
# Copyright (c) 2026 Fenolite contributors
"""Write symbols.toml, the c0390 table of generic symbols per device class (batch 5).

Every drawing here is authored for fenolite-library: conventional schematic shapes (box or zigzag resistor,
plate capacitor, triangle-and-bar diode, transistor, op-amp triangle) drawn with Fenolite's own
coordinates on the 2.54 mm grid. No third-party symbol file is read. Pin numbers follow the common
package pin-outs named in each row's summary; a device record maps functions to pins.
"""

from __future__ import annotations

import json
from decimal import Decimal
from pathlib import Path


def mm(v: float | str | Decimal) -> str:
    d = Decimal(str(v)).quantize(Decimal("0.001"))
    text = format(d.normalize(), "f")
    return f"{'0' if text in ('-0', '') else text}mm"


def pt(x, y):
    return [mm(x), mm(y)]


def pin(number, x, y, rot=0, length=2.54):
    p = {"number": str(number), "at": pt(x, y), "length": mm(length)}
    if rot:
        p["rotation"] = f"{rot}deg"
    return p


def line(*points, width=None):
    g = {"kind": "line", "points": [pt(*p) for p in points]}
    if width:
        g["width"] = mm(width)
    return g


def poly(*points, filled=True):
    return {"kind": "polygon", "points": [pt(*p) for p in points], "filled": filled}


def rect(a, b, filled=False):
    g = {"kind": "rect", "points": [pt(*a), pt(*b)]}
    if filled:
        g["filled"] = True
    return g


def circle(c, r):
    return {"kind": "circle", "points": [pt(*c), pt(c[0] + r, c[1])]}


def arc_points(cx, cy, r, a0, a1, n=8):
    import math

    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]


ROWS: list[dict] = []


def leads(x):
    """Lead lines from the pin ends at +-2.54 mm to a body edge at +-x."""
    return [line((-2.54, 0), (-x, 0)), line((x, 0), (2.54, 0))]


AMP = [line((-5.08, -2.54), (-3.81, -2.54)), line((-5.08, 2.54), (-3.81, 2.54)), line((3.81, 0), (5.08, 0)),
       # + and - drawn inside the triangle, so pin names (V+, V-) can stay hidden and never cross the numbers.
       line((-3.302, 2.54), (-2.286, 2.54)), line((-2.794, 2.032), (-2.794, 3.048)), line((-3.302, -2.54), (-2.286, -2.54))]


def segments(graphics):
    """Split every multi-point line into two-point lines.

    The pinned core's KiCad symbol writer emits only the first two points of a `line` graphic (core gap G-5),
    so a zigzag or an arc drawn as one polyline would lose all but its first segment.
    """
    out = []
    for g in graphics:
        if g["kind"] == "line" and len(g["points"]) > 2:
            extra = {k: v for k, v in g.items() if k not in ("kind", "points")}
            out += [{"kind": "line", "points": [a, b], **extra} for a, b in zip(g["points"], g["points"][1:])]
        else:
            out.append(g)
    return out


def add(name, title, summary, ref, pins, placements, graphics, tags, hide_names=True, hide_numbers=False, category="Generic symbol"):
    sym = {"reference": ref, "pin_names_hidden": hide_names}
    if hide_numbers:
        sym["pin_numbers_hidden"] = True
    sym["pins"] = placements
    sym["graphic"] = segments(graphics)
    ROWS.append({"name": name, "title": title, "summary": summary, "category": category, "tags": tags,
                 "record": {"pin": [{"number": str(n), "name": nm, "type": t} for n, nm, t in pins], "symbol": sym}})


two = [pin(1, -5.08, 0), pin(2, 5.08, 0, 180)]
add("Resistor", "Resistor (box)", "Generic two-terminal resistor, box outline", "R",
    [(1, "~", "passive"), (2, "~", "passive")], two, [rect((-2.54, -1.016), (2.54, 1.016))], ["resistor"], hide_numbers=True)
zig = [(-2.54, 0)] + [(-2.2225 + 0.635 * i, 1.016 if i % 2 == 0 else -1.016) for i in range(8)] + [(2.54, 0)]
add("Resistor_US", "Resistor (zigzag)", "Generic two-terminal resistor, zigzag", "R",
    [(1, "~", "passive"), (2, "~", "passive")], two, [line(*zig)], ["resistor"], hide_numbers=True)
add("Capacitor", "Capacitor", "Generic non-polarized capacitor", "C",
    [(1, "~", "passive"), (2, "~", "passive")], two,
    [line((-0.635, -2.032), (-0.635, 2.032), width=0.508), line((0.635, -2.032), (0.635, 2.032), width=0.508), *leads(0.635)], ["capacitor"], hide_numbers=True)
add("Capacitor_Polarized", "Capacitor, polarized", "Generic polarized capacitor, pin 1 positive", "C",
    [(1, "+", "passive"), (2, "-", "passive")], two,
    [*leads(1.016), rect((-1.016, -2.032), (-0.635, 2.032)), rect((0.635, -2.032), (1.016, 2.032), filled=True),
     line((-2.286, 1.524), (-1.524, 1.524)), line((-1.905, 1.143), (-1.905, 1.905))], ["capacitor", "polarized"], hide_numbers=True)
hump = []
for cx in (-1.905, -0.635, 0.635, 1.905):
    hump += arc_points(cx, 0, 0.635, 180, 0)[(1 if hump else 0):]
add("Inductor", "Inductor", "Generic inductor", "L",
    [(1, "~", "passive"), (2, "~", "passive")], two, [line(*hump)], ["inductor"], hide_numbers=True)
add("Ferrite_Bead", "Ferrite bead", "Generic ferrite bead, filled box", "FB",
    [(1, "~", "passive"), (2, "~", "passive")], two,
    [rect((-1.524, -0.762), (1.524, 0.762), filled=True), *leads(1.524)], ["ferrite-bead", "inductor"], hide_numbers=True)
tri = poly((-1.27, -1.27), (1.27, 0), (-1.27, 1.27), filled=False)
DLEADS = [line((-2.54, 0), (-1.27, 0)), line((1.27, 0), (2.54, 0))]
dpins = [pin(1, 5.08, 0, 180), pin(2, -5.08, 0, 0)]
dnames = [(1, "K", "passive"), (2, "A", "passive")]
add("Diode", "Diode", "Generic diode, pin 1 cathode, pin 2 anode", "D", dnames, dpins,
    [tri, *DLEADS, line((1.27, -1.27), (1.27, 1.27)), line((-1.27, 0), (1.27, 0))], ["diode"])
add("Diode_Schottky", "Schottky diode", "Generic Schottky diode, pin 1 cathode, pin 2 anode", "D", dnames, dpins,
    [tri, line((1.778, 1.016), (1.778, 1.27), (1.27, 1.27), (1.27, -1.27), (0.762, -1.27), (0.762, -1.016)), line((-1.27, 0), (1.27, 0)), *DLEADS], ["diode", "schottky"])
add("Diode_Zener", "Zener diode", "Generic Zener diode, pin 1 cathode, pin 2 anode", "D", dnames, dpins,
    [tri, line((1.778, 1.524), (1.27, 1.27), (1.27, -1.27), (0.762, -1.524)), line((-1.27, 0), (1.27, 0)), *DLEADS], ["diode", "zener"])
add("TVS_Bidirectional", "TVS diode, bidirectional", "Generic bidirectional transient voltage suppressor", "D",
    [(1, "A1", "passive"), (2, "A2", "passive")], [pin(1, -5.08, 0, 0, 2.54), pin(2, 5.08, 0, 180, 2.54)],
    [poly((-2.54, -1.27), (0, 0), (-2.54, 1.27), filled=False), poly((2.54, -1.27), (0, 0), (2.54, 1.27), filled=False),
     line((0.508, 1.524), (0, 1.27), (0, -1.27), (-0.508, -1.524))], ["diode", "tvs"])
arrow = lambda x, y: [line((x, y), (x + 1.016, y + 1.016)), poly((x + 1.016, y + 1.016), (x + 0.381, y + 0.889), (x + 0.889, y + 0.381))]
add("LED", "Light-emitting diode", "Generic LED, pin 1 cathode, pin 2 anode", "D", dnames, dpins,
    [tri, *DLEADS, line((1.27, -1.27), (1.27, 1.27)), line((-1.27, 0), (1.27, 0)), *arrow(-0.508, 1.524), *arrow(0.508, 1.524)], ["diode", "led"])


def bjt(name, title, pnp):
    g = [line((-0.508, -1.524), (-0.508, 1.524), width=0.508), line((-0.508, 0.635), (2.54, 2.54)), line((-0.508, -0.635), (2.54, -2.54)),
         circle((1.016, 0), 2.794)]
    g.append(poly((1.381, -1.345), (0.406, -1.207), (0.957, -2.023)) if pnp else poly((2.083, -2.254), (1.532, -1.438), (1.108, -2.116)))
    add(name, title, f"Generic {'PNP' if pnp else 'NPN'} bipolar transistor; pins 1 B, 2 E, 3 C (common SOT-23 pin-out)", "Q",
        [(1, "B", "input"), (2, "E", "passive"), (3, "C", "passive")],
        [pin(1, -5.08, 0, 0), pin(2, 2.54, -5.08, 90), pin(3, 2.54, 5.08, 270)], [line((-2.54, 0), (-0.508, 0)), *g], ["bjt", "pnp" if pnp else "npn", "transistor"])


bjt("BJT_NPN", "NPN transistor", False)
bjt("BJT_PNP", "PNP transistor", True)


def mos(name, title, p):
    g = [line((-2.032, -1.905), (-2.032, 1.905)), line((-1.27, -2.032), (-1.27, -1.016)), line((-1.27, -0.508), (-1.27, 0.508)),
         line((-1.27, 1.016), (-1.27, 2.032)), line((-1.27, 1.524), (2.54, 1.524), (2.54, 2.54)), line((-1.27, -1.524), (2.54, -1.524), (2.54, -2.54)),
         line((-1.27, 0), (2.54, 0), (2.54, -1.524)), circle((0.635, 0), 2.794)]
    g.append(poly((-0.381, 0), (0.381, 0.381), (0.381, -0.381)) if p else poly((-1.27, 0), (-0.508, 0.381), (-0.508, -0.381)))
    add(name, title, f"Generic {'P' if p else 'N'}-channel enhancement MOSFET; pins 1 G, 2 S, 3 D (common SOT-23 pin-out)", "Q",
        [(1, "G", "input"), (2, "S", "passive"), (3, "D", "passive")],
        [pin(1, -5.08, 0, 0), pin(2, 2.54, -5.08, 90), pin(3, 2.54, 5.08, 270)], [line((-2.54, 0), (-2.032, 0)), *g], ["mosfet", "pmos" if p else "nmos", "transistor"])


mos("MOSFET_N", "N-channel MOSFET", False)
mos("MOSFET_P", "P-channel MOSFET", True)
add("OpAmp", "Operational amplifier", "Generic single operational amplifier; pins 2 -IN, 3 +IN, 4 V-, 6 OUT, 7 V+ (common 8-pin single pin-out)", "U",
    [(2, "-", "input"), (3, "+", "input"), (4, "V-", "power_in"), (6, "~", "output"), (7, "V+", "power_in")],
    [pin(2, -7.62, -2.54), pin(3, -7.62, 2.54), pin(4, 0, -5.08, 90), pin(6, 7.62, 0, 180), pin(7, 0, 5.08, 270)],
    [poly((-3.81, -5.08), (3.81, 0), (-3.81, 5.08), filled=False), *AMP], ["amplifier", "opamp"])
add("Comparator", "Comparator", "Generic comparator; pins 2 -IN, 3 +IN, 4 V-, 7 OUT (open collector), 8 V+", "U",
    [(2, "-", "input"), (3, "+", "input"), (4, "V-", "power_in"), (7, "~", "open_collector"), (8, "V+", "power_in")],
    [pin(2, -7.62, -2.54), pin(3, -7.62, 2.54), pin(4, 0, -5.08, 90), pin(7, 7.62, 0, 180), pin(8, 0, 5.08, 270)],
    [poly((-3.81, -5.08), (3.81, 0), (-3.81, 5.08), filled=False), *AMP], ["comparator"])
add("Regulator_Linear", "Linear regulator, three terminals", "Generic three-terminal positive linear regulator; pins 1 VIN, 2 GND, 3 VOUT", "U",
    [(1, "VIN", "power_in"), (2, "GND", "power_in"), (3, "VOUT", "power_out")],
    [pin(1, -7.62, 2.54, 0), pin(2, 0, -5.08, 90), pin(3, 7.62, 2.54, 180)], [rect((-5.08, -2.54), (5.08, 5.08))], ["ldo", "regulator"], hide_names=False)
add("Crystal", "Crystal, two terminals", "Generic quartz crystal, two terminals", "Y",
    [(1, "1", "passive"), (2, "2", "passive")], two,
    [*leads(1.524), rect((-0.762, -1.524), (0.762, 1.524)), line((-1.524, -1.27), (-1.524, 1.27)), line((1.524, -1.27), (1.524, 1.27))], ["crystal"], hide_numbers=True)
add("Crystal_GND24", "Crystal, four terminals", "Generic quartz crystal in a four-pad package; pins 1 and 3 crystal, 2 and 4 case ground", "Y",
    [(1, "1", "passive"), (2, "GND", "passive"), (3, "3", "passive"), (4, "GND", "passive")],
    [pin(1, -5.08, 0), pin(3, 5.08, 0, 180), pin(2, 0, -5.08, 90), pin(4, 0, 5.08, 270)],
    [*leads(1.524), line((0, -2.54), (0, -1.524)), line((0, 1.524), (0, 2.54)), rect((-0.762, -1.524), (0.762, 1.524)), line((-1.524, -1.27), (-1.524, 1.27)), line((1.524, -1.27), (1.524, 1.27))], ["crystal"])
add("Fuse", "Fuse", "Generic fuse", "F", [(1, "~", "passive"), (2, "~", "passive")], two,
    [rect((-2.54, -0.762), (2.54, 0.762)), line((-2.54, 0), (2.54, 0))], ["fuse"], hide_numbers=True)

for n in range(1, 41):
    pl = [pin(i + 1, -5.08, -2.54 * i) for i in range(n)]
    add(f"Conn_01x{n:02d}", f"Connector, 1 row, {n} pins", f"Generic single-row connector, {n} pins, pin 1 at the top", "J",
        [(i + 1, f"Pin_{i + 1}", "passive") for i in range(n)], pl,
        [rect((-2.54, 1.27), (0, -2.54 * (n - 1) - 1.27))], ["connector", "single-row"], category="Generic connector symbol")
for n in range(1, 41):
    pl = []
    for i in range(n):
        pl += [pin(2 * i + 1, -5.08, -2.54 * i), pin(2 * i + 2, 5.08, -2.54 * i, 180)]
    add(f"Conn_02x{n:02d}", f"Connector, 2 rows, {2 * n} pins", f"Generic two-row connector, {2 * n} pins, odd pins left, even pins right", "J",
        [(i + 1, f"Pin_{i + 1}", "passive") for i in range(2 * n)], pl,
        [rect((-2.54, 1.27), (2.54, -2.54 * (n - 1) - 1.27))], ["connector", "dual-row"], category="Generic connector symbol")


def tv(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, str)):
        return json.dumps(v)
    if isinstance(v, list):
        return "[" + ", ".join(tv(x) for x in v) + "]"
    if isinstance(v, dict):
        return "{ " + ", ".join(f"{k} = {tv(x)}" for k, x in v.items()) + " }"
    raise TypeError(v)


out = ['''# SPDX-License-Identifier: CC0-1.0
# Generic symbols per device class, batch 5 of change c0390. Written by symbols_table.py; drawings authored
# here on the 2.54 mm grid; no third-party symbol file read.
schema = "fenolite.c0390-family.v0"
kind = "symbol"
namespace = "FenoliteSymbols"
category = "Generic symbol"
date = "2026-11-04"
sources = ["D-0422"]
used = "Original generic schematic drawings authored for fenolite-library; no manufacturer data."
tags = ["generic", "symbol"]
''']
for r in ROWS:
    out.append(f'''
[[row]]
name = {json.dumps(r["name"])}
title = {json.dumps(r["title"])}
summary = {json.dumps(r["summary"])}
category = {json.dumps(r["category"])}
tags = {tv(r["tags"])}
record.pin = {tv(r["record"]["pin"])}
record.symbol = {tv(r["record"]["symbol"])}
''')
Path(__file__).with_name("symbols.toml").write_text("".join(out), encoding="utf-8")
print(len(ROWS), "symbols")
