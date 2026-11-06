#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
# Copyright (c) 2026 Fenolite contributors
"""Write devices-basic.toml, the c0390 table of generic devices (batch 12).

Each device joins a library symbol (FenoliteSymbols) with a library footprint already in fenolite-library and
maps the symbol's pins to the footprint's pads. Nothing new is measured here: the sources of a device are
those of its symbol and footprint (expand.py reads them from the records). No manufacturer, MPN or rating
is claimed; a design picks the value and the part.

    python3 devices_table.py          # writes devices-basic.toml next to this file
"""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

RESISTORS = {
    "008004": "CHIP008004_B0.3x0.15", "01005": "CHIP01005_B0.4x0.2", "0201": "CHIP0201_B0.6x0.3",
    "0402": "CHIP0402_B1x0.5", "0603": "CHIP0603_B1.6x0.8", "0805": "CHIP0805_B2x1.25",
    "1206": "CHIP1206_B3.1x1.6", "1210": "CHIP1210_B3.1x2.6", "1218": "CHIP1218_B3.1x4.6",
    "2010": "CHIP2010_B5x2.5", "2512": "CHIP2512_B6.35x3.1",
}
CAPACITORS = {
    "0402": "CHIP0402_B1x0.5", "0603": "CHIP0603_B1.6x0.8", "0805": "CHIP0805_B2x1.25",
    "1206": "CHIP1206_B3.2x1.6", "1210": "CHIP1210_B3.2x2.5", "1808": "CHIP1808_B4.57x2.03",
    "1812": "CHIP1812_B4.5x3.2", "1825": "CHIP1825_B4.5x6.4", "2220": "CHIP2220_B5.59x5.08",
    "2225": "CHIP2225_B5.59x6.35", "3640": "CHIP3640_B9.14x10.2",
}
DIODE_PACKAGES = {
    "SOD-523": "SOD523_Diodes", "SOD-323": "SOD323_Diodes", "SOD-323F": "SOD323F_Diodes",
    "SOD-123": "SOD123_Diodes", "SOD-123F": "SOD123F_Diodes", "SMA": "SMA_Diodes", "SMB": "SMB_Diodes",
    "SMC": "SMC_Diodes",
}
ZENER_PACKAGES = ("SOD-523", "SOD-323", "SOD-323F", "SOD-123", "SOD-123F")
TVS_PACKAGES = ("SMA", "SMB", "SMC")
FUSES = ("0603", "0805", "1206")
LEDS = ("0402", "0603", "0805", "1206")
SOT23 = "FenolitePackageSOT:SOT23-3_Microchip-TT"
TRANSISTORS = (
    ("Q_NPN", "BJT_NPN", "NPN bipolar transistor", "Q", {"B": "1", "E": "2", "C": "3"}, "B on pad 1, E on pad 2, C on pad 3"),
    ("Q_PNP", "BJT_PNP", "PNP bipolar transistor", "Q", {"B": "1", "E": "2", "C": "3"}, "B on pad 1, E on pad 2, C on pad 3"),
    ("Q_NMOS", "MOSFET_N", "N-channel MOSFET", "Q", {"G": "1", "S": "2", "D": "3"}, "G on pad 1, S on pad 2, D on pad 3"),
    ("Q_PMOS", "MOSFET_P", "P-channel MOSFET", "Q", {"G": "1", "S": "2", "D": "3"}, "G on pad 1, S on pad 2, D on pad 3"),
)
CRYSTALS = {
    "3225": "Crystal_SMD_3225-4Pin_3.2x2.5mm_Abracon-ABM8",
    "5032": "Crystal_SMD_5032-4Pin_5.0x3.2mm_Abracon-ABM3B",
}


def row(name, title, summary, symbol, footprint, prefix, pins, ends=None, tags=(), used=""):
    record = {"symbol": symbol, "footprint": footprint, "ref_prefix": prefix, "value": name}
    if ends:
        record["ends"] = list(ends)
    record["pins"] = pins
    return {"name": name, "title": title, "summary": summary, "tags": list(tags), "used": used, "record": record}


def two(p1="1", p2="2"):
    return {"P1": p1, "P2": p2}


def diode_pins():
    # Symbol pin 1 is the cathode, pin 2 the anode; the c0390 diode lands keep pad 1 at the cathode.
    return {"K": "1", "A": "2"}


