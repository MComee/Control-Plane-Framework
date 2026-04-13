# Genesis Omni Protocol Index

This directory contains the complete Genesis Omni protocol layer for Control Plane Framework.

## Files

- `canonical-genesis-omni-2.7-st.md` — authoritative local copy of the Genesis Omni 2.7 ST protocol
- `framework-adoption.md` — defines how Control Plane Framework adopts and applies the protocol
- `protocol-status.md` — declares authority, lineage, stability, and inheritance rules

## Why this exists

Control Plane Framework previously referenced Genesis Omni at a high level without embedding the full governing protocol artifact in the framework itself.

This directory corrects that gap by making the protocol layer explicit, self-contained, and versioned.

## Reading order

1. `canonical-genesis-omni-2.7-st.md`
2. `framework-adoption.md`
3. `protocol-status.md`

## Role in the control structure

The protocol layer is part of the control structure of Control Plane Framework.

It defines:

- reasoning posture
- decomposition expectations
- validation and falsification expectations
- command semantics
- inheritance expectations for downstream projects
