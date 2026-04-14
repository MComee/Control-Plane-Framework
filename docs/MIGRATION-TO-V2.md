# Migration Guide — V1 to V2 Templates

## Purpose

This document defines how to migrate legacy framework usage to the control-plane compliant V2 system.

## Required changes

### 1. Replace templates

Replace all:

- `*.template.md`

With:

- `*.template.v2.md`

### 2. Add metadata

Each artifact must include YAML frontmatter:

```
---
artifact_type:
lane:
status:
owner:
dependencies:
---
```

### 3. Define dependencies

Each artifact must explicitly declare dependencies according to:

mission → []
product-brief → [mission]
roadmap → [mission, product-brief]
tasks → [roadmap]
implementation-plan → [tasks]
validation → [implementation-plan]
acceptance → [validation]

### 4. Set initial states

Use:

- draft

For all new artifacts until validation is performed.

### 5. Run validation

Execute:

```
python scripts/validate_framework_v4.py
```

## Success condition

Migration is complete when:

- all artifacts use V2 templates
- metadata is present and valid
- dependencies resolve correctly
- validation passes

## Notes

Legacy templates may remain temporarily but should not be used for new work.
