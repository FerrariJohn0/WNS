# Task Tracker API

A full-stack Task Management Application built using FastAPI, Streamlit, PostgreSQL, and SQLAlchemy.

---

## Features

- Create Tasks
- View Tasks
- Update Tasks
- Delete Tasks
- Async FastAPI APIs
- PostgreSQL Database Integration
- SQLAlchemy ORM
- Streamlit Frontend UI
- Swagger API Documentation
- Environment Variable Configuration
- Error Handling and Validation

---

## Tech Stack

### Backend

- FastAPI
- Uvicorn
- SQLAlchemy
- PostgreSQL
- AsyncPG
- Pydantic

### Frontend

- Streamlit
- Pandas
- Requests

---

## Project Architecture

```text
Streamlit Frontend
        ↓
FastAPI Backend APIs
        ↓
SQLAlchemy ORM
        ↓
PostgreSQL Database
```

---

## Project Structure

```text
task_tracker_API/
│
├── backend/
│   ├── app/
│   │   ├── core/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── .env
│   ├── requirements.txt
│   └── venv/
│
├── frontend/
│   └── streamlit_app.py
│
└── README.md
```

---

## Database Schema

### Tasks Table

| Column      | Type     |
| ----------- | -------- |
| id          | Integer  |
| title       | String   |
| description | Text     |
| status      | String   |
| priority    | String   |
| due_date    | Date     |
| created_at  | DateTime |
| updated_at  | DateTime |

---

## API Endpoints

| Method | Endpoint    | Description    |
| ------ | ----------- | -------------- |
| POST   | /tasks/     | Create Task    |
| GET    | /tasks/     | Get All Tasks  |
| GET    | /tasks/{id} | Get Task By ID |
| PUT    | /tasks/{id} | Update Task    |
| DELETE | /tasks/{id} | Delete Task    |

---

## Swagger API Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

---

## Installation and Setup

### 1. Clone Repository

```bash
git clone <repository_url>
```

---

### 2. Navigate to Backend

```bash
cd backend
```

---

### 3. Create Virtual Environment

```bash
python -m venv venv
```

---

### 4. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

---

### 5. Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy asyncpg psycopg2-binary pydantic python-dotenv greenlet
```

---

### 6. Configure Environment Variables

Create `.env` file inside backend folder.

```env
DATABASE_URL=postgresql+asyncpg://username:password@localhost/task_tracker_db
```

---

### 7. Run FastAPI Backend

```bash
uvicorn app.main:app --reload
```

---

### 8. Run Streamlit Frontend

Open another terminal:

```bash
cd frontend
```

Run:

```bash
streamlit run streamlit_app.py
```

---

## Streamlit Features

- Hidden database IDs
- Serial number display
- Dropdown-based task selection
- Dynamic task updates
- Responsive task table

---

## Future Enhancements

- JWT Authentication
- User Login System
- Search and Filters
- Task Categories
- Dashboard Analytics
- Docker Deployment
- CI/CD Pipeline

---

## Author

FerrariJohn0
