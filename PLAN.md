# DecodeLabs Task 1 --- REST API Engine Master Upgrade Plan

## Production-Ready RESTful API Engine Architecture

> **Working principle:** Implement a clean, production-oriented, modular RESTful API Engine using FastAPI and Pydantic v2 for DecodeLabs Task 1. Build a strict, fully-tested, documented, and containerized backend microservice.

## 0. Non-Negotiable Safety Rules

1. Do not delete existing project files unless proven redundant and explicitly required.
2. Never hardcode or commit `.env`, API keys, secrets, virtual environments, or caches (`__pycache__`).
3. Every completed phase MUST end with:
   - Syntax and import verification
   - Executing pytest suite
   - Checking `git status`
   - Creating a clear, meaningful Git commit
   - Pushing to remote: https://github.com/hafizabdulaziz/decodelabs-task1-rest-api-engine.git
4. Keep the working tree clean after every completed phase.
5. Follow this master plan continuously without stopping after tiny actions. Only stop for security-sensitive or destructive blockers.

------------------------------------------------------------------------

# 1. Product & Architecture Identity

- **Project Name:** REST Engine --- Production-Ready RESTful API Service
- **Repository:** decodelabs-task1-rest-api-engine
- **Core Tech Stack:** Python 3.10+, FastAPI (Async), Pydantic v2, Pytest, Uvicorn, Docker, GitHub Actions.

------------------------------------------------------------------------

# 2. Phase 1 --- Architecture Setup & Baseline

1. Inspect the target directory and initialize virtual environment/dependencies.
2. Create standard production directory structure:
   ```text
   decodelabs-task1-rest-api-engine/
   ├── app/
   │   ├── __init__.py
   │   ├── main.py
   │   ├── core/
   │   │   ├── __init__.py
   │   │   └── config.py
   │   ├── schemas/
   │   │   ├── __init__.py
   │   │   └── product.py
   │   ├── db/
   │   │   ├── __init__.py
   │   │   └── store.py
   │   └── api/
   │       └── v1/
   │           ├── __init__.py
   │           └── products.py
   ├── tests/
   │   ├── __init__.py
   │   ├── conftest.py
   │   └── test_products.py
   ├── .gitignore
   ├── requirements.txt
   └── README.md
