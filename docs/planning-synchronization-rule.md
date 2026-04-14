# Planning Synchronization Rule

## Purpose

Require planning work to update repository-based project memory rather than remain trapped in transient chat sessions or informal notes.

---

## Core Rule

When planning materially changes project understanding, corresponding project files must be updated.

Planning is not complete until project truth is synchronized into repository state.

---

## Single-project scope

In a derived repository, this rule applies to one controlled project under `project/`.

---

## Required update targets

When planning changes occur, update all materially affected artifacts, including as appropriate:

- `project/vision/core_vision.md`
- `project/vision/constraints.md`
- `project/vision/brainstorming.md`
- `project/docs/features/*`
- `project/docs/task_groups/*`
- `project/docs/tasks/*`
- `project/docs/priorities/now.md`
- `project/docs/priorities/next.md`
- `project/docs/priorities/later.md`
- `project/docs/priorities/blocked.md`
- `project/docs/priorities/done.md`
- `project/docs/roadmap.md`
- `project/docs/decisions.md`
- `project/now/description.md`
- `project/now/prompt.md`
- `project/now/metadata.json`

---

## Planning completion rule

A planning session should not be considered complete until:

1. planning changes are identified
2. affected artifacts are updated
3. priorities are rechecked
4. active work state is rechecked
5. contradictory stale content is resolved

---

## Relationship to execution

Execution should consume synchronized repository truth.

Planning synchronization is a prerequisite for reliable execution handoff.

---

## Bottom Line

Planning durability depends on repository synchronization. This is mandatory discipline, not optional housekeeping.
