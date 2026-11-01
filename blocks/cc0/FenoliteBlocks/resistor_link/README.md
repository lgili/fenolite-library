# Resistor link

Authored for fenolite-library and dedicated under CC0-1.0. This package is an original connectivity
example: one generic shipped `Fenolite:R_0603` resistor connects `LEFT` to `RIGHT`. It is not a
manufacturer part recommendation, a power rating, an analogue model or a validated product circuit.

`resistance` changes the resistor's design value; the default is `4.7k`. The usage example selects
`10k`. Tests check parameter propagation and independent terminal nets. The golden records the usage
circuit and rules; it supplies no independent electrical or manufacturing proof. Evidence is INFERRED.

The package exports only `resistor_link`. Indexing and explicit tests execute it; discovery reads
`block.json` without importing it. No network, file-write or import-time side effect is required.
