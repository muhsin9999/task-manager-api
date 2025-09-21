# Task Manager API

A production-ready, cloud-native REST API for managing tasks. Built with FastAPI, PostgreSQL, Docker, and best backend practices.

## 🚀 Features

- User registration & JWT authentication
- CRUD for tasks (create, read, update, delete)
- Task status (pending, completed, priority)
- Filtering, sorting, and pagination
- API docs (OpenAPI/Swagger)
- Dockerized for easy local and cloud deployment
- CI/CD ready (GitHub Actions)
- Unit/integration test support (pytest)
- Clean, modular codebase

## 🛠️ Tech Stack

- FastAPI (Python 3.10+)
- PostgreSQL
- SQLAlchemy
- Pydantic
- Docker & Docker Compose
- GitHub Actions (CI/CD)
- pytest

## ⚡️ Quickstart

### 1. Clone the Repo

```bash
git clone https://github.com/muhsin9999/task-manager-api.git
cd task-manager-api
```

### 2. Setup Environment

- Copy `.env.example` to `.env` and fill in your variables

### 3. Run with Docker Compose

```bash
docker-compose up --build
```

- FastAPI docs at `http://localhost:8000/docs`
- PostgreSQL at `localhost:5432`

### 4. Run Tests

```bash
docker-compose exec app pytest
```

## 🧩 Project Structure

```
task-manager-api/
│
├── app/
│   ├── main.py           # FastAPI app entrypoint
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   ├── database.py       # DB config
│   ├── routers/          # API routers (users, tasks, auth)
│   ├── services/         # Business logic
│   ├── tests/            # Tests
│   └── ...               
├── .env.example
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
├── .gitignore
└── ...
```

## ✨ Contributing

1. Fork this repo and clone your fork.
2. Create a new branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add my feature'`
4. Push to your fork: `git push origin feature/my-feature`
5. Open a pull request!

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👋 Author

- [muhsin9999](https://github.com/muhsin9999)