Folder Structure

.
├── app/
│   ├── __init__.py
│   ├── main.py              # Entry point: initializes FastAPI and includes routers
│   ├── api/                 # Route handlers and API versioning
│   │   └── v1/
│   │       ├── api.py       # Main router for v1
│   │       └── endpoints/   # Individual resource routes (e.g., users.py, items.py)
│   ├── core/                # Global config (settings, security, constants)
│   ├── crud/                # Create, Read, Update, Delete logic (optional but common)
│   ├── db/                  # Database session management and base setup
│   ├── models/              # Database models (e.g., SQLAlchemy or Tortoise)
│   ├── schemas/             # Pydantic models for request/response validation
│   └── services/            # Complex business logic (separated from routes)
├── tests/                   # Unit and integration tests
├── alembic/                 # Database migrations (if using Alembic)
├── .env                     # Environment variables
├── Dockerfile               # Containerization instructions
└── requirements.txt         # Project dependencies




Packages installation 
pip install -r requirements-dev.txt # Development
pip install -r requirements.txt # Production


Environment Settings
ENV = production or development
DEBUG = True or False
PGSQL_DATABASE_URL = postgresql connection string