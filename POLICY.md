# Policy

## Accepted licences

Only items whose upstream licence explicitly allows modification and redistribution:

- CERN-OHL-P, CERN-OHL-W and CERN-OHL-S (v1.2 and v2)
- CC0-1.0, CC-BY (3.0, 4.0), CC-BY-SA (2.5, 3.0, 4.0)
- MIT, BSD-2-Clause, BSD-3-Clause, Apache-2.0, Solderpad
- GPL-2.0-or-later, GPL-3.0
- TAPR-OHL-1.0

## Never accepted

- items with no licence (all rights reserved);
- non-commercial (NC) or no-derivatives (ND) licences;
- material from platforms whose terms forbid copying, bulk collection or data mining (for example
  EasyEDA/OSHWLab), and examples bundled with commercial EDA tools;
- KiCad's official library files and vendor 3D models (referenced by name only);
- anything taken from an employer or a private project.

## Every item

- one folder `<kind>/<licence-family>/<item>/` holding the item, `LICENSE`, `NOTICE` and `PROVENANCE.json`;
- the upstream notices are kept unchanged; the conversion is recorded as a dated modification;
- share-alike items stay under their licence; nothing is relicensed;
- a converted board enters only with a passing fidelity proof (`fenolite verify-source`), or with each
  difference written down in `PROVENANCE.json`;
- CI regenerates each item from its pinned upstream commit and checks this policy.

## Use

Items are published for people to use and as test and benchmark inputs for Fenolite. Any use for training
machine-learning models is a separate, public decision that respects the authors' licences and
machine-readable opt-outs.

## Marketing

Images of third-party items are renders made by Fenolite, shown with the designer, the licence and a link
to the original. No third-party logo is used, and no wording implies endorsement.

## Contributions

By pull request, with a `Signed-off-by` line (Developer Certificate of Origin) on every commit.
