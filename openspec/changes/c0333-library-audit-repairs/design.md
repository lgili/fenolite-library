# Scoped factual repairs and real replay

Read CONTRIBUTING.md, POLICY.md and the closed licence registry first. The current 32 audit findings
include seven raw-versus-normalised licence-hash mistakes whose existing text is already approved.
Correct those factual hashes while preserving LICENSE, all payloads and fidelity bytes. Record a patch
metadata version and dated notice without dropping the original notice. The first iteration must show
exactly those seven findings disappear and every other finding remains unchanged.

Treat family/path and logical-id corrections separately. Upstream paths keep their original case and
immutable URLs; only library identity/path is canonicalised. Preserve every payload byte.

The Apache tiny_tapeout, CC-BY-SA OpenAir and CERN RoyalBlue licence texts have been checked byte-for-byte against
KiCad's official mirror at the recorded commit. The actual CODEOWNER decisions are recorded separately for the first two texts and RoyalBlue; no approval is inferred.

Fresh board replacements require actual dry-run/plan/confirm import, default complete fidelity proof,
recorded provenance and portable replay. Diagnostic snapshots are immutable and explicitly not final
validation. No private paths, new runtime dependency, copied parser implementation or official KiCad
library material enters the core. Keep unsuccessful proofs and source-owner blockers visible.

## KiCad10 replay CI pin

Derived padvia proofs require actual KiCad10; the historical9.0.2 library container pin cannot execute that contract. Review the official kicad/kicad10.0.6 immutable digest already selected by the core, verify registry body/header digests and linux/amd64 descriptor/config metadata without claiming executed version. A corresponding actual container `kicad-cli version` must still pass locally or in the existing CI action's exact version gate. Preserve the old9pin as historical observation and retain the public core SHA until root supplies its validated public replacement. No publication or CI-green claim follows from metadata preparation.
