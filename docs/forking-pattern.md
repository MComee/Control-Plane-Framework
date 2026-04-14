# Forking Pattern

## Purpose

Control Plane Framework is intended to support a two-layer working model:

- a clean public framework repository
- private or project-specific forks for implementation work

This pattern allows the framework to remain stable, reusable, and portfolio-safe while product-specific work continues in separate repositories.

## Recommended model

### 1. Public framework repository
The public framework repository serves as:

- the canonical control-plane reference
- the home of protocol, structure, and reusable templates
- a stable public artifact that demonstrates architectural approach

This repository should remain general, reusable, and not drift into a single product implementation.

### 2. Derived project repository
A derived repository serves as:

- the implementation environment for one controlled project
- the location where project planning, governance, execution, and validation state are maintained
- the place where product-specific work happens while framework discipline is preserved

## Why this pattern works

This separation preserves three important boundaries:

- framework vs. product
- reusable structure vs. project-specific implementation
- public reference vs. private execution

It also supports a workflow in which the framework can evolve carefully while active projects move independently.

## Typical startup flow

1. Start from the public Control Plane Framework repository.
2. Fork the repository or clone its structure into a new private repository.
3. Rename the project to match the new application or system.
4. Instantiate the controlled project under `project/`.
5. Capture the protected core vision.
6. Complete initial module and task decomposition.
7. Establish priorities.
8. Establish the active-work handoff package.
9. Execute and validate implementation work using the framework.
10. Promote only reusable framework improvements back to the public framework repository.

## What belongs in the public framework repo

Keep these in the public framework repository:

- reusable documentation
- generalized templates
- protocol or governance guidance
- framework-level workflow improvements
- neutral examples that do not expose private product details

## What belongs in derived repositories

Keep these in derived repositories:

- one controlled project's implementation code
- project-specific prompts or project data
- implementation details tied to that project
- sensitive experiments
- internal notes that are not meant to become reusable framework assets

## Promotion rule

A useful decision rule is:

- if a change improves the framework as a reusable system, consider promoting it back
- if a change only serves one project, keep it in the derived repository

## Governance for the public framework

The public framework repository should keep `main` clean and reviewed.

Recommended posture:

- protect `main`
- make changes through branches and pull requests
- require owner review before merge
- treat the public repo as a stable reference implementation of the framework itself

## Long-term benefit

Over time, this pattern allows a developer to build project-specific systems on top of a stable public framework without diluting the clarity of the framework repository.
