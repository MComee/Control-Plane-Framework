# Project Initialization Standard

## Purpose

Define what it means to initialize a real project from Control Plane Framework.

This standard exists so that a derived repository does more than copy framework docs. It must instantiate a working control structure for the one product or system being built.

---

## A project is not fully initialized until it has

1. a canonical project workspace
2. a protected core vision
3. initial module decomposition
4. initial task decomposition
5. explicit priority files
6. an authoritative active-work package
7. evidence directories

---

## Required workspace

Each derived repository should instantiate its controlled project under:

`project/`

This allows the framework to remain stable while project-specific control state lives in one defined location.

---

## Required initialization steps

### Step 1: Create the project workspace

Create `project/` and required control subdirectories.

### Step 2: Capture the core vision

Create `project/vision/core_vision.md` with the project's north-star intent.

### Step 3: Record constraints

Create `project/vision/constraints.md` to document guardrails, assumptions, or non-negotiables.

### Step 4: Start decomposition

Create at least one module file under `project/docs/modules/`.

### Step 5: Create initial tasks

Create bounded task files under `project/docs/tasks/` derived from module decomposition.

### Step 6: Establish priorities

Populate priority files under `project/docs/priorities/`.

### Step 7: Establish active work

Create the active-work package under `project/now/`.

### Step 8: Establish evidence locations

Create evidence directories under `project/evidence/`.

### Step 9: Create implementation placeholder

Create `project/app/` as the placeholder where stack-specific implementation lives.

---

## Minimum initialized project tree

```text
project/
├── vision/
│   ├── core_vision.md
│   ├── constraints.md
│   └── brainstorming.md
├── docs/
│   ├── modules/
│   ├── tasks/
│   ├── priorities/
│   │   ├── now.md
│   │   ├── next.md
│   │   ├── later.md
│   │   ├── blocked.md
│   │   └── done.md
│   ├── roadmap.md
│   ├── decisions.md
│   ├── definition_of_done.md
│   └── execution_control.md
├── now/
│   ├── description.md
│   ├── prompt.md
│   └── metadata.json
├── evidence/
│   ├── run_logs/
│   ├── test_runs/
│   └── artifacts/
└── app/
```

---

## Bottom Line

A derived repository is ready for disciplined AI-assisted development only after its single controlled project structure under `project/` has been instantiated.
