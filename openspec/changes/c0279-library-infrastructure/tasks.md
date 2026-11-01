# Tasks

- [x] 1. Read guidance, refs and the c0279/c0273/c0266 external contracts; record base and decisions.
  Proof: inspect git refs and strict OpenSpec validation.
  Passed 2026-11-01: first-boards 2cdbe73bf3069d22b1959f01cac087f6dbb6cc49; no AGENTS.md;
  older setup d7e887d7 supplies root metadata only. Strict validation valid without warnings.
- [x] 2. Add root licence/use statements, manifests, DCO contribution rules and CODEOWNERS.
  Proof: audit root and compare the shipped licence list; record existing board blockers.
  Passed root checks 2026-11-01: the licence list is byte-identical to local core 5d8afc2f.
  Root audit exits 5 with 38 existing board findings (23 provenance, 12 proof, 2 licence-text,
  1 family mismatch); no README/root finding remains. Board files are unchanged.
- [x] 3. Author one original CC0 block with usage/tests/golden and canonical record.
  Proof: blocks index --check and blocks test with an explicitly identified sibling feature checkout.
  Passed 2026-11-01 with local core 5d8afc2f: index --check exits 0, usage and two connectivity
  tests pass, reviewed golden is equal, and audit --item exits 0. Public-pin/branch CI remains pending.
- [x] 4. Add independent check, benchmark, release and gallery workflows with immutable tool selection.
  Proof: parse workflows, inspect capability guards and validate shell snippets; record unavailable jobs.
  Passed 2026-11-01: five YAML files parse, shell blocks pass bash -n and 19 Python heredocs compile.
  Public capability guard refuses the four missing feature commands. Clean block core 5d8afc2f and
  clean device core 2c9afd54 each pass their own capability subset; no combined feature proof is claimed.
  The exact block workflow body passes. File/socket/process negative controls are refused. Image
  metadata accepts the root-verified digest and rejects a blank negative control; CLI execution
  remains required and unrun here. Publication switches and board concurrency limits are checked.
  This is local source/probe validation, not actionlint or actual GitHub CI; see docs/validation.md.
- [x] 5. Record local proofs/blockers, compare board bytes, and make an exact user-signed local commit.
  Proof: focused checks, git diff --check, unchanged boards and clean status after commit.
  Passed 2026-11-01: final clean-core block/index/item-audit proofs, licence-copy test, capability and
  import controls, ruff/format and strict validation pass. Existing board tree remains
  15fa5f749fbeb0a4a020b947d4f2a6f2bf5c55b7. Signed local commit and clean status verified; no push,
  PR, tag, release, Pages deployment, new third-party conversion or board-proof edit was performed.
- [ ] 6. Publish only when root authorises it; confirm actual cac branch CI on the exact public tool pin.
  Pending: root owns publication; no PR, tag, release or Pages deployment is authorised now.
