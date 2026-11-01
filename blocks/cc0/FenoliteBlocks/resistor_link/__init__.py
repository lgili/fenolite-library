# SPDX-License-Identifier: CC0-1.0
# Copyright (c) 2026 Fenolite contributors
# Authored for fenolite-library; no upstream design material.
"""A single generic resistor with two named terminals, for package and connectivity examples."""

from fenolite.dsl import Net, block, connect, mm, param

__all__ = ["resistor_link"]


@block(
    id="FenoliteBlocks:resistor_link",
    version="1.0.0",
    summary="Two-terminal generic resistor link",
    category="other",
    licence="CC0-1.0",
    sources=("D-0001",),
)
def resistor_link(b, *, resistance=param("4.7k", doc="Resistor value as a design value string")):
    left = b.port("LEFT", Net, direction="inout", doc="Resistor terminal 1")
    right = b.port("RIGHT", Net, direction="inout", doc="Resistor terminal 2")
    resistor = b.part("R", device="Fenolite:R_0603", value=resistance)
    resistor.place(mm(5), mm(5))
    connect(left, resistor[1])
    connect(right, resistor[2])
