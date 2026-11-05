# Tasks

- [ ] 1. Read the policy, the existing items and the core's generator and audit contracts; write and
  strictly validate this change before any item.
  Proof: `openspec validate c0390-library-growth --strict`.
- [ ] 2. Register the datasheets and standards read as D-ids (block D-0390 onward) in one commit.
  Proof: the core's `source_ids` reader accepts `sources.toml`.
- [ ] 3. Batch 1: chip resistors, capacitors, inductors and ferrite beads.
  Proof: per item library check, regeneration, review sheet and item audit; one commit.
- [ ] 4. Batch 2: molded diode packages (SOD, SMA/SMB/SMC, MiniMELF).
  Proof: as task 3.
- [ ] 5. Batch 3: SOT packages.
  Proof: as task 3.
- [ ] 6. Batch 4: SOIC, SSOP, TSSOP, MSOP.
  Proof: as task 3.
- [ ] 7. Batch 5: generic symbols per device class.
  Proof: library check and symbol regeneration per item; item audit.
- [ ] 8. Licence register of import candidates, each read in its own repository.
  Proof: a verdict per source with the evidence; unclear sources listed for the maintainer.
- [ ] 9. M2 batches 6 to 9 (QFN/DFN/QFP, TO, DIP, headers and sockets).
- [ ] 10. M3 batches 10 to 12 (BGA, terminal blocks, USB, crystals, devices).
- [ ] 11. M4 imports from accepted upstream libraries.
- [ ] 12. Report per batch: family or source, licence, items, proof, commit, open points; no push.
