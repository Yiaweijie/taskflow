# Team Tasks

Pull the repo, do your tasks below, commit each change separately, then push.

---

## Stewart — Frontend

Make these changes one at a time. Commit after each one.

### Commit 1: Update background color
- Open `frontend/style.css`
- Find `background: #f5f5f5;` (in the `body` rule)
- Change it to `background: #eef2f7;`
- Commit message: `Update background color to softer blue`

### Commit 2: Add delete button to task cards
- Open `frontend/app.js`
- Find the `createTaskCard` function
- In the `card.innerHTML` template, add a delete button after the assignee div:
```html
<button class="delete-btn" onclick="deleteTask(${task.id})">×</button>
```
- Add this function anywhere in the file:
```js
async function deleteTask(taskId) {
    await fetch(`${API_URL}/tasks/${taskId}`, { method: "DELETE" });
    loadTasks();
}
```
- Commit message: `Add delete button to task cards`

### Commit 3: Add task count to header
- Open `frontend/index.html`
- Find the `<p>Simple task management for teams</p>` line in the header
- Add below it: `<span id="task-count"></span>`
- Open `frontend/app.js`, at the end of the `renderTasks` function add:
```js
document.getElementById("task-count").textContent = `${tasks.length} tasks total`;
```
- Commit message: `Add task count display to header`

### Commit 4: Improve card hover style
- Open `frontend/style.css`
- Find the `.task-card:hover` rule
- Change it to:
```css
.task-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    background: #ffffff;
}
```
- Commit message: `Improve card hover animation`

---

## Jerrold — Docs

Make these changes one at a time. Commit after each one.

### Commit 1: Add setup instructions to notes
- Open `docs/notes.md`
- Add this at the bottom:
```
## Setup Guide

1. Clone the repo
2. cd into backend/
3. Run: pip install -r requirements.txt
4. Run: python app.py
5. Open frontend/index.html in a browser
6. The app connects to localhost:5000 automatically
```
- Commit message: `Add setup instructions to notes`

### Commit 2: Create API reference
- Create a new file `docs/api-reference.md` with this content:
```
# API Reference

Base URL: http://localhost:5000/api

## GET /tasks
Returns all tasks. Optional query params: status, assignee

## POST /tasks
Create a task. Body: { "title": "...", "description": "...", "priority": "low|medium|high" }

## PUT /tasks/:id
Update a task. Body: any fields to change (title, description, status, priority, assignee)

## DELETE /tasks/:id
Delete a task by ID.

## GET /stats
Returns task counts by status: { total, todo, in_progress, done }

## GET /tasks/search?q=keyword
Search tasks by keyword in title or description.
```
- Commit message: `Add API reference doc`

### Commit 3: Update team members in README
- Open `README.md`
- Find the Team section and update it to:
```
## Team

- **Wei Ji** — Backend API & project setup
- **Stewart** — Frontend UI & styling
- **Jerrold** — Docs, testing & deployment
```
- Commit message: `Update team members in README`

### Commit 4: Add meeting notes
- Create a new file `docs/meeting-notes.md` with this content:
```
# Meeting Notes

## July 23 — Final sync before deadline

Attendees: Wei Ji, Stewart, Jerrold

### Decisions
- Keep JSON file storage, no database
- No drag-and-drop, just click to cycle status
- Stewart will finish the delete button today
- Jerrold to document all API endpoints

### Action items
- [ ] Stewart: fix task list refresh after delete
- [ ] Jerrold: finish API reference
- [ ] Wei Ji: add any missing error handling
- [x] Wei Ji: fix CORS issue
```
- Commit message: `Add meeting notes from July 23`

---

## After you're done

Push your commits. That's it!
