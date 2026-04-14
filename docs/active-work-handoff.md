# Active Work Handoff

## Purpose

Define the authoritative active-work handoff model used by Control Plane Framework to bridge planning and execution.

This model is the framework's third control layer: execution handoff.

It exists so the framework can support multiple implementation tools without losing control of what the current work item actually is.

The key idea is simple:

- planning state is maintained in project docs
- the exact current work item is materialized in one active-work package
- the operator reviews that package
- execution tools consume that package in a bounded way

---

## Canonical Active Work Location

Each project must maintain an authoritative active-work package under:

`project/now/`

Required files:

- `description.md`
- `prompt.md`
- `metadata.json`

---

## Why this exists

LLM-based and AI-assisted tools can drift when they infer current work from broad context alone.

The active-work package reduces that drift by providing:

- one exact current work target
- one human-readable explanation
- one machine-consumable prompt
- one structured metadata record

---

## File responsibilities

## `project/now/description.md`

Human-readable summary of the active work item.

Recommended contents:

- task title
- short explanation of what happens next
- why this task matters now
- expected outcome
- important constraints
- major risks or edge cases
- what should happen after completion

---

## `project/now/prompt.md`

Machine-consumable handoff prompt.

This file should contain the exact scoped execution request used by an implementation tool.

Recommended contents:

- exact objective
- allowed files
- forbidden files
- required reads
- required validations
- evidence expectations
- completion criteria
- instructions if blocked

---

## `project/now/metadata.json`

Structured representation of the active work item.

Example fields:

- `project_name`
- `lane`
- `task_id`
- `status`
- `created_at`
- `updated_at`
- `depends_on`
- `allowed_paths`
- `forbidden_paths`
- `validation_requirements`
- `evidence_paths`
- `supersedes`
- `superseded_by`

The schema may evolve, but a metadata file should always exist.

---

## Relationship to priorities

The active-work package is not the same thing as planning priority files.

Priority files answer:

- what is most important now?
- what should happen next?
- what is deferred?
- what is blocked?

The active-work package answers:

- what exact bounded thing should be executed right now?

This distinction keeps planning state and execution state from collapsing into each other.

---

## Generation model

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

## Tool-agnostic execution adapter principle

The active-work package is intentionally tool-agnostic.

It should support:

- command-line AI tools
- IDE chat integrations
- local or hosted model runtimes
- custom orchestrators

The framework standardizes the active-work package itself.

Tool-specific prompts, adapters, or integration payloads should be derived from this canonical package.

---

## Human review before execution

Before sending work to an execution tool, the operator should inspect:

- `project/now/description.md`
- `project/now/prompt.md`
- `project/now/metadata.json`

This is a safety and control feature.

---

## Example operator command concept

An eventual local workflow may support a command such as:

`align to active work`

That command should conceptually:

1. locate the controlled project under `project/`
2. open `project/now/description.md`
3. open `project/now/prompt.md`
4. verify metadata and scope
5. allow human review
6. pass the prompt to the chosen tool
7. persist evidence after execution

The framework does not require one command implementation, but it does define the control concept.

---

## Supersession rule

If planning changes invalidate the current active-work package, the package should be explicitly updated rather than silently reused.

Metadata should indicate supersession where possible.

Only one authoritative active-work package should be treated as current for the project unless parallel lanes are explicitly supported.

---

## Bottom Line

The active-work package is the framework bridge between planning truth and implementation action.

It keeps execution precise, reviewable, and tool-agnostic.
