# Contributing

Each commit must carry one Signed-off-by trailer certifying the Developer Certificate of Origin 1.1:
https://developercertificate.org/ . Use git commit -s.

Follow POLICY.md and licences.toml. An item needs its upstream URL and immutable commit, licence,
authors, original notices, a dated modification notice and reproducible conversion steps.
No employer or private material, unlicensed work, NC/ND terms or platform-restricted sources enter.
The root CC0 licence applies only to repository-authored files; never replace an item's licence.

Run fenolite library audit . --json before publishing changes. Review all licence and provenance
findings. Converted boards need a fidelity proof or explicit accepted differences; never invent a
passing proof. Keep third-party payloads in this repository, separate from the Fenolite tool.

Use the five plural kind folders, then the licence family and literal namespace/name path. Record
one item version in item.json and PROVENANCE.json; retain every original notice. Generated files
must match their source records and conversion steps. Never edit a proof report to remove a failure.
The closed machine-readable allow-list is licences.toml; the root CC0 dedication cannot relicense
upstream material. A new licence-text digest requires documented CODEOWNERS review.

Blocks export exactly one BlockDef in __all__, hold canonical block.json and executes=true, and
include usage/<name>.py, tests/test_<name>.py and golden/<name>.json. Indexing and tests execute
package code explicitly; static discovery must not. Keep imports free of network and write effects.
Run `fenolite blocks index blocks/<family>/<namespace>/<name> --check --json` and
`fenolite blocks test <namespace>:<name> --from blocks/<family>/<namespace>/<name>/__init__.py --json`.

For device records, register public facts with D- ids in sources.toml. Check generated outputs and
old/new review sheets. Seeding a CC0 library is a conversion step, not validation: seeded records
remain UNVERIFIED unless a person inspects and accepts the current sheet and source mappings.
Commit generated symbol/footprint outputs below each item's generated/ folder, list them in item.json,
and reproduce them with `library symbol` or `library generate` before contribution. CI compares the
planned output digests with those files; it never silently rewrites them.

CI checks cac/** branches as well as contributions. This preparation authorises no pull request,
tag or release. The release and Pages workflows use protected environments and must be invoked
only under a maintainer's separate publication instruction. Their presence is not a release proof.
