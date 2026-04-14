# Start Here

If you are new to Control Plane Framework, use this sequence:

1. Read the top-level `README.md` for purpose and routing.
2. Read `docs/overview.md` for the three-layer model.
3. Read `docs/architecture.md` for lane and layer structure.
4. Read `docs/tool-selection.md` for model-agnostic execution posture.
5. Read `docs/repository-governance.md` for framework self-governance.
6. Read `docs/forking-pattern.md` before starting a derived repository.
7. Review `examples/sample-project-brief.md` for initialization context.

## Fast path

If your goal is to start a new project quickly:

- fork the repository
- instantiate `project/`
- capture protected vision
- decompose into features, task groups, and tasks
- set priorities and active work
- begin implementation only after control structure is in place

## Project initialization requirement

Before implementation begins in a derived repository, the controlled project structure must be instantiated.

At minimum, this includes:

- the canonical `project/` workspace
- protected vision files
- initial feature decomposition
- initial task-group decomposition
- initial atomic tasks
- priority files
- an active-work handoff package

See:

- [Project Operating Contract](/docs/project-operating-contract.md)
- [Project Initialization Standard](/docs/project-initialization-standard.md)
- [Active Work Handoff](/docs/active-work-handoff.md)
- [Planning Synchronization Rule](/docs/planning-synchronization-rule.md)
