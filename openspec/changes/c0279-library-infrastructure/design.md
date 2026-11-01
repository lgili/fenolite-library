# Design

Entry 2026-11-01: base origin/first-boards at 2cdbe73bf3069d22b1959f01cac087f6dbb6cc49.
No AGENTS.md exists in this checkout. POLICY.md and the c0279/c0273/c0266 contracts were read.
The older cac/c0279-library-setup branch has root metadata but also board changes; reuse only the
root legal text and author-authored contribution rules, and leave every existing board byte intact.

Decided 2026-11-01: repository-owned files and the new original block are CC0-1.0. The root licence
does not cover independently licensed items. The allow-list stays byte-identical to the pinned core.
The authored item's dedication is recorded explicitly; no third-party design or parser is copied.

Decided 2026-11-01: library.toml holds one exact public Fenolite commit. Workflows install that
commit and reject unavailable capabilities. A future feature-pin update changes this single field
and synchronises the shipped licence table when it differs;
no moving development branch or unpublished commit is presented as a working dependency.

Decided 2026-11-01: validation runs on cac/** pushes and manual dispatch, with PR support for future
contributions. No workflow creates a PR, tag or release. Release and Pages publishing require an
existing authorised release/tag and protected environment approval; local preparation does neither.

Decided 2026-11-01: use independent audit, records, blocks, replay and proof jobs so a missing new
command or an existing board failure stays visible. A nonblocking benchmark preserves every failure
in its report. Render artefacts support review and never change evidence labels or accepted differences.

Decided 2026-11-01: local checks may use an explicitly selected sibling core checkout in an isolated
venv. Record its commit separately from the public workflow pin. Never commit machine-specific paths.
Existing board audit/replay/proof failures remain blockers until the authorised core integration passes.
