# SPDX-License-Identifier: CC0-1.0
# Copyright (c) 2026 Fenolite contributors
# Authored for fenolite-library; no upstream design material.
"""Connectivity assertions for the two-terminal example; no electrical simulation is claimed."""

from pathlib import Path
from runpy import run_path

from fenolite.testing import instantiate

resistor_link = run_path(str(Path(__file__).resolve().parents[1] / "__init__.py"))["resistor_link"]


def test_parameter_reaches_the_resistor():
    with instantiate(resistor_link, resistance="22k") as design:
        assert design.ref("dut/R").value == "22k"


def test_terminals_stay_distinct():
    with instantiate(resistor_link) as design:
        part = design.ref("dut/R")
        assert part[1].net == design.net("dut/LEFT").name
        assert part[2].net == design.net("dut/RIGHT").name
        assert part[1].net != part[2].net
