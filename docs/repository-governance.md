# Repository Governance

## Objective

The main branch should remain a clean, stable reference branch.

For this framework, main is intended to represent reviewed, accepted state rather than active experimentation. Proposed changes should be reviewed before they are merged, and final authority over main should remain with the repository owner.

## Governance posture

Recommended posture for this repository:

- treat `main` as protected
- make changes in branches, not directly on `main`
- review proposed changes before merge
- require owner approval for important framework changes
- keep the public framework clean and reusable

## Recommended branch model

- `main`: protected, stable, reviewed branch
- short-lived feature branches: active work and proposals
- optional draft branches: experimental or incomplete changes

## Merge expectations

Before changes are merged into `main`, they should satisfy:

- clear summary of what changed
- lane impact identified
- constraints considered
- validation described
- owner review completed

## Human control principle

This framework assumes that AI tools may propose or help implement changes, but acceptance into `main` should remain a human-controlled action.

## Recommended GitHub settings

To enforce this posture in GitHub:

1. Enable branch protection for `main`.
2. Require pull requests before merging.
3. Require at least one approval before merging.
4. Restrict direct pushes to `main`.
5. Optionally require review from code owners.
6. Optionally dismiss stale approvals when new commits are pushed.

## CODEOWNERS

This repository includes a `CODEOWNERS` file so branch protection can require owner review when that setting is enabled.

## Why this matters

The framework is intended to act as a stable public artifact and reusable baseline. Protecting `main` preserves trust in the repository and keeps the framework from drifting due to unreviewed changes.
