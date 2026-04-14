# Overview

Control Plane Framework is a reusable repository framework for governed, model-agnostic AI-assisted development.

Its purpose is to provide a control structure before implementation begins. Rather than layering process after code already exists, the framework treats planning, governance, execution, and validation as first-class system parts.

## Intended use

This framework is intended for developers who:

- work across multiple AI tools
- want a reusable starting point for new projects
- need a clean separation between process control and product code
- want planning and governance in place before major implementation

## What makes this different

The framework is not tied to a language, stack, or product category.

It emphasizes:

- stable process over tool-specific habits
- reusable structure over ad hoc setup
- explicit governance over implicit assumptions
- validation and review over unchecked iteration

## Core lanes

The framework is organized into four lanes:

- Planning
- Governance
- Execution
- Validation

Each lane has templates that can be initialized and refined over time.

## Three-layer control model

Each derived repository controls one project and operates three layers:

### Layer 1: Framework self-governance

The framework governs itself and preserves doctrine, routing rules, and anti-drift behavior.

### Layer 2: Project control

The same repository governs one controlled project under `project/`, including:

- protected vision
- features
- task groups
- atomic tasks
- priorities
- active work state
- evidence continuity

### Layer 3: Execution handoff

The active-work package under `project/now/` bridges planning truth and implementation action.

Execution tools should consume this canonical package, and tool-specific adapters should be derived from it.

## Typical lifecycle

1. Fork or derive the framework for a new project.
2. Instantiate `project/`.
3. Capture protected vision and constraints.
4. Decompose into features, task groups, and tasks.
5. Set priorities.
6. Define and review active work.
7. Execute and validate under framework controls.

## Project control beyond framework posture

The framework organizes itself and also governs the one actual project built inside the same repository.

This is why planning artifacts, priority state, and active-work handoff are treated as durable repository assets.

## Outcome

The intended outcome is a project environment where AI tools are useful without becoming the workflow itself. The developer stays in control while the framework keeps work coherent as tools and models evolve.
