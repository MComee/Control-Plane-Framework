# Active Work Handoff

## Purpose

Define the authoritative active-work handoff model used by Control Plane Framework to bridge planning and execution.

This document exists so that the framework can support multiple implementation tools without losing control of what the current work item actually is.

The key idea is simple:

* project planning state is maintained in project docs
* the exact current work item is materialized in one active-work package
* the developer reviews that package
* implementation tools consume that package in a bounded way

---

## Canonical Active Work Location

Each project must maintain an authoritative active-work package under:

`projects/<project-name>/now/`

Required files:

* `description.md`
* `prompt.md`
* `metadata.json`

---

## Why this exists

Large language models and AI-assisted tools are useful, but they can drift when forced to infer the current work item from broad context alone.

This active-work package exists to reduce that drift.

It provides:

* one exact current work target
* one human-readable explanation
* one machine-consumable prompt
* one structured metadata record

---

## File Responsibilities

## `description.md`

Human-readable summary of the active work item.

Recommended contents:

* task title
* short explanation of what happens next
* why this task matters now
* expected outcome
* important constraints
* major risks or edge cases
* what should happen after completion

This file is for operator clarity and pre-execution review.

---

## `prompt.md`

Machine-consumable handoff prompt.

This file should contain the exact scoped execution request to be used by an implementation tool.

It should be specific enough to reduce ambiguity and bounded enough to avoid silent scope creep.

Recommended contents:

* exact objective
* allowed files
* forbidden files
* required reads
* required validations
* evidence expectations
* completion criteria
* instructions if blocked

---

## `metadata.json`

Structured representation of the active work item.

Example fields:

* `project_name`
* `lane`
* `task_id`
* `status`
* `created_at`
* `updated_at`
* `depends_on`
* `allowed_paths`
* `forbidden_paths`
* `validation_requirements`
* `evidence_paths`
* `supersedes`
* `superseded_by`

The schema may evolve, but a metadata file should always exist.

---

## Relationship to Priorities

The active-work package is not the same thing as the planning priority files.

Priority files answer questions such as:

* what is most important now?
* what should happen next?
* what is deferred?
* what is blocked?

The active-work package answers a more specific question:

* what exact bounded thing should be executed right now?

This distinction keeps planning state and execution state from collapsing into each other.

---

## Generation Model

The active-work package should be generated or updated after planning and prioritization are complete enough to define one bounded next step.

Typical sequence:

1. planning updates project understanding
2. project docs are synchronized
3. priorities are reviewed
4. one bounded task is selected
5. the active-work package is updated
6. the operator reviews the package
7. implementation begins

---

## Tool-Agnostic Principle

The active-work package is intentionally tool-agnostic.

It should support:

* command-line AI tools
* IDE chat integrations
* local or hosted model runtimes
* custom orchestrators

The framework standardizes the active-work package itself.

Specific handoff formats for a given tool can be generated from that package when needed.

---

## Human Review Before Execution

The developer should be able to inspect:

* `description.md`
* `prompt.md`
* `metadata.json`

before sending the task to an implementation tool.

This is an important safety and control feature.

---

## Example Operator Command Concept

An eventual local workflow may support a command such as:

`align to active work`

That command should conceptually:

1. locate the active project
2. open `now/description.md`
3. open `now/prompt.md`
4. verify metadata and scope
5. allow human review
6. pass the prompt to the chosen tool
7. persist evidence after execution

The framework does not require one command implementation, but it does define the control concept.

---

## Supersession Rule

If planning changes invalidate the current active work package, the package should be explicitly updated rather than silently reused.

Metadata should indicate supersession where possible.

Only one authoritative active-work package should be treated as current for a given project unless the project explicitly supports parallel lanes of implementation.

---

## Bottom Line

The active-work package is the framework’s bridge between planning truth and implementation action.

It exists so that execution can remain precise, reviewable, and tool-agnostic.
