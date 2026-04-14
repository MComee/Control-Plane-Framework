# Project Operating Contract

## Purpose

Define the minimum required control structure for the single controlled project initialized from Control Plane Framework.

This contract ensures the framework governs not only itself, but also the planning, decomposition, prioritization, and execution flow of the one software project being built in a derived repository.

The goal is to prevent planning drift, preserve project vision, keep decomposition durable, and provide a human-reviewable, machine-consumable active-work handoff for execution tools.

---

## Layer relationship

Control Plane Framework in a derived repository should be operated as:

1. framework self-governance layer
2. project control layer
3. execution handoff layer

This document defines the project control layer and its interface to execution handoff.

---

## Core Principle

A derived repository is not operationally initialized until it has:

- one canonical controlled project workspace at `project/`
- a protected core vision
- modular planning artifacts derived from that vision
- atomic task artifacts derived from those modules
- explicit priority state
- a single authoritative active-work package
- evidence locations for validation and repair continuity

---

## Required Project Workspace

The controlled project workspace is:

`project/`

Inside that workspace, the following top-level directories are required:

- `vision/`
- `docs/`
- `now/`
- `evidence/`

An implementation directory such as `app/`, `src/`, or another stack-appropriate location may also exist inside `project/`, but it does not replace the required control directories.

---

## Required Minimum Structure

```text
project/
├── vision/
│   ├── core_vision.md
│   ├── constraints.md
│   └── brainstorming.md
├── docs/
│   ├── modules/
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

Additional directories may be added per project needs, but these control artifacts should not be omitted.

---

## Protected Vision Rule

`project/vision/core_vision.md` is the canonical source of project intent.

It is a protected doctrine file.

Rules:

- only Planning lane may materially change `project/vision/core_vision.md`
- Execution lane may reference it but must not silently rewrite it
- Validation lane may assess alignment to it but must not redefine it
- Governance lane may impose constraints on how it is executed, but must not mutate it by accident

Changes to the core vision should be explicit, reviewable, and intentional.

---

## Vision Distillation Rule

The project vision must be decomposed into durable planning artifacts:

- broad capabilities or workstreams should be represented in `project/docs/modules/`
- modules should be decomposed into bounded task files in `project/docs/tasks/`
- tasks should remain traceable back to modules and, where possible, back to the core vision

This keeps planning context durable between sessions and reduces drift during AI-assisted work.

---

## Priority Rule

The project must maintain explicit priority state in `project/docs/priorities/`.

Minimum required states:

- `now.md`
- `next.md`
- `later.md`
- `blocked.md`
- `done.md`

These files represent planning state, not the machine-consumable active handoff.

---

## Active Work Rule

The project must contain one authoritative active-work package under:

- `project/now/description.md`
- `project/now/prompt.md`
- `project/now/metadata.json`

This package defines the exact current work item for execution.

### `project/now/description.md`

Human-readable explanation of:

- what happens next
- why it matters
- what successful completion looks like
- major constraints or risks

### `project/now/prompt.md`

Machine-consumable handoff prompt for the active implementation step.

### `project/now/metadata.json`

Structured metadata for the active work item, such as:

- lane
- task id
- status
- allowed paths
- forbidden paths
- validation requirements
- dependencies
- supersession state

Only one authoritative active-work package should exist at a time for the project unless parallel execution tracks are explicitly defined.

---

## Planning Synchronization Rule

Planning must not live only in chat memory.

Every planning session that materially changes project understanding should update the repository artifacts that carry project truth.

At minimum, update all affected artifacts in `project/vision/`, `project/docs/`, and `project/now/`.

---

## Atomic Task Rule

Task files under `project/docs/tasks/` should be bounded and reviewable.

Each task file should include, at minimum:

- task id
- title
- parent module(s)
- purpose
- dependencies
- allowed scope
- completion criteria
- validation expectations
- evidence expectations
- status

---

## Tool Handoff Rule

The execution handoff layer must support multiple execution environments, including:

- command-line AI tools
- IDE-integrated assistants
- API-based or custom orchestrators

The framework should not assume one model or interface.

Instead, the canonical active-work package under `project/now/` is the source of truth.

Tool-specific prompts or handoff artifacts should be derived from that source, not invented ad hoc.

---

## Human Review Rule

Before implementation begins, the operator should be able to review:

- `project/now/description.md`
- `project/now/prompt.md`
- `project/now/metadata.json`

This preserves human control and improves auditability.

---

## Evidence Rule

The project must preserve validation continuity.

Execution outcomes should be captured under:

- `project/evidence/run_logs/`
- `project/evidence/test_runs/`
- `project/evidence/artifacts/`

The exact evidence format can vary by project, but the locations should exist.

---

## Project Initialization Standard

A derived repository should not be considered fully initialized until:

1. `project/` workspace exists
2. protected core vision exists
3. module decomposition has started
4. initial task breakdown exists
5. priority files exist
6. active-work files exist
7. evidence directories exist

---

## Bottom Line

Control Plane Framework should govern more than repository posture.

It should govern the durable single-project operating structure required to preserve vision, reduce drift, prioritize execution, and hand implementation off to tools in a controlled, reviewable way.
