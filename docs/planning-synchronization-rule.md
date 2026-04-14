# Planning Synchronization Rule

## Purpose

Require planning work to update the repository-based project memory rather than remain trapped in transient chat sessions or informal notes.

This rule exists because planning drift is one of the most common failure modes in AI-assisted development.

---

## Core Rule

When a planning session materially changes project understanding, the corresponding project files must be updated.

Planning is not complete until project truth is synchronized into the repository.

---

## Why this matters

Without synchronization, projects accumulate hidden drift:

* the vision in chat differs from the vision in docs
* modules no longer reflect current thinking
* task breakdowns become stale
* priority files no longer match intent
* implementation tools act on outdated assumptions

This causes compounding misalignment over time.

---

## Required update targets

When planning changes occur, update all affected artifacts, including as appropriate:

* `vision/core_vision.md`
* `vision/constraints.md`
* `vision/brainstorming.md`
* `docs/modules/*`
* `docs/tasks/*`
* `docs/priorities/now.md`
* `docs/priorities/next.md`
* `docs/priorities/later.md`
* `docs/roadmap.md`
* `docs/decisions.md`
* `now/description.md`
* `now/prompt.md`
* `now/metadata.json`

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

* did the project vision change?
* did the module breakdown change?
* did the task breakdown change?
* did priorities change?
* did the exact next execution target change?

If the answer is yes, the corresponding files should be updated immediately.

---

## Relationship to execution

Execution should consume repository truth, not stale planning memory.

That means planning synchronization is a prerequisite for reliable execution.

---

## Bottom Line

Planning is only durable when repository state reflects current understanding.

The framework therefore treats planning synchronization as a mandatory discipline, not an optional housekeeping step.
