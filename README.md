# Control Plane Framework

A reusable control-plane framework for governed AI-assisted software development.

Control Plane Framework is a model-agnostic repository framework for planning, governing, executing, and validating software work across chat-based and command-line AI tooling.

It is designed for developers who do not want to rebuild process, workflow structure, and repository conventions from scratch for every new project. Instead, the framework provides a repeatable control layer that can be forked and adapted per project.

## Start Here

If you are evaluating the framework or preparing to fork it for a new project, use this reading order:

- [Start Here](docs/start-here.md)
- [Overview](docs/overview.md)
- [Architecture](docs/architecture.md)
- [Tool Selection](docs/tool-selection.md)
- [Repository Governance](docs/repository-governance.md)
- [Forking Pattern](docs/forking-pattern.md)
- [Use Cases](docs/use-cases.md)
- [Framework Diagram](docs/diagram.md)
- [Genesis Omni 2.7 Protocol](docs/protocols/genesis-omni-2.7.md)

## Purpose

This framework treats the repository as part of the project's control system, not only as a code container.

It is structured to support:

- planning before implementation
- explicit governance and prioritization
- controlled execution workflows
- validation before acceptance
- reusable project initialization patterns
- model-agnostic AI-assisted development

## What problem it solves

Many projects begin with implementation-first workflows and only later attempt to organize planning, constraints, quality gates, and review practices. That often creates drift, rework, unclear priorities, and inconsistent execution.

In AI-assisted development, drift becomes more pronounced when multiple tools are used without a unifying workflow.

Control Plane Framework addresses this by providing:

- a reusable repository structure for new projects
- predefined lanes for planning, governance, execution, and validation
- templates that standardize project startup and iteration
- a protocol layer for workflow discipline and control expectations
- a model-agnostic structure that remains stable when tools change
- a required single-project operating structure that preserves vision, decomposition, priorities, and active execution handoff

## Layered control model

Each derived repository instance controls exactly one project and operates three layers:

### 1. Framework self-governance

The framework governs itself and preserves doctrine, anti-drift rules, and reusable control patterns.

### 2. Project control

The repository governs one controlled project under `project/`, including:

- protected vision
- feature-level decomposition
- task-group decomposition
- atomic tasks
- explicit priorities
- active work state
- evidence continuity

### 3. Execution handoff

The active work package under `project/now/` is the canonical bridge from planning truth to implementation execution.

Tool-specific prompts or adapter instructions should be derived from that package so execution remains bounded and auditable across interfaces.

See:

- [Project Operating Contract](docs/project-operating-contract.md)
- [Project Initialization Standard](docs/project-initialization-standard.md)
- [Planning Synchronization Rule](docs/planning-synchronization-rule.md)
- [Active Work Handoff](docs/active-work-handoff.md)

## Control Routing Model

When an AI tool connects to this repository, it should route by phase:

1. Read `README.md`.
2. Determine current phase:
- Planning
- Execution Prep
- Execution
- Validation
3. Follow phase-specific control paths.

### Planning

Read and synchronize:

- `project/vision/`
- `project/docs/features/`
- `project/docs/task_groups/`
- `project/docs/tasks/`
- `project/docs/priorities/`

### Execution Prep

Use the active-work package:

- `project/now/description.md`
- `project/now/prompt.md`
- `project/now/metadata.json`

### Execution

Modify only allowed execution paths for the current task.

### Validation

Verify:

- no protected files changed
- output matches the active prompt
- evidence exists in required evidence paths

## Project Control Structure

A derived repository is operationally initialized when it instantiates one controlled project workspace at `project/`.

Minimum project control structure:

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

## Recommended repository posture

This repository is intended to remain a clean, reusable public framework.

Recommended posture:

- keep `main` protected and reviewed
- make changes through branches and pull requests
- require owner review before merge
- use private forks or derivative repositories for product-specific implementation work

See:

- [Repository Governance](docs/repository-governance.md)
- [.github/CODEOWNERS](.github/CODEOWNERS)

## Example use cases

Control Plane Framework is designed for:

- private application development
- internal tooling
- CLI tools
- research and experimentation
- multi-model workflows that combine chat-based and command-line AI tools

See [Use Cases](docs/use-cases.md) for details.

## Repository layout

```text
.
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── docs/
│   ├── start-here.md
│   ├── overview.md
│   ├── architecture.md
│   ├── quickstart.md
│   ├── tool-selection.md
│   ├── repository-governance.md
│   ├── forking-pattern.md
│   ├── use-cases.md
│   ├── diagram.md
│   ├── project-operating-contract.md
│   ├── project-initialization-standard.md
│   ├── planning-synchronization-rule.md
│   ├── active-work-handoff.md
│   └── protocols/
│       └── genesis-omni-2.7.md
├── examples/
│   └── sample-project-brief.md
├── framework/
│   ├── planning/
│   │   └── project-template/
│   │       ├── README.md
│   │       └── project/
│   │           ├── vision/
│   │           │   ├── core_vision.md
│   │           │   ├── constraints.md
│   │           │   └── brainstorming.md
│   │           ├── docs/
│   │           │   ├── features/
│   │           │   │   └── README.md
│   │           │   ├── task_groups/
│   │           │   │   └── README.md
│   │           │   ├── tasks/
│   │           │   │   └── README.md
│   │           │   ├── priorities/
│   │           │   │   ├── now.md
│   │           │   │   ├── next.md
│   │           │   │   ├── later.md
│   │           │   │   ├── blocked.md
│   │           │   │   └── done.md
│   │           │   ├── roadmap.md
│   │           │   ├── decisions.md
│   │           │   ├── definition_of_done.md
│   │           │   └── execution_control.md
│   │           ├── now/
│   │           │   ├── description.md
│   │           │   ├── prompt.md
│   │           │   └── metadata.json
│   │           ├── evidence/
│   │           │   ├── run_logs/
│   │           │   ├── test_runs/
│   │           │   └── artifacts/
│   │           └── app/
│   │               └── README.md
│   ├── governance/
│   ├── execution/
│   └── validation/
└── .github/
    ├── CODEOWNERS
    ├── ISSUE_TEMPLATE/
    └── PULL_REQUEST_TEMPLATE.md
```
