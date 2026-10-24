# FastProducts — RESTful Product Catalog Service

![CI/CD Build](https://img.shields.io/github/actions/workflow/status/hafizabdulaziz/decodelabs-task1-rest-api-engine/ci.yml?branch=main&style=flat-square&logo=github-actions&label=CI%2FCD%20Build)
![Python Version](https://img.shields.io/badge/python-3.11-blue.svg?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg?style=flat-square&logo=fastapi)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0%20Async-red.svg?style=flat-square&logo=python)
![License](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)

An asynchronous RESTful microservice engineered with FastAPI, SQLAlchemy 2.0 (Async), and Pydantic v2 for product catalog management.

## Overview

FastProducts provides an asynchronous product catalog backend supporting relational persistence, dynamic multi-attribute query parsing, structured pagination envelopes, correlation-traced JSON logging, request rate limiting, and containerized deployment pipelines.

## System Architecture

```text
                  +-----------------------------+
                  |      Client Request         |
                  +--------------+--------------+
                                 |
                                 v
                  +-----------------------------+
                  |   Security Middleware       |
                  | (RateLimit, CORS, Security) |
                  +--------------+--------------+
                                 |
                                 v
                  +-----------------------------+
                  |   Telemetry Middleware      |
                  | (X-Request-ID, JSON Logs)   |
                  +--------------+--------------+
                                 |
                                 v
                  +-----------------------------+
                  |     FastAPI Router V1       |
                  |  (Pydantic v2 Validation)   |
                  +--------------+--------------+
                                 |
                                 v
                  +-----------------------------+
                  |   Async Persistence Layer   |
                  | (SQLAlchemy 2.0 + aiosqlite)|
                  +-----------------------------+
```

## Key Technical Features

### Asynchronous Core & Persistence
- **Non-Blocking I/O**: Designed end-to-end on asynchronous patterns using FastAPI and `aiosqlite`.
- **SQLAlchemy 2.0 AsyncEngine**: Implements modern `AsyncSession` patterns with declarative typing and startup seed data initialization.

### Querying & Pagination Mechanics
- **Dynamic Search & Filtering**: Case-insensitive substring matching across title and description fields, category filtering, and price boundary constraints (`min_price`, `max_price`).
- **Flexible Sorting**: Parameterized sorting across fields such as `price` and `created_at`.
- **Standardized Pagination Envelope**: Responses adhere to a predictable envelope structure:
  ```json
  {
    "items": [...],
    "total": 42,
    "page": 1,
    "size": 10,
    "pages": 5
  }
  ```

### Defensive Controls & Security
- **Rate Limiting**: Request throttling implemented via `slowapi` to protect against endpoint exhaustion.
- **HTTP Hardening**: Configured HTTP security response headers, strict CORS origins, and Trusted Host middleware.

### Observability & Telemetry
- **Structured JSON Logging**: Centralized logging via Loguru with structured JSON output formatting.
- **Correlation Tracing**: Middleware automatically generates and propagates unique `X-Request-ID` request headers.

## Technology Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Framework** | FastAPI | Asynchronous web framework |
| **Persistence** | SQLAlchemy 2.0 | Async ORM paired with the SQLite (`aiosqlite`) driver |
| **Data Validation** | Pydantic v2 | Runtime schema validation and serialization |
| **Testing** | Pytest & pytest-asyncio | Unit and integration test suite |
| **Observability** | Loguru | Structured JSON logging with request tracking |
| **CI/CD** | GitHub Actions | Automated linting, test execution, and Docker build workflows |
| **Containerization** | Docker | Multi-stage lightweight container packaging |

## Setup & Local Execution

### Local Development Environment

1. **Clone the repository**:
   ```bash
   git clone https://github.com/hafizabdulaziz/decodelabs-task1-rest-api-engine.git
   cd decodelabs-task1-rest-api-engine
   ```

2. **Configure Virtual Environment**:
   ```bash
   python -m venv .venv
   
   # Windows:
   .venv\Scripts\activate
   # Linux / macOS:
   source .venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install --no-cache-dir -r requirements.txt
   ```

4. **Execute Automated Tests**:
   ```bash
   pytest -v
   ```

5. **Start Application Server**:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

### Docker Deployment

Build and run using the provided Dockerfile:

```bash
# Build Docker image
docker build -t rest-api-engine:latest .

# Run container instance
docker run -d -p 8000:8000 --name rest-engine-service rest-api-engine:latest
```

The service will be accessible at `http://localhost:8000`.

## Interactive API Documentation

Interactive OpenAPI documentation is available locally at:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Continuous Integration (CI/CD)

Every push to the `main` branch triggers an automated GitHub Actions pipeline (`.github/workflows/ci.yml`) performing:
- Dependency resolution and environment setup.
- Comprehensive `pytest` test suite execution.
- Docker build verification.

## License

Distributed under the MIT License. See LICENSE for details.
