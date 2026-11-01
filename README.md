# fenolite-library

Third-party electronics design material converted to [Fenolite](https://github.com/lgili/Fenolite)'s
formats: symbols, footprints, devices, circuit blocks and whole boards (schematic and layout as code).

**Each item keeps its own upstream licence.** This repository is an aggregation of independently licensed
items; there is no single licence for its contents. Every item folder carries:

- `LICENSE`: the upstream licence text;
- `NOTICE`: the upstream copyright and attribution notices, and a dated note of the modifications made
  (the conversion to Fenolite's formats);
- `PROVENANCE.json`: where the item came from (URL and commit), its authors, its SPDX licence id, the
  Fenolite version and steps of the conversion, and the result of the fidelity proof.

The Fenolite tool itself contains no third-party design material. Users pull items from here into their
own projects with `fenolite get <kind> <id>`, which shows the licence before anything is written and copies
the `LICENSE` and `NOTICE` along with the item.

## Layout

```
symbols/<licence-family>/<item>/
footprints/<licence-family>/<item>/
devices/<licence-family>/<item>/
blocks/<licence-family>/<item>/
boards/<licence-family>/<item>/
```

## Rules

See [POLICY.md](POLICY.md): which licences are accepted, what every item must carry, and what is never
accepted.

Names and trademarks of the original projects belong to their owners. Their presence here does not imply
any endorsement of Fenolite.

## Repository licence and use

The repository's own documentation, manifests and workflows are dedicated under
[CC0-1.0](LICENSE). This licence does not cover the items: each directory keeps its upstream licence,
notices and provenance. New original items identify their own licence explicitly.

Items are test and benchmark inputs for Fenolite and starting points for people's projects.
No item is used for machine-learning training.

## Get an item

Use a compatible Fenolite build and review its write plan before confirming it:

```sh
fenolite get block FenoliteBlocks:resistor_link --script design.py --dry-run --json
fenolite get --locked design.py --offline --dry-run --json
```

These commands need a published library release containing the item; this branch creates no release.
The library item pin records the exact release and bytes, separately from the block-instance version.
Builds read vendored files offline. Only an explicit `get` command fetches library items.

## Validate and contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for DCO sign-off, licence and provenance review, and
[reviews/](reviews/) for human device reviews. `library.toml` pins one exact public Fenolite commit.
The [validation status](docs/validation.md) distinguishes local feature-checkout proofs from jobs
blocked by that older public pin and existing board fidelity findings.

```sh
fenolite library audit . --json
fenolite blocks index blocks/cc0/FenoliteBlocks/resistor_link --check --json
```

The new block/check/seed commands require the future validated feature pin. A missing capability
fails its CI job; it is never counted as a passing check. Seeded device records are unverified until
reviewed. Check their licence, source mapping, dimensions and ratings before using them.
