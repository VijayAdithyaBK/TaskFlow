# TaskFlow API

A simple, robust, and efficient Task Manager API built with FastAPI and SQLAlchemy. This project provides a solid foundation for managing tasks with a local SQLite database, featuring full CRUD capabilities and a clean architecture.

## Key Features

- **Task Management**: Create and retrieve tasks with ease.
- **Persistent Storage**: Utilizes SQLite for local data persistence.
- **Automated Documentation**: Interactive API docs via Swagger (FastAPI).
- **Clean Architecture**: Separated routes, models, schemas, and database configuration.

## Tech Stack

- **Framework**: FastAPI
- **Language**: Python 3.x
- **ORM**: SQLAlchemy
- **Database**: SQLite
- **Validation**: Pydantic
- **Server**: Uvicorn

## Prerequisites

- **Python**: 3.8+ recommended
- **pip**: Python package installer

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/taskflow.git
cd taskflow
```

### 2. Set Up Virtual Environment (Recommended)

```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
uvicorn app:app --reload
```

The server will start at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Architecture Overview

### Directory Structure

```
taskflow/
├── routes/
│   └── task_router.py   # Task-specific route handlers
├── app.py               # App entry point & router initialization
├── models.py            # SQLAlchemy database models
├── schemas.py           # Pydantic data validation schemas
├── db.py                # Database connection & session setup
├── requirements.txt     # Project dependencies
└── .tasks.db            # SQLite database (auto-generated)
```

### Request Flow

1. **Client** makes a request to an endpoint.
2. **FastAPI** routes the request to the appropriate handler in `routes/task_router.py`.
3. **Pydantic** validates the request body using `schemas.py`.
4. **SQLAlchemy** interacts with the **SQLite** database using `models.py`.
5. **FastAPI** returns the JSON response to the client.

## API Endpoints

### Root
- **GET** `/` - Returns a welcome message.

### Tasks
- **GET** `/tasks/` - Retrieves all tasks.
- **POST** `/tasks/` - Creates a new task.
  - **Body**: `{ "title": "string", "description": "string", "completed": boolean }`

### Documentation
- **Interactive Docs (Swagger UI)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative Docs (ReDoc)**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Available Scripts

| Command | Description |
|---------|-------------|
| `uvicorn app:app --reload` | Starts the development server with auto-reload. |
| `pip install -r requirements.txt` | Installs all required packages. |

## Deployment

This project is configured for deployment using **Gunicorn** with **Uvicorn** workers, as specified in the `Procfile`.

### Production Command
```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app
```

## Troubleshooting

### Database Issues
- **Error**: `sqlite3.OperationalError: no such table: tasks`
- **Solution**: The application is configured to create tables on startup. Ensure `app.py` is executed correctly. If the `.tasks.db` file is corrupted, you can safely delete it and restart the server.

### Server Not Starting
- **Solution**: Ensure no other process is using port 8000. You can specify a different port using `--port XXXX`.
