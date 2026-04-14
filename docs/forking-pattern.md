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

### 2. Private project forks
Private forks or derivative repositories serve as:

- implementation environments for product-specific work
- places for experiments, proprietary planning, and active development
- repositories where the framework is adapted to a specific application or system

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
4. Instantiate the project operating structure under `projects/<project-name>/`.
5. Capture the project's protected core vision.
6. Complete initial module and task decomposition.
7. Define project-specific governance constraints and acceptance criteria.
8. Create the active-work handoff package.
9. Perform implementation work in the private repository.
10. Promote only reusable framework improvements back to the public framework repository.

## What belongs in the public framework repo

Keep these in the public framework repository:

- reusable documentation
- generalized templates
- protocol or governance guidance
- framework-level workflow improvements
- neutral examples that do not expose private product details

## What belongs in private forks

Keep these in private forks or project-specific repositories:

- product-specific code
- proprietary prompts or project data
- implementation details tied to a single application
- sensitive experiments
- internal notes that are not meant to become reusable framework assets

## Promotion rule

A useful decision rule is:

- if a change improves the framework as a reusable system, consider promoting it back
- if a change only serves one product, keep it in the product repository

## Governance for the public framework

The public framework repository should keep `main` clean and reviewed.

Recommended posture:

- protect `main`
- make changes through branches and pull requests
- require owner review before merge
- treat the public repo as a stable reference implementation of the framework itself

## Long-term benefit

Over time, this pattern allows a developer to build a portfolio of private or product-specific work on top of a stable public framework without diluting the clarity of the framework repository.
