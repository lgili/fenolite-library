# Library infrastructure

The first-boards branch holds conversions but lacks the repository metadata and checks required by
Fenolite changes c0279, c0273 and c0266. Prepare that infrastructure without changing existing board
payloads, conversion records, accepted differences or proof reports.

Add licence and contribution rules, a public immutable core tool pin, separate CI checks, deferred
release/gallery workflows and a small original CC0 block package. Publication, releases, tags and
pull requests remain outside this local change. Actual branch CI replaces the proposed PR proof;
it remains pending until publication and a suitable public core feature pin are available.
