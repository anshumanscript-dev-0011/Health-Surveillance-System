# Backend Standards

## Naming Conventions
- Variables: snake_case
- Functions: snake_case
- Classes: PascalCase
- Constants: UPPER_SNAKE_CASE

## API Standards
- RESTful APIs
- Plural resource names
- Lowercase URLs
- Version APIs under `/api/v1/` (recommended)

## Authentication
- JWT Authentication

## Database
- Integer IDs (or UUIDs if chosen)
- UTC timezone
- Timezone-aware timestamps

## Delete Strategy
- Soft delete for important business records
- Hard delete for temporary or test data

## Logging
- Use Python logging
- Do not use `print()` for production logging

## API Response Format
- Consistent success/error response structure

## Code Quality
- Follow PEP 8
- Use Black for formatting (optional)
- Use Ruff or Flake8 for linting (optional)