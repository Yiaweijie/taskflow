"""
TaskFlow - Simple Task Manager API
Built with Flask for our university group project.
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import json
import os

app = Flask(__name__)
CORS(app)  # Allow frontend to connect from different port

# Simple file-based storage (no database needed)
DATA_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


def load_tasks():
    """Load tasks from JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    """Get all tasks, optionally filtered by status or assignee."""
    tasks = load_tasks()
    status = request.args.get("status")
    assignee = request.args.get("assignee")

    if status:
        tasks = [t for t in tasks if t["status"] == status]
    if assignee:
        tasks = [t for t in tasks if t["assignee"] == assignee]

    return jsonify(tasks)


@app.route("/api/tasks", methods=["POST"])
def create_task():
    """Create a new task."""
    data = request.get_json()
    tasks = load_tasks()

    # Fix: use max ID instead of length to avoid collisions after deletions
    next_id = max((t["id"] for t in tasks), default=0) + 1
    new_task = {
        "id": next_id,
        "title": data["title"],
        "description": data.get("description", ""),
        "status": "todo",
        "priority": data.get("priority", "medium"),
        "assignee": data.get("assignee", None),
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
    }

    tasks.append(new_task)
    save_tasks(tasks)
    return jsonify(new_task), 201


@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    """Update an existing task."""
    data = request.get_json()
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = data.get("title", task["title"])
            task["description"] = data.get("description", task["description"])
            task["status"] = data.get("status", task["status"])
            task["priority"] = data.get("priority", task["priority"])
            task["assignee"] = data.get("assignee", task["assignee"])
            task["updated_at"] = datetime.now().isoformat()
            save_tasks(tasks)
            return jsonify(task)

    return jsonify({"error": "Task not found"}), 404


@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """Delete a task."""
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    return jsonify({"message": "Task deleted"}), 200


@app.route("/api/stats", methods=["GET"])
def get_stats():
    """Get task statistics."""
    tasks = load_tasks()
    return jsonify({
        "total": len(tasks),
        "todo": len([t for t in tasks if t["status"] == "todo"]),
        "in_progress": len([t for t in tasks if t["status"] == "in_progress"]),
        "done": len([t for t in tasks if t["status"] == "done"]),
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
