# SPDX-License-Identifier: CC0-1.0
# Copyright (c) 2026 Fenolite contributors
# Authored for fenolite-library; no upstream design material.
"""The complete usage circuit: one resistor between two independent terminal nets."""

from pathlib import Path
from runpy import run_path

from fenolite.dsl import Design, Part, connect, mm

resistor_link = run_path(str(Path(__file__).resolve().parents[1] / "__init__.py"))["resistor_link"]
design = Design("resistor-link-usage")
design.board(mm(20), mm(12))
link = design.use(resistor_link, "link", resistance="10k")
terminals = Part("J1", device="Fenolite:Conn_1x2_P2.54")
design.add(terminals)
terminals.place(mm(15), mm(5))
connect(link.LEFT, terminals[1])
connect(link.RIGHT, terminals[2])
