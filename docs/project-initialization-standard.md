# Project Initialization Standard

## Purpose

Define what it means to initialize a real project from Control Plane Framework.

This standard exists so that a project fork does more than copy framework docs. It must instantiate a working control structure for the product or system being built.

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

Each project should be instantiated under:

`projects/<project-name>/`

This allows the framework to remain stable while the product-specific control structure lives in a defined location.

---

## Required initialization steps

### Step 1: Create the project workspace

Create the project directory and required control subdirectories.

### Step 2: Capture the core vision

Create `vision/core_vision.md` with the project’s north-star intent.

### Step 3: Record constraints

Create `vision/constraints.md` to document guardrails, assumptions, or non-negotiables.

### Step 4: Start decomposition

Create at least one module file under `docs/modules/`.

### Step 5: Create initial tasks

Create bounded task files under `docs/tasks/` derived from the module decomposition.

### Step 6: Establish priorities

Populate the priority files under `docs/priorities/`.

### Step 7: Establish active work

Create the active-work package under `now/`.

### Step 8: Establish evidence locations

Create the evidence directories for logs, test runs, and artifacts.

---

## Minimum initialized project tree

```text
projects/<project-name>/
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
└── evidence/
    ├── run_logs/
    ├── test_runs/
    └── artifacts/
```

---

## Bottom Line

A project fork is only truly ready for disciplined AI-assisted development after its project control structure has been instantiated.
