# Contributing

## Contribution posture

Contributions should preserve the distinction between:

- protocol layer
- framework layer
- project-specific implementation patterns

This repository is intended to remain a reusable control-plane framework rather than drift into a single product implementation.

## Contribution priorities

High-value contributions typically improve one of the following:

- clarity of the control-plane model
- quality of planning, governance, execution, or validation templates
- documentation and examples
- workflow consistency across multiple AI tools
- reviewability and auditability of changes

## Before opening a pull request

1. Identify which lane the change affects.
2. Document the reason for the change.
3. Note any constraints or tradeoffs.
4. Update documentation if the workflow changes.
5. Validate that the change improves the framework rather than coupling it to a single tool or product.

## What to avoid

Avoid contributions that:

- hard-code the framework to a single vendor, model, or runtime
- collapse governance into implementation-only workflow
- turn the framework into a product-specific scaffold
- remove human review expectations from critical checkpoints

## Pull requests

Use the pull request template and explain:

- what changed
- why it changed
- which lane was affected
- what validation was performed

## Issues

When opening an issue, place it in the most appropriate lane:

- Planning
- Governance
- Execution
- Validation
