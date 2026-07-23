# Git Workflow

## Overview

This document defines the Git branching strategy and development workflow for the Smart Health Surveillance & Early Warning System.

The objective is to maintain a clean, organized, and stable codebase throughout the project lifecycle.

---

## Branch Strategy

### main

* Stable production-ready branch.
* Only tested and reviewed code should be merged into this branch.

### develop

* Main development branch.
* All completed feature branches are merged here before moving to `main`.

### Feature Branches

Each major feature will be developed in its own branch.

Example branches:

* feature/authentication
* feature/accounts
* feature/locations
* feature/patients
* feature/diseases
* feature/laboratory
* feature/alerts
* feature/dashboard
* feature/analytics
* feature/notifications
* feature/ai-prediction

---

## Development Workflow

```text
main
   │
   ▼
develop
   │
   ▼
feature branch
   │
   ▼
Development
   │
   ▼
Testing
   │
   ▼
Documentation Update
   │
   ▼
Merge into develop
   │
   ▼
Merge into main
```

---

## Commit Message Convention

The following prefixes should be used for commit messages:

| Prefix   | Purpose               |
| -------- | --------------------- |
| docs     | Documentation updates |
| feat     | New features          |
| fix      | Bug fixes             |
| refactor | Code improvements     |
| test     | Test cases            |
| chore    | Maintenance tasks     |

### Examples

* docs: update API documentation
* feat: implement patient registration API
* fix: resolve JWT authentication issue
* refactor: improve dashboard service
* test: add patient API unit tests

---

## Best Practices

* Create a new feature branch for every major module.
* Keep commits small and focused.
* Write meaningful commit messages.
* Test features before merging.
* Update documentation whenever a significant feature is completed.
* Never commit sensitive information such as API keys, passwords, or `.env` files.
* Keep the `main` branch stable and deployable at all times.

---

## Future Improvements

As the project grows, the Git workflow may be enhanced with:

* Pull Request reviews
* GitHub Actions for CI/CD
* Branch protection rules
* Automated testing before merge
* Semantic versioning for releases
