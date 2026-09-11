# 🚀 REST API Engine — Portfolio-Grade Async Microservice

![CI/CD Pipeline](https://img.shields.io/github/actions/workflow/status/hafizabdulaziz/decodelabs-task1-rest-api-engine/ci.yml?branch=main&style=flat-square&logo=github-actions&label=CI%2FCD%20Build)
![Python Version](https://img.shields.io/badge/python-3.11-blue.svg?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg?style=flat-square&logo=fastapi)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0%20Async-red.svg?style=flat-square&logo=python)
![License](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)

An enterprise-ready, asynchronous RESTful microservice architected with **FastAPI**, **SQLAlchemy 2.0 (Async)**, and **Pydantic v2**. Designed to demonstrate production engineering standards including async DB persistence, dynamic query parsing, standardized pagination envelopes, structured JSON observability, security hardening, and zero-downtime CI/CD containerization.

---

## 🏛️ System Architecture

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
                  | (SQLAlchemy 2.0 + aiosqlite) |
                  +-----------------------------+

---

## ✨ Key Technical Capabilities

### ⚡ Asynchronous Core & Persistence
* **Non-Blocking I/O:** Built completely on `async/await` patterns using FastAPI and `aiosqlite`.
* **SQLAlchemy 2.0 ORM:** Employs modern `AsyncSession` handling with strict declarative typing and automated startup seed initialization.

### 🔍 Advanced Querying & Pagination Envelopes
* **Dynamic Search & Filtering:** Case-insensitive search across title/description fields, category matching, and price range bounds (`min_price`, `max_price`).
* **Multi-Field Sorting:** Flexible sorting mechanics supporting multi-attribute ordering (`price`, `created_at`).
* **Metadata Envelope:** Returns standardized pagination metadata:
  ```json
  {
    "items": [...],
    "total": 42,
    "page": 1,
    "size": 10,
    "pages": 5
  }
  ```

### 🛡️ Security Hardening
* **Rate Limiting:** Protects endpoints from abuse via `slowapi` rate limiting.
* **HTTP Security Headers:** Implements security headers alongside strict CORS and Trusted Host configurations.

### 📊 Observability & Telemetry
* **Correlated Structured Logging:** Integrated with `Loguru` to output machine-parsable JSON logs.
* **Request Tracing:** Automatically injects and propagates unique `X-Request-ID` headers across the middleware chain.

---

## 🛠️ Tech Stack & Ecosystem

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Framework** | FastAPI | High-performance async Python web framework |
| **Persistence** | SQLAlchemy 2.0 | Async ORM with SQLite (aiosqlite) driver |
| **Validation** | Pydantic v2 | High-speed data parsing and validation |
| **Testing** | Pytest + Asyncio | Integration & unit test coverage |
| **CI/CD** | GitHub Actions | Automated linting, test validation, & Docker build |
| **Containerization** | Docker | Multi-stage slim runtime build |
| **Logging** | Loguru | Structured JSON logging with request tracing |

---

## ⚡ Quick Start Guide

### Local Development Setup
1. **Clone Repository:**
   ```bash
   git clone https://github.com/hafizabdulaziz/decodelabs-task1-rest-api-engine.git
   cd decodelabs-task1-rest-api-engine
   ```
2. **Environment Configuration:**
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/Mac:
   source .venv/bin/activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install --no-cache-dir -r requirements.txt
   ```
4. **Execute Test Suite:**
   ```bash
   pytest -v
   ```
5. **Launch Application:**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

### 🐳 Docker Deployment
Build and run the production-ready lightweight Docker container:
```bash
# Build Docker Image
docker build -t rest-api-engine:latest .

# Run Container
docker run -d -p 8000:8000 --name rest-engine-service rest-api-engine:latest
```
Access the live service at `http://localhost:8000`.

---

## 📖 Interactive API Documentation
Once running, explore and test the endpoints natively via:
* **Swagger UI:** `http://localhost:8000/docs`
* **ReDoc:** `http://localhost:8000/redoc`

---

## 🧪 CI/CD Automation
Every commit pushed to `main` triggers a GitHub Actions workflow (`.github/workflows/ci.yml`) that performs:
* Environment setup and dependency installation.
* Execution of `pytest` test suite (ensuring 100% pass rate).
* Docker image build verification.

---

## 📜 License
Distributed under the MIT License. See LICENSE for details.
