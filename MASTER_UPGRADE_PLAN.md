# REST Engine --- Portfolio-Grade Production Microservice Transformation

## Master Upgrade Plan for decodelabs-task1-rest-api-engine

> **Goal:** Upgrade the existing verified DecodeLabs Task 1 FastAPI service into an enterprise-ready, portfolio-grade REST Engine with async database persistence, rate-limiting, structured telemetry, CI/CD, and full automated testing.

## 0. Safety & Execution Rules

1. Inspect existing files in `app/` and `tests/` first. Preserve existing passing API logic and verified contract endpoints.
2. Never commit `.env`, secrets, virtual environments, or SQLite DB files (`*.db`).
3. Every completed phase MUST end with:
   - Syntax and import checks
   - Running `pytest` suite
   - Checking `git status`
   - Git commit with standardized conventional commit message
   - Pushing to remote repository: https://github.com/hafizabdulaziz/decodelabs-task1-rest-api-engine.git
4. Execute continuously without stopping for tiny approvals unless blocked by critical security issues.

------------------------------------------------------------------------

# Phase 1 --- Async Database & ORM Layer (SQLAlchemy 2.0 + SQLite)

1. Add `sqlalchemy` and `aiosqlite` to `requirements.txt`.
2. Create `app/db/session.py` with async engine and sessionmaker.
3. Create `app/db/models.py` defining `Product` model with columns: `id` (int/uuid), `title`, `description`, `price`, `category`, `stock`, `is_active`, `created_at`.
4. Update `app/db/store.py` or repository layer to use async SQLAlchemy sessions instead of in-memory dictionary.
5. Add DB seed initialization on startup in `app/main.py`.

### Commit:
`feat(db): integrate async SQLAlchemy 2.0 persistence layer`

------------------------------------------------------------------------

# Phase 2 --- Dynamic Filtering, Sorting & Paginated Metadata

1. Update `GET /api/v1/products` in `app/api/v1/products.py`:
   - Support query parameters: `category` (optional), `search` (text search in title/description), `min_price`, `max_price`, `sort_by` (`price_asc`, `price_desc`, `created_at`).
   - Add standard metadata envelope:
     ```json
     {
       "total": 100,
       "page": 1,
       "size": 10,
       "items": [...]
     }
     ```
2. Validate negative numbers or invalid sort keys with Pydantic schemas.

### Commit:
`feat(api): add advanced filtering, sorting, and paginated response envelope`

------------------------------------------------------------------------

# Phase 3 --- Rate Limiting & Security Hardening

1. Add `slowapi` to `requirements.txt`.
2. Implement rate-limiting middleware in `app/main.py` (e.g., limit `/api/v1/products` creation/updates).
3. Add CORS middleware and Trusted Host middleware.
4. Add security headers (`X-Content-Type-Options`, `X-Frame-Options`, `X-XSS-Protection`).

### Commit:
`feat(security): implement rate-limiting, CORS, and security HTTP headers`

------------------------------------------------------------------------

# Phase 4 --- Structured Logging & Request Correlation ID

1. Add `loguru` to `requirements.txt`.
2. Implement middleware in `app/main.py` that generates a unique `X-Request-ID` UUID for every incoming HTTP request.
3. Attach `X-Request-ID` to response headers and log request details (method, path, status, latency) in structured format.

### Commit:
`feat(telemetry): add structured JSON logging and X-Request-ID middleware`

------------------------------------------------------------------------

# Phase 5 --- GitHub Actions CI/CD Pipeline

1. Create `.github/workflows/ci.yml`:
   - Trigger on `push` and `pull_request` to `main` branch.
   - Set up Python 3.11 environment.
   - Install dependencies from `requirements.txt`.
   - Run `pytest` test suite with code coverage report.
   - Verify Docker image build using `docker build .`.

### Commit:
`ci: configure automated testing and build pipeline with GitHub Actions`

------------------------------------------------------------------------

# Phase 6 --- Pytest Expansion & Integration Test Coverage

1. Update `tests/test_products.py` to cover:
   - Async DB session operations.
   - Pagination, category filtering, and text search scenarios.
   - Rate limit rejection scenarios.
   - Validation failure edge cases.
2. Ensure 100% test pass rate with `pytest`.

### Commit:
`test: expand integration coverage for async DB, filters, and rate-limiting`

------------------------------------------------------------------------

# Phase 7 --- Comprehensive Architecture README Rewrite

1. Rewrite `README.md` to reflect full portfolio transformation:
   - High-Level Architecture Diagram (ASCII/Mermaid)
   - Tech Stack Highlights (FastAPI Async, SQLAlchemy 2.0, Pydantic v2, Pytest, Docker, CI/CD)
   - Complete API Specs & Request/Response JSON examples
   - Local Setup & Docker Deployment Instructions
   - Telemetry, Logging, & Rate Limiting Documentation
2. Perform final `git status`, test run, and push all commits to GitHub.

### Commit:
`docs: finalize production architecture documentation and portfolio audit`
