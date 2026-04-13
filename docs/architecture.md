# Architecture

## Architectural posture

Control Plane Framework is organized around a separation between workflow and tooling.

The framework does not assume that a single model, interface, or vendor should drive all development work. Instead, it provides a stable repository-level operating structure that can coordinate planning, governance, execution, and validation across changing tools.

## Primary layers

### 1. Protocol layer
The protocol layer defines workflow posture, expectations, and control assumptions. In this repository, that guidance is documented in `docs/protocols/genesis-omni-2.7.md`.

### 2. Framework layer
The framework layer contains reusable templates and structures that make the control plane operational for a new project.

### 3. Project layer
The project layer is the forked implementation repository where product-specific planning, code, tasks, and validation artifacts are created.

## Lane model

### Planning lane
Responsible for project intent and direction.

Includes:
- mission
- product brief
- roadmap
- backlog

### Governance lane
Responsible for decision boundaries and control rules.

Includes:
- priorities
- constraints
- review gates
- operating rules

### Execution lane
Responsible for implementation-facing work.

Includes:
- tasks
- implementation plan
- change records

### Validation lane
Responsible for determining whether a change or milestone is acceptable.

Includes:
- test plan
- audit notes
- acceptance criteria

## Design assumptions

- The repository is part of the control system.
- Planning should exist before major execution begins.
- Governance should be explicit and reviewable.
- AI tools should support the workflow, not replace it.
- Tool choice should remain interchangeable when possible.
- Human review should remain present at important decision points.

## Operational consequence

A project forked from this framework inherits a reusable control-plane structure. That makes it easier to start new work with a stable operating model rather than rebuilding structure project by project.
