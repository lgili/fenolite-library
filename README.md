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

The repository's own documentation and configuration are licensed under CC0-1.0.
This licence does not cover the items: each item retains its upstream licence and notices.
Items are test and benchmark inputs. No item is used for machine-learning training.

See CONTRIBUTING.md for provenance review and contribution requirements.
