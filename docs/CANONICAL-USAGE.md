# Canonical Usage Guide

## Purpose

This document defines the authoritative usage path for Control Plane Framework.

## Canonical control-plane path

Use the following artifacts as the current authoritative control-plane system:

- `docs/protocols/PROTOCOL-LAYER.md`
- `docs/protocols/genesis-omni/canonical-genesis-omni-2.7-st.md`
- `framework/FRAMEWORK-CONTRACT.yaml`
- `framework/STATE-MODEL.yaml`
- `framework/DEPENDENCY-GRAPH.yaml`
- `framework/ARTIFACT-REGISTRY.yaml`
- `framework/SCHEMAS/artifact-metadata.schema.yaml`
- `scripts/validate_framework_v4.py`

## Canonical templates

Use `*.template.v2.md` files as the active template system.

These templates include machine-readable metadata and are the basis for artifact validation and dependency resolution.

## Legacy artifacts

Legacy files may remain in the repository for transition compatibility, but they are not the canonical control-plane path.

Legacy examples include:

- `docs/protocols/genesis-omni-2.7.md`
- legacy `*.template.md` files without metadata

## Validation entry point

The strongest repository-level validator is:

- `scripts/validate_framework_v4.py`

## Reviewer guidance

If you are evaluating whether this repository functions as a real control plane, inspect the following in order:

1. Protocol layer
2. Framework contract
3. State model
4. Dependency graph
5. Artifact registry
6. V2 templates
7. Validation engine v4
8. Example project chain under `examples/real-project/`
