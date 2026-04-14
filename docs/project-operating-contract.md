# Project Operating Contract

## Purpose

Define the minimum required control structure for the single controlled project in a derived Control Plane Framework repository.

This contract ensures the framework governs both itself and the one project's planning, decomposition, prioritization, and execution handoff.

---

## Layer relationship

Control Plane Framework in a derived repository operates three layers:

1. framework self-governance
2. project control
3. execution handoff

This document defines the project control layer and its execution safety boundaries.

---

## Core Principle

A derived repository is not operationally initialized until it has:

- one canonical project workspace at `project/`
- protected vision artifacts
- feature decomposition
- task-group decomposition
- atomic task artifacts
- explicit priority state
- a single authoritative active-work package
- evidence locations for validation continuity

---

## Required Project Workspace

The controlled project workspace is:

`project/`

Inside that workspace, the following top-level directories are required:

- `vision/`
- `docs/`
- `now/`
- `evidence/`

An implementation directory such as `app/`, `src/`, or another stack-appropriate location may also exist inside `project/`, but it does not replace control directories.

---

## Required Minimum Structure

```text
project/
├── vision/
│   ├── core_vision.md
│   ├── constraints.md
│   └── brainstorming.md
├── docs/
│   ├── features/
│   ├── task_groups/
│   ├── tasks/
│   ├── priorities/
│   │   ├── now.md
│   │   ├── next.md
│   │   ├── later.md
│   │   ├── blocked.md
│   │   └── done.md
│   ├── roadmap.md
│   ├── decisions.md
│   ├── definition_of_done.md
│   └── execution_control.md
├── now/
│   ├── description.md
│   ├── prompt.md
│   └── metadata.json
├── evidence/
│   ├── run_logs/
│   ├── test_runs/
│   └── artifacts/
└── app/
```

---

## Protected Vision Rule

`project/vision/core_vision.md` is the canonical source of project intent and is treated as protected doctrine.

`project/vision/constraints.md` is also protected planning doctrine.

Changes to protected vision artifacts should be explicit, reviewable, and planning-lane controlled.

---

## Vision Distillation Rule

The project vision must be decomposed into durable planning artifacts:

- capabilities should be represented in `project/docs/features/`
- implementation scopes should be represented in `project/docs/task_groups/`
- atomic execution units should be represented in `project/docs/tasks/`
- tasks should trace back to task groups, features, and vision

---

## Priority Rule

The project must maintain explicit priority state in `project/docs/priorities/`:

- `now.md`
- `next.md`
- `later.md`
- `blocked.md`
- `done.md`

These files represent planning state, not direct execution output.

---

## Active Work Rule

The project must contain one authoritative active-work package under:

- `project/now/description.md`
- `project/now/prompt.md`
- `project/now/metadata.json`

This package defines the exact current work item for execution.

---

## Execution Safety Model

Execution and planning are intentionally separated.

Planning controls doctrine and decomposition artifacts. Execution applies bounded implementation changes and returns evidence.

Validation is responsible for enforcing this separation.

### Protected files (must not be modified during execution)

- `project/vision/core_vision.md`
- `project/vision/constraints.md`
- `project/docs/features/*`
- `project/docs/task_groups/*`
- `project/docs/priorities/*`

### Restricted files

- `project/docs/tasks/*` may be updated only when explicitly part of planning or task-tracking updates.

### Allowed execution mutation scope

- `project/app/*`
- `project/evidence/*`
- test and code outputs required by the active task

## Forbidden Mutation Rule

Execution tools must not modify protected files.

Any execution run that mutates protected files is invalid.

The validation layer must detect and reject such runs.

---

## Tool Handoff Rule

Execution handoff must remain tool-agnostic and support:

- command-line AI tools
- IDE-integrated assistants
- API-based or custom orchestrators

The canonical source of truth is `project/now/`.

Tool-specific prompts or adapter payloads should be derived from that source, not invented ad hoc.

---

## Human Review Rule

Before execution begins, the operator should review:

- `project/now/description.md`
- `project/now/prompt.md`
- `project/now/metadata.json`

---

## Evidence Rule

Execution outcomes should be captured under:

- `project/evidence/run_logs/`
- `project/evidence/test_runs/`
- `project/evidence/artifacts/`

---

## Bottom Line

Control Plane Framework governs more than repository posture.

It governs a durable single-project control structure with explicit execution safety boundaries.
