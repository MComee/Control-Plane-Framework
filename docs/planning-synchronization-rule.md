# Planning Synchronization Rule

## Purpose

Require planning work to update repository-based project memory rather than remain trapped in transient chat sessions or informal notes.

This rule exists because planning drift is one of the most common failure modes in AI-assisted development.

---

## Core Rule

When a planning session materially changes project understanding, corresponding project files must be updated.

Planning is not complete until project truth is synchronized into the repository.

---

## Single-project scope

In a derived repository, this rule applies to one controlled project under `project/`.

Planning must synchronize into that one project's control artifacts, not a multi-project workspace.

---

## Why this matters

Without synchronization, projects accumulate hidden drift:

- vision in chat differs from vision in docs
- modules no longer reflect current thinking
- task breakdowns become stale
- priority files no longer match intent
- execution tools act on outdated assumptions

This causes compounding misalignment over time.

---

## Required update targets

When planning changes occur, update all affected artifacts, including as appropriate:

- `project/vision/core_vision.md`
- `project/vision/constraints.md`
- `project/vision/brainstorming.md`
- `project/docs/modules/*`
- `project/docs/tasks/*`
- `project/docs/priorities/now.md`
- `project/docs/priorities/next.md`
- `project/docs/priorities/later.md`
- `project/docs/roadmap.md`
- `project/docs/decisions.md`
- `project/now/description.md`
- `project/now/prompt.md`
- `project/now/metadata.json`

Not every session updates every file, but every materially affected file should be brought back into alignment.

---

## Planning completion rule

A planning session should not be considered complete until:

1. planning changes have been identified
2. affected project artifacts have been updated
3. priorities have been rechecked
4. active work state has been rechecked
5. stale contradictory content has been resolved

---

## Minimum expectation

At minimum, every meaningful planning session should answer:

- did the project vision change?
- did module decomposition change?
- did task decomposition change?
- did priorities change?
- did the exact next execution target change?

If the answer is yes, the corresponding files should be updated immediately.

---

## Relationship to execution

Execution should consume synchronized repository truth, not stale planning memory.

Planning synchronization is therefore a prerequisite for reliable execution handoff.

---

## Bottom Line

Planning is only durable when repository state reflects current understanding.

The framework treats planning synchronization as a mandatory discipline, not optional housekeeping.
