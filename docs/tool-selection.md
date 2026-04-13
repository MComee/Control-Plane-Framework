# Tool Selection

## Purpose

Control Plane Framework is designed for model-agnostic, multi-tool workflows.

The framework assumes that a developer may use more than one AI tool in the same project and that different tools may be stronger at different tasks. The objective is not to standardize on a single chat interface, command-line tool, or model provider. The objective is to standardize the workflow around which those tools operate.

## Core principle

Choose tools by task fit, not by habit.

A stable control plane makes it possible to swap or combine tools without destabilizing the project workflow.

## Chat-based tools

Chat-based tools are often well-suited for:

- project scoping
- planning and decomposition
- architecture discussion
- critique and alternative reasoning
- documentation drafting
- review-oriented interaction

A project may use multiple chat-based tools in parallel as long as they can participate in repository-aware workflow and follow the structure of the project.

## Command-line tools

Command-line or local AI tools are often well-suited for:

- implementation work against a local checkout
- file-by-file iteration
- terminal-driven workflows
- scripted or repeatable operations
- local validation and patch generation

A project may use multiple command-line tools if they improve task-specific execution.

## Repository interaction expectations

Preferred tools are those that can work with repository context in a controlled way. That may include:

- direct GitHub integration
- local Git access
- structured file creation or modification
- compatibility with project templates and review gates

## Selection criteria

When choosing a tool for a task, evaluate:

- reasoning quality for the task type
- ability to preserve structure and constraints
- reliability of file or repository interaction
- ease of review before accepting changes
- suitability for the current phase of work

## Example pattern

A single project might use:

- one chat-based tool for planning and decomposition
- another for critique or second-pass review
- one command-line tool for local implementation
- human review before accepting changes into protected branches

## Anti-patterns

Avoid:

- forcing all work through a single tool when better task-specific options exist
- coupling the framework to a single vendor or runtime
- allowing tools to bypass review structure
- treating AI tool choice as more important than workflow discipline

## Conclusion

The framework is designed so that tooling can evolve while the operating model remains stable. Tool choice is important, but tool choice is not the control plane.