def rows():
    out = []
    for case, fp in RESISTORS.items():
        out.append(row(f"R_{case}", f"Resistor, {case} chip", f"Generic {case} chip resistor",
                       "FenoliteSymbols:Resistor", f"FenoliteResistorSMD:{fp}", "R", two(), ("P1", "P2"),
                       ("resistor", case), "symbol pins 1, 2 on pads 1, 2"))
    for case, fp in CAPACITORS.items():
        out.append(row(f"C_{case}", f"Capacitor, {case} chip", f"Generic {case} chip capacitor (non-polarized)",
                       "FenoliteSymbols:Capacitor", f"FenoliteCapacitorSMD:{fp}", "C", two(), ("P1", "P2"),
                       ("capacitor", case), "symbol pins 1, 2 on pads 1, 2"))
    out.append(row("L_0603", "Inductor, 0603 chip", "Generic 0603 chip inductor",
                   "FenoliteSymbols:Inductor", "FenoliteInductorSMD:CHIP0603_B1.6x0.8", "L", two(), ("P1", "P2"),
                   ("inductor", "0603"), "symbol pins 1, 2 on pads 1, 2"))
    out.append(row("FB_0603", "Ferrite bead, 0603 chip", "Generic 0603 chip ferrite bead on the 0603 inductor land",
                   "FenoliteSymbols:Ferrite_Bead", "FenoliteInductorSMD:CHIP0603_B1.6x0.8", "FB", two(), ("P1", "P2"),
                   ("ferrite", "0603"), "symbol pins 1, 2 on pads 1, 2"))
    for case in FUSES:
        out.append(row(f"Fuse_{case}", f"Fuse, {case} chip", f"Generic {case} chip fuse on the {case} chip-resistor land",
                       "FenoliteSymbols:Fuse", f"FenoliteResistorSMD:{RESISTORS[case]}", "F", two(), ("P1", "P2"),
                       ("fuse", case), "symbol pins 1, 2 on pads 1, 2"))
    for case in LEDS:
        out.append(row(f"LED_{case}", f"LED, {case} chip", f"Generic {case} chip LED on the {case} chip-resistor land, "
                       "pad 1 cathode (the land carries no polarity mark)",
                       "FenoliteSymbols:LED", f"FenoliteResistorSMD:{RESISTORS[case]}", "D", diode_pins(), ("A", "K"),
                       ("led", case), "K (symbol pin 1) on pad 1, A (pin 2) on pad 2"))
    for name, symbol, what, prefix, pins, used in TRANSISTORS:
        out.append(row(f"{name}_SOT-23", f"{what[0].upper()}{what[1:]}, SOT-23", f"Generic {what} in SOT-23 with the "
                       "common pin-out of the symbol: " + used.replace(" on ", " ").replace("pad ", ""),
                       f"FenoliteSymbols:{symbol}", SOT23, prefix, pins, None,
                       ("transistor", "sot-23"), f"symbol pins 1, 2, 3 on pads 1, 2, 3 ({used})"))
    for size, fp in CRYSTALS.items():
        out.append(row(f"Crystal_GND24_{size}", f"Crystal, SMD {size}, 4 pads",
                       f"Generic four-pad SMD crystal {size}: pads 1 and 3 the crystal, pads 2 and 4 the lid (GND)",
                       "FenoliteSymbols:Crystal_GND24", f"FenoliteCrystal:{fp}", "Y",
                       {"X1": "1", "X2": "3", "GND": {"map": {"2": "2", "4": "4"}}}, None, ("crystal", size),
                       "symbol pins 1 to 4 on pads 1 to 4"))
    for pkg, fp in DIODE_PACKAGES.items():
        out.append(row(f"D_{pkg}", f"Diode, {pkg}", f"Generic diode in {pkg}, pad 1 cathode",
                       "FenoliteSymbols:Diode", f"FenoliteDiodeSMD:{fp}", "D", diode_pins(), ("A", "K"),
                       ("diode", pkg.lower()), "K (symbol pin 1) on pad 1, A (pin 2) on pad 2"))
        out.append(row(f"D_Schottky_{pkg}", f"Schottky diode, {pkg}", f"Generic Schottky diode in {pkg}, pad 1 cathode",
                       "FenoliteSymbols:Diode_Schottky", f"FenoliteDiodeSMD:{fp}", "D", diode_pins(), ("A", "K"),
                       ("diode", "schottky", pkg.lower()), "K (symbol pin 1) on pad 1, A (pin 2) on pad 2"))
    for pkg in ZENER_PACKAGES:
        out.append(row(f"D_Zener_{pkg}", f"Zener diode, {pkg}", f"Generic Zener diode in {pkg}, pad 1 cathode",
                       "FenoliteSymbols:Diode_Zener", f"FenoliteDiodeSMD:{DIODE_PACKAGES[pkg]}", "D", diode_pins(),
                       ("A", "K"), ("diode", "zener", pkg.lower()), "K (symbol pin 1) on pad 1, A (pin 2) on pad 2"))
    for pkg in TVS_PACKAGES:
        out.append(row(f"D_TVS_Bidirectional_{pkg}", f"Bidirectional TVS diode, {pkg}",
                       f"Generic bidirectional TVS diode in {pkg}",
                       "FenoliteSymbols:TVS_Bidirectional", f"FenoliteDiodeSMD:{DIODE_PACKAGES[pkg]}", "D",
                       {"A1": "1", "A2": "2"}, ("A1", "A2"), ("diode", "tvs", pkg.lower()),
                       "A1 (symbol pin 1) on pad 1, A2 (pin 2) on pad 2"))
    out.append(row("Regulator_Linear_SOT-223_GND-OUT-IN", "Linear regulator, SOT-223, pins GND/ADJ, OUT, IN",
                   "Generic three-terminal linear regulator in SOT-223 with the 1117-style pin-out: pad 1 GND/ADJ, "
                   "pad 2 and tab VOUT, pad 3 VIN",
                   "FenoliteSymbols:Regulator_Linear", "FenolitePackageSOT:SOT223_Diodes", "U",
                   {"VIN": {"map": {"1": "3"}}, "GND": {"map": {"2": "1"}}, "VOUT": {"map": {"3": ["2", "4"]}}},
                   None, ("regulator", "sot-223"), "VIN (symbol pin 1) on pad 3, GND (2) on pad 1, VOUT (3) on pad 2 and tab 4"))
    out.append(row("Regulator_Linear_TO-220-3_IN-GND-OUT", "Linear regulator, TO-220, pins IN, GND, OUT",
                   "Generic three-terminal linear regulator in TO-220 upright with the 78xx-style pin-out: "
                   "pad 1 VIN, pad 2 GND, pad 3 VOUT",
                   "FenoliteSymbols:Regulator_Linear", "FenolitePackageTO:TO-220-3_P2.54_Microchip-AB_Vertical", "U",
                   {"VIN": "1", "GND": "2", "VOUT": "3"}, None, ("regulator", "to-220"),
                   "VIN (symbol pin 1) on pad 1, GND (2) on pad 2, VOUT (3) on pad 3"))
    for n in range(1, 41):
        pins = {f"P{i}": str(i) for i in range(1, n + 1)}
        out.append(row(f"Conn_01x{n:02d}_P2.54", f"Pin header 1x{n:02d}, 2.54 mm",
                       f"Generic 1 x {n} pin header, 2.54 mm pitch, through-hole",
                       f"FenoliteSymbols:Conn_01x{n:02d}", f"FenoliteConnectorHeader:HDR1x{n}_P2.54_Samtec-TSW", "J",
                       pins, None, ("connector", "header", "2.54mm"), f"symbol pins 1 to {n} on pads 1 to {n}"))
    for pitch, series, first in (("2.54", "TSW", 1), ("1.27", "FTSH", 2)):
        for n in range(first, 41):
            pins = {f"P{i}": str(i) for i in range(1, 2 * n + 1)}
            out.append(row(f"Conn_02x{n:02d}_P{pitch}", f"Pin header 2x{n:02d}, {pitch} mm",
                           f"Generic 2 x {n} pin header, {pitch} mm pitch, odd pins in the first row, through-hole",
                           f"FenoliteSymbols:Conn_02x{n:02d}", f"FenoliteConnectorHeader:HDR2x{n}_P{pitch}_Samtec-{series}",
                           "J", pins, None, ("connector", "header", f"{pitch}mm"),
                           f"symbol pins 1 to {2 * n} on pads 1 to {2 * n} (odd pins first row)"))
    return out


