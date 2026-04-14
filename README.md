# Control Plane Framework

A reusable control-plane framework for governed AI-assisted software development.

Control Plane Framework is a model-agnostic repository framework for planning, governing, executing, and validating software work across both chat-based and command-line AI tooling.

It is designed for developers who do not want to rebuild process, workflow structure, and repository conventions from scratch for every new project. Instead, the framework provides a repeatable control layer that can be forked and adapted to new applications, systems, and experiments.

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

This framework treats the repository as more than a code container. It treats the repository as part of the project's control system.

That means the repository is structured to support:

- planning before implementation
- explicit governance and prioritization
- controlled execution workflows
- validation before acceptance
- reusable project initialization patterns
- model-agnostic AI-assisted development

## What problem it solves

Many projects begin with an implementation-first workflow and only later attempt to organize planning, constraints, quality gates, and review practices. That often creates drift, rework, unclear priorities, and inconsistent execution.

In AI-assisted development, the problem becomes more pronounced when multiple tools are used without a unifying workflow. Different models may be strong at different tasks, but without an operating structure, tool switching creates fragmentation rather than leverage.

Control Plane Framework solves this by providing:

- a reusable repository structure for new projects
- predefined lanes for planning, governance, execution, and validation
- templates that standardize project startup and iteration
- a protocol layer for workflow discipline and control expectations
- a model-agnostic structure that remains stable even when tools change
- a required project operating structure that preserves product vision, decomposition, priorities, and active execution handoff

## Model-Agnostic Workflow Orchestration

Control Plane Framework is designed to unify workflows across multiple AI tools rather than enforce reliance on a single model, interface, or vendor.

Modern AI-assisted development often involves both:

- chat-based interfaces for planning, reasoning, decomposition, review, and structured collaboration
- command-line or programmatic tools for implementation, local iteration, file operations, and repository work

This framework provides a structure that allows both to operate within a single governed workflow.

### Multi-Model Strategy

Instead of selecting a single tool for every task, this framework supports a multi-model approach:

- different tools can be used for different classes of work
- tools can be selected based on strengths rather than convenience
- workflows remain consistent even as models and interfaces change

A developer may choose to:

- use one chat-based tool for planning and decomposition
- use another for critique, review, or alternative reasoning
- use a command-line tool or local runtime for implementation and iteration

The framework does not prescribe which tools to use. It assumes that:

- multiple tools may be used in the same project
- different tools may perform better on different problems
- the workflow should remain stable regardless of tool choice

### Integration Expectations

The framework is designed to work with tools that can interact with a repository in a controlled way.

Typical capabilities include:

- reading repository context
- writing or proposing structured file changes
- following prompt or workflow templates
- operating inside defined constraints and review gates

In practice, this may include:

- chat-based AI tools with repository integration
- command-line AI tools operating on a local checkout
- custom or self-hosted interfaces built on top of model APIs and Git workflows

The framework does not depend on a single integration mechanism. It can be used with:

- direct GitHub integrations
- local Git workflows
- custom adapters or orchestration layers

### Separation of Workflow and Tooling

A key design principle of the framework is separation between:

- **workflow structure**: planning, governance, execution, validation
- **tooling choice**: which model or interface is used for a given task

This separation allows:

- tools to be swapped without redesigning the workflow
- multiple tools to be used in parallel
- experimentation with new models without destabilizing project process

### Why this matters

AI tooling changes rapidly, and no single model is consistently optimal across all tasks.

By structuring development around a stable control plane rather than a single tool, this framework enables:

- more reliable workflows
- better use of model-specific strengths
- reduced coupling between process and tooling
- long-term adaptability as new tools emerge

The result is a system where the developer remains in control of the workflow, while AI tools act as interchangeable components within that system.

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

## Core operating model

The framework is organized around four primary lanes:

### 1. Planning
Used to define mission, scope, product brief, roadmap, assumptions, and backlog before implementation begins.

### 2. Governance
Used to define priorities, constraints, decision rules, review gates, and operating standards.

### 3. Execution
Used to convert plans into implementation tasks, work items, changes, and iteration flow.

### 4. Validation
Used to verify readiness, acceptance criteria, auditability, and quality before changes are treated as complete.

## Project Control Structure

Control Plane Framework governs framework posture and also expects each real project to instantiate a canonical project workspace under `projects/<project-name>/`.

A fully initialized project includes:

- a protected core vision
- modular decomposition derived from that vision
- atomic task artifacts
- explicit planning priorities
- an authoritative active-work package
- evidence locations for validation continuity

See:

- [Project Operating Contract](docs/project-operating-contract.md)
- [Project Initialization Standard](docs/project-initialization-standard.md)
- [Planning Synchronization Rule](docs/planning-synchronization-rule.md)
- [Active Work Handoff](docs/active-work-handoff.md)

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
│   │       ├── vision/
│   │       │   ├── core_vision.md
│   │       │   ├── constraints.md
│   │       │   └── brainstorming.md
│   │       ├── docs/
│   │       │   ├── modules/
│   │       │   │   └── README.md
│   │       │   ├── tasks/
│   │       │   │   └── README.md
│   │       │   ├── priorities/
│   │       │   │   ├── now.md
│   │       │   │   ├── next.md
│   │       │   │   ├── later.md
│   │       │   │   ├── blocked.md
│   │       │   │   └── done.md
│   │       │   ├── roadmap.md
│   │       │   ├── decisions.md
│   │       │   ├── definition_of_done.md
│   │       │   └── execution_control.md
│   │       └── now/
│   │           ├── description.md
│   │           ├── prompt.md
│   │           └── metadata.json
│   ├── governance/
│   ├── execution/
│   └── validation/
└── .github/
    ├── CODEOWNERS
    ├── ISSUE_TEMPLATE/
    └── PULL_REQUEST_TEMPLATE.md
```
