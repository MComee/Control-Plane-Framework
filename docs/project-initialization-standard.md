# Project Initialization Standard

## Purpose

Define what it means to initialize one real project from Control Plane Framework.

A derived repository is not ready until the controlled `project/` workspace is instantiated.

---

## A project is not fully initialized until it has

1. a canonical project workspace
2. protected vision artifacts
3. initial feature decomposition
4. initial task-group decomposition
5. initial atomic tasks
6. explicit priority files
7. an authoritative active-work package
8. evidence directories

---

## Required workspace

Instantiate the controlled project under:

`project/`

---

## Required initialization steps

### Step 1: Create project workspace

Create `project/` and core control directories.

### Step 2: Capture protected vision

Create:

- `project/vision/core_vision.md`
- `project/vision/constraints.md`
- `project/vision/brainstorming.md`

### Step 3: Start decomposition

Create at least:

- one feature file under `project/docs/features/`
- one task-group file under `project/docs/task_groups/`
- one atomic task file under `project/docs/tasks/`

### Step 4: Establish priorities

Populate `project/docs/priorities/`.

### Step 5: Establish active work

Create `project/now/description.md`, `project/now/prompt.md`, and `project/now/metadata.json`.

### Step 6: Establish evidence locations

Create `project/evidence/run_logs/`, `project/evidence/test_runs/`, and `project/evidence/artifacts/`.

### Step 7: Establish implementation placeholder

Create `project/app/`.

---

## Minimum initialized project tree

```text
project/
├── vision/
│   ├── core_vision.md
│   ├── constraints.md
│   └── brainstorming.md
├── docs/
│   ├── features/
│   ├── task_groups/
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

A derived repository is ready only after its single controlled `project/` structure is in place.