def toml_value(value):
    if isinstance(value, dict):
        return "{ " + ", ".join(f"{json.dumps(k) if not k.isidentifier() else k} = {toml_value(v)}" for k, v in value.items()) + " }"
    if isinstance(value, list):
        return "[" + ", ".join(toml_value(v) for v in value) + "]"
    return json.dumps(value)


def rows_more():
    """Batch 13: devices on the footprints and symbols added after batch 12."""
    out = []
    for kind, symbol, prefix, what in (("FB", "Ferrite_Bead", "FB", "ferrite bead"), ("L", "Inductor", "L", "inductor")):
        for case in ("0805", "1206"):
            out.append(row(f"{kind}_{case}", f"{what[0].upper()}{what[1:]}, {case} chip",
                           f"Generic {case} chip {what} on the {case} chip-resistor land",
                           f"FenoliteSymbols:{symbol}", f"FenoliteResistorSMD:{RESISTORS[case]}", prefix, two(), ("P1", "P2"),
                           (kind.lower() == "fb" and "ferrite" or "inductor", case), "symbol pins 1, 2 on pads 1, 2"))
    out.append(row("OpAmp_Single_SC70-5", "Operational amplifier, single, SC-70-5",
                   "Generic single op-amp in SC-70-5 with the common pin-out: pad 1 +IN, 2 V-, 3 -IN, 4 OUT, 5 V+",
                   "FenoliteSymbols:OpAmp", "FenolitePackageSOT:SC70-5_Microchip-LT", "U",
                   {"INP": {"map": {"3": "1"}}, "VN": {"map": {"4": "2"}}, "INN": {"map": {"2": "3"}},
                    "OUT": {"map": {"6": "4"}}, "VP": {"map": {"7": "5"}}}, None, ("opamp", "sc-70-5"),
                   "+IN (symbol pin 3) on pad 1, V- (4) on pad 2, -IN (2) on pad 3, OUT (6) on pad 4, V+ (7) on pad 5"))
    out.append(row("D_Zener_Dual_CommonAnode_SOT-23", "Dual Zener diode, common anode, SOT-23",
                   "Generic dual Zener diode with a common anode in SOT-23: pad 1 K1, pad 2 K2, pad 3 A",
                   "FenoliteSymbols:Diode_Zener_Dual_CommonAnode", SOT23, "D", {"K1": "1", "K2": "2", "A": "3"}, None,
                   ("diode", "zener", "sot-23"), "symbol pins 1, 2, 3 on pads 1, 2, 3"))
    out.append(row("Optocoupler_NPN_DIP4-SMD", "Optocoupler, phototransistor output, 4-lead SMD DIP",
                   "Generic optocoupler with an NPN phototransistor output in a 4-lead SMD DIP: pad 1 A, 2 K, 3 E, 4 C",
                   "FenoliteSymbols:Optocoupler_NPN", "FenolitePackageDIP:DIP4_SMD_W7.62_P2.54_Vishay-Opt7", "U",
                   {"A": "1", "K": "2", "E": "3", "C": "4"}, None, ("optocoupler", "dip-4", "smd"),
                   "symbol pins 1 to 4 on pads 1 to 4"))
    return out


