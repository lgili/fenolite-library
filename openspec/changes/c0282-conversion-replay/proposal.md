# Recheck four converted boards after the core geometry integration

The existing ECC83, sonde xilinx, video and Coldfire kit items were converted with an older core and
carry historical accepted differences and incomplete proof metadata. Rerun their original recorded
inputs and CLI recipes with exact core b02e09fea8145442f0af61f571e58a075385df9e, measure current
differences and compare the twelve original issues plus later entries 13–14.

Only actual generated conversion payloads, conversion/proof/provenance/item records and measured
status are updated. Preserve upstream licences and notices, do not create new accepted differences,
and keep unperformed KiCad/CI/publication gates open. No CAD enters the Fenolite core repository.

No push, pull request, tag, release or protected-branch action is authorised by this change.

The 2026-11-01 continuation repeats the same four recorded conversions against the frozen model-0
cut `dbfd6fc36e18300c4a9aef1983f7130fea4e3b71`, verifying its source0 receipt/schema hashes. It records
actual strict import and available full-proof outcomes separately from unchanged existing-payload
baselines. Candidates that fail policy stay in temporary scratch; only measured diagnostics and
issue status enter the repository, with no new accepted difference or public tool-pin update.

The 2026-11-02 L10 continuation uses exact clean model-0 source
`695dee0f1bdf2cff066edad0220c63cf064ae0a2`. It records all four now-unblocked strict imports and
actual default full proofs, including remaining presentation failures. Original item payloads and
acceptances stay unchanged until a candidate really satisfies the library's full proof policy.

The later maintainer-host continuation on signed core de6c6f2f permits replacing
only the actually passing Video and Sonde candidates. Reviewed CLI record plans,
complete zero-acceptance proofs, exact portable replay trees, independently
verified upstream hashes and preserved terms are required. Remaining diagnostics,
the older public tool pin and all native/CI/publication gates stay explicit.
