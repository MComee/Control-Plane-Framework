# Genesis Omni Protocol Status

## Authority

The canonical Genesis Omni 2.7 ST document located in:

`docs/protocols/genesis-omni/canonical-genesis-omni-2.7-st.md`

is the authoritative protocol artifact within Control Plane Framework.

## Source lineage

- Original origin: TerminalGuru repository
- Imported into this repository to eliminate external dependency on protocol definition

## Status

- Version: 2.7-ST
- Stability: Treated as stable unless superseded by a formally versioned update

## Modification policy

- Direct edits to the canonical protocol should be avoided
- Changes should occur through versioned upgrades (e.g., 2.8, 3.0)
- Framework-specific interpretation belongs in separate documents (see framework-adoption.md)

## Inheritance rules

Forked repositories:

- SHOULD inherit this protocol
- MAY extend it with project-specific constraints
- MUST NOT silently contradict core mandates (zero-assumption, falsification, VTE, etc.)

## Rationale

This file exists to ensure that Control Plane Framework is:

- self-contained
- internally consistent
- not dependent on external repositories for its core operating doctrine