def write_table(path, rows_, header, date):
    lines = header + [
        'schema = "fenolite.c0390-family.v0"',
        'kind = "device"',
        'namespace = "FenoliteDevices"',
        'category = "Generic device"',
        f'date = "{date}"',
        'tags = ["device", "generic"]',
    ]
    for r in rows_:
        lines += ["", "[[row]]"]
        for key in ("name", "title", "summary", "used"):
            lines.append(f"{key} = {json.dumps(r[key])}")
        lines.append(f"tags = {toml_value(r['tags'])}")
        for key, value in r["record"].items():
            lines.append(f"record.{key} = {toml_value(value)}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{path.name}: {len(rows_)} rows")


def main():
    write_table(HERE / "devices-more.toml", rows_more(), [
        "# SPDX-License-Identifier: CC0-1.0",
        "# Generic devices, batch 13 of change c0390, written by devices_table.py: each joins a FenoliteSymbols",
        "# symbol with a fenolite-library footprint and maps pins to pads. Sources come from the symbol and",
        "# footprint records; no manufacturer, part number or rating is claimed.",
    ], "2026-11-06")


def main_batch12():
    lines = [
        "# SPDX-License-Identifier: CC0-1.0",
        "# Generic devices, batch 12 (first part) of change c0390, written by devices_table.py: each joins a",
        "# FenoliteSymbols symbol with a fenolite-library footprint and maps pins to pads. Sources come from the",
        "# symbol and footprint records; no manufacturer, part number or rating is claimed.",
        'schema = "fenolite.c0390-family.v0"',
        'kind = "device"',
        'namespace = "FenoliteDevices"',
        'category = "Generic device"',
        'date = "2026-11-05"',
        'tags = ["device", "generic"]',
    ]
    for r in rows():
        lines += ["", "[[row]]"]
        for key in ("name", "title", "summary", "used"):
            lines.append(f"{key} = {json.dumps(r[key])}")
        lines.append(f"tags = {toml_value(r['tags'])}")
        for key, value in r["record"].items():
            lines.append(f"record.{key} = {toml_value(value)}")
    (HERE / "devices-basic.toml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(rows())} rows")


if __name__ == "__main__":
    main_batch12()
    main()
