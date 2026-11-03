# Repair the remaining library audit findings

The maintainer requested completion of the remaining CAC library work. The current root audit has
32 findings after the independently proved Video/Sonde refresh. This change covers the other items,
with separate factual metadata repairs, actual fresh conversion/proof work and final branch validation.
It does not expand c0282's historical four-item measurements or turn historical failures into passes.

Preserve original source terms, payloads and generated proof bytes unless real, reviewed commands
justify their replacement. Never invent accepted differences or skipped-level reasons. Register a new
licence-text digest only after a real documented CODEOWNER approval. Keep the public tool pin until
root supplies a published validated source. Root owns push, CI, integration and later cleanup.
