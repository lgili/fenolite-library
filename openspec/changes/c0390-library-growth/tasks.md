# Tasks

- [x] 1. Read the policy, the existing items and the core's generator and audit contracts; write and
  strictly validate this change before any item.
  Proof: `openspec validate c0390-library-growth --strict`.
- [x] 2. Register the datasheets and standards read as D-ids (block D-0390 onward) in one commit.
  Proof: the core's `source_ids` reader accepts `sources.toml`.
- [x] 3. Batch 1: chip resistors, capacitors, inductors and ferrite beads.
  Proof: per item library check, regeneration, review sheet and item audit; one commit.
- [x] 4. Batch 2: molded diode packages (SOD, SMA/SMB/SMC, MiniMELF).
  Proof: as task 3. MiniMELF and PowerDI-123 left out (gap G-2).
- [x] 5. Batch 3: SOT packages.
  Proof: as task 3. SOT-23-3, SOT-523 and SOT-89 left out (gaps G-2, G-3).
- [x] 6. Batch 4: SOIC, SSOP, TSSOP, MSOP.
  Proof: as task 3. SSOP needs a source; SO-8EP waits for gap G-2.
- [x] 7. Batch 5: generic symbols per device class.
  Proof: library check and symbol regeneration per item; item audit.
- [x] 8. Licence register of import candidates, each read in its own repository.
  Proof: a verdict per source with the evidence; unclear sources listed for the maintainer
  (`licence-register.md`).
- [ ] 9. M2 batches 6 to 9 (QFN/DFN/QFP, TO, DIP, headers and sockets).
- [ ] 10. M3 batches 10 to 12 (BGA, terminal blocks, USB, crystals, devices).
- [ ] 11. M4 imports from accepted upstream libraries.
- [ ] 12. Report per batch: family or source, licence, items, proof, commit, open points; no push.

M1 proof (2026-11-04): `families/prove.py` over all 146 items (45 footprints, 101 symbols): 146/146 pass
library check with no finding, item audit, byte-equal regeneration and 292 rendered review sheets.
