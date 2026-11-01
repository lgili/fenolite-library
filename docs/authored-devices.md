# Original illustrative device items

This original CC0 set demonstrates records, exact dependency pins and offline vendoring. It is
UNVERIFIED example data authored for fenolite-library, not a conversion, manufacturer specification,
recommended component or reviewed design. No external library or upstream fixture was copied.

| Kind | Literal item id | Source payload |
|---|---|---|
| Symbol | FenoliteDevices:IllustrativeSymbol | symbols/cc0/FenoliteDevices/IllustrativeSymbol/pins.toml |
| Footprint | FenoliteDevices:IllustrativeLand | footprints/cc0/FenoliteDevices/IllustrativeLand/package.toml |
| Device | FenoliteDevices:IllustrativeResistor | devices/cc0/FenoliteDevices/IllustrativeResistor/device.toml |

Each item is version 1.0.0, includes the full CC0 legal text, a dated NOTICE and authored provenance,
and uses the original source D-0003. D-0002 identifies the legal code. The device depends on exactly
symbol/FenoliteDevices:IllustrativeSymbol@1.0.0 and footprint/FenoliteDevices:IllustrativeLand@1.0.0.

## Invented example values

Every value below was chosen here. None comes from a datasheet or a manufacturing standard.

| Property | Original example value |
|---|---|
| Symbol | Two passive A/B pins at x = -5.08 mm and +5.08 mm, each 2.54 mm long |
| Symbol body | Rectangle from (-2.54 mm, -1.27 mm) to (2.54 mm, 1.27 mm) |
| Pad mapping | A/pin 1/pad 1 and B/pin 2/pad 2 |
| Lands | Two 1.2 mm by 1.8 mm rectangles at x = -2.1 mm and +2.1 mm |
| Body dimensions | 3.6 mm by 1.4 mm; height metadata 0.8 mm |
| Courtyard | 6.5 mm by 3 mm rectangle |
| Value and tolerance | 2.2k, 10% |
| Voltage | Operating 10 V; absolute maximum 20 V |
| Current | Operating 6 mA; absolute maximum 15 mA |
| Power | Operating 75 mW; absolute maximum 250 mW |
| Temperature | Operating -10 to 50 degC; absolute maximum -20 to 70 degC |
| Example identifier | AUTHORED-EXAMPLE-2K2; lifecycle unknown, no manufacturer or real orderable MPN |

The records contain no human review entries. Licence dedication is the author's CC0 choice and is
not a review of pin mapping, physical dimensions or electrical limits. Native output generation and
successful builds do not raise the records' evidence above UNVERIFIED.

## Local proofs and the required source-register fix

Local proofs selected clean Fenolite core 7645b8931fe21aee293e1bfa11ec86b035d28da4 in an isolated
venv. All three records parse and each item audit exits 0. Both native outputs reproduce twice with
identical bytes, and the exact explicit-record regeneration workflow body passes. Explicit records use
the core record/backend APIs; family-generator records retain their library generate path. This avoids
sending generator=explicit data to the separate family-only generator.

Final proofs use a clean detached copy of core 04a9d07e6e8d0140e9d07e2e89379531ecc03ef5, which
fixes the external D-source register reader. The exact record check now exits 0 without waivers.
A reviewed --sheets write plan was confirmed and produced six HTML sheets; no review acceptance,
reviewer entry or evidence promotion was performed. Generation and the offline proof were rerun on
that exact fixed core and pass with the current data.

```sh
fenolite library audit . --item symbols/cc0/FenoliteDevices/IllustrativeSymbol --json
fenolite library audit . --item footprints/cc0/FenoliteDevices/IllustrativeLand --json
fenolite library audit . --item devices/cc0/FenoliteDevices/IllustrativeResistor --json
fenolite library check symbols/cc0/FenoliteDevices/IllustrativeSymbol \
  footprints/cc0/FenoliteDevices/IllustrativeLand devices/cc0/FenoliteDevices/IllustrativeResistor --json
```

On the initial 7645b893 core the last command exits 5 with five library.source-unknown findings for D-0003,
including dependency repeats. Its library check register reader recognises only S-ids in sources.toml;
the library item audit correctly validates the registered D-id. The future public tool pin must include
the 04a9d07e fix. No source alias, skip or waiver was added. A negative control with D-9999 is refused by the
audit, and removing a pad correctly produces library.pad-count in the record checker.

## Offline local distribution proof

A temporary subset held only these three original items plus root manifests and notices. Its audit
was clean. The pure local distribution builder produced the index, three archives and SHA256SUMS in
the proof workspace; it published nothing and included no existing board.

The proof ran reviewed get from those local assets with --offline, then direct-authored and vendored
builds and a frozen dry run. Socket and subprocess creation were blocked throughout get/build.
All three literal version/tree/index pins were retained after build, and LICENSE/NOTICE were copied.
The native used symbol/footprint files, board model and circuit connectivity equal the direct-record
build. The builds reported only circuit.policy-missing and circuit.value-unknown informational findings;
they supply no electrical-policy, oracle or manufacturing proof.

```sh
fenolite get device FenoliteDevices:IllustrativeResistor --from LOCAL_ASSETS \
  --script design.py --offline --dry-run --json
# Review the plan, then confirm its exact plan_id before building:
fenolite get device FenoliteDevices:IllustrativeResistor --from LOCAL_ASSETS \
  --script design.py --offline --confirm --plan PLAN_ID --json
fenolite build design.py --out out --frozen --dry-run --json
```

LOCAL_ASSETS and PLAN_ID name the temporary authored-only proof assets and reviewed plan. The full
repository still has the 38 existing board audit errors and cannot produce an audited public release.
The public workflow tool pin lacks newer commands and the source-register fix; actual branch CI, reviewed records, any external
seed and a published release/tag remain open.

## Official image research

The [official KiCad Docker overview](https://hub.docker.com/r/kicad/kicad) documents version-specific
release tags. Docker Hub's [9.0.2-amd64 manifest page](https://hub.docker.com/layers/kicad/kicad/9.0.2-amd64/images/sha256-8a43a0dd03e56d428cc516e2a1bd106260ef2c572288f995af67970d900cf607?tab=layers)
identifies linux/amd64 and manifest sha256:8a43a0dd03e56d428cc516e2a1bd106260ef2c572288f995af67970d900cf607.
The pinned immutable ref is docker.io/kicad/kicad@sha256:8a43a0dd03e56d428cc516e2a1bd106260ef2c572288f995af67970d900cf607.

The root worker fetched the public registry manifest and confirmed that its body SHA-256 and
Docker-Content-Digest both equal that digest, with linux/amd64 configuration. Its verification receipt
was checked here against the official page's digest, architecture and explicit cli_executed=false.
This read-only registry evidence is registered as D-0004, and
the root-authorised official digest is now tools.kicad_image. No image was pulled or executed here,
and no Dockerfile implementation was read. Actual CLI-version execution remains unproved and is
required by the installer job before replay/proof/render. The multiarch tag metadata
endpoint is https://hub.docker.com/v2/repositories/kicad/kicad/tags/9.0.2 and the registry manifest
endpoint is https://registry-1.docker.io/v2/kicad/kicad/manifests/9.0.2. The root worker owns the actual
expected-version CLI run; a verified manifest identity is not a runtime or fidelity proof.
