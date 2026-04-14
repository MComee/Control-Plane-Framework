# Forking Pattern

## Purpose

Control Plane Framework is designed for a two-repository pattern:

- a clean public framework repository
- derived repositories for project implementation

This preserves framework reusability while allowing project-specific execution.

## Recommended model

### 1. Public framework repository

The public framework repository serves as:

- the canonical control reference
- the home of reusable doctrine, templates, and routing
- a stable public artifact for framework evolution

This repository should remain general and reusable.

### 2. Derived project repository

A derived repository serves as:

- the implementation environment for one controlled project
- the location where project planning, governance, execution, and validation state are maintained
- the place where project-specific work happens under framework control

## Typical startup flow

1. Start from the public Control Plane Framework repository.
2. Fork it or clone its structure into a private repository.
3. Rename the project to match the target system.
4. Instantiate the controlled project under `project/`.
5. Capture the protected core vision.
6. Decompose into features, task groups, and tasks.
7. Establish priorities.
8. Establish the active-work handoff package.
9. Execute and validate implementation work under framework rules.
10. Promote only reusable framework improvements back to the public framework repository.

## What belongs in the public framework repo

Keep these in the public framework repository:

- reusable documentation
- generalized templates
- framework-level governance and routing guidance
- neutral examples without private product details

## What belongs in derived repositories

Keep these in derived repositories:

- one controlled project's implementation code
- project-specific prompts or project data
- implementation details tied to that project
- sensitive experiments
- internal notes that are not reusable framework assets

## Promotion rule

Use this rule:

- if a change improves the framework as a reusable system, promote it back
- if a change only serves one project, keep it in the derived repository

## Governance for the public framework

The public framework repository should keep `main` clean and reviewed.

Recommended posture:

- protect `main`
- make changes through branches and pull requests
- require owner review before merge

## Long-term benefit

This pattern enables project-specific delivery on top of a stable framework without diluting framework clarity.
