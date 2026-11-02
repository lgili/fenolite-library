# Two passing converted items — 2026-11-02

Video and sonde_xilinx are refreshed to item version 1.0.1 using signed core
`de6c6f2f4dd53cdda45b4119f63822b5bd3ea6eb` (Fenolite 0.7.0.dev0).
The [machine receipt](item-refresh-maintainer-host.json) binds the measured
proofs, replay trees, immutable upstream revision and audit counts.

Both fresh default proofs compare all levels 1–8 and S equal, with zero
accepted differences. The proof records were produced by actual reviewed
`verify-source --record` plans and exact-ID confirmations; no result was edited.
The packaged PROVENANCE import record retains that exact generated record,
including its fidelity member. Video has 116 declared payload files and Sonde 27.

Each portable two-step recipe was executed with `library replay --with-current`
against the original recorded upstream. Both steps exit 0 and the resulting
output tree equals the packaged declared payload tree. The record step uses
`--no-backup` for newly generated scratch provenance: an initial replay correctly
failed when an undeclared `.bak` appeared. The strict output-tree check remains.
The Video confirmation completed and its reviewed output digest was checked;
a later harness assertion failed on an omitted empty `accepted` member. The
raw confirmation reply was not saved. Resume validation checked the actual
record against the saved real plan and all nine results without repeating or
inventing the confirmation. Sonde's raw confirmation reply was saved normally.

The original 24 native inputs plus LICENSE were independently fetched through
the official KiCad GitHub mirror at recorded revision
`97acc80c223d75520c03fc44cab63cd9a3202c42`: all 25 byte digests match.
Original LICENSE bytes remain unchanged and each old NOTICE remains a verbatim
suffix beneath a dated conversion notice. Attribution, SPDX, source revision
and UNVERIFIED evidence are retained. Licence metadata now uses the measured
normalised digest already approved in licences.toml; no new digest is added.

The actual root audit has 32 findings (previously 38): 19 provenance, 10 failed
proof, two licence-text and one family mismatch. Neither selected item has a
finding; the multiset of all other findings is exactly unchanged. The separate
private-list residue scan reports four existing absolute-path findings in four
untouched OpenAir footprint files. These are retained blockers, not waivers.
The private-list staged scan passes with zero hits in 53 changed files.

ECC83 still has a measured presentation difference: six visible schematic
Footprint fields refer to official library namespaces while its board uses the
local Footprints namespace. Coldfire explicitly refuses unsupported visible
bold text. Neither result is accepted or promoted to passing here. The earlier
[maintainer-host diagnostic](conversion-replay-maintainer-host.md), L10 and
older reports remain historical evidence of their measured sources.

The public tool pin is unchanged. No native GUI success, complete root audit,
exact-head CI, final model-0 capture, model-1 activation, push or release is
claimed by these two local item refreshes.
