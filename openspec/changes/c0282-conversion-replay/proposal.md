# Recheck four converted boards after the core geometry integration

The existing ECC83, sonde xilinx, video and Coldfire kit items were converted with an older core and
carry historical accepted differences and incomplete proof metadata. Rerun their original recorded
inputs and CLI recipes with exact core b02e09fea8145442f0af61f571e58a075385df9e, measure current
differences and compare the twelve original issues plus later entries 13–14.

Only actual generated conversion payloads, conversion/proof/provenance/item records and measured
status are updated. Preserve upstream licences and notices, do not create new accepted differences,
and keep unperformed KiCad/CI/publication gates open. No CAD enters the Fenolite core repository.

No push, pull request, tag, release or protected-branch action is authorised by this change.
