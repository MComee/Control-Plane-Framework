# Genesis Omni 2.7 — Framework Adoption

## Purpose

This document defines how Control Plane Framework adopts and uses the Genesis Omni 2.7 ST protocol.

## Layer model

Control Plane Framework operates across three distinct layers:

1. Protocol Layer (Genesis Omni)
2. Framework Layer (Control Plane Framework)
3. Project Layer (forked repositories)

## Role of Genesis Omni inside the framework

Genesis Omni defines:

- epistemological constraints
- task decomposition rules
- validation and falsification requirements
- command semantics (/plan, /run, /audit, etc.)

The framework does NOT replace these rules.
The framework organizes how they are applied.

## Mapping to framework lanes

Genesis Omni expectations map to framework lanes as follows:

- Planning → Atomic decomposition (/plan), zero-assumption policy
- Governance → constraint visibility, review gates, falsification posture
- Execution → controlled iteration (/run), bounded task resolution
- Validation → /test, /audit, /verify, VTE compliance

## Enforcement stance

Within Control Plane Framework:

- Genesis Omni is treated as a governing reference
- Framework artifacts should not contradict core protocol mandates
- Project forks may extend, but should not silently weaken protocol guarantees

## Interpretation boundary

Genesis Omni defines HOW reasoning and execution should behave.
Control Plane Framework defines WHERE that behavior is structured in a repository.

They are complementary, not interchangeable.
