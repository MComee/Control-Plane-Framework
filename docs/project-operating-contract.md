# Project Operating Contract

## Purpose

Define the minimum required control structure for any project initialized from Control Plane Framework.

This contract exists to ensure that the framework governs not only itself, but also the actual planning, decomposition, prioritization, and execution flow of the software project being built with it.

The goal is to prevent planning drift, preserve project vision, keep decomposition durable, and provide a human-reviewable, machine-consumable active work handoff for implementation tools.

---

## Core Principle

A project created from this framework is not considered operationally initialized until it has:

* a protected core vision
* modular planning artifacts derived from that vision
* atomic task artifacts derived from those modules
* explicit priority state
* a single authoritative active work handoff
* evidence locations for validation and repair continuity

---

## Required Project Workspace

Each initialized project must contain a canonical project workspace:

`projects/<project-name>/`

Inside that workspace, the following top-level directories are required:

* `vision/`
* `docs/`
* `now/`
* `evidence/`

An application or implementation directory such as `app/`, `src/`, or another stack-appropriate location may also exist inside the project workspace, but it does not replace the required control directories.

---

## Required Minimum Structure

The framework requires the following minimum structure for each project:

```text
projects/<project-name>/
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
└── evidence/
    ├── run_logs/
    ├── test_runs/
    └── artifacts/
```

Additional directories may be added per project needs, but these minimum control artifacts should not be omitted.

---

## Protected Vision Rule

`vision/core_vision.md` is the canonical source of project intent.

It must be preserved and treated as a protected doctrine file.

Rules:

* only Planning lane may materially change `vision/core_vision.md`
* Execution lane may reference it but must not silently rewrite it
* Validation lane may assess alignment to it but must not redefine it
* Governance lane may impose constraints on how it is executed, but must not mutate it by accident

Changes to the core vision should be explicit, reviewable, and intentional.

---

## Vision Distillation Rule

The project vision must be decomposed into durable planning artifacts.

That means:

* broad capabilities or workstreams should be represented as module files in `docs/modules/`
* those modules should be further decomposed into atomic or bounded task files in `docs/tasks/`
* tasks should remain traceable back to modules and, where possible, back to the core vision

The goal is to keep planning context from being lost between sessions and to reduce drift during AI-assisted work.

---

## Priority Rule

Each project must maintain explicit priority state in `docs/priorities/`.

Minimum required states:

* `now.md`
* `next.md`
* `later.md`
* `blocked.md`
* `done.md`

These files represent project planning state, not the exact machine-consumable execution handoff.

The priority layer exists to preserve project-level sequencing and decision continuity.

---

## Active Work Rule

Each project must contain a single authoritative active work handoff under:

* `now/description.md`
* `now/prompt.md`
* `now/metadata.json`

These files define the exact current work item for execution.

### `now/description.md`

Human-readable explanation of:

* what happens next
* why it matters
* what successful completion looks like
* major constraints or risks

### `now/prompt.md`

Machine-consumable handoff prompt for the active implementation step.

### `now/metadata.json`

Structured metadata for the active work item, such as:

* lane
* task id
* status
* allowed paths
* forbidden paths
* validation requirements
* dependencies
* supersession state

Only one authoritative active work package should exist at a time for a given project unless the project intentionally supports parallel execution tracks.

---

## Planning Synchronization Rule

Planning must not live only in chat memory.

Every planning session that materially changes project understanding should update the repository artifacts that carry project truth.

At minimum, when planning changes occur, update all affected:

* `vision/` files if project intent changes
* module files if decomposition changes
* task files if execution understanding changes
* priority files if sequencing changes
* active work handoff files if the immediate next step changes

This is mandatory because repository state should remain the durable control surface.

---

## Atomic Task Rule

Task files under `docs/tasks/` should be bounded and reviewable.

Each task file should include, at minimum:

* task id
* title
* parent module(s)
* purpose
* dependencies
* allowed scope
* completion criteria
* validation expectations
* evidence expectations
* status

The framework does not force one exact wording style, but it does require that tasks remain actionable, reviewable, and traceable.

---

## Tool Handoff Rule

The framework must support multiple execution environments, including:

* command-line AI tools
* IDE-integrated chat or assistant tools
* API-based or custom orchestration tools

The framework should not assume one model or one interface.

Instead, the canonical active work package under `now/` is the source of truth.

Tool-specific prompts or handoff artifacts should be derived from that source, not invented ad hoc.

---

## Human Review Rule

Before implementation execution begins, the developer or operator should be able to review:

* the active work description
* the exact active prompt
* the scope and constraints in metadata

This preserves human control and makes the system safer and easier to audit.

---

## Evidence Rule

Every project must preserve validation continuity.

Execution outcomes should be captured under:

* `evidence/run_logs/`
* `evidence/test_runs/`
* `evidence/artifacts/`

The exact evidence format can vary by project, but the locations must exist and the habit of evidence return must be preserved.

---

## Project Initialization Standard

A newly forked or derived project from this framework should not be considered fully initialized until:

1. project workspace exists
2. protected core vision exists
3. module decomposition has started
4. initial task breakdown exists
5. priority files exist
6. active work handoff files exist
7. evidence directories exist

Until those are in place, the framework is only partially instantiated for the project.

---

## Bottom Line

Control Plane Framework should govern more than repository posture.

It should govern the durable project operating structure required to preserve vision, reduce drift, decompose work, prioritize execution, and hand implementation off to tools in a controlled, reviewable way.
