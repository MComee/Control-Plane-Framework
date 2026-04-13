# Framework Diagram

```mermaid
flowchart TD
    A[Protocol Layer\nGenesis Omni 2.7] --> B[Framework Layer\nControl Plane Framework]
    B --> C[Planning Lane]
    B --> D[Governance Lane]
    B --> E[Execution Lane]
    B --> F[Validation Lane]
    C --> G[Project Fork]
    D --> G
    E --> G
    F --> G
    H[Chat-Based AI Tools] --> G
    I[Command-Line AI Tools] --> G
    J[Human Review] --> G
```

## Interpretation

- The protocol layer defines posture and operating expectations.
- The framework layer provides reusable structure.
- The project fork is where product-specific work happens.
- Multiple AI tools may participate in the same project.
- Human review remains part of the control loop.
