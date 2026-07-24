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
