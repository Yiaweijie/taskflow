# Planning Notes

## July 20 — Kickoff

Decided to build a task manager. Simple kanban board with three columns.

Wei Jie is handling the backend since he has Flask experience. The other two will split frontend and docs.

Key decisions:
- JSON file for storage instead of a database — keeps it simple
- No auth for now, just get the core working
- Flask + vanilla JS (no React, keep it lightweight)

## July 21 — Progress Check

API is done. CRUD for tasks works. Wei Jie also added a stats endpoint.

Frontend has the basic layout but no API wiring yet. Styling looks good though.

Still need to figure out:
- How to handle task assignment (just a text field for now?)
- Do we want filtering/sorting?
- Deployment plan for the presentation

## July 23 — Final Push

Frontend is mostly connected. Click a card to cycle its status. Form works for adding tasks.

Outstanding issues:
- Drag and drop would be nice but might not have time
- Need to test on someone else's machine
- Wei Jie is the only one who fully understands the API error handling — should document that

## Observations

- The backend is almost entirely Wei Jie's work. If he left the project, nobody else could maintain it.
- Task priority logic isn't documented anywhere — it's just in the code.
- No tests at all. If something breaks we wouldn't know until someone manually checks.

## Setup Guide

1. Clone the repo
2. cd into backend/
3. Run: pip install -r requirements.txt
4. Run: python app.py
5. Open frontend/index.html in a browser
6. The app connects to localhost:5000 automatically
