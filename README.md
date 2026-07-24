# TaskFlow

A simple task management app for small teams. Built as a university group project.

## Team

- **Wei Ji** — Backend API & project setup
- **Person A** — Frontend UI & styling
- **Person B** — Docs, testing & deployment

## Tech Stack

- **Backend:** Python + Flask
- **Frontend:** Vanilla HTML/CSS/JavaScript
- **Storage:** JSON file (no database needed for now)

## Getting Started

### Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

The API runs at `http://localhost:5000`.

### Frontend

Just open `frontend/index.html` in a browser. If the API is running, it connects automatically.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/tasks | List all tasks |
| POST | /api/tasks | Create a task |
| PUT | /api/tasks/:id | Update a task |
| DELETE | /api/tasks/:id | Delete a task |
| GET | /api/stats | Task statistics |

## Project Structure

```
seed-project/
├── backend/
│   ├── app.py           # Flask API
│   ├── tasks.json       # Data storage
│   └── requirements.txt
├── frontend/
│   ├── index.html       # Main page
│   ├── app.js           # Frontend logic
│   └── style.css        # Styles
├── docs/
│   └── notes.md         # Planning notes
└── README.md
```

## TODO

- [x] Set up project structure
- [x] Build REST API
- [x] Create basic frontend
- [ ] Add drag-and-drop for task cards
- [ ] Add user authentication
- [ ] Deploy somewhere (Render? Vercel?)
