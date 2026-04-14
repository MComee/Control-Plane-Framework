# Overview

Control Plane Framework is a reusable repository framework for governed, model-agnostic AI-assisted development.

Its purpose is to give a project an operating structure before implementation begins. Rather than starting from a blank repository and layering process in later, the framework starts with a control-plane mindset: planning, governance, execution, and validation are treated as first-class parts of the system.

## Intended use

This framework is intended for developers who:

- work across multiple AI tools
- want a reusable starting point for new projects
- need a cleaner separation between process and product code
- want planning and governance to exist before major implementation begins

## What makes this different

The framework is not tied to a language, stack, or product category. It can be used for application development, systems work, experiments, internal tooling, prototypes, and architecture-heavy projects.

The central assumption is that workflows should remain stable even if tools change. That means the framework emphasizes:

- stable process over tool-specific habits
- reusable structure over ad hoc project setup
- explicit governance over implicit assumptions
- validation and review over unchecked iteration

## Core lanes

The framework is organized into four lanes:

- Planning
- Governance
- Execution
- Validation

Each lane has templates that can be completed at project startup and refined over time.

## Layered control model

Control Plane Framework operates as a layered control model in each derived repository.

### 1) Framework self-governance

The framework governs itself. It preserves doctrine, anti-drift discipline, and reusable control patterns so the framework remains stable and reviewable.

### 2) Project control

A derived repository controls one real project under `project/`, not many projects under one orchestrator.

That controlled project contains:

- protected vision
- modular decomposition
- atomic task structure
- explicit priorities
- active work state
- evidence continuity

### 3) Execution handoff

The active-work package under `project/now/` bridges planning truth and implementation action.

Execution tools consume this canonical package, and any tool-specific adapter prompts are derived from it.

## Typical lifecycle

1. Fork or derive the framework for a new project.
2. Instantiate the controlled project workspace at `project/`.
3. Capture protected vision and constraints.
4. Decompose into modules and tasks.
5. Set planning priorities.
6. Define and review active work.
7. Execute and validate inside framework controls.

## Project control beyond framework posture

The framework is not only intended to organize itself. It is also intended to govern the one actual project being built inside the same repository.

This is why planning artifacts, priority state, and active-work handoff are treated as first-class repository assets.

## Outcome

The intended outcome is a project environment where AI tools are useful without becoming the workflow itself. The developer remains in control, and the framework provides the operating structure that keeps work coherent as tools, models, and implementation details evolve.
