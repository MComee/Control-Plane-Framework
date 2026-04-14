# Active Work Handoff

## Purpose

Define the authoritative active-work handoff model used by Control Plane Framework to bridge planning and execution.

This model is the third layer of framework control: tool-agnostic execution handoff.

---

## Canonical Active Work Location

Each project maintains one authoritative active-work package under:

`project/now/`

Required files:

- `description.md`
- `prompt.md`
- `metadata.json`

---

## Why this exists

Execution tools drift when they infer scope from broad context.

The active-work package provides one bounded current target with both human-readable and machine-consumable context.

---

## File responsibilities

### `project/now/description.md`

Human-readable summary of current work, constraints, and expected outcome.

### `project/now/prompt.md`

Machine-consumable execution prompt for the current bounded task.

### `project/now/metadata.json`

Structured active-work metadata, including scope, dependencies, validation requirements, and evidence paths.

---

## Tool-agnostic execution adapters

Execution handoff should support multiple tools, including:

- ChatGPT
- Gemini
- Claude
- Codex
- local tools and custom orchestrators

Tool-specific prompts or adapter payloads should be derived from the canonical `project/now/` package.

---

## Execution safety boundary

Execution tools should modify only allowed execution scope and must not mutate protected planning doctrine.

Protected-file policy is defined in `docs/project-operating-contract.md`.

---

## Human review before execution

Before execution begins, the operator should inspect:

- `project/now/description.md`
- `project/now/prompt.md`
- `project/now/metadata.json`

---

## Supersession rule

If planning invalidates current active work, replace the package explicitly and record supersession metadata.

---

## Bottom Line

The active-work package is the durable bridge between planning truth and execution action.
