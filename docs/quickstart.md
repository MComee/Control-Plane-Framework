# Quickstart

## Goal

Use this framework as the starting point for a new private or public project without rebuilding planning and governance structure from scratch.

## Recommended startup flow

1. Fork this repository.
2. Rename the fork to match the new project.
3. Update the planning templates under `framework/planning/`.
4. Define priorities and constraints under `framework/governance/`.
5. Translate the plan into actionable work under `framework/execution/`.
6. Establish validation criteria under `framework/validation/`.
7. Begin implementation only after the basic control structure is in place.

## Multi-tool workflow example

A typical workflow may involve multiple AI tools:

- a chat-based tool for planning and decomposition
- a second chat-based tool for critique or comparison
- a command-line tool for implementation against a local checkout
- human review before accepting major changes

The framework does not require a single tool. It is designed so that tool choice can change without breaking the workflow.

## Minimum setup checklist

Complete these before major implementation begins:

- `framework/planning/mission.template.md`
- `framework/planning/roadmap.template.md`
- `framework/governance/priorities.template.md`
- `framework/governance/constraints.template.md`
- `framework/validation/acceptance.template.md`

## Optional next steps

- Create issue labels aligned to the four lanes.
- Add branch naming conventions.
- Add CI rules or review requirements.
- Extend the protocol layer for your environment.
