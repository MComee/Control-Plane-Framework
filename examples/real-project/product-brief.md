---
artifact_type: product-brief
lane: planning
status: defined
owner: example
dependencies:
  - mission
---

# Summary
A minimal example project used to prove the control-plane artifact chain.

# Problem statement
A reviewer needs a concrete, inspectable artifact chain that demonstrates the framework working as a real control plane.

# Intended users
Engineers evaluating the framework.

# Primary use cases
- inspect artifact metadata
- inspect dependency chain
- verify lifecycle progression
- run validation against a complete example

# Desired outcomes
- the example validates cleanly
- dependencies are explicit
- lifecycle states are coherent

# Success metrics
- validator passes
- no missing dependencies
- no invalid lifecycle state

# Non-goals
- production deployment
- application-specific code

# Assumptions
The framework repository contains the required validators and schemas.

# Open questions
None
